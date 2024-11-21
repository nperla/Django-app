# Generated by Django 4.1.2 on 2024-11-20 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('producer', models.CharField(max_length=50)),
                ('genre', models.CharField(choices=[('action', 'Action'), ('fantasy', 'Fantasy'), ('adventure', 'Adventure'), ('romance', 'Romance'), ('sci-fi', 'Sci Fi'), ('anime', 'Anime')], max_length=20)),
                ('release_date', models.DateField()),
            ],
        ),
    ]