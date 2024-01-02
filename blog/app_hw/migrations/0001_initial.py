# Generated by Django 4.2.8 on 2023-12-10 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_post', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('description_post', models.TextField()),
                ('quantity_likes', models.PositiveIntegerField()),
            ],
        ),
    ]