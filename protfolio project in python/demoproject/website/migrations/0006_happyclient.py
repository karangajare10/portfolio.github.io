# Generated by Django 5.0.3 on 2024-11-26 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_skill'),
    ]

    operations = [
        migrations.CreateModel(
            name='Happyclient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('happy_number', models.IntegerField()),
                ('happy_title', models.CharField(max_length=100)),
                ('happy_sub_title', models.CharField(max_length=100)),
            ],
        ),
    ]
