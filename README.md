Installation
------------

The proxy service must be accessible from gitlab so, in general,
it should be located in a server with a public address.

It is recommended to run the proxy service under a non-privileged account.

```
su - gitsync
git clone https://github.com/javicacheiro/salt-git-synchronizer-proxy
cd salt-git-synchronizer-proxy
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
cd salt-git-synchronizer-proxy
. venv/bin/activate
FLASK_CONFIG=production gunicorn --workers=2 --bind=localhost:5000 wsgi:application
```

Usage
-----

Add the following webhooks to gitlab:

```
# salt-state repo
https://<ADDRESS>/gitlab/v1/salt-state/events/push 
# salt-pillar repo
https://<ADDRESS>/gitlab/v1/salt-pillar/events/push 
```
