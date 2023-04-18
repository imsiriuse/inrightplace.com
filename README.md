DEPLOYMENT
git clone git@github.com:imsiriuse/inrightplace.com.git

START SERVER
python -m manage makemigrations
python -m manage migrate
python -m manage runserver 0.0.0.0:8000
