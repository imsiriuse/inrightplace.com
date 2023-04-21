DEPLOYMENT
git clone git@github.com:imsiriuse/inrightplace.com.git
python setup.py sdist
pip install dist/inrightplace-*.tar.gz

$env:PYTHONPATH = "inrightplace"
$env:DJANGO_SETTINGS_MODULE = "inrightplace.settings"
$env:MOD_WSGI_APACHE_ROOTDIR= "C:\xampp\apache"
$env:VCINSTALLDIR= "C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC"

