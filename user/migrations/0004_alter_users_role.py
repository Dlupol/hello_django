# Generated by Django 4.1.3 on 2022-11-25 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_permission_role_users_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='role',
            field=models.ForeignKey(default=3, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.role'),
        ),
    ]
