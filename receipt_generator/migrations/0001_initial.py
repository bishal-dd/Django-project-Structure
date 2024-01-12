# Generated by Django 5.0.1 on 2024-01-08 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100, null=True)),
                ('logo_image', models.TextField(null=True)),
                ('phone_no', models.IntegerField(blank=True, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('city', models.CharField(max_length=100, null=True)),
                ('title', models.CharField(max_length=100, null=True)),
                ('signature_image', models.TextField(null=True)),
                ('manual_signature_image', models.CharField(max_length=20000, null=True)),
                ('slug', models.SlugField()),
            ],
        ),
    ]
