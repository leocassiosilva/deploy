# Generated by Django 3.1.5 on 2021-03-19 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(db_column='id_status', primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'status_trabalho',
                'managed': True,
            },
        ),
    ]
