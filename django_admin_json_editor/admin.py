import json

from django import forms
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe


class JSONEditorWidget(forms.Widget):
    template_name = 'django_admin_json_editor/editor.html'

    def __init__(self, schema, collapsed=True, sceditor=False, editor_options=None, independent_fieldset=False):
        super(JSONEditorWidget, self).__init__()
        self._schema = schema
        self._collapsed = collapsed
        self._sceditor = sceditor
        self._independent_fieldset = independent_fieldset
        self._editor_options = {
            'theme': 'spectre',
            'iconlib': 'spectre',
        }
        self._editor_options.update(editor_options or {})

    def render(self, name, value, attrs=None, renderer=None):
        if callable(self._schema):
            schema = self._schema(self)
        else:
            schema = self._schema

        schema['title'] = ' '
        schema['options'] = {'collapsed': int(self._collapsed)}

        editor_options = self._editor_options.copy()
        editor_options['schema'] = schema

        context = {
            'name': name,
            'data': value,
            'editor_options': json.dumps(editor_options),
            'independent_fieldset': self._independent_fieldset
        }
        return mark_safe(render_to_string(self.template_name, context))

    @property
    def media(self):
        css = {
            'all': [
                'django_admin_json_editor/style.css',
            ]
        }
        js = [
            'django_admin_json_editor/jsoneditor/jsoneditor.min.js',
        ]

        if self._editor_options['iconlib'] == 'fontawesome':
            css['all'].append('django_admin_json_editor/fontawesome/css/font-awesome.min.css')
        elif self._editor_options['iconlib'] == 'spectre':
            css['all'].append('django_admin_json_editor/spectre/spectre-icons.min.css')
        if self._editor_options['theme'] == 'spectre':
            css['all'].append('django_admin_json_editor/spectre/spectre.min.css')
            css['all'].append('django_admin_json_editor/spectre/spectre-exp.min.css')
        elif self._editor_options['theme'] == 'bootstrap4':
            css['all'].append('django_admin_json_editor/bootstrap/css/bootstrap.min.css')
            js.append('django_admin_json_editor/jquery/jquery-3.5.1.slim.min.js')
            js.append('django_admin_json_editor/bootstrap/js/bootstrap.bundle.min.js')

        if self._sceditor:
            css['all'].append('django_admin_json_editor/sceditor/themes/default.min.css')
            js.append('django_admin_json_editor/sceditor/jquery.sceditor.bbcode.min.js')
        return forms.Media(css=css, js=js)
