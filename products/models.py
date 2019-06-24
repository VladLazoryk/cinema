from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Категория фильмов'
        verbose_name_plural = 'Категория фильмов'




class Product(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, blank=True, null=True, default=None)
    short_description = models.TextField(blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    premiere = models.CharField(max_length=64, blank=True, null=True, default=None)
    country = models.TextField(blank=True, null=True, default=None)
    genre = models.TextField(blank=True, null=True, default=None)
    director = models.TextField(blank=True, null=True, default=None)
    time = models.CharField(max_length=64, blank=True, null=True, default=None)

    def __str__(self):
        return "%s, %s" % (self.category, self.name)

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильм'


class ProductImage(models.Model):
    product = models.ForeignKey(Product,  on_delete=models.CASCADE, blank=True, null=True, default=None)
    image = models.ImageField(upload_to='products_images/')
    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'