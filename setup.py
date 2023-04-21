from setuptools import setup, find_packages

setup(
    name='inrightplace',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'django>=4.2',
        'django-bootstrap5>=23.1',
        'psycopg2>=2.9.6',
        'python-dotenv>=1.0.0',
        'mod_wsgi>=4.9.4'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
    ]
)
