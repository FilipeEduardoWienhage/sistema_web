# Generated by Django 5.1.2 on 2024-10-16 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('steamfake', '0010_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='descricao',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
