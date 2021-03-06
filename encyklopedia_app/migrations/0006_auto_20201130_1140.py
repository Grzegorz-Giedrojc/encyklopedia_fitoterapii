# Generated by Django 3.1.2 on 2020-11-30 10:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('encyklopedia_app', '0005_auto_20201130_1128'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Post_apteczka',
        ),
        migrations.AddField(
            model_name='post',
            name='members',
            field=models.ManyToManyField(to='encyklopedia_app.Member'),
        ),
    ]
