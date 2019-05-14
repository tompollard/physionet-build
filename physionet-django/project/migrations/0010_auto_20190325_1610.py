# Generated by Django 2.1.7 on 2019-03-25 20:10

from django.db import migrations, models
import user.validators


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0009_auto_20190319_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='activeproject',
            name='short_description',
            field=models.CharField(blank=True, max_length=250, validators=[user.validators.validate_alphaplusplus]),
        ),
        migrations.AddField(
            model_name='archivedproject',
            name='short_description',
            field=models.CharField(blank=True, max_length=250, validators=[user.validators.validate_alphaplusplus]),
        ),
        migrations.AddField(
            model_name='publishedproject',
            name='short_description',
            field=models.CharField(blank=True, max_length=250, validators=[user.validators.validate_alphaplusplus]),
        ),
    ]