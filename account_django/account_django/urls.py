"""
URL configuration for account_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# 📄 ملف [ account/account_django/account_django/urls.py ]

# 🌐 تكوين الروابط الرئيسية لمشروع Django
# 🌐 Main URL Configuration for Django Project

# 🔧 استيراد لوحة تحكم الإدارة من Django
from django.contrib import admin

# 🔗 استيراد الدوال path و include من Django لتحديد الروابط
from django.urls import (
    path,
    include,
)

# ⚙️ استيراد إعدادات Django
from django.conf import settings

# 📁 استيراد static لعرض ملفات الوسائط
from django.conf.urls.static import static


urlpatterns = [
    # 🔗 تضمين روابط تطبيق 'account' للنقاط البرمجية
    # 🌐 Include URLs from the 'account' app for API endpoints
    path(
        "api/", include("account.urls")
    ),  # 🔗 الرابط الأساسي الذي يوجه إلى تطبيق "account" للحصول على النقاط البرمجية
    # 🔧 لوحة تحكم الإدارة لإدارة الموقع
    # 🌐 Admin panel for site management
    path("admin/", admin.site.urls),  # 🔑 الرابط للوصول إلى لوحة تحكم الإدارة في Django
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# 🖼️ عرض ملفات الوسائط أثناء التطوير
# 🌐 Serve media files during development
# 🎥 تقوم هذه السطر بإعداد نظام عرض ملفات الوسائط (مثل الصور والفيديوهات) أثناء مرحلة التطوير باستخدام الروابط المحددة في الإعدادات (settings).
