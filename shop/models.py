"""このファイル内に、必要なテーブルがすべて定義されます"""
from django.db import models
from django.contrib.auth import get_user_model


class Category(models.Model):
    """商品カテゴリー"""
    name = models.CharField(verbose_name='カテゴリ', max_length=100, blank=False, null=False)

    def __str__(self):
        if hasattr(self, 'product_count'):
            return f'{self.name}({self.product_count})'
        return self.name


class Product(models.Model):
    """商品"""
    name = models.CharField(verbose_name='名前', max_length=200, blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    price = models.IntegerField(verbose_name='単価',)
    description = models.CharField(verbose_name='説明', max_length=100, blank=False, null=False)
    inactive = models.BooleanField(default=False)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField('作成日時', auto_now_add=True)


class Discussion(models.Model):
    """会話"""
    chat = models.TextField(verbose_name='会話')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField('作成日時', auto_now_add=True)
