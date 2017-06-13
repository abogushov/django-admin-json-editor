# An example of using application

To run example to this steps:

```bash
python3 -m venv env
. env/bin/activate
pip install -r requirements.txt
createdb json_editor_example
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open `http://localhost:8000/admin/app/jsonmodel/add/`. You will see:

![Example](django-admin-json-editor/examples/json_editor_example/example.png)

