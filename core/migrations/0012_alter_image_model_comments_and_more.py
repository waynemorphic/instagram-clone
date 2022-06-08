# Generated by Django 4.0.5 on 2022-06-08 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_image_model_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image_model',
            name='comments',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='image_model',
            name='image_caption',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='profile_model',
            name='bio',
            field=models.CharField(max_length=250),
        ),
    ]
