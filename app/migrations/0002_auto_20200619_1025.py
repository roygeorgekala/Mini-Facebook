# Generated by Django 3.0.7 on 2020-06-19 04:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='About',
            new_name='about',
        ),
        migrations.RenameField(
            model_name='userinfo',
            old_name='Birthday',
            new_name='birthday',
        ),
        migrations.RenameField(
            model_name='userinfo',
            old_name='Gender',
            new_name='gender',
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='profile_pic',
            field=models.ImageField(blank='True', upload_to='profile_pic/'),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=400)),
                ('photo', models.ImageField(null=True, upload_to='post_images/')),
                ('video', models.FileField(null=True, upload_to='video_videos/')),
                ('l', models.IntegerField(default=0)),
                ('c', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.userinfo')),
            ],
        ),
    ]
