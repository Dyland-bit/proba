from django.db import models

# Create your models here.

class Files(models.Model):
    """Представление модели файлов."""

    name = models.CharField(max_length=100, verbose_name='Имя файла')

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'
        db_table = 'files' # Название таблицы в базе

    def __str__(self):
        """Unicode представление файлов."""
        return "<Файл('%s')>" % (self.name)

class Shops(models.Model):
    """Представление модели Магазины."""

    name = models.CharField(max_length=50, verbose_name='Название магазина')
    # buy = models.ForeignKey(Buys, on_delete=models.SET_NULL, null=True)
    
    class Meta:

        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазин'
        db_table = 'shops' # Название таблицы в базе

    def __str__(self):
        return self.name

class Categorys(models.Model):
    """Представление модели Категории."""

    name = models.CharField(max_length=50, verbose_name='Название категории')
    is_active = models.BooleanField(default=True)
    # subcategory = models.ForeignKey(Subcategorys, on_delete=models.SET_NULL, null=True)
    # product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True)

    class Meta:

        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        db_table = 'categorys' # Название таблицы в базе

    def __str__(self):
        return self.name

class Subcategorys(models.Model):
    """Представление модели Подкатегории."""
    
    name = models.CharField(max_length=50, verbose_name='Название подкатегории')
    сategory = models.ForeignKey(Categorys, on_delete=models.SET_NULL, null=True, blank=True)
    # product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True)

    class Meta:

        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'
        db_table = 'subcategorys' # Название таблицы в базе

    def __str__(self):
        return "%s - %s" % (self.сategory, self.name)

class Products(models.Model):
    """Представление модели Продукты."""
    
    name = models.CharField(max_length=100, verbose_name='Название продукта')
    # сategory = models.ForeignKey(Categorys, on_delete=models.SET_NULL, null=True)
    subcategory = models.ForeignKey(Subcategorys, on_delete=models.SET_NULL, null=True, blank=True)
    # buy = models.ForeignKey(Buys, on_delete=models.SET_NULL, null=True)

    class Meta:

        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        db_table = 'products' # Название таблицы в базе

    def __str__(self):
        return self.name

class Buys(models.Model):
    """Представление модели Покупки."""
    
    id_prd = models.ForeignKey(Products, on_delete=models.SET_DEFAULT, blank=True, null=True, default=None,  verbose_name = 'ID продукта')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name = 'Цена за ед.')
    quantity = models.FloatField(default=1, verbose_name = 'Количество') 
    sum = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name = 'Сумма') #price*quantity
    date = models.DateTimeField(verbose_name = 'Дата покупки')
    id_shop =  models.ForeignKey(Shops, on_delete=models.SET_NULL, null=True, blank=True, verbose_name = 'ID магазина')

    class Meta:

        verbose_name = 'Покупка'
        verbose_name_plural = 'Покупки'
        db_table = 'buys' # Название таблицы в базе

    def __str__(self):
        return "<Buy('%s','%s','%s','%s','%s','%s'>" % (
            self.id_prd, self.price, self.quantity,
            self.sum, self.date, self.id_shop)




