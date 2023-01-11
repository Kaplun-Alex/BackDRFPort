# Generated by Django 4.1.4 on 2023-01-11 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_category', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_field', models.CharField(max_length=4096, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portcoreapi.category')),
            ],
        ),
    ]