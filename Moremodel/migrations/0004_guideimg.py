# Generated by Django 2.2.4 on 2019-08-19 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Moremodel', '0003_auto_20190817_1804'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuideImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'guide_img',
            },
        ),
    ]