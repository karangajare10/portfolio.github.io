# Generated by Django 5.0.3 on 2024-11-26 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_portfolio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='portfolio_image_2',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='portfolio_image_3',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='portfolio_image_4',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='portfolio_image_5',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='portfolio_image_6',
        ),
    ]
