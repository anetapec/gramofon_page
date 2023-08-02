Install pipenv
First, use the following command to install pipenv tool:
```bash
pip install pipenv
```
Second on Windows , replace your <username> in the following paths and add them to the PATH environment variable:

c:\Users\<username>\AppData\Roaming\Python\Python38\Site-Packages
C:\Users\<username>\AppData\Roaming\Python\Python38\Scripts

Install pipenv on Linux
```bash


PS C:\software\repos\gramofon_page> python -m pipenv install django
PS C:\software\repos\gramofon_page> ls

    Directory: C:\software\repos\gramofon_page

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d----          02.08.2023    13:26                .vscode
d----          02.08.2023    13:26                automation
d----          02.08.2023    23:20                gramofonsite
d----          02.08.2023    13:26                media
d----          02.08.2023    23:27                mysite
d----          02.08.2023    13:26                teamporary
d----          02.08.2023    13:26                venv
d----          02.08.2023    23:40                websites
-a---          02.08.2023    15:27             68 .gitignore
-a---          02.08.2023    13:26            684 manage.py
-a---          02.08.2023    23:58            152 Pipfile ---> this file gets created with the environemnt dependency
-a---          02.08.2023    23:58           2122 Pipfile.lock  ---> this file gets created with the environemnt dependency
-a---          02.08.2023    23:56            118 README.md
-a---          02.08.2023    15:27            186 requirements.txt
```
Activating virtual environments
```bash
python -m pipenv shell
python -m pipenv --venv # this shows the path for the virtual env directory to be used in VScode interpreter
```

Starting project in current directory reduces redundant top folder 
```bash
django-admin.exe startproject gramofon .
```


Django DEBUG toolbar
https://django-debug-toolbar.readthedocs.io/en/latest/installation.html
```bash
python -m pip install django-debug-toolbar
```