# Generated by Django 4.2.6 on 2023-12-21 23:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_remove_product_rating_alter_review_user_rating'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Review',
        ),
    ]
