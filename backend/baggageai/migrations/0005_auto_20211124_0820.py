# Generated by Django 3.2.9 on 2021-11-24 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baggageai', '0004_auto_20211124_0646'),
    ]

    operations = [
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=100)),
                ('object_detected', models.CharField(max_length=200)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='file',
            name='remark',
        ),
    ]