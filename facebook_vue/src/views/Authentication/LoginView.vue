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
              <form class="form_login" v-on:submit.prevent="submitForm">
                <prime_card class="p-3">
                  <template #header>
                    <div class="my-5 font-bold text-3xl">Log in</div>
                  </template>

                  <template #title>
                    <prime_float_label class="mt-5">
                      <prime_input_text
                        id="emailAddress"
                        v-model="form.email"
                        class="block w_100"
                      />
                      <label for="emailAddress" class="text-base">Your E-mail Address</label>
                    </prime_float_label>
                  </template>
                  <template #content>
                    <prime_float_label class="mt-5">
                      <prime_input_password
                        id="password"
                        v-model="form.password"
                        class=""
                        :feedback="false"
                      />
                      <label for="password">password</label>
                    </prime_float_label>
                  </template>
                  <template #footer>
                    <div class="row">
                      <!-- Errors -->
                      <template v-if="errors.length > 0">
                        <div class="alert alert-danger" role="alert">
                          <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                        </div>
                      </template>

                      <!-- Login -->
                      <div class="mt-3">
                        <prime_button
                          type="button"
                          label="Log In"
                          severity="info"
                          class="!block w_100 bg_facebook_color_1_important"
                        />
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
                <form class="space-y-6" v-on:submit.prevent="submitFormSignup">
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
                        <div>
                          v-model="form.name"
                          <prime_input_text placeholder="First name" v-model="formSignup.name" />
                        </div>
                        <div>
                          <prime_input_text placeholder="Surname" />
                        </div>
                        <div class="col-span-full">
                          <prime_input_text placeholder="Mobile number or email address" />
                        </div>
                        <div class="col-span-full">
                          <prime_input_password placeholder="New Password" />
                        </div>
                        <div class="col-span-full">Date of birth</div>
                        <div class="col-span-full">
                          <div class="flex flex-col md:flex-row gap-2">
                            <prime_input_group>
                              <prime_date_picker v-model="date" :placeholder="date" />
                            </prime_input_group>
                            <prime_input_group>
                              <prime_date_picker v-model="date" :placeholder="date" />
                            </prime_input_group>
                            <prime_input_group>
                              <prime_date_picker v-model="date" :placeholder="date" />
                            </prime_input_group>
                          </div>
                        </div>
                        <div class="col-span-full">Gender</div>
                        <div class="flex flex-col md:flex-row gap-2">
                          <prime_input_group>
                            <prime_check_box
                              v-model="gender"
                              inputId="ingredient1"
                              name="gender"
                              value="Female"
                            />
                            <label for="ingredient1" class="ml-2"> Female </label>
                          </prime_input_group>
                          <prime_input_group>
                            <prime_check_box
                              v-model="gender"
                              inputId="ingredient2"
                              name="gender"
                              value="Male"
                            />
                            <label for="ingredient2" class="ml-2"> Male </label>
                          </prime_input_group>

                          <prime_input_group>
                            <prime_check_box
                              v-model="gender"
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
                      <prime_button
                        label="Signup"
                        severity="success"
                        class="d_block_important mt-5 mb-3 mx-auto w_50"
                      />
                    </div>
                  </prime_dialog>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
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
      form: {
        email: '',
        password: ''
      },
      errors: [],
      visible: false,
      // For Date
      date: null,
      // Signup
      formSignup: {
        email: '',
        name: '',
        personal_phone: '',
        public_phone: '',
        address: '',
        password1: '',
        password2: ''
      },
      errorsSignup: []
    }
  },
  methods: {
    async submitForm() {
      this.errors = []
      if (this.form.email === '') {
        this.errors.push('Your e-mail is missing')
      }
      if (this.form.password === '') {
        this.errors.push('Your password is missing')
      }
      if (this.errors.length === 0) {
        await axios
          .post('/api/login/', this.form)
          .then((response) => {
            this.userStore.setToken(response.data)
            axios.defaults.headers.common['Authorization'] = 'Bearer ' + response.data.access
          })
          .catch((error) => {
            console.log('error', error)

            this.errors.push('The email or password is incorrect! Or the user is not activated!')
          })
      }
      if (this.errors.length === 0) {
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
      this.errors = []
      if (this.formSignup.email === '') {
        this.errors.push('Your e-mail is missing')
      }
      if (this.formSignup.name === '') {
        this.errors.push('Your name is missing')
      }
      if (this.formSignup.personal_phone === '') {
        this.errors.push('Your Personal Phone is missing')
      }
      if (this.formSignup.public_phone === '') {
        this.errors.push('Your Public Phone is missing')
      }
      if (this.form.address === '') {
        this.errors.push('Your Address is missing')
      }
      if (this.formSignup.password1 === '') {
        this.errors.push('Your password is missing')
      }
      if (this.formSignup.password1 !== this.formSignup.password2) {
        this.errors.push('The password does not match')
      }
      if (this.errorsSignup.length === 0) {
        axios
          .post('/api/signup/', this.formSignup)
          .then((response) => {
            if (response.data.message === 'success') {
              // this.toastStore.showToast(
              //   5000,
              //   'The user is registered. Please activate your account by clicking your email link.',
              //   'bg-emerald-500'
              // )
              this.formSignup.email = ''
              this.formSignup.name = ''
              this.formSignup.personal_phone = ''
              this.formSignup.public_phone = ''
              this.formSignup.address = ''
              this.formSignup.password1 = ''
              this.formSignup.password2 = ''
              // this.$router.push('/loginView')
            } else {
              const data = JSON.parse(response.data.message)
              for (const key in data) {
                this.errors.push(data[key][0].message)
              }
              // this.toastStore.showToast(
              //   5000,
              //   'Something went wrong. Please try again',
              //   'bg-red-300'
              // )
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
