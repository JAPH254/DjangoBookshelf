# Generated by Django 4.2.7 on 2023-11-06 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('author', models.CharField(blank=250, max_length=250)),
                ('isbn', models.CharField(blank=250, max_length=250)),
                ('summary', models.CharField(blank=True, max_length=250)),
                ('genre', models.CharField(max_length=250)),
                ('publish_date', models.DateField()),
            ],
        ),
    ]
