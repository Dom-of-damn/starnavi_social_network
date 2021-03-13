# Generated by Django 3.1.7 on 2021-03-13 15:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_post_postfeedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostsFeedBack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.BooleanField(default=True, verbose_name='like')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='created')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.post', verbose_name='post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
        migrations.DeleteModel(
            name='PostFeedBack',
        ),
    ]
