# Generated by Django 4.1.3 on 2022-11-12 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Authenticate', '0005_rename_forget_token_profile_forget_password_token'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='forget_password_token',
            new_name='forget_token',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='created_at',
        ),
    ]