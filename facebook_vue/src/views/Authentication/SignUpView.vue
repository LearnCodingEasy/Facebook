<template>
  <div class="wrapper_signup_page">
    <div class="inner_signup_page">
      <div class="container">
        <h1 class="mb-6 text-2xl">Sign up</h1>
        <form class="space-y-6" v-on:submit.prevent="submitForm">
          <div class="row">
            <div class="col">
              <!-- Name -->
              <div class="mb-3">
                <label class="form-label" for="name">Name</label><br />
                <input
                  type="text"
                  id="name"
                  v-model="form.name"
                  placeholder="Your Full Name"
                  class="form-control"
                />
              </div>
              <!-- Personal Phone -->
              <div class="mb-3">
                <label class="form-label" for="personal_phone">Personal Phone</label><br />
                <input
                  type="number"
                  id="personal_phone"
                  v-model="form.personal_phone"
                  placeholder="Your Personal Phone"
                  class="form-control"
                />
              </div>
              <!-- Public Phone -->
              <div class="mb-3">
                <label class="form-label" for="public_phone">Public Phone</label><br />
                <input
                  type="number"
                  id="public_phone"
                  v-model="form.public_phone"
                  placeholder="Your Public Phone"
                  class="form-control"
                />
              </div>
              <p class="font-bold">
                Already have an account?
                <RouterLink to="/loginView" class="underline">Click here </RouterLink>
                to log in!
              </p>
            </div>
            <div class="col">
              <!-- Address -->
              <div class="mb-3">
                <label class="form-label" for="address">Address</label><br />
                <input
                  type="text"
                  id="address"
                  v-model="form.address"
                  placeholder="Your Address"
                  class="form-control"
                />
              </div>
              <!-- E-mail -->
              <div class="mb-3">
                <label class="form-label" for="email">E-mail</label><br />
                <input
                  type="email"
                  id="email"
                  v-model="form.email"
                  placeholder="Your E Mail "
                  class="form-control"
                />
              </div>
              <!-- Password -->
              <div class="mb-3">
                <label class="form-label" for="password1">Password</label><br />
                <input
                  type="password"
                  id="password1"
                  v-model="form.password1"
                  placeholder="Your password"
                  class="form-control"
                />
              </div>
              <!-- Repeat password -->
              <div>
                <label class="form-label" for="password2">Repeat password</label><br />
                <input
                  type="password"
                  id="password2"
                  v-model="form.password2"
                  placeholder="Repeat your password"
                  class="form-control"
                />
              </div>
              <!-- Errors -->
              <template v-if="errors.length > 0">
                <div class="alert alert-danger" role="alert">
                  <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                </div>
              </template>
            </div>
            <div class="col-12 mt-3">
              <!-- Sign up -->
              <div class="d-grid gap-2">
                <button class="w-50 m-auto d-block btn btn-primary">Sign up</button>
              </div>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
// eslint-disable-next-line no-unused-vars
import { RouterLink } from 'vue-router'

export default {
  name: 'SignupView',
  setup() {
    return {}
  },
  data() {
    return {
      form: {
        email: '',
        name: '',
        personal_phone: '',
        public_phone: '',
        address: '',
        password1: '',
        password2: ''
      },
      errors: []
    }
  },
  methods: {
    submitForm() {
      this.errors = []
      if (this.form.email === '') {
        this.errors.push('Your e-mail is missing')
      }
      if (this.form.name === '') {
        this.errors.push('Your name is missing')
      }
      if (this.form.personal_phone === '') {
        this.errors.push('Your Personal Phone is missing')
      }
      if (this.form.public_phone === '') {
        this.errors.push('Your Public Phone is missing')
      }
      if (this.form.address === '') {
        this.errors.push('Your Address is missing')
      }
      if (this.form.password1 === '') {
        this.errors.push('Your password is missing')
      }
      if (this.form.password1 !== this.form.password2) {
        this.errors.push('The password does not match')
      }
      if (this.errors.length === 0) {
        axios
          .post('/api/signup/', this.form)
          .then((response) => {
            if (response.data.message === 'success') {
              this.toastStore.showToast(
                5000,
                'The user is registered. Please activate your account by clicking your email link.',
                'bg-emerald-500'
              )
              this.form.email = ''
              this.form.name = ''
              this.form.personal_phone = ''
              this.form.public_phone = ''
              this.form.address = ''
              this.form.password1 = ''
              this.form.password2 = ''
              this.$router.push('/loginView')
            } else {
              const data = JSON.parse(response.data.message)
              for (const key in data) {
                this.errors.push(data[key][0].message)
              }
              this.toastStore.showToast(
                5000,
                'Something went wrong. Please try again',
                'bg-red-300'
              )
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
  cd tom_and_jerry_vue
  npm run dev
  __________________________________________
  Name           = Hossam Rashad
  Personal Phone = 01091642528
  Public Phone   = 01101853042
  Address        = Egypt
  E-mail         = learncodingeasy@yahoo.com
  Password       = zxc123456789
  __________________________________________
  Name           = Hossam Rashad
  Personal Phone = 01091642528
  Public Phone   = 01101853042
  Address        = Egypt
  E-mail         = bibo2010508@yahoo.com
  Password       = zxc123456789
-->
