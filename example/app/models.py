from django.db import models
from django.contrib.postgres.fields import JSONField


class JSONModel(models.Model):
    data = JSONField(default={
        'text': 'some text',
        'status': False,
        'html': '<h1>Default</h1>',
    })


class ArrayJSONModel(models.Model):
    roles = JSONField(default=[])


class Tag(models.Model):
    name = models.CharField('name', max_length=10)
    
    
class OtherJSONModel(models.Model):
    name = models.CharField(max_length=50)
    data = JSONField(default={
        'other_text': 'some other text',
        'status': True,
    })
    
class RelatedJSONModel(models.Model):
    parent = models.ForeignKey(OtherJSONModel, on_delete=models.CASCADE)
    related_data = JSONField(default={
        'related_info': '',
        'relevant': False,
    })
