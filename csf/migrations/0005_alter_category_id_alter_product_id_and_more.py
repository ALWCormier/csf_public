# Generated by Django 4.2.3 on 2023-07-24 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csf', '0004_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
