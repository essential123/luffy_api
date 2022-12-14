# Generated by Django 3.2.12 on 2022-11-07 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='最后更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('is_show', models.BooleanField(default=True, verbose_name='是否显示')),
                ('orders', models.IntegerField(verbose_name='优先级')),
                ('title', models.CharField(max_length=32, unique=True, verbose_name='名称')),
                ('image', models.ImageField(upload_to='banner', verbose_name='图片')),
                ('link', models.CharField(max_length=64, verbose_name='跳转链接')),
                ('info', models.TextField(verbose_name='详情')),
            ],
            options={
                'verbose_name_plural': '轮播图表',
                'db_table': 'luffy_banner',
            },
        ),
    ]
