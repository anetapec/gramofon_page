import subprocess

result1 = subprocess.Popen([f"python3 manage.py makemigrations" ], shell=True)
print(result1.communicate())

result2 = subprocess.Popen([f"python3 manage.py migrate" ], shell=True)
print(result2.communicate())

result2 = subprocess.Popen([f"python3 manage.py runserver"], shell=True)
print(result2.communicate())