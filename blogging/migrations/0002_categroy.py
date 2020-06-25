# Generated by Django 2.1.5 on 2020-06-22 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categroy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(blank=True)),
                ('posts', models.ManyToManyField(related_name='categroies', to='blogging.Post')),
            ],
        ),
    ]