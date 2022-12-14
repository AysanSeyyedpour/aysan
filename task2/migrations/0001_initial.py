# Generated by Django 4.0.3 on 2022-12-02 17:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='content',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('des', models.CharField(max_length=200, null=True)),
                ('created', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('created', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='registration',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('course_id', models.UUIDField()),
                ('student_id', models.UUIDField()),
                ('created', models.UUIDField()),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('created', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
