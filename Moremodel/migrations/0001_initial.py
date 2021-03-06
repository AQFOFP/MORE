# Generated by Django 2.2.4 on 2019-08-17 02:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artititle', models.CharField(max_length=200)),
                ('artidescribe', models.CharField(max_length=200)),
                ('articontent', models.CharField(max_length=255)),
                ('artiimg', models.CharField(max_length=200)),
                ('artirelation', models.CharField(max_length=255)),
                ('artidatetime', models.DateTimeField(auto_now_add=True)),
                ('artitype', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'more_article',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentscontent', models.CharField(max_length=200)),
                ('commentsdatetime', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Moremodel.Article')),
            ],
            options={
                'db_table': 'more_comments',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=100)),
                ('sex', models.BooleanField(default=True)),
                ('icon', models.CharField(max_length=200)),
                ('introduct', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'more_user',
            },
        ),
        migrations.CreateModel(
            name='Historyread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hisreaddatetime', models.DateTimeField()),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Moremodel.Article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Moremodel.User')),
            ],
            options={
                'db_table': 'more_historyread',
            },
        ),
        migrations.CreateModel(
            name='Focus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('focuuser', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_focu', to='Moremodel.User')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Moremodel.User')),
            ],
            options={
                'db_table': 'more_focus',
            },
        ),
        migrations.CreateModel(
            name='Commentszan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Moremodel.Comments')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Moremodel.User')),
            ],
            options={
                'db_table': 'more_commentszan',
            },
        ),
        migrations.AddField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Moremodel.User'),
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastreadtime', models.DateTimeField()),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Moremodel.Article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Moremodel.User')),
            ],
            options={
                'db_table': 'more_collection',
            },
        ),
    ]
