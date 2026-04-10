# Content Storage Platform

**Content Storage** is a modern, full-stack SaaS platform designed specifically for content creators. Built for speed, security, and aesthetics, it provides a seamless experience for creators to securely upload, manage, and store their high-quality photos and videos directly from their personalized dashboard.

This repository serves as a fully functional proof-of-concept for a Content Management SaaS platform. 

### Key Features
- **Dynamic Content Gallery**: A premium, responsive grid dashboard capable of hosting native HTML5 video previews and high-res image galleries.
- **Smart Upload Parsing**: Automatically tags and categorizes uploaded media files based on content type.
- **Modern Glassmorphic UI**: Beautifully styled utilizing Tailwind CSS with deep, immersive background gradients, drop-blurs, and interactive micro-animations.
- **Robust Authentication**: Powered by Django Allauth for secure email/password and social login flows.
- **Tiered Subscriptions**: Pre-configured dynamic pricing models ready to be hooked into Stripe (Pro, Starter, Annual plans).
- **Cloud-Ready Infrastructure**: Designed to seamlessly transition from local SQLite/storage to Neon Postgres DB and AWS S3 storage for production deployment via Docker/Railway.

---

## What is inside

- Django 5 & Python 3.13
- Tailwind CSS
- Django Allauth for authentication
- Stripe integration architecture for subscription flows
- SQLite for local development (ready for Neon Postgres)

## What you need before you start

- Git
- Python 3.11 or newer
- `pip`
- Node.js and `npm` if you want to rebuild frontend assets locally

## Clone the project

```bash
git clone https://github.com/SAHIL15KP/content-storage.git
cd content-storage
```

## Create a virtual environment

### macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows PowerShell

```powershell
py -m venv venv
.\venv\Scripts\Activate.ps1
```

## Install Python dependencies

I recommend installing both the main and development requirements so you have the same tools I use locally.

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install -r requirements.dev.txt
```

`requirements.dev.txt` currently installs `rav`, which is a small task runner used in this repo.

## Install frontend dependencies

This step is only needed if you plan to rebuild or watch Tailwind assets. The app can still run locally without it because the repo already includes built static files.

```bash
npm install
```

## Create your local environment file

### macOS/Linux

```bash
cp .env.sample .env
```

### Windows PowerShell

```powershell
Copy-Item .env.sample .env
```

At minimum, make sure these values are set in `.env`:

- `DJANGO_DEBUG=1`
- `DJANGO_SECRET_KEY="<your-secret-key>"`

Useful notes:

- Leave `DATABASE_URL` empty if you want to use the default local SQLite database.
- Add the email settings only if you want to test email delivery and account verification flows.
- Add `STRIPE_SECRET_KEY` only if you want to test billing or checkout features.

## Generate a Django secret key

Run this once, then paste the output into `DJANGO_SECRET_KEY` inside `.env`:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

## Download vendor static files

The UI uses a few vendor assets that should be pulled once before local development:

```bash
cd src
python manage.py vendor_pull
```

## Run migrations

Still inside `src`, run:

```bash
python manage.py migrate
```

If you did not set `DATABASE_URL`, Django will create and use a local SQLite database automatically.

## Create an admin user

```bash
python manage.py createsuperuser
```

## Start the development server

```bash
python manage.py runserver
```

Open the app at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Optional frontend commands

Run these from the project root, not from `src`.

If you installed Node dependencies and want to work on styles locally:

```bash
npm run watch
```

To build the production CSS bundle:

```bash
npm run build
```

## Optional `rav` commands

If you like using the task runner, these are the main commands available:

- `rav run install`
- `rav run install_dev`
- `rav run migrate`
- `rav run dev`
- `rav run test`
- `rav run vendors_pull`
- `rav run collectstatic`

Important note for Windows users: the current `rav.yaml` uses `venv/bin/...` paths, so the direct `python manage.py ...` commands in this README are the safest option unless you update those paths for Windows.

## Local development notes

- You do not need Postgres just to get started locally. SQLite works out of the box.
- You do not need Stripe credentials unless you are actively testing checkout or subscription flows.
- You do not need SMTP credentials unless you want to test email sending end to end.
- This setup guide does not force any cloud storage or upload service. If you want to add your own image or video upload flow later, you can do that on top of the normal local Django setup.

## Troubleshooting

- If `python manage.py vendor_pull` fails, check your internet connection and try again.
- If signup or email verification is not working, make sure your email settings in `.env` are valid.
- If billing pages fail, confirm that `STRIPE_SECRET_KEY` is set correctly.
- If `rav` commands do not work on Windows, use the direct commands from this README instead.

## Docker

If you prefer to run the project with Docker, the repo already includes a `Dockerfile`. You will still need a valid `.env` file before building and running the container.
