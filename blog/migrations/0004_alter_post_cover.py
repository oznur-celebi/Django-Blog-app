# Generated by Django 4.0.1 on 2022-02-09 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cover',
            field=models.ImageField(default='design.jpg', upload_to='cover/'),
        ),
    ]
