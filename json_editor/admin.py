import json

from django import forms
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string


class JSONEditorWidget(forms.Widget):

    template_name = 'django_json_editor/django_json_editor.html'

    def __init__(self, schema, collapsed=True):
        super().__init__()
        self._schema = schema
        self._collapsed = int(collapsed)

    def render(self, name, value, attrs=None):
        self._schema['title'] = name
        self._schema['options'] = {'collapsed': 1}

        context = {
            'name': name,
            'schema': self._schema,
            'data': json.loads(value),
        }
        return mark_safe(render_to_string(self.template_name, context))

    class Media:
        css = {'all': (
            'django_json_editor/bootstrap/css/bootstrap.min.css',
            'django_json_editor/fontawesome/css/font-awesome.min.css',
            'django_json_editor/style.css',
        )}
        js = (
            'django_json_editor/jquery/jquery.min.js',
            'django_json_editor/bootstrap/js/bootstrap.min.js',
            'django_json_editor/jsoneditor/jsoneditor.min.js',
        )
