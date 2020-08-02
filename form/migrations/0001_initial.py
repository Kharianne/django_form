# Generated by Django 3.0.8 on 2020-08-02 19:03

from django.db import migrations, models
import form.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(blank=True, max_length=255)),
                ('ico', models.CharField(max_length=8, validators=[form.validators.validate_ico])),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
