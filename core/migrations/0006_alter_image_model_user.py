# Generated by Django 4.0.5 on 2022-06-06 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_image_model_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image_model',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.user_model'),
        ),
    ]
