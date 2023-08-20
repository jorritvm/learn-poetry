# Learn poetry

## Purpose
The purpose of this repo is to learn poetry for package management and package building. Different approaches are compared.

## flat versus src layout
A lot was writtne on this topic:
* https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/
* https://py-pkgs.org/04-package-structure#the-source-layout

TLDR; the source layout has some advantages but requires the package to be installed (in editable mode) before you can use / test your code.


## Poetry setup
* `poetry` is best installed following [the official documentation guidelines](https://python-poetry.org/docs/#installation) instead of using pip. 
* `poetry` has its own virtual environments but uses a cache for this. I prefer to have my virtual environments inside my package folder:
```
C:\Users\jorrit>poetry config virtualenvs.in-project true

C:\Users\jorrit>poetry config --list
cache-dir = "C:\\Users\\jorrit\\AppData\\Local\\pypoetry\\Cache"
experimental.system-git-client = false
installer.max-workers = null
installer.modern-installation = true
installer.no-binary = null
installer.parallel = true
virtualenvs.create = true
virtualenvs.in-project = true   <--- this is better!
virtualenvs.options.always-copy = false
virtualenvs.options.no-pip = false
virtualenvs.options.no-setuptools = false
virtualenvs.options.system-site-packages = false
virtualenvs.path = "{cache-dir}\\virtualenvs"  # C:\Users\jorrit\AppData\Local\pypoetry\Cache\virtualenvs
virtualenvs.prefer-active-python = false
virtualenvs.prompt = "{project_name}-py{python_version}"
```

## Poetry-pycharm
Folder `poetry-pycharm` contains a project set up in pycharm.
[<img src="doc/pycharm01.png" width="300"/>](doc/pycharm_01.png)

This results in a very simple project structure.
If you want to do any package development you will have to add a lot of structure (e.g. the 'source'-layout) to this.
```
Folder PATH listing for volume Windows-SSD
Volume serial number is 6E8D-45D5
C:.
ª   main.py
ª   pyproject.toml
ª   
+---.idea
ª       ...
+---.venv
    ª   ... (contains the environment created by poetry)
```

## Poetry-new
Folder `poetry-new` contains a project set up with 
```
C:\Users\jorrit\Desktop\learn-poetry>poetry new poetry-new
Created package poetry_new in poetry-new
```
This structure is meant to start building a package BUT
* it uses the flat layout and not the source layout
* it has no venv set up from the start
```
Folder PATH listing for volume Windows-SSD
Volume serial number is 6E8D-45D5
C:.
ª   pyproject.toml
ª   README.md
ª   
+---poetry_new
ª       __init__.py
ª       
+---tests
        __init__.py     
```
You could add the venv when 'adding' the pycharm project.
[<img src="doc/pycharm02.png" width="300"/>](doc/pycharm_02.png)

Moving to a 'source'-layout manually also requires updates to the pyprojec.toml file so this is not advised (see next project).

## Poetry-new-src
There is an easy way to set up a python package project in source layout:
```
C:\Users\jorrit\Desktop\learn-poetry>poetry new --src poetry-new-src
Created package poetry_new_src in poetry-new-src
```
Indeed, this results in the desired layout.
```
Folder PATH listing for volume Windows-SSD
Volume serial number is 6E8D-45D5
C:.
│   pyproject.toml
│   README.md
│
├───src
│   └───poetry_new_src
│           __init__.py
│
└───tests
        __init__.py
```
Note that this project, like the previous one, does not come with a venv out of the box. However, the first time we install a package using `poetry add` this environment is immediatly created for us by poetry.
```
C:\Users\jorrit\Desktop\learn-poetry\poetry-new-src>poetry add requests
Creating virtualenv poetry-new-src in C:\Users\jorrit\Desktop\learn-poetry\poetry-new-src\.venv
Using version ^2.31.0 for requests

Updating dependencies
Resolving dependencies...

Package operations: 5 installs, 0 updates, 0 removals

  • Installing certifi (2023.7.22)
  • Installing charset-normalizer (3.2.0)
  • Installing idna (3.4)
  • Installing urllib3 (2.0.4)
  • Installing requests (2.31.0)

Writing lock file
```
In addition, this dependency is immediatly added to pyproject.toml
```
[tool.poetry]
name = "poetry-new-src"
version = "0.1.0"
description = ""
authors = ["Jorrit Vander Mynsbrugge <44178217+jorritvm@users.noreply.github.com>"]
readme = "README.md"
packages = [{include = "poetry_new_src", from = "src"}]

[tool.poetry.dependencies]
python = "^3.9"
requests = "^2.31.0"


[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```