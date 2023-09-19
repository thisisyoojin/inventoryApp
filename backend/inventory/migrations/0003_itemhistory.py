# Generated by Django 4.2.3 on 2023-07-21 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_seller_item_seller'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_on', models.DateField()),
                ('item_id', models.CharField()),
                ('count', models.PositiveIntegerField()),
            ],
            options={
                'unique_together': {('updated_on', 'item_id')},
            },
        ),
    ]
