# 📄 صفحة [account/account_django/account/models.py]

# 🌟 1️⃣ **from django.contrib import admin**
#     - يتم هنا استيراد الوحدة `admin` من مكتبة Django.
#     - وحدة `admin` توفر لوحة تحكم إدارية جاهزة لإدارة النماذج (Models) والبيانات في المشروع.
#
# 🌟 2️⃣ **from .models import User**
#     - يتم استيراد النموذج (Model) `User` من ملف `models.py` الموجود في نفس التطبيق.
#     - النموذج `User` يُستخدم لتمثيل جدول في قاعدة البيانات يحتوي على معلومات مثل المستخدمين.
#
# 🌟 3️⃣ **admin.site.register(User)**
#     - يتم تسجيل النموذج `User` داخل لوحة التحكم الإدارية باستخدام هذا السطر.
#     - بعد التسجيل، سيظهر النموذج `User` في لوحة التحكم الإدارية، ويمكن للمسؤولين إضافة، تعديل، أو حذف البيانات المتعلقة به.
#     - تسجيل النموذج يجعل إدارة البيانات أكثر سهولة ومرونة من خلال واجهة المستخدم الإدارية.

from django.contrib import admin
from .models import User

admin.site.register(User)
