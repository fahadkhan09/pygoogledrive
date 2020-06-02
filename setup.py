from setuptools import setup

setup(
    name='PyGoogleDrive',
    version='1.0.1',
    description='Google Drive API made easy with PyGoogleDrive',
    long_description=open('README.rst').read(),
    packages=['PyGoogleDrive'],
    author='Fahad Khan',
    author_email='fahadkhan6302@gmail.com',
    keywords=['python', 'google drive', 'api', 'PyGoogleDrive'],
    url='https://github.com/fahadkhan09/pygoogledrive',
    license="GPLv3+",
    install_requires=[
        "google-api-python-client >= 1.2",
        "oauth2client >= 4.0.0",
        "PyYAML >= 3.0",
        "google-auth-oauthlib",
    ],

)