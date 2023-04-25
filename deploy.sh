#load virtualenv
source .venv/bin/activate
pip install uwsgi

#load static files
mkdir static
mkdir media
python manage.py collectstatic

#create folder for socket
mkdir /run/inrightplace
chown $USER:$USER /run/inrightplace

#load nginx config
/etc/init.d/nginx stop
cp run/inrightplace.conf /etc/nginx/sites-available
ln -s /etc/nginx/sites-available/inrightplace.conf /etc/nginx/sites-enabled
uwsgi --ini run/uwsgi.ini
/etc/init.d/nginx start
