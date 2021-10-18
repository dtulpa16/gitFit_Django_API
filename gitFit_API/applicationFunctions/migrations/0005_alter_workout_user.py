# Generated by Django 3.2.8 on 2021-10-17 20:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('applicationFunctions', '0004_auto_20211010_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
