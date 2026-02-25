# Setup Guide

### Clone
```bash
git clone https://github.com/yanicells/commongrounds-21.git
cd commongrounds-21
```

### Switching branch
```bash
git checkout feat/<appname>
```

### Using venv
```bash
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
.\venv\Scripts\activate  # Windows
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Set up environment variables
Create a `.env` file:
```
SECRET_KEY='your-secret-key-here'
STATIC_ROOT='staticfiles/'
DEBUG=True
```

### Run migrations
```bash
python3 manage.py migrate
```

### Create a superuser (for admin)
```bash
python3 manage.py createsuperuser
```

---

## App-level Notes

### Create branch and app
```bash
git checkout -b feat/<appname>
python manage.py startapp <appname>
```

### Register the app
Add `<appname>` to `INSTALLED_APPS` in `settings.py`:
```python
INSTALLED_APPS = [
    ...
    '<appname>',
]
```

### Create templates
App templates go inside:
```
<appname>/templates/<appname>/
```
All templates should extend the base:
```html
{% extends 'base.html' %}
{% load static %}

{% block title %}Page Title{% endblock %}

{% block content %}
  <!-- your content here -->
{% endblock %}
```

### Setup URLs
Create `<appname>/urls.py` and add your routes there. Then include it in `commongrounds/urls.py`:
```python
path('<appname>/', include('<appname>.urls', namespace='<appname>')),
```

### Commit and push
```bash
git add .
git commit -m "feat: commit message here"
git push origin feat/<appname>
```
