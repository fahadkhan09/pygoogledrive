PyGoogle Drive
--------------

*PyGoogleDrive* is a wrapper library of
`google-api-python-client <https://github.com/google/google-api-python-client>`_
that simplifies many common Google Drive API tasks You can just need to create credentials.json and place in your root directory.

Project Info
------------

- Homepage: `https://pypi.python.org/pypi/PyGoogleDrive <https://pypi.python.org/pypi/PyGoogleDrive>`_
- GitHub: `https://github.com/fahadkhan09/pygoogledrive <https://github.com/fahadkhan09/PyGoogleDrive>`_

Features of PyGoogleDrive
-------------------------
-  You can just need to create credentials.json and place in your root directory
-  Simplifies OAuth2.0 into just few lines with flexible settings.
-  Wraps `Google Drive API <https://developers.google.com/drive/>`_ into
   classes of each resource to make your program more object-oriented.
-  Helps common operations else than API calls, such as content fetching
   and pagination control.

How to install
--------------

You can install PyGoogleDrive with regular ``pip`` command.

::

     pip install PyGoogleDrive


How to get credentials.json
---------------------------

 - For credentials.json just visit https://console.developers.google.com/
    1. Create project
    2. Select credentials
    3. Add OAuth 2.0 Client IDs by clicking CREATE CREDENTIALS button
    4. select web application
    5. For Authorized JavaScript origins add  http://localhost without '/' in end
    6. For Authorized redirect URIs add http://localhost/
    7. Download file and rename it to credentials.json
    8. Add this file to project directory

OAuth made easy
---------------

When you create instance it will automatically open url for google authentication
After successfully authentication token.pickle file is created in root directory



.. code:: python


    from PyGoogleDrive.PyGoogleDrive import PyGoogleDrive

    drive = PyGoogleDrive()


Folder management
-------------------------

We can use ```drive```  instance to create Folder

.. code:: python

    drive.createfolder('folder_name')


createfolder function will return folder id that is created on Google drive


File management
---------------------------------

*PyGoogleDrive* handles custom  file upload.

.. code:: python

    drive.uploadfile(name, file_path, mimetype, folder_name)

uploadfile function will return file id created on google drive folder_name is optionals
if you want to upload file in specific  folder then add folder_name = 'document'

