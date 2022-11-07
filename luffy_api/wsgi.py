"""
上线的配置，后面使用WSGI服务器去运行
WSGI config for luffy_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'luffy_api.settings.prod')

application = get_wsgi_application()
