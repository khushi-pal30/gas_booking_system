# Generated by Django 4.1.6 on 2023-05-19 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gas', '0002_signup_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
                ('email', models.CharField(max_length=20, null=True)),
                ('contact', models.CharField(max_length=30, null=True)),
                ('complain', models.CharField(max_length=90, null=True)),
            ],
        ),
    ]
