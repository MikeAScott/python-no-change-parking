No Change Parking Application
=============================
Python flask builder implementation of No Change Parking

Prerequisites
-------------
* Python 3 

Install it
----------
``` bash
git clone https://mikeascott/python-no-change-parking.git no-change-parking
cd no-change-parking
# Create python virtual env
virtualenv venv
source venv/bin/activate
# Install required libraries into the virtual env
pip install -r requirements.txt
```
Run it
------
``` bash
export FLASK_APP=app
# Create an admin user
flask fab create-admin
# Run dev server
flask run
```

Use it
------
```bash
# Mac OSX
open http://localhost:5000
# Linux Gnome
xdg-open http://localhost:5000
```

Package it
----------
``` bash
python setup.py bdist_wheel
```

Deploy it properly
------------------
Beyond the scope of this for now

Will be putting an packager in soon
