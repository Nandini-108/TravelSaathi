# Generated by Django 3.2.7 on 2021-09-14 13:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tour', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tour_package',
            old_name='title',
            new_name='tour_title',
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guests', models.IntegerField(default=1)),
                ('tour_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tour.tour_package')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]