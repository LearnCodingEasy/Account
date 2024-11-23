// استيراد الدوال والأنماط من مكتبة node:url
import { fileURLToPath, URL } from "node:url";

// استيراد دالة defineConfig من Vite لضبط إعدادات البناء
import { defineConfig } from "vite";

// استيراد المكون الإضافي Vue من Vite
import vue from "@vitejs/plugin-vue";

// استيراد مكون VitePWA لإضافة ميزات تطبيق الويب التقدمي (PWA)
import { VitePWA } from "vite-plugin-pwa";

// تصدير الإعدادات الأساسية لمشروع Vite باستخدام defineConfig
export default defineConfig({
  plugins: [
    // إضافة مكون Vue لتوجيه ملفات .vue
    vue(),
    // إضافة إعدادات PWA لتفعيل ميزات التطبيق التقدمي
    VitePWA({
      // تفعيل التسجيل التلقائي لـ Service Worker (التحديث التلقائي)
      registerType: "autoUpdate",
      workbox: {
        // أنماط الملفات التي سيتم تخزينها في الكاش
        globPatterns: ["**/*.{js,css,html,ico,png,svg}"],
        clientsClaim: true, // تأكيد أن الـ Service Worker سيدير الطلبات
        skipWaiting: true, // تخطي انتظار التثبيت
        cleanupOutdatedCaches: false, // عدم تنظيف الكاشات القديمة
        offlineGoogleAnalytics: true, // تمكين تحليلات جوجل للعمل أثناء عدم الاتصال
        sourcemap: true, // تضمين الـ sourcemaps
        runtimeCaching: [
          {
            // تحديد الأنماط التي يجب أن يتعامل معها Service Worker
            urlPattern: ({ request }) =>
              request.destination === "document" ||
              request.destination === "script" ||
              request.destination === "style" ||
              request.destination === "image" ||
              request.destination === "font",
            handler: "StaleWhileRevalidate", // استخدام استراتيجية الكاش التي تعتمد على إعادة التحقق من البيانات
            options: {
              cacheName: "assets-cache", // اسم الكاش
              expiration: {
                maxEntries: 100, // الحد الأقصى لعدد الملفات في الكاش
                maxAgeSeconds: 60 * 60 * 24 * 30, // مدة صلاحية الكاش (30 يوم)
              },
            },
          },
        ],
      },
      devOptions: {
        enabled: true, // تمكين إعدادات PWA أثناء التطوير
      },
      injectRegister: "auto", // إضافة التسجيل التلقائي للـ Service Worker
      includeAssets: ["**/*"], // تضمين جميع الملفات في الكاش
      manifest: {
        // بيانات التطبيق مثل الاسم، اللون، الأيقونات
        name: "Script Youtube",
        short_name: "Script Youtube",
        description: "My Awesome App Script Youtube",
        theme_color: "#ffffff", // لون خلفية التطبيق
        icons: [
          // الأيقونات بأحجام متعددة لاستخدامها في تثبيت التطبيق على الهواتف
          {
            src: "./images/icons/account_icon_72x72.png",
            type: "image/png",
            sizes: "72x72",
            purpose: "any maskable", // تستخدم لتطبيقات الويب التقدمي
          },
          {
            src: "./images/icons/account_icon_96x96.png",
            type: "image/png",
            sizes: "96x96",
            purpose: "any maskable",
          },
          {
            src: "./images/icons/account_icon_128x128.png",
            type: "image/png",
            sizes: "128x128",
            purpose: "any maskable",
          },
          {
            src: "./images/icons/account_icon_144x144.png",
            type: "image/png",
            sizes: "144x144",
            purpose: "any maskable",
          },
          {
            src: "./images/icons/account_icon_152x152.png",
            type: "image/png",
            sizes: "152x152",
            purpose: "any maskable",
          },
          {
            src: "./images/icons/account_icon_192x192.png",
            type: "image/png",
            sizes: "192x192",
            purpose: "any maskable",
          },
          {
            src: "./images/icons/account_icon_384x384.png",
            type: "image/png",
            sizes: "384x384",
            purpose: "any maskable",
          },
          {
            src: "./images/icons/account_icon_512x512.png",
            type: "image/png",
            sizes: "512x512",
            purpose: "any maskable",
          },
        ],
        screenshots: [
          // لقطة شاشة لعرض واجهة التطبيق في متجر التطبيقات
          {
            src: "./images/screenshots/screenshots.png",
            sizes: "640x480",
            type: "image/png",
            form_factor: "wide", // يمكن تغييره إلى "narrow" للعرض الضيق
          },
        ],
      },
    }),
  ],
  // تحديد الملفات التي يجب على Vite التعامل معها
  content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  resolve: {
    // تعيين الاختصارات لاستيراد الملفات من مجلد src
    alias: {
      "@": fileURLToPath(new URL("./src", import.meta.url)),
    },
  },
});
