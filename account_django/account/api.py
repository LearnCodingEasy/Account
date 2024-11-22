# 📄 ملف [ messenger/messenger_django/account/api.py ]

# 🌐 API for User Signup and Profile Info Retrieval
# 🌐 API لتسجيل المستخدم واسترجاع معلومات الحساب

# Django إستيراد إعدادات المشروع في
from django.conf import settings

# إستيراد نموذج تغيير كلمة المرور
from django.contrib.auth.forms import PasswordChangeForm

# إستيراد دالة إرسال البريد الإلكتروني
from django.core.mail import send_mail

# JSON لإرجاع استجابات JsonResponse إستيراد
from django.http import JsonResponse

# إستيراد الديكورات لتعريف وحدات الواجهة البرمجية
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)

# إستيراد النماذج المخصصة لتسجيل المستخدم وتعديل الملف الشخصي
from .forms import SignupForm, ProfileForm

# إستيراد النماذج المخصصة للمستخدم وطلبات الصداقة
from .models import User, FriendshipRequest

# إستيراد المسلسلات للمستخدم وطلبات الصداقة
from .serializers import UserSerializer, FriendshipRequestSerializer


# 📝 Signup API Endpoint
# 📝 واجهة برمجية للتسجيل
@api_view(["POST"])  # 📬 السماح فقط بالطلبات من نوع POST.
@authentication_classes([])  # 🚫 لا تتطلب مصادقة
@permission_classes([])  # 🚫 لا تتطلب أذونات
def signup(request):
    """
    وظيفة للتعامل مع تسجيل المستخدم.
    """
    # 🗃️ البيانات المُرسلة مع الطلب.
    data = request.data
    message = "success"

    # 🧾 Initialize signup form with request data
    # 🧾 تهيئة نموذج التسجيل باستخدام بيانات الطلب
    form = SignupForm(
        {
            "name": data.get("name"),
            "surname": data.get("surname"),
            "email": data.get("email"),
            "date_of_birth": data.get("date_of_birth"),
            "gender": data.get("gender"),
            "password1": data.get("password1"),
            "password2": data.get("password2"),
        }
    )

    # ✅ Check if form is valid ✅ التحقق من صحة النموذج
    if form.is_valid():
        # 🛠️ Save the new user 🛠️ حفظ المستخدم الجديد
        user = form.save()
        # 🔓 Activate the account 🔓 تنشيط الحساب مباشرة
        user.is_active = True
        user.save()

        # 📤 إرجاع رسالة نجاح.
        return JsonResponse({"message": message, "email_sent": True}, safe=False)
    else:
        # ❌ If errors exist, return them ❌ إذا كان هناك أخطاء
        message = form.errors.as_json()
    # 🔍 Print errors for debugging 🔍 طباعة الأخطاء لأغراض التصحيح
    print(message)
    return JsonResponse({"message": message}, safe=False)


# 👤 User Info API Endpoint
# JSON إرجاع بيانات المستخدم الحالي كاستجابة
# 👤 واجهة برمجية لاسترجاع معلومات المستخدم
@api_view(["GET"])
def me(request):
    """
    وظيفة لاسترجاع بيانات المستخدم الحالي.
    """
    # ✅ إذا كان المستخدم مصادقًا.
    if request.user.is_authenticated:
        # 📜 تحويل بيانات المستخدم إلى JSON.
        user_serializer = UserSerializer(request.user)
        return JsonResponse(user_serializer.data, safe=False)
    # ❌ إرجاع رسالة خطأ إذا كان المستخدم غير مصادق.
    return JsonResponse({"error": "User not authenticated"}, status=401)


# 📝 Profile API Endpoint
# 📝 واجهة برمجية لاسترجاع بيانات المستخدم
# 🌐 السماح فقط بطلبات GET.
@api_view(["GET"])
def profile(request, id):
    """
    وظيفة لاسترجاع بيانات ملف المستخدم بناءً على معرفه الفريد (ID).
    """
    user = User.objects.get(pk=id)
    # print("Profile User By Id 👉️", user)

    # 📜 تسلسل بيانات المستخدم باستخدام السيريالايزر المخصص.
    user_serializer = UserSerializer(user)
    # print("Profile User By Id 👍", user_serializer)

    # 🟢 افتراض أن المستخدم يمكنه إرسال طلب صداقة.
    can_send_friendship_request = True

    # 🔒 التحقق مما إذا كان المستخدم بالفعل صديقًا.
    if request.user in user.friends.all():
        can_send_friendship_request = False  # 🛑 لا يمكن إرسال طلب صداقة.

    # 🔍 Check if a request already exists between the users
    # 🔍 التحقق مما إذا كان هناك طلب صداقة موجود بالفعل بين المستخدمين
    check1 = FriendshipRequest.objects.filter(created_for=request.user).filter(
        created_by=user
    )
    check2 = FriendshipRequest.objects.filter(created_for=user).filter(
        created_by=request.user
    )
    # For Test
    # print("How Is User check1", check1)
    # print("_______________________________________")
    # print("How Is User check2", check2)
    # print("_______________________________________")

    # 🔴 إذا كان هناك طلب صداقة موجود، لا يمكن إرسال طلب جديد.
    if check1 or check2:
        can_send_friendship_request = False

    # 📤 إرجاع بيانات المستخدم وصلاحية إرسال طلب الصداقة كاستجابة JSON.
    return JsonResponse(
        {
            "user": user_serializer.data,  # بيانات المستخدم المسلسلة.
            "can_send_friendship_request": can_send_friendship_request,  # صلاحية إرسال طلب الصداقة.
        },
        safe=False,  # ⚠️ يتيح إرجاع البيانات غير المهيكلة كـ JSON.
    )


# 📝 واجهة برمجية لتعديل الملف الشخصي
@api_view(["POST"])  # 🌐 هذه الدالة تستجيب فقط لطلبات POST
def editprofile(request):
    # 👤 استرجاع بيانات المستخدم الحالي من الطلب
    # 👤 `request.user` تمثل المستخدم الذي أرسل الطلب
    user = request.user

    # 📧 الحصول على البريد الإلكتروني الجديد المرسل مع الطلب
    # 📧 يتم استخدام `request.data.get` للحصول على قيمة الحقل "email"
    email = request.data.get("email")

    # 📧 التحقق إذا كان البريد الإلكتروني مستخدمًا بالفعل من قبل مستخدم آخر
    # 📧 يتم استبعاد المستخدم الحالي من البحث باستخدام `exclude(id=user.id)`
    if User.objects.exclude(id=user.id).filter(email=email).exists():
        # 🔴 إذا تم العثور على البريد الإلكتروني بالفعل، يتم إرجاع رسالة خطأ
        return JsonResponse({"message": "email already exists"})
    else:
        # 📝 تهيئة نموذج تعديل الملف الشخصي
        # 📝 يتم تمرير البيانات من الطلب (`request.POST`) وأي ملفات (`request.FILES`)
        # 📝 `instance=user` يربط النموذج بالمستخدم الحالي لتعديل بياناته
        form = ProfileForm(request.POST, request.FILES, instance=user)

        # ✅ Validate and save profile if valid
        # ✅ التحقق من صحة النموذج
        # ✅ إذا كانت البيانات صالحة، يتم حفظ التعديلات في قاعدة البيانات
        if form.is_valid():
            form.save()

        # 🔄 تسلسل بيانات المستخدم المحدثة
        # 🔄 يتم استخدام `UserSerializer` لتحويل بيانات المستخدم إلى صيغة JSON
        serializer = UserSerializer(user)

        # 🔄 إرجاع رسالة نجاح تحتوي على بيانات المستخدم المحدثة
        return JsonResponse({"message": "information updated", "user": serializer.data})


# 🛠️ واجهة برمجية لتغيير كلمة المرور
@api_view(["POST"])  # 🌐 الدالة تقبل فقط طلبات POST
def editpassword(request):
    # 🔒 تهيئة نموذج تغيير كلمة المرور
    # 🔒 `PasswordChangeForm` هو نموذج افتراضي من Django لتغيير كلمة المرور
    # 🔒 يتم تمرير بيانات الطلب (`request.POST`) والمستخدم الحالي (`user`)
    user = request.user
    form = PasswordChangeForm(data=request.POST, user=user)

    # ✅ Validate and save new password if valid
    # ✅ التحقق من صحة البيانات في النموذج
    if form.is_valid():
        # 🛠️ إذا كانت البيانات صالحة، يتم حفظ كلمة المرور الجديدة
        form.save()
        # 🟢 إرجاع استجابة نجاح للعميل
        return JsonResponse({"message": "success"})
    else:
        # ❌ Return errors if form is invalid
        # ❌ إذا كانت البيانات غير صالحة، يتم إرجاع الأخطاء
        # 🔍 يتم استخدام `form.errors.as_json()` لتحويل الأخطاء إلى صيغة JSON
        return JsonResponse({"message": form.errors.as_json()}, safe=False)


# 🌐 Friendship Request and Friends Management API
# 🌐 واجهة برمجية لإدارة طلبات الصداقة وإدارة الأصدقاء
@api_view(["POST"])  # 🌐 الدالة تقبل فقط طلبات POST
def send_friendship_request(request, pk):
    # 👤 Get the user to whom the friendship request is being sent
    # 👤 استرجاع بيانات المستخدم الذي سيتم إرسال طلب الصداقة إليه
    # `pk` هو المعرف الفريد للمستخدم المستهدف
    user = User.objects.get(pk=pk)
    # For Test
    # print("How Is User Send Friend Ship Request", pk)
    # print("_______________________________________")

    # 🔍 Check if a request already exists between the users
    # 🔍 التحقق مما إذا كان هناك طلب صداقة موجود بالفعل بين المستخدمين
    # البحث عن طلب تم إنشاؤه من المستخدم المستهدف إلى المستخدم الحالي
    check1 = FriendshipRequest.objects.filter(created_for=request.user).filter(
        created_by=user
    )
    # البحث عن طلب تم إنشاؤه من المستخدم الحالي إلى المستخدم المستهدف
    check2 = FriendshipRequest.objects.filter(created_for=user).filter(
        created_by=request.user
    )
    # For Test
    # print("How Is User check1", check1)
    # print("_______________________________________")
    # print("How Is User check2", check2)
    # print("_______________________________________")

    # 🛠️ إذا لم يكن هناك أي طلبات صداقة موجودة بالفعل
    if not check1 or not check2:
        # ✉️ Create a new friendship request if it doesn't exist
        # ✉️ إنشاء طلب صداقة جديد إذا لم يكن موجودًا
        friendrequest = FriendshipRequest.objects.create(
            created_for=user, created_by=request.user
        )
        # For Test
        # print("Friend Ship Request If ", friendrequest)
        # print("_______________________________________")
        # Return = The Message Show In Frontend
        # 🟢 إرجاع رسالة نجاح لإنشاء طلب الصداقة
        return JsonResponse({"message": "friendship request created"})
    else:
        # Return = The Message Show In Frontend
        # ❌ إذا كان هناك طلب صداقة موجود، يتم إرجاع رسالة خطأ
        return JsonResponse({"message": "request already sent"})


# 🌐 واجهة برمجية لجلب الأصدقاء وطلبات الصداقة لمستخدم معين
@api_view(["GET"])  # 🌐 الدالة تقبل فقط طلبات GET
def friends(request, pk):
    # 👥 Get the friends and requests for the specified user
    # 👥 جلب الأصدقاء والطلبات للمستخدم المحدد
    user = User.objects.get(pk=pk)
    # print("Friends User By Id 👉️", user)

    # 📝 تعريف قائمة لتخزين طلبات الصداقة إذا كان المستخدم الحالي هو نفس المستخدم المطلوب
    requests = []
    # print("Friends Requests By Id 👉️", requests)

    # 📝 Check if the current user is the requested user
    # 📝 التحقق مما إذا كان المستخدم الحالي هو نفس المستخدم المطلوب
    if user == request.user:
        # 🔍 جلب طلبات الصداقة التي تم إنشاؤها للمستخدم الحالي والتي لم يتم إرسالها بعد
        requests = FriendshipRequest.objects.filter(
            created_for=request.user, status=FriendshipRequest.NOT_SENT
        )
        # print("requests Friends", requests)

        # 🔄 تحويل الطلبات إلى بيانات JSON باستخدام السيريالايزر
        requests = FriendshipRequestSerializer(requests, many=True)
        requests = requests.data

        # print("Friends Requests By Id 👉️", requests)

    # 👫 Retrieve all friends of the user 👫 جلب جميع أصدقاء المستخدم
    friends = user.friends.all()
    # print("Friends Friends 👉️", friends)

    # 📤 إرجاع البيانات كاستجابة JSON تحتوي على بيانات المستخدم، الأصدقاء، والطلبات
    return JsonResponse(
        {
            "user": UserSerializer(user).data,  # بيانات المستخدم
            "friends": UserSerializer(friends, many=True).data,  # بيانات الأصدقاء
            "requests": requests,  # طلبات الصداقة (إذا كانت موجودة)
        },
        safe=False,  # السماح بتمرير كائنات ليست من نوع القاموس
    )


# 🌐 واجهة برمجية لاقتراح المستخدمين الذين قد يعرفهم المستخدم الحالي
@api_view(["GET"])  # 🌐 الدالة تقبل فقط طلبات GET
def my_friendship_suggestions(request):

    # 🤝 Suggest users the current user may know
    # 🤝 اقتراح المستخدمين الذين قد يعرفهم المستخدم الحالي
    # 🧑‍🤝‍🧑 السيريالايزر يقوم بتحويل قائمة المستخدمين الذين قد يعرفهم المستخدم إلى صيغة JSON
    serializer = UserSerializer(request.user.people_you_may_know.all(), many=True)
    # print("🤝 Suggest users", serializer)

    # 📤 إرجاع البيانات كاستجابة JSON
    return JsonResponse(serializer.data, safe=False)


# 🌐 واجهة برمجية لمعالجة وتحديث حالة طلب الصداقة
@api_view(["POST"])  # 🌐 الدالة تستقبل فقط طلبات POST
def handle_request(request, pk, status):

    # 🛠️ Handle and update the status of a friendship request
    # 🛠️ معالجة وتحديث حالة طلب الصداقة
    # 🛠️ نقوم أولاً بالحصول على المستخدم الذي يتعلق به طلب الصداقة باستخدام الـ pk
    user = User.objects.get(pk=pk)

    # 💡 البحث عن طلب الصداقة الذي أرسله المستخدم الحالي إلى المستخدم المقصود
    # 💡 باستخدام filter لاستخراج طلب الصداقة من قاعدة البيانات.
    friendship_request = FriendshipRequest.objects.filter(
        created_for=request.user, created_by=user
    ).first()  # نستخدم first() لجلب أول طلب صداقة أو None إذا لم يوجد

    # 🔴 إذا لم يتم العثور على طلب صداقة بين المستخدمين
    # 🔴 سنعيد رسالة خطأ بالرمز 404 إذا لم نجد طلب صداقة
    if not friendship_request:
        return JsonResponse({"error": "Friendship request not found"}, status=404)

    # 💬 تحديث حالة طلب الصداقة بناءً على الحالة المرسلة
    # 💬 إذا تم قبول أو رفض طلب الصداقة، سيتم تحديث الحالة وتخزينها
    friendship_request.status = status
    friendship_request.save()

    # 👥 Add each user to the other's friends list if accepted
    # 👥 إضافة كل مستخدم إلى قائمة أصدقاء الآخر إذا تم قبول طلب الصداقة
    # 👥 بعد قبول الطلب، نقوم بإضافة كل مستخدم إلى قائمة أصدقاء الآخر
    if status == "accepted":  # فقط إذا كانت الحالة "مقبول" نقوم بإضافة الأصدقاء
        user.friends.add(request.user)  # إضافة المستخدم الحالي كصديق للمستخدم الآخر
        user.friends_count += 1  # زيادة عدد الأصدقاء للمستخدم الآخر
        user.save()  # حفظ التعديلات
        request_user = request.user
        request_user.friends_count += 1  # زيادة عدد الأصدقاء للمستخدم الحالي
        request_user.save()  # حفظ التعديلات

    # 💬 إرسال رد يتضمن الحالة الحالية للطلب وتأكيد التحديث
    # 💬 يتم إرجاع رسالة توضح أنه تم تحديث حالة الطلب بنجاح
    return JsonResponse({"message": f"Friendship request {status} successfully"})
