// Page [ account/account_vue/src/stores/user.js ]
import { defineStore } from "pinia"; // 📦 استيراد مكتبة Pinia لإنشاء المخزن
import axios from "axios"; // 📡 استيراد مكتبة axios لإجراء طلبات HTTP

// تعريف المخزن لاستخدامه مع Pinia
export const useUserStore = defineStore({
  id: "user", // 🎭 تعريف اسم المخزن الذي سيتم تخزينه
  state: () => ({
    user: {
      isAuthenticated: false, // 🛑 حالة المصادقة، افتراضيًا غير مصادق عليه
      id: null, // 🆔 معرّف المستخدم
      name: null, // 🏷️ اسم المستخدم
      surname: null, // 🏷️ لقب المستخدم
      email: null, // 📧 البريد الإلكتروني
      date_of_birth: null, // 📅 تاريخ الميلاد
      access: null, // 🔑 رمز الوصول
      refresh: null, // 🔄 رمز التحديث
      friends_count: 0, // 📋 عدد الأصدقاء
      gender: null, // 👤 جنس المستخدم
      get_avatar: null, // 🖼️ صورة الملف الشخصي
      get_cover: null, // 🖼️ صورة الغلاف
      task_count: 0 // 📋 عدد المهام
    }
  }),
  actions: {
    // 🔄 تهيئة المخزن
    initStore() {
      if (localStorage.getItem("user.access")) {
        // إذا كان المستخدم قد سجل دخوله مسبقًا
        this.user.isAuthenticated = true;
        this.user.id = localStorage.getItem("user.id");
        this.user.name = localStorage.getItem("user.name");
        this.user.surname = localStorage.getItem("user.surname");
        this.user.email = localStorage.getItem("user.email");
        this.user.date_of_birth = localStorage.getItem("user.date_of_birth");
        this.user.gender = localStorage.getItem("user.gender");
        this.user.get_avatar = localStorage.getItem("user.get_avatar");
        this.user.get_cover = localStorage.getItem("user.get_cover");
        this.user.access = localStorage.getItem("user.access");
        this.user.refresh = localStorage.getItem("user.refresh");
        this.user.friends_count = localStorage.getItem("user.friends_count");
        this.user.task_count = localStorage.getItem("user.task_count");
        this.refreshToken(); // تحديث الرمز عند التهيئة
      }
    },
    // 🔑 تعيين رموز الوصول والتحديث
    setToken(data) {
      this.user.access = data.access;
      this.user.refresh = data.refresh;
      this.user.isAuthenticated = true;
      localStorage.setItem("user.access", data.access);
      localStorage.setItem("user.refresh", data.refresh);
    },
    // ❌ إزالة الرموز ومسح بيانات المستخدم
    removeToken() {
      this.user.refresh = null;
      this.user.access = null;
      this.user.isAuthenticated = false;
      this.user.id = null;
      this.user.name = null;
      this.user.surname = null;
      this.user.email = null;
      this.user.date_of_birth = null;
      this.user.gender = null;
      this.user.get_avatar = null;
      this.user.get_cover = null;
      this.user.friends_count = null;
      this.user.task_count = null;

      // مسح البيانات من localStorage
      localStorage.setItem("user.access", "");
      localStorage.setItem("user.refresh", "");
      localStorage.setItem("user.id", "");
      localStorage.setItem("user.name", "");
      localStorage.setItem("user.surname", "");
      localStorage.setItem("user.email", "");
      localStorage.setItem("user.date_of_birth", "");
      localStorage.setItem("user.gender", "");
      localStorage.setItem("user.get_avatar", "");
      localStorage.setItem("user.get_cover", "");
      localStorage.setItem("user.friends_count", "");
      localStorage.setItem("user.task_count", "");
    },
    // ✍️ تعيين بيانات المستخدم في الحالة و localStorage
    setUserInfo(user) {
      this.user.id = user.id;
      this.user.name = user.name;
      this.user.surname = user.surname;
      this.user.email = user.email;
      this.user.date_of_birth = user.date_of_birth;
      this.user.gender = user.gender;
      this.user.get_avatar = user.get_avatar;
      this.user.get_cover = user.get_cover;
      this.user.friends_count = user.friends_count;
      this.user.task_count = user.task_count;

      // حفظ البيانات في localStorage
      localStorage.setItem("user.id", this.user.id);
      localStorage.setItem("user.name", this.user.name);
      localStorage.setItem("user.surname", this.user.surname);
      localStorage.setItem("user.email", this.user.email);
      localStorage.setItem("user.date_of_birth", this.user.date_of_birth);
      localStorage.setItem("user.gender", this.user.gender);
      localStorage.setItem("user.get_avatar", this.user.get_avatar);
      localStorage.setItem("user.get_cover", this.user.get_cover);
      localStorage.setItem("user.friends_count", this.user.friends_count);
      localStorage.setItem("user.task_count", this.user.task_count);
    },
    // 🔄 تحديث رمز الوصول
    refreshToken() {
      console.log("Attempting to refresh token:", this.user.refresh);
      // إرسال طلب لتحديث رمز الوصول
      axios
        .post("/api/refresh/", {
          refresh: this.user.refresh
        })
        .then((response) => {
          this.user.access = response.data.access;
          localStorage.setItem("user.access", response.data.access);
          axios.defaults.headers.common["Authorization"] =
            "Bearer " + response.data.access; // إعداد الرمز في رأس الطلب
        })
        .catch((error) => {
          console.log(error);
          this.removeToken(); // إزالة الرموز في حال حدوث خطأ
        });
    }
  }
});
