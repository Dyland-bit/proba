# Generated by Django 2.2.6 on 2020-05-15 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название категории')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'db_table': 'categorys',
            },
        ),
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя файла')),
            ],
            options={
                'verbose_name': 'Файл',
                'verbose_name_plural': 'Файлы',
                'db_table': 'files',
            },
        ),
        migrations.CreateModel(
            name='Shops',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название магазина')),
            ],
            options={
                'verbose_name': 'Магазин',
                'verbose_name_plural': 'Магазин',
                'db_table': 'shops',
            },
        ),
        migrations.CreateModel(
            name='Subcategorys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название подкатегории')),
                ('сategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Categorys')),
            ],
            options={
                'verbose_name': 'Подкатегория',
                'verbose_name_plural': 'Подкатегории',
                'db_table': 'subcategorys',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название продукта')),
                ('subcategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Subcategorys')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='Buys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Цена')),
                ('quantity', models.FloatField(default=1, verbose_name='Количество')),
                ('sum', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Сумма')),
                ('date', models.DateTimeField(verbose_name='Дата покупки')),
                ('id_prd', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='core.Products', verbose_name='ID продукта')),
                ('id_shop', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Shops', verbose_name='ID магазина')),
            ],
            options={
                'verbose_name': 'Покупка',
                'verbose_name_plural': 'Покупки',
                'db_table': 'buys',
            },
        ),
    ]