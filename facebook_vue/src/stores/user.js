// Page [ facebook/facebook_vue/src/stores/user.js ]
// `pinia`من مكتبة `defineStore` استيراد 
import { defineStore } from 'pinia'
// HTTP للتعامل مع طلبات `axios` استيراد 
import axios from 'axios'
// `defineStore` باستخدام `useUserStore` تعريف وتصدير
export const useUserStore = defineStore({
      // (store) تعيين معرّف فريد للمخزن 
    id: 'user',
    // (store) تعيين معرّف فريد للمخزن 
    state: () => ({
        // تحديد الخصائص الافتراضية للمستخدم
        user: {
            // هل المستخدم مسجل دخول أم لا
            isAuthenticated: false, 
            // معرّف المستخدم
            id: null,
            // اسم المستخدم
            name: null,
            // لقب المستخدم
            surname: null,
            // بريد المستخدم الإلكتروني
            email: null,
            // تاريخ ميلاد المستخدم
            date_of_birth: null,
            // رمز الوصول (Access Token)
            access: null,
            // رمز التجديد (Refresh Token)
            refresh: null,
            // ? 2
            // Profile
            // صورة المستخدم الرمزية (غير مستخدم حالياً)
            avatar: null,
            // personal_phone: null, // هاتف المستخدم الشخصي (غير مستخدم حالياً)
            // public_phone: null,   // هاتف المستخدم العام (غير مستخدم حالياً)
            // address: null,        // عنوان المستخدم (غير مستخدم حالياً)
            // workplace_company: null, // شركة العمل (غير مستخدم حالياً)
            // workplace_position: null, // منصب العمل (غير مستخدم حالياً)
            // workplace_city_town: null, // مدينة أو بلدة العمل (غير مستخدم حالياً)
            // workplace_description: null, // وصف العمل (غير مستخدم حالياً)
            // workplace_time_period: null, // فترة العمل (غير مستخدم حالياً)

            // cover: null           // صورة غلاف المستخدم (غير مستخدم حالياً)
        }
    }),
    // (store) في المخزن (actions) تعريف الإجراءات 
    actions: {
        // إجراء لتهيئة المخزن واستعادة بيانات المستخدم من التخزين المحلي
        initStore() {
            // console.log('initStore', localStorage.getItem('user.access'))
            // إذا كان هناك رمز وصول محفوظ في التخزين المحلي
            if (localStorage.getItem('user.access')) {
                console.log('User has access!')
                // تعيين خصائص المستخدم باستخدام البيانات المخزنة محلياً
                this.user.isAuthenticated = true
                this.user.id = localStorage.getItem('user.id')
                this.user.name = localStorage.getItem('user.name')
                this.user.surname = localStorage.getItem('user.surname')
                this.user.email = localStorage.getItem('user.email')
                this.user.date_of_birth = localStorage.getItem('user.date_of_birth')
                this.user.access = localStorage.getItem('user.access')
                this.user.refresh = localStorage.getItem('user.refresh')
                this.user.avatar = localStorage.getItem('user.avatar')
                // this.user.personal_phone = localStorage.getItem('user.personal_phone')
                // this.user.public_phone = localStorage.getItem('user.public_phone')
                // this.user.address = localStorage.getItem('user.address')
                // this.user.workplace_company = localStorage.getItem('user.workplace_company')
                // this.user.workplace_position = localStorage.getItem('user.workplace_position')
                // this.user.workplace_city_town = localStorage.getItem('user.workplace_city_town')
                // this.user.workplace_description = localStorage.getItem('user.workplace_description')
                // this.user.workplace_time_period = localStorage.getItem('user.workplace_time_period')
                // this.user.cover = localStorage.getItem('user.cover')
                // تحديث رمز الوصول
                this.refreshToken()
                // console.log('Initialized user:', this.user)
            }
        },
        // إجراء لتعيين رموز الوصول والتجديد في المخزن وفي التخزين المحلي
        setToken(data) {
            console.log('setToken', data)
            // تعيين الرموز في المخزن
            this.user.access = data.access
            this.user.refresh = data.refresh
            this.user.isAuthenticated = true
            // تخزين الرموز في التخزين المحلي
            localStorage.setItem('user.access', data.access)
            localStorage.setItem('user.refresh', data.refresh)

            console.log('user.access: ', localStorage.getItem('user.access'))
        },
        // إجراء لإزالة الرموز وتفريغ بيانات المستخدم
        removeToken() {
            console.log('removeToken')
            // إعادة تعيين بيانات المستخدم إلى قيمها الافتراضية
            this.user.refresh = null
            this.user.access = null
            this.user.isAuthenticated = false
            this.user.id = null
            this.user.name = null
            this.user.surname = null
            this.user.email = null
            this.user.date_of_birth = null
            // this.user.personal_phone = null
            // this.user.public_phone = null
            // this.user.address = null
            // this.user.workplace_company = null
            // this.user.workplace_position = null
            // this.user.workplace_city_town = null
            // this.user.workplace_description = null
            // this.user.workplace_time_period = null
            // this.user.cover = null
            // إزالة البيانات المخزنة في التخزين المحلي
            localStorage.setItem('user.access', '')
            localStorage.setItem('user.refresh', '')
            localStorage.setItem('user.id', '')
            localStorage.setItem('user.name', '')
            localStorage.setItem('user.surname', '')
            localStorage.setItem('user.email', '')
            localStorage.setItem('user.date_of_birth', '')
            // ? 2
            // Profile
            this.user.avatar = null
            localStorage.setItem('user.avatar', '')
            // localStorage.setItem('user.personal_phone', '')
            // localStorage.setItem('user.public_phone', '')
            // localStorage.setItem('user.address', '')
            // localStorage.setItem('user.workplace_company', '')
            // localStorage.setItem('user.workplace_position', '')
            // localStorage.setItem('user.workplace_city_town', '')
            // localStorage.setItem('user.workplace_description', '')
            // localStorage.setItem('user.workplace_time_period', '')
            // localStorage.setItem('user.cover', '')
        },
        // إجراء لتحديث بيانات المستخدم وتخزينها في التخزين المحلي
        setUserInfo(user) {
            console.log('setUserInfo', user)
            // تعيين بيانات المستخدم في المخزن
            this.user.id = user.id
            this.user.name = user.name
            this.user.surname = user.surname
            this.user.email = user.email
            this.user.date_of_birth = user.date_of_birth
            // ? 2
            // Profile
            this.user.avatar = user.avatar
            // this.user.personal_phone = user.personal_phone
            // this.user.public_phone = user.public_phone
            // this.user.address = user.address
            // this.user.workplace_company = user.workplace_company
            // this.user.workplace_position = user.workplace_position
            // this.user.workplace_city_town = user.workplace_city_town
            // this.user.workplace_description = user.workplace_description
            // this.user.workplace_time_period = user.workplace_time_period
            // this.user.cover = user.cover

            localStorage.setItem('user.id', this.user.id)
            localStorage.setItem('user.name', this.user.name)
            localStorage.setItem('user.surname', this.user.surname)
            localStorage.setItem('user.email', this.user.email)
            localStorage.setItem('user.date_of_birth', this.user.date_of_birth)
            // ? 2
            // Profile
            localStorage.setItem('user.avatar', this.user.avatar)
            // localStorage.setItem('user.personal_phone', this.user.personal_phone)
            // localStorage.setItem('user.public_phone', this.user.public_phone)
            // localStorage.setItem('user.address', this.user.address)
            // localStorage.setItem('user.workplace_company', this.user.workplace_company)
            // localStorage.setItem('user.workplace_position', this.user.workplace_position)
            // localStorage.setItem('user.workplace_city_town', this.user.workplace_city_town)
            // localStorage.setItem('user.workplace_description', this.user.workplace_description)
            // localStorage.setItem('user.workplace_time_period', this.user.workplace_time_period)
            // localStorage.setItem('user.cover', this.user.cover)
            // console.log('User', this.user)
        },
        // إجراء لتحديث رمز الوصول باستخدام رمز التجديد
        refreshToken() {
            // لتحديث رمز الوصول HTTP إرسال طلب 
            axios.post('/api/refresh/', {
                refresh: this.user.refresh
            })
                .then((response) => {
                    // تحديث رمز الوصول في المخزن والتخزين المحلي
                    this.user.access = response.data.access
                    localStorage.setItem('user.access', response.data.access)
                    // للطلبات المستقبلية Authorization تعيين رأس 
                    axios.defaults.headers.common["Authorization"] = "Bearer " + response.data.access
                })
                .catch((error)=>{
                    // في حالة وجود خطأ، إزالة الرموز
                    console.log(error)
                    this.removeToken()
                })
        },
    }
})