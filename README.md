# Cybersecurity Portfolio

A modern, responsive cybersecurity portfolio built with Django. Showcase your skills, projects, certifications, and experience in a professional manner.

## Features

- Modern, responsive design
- Mobile-friendly interface
- Django admin panel for easy content management
- Skills visualization with proficiency levels
- Project showcase with detailed descriptions
- Certifications and achievements display
- Contact form integration
- Easy deployment to cloud platforms

## Tech Stack

- **Backend:** Django 4.2
- **Frontend:** HTML5, CSS3, JavaScript
- **Database:** SQLite (development) / PostgreSQL (production ready)
- **Server:** Gunicorn
- **Static Files:** WhiteNoise

## Quick Start

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/cybersec-portfolio.git
cd cybersec-portfolio
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run migrations**
```bash
python manage.py migrate
```

5. **Populate sample data**
```bash
python populate_data.py
```

6. **Create superuser** (optional - already created by populate script)
```bash
python manage.py create_default_superuser
```
Default credentials: `admin` / `admin`

7. **Run development server**
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to view your portfolio!

## Customization

### Update Portfolio Content

1. **Via Admin Panel (Recommended)**
   - Navigate to `http://127.0.0.1:8000/admin`
   - Login with admin credentials
   - Edit Profile, Projects, Skills, Experience, etc.

2. **Via populate_data.py**
   - Edit the `populate_data.py` file
   - Run `python populate_data.py` to update

### Modify Settings

Edit `portfolio_project/settings.py` for:
- Database configuration
- Static files settings
- Security settings
- Email configuration

## Deployment

### Deploy to Render

1. **Push to GitHub**
```bash
git add .
git commit -m "Initial commit"
git push origin main
```

2. **Create Render Account**
   - Go to [render.com](https://render.com)
   - Sign up with GitHub

3. **Create Web Service**
   - Click "New +" → "Web Service"
   - Connect your repository
   - Configure:
     - **Build Command:** `pip install -r requirements.txt && python manage.py migrate && python populate_data.py && python manage.py create_default_superuser && python manage.py collectstatic --noinput`
     - **Start Command:** `gunicorn portfolio_project.wsgi:application`
     - **Environment Variables:**
       - `PYTHON_VERSION`: `3.10.12`
       - `SECRET_KEY`: (generate a new one)
       - `DEBUG`: `False`

4. **Deploy!**

### Deploy to Other Platforms

- **Heroku:** Procfile included
- **Railway:** Auto-detection enabled
- **AWS/GCP/Azure:** Configure with gunicorn

## Project Structure

```
cybersec-portfolio/
├── portfolio/                 # Main app
│   ├── models.py             # Database models
│   ├── views.py              # View logic
│   ├── urls.py               # URL routing
│   ├── admin.py              # Admin configuration
│   └── management/           # Custom commands
├── portfolio_project/        # Project settings
│   ├── settings.py          # Django settings
│   ├── urls.py              # Root URL config
│   └── wsgi.py              # WSGI config
├── templates/               # HTML templates
├── static/                  # Static files (CSS, JS, images)
├── media/                   # User uploads
├── populate_data.py         # Sample data script
├── requirements.txt         # Python dependencies
├── Procfile                 # Heroku deployment
├── runtime.txt             # Python version
└── manage.py               # Django management script
```

## Database Models

- **Profile:** Personal information, contact details, bio
- **Education:** Academic background
- **Certification:** Professional certifications
- **Experience:** Work history
- **Project:** Portfolio projects
- **Skill:** Technical skills with proficiency levels

## Security Notes

**Important for Production:**

1. Change `SECRET_KEY` in settings.py
2. Set `DEBUG = False`
3. Update `ALLOWED_HOSTS`
4. Change default admin credentials
5. Use environment variables for sensitive data
6. Enable HTTPS
7. Configure CSRF and CORS properly

## Customization Guide

### Add New Sections

1. Create model in `portfolio/models.py`
2. Register in `portfolio/admin.py`
3. Create migrations: `python manage.py makemigrations`
4. Apply migrations: `python manage.py migrate`
5. Update templates in `templates/`

### Styling

- Edit `static/css/style.css` for custom styles
- Modify templates in `templates/` for layout changes
- Add JavaScript in `static/js/`

## Troubleshooting

**Database not found:**
```bash
python manage.py migrate
```

**Static files not loading:**
```bash
python manage.py collectstatic
```

**Admin not accessible:**
```bash
python manage.py create_default_superuser
```

## Contributing

Feel free to fork this project and customize it for your needs. Pull requests are welcome!

## License

MIT License - feel free to use this project for your portfolio.

## Support

For issues and questions:
- Open an issue on GitHub
- Check existing issues for solutions

## Changelog

### v1.0.0
- Initial release
- Basic portfolio functionality
- Admin panel integration
- Responsive design
- Deployment ready

---

Built for cybersecurity professionals
