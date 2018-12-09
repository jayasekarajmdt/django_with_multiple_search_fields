# Generated by Django 2.1.4 on 2018-12-09 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_freelancer_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='freelancer',
            name='skills',
            field=models.ManyToManyField(to='search.skill'),
        ),
    ]
