
**API Documentation**

API documentation can be found on https://www.postman.com/collections/e8a6586e6f59d07cbb3a

**Development**
1. copy `local_dist.py` to `local.py` in `shareimages` folder.
1. run `pip -r requirements_devel.txt`

**Testing**

Before you send your code to remote repository, please run all test locally

```
$ safety check --full-report
$ black --check -l 120 --exclude=migrations --exclude=venv .
$ flake8 .
$ bandit -x tests,./venv/ -r .
$ isort --check-only --diff .
$ coverage run --omit="venv/*" --branch --source=. ./manage.py test
```

You can run this commands to fix some bugs from static code analysis:
```
$ black -l 120 --exclude=migrations --exclude=venv .
$ isort .
```
