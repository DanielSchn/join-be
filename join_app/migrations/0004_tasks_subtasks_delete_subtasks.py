# Generated by Django 5.1.1 on 2024-09-20 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join_app', '0003_rename_email_contacts_mail_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='subtasks',
            field=models.JSONField(default=list),
        ),
        migrations.DeleteModel(
            name='Subtasks',
        ),
    ]
