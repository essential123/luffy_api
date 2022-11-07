from django.db import models

from utils.models import BaseModel


class Banner(BaseModel):
    # 图片地址，图片名，图片介绍，link地址
    title = models.CharField(max_length=32, unique=True, verbose_name='名称')
    image = models.ImageField(upload_to='banner', verbose_name='图片')
    link = models.CharField(max_length=64, verbose_name='跳转链接')
    info = models.TextField(verbose_name='详情')

    class Meta:
        db_table = 'luffy_banner'
        verbose_name_plural = '轮播图表'

    def __str__(self):
        return self.title
