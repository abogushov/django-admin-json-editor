# An example of using application

To run example to this steps:

```bash
cd example
python3 -m venv env
. env/bin/activate
pip install -r requirements.txt
createdb django_admin_json_editor
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open `http://localhost:8000/admin/app/jsonmodel/add/`. You will see:

![Example](example.png)