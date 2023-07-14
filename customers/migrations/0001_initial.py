# Generated by Django 4.2.2 on 2023-06-19 09:46

from django.db import migrations, models
# migrations describe changes to the database


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('industry', models.CharField(max_length=100)),
            ],
        ),
    ]
