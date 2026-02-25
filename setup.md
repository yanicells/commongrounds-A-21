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
