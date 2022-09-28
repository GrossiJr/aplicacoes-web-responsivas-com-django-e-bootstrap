# Generated by Django 4.0.2 on 2022-09-28 00:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_data_publicacao_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data_publicacao',
            field=models.DateTimeField(verbose_name=datetime.datetime(2022, 9, 28, 0, 39, 43, 844453, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='Assunto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('posts', models.ManyToManyField(to='blog.Post')),
            ],
        ),
    ]
