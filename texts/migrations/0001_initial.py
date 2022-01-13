# Generated by Django 3.2 on 2022-01-11 14:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('whatthegam', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_dt', models.DateTimeField(auto_now=True)),
                ('x_axis', models.FloatField(default=0.0)),
                ('y_axis', models.FloatField(default=0.0)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('written_school', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='whatthegam.school')),
            ],
        ),
    ]
