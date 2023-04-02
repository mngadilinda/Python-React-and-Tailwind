# Generated by Django 4.1.5 on 2023-04-01 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_one', '0002_module_module_image_alter_lesson_lesson_imgs_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='lesson_imgs',
            field=models.ImageField(blank=True, null=True, upload_to='static/lessons/imgs'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='lesson_notes',
            field=models.FileField(blank=True, null=True, upload_to='staticlesson/notes'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='lesson_vid',
            field=models.FileField(blank=True, null=True, upload_to='static/lesson/video'),
        ),
        migrations.AlterField(
            model_name='module',
            name='module_image',
            field=models.ImageField(blank=True, null=True, upload_to='static/modules/'),
        ),
        migrations.AlterField(
            model_name='program',
            name='program_image',
            field=models.ImageField(blank=True, null=True, upload_to='static/prorams/'),
        ),
    ]