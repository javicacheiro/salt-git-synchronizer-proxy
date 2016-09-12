Installation
------------

The proxy service must be accessible from gitlab so, in general,
it should be located in a server with a public address.

It is recommended to run the proxy service under a non-privileged account.

```
su - gitsync
git clone https://github.com/javicacheiro/salt-git-synchronizer-proxy
# IMPORTANT: Rename the repo to salt-proxy to avoid later issues with
# gunicorn not finding flask module
mv salt-git-synchronizer-proxy salt-proxy
cd salt-proyx
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
pip install gunicorn
```

Running the service
-------------------

It is recommended to run the proxy service under a non-privileged account.

```
su - gitsync
cd salt-proxy
. venv/bin/activate
FLASK_CONFIG=production gunicorn --workers=2 --bind=localhost:5000 wsgi:application
```

Issues
------
### ImportError: No module named flask
gunicorn is unable to import flask and returns:

    ImportError: No module named flask

Solution: Rename the salt-git-synchronizer-proxy directory to salt-proxy
or any other short name.

Usage
-----

Add the following webhooks to gitlab:

```
# salt-state repo
https://<ADDRESS>/gitlab/v1/salt-state/events/push 
# salt-pillar repo
https://<ADDRESS>/gitlab/v1/salt-pillar/events/push 
```

Configure the appropriate Secret Token in config/production.py and in
the webhook configuration.
