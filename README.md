# Drawer

**Drawer** is a modern, full-stack SaaS platform designed specifically for content creators. Built for speed, security, and aesthetics, it provides a seamless experience for creators to securely upload, manage, and store their high-quality photos and videos directly from their personalized dashboard.

This repository serves as a fully functional proof-of-concept for a Content Management SaaS platform. 

## 🚀 Key Features

- **Dynamic Content Gallery**: A premium, responsive grid dashboard capable of hosting native HTML5 video previews and high-res image galleries.
- **Smart Upload Parsing**: Automatically tags and categorizes uploaded media files based on content type.
- **Modern Glassmorphic UI**: Beautifully styled utilizing Tailwind CSS with deep, immersive background gradients, drop-blurs, and interactive micro-animations.
- **Robust Authentication**: Powered by Django Allauth for secure email/password and social login flows.
- **Tiered Subscriptions**: Pre-configured dynamic pricing models ready to be hooked into Stripe (Pro, Starter, Annual plans).
- **Cloud-Ready Infrastructure**: Designed to seamlessly transition from local SQLite/storage to Neon Postgres DB and AWS S3 storage for production deployment via Docker/Railway.

---

## 📸 Screenshots

<img width="1891" height="981" alt="Screenshot 1" src="https://github.com/user-attachments/assets/065e3c14-af43-470e-aff3-593bc58a6daf" />
<img width="1911" height="988" alt="Screenshot 2" src="https://github.com/user-attachments/assets/5ae54da0-80bd-4b84-b649-04ff4ba58e5d" />
<img width="1909" height="981" alt="Screenshot 3" src="https://github.com/user-attachments/assets/7197e314-b4d3-4186-8fd9-9cc8d0866c3f" />
<img width="1919" height="994" alt="Screenshot 4" src="https://github.com/user-attachments/assets/8ca945a3-8805-4f58-be12-bedca143f792" />
<img width="1889" height="997" alt="Screenshot 5" src="https://github.com/user-attachments/assets/143427dc-aca5-4bd8-ae65-61c135351ea3" />

## 🛠 Tech Stack

- **Backend**: Django 5 & Python 3.13
- **Frontend**: HTML5, Tailwind CSS
- **Authentication**: Django Allauth
- **Payments**: Stripe integration architecture for subscription flows
- **Database**: SQLite for local development (production-ready for Neon Postgres)
- **Deployment**: Configured for Docker and Railway

---

## 💻 Local Development Setup

### 1. Prerequisites
- Git
- Python 3.11+
- `pip`
- Node.js & `npm` (optional, for frontend UI building)

### 2. Clone the repository
```bash
git clone https://github.com/SAHIL15KP/content-storage.git
cd content-storage
```

### 3. Virtual Environment setup

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows PowerShell:**
```powershell
py -m venv venv
.\venv\Scripts\Activate.ps1
```

### 4. Install Dependencies
```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install -r requirements.dev.txt
```
*(The `requirements.dev.txt` installs `rav`, a lightweight task runner used in this project.)*

### 5. Install Frontend Dependencies (Optional)
Required only if you plan to rebuild or watch Tailwind assets.
```bash
npm install
```

### 6. Environment Variables configuration

**macOS/Linux:**
```bash
cp .env.sample .env
```

**Windows PowerShell:**
```powershell
Copy-Item .env.sample .env
```

**Generate a Django Secret Key:**
Run this command and paste the output as `DJANGO_SECRET_KEY` in your `.env` file:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Make sure at minimum you have set:
- `DJANGO_DEBUG=1`
- `DJANGO_SECRET_KEY="<your-generated-key>"`

*(Leave `DATABASE_URL` empty to use local SQLite. Only add Stripe/Email variables for testing those flows).*

### 7. Fetch Static Assets
Vendor assets need to be pulled down once for the UI:
```bash
cd src
python manage.py vendor_pull
```

### 8. Database Migrations
```bash
python manage.py migrate
```

### 9. Create an Admin User
```bash
python manage.py createsuperuser
```

### 10. Start the Development Server
```bash
python manage.py runserver
```
Open the app at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

---

## 🎨 Optional Frontend Commands
Run these from the **project root** (not the `src` directory):

Watch for Tailwind CSS changes:
```bash
npm run watch
```

Build the production CSS bundle:
```bash
npm run build
```

## ⚙️ Optional `rav` Task Runner
If you enjoy using a task runner, use these handy shortcuts:
- `rav run install`
- `rav run install_dev`
- `rav run migrate`
- `rav run dev`
- `rav run test`
- `rav run vendors_pull`
- `rav run collectstatic`

*(Note for Windows users: By default, `rav.yaml` relies on `venv/bin/...` paths. Using the direct Python `manage.py` commands is recommended unless paths are updated.)*

## 🐳 Docker Deployment
A `Dockerfile` is included and ready for deployment. Simply provide a valid `.env` file containing everything needed before building and spinning up the container.
