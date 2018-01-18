# Django Administration JSON Editor

[![Build Status](https://travis-ci.org/abogushov/django-admin-json-editor.svg?branch=master)](https://travis-ci.org/abogushov/django-admin-json-editor)



Application adds support for editing JSONField in Django Administration via https://github.com/jdorn/json-editor.

## Quick start

Install application via pip:

```bash
pip install django-admin-json-editor
```

Add application to the INSTALLED_APPS settings:

```python
INSTALLED_APPS = [
    ...
    'django_admin_json_editor',
    ...
]
```

Define schema of json field:

```python
DATA_SCHEMA = {
    'type': 'object',
    'title': 'Data',
    'properties': {
        'text': {
            'title': 'Some text',
            'type': 'string',
            'format': 'textarea',
        },
        'status': {
            'title': 'Status',
            'type': 'boolean',
        },
    },
}
```

Use JSONEditorWidget to bind editor to the form field:

```python
class JSONModelAdminForm(forms.ModelForm):
    class Meta:
        model = JSONModel
        fields = '__all__'
        widgets = {
            'data': JSONEditorWidget(DATA_SCHEMA, collapsed=False),
        }
```

### Dynamic schema

It is possible to build dynamic schema for widget:

```python
def dynamic_schema(widget):
    return {
        'type': 'array',
        'title': 'tags',
        'items': {
            'type': 'string',
            'enum': [i for i in Tag.objects.values_list('name', flat=True)],
        }
    }
```

```python
@admin.register(JSONModel)
class JSONModelAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        widget = JSONEditorWidget(dynamic_schema, False)
        form = super().get_form(request, obj, widgets={'tags': widget}, **kwargs)
        return form
```

