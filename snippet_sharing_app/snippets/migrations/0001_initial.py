# Generated by Django 4.2.3 on 2023-07-22 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('secret_key', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
