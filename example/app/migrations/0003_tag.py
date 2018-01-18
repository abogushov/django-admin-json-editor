from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_roles'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='name')),
            ],
        ),
    ]
