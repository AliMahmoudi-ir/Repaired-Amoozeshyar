# Generated by Django 5.0.2 on 2024-12-01 18:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_user_table_tel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='father_Name',
            field=models.CharField(max_length=20, verbose_name='نام پدر'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_Name',
            field=models.CharField(max_length=20, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_Name',
            field=models.CharField(max_length=20, verbose_name='نام خانوادگی'),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('country', models.CharField(max_length=15, verbose_name='کشور')),
                ('state', models.CharField(max_length=15, verbose_name='استان')),
                ('city', models.CharField(max_length=15, verbose_name='شهر')),
                ('district', models.CharField(max_length=15, verbose_name='منطقه')),
                ('street', models.CharField(max_length=15, verbose_name='خیابان')),
                ('alley', models.CharField(max_length=15, verbose_name='کوچه')),
                ('no', models.IntegerField(verbose_name='پلاک')),
                ('floor', models.IntegerField(verbose_name='طبقه')),
                ('post_ID', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='کدپستی')),
                ('user_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.user', verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'آدرس',
                'verbose_name_plural': 'آدرس ها',
                'db_table': 'Address',
            },
        ),
    ]