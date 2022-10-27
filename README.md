
# how to successfully run it

<br>
enable <i>venv</i> virtual environment<br>

```
.\venv\Scripts\Activate.ps1 
```

<br>
run the server<br>

```
python manage.py runserver 
```

<br>
now you can access the open department table, for that you need to access the address that the server is running

```
http://127.0.0.1:8000/
```

<br>
to view the admin table

```
url: http://127.0.0.1:8000/admin
login: igs_admin
password: 1234

```

<br>
to list/add/delete department

```
http://127.0.0.1:8000/api/departments

```

<br>
to list/add/delete employee

```
http://127.0.0.1:8000/api/employees

```
