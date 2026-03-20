import os
import sys
from pathlib import Path
from django.conf.urls.static import static
from django.conf import settings

BASE_DIR = Path(__file__).parent.resolve()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'onefile.settings')

import django
from django.conf import settings

if not settings.configured:
    settings.configure(
        DEBUG=True,
        SECRET_KEY='devkey123',
        ROOT_URLCONF=__name__,
        ALLOWED_HOSTS=['*'],
        MIDDLEWARE=[
            'django.middleware.common.CommonMiddleware',
        ],
        TEMPLATES=[{
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [BASE_DIR / 'templates'],  # index.html и layouts/base.html
            'APP_DIRS': True,
        }],
        STATIC_URL='/static/',
        STATICFILES_DIRS=[BASE_DIR / 'static'],
    )

django.setup()

# --------------------------
# URL маршруты
# --------------------------
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='ask.html')),
]
urlpatterns += static(settings.STATIC_URL, document_root=BASE_DIR / 'static')
# --------------------------
# Запуск сервера
# --------------------------
from django.core.management import execute_from_command_line

if __name__ == '__main__':
    sys.argv = [sys.argv[0], 'runserver', '8000']
    execute_from_command_line(sys.argv)