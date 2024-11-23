import './assets/main.css'  // استيراد ملف CSS الرئيسي للمشروع

// My Style
import "./assets/scss/style.scss";  // استيراد ملف SCSS الخاص بالتصميم

import { createApp } from 'vue'  // استيراد دالة createApp من Vue لإنشاء التطبيق
import { createPinia } from 'pinia'  // استيراد Pinia لإدارة الحالة (State Management) في Vue

import App from './App.vue'  // استيراد المكون الرئيسي للتطبيق
import router from './router'  // استيراد إعدادات التوجيه (Vue Router)

// Axios  Import
// استيراد مكتبة Axios للتعامل مع طلبات HTTP
import axios from "axios";
axios.defaults.baseURL = "http://127.0.0.1:8000";  // تعيين الـ base URL الخاص بـ Axios

// --------------- PrimeVue Core Configuration ---------------
// Import PrimeVue library configuration
// استيراد إعدادات مكتبة PrimeVue
import PrimeVue from "primevue/config";

// --------------- Popup Services (For Dialogs and Confirmations) ---------------
// Import services for confirmation and dialog popups
// استيراد خدمات النوافذ المنبثقة لتأكيد العمليات وفتح الحوارات
import ConfirmationService from "primevue/confirmationservice";
import DialogService from "primevue/dialogservice";

// Buttons
// استيراد مكونات الأزرار وزر التبديل
import Button from "primevue/button";
import ToggleButton from "primevue/togglebutton";

// --------------- Form Components ---------------
// استيراد مكونات النماذج
import Fluid from "primevue/fluid";
import InputText from "primevue/inputtext";
import Textarea from "primevue/textarea";
import Password from "primevue/password";
import FloatLabel from "primevue/floatlabel";
import Checkbox from "primevue/checkbox";
import RadioButton from "primevue/radiobutton";
import Listbox from "primevue/listbox";
import DatePicker from "primevue/datepicker";
import InputGroup from "primevue/inputgroup";
import InputGroupAddon from "primevue/inputgroupaddon";
import ColorPicker from "primevue/colorpicker";

// --------------- File Components ---------------
// استيراد مكونات تحميل الملفات
import FileUpload from "primevue/fileupload";

// --------------- Menu Components ---------------
// استيراد مكونات القائمة
import Menubar from "primevue/menubar";
import TieredMenu from "primevue/tieredmenu";

// --------------- Image Components ---------------
// استيراد مكونات الصور
import Image from "primevue/image";
import Avatar from "primevue/avatar";
import AvatarGroup from "primevue/avatargroup";

// --------------- Popup Components ---------------
// استيراد مكونات النوافذ المنبثقة مثل Popover و Dialog و Drawer
import Popover from "primevue/popover";
import Dialog from "primevue/dialog";
import Drawer from "primevue/drawer";

// --------------- Panel Components ---------------
// استيراد مكونات اللوحات مثل Fieldset و Stepper
import Fieldset from "primevue/fieldset";
import Stepper from "primevue/stepper";
import StepList from "primevue/steplist";
import StepPanels from "primevue/steppanels";
import StepItem from "primevue/stepitem";
import Step from "primevue/step";
import StepPanel from "primevue/steppanel";

// --------------- Card Components ---------------
// استيراد مكون البطاقات
import Card from "primevue/card";

// --------------- Theme Components ---------------
// استيراد مكونات السمات مثل Noir و ThemeSwitcher
import Noir from "./presets/Noir.js";
import ThemeSwitcher from "./components/Theme/ThemeSwitcher.vue";

// --------------- Notification Components ---------------
// استيراد مكونات التنبيهات مثل Toast و Message
import Toast from "primevue/toast";
import ToastService from "primevue/toastservice";
import Message from "primevue/message";

// --------------- Icon Components ---------------
// استيراد مكونات الأيقونات
import IconField from "primevue/iconfield";
import InputIcon from "primevue/inputicon";

// --------------- Editor Components ---------------
// استيراد مكون محرر النصوص الغني (Quill-based)
import Editor from "primevue/editor";

// --------------- Table Components ---------------
// استيراد مكونات الجدول لعرض البيانات
import DataTable from "primevue/datatable";
import Column from "primevue/column";
import ColumnGroup from "primevue/columngroup";  // اختياري
import Row from "primevue/row";  // اختياري

// --------------- Placeholder Components ---------------
// استيراد مكون Skeleton للتحميل المؤقت
import Skeleton from "primevue/skeleton";

// --------------- Badge Components ---------------
// استيراد مكونات الشارات
import Badge from "primevue/badge";
import OverlayBadge from "primevue/overlaybadge";

// --------------- Carousel Components ---------------
// استيراد مكون Carousel لعرض الصور أو المحتوى بشكل دوار
import Carousel from 'primevue/carousel';

// --------------- Tag Components ---------------
// استيراد مكون Tag
import Tag  from 'primevue/tag';

// --------------- DataView Components ---------------
// استيراد مكون DataView لعرض البيانات بطريقة مرنة
import DataView from 'primevue/dataview';

// --------------- Paginator Components ---------------
// استيراد مكون Paginator للتنقل بين الصفحات
import Paginator from 'primevue/paginator';

// --------------- Styles ---------------
// استيراد الأنماط الخاصة بـ PrimeVue و Tailwind CSS
import "primeicons/primeicons.css";
import "tailwindcss/tailwind.css";

// Font Awesome
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { library } from "@fortawesome/fontawesome-svg-core";
import { fas } from "@fortawesome/free-solid-svg-icons";
import { fab } from "@fortawesome/free-brands-svg-icons";
import { far } from "@fortawesome/free-regular-svg-icons";
// إضافة أيقونات Font Awesome إلى مكتبة SVG
library.add(fas, far, fab);

const app = createApp(App)

app.use(createPinia())  // تفعيل Pinia لإدارة الحالة
app.use(router, axios);  // تفعيل التوجيه وAxios

// تعريف مكون FontAwesome
// eslint-disable-next-line vue/multi-word-component-names
app.component("fa", FontAwesomeIcon);

// --------------- Initialize PrimeVue ---------------
app.use(PrimeVue, {
  theme: {
    preset: Noir,  // تعيين السمة المبدئية
    options: {
      prefix: "p",
      darkModeSelector: ".p-dark",
      cssLayer: false
    }
  }
});

// تهيئة وإضافة الخدمات
app.use(ConfirmationService);
app.use(DialogService);
app.use(ToastService);

// --------------- Register Components ---------------
app.component("prime_button", Button);
app.component("ThemeSwitcher", ThemeSwitcher);
app.component("prime_fluid", Fluid);
app.component("prime_input_text", InputText);
app.component("prime_textarea", Textarea);
app.component("prime_input_password", Password);
app.component("prime_float_label", FloatLabel);
app.component("prime_check_box", Checkbox);
app.component("prime_radio_button", RadioButton);
app.component("prime_list_box", Listbox);
app.component("prime_date_picker", DatePicker);
app.component("prime_input_group", InputGroup);
app.component("prime_input_group_addon", InputGroupAddon);
app.component("prime_file_upload", FileUpload);
app.component("prime_toggle_button", ToggleButton);
app.component("prime_color_picker", ColorPicker);

// مكونات القائمة
app.component("prime_menubar", Menubar);
app.component("prime_tiered_menu", TieredMenu);

// مكونات الصور
app.component("prime_image", Image);
app.component("prime_avatar", Avatar);
app.component("prime_avatar_group", AvatarGroup);

// مكونات البطاقة
app.component("prime_card", Card);

// مكونات النوافذ المنبثقة
app.component("prime_popover", Popover);
app.component("prime_dialog", Dialog);
app.component("prime_drawer", Drawer);

// مكونات اللوحات
app.component("prime_fieldset", Fieldset);
app.component("prime_stepper", Stepper);
app.component("prime_steplist", StepList);
app.component("prime_steppanels", StepPanels);
app.component("prime_stepitem", StepItem);
app.component("prime_step", Step);
app.component("prime_steppanel", StepPanel);

// مكونات التنبيهات
app.component("prime_toast", Toast);
app.component("prime_message", Message);

// مكونات الأيقونات
app.component("prime_icon_field", IconField);
app.component("prime_input_icon", InputIcon);

// مكون المحرر
app.component("prime_editor", Editor);

// مكونات الجدول
app.component("prime_data_table", DataTable);
app.component("prime_column", Column);
app.component("prime_column_group", ColumnGroup);
app.component("prime_row", Row);

// مكونات التحميل المؤقت
app.component("prime_skeleton", Skeleton);

// مكونات الشارات
app.component("prime_badge", Badge);
app.component("prime_overlay_badge", OverlayBadge);

// مكون Carousel
app.component("prime_carousel", Carousel);

// مكون Tag
app.component("prime_tag", Tag);

// مكونات DataView
app.component("prime_data_view", DataView);

// مكون Paginator
app.component("prime_paginator", Paginator);

app.mount('#app')  // تشغيل التطبيق على العنصر #app
