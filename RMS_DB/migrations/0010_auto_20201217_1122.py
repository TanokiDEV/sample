# Generated by Django 3.1.4 on 2020-12-17 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RMS_DB', '0009_product_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Bread', 'Bread'), ('Vegetables', 'Vegetables'), ('Meat', 'Meat'), ('Fish', 'Fish')], max_length=200, null=True),
        ),
    ]
