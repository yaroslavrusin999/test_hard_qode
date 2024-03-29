# Generated by Django 4.2 on 2024-02-29 09:52

from django.db import migrations, models
import django.db.models.deletion
import product.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=255)),
                ('start_date', models.DateTimeField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, validators=[product.validators.validate_positiv_price])),
                ('max_students', models.PositiveSmallIntegerField()),
                ('min_students', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('link_to_video', models.URLField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='product.product')),
            ],
        ),
    ]
