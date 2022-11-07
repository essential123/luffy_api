from .models import Banner
from .serializer import BannerSerializer

# 自动生成路由
from rest_framework.viewsets import GenericViewSet
# 获取所有
from utils.view import CommonListModelMixin
from django.conf import settings


class BannerView(GenericViewSet, CommonListModelMixin):
    queryset = Banner.objects.all().filter(is_delete=False, is_show=True).order_by('orders')[:settings.BANNER_COUNT]
    serializer_class = BannerSerializer
