# Generated by Django 3.2.7 on 2021-09-17 14:40

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('character_cards', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Character_Cards',
            new_name='CharacterCards',
        ),
        migrations.RenameField(
            model_name='charactercards',
            old_name='CharacterDescription',
            new_name='character_description',
        ),
    ]
