"""
Management command to fix the socialaccount migration state mismatch.

When socialaccount is re-enabled after being temporarily disabled, Django's
migration state can fall out of sync with the actual database schema. This
command marks socialaccount migrations 0001-0006 as applied (faked) in the
django_migrations table without executing them, preventing DuplicateColumn
errors caused by columns that already exist in the database.
"""

from typing import Any

from django.core.management.base import BaseCommand
from django.db import connection


SOCIALACCOUNT_MIGRATIONS = [
    ("allauth.socialaccount", "0001_initial"),
    ("allauth.socialaccount", "0002_token_max_lengths"),
    ("allauth.socialaccount", "0003_extra_data_default_dict"),
    ("allauth.socialaccount", "0004_app_provider_id_settings"),
    ("allauth.socialaccount", "0005_socialtoken_nullable_app"),
    ("allauth.socialaccount", "0006_alter_socialaccount_extra_data"),
]


class Command(BaseCommand):
    help = (
        "Fake-apply socialaccount migrations 0001-0006 to fix migration state "
        "mismatch when the column already exists in the database."
    )

    def handle(self, *args: Any, **options: Any) -> None:
        self.stdout.write("Checking socialaccount migration state...")

        with connection.cursor() as cursor:
            # Ensure the django_migrations table exists before querying it
            cursor.execute(
                """
                SELECT EXISTS (
                    SELECT FROM information_schema.tables
                    WHERE table_name = 'django_migrations'
                )
                """
            )
            table_exists = cursor.fetchone()[0]

            if not table_exists:
                self.stdout.write(
                    self.style.WARNING(
                        "django_migrations table does not exist yet — skipping."
                    )
                )
                return

            faked = 0
            for app, name in SOCIALACCOUNT_MIGRATIONS:
                cursor.execute(
                    "SELECT COUNT(*) FROM django_migrations WHERE app = %s AND name = %s",
                    [app, name],
                )
                already_recorded = cursor.fetchone()[0]

                if already_recorded:
                    self.stdout.write(f"  Already recorded: {app} {name}")
                else:
                    cursor.execute(
                        "INSERT INTO django_migrations (app, name, applied) "
                        "VALUES (%s, %s, NOW())",
                        [app, name],
                    )
                    self.stdout.write(
                        self.style.SUCCESS(f"  Faked: {app} {name}")
                    )
                    faked += 1

        if faked:
            self.stdout.write(
                self.style.SUCCESS(
                    f"Done — marked {faked} socialaccount migration(s) as applied."
                )
            )
        else:
            self.stdout.write("Done — no changes needed.")
