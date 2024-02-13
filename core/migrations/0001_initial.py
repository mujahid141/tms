# Generated by Django 4.2.6 on 2024-02-13 09:27

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
                ('title', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('discription', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userName', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=255)),
                ('lastName', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskId', models.UUIDField(auto_created=True)),
                ('taskName', models.CharField(max_length=255)),
                ('discription', models.CharField(max_length=255)),
                ('startingDate', models.DateTimeField(auto_now_add=True)),
                ('duration', models.DurationField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.user')),
            ],
        ),
    ]