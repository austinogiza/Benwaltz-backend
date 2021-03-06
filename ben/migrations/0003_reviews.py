# Generated by Django 3.1.2 on 2021-04-17 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ben', '0002_contact_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('feel', models.CharField(max_length=200)),
                ('number', models.CharField(max_length=200)),
                ('rating', models.CharField(max_length=200)),
                ('recommend', models.BooleanField(default=False)),
                ('suggest', models.CharField(max_length=200)),
                ('social', models.CharField(max_length=200)),
                ('comment', models.TextField()),
                ('photo', models.ImageField(upload_to='')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
