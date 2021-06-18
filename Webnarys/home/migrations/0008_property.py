# Generated by Django 3.2.3 on 2021-06-15 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20210615_1721'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institute_name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('rent', models.DecimalField(decimal_places=2, max_digits=5)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='properties', to='home.vendor')),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
    ]