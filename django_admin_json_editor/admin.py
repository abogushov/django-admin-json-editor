import json

from django import forms
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe


class JSONEditorWidget(forms.Widget):
    template_name = 'django_admin_json_editor/editor.html'

    def __init__(self, schema, collapsed=True, sceditor=False, editor_options=None):
        super(JSONEditorWidget, self).__init__()
        self._schema = schema
        self._collapsed = collapsed
        self._sceditor = sceditor
        self._editor_options = editor_options or {}

    def render(self, name, value, attrs=None, renderer=None):
        if callable(self._schema):
            schema = self._schema(self)
        else:
            schema = self._schema

        schema['title'] = ' '
        schema['options'] = {'collapsed': int(self._collapsed)}

        editor_options = {
            'theme': 'bootstrap3',
            'iconlib': 'fontawesome4',
            'schema': schema,
        }
        editor_options.update(self._editor_options)

        context = {
            'name': name,
            'data': value,
            'sceditor': int(self._sceditor),
            'editor_options': json.dumps(editor_options),
        }
        return mark_safe(render_to_string(self.template_name, context))

    @property
    def media(self):
        css = {
            'all': [
                'django_admin_json_editor/bootstrap/css/bootstrap.min.css',
                'django_admin_json_editor/fontawesome/css/font-awesome.min.css',
                'django_admin_json_editor/style.css',
            ]
        }
        js = [
            'django_admin_json_editor/jquery/jquery.min.js',
            'django_admin_json_editor/bootstrap/js/bootstrap.min.js',
            'django_admin_json_editor/jsoneditor/jsoneditor.min.js',
        ]
        if self._sceditor:
            css['all'].append('django_admin_json_editor/sceditor/themes/default.min.css')
            js.append('django_admin_json_editor/sceditor/jquery.sceditor.bbcode.min.js')
        return forms.Media(css=css, js=js)
