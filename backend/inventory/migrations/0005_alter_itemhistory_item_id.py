# Generated by Django 4.2.3 on 2023-07-21 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_alter_itemhistory_updated_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemhistory',
            name='item_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.item'),
        ),
    ]