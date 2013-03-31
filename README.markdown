
==========
Bugtracker
==========

Bugtracker is a simple Django 1.5 admin-based app for tracking bugs.

Features
--------

* Manage tickets using Django admin.

Quick start
-----------

1. Add "bugtracker" to your INSTALLED_APPS setting like this::

      INSTALLED_APPS = (
          ...
          'bugtracker',
      )

2. Run `python manage.py syncdb` to create the bugtracker models.

3. Start the development server and visit 
   http://127.0.0.1:8000/admin/bugtracker/ticket/ to add tickets. 

Dependencies
------------

* [Django 1.5.1](https://pypi.python.org/pypi/Django/1.5.1)
