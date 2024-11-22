# 📄 ملف [ account/account_django/account/urls.py ]

# 🌐 تكوين الروابط لواجهة برمجية لإدارة المستخدم والأصدقاء
# 🌐 URL Configuration for User and Friend Management API

from django.urls import path  # 📦 استيراد path من مكتبة Django لتحديد الروابط
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)  # 🛡️ استيراد عرض الحصول على رمز JWT وتحديثه
from . import api  # 🔧 استيراد الوظائف من ملف api

urlpatterns = [
    # 👤 استرجاع معلومات المستخدم الحالي
    # 🌐 Retrieve current user's information
    path(
        "me/", api.me, name="me"
    ),  # 👥 رابط لاسترجاع معلومات المستخدم الذي قام بتسجيل الدخول
    # 📝 تسجيل مستخدمين جدد
    # 🌐 Signup for new users
    path("signup/", api.signup, name="signup"),  # 📝 رابط لتسجيل مستخدمين جدد
    # 🔑 الحصول على رمز JWT لتسجيل الدخول
    # 🌐 Obtain JWT token for login
    path(
        "login/", TokenObtainPairView.as_view(), name="token_obtain"
    ),  # 🔑 رابط للحصول على رمز JWT لتسجيل الدخول
    # ♻️ تحديث رمز JWT
    # 🌐 Refresh JWT token
    path(
        "refresh/", TokenRefreshView.as_view(), name="token_refresh"
    ),  # 🔄 رابط لتحديث رمز JWT
    # ___________________________
    # ___________________________
    # ___________________________
    # ** إدارة الملف الشخصي للمستخدم **
    # 📝 استرجاع الملف الشخصي للمستخدم بناءً على معرفه
    # 🌐 Retrieve user profile by ID
    path(
        "profile/<uuid:id>/", api.profile, name="profile"
    ),  # 👤 رابط لعرض الملف الشخصي للمستخدم باستخدام المعرف (ID)
    # ✏️ تعديل الملف الشخصي للمستخدم
    # 🌐 Edit user profile
    path(
        "editprofile/", api.editprofile, name="editprofile"
    ),  # 📝 رابط لتعديل الملف الشخصي للمستخدم
    # 🔒 تغيير كلمة مرور المستخدم
    # 🌐 Change user password
    path(
        "editpassword/", api.editpassword, name="editpassword"
    ),  # 🔑 رابط لتغيير كلمة مرور المستخدم
    # ___________________________
    # ___________________________
    # ___________________________
    # ** إدارة الأصدقاء **
    # 👫 استرجاع أصدقاء المستخدم
    # 🌐 Retrieve friends of a user
    path(
        "friends/<uuid:pk>/", api.friends, name="friends"
    ),  # 👥 رابط لاسترجاع أصدقاء المستخدم بناءً على المعرف (ID)
    # 🤝 استرجاع الأصدقاء المقترحين للمستخدم
    # 🌐 Retrieve suggested friends for the user
    path(
        "friends/suggested/",
        api.my_friendship_suggestions,
        name="my_friendship_suggestions",
    ),  # 👫 رابط لاسترجاع الأصدقاء المقترحين بناءً على الصداقات السابقة
    # ✉️ إرسال طلب صداقة
    # 🌐 Send a friendship request
    path(
        "friends/<uuid:pk>/request/",
        api.send_friendship_request,
        name="send_friendship_request",
    ),  # 💌 رابط لإرسال طلب صداقة إلى مستخدم آخر
    # 🛠️ معالجة طلب الصداقة (قبول/رفض)
    # 🌐 Handle a friendship request (accept/reject)
    path(
        "friends/<uuid:pk>/<str:status>/", api.handle_request, name="handle_request"
    ),  # 👥 رابط لمعالجة طلب الصداقة (قبول أو رفض)
]
