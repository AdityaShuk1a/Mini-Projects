# Generated by Django 5.1.1 on 2024-10-08 15:08

import api.models
import django.core.validators
import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=50)),
                ('user_email', models.EmailField(max_length=254, unique=True, validators=[django.core.validators.EmailValidator()])),
                ('user_phone_number', models.BigIntegerField(unique=True)),
                ('timestamp', models.BigIntegerField(default=api.models.current_timestamp, editable=False)),
                ('user_password', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='NotesModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('note_heading', models.CharField(blank=True, max_length=255)),
                ('note_body', models.TextField()),
                ('created_at_timestamp', models.BigIntegerField(default=api.models.current_timestamp, editable=False)),
                ('updated_at_timestamp', models.BigIntegerField(default=api.models.current_timestamp, editable=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='api.usermodel')),
            ],
            options={
                'ordering': ['-updated_at_timestamp'],
            },
        ),
    ]
