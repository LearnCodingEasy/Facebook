<template>
  <div class="wrapper_login_page">
    <div class="inner_login_page">
      <div class="container">
        <div class="flex justify-center align-middle w_80 m-auto">
          <div class="grid grid-cols-3 gap-4 w_95">
            <div class="wrapper_text_login col-span-2">
              <div class="inner">
                <div class="title">facebook</div>
                <div class="subtitle">
                  Facebook helps you connect and share <br />
                  with the people in your life.
                </div>
              </div>
            </div>
            <div class="wrapper_form_login shadow-2xl rounded-lg">
              <!-- Log in -->
              <form class="form_login" v-on:submit.prevent="submitFormLogin">
                <prime_card class="p-3">
                  <template #header>
                    <div class="my-5 font-bold text-3xl">Log in</div>
                  </template>
                  <template #title>
                    <prime_float_label class="mt-5">
                      <prime_input_text
                        id="emailAddress"
                        v-model="formLogin.email"
                        class="block w_100"
                      />
                      <label for="emailAddress" class="text-base">Your E-mail Address</label>
                    </prime_float_label>
                  </template>
                  <template #content>
                    <prime_float_label class="mt-5">
                      <prime_input_password
                        id="password"
                        v-model="formLogin.password"
                        :feedback="false"
                      />
                      <label for="password">password</label>
                    </prime_float_label>
                  </template>
                  <template #footer>
                    <div class="row">
                      <!-- Errors -->
                      <template v-if="errorsLogin.length > 0">
                        <prime_toast></prime_toast>
                      </template>
                      <!-- Login -->
                      <div class="mt-3">
                        <button
                          type="submit"
                          class="d_block_important mt-5 mb-3 mx-auto w_100 bg-blue-500 py-3 px-5 rounded text-white"
                          @click.prevent="submitFormLogin"
                        >
                          Log In
                        </button>
                        <a href="#" class="text-blue-600 mx-auto my-4 block text-center"
                          >Forgotten password?</a
                        >
                        <hr />
                        <!-- Button Signup -->
                        <prime_button
                          label="Create new account"
                          severity="success"
                          @click="visible = true"
                          class="d_block_important my-5 mx-auto"
                        />
                      </div>
                    </div>
                  </template>
                </prime_card>
              </form>
              <!-- Signup -->
              <div class="card flex justify-center">
                <!-- @submit.prevent="submitFormSignup" -->
                <form class="space-y-6">
                  <!-- <form class="space-y-6" @submit.prevent="submitFormSignup"> -->
                  <prime_dialog
                    v-model:visible="visible"
                    modal
                    header="Sign Up"
                    :style="{ width: '25rem' }"
                  >
                    <span class="text-surface-500 dark:text-surface-400 block mb-8"
                      >It's quick and easy.</span
                    >
                    <prime_fluid>
                      <div class="grid grid-cols-2 gap-4">
                        <!-- First name -->
                        <div>
                          <prime_input_text placeholder="First name" v-model="formSignup.name" />
                        </div>
                        <!-- Surname -->
                        <div>
                          <prime_input_text placeholder="Surname" v-model="formSignup.surname" />
                        </div>
                        <!-- Mobile number or email address -->
                        <div class="col-span-full">
                          <prime_input_text
                            placeholder="Mobile number or email address"
                            v-model="formSignup.email"
                          />
                        </div>
                        <!-- password1 -->
                        <div class="col-span-full">
                          <prime_input_password
                            placeholder="New Password"
                            v-model="formSignup.password1"
                          />
                        </div>
                        <!-- password2 -->
                        <div class="col-span-full">
                          <prime_input_password
                            placeholder="Repeat password"
                            v-model="formSignup.password2"
                          />
                        </div>
                        <!-- Date of birth -->
                        <div class="col-span-full">Date of birth</div>
                        <div class="col-span-full">
                          <div class="flex flex-col md:flex-row gap-2">
                            <!-- Day -->
                            <prime_input_group>
                              <prime_date_picker v-model="day" view="day" dateFormat="dd" />
                            </prime_input_group>
                            <!-- Month -->
                            <prime_input_group>
                              <prime_date_picker v-model="month" view="month" dateFormat="mm" />
                            </prime_input_group>
                            <!-- Year -->
                            <prime_input_group>
                              <prime_date_picker v-model="year" view="year" dateFormat="yy" />
                            </prime_input_group>
                          </div>
                        </div>
                        <!-- Gender -->
                        <div class="col-span-full">Gender</div>
                        <div class="flex flex-col md:flex-row gap-2">
                          <prime_input_group>
                            <prime_check_box
                              v-model="formSignup.gender"
                              inputId="ingredient1"
                              name="gender"
                              value="Female"
                            />
                            <label for="ingredient1" class="ml-2"> Female </label>
                          </prime_input_group>
                          <prime_input_group>
                            <prime_check_box
                              v-model="formSignup.gender"
                              inputId="ingredient2"
                              name="gender"
                              value="Male"
                            />
                            <label for="ingredient2" class="ml-2"> Male </label>
                          </prime_input_group>

                          <prime_input_group>
                            <prime_check_box
                              v-model="formSignup.gender"
                              inputId="ingredient3"
                              name="gender"
                              value="Custom"
                            />
                            <label for="ingredient3" class="ml-2"> Custom </label>
                          </prime_input_group>
                        </div>
                      </div>
                    </prime_fluid>
                    <div class="flex justify-center gap-2">
                      <button
                        type="submit"
                        class="d_block_important mt-5 mb-3 mx-auto w_50 bg-green-500 py-3 px-5 rounded text-white"
                        @click.prevent="submitFormSignup"
                      >
                        Submit
                      </button>
                    </div>
                  </prime_dialog>
                  <!-- Errors -->
                  <template v-if="errorsSignup.length > 0">
                    <prime_toast />
                  </template>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <prime_toast />
  </div>
</template>

<script>
import axios from 'axios'
// eslint-disable-next-line no-unused-vars
import { RouterLink } from 'vue-router'

export default {
  name: 'loginView',
  setup() {
    return {}
  },
  data() {
    return {
      formLogin: {
        email: '',
        password: ''
      },
      errorsLogin: [],
      // visible Signup
      visible: false,
      // Signup
      formSignup: {
        name: '',
        surname: '',
        email: '',
        date_of_birth: null,
        gender: '',
        password1: '',
        password2: ''
      },
      day: '',
      month: '',
      year: '',
      errorsSignup: []
    }
  },
  methods: {
    async submitFormLogin() {
      console.log(`Yes`)
      this.errorsLogin = []
      if (this.formLogin.email === '') {
        this.$toast.add({
          severity: 'error',
          summary: 'User Name missing',
          detail: 'Your name is missing',
          life: 3000
        })
        this.errorsLogin.push('Your e-mail is missing')
      }
      if (this.formLogin.password === '') {
        this.$toast.add({
          severity: 'error',
          summary: 'User password is missing',
          detail: 'Your password is missing',
          life: 3000
        })
        this.errorsLogin.push('Your password is missing')
      }
      if (this.errorsLogin.length === 0) {
        await axios
          .post('/api/login/', this.formLogin)
          .then((response) => {
            this.userStore.setToken(response.data)
            console.log('response.data: ', response.data)
            axios.defaults.headers.common['Authorization'] = 'Bearer ' + response.data.access
          })
          .catch((error) => {
            console.log('error', error)

            this.errors.push('The email or password is incorrect! Or the user is not activated!')
          })
      }
      if (this.errorsLogin.length === 0) {
        await axios
          .get('/api/me/')
          .then((response) => {
            this.userStore.setUserInfo(response.data)
            this.$router.push('/')
          })
          .catch((error) => {
            console.log('error', error)
          })
      }
    },
    submitFormSignup() {
      this.errorsSignup = []

      // استخراج اليوم، الشهر، والسنة من كائنات Date وتنسيقها
      const day = this.day.getDate().toString().padStart(2, '0')
      const month = (this.month.getMonth() + 1).toString().padStart(2, '0')
      const year = this.year.getFullYear()

      const formattedDate = `${year}-${month}-${day}`
      this.formSignup.date_of_birth = formattedDate

      if (this.formSignup.name === '') {
        this.$toast.add({
          severity: 'error',
          summary: 'User Name missing',
          detail: 'Your name is missing',
          life: 3000
        })
        this.errorsSignup.push('Your name is missing')
      }
      if (this.formSignup.surname === '') {
        this.$toast.add({
          severity: 'error',
          summary: 'User Surname missing',
          detail: 'Your Surname is missing',
          life: 3000
        })
        this.errorsSignup.push('Your surname is missing')
      }
      if (this.formSignup.email === '') {
        this.$toast.add({
          severity: 'error',
          summary: 'User Is missing',
          detail: 'Your e-mail is missing',
          life: 3000
        })
        this.errorsSignup.push('Your e-mail is missing')
      }
      if (this.formSignup.password1 === '') {
        this.$toast.add({
          severity: 'error',
          summary: 'User passwordIs missing',
          detail: 'Your password is missing',
          life: 3000
        })
        this.errorsSignup.push('Your password is missing')
      }
      if (this.formSignup.password1 !== this.formSignup.password2) {
        this.$toast.add({
          severity: 'error',
          summary: 'User  password does not match',
          detail: 'Your password  does not match',
          life: 3000
        })
        this.errorsSignup.push('The password does not match')
      }
      if (this.errorsSignup.length === 0) {
        axios
          .post('/api/signup/', this.formSignup)
          .then((response) => {
            if (response.data.message === 'success') {
              this.$toast.add({
                severity: 'success',
                summary: 'User Is Registered',
                detail: 'Please activate your account by clicking your email link',
                life: 3000
              })
              this.formSignup.name = ''
              this.formSignup.surname = ''
              this.formSignup.email = ''
              this.formSignup.date_of_birth = ''
              this.formSignup.gender = ''
              this.formSignup.password1 = ''
              this.formSignup.password2 = ''
              // this.$router.push('/loginView')
              window.location.reload()
            } else {
              const data = JSON.parse(response.data.message)
              this.$toast.add({
                severity: 'error',
                summary: 'Error Message',
                detail: 'Message Content Something went wrong. Please try again',
                life: 6000
              })
              for (const key in data) {
                this.errors.push(data[key][0].message)
              }
              console.log(`Bad`, this.formSignup.date_of_birth)
              console.log(`Day`, this.day)
              console.log(`month`, this.month)
              console.log(`year`, this.year)
            }
          })
          .catch((error) => {
            console.log('error', error)
          })
      }
    }
  }
}
</script>

<!-- 
  Name           = Hossam Rashad
  Personal Phone = 01091642528
  Public Phone   = 01101853042
  Address        = Egypt
  E-mail         = learncodingeasy@yahoo.com
  Password       = zxc123456789
-->
