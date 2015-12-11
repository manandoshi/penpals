# Penpals

# Instructions:

1. Pull the repo
```
git pull https://github.com/manandoshi/penpals
```

2. Make it a virtual environment
```
virtualenv .
```

3.  Install the dependancies
```
pip install -U -r requirements.txt
```

**DO NOT** *git add the virtualenv folders (bin, usr, lib, local etc)*

**DO NOT USE git add .**

# Final Directory Structure:

penpals
|_README.md
|_requirements.txt
|_project
	|_manage.py
	|_project
	|	|_ __init__.py
	|	|_ settings.py
	|	|_ urls.py
	|	|_ wsgi.py
	|_penpals
		|_ admin.py
		|_ apps.py
		|_ models.py
		|_ tests.py
		|_ views.py
		|_migrations
		|	|_ __init__.py
		|_static
		|	|_penpals
		|_templates
			|_penpals