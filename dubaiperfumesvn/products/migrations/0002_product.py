# Generated by Django 2.0.1 on 2018-01-16 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('price', models.PositiveIntegerField()),
                ('description', models.CharField(max_length=300)),
                ('info', models.TextField()),
                ('star', models.FloatField()),
            ],
        ),
    ]
