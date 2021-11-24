# Generated by Django 3.2.9 on 2021-11-24 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baggageai', '0003_postfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('remark', models.CharField(max_length=20)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Items',
        ),
        migrations.DeleteModel(
            name='Postfile',
        ),
    ]
