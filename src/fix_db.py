import os
import django
from django.db import connection

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cfehome.settings')
django.setup()

def fix_db():
    with connection.cursor() as cursor:
        # Check if the join table exists
        cursor.execute("SELECT 1 FROM information_schema.tables WHERE table_name = 'socialaccount_socialapp_sites';")
        exists = cursor.fetchone()
        
        if not exists:
            print("--- SURGICAL FIX: Creating missing socialaccount_socialapp_sites table ---")
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS socialaccount_socialapp_sites (
                    id SERIAL PRIMARY KEY,
                    socialapp_id INTEGER NOT NULL REFERENCES socialaccount_socialapp(id) DEFERRABLE INITIALLY DEFERRED,
                    site_id INTEGER NOT NULL REFERENCES django_site(id) DEFERRABLE INITIALLY DEFERRED,
                    UNIQUE (socialapp_id, site_id)
                );
                CREATE INDEX IF NOT EXISTS socialaccount_socialapp_sites_socialapp_id_idx ON socialaccount_socialapp_sites (socialapp_id);
                CREATE INDEX IF NOT EXISTS socialaccount_socialapp_sites_site_id_idx ON socialaccount_socialapp_sites (site_id);
            """)
            print("--- Table created successfully ---")
        else:
            print("--- Table socialaccount_socialapp_sites already exists, skipping creation ---")

if __name__ == "__main__":
    try:
        fix_db()
    except Exception as e:
        print(f"--- Warning: DB fix encountered an error: {e} ---")
