# Generated by Django 4.2.11 on 2024-11-21 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsfeed', '0002_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='posts/img/Blank.jpg', upload_to='posts/img/'),
        ),
    ]
