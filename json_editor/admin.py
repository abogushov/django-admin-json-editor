import copy

import collections
from django import forms
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string


class JSONEditorWidget(forms.Widget):

    template_name = 'django_json_editor/django_json_editor.html'

    def __init__(self, schema, collapsed=True):
        super().__init__()
        self._schema = schema
        self._collapsed = collapsed

    def render(self, name, value, attrs=None):
        if callable(self._schema):
            schema = self._schema(self)
        else:
            schema = copy.copy(self._schema)

        self.schema_updater(schema)

        schema['title'] = ' '
        schema['options'] = {'collapsed': int(self._collapsed)}

        context = {
            'name': name,
            'schema': schema,
            'data': value,
        }
        return mark_safe(render_to_string(self.template_name, context))

    @classmethod
    def schema_updater(cls, nested):
        """Updates schema to format allowed by JS"""
        for key, value in nested.items():
            if isinstance(value, collections.Mapping):
                cls.schema_updater(value)
            else:
                # Replace bool values with integers
                nested[key] = int(value) if isinstance(value, bool) else value

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
