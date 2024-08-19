import { defineStore } from 'pinia'
import axios from 'axios'

export const useUserStore = defineStore({
    id: 'user',

    state: () => ({
        user: {
            isAuthenticated: false,
            id: null,
            name: null,
            surname: null,
            email: null,
            date_of_birth: null,
            access: null,
            refresh: null,
            // personal_phone: null,
            // public_phone: null,
            // address: null,
            // workplace_company: null,
            // workplace_position: null,
            // workplace_city_town: null,
            // workplace_description: null,
            // workplace_time_period: null,
            // avatar: null,
            // cover: null
        }
    }),

    actions: {
        initStore() {
            // console.log('initStore', localStorage.getItem('user.access'))
            if (localStorage.getItem('user.access')) {
                console.log('User has access!')
                this.user.isAuthenticated = true
                this.user.id = localStorage.getItem('user.id')
                this.user.name = localStorage.getItem('user.name')
                this.user.surname = localStorage.getItem('user.surname')
                this.user.email = localStorage.getItem('user.email')
                this.user.date_of_birth = localStorage.getItem('user.date_of_birth')
                this.user.access = localStorage.getItem('user.access')
                this.user.refresh = localStorage.getItem('user.refresh')
                // this.user.personal_phone = localStorage.getItem('user.personal_phone')
                // this.user.public_phone = localStorage.getItem('user.public_phone')
                // this.user.address = localStorage.getItem('user.address')
                // this.user.workplace_company = localStorage.getItem('user.workplace_company')
                // this.user.workplace_position = localStorage.getItem('user.workplace_position')
                // this.user.workplace_city_town = localStorage.getItem('user.workplace_city_town')
                // this.user.workplace_description = localStorage.getItem('user.workplace_description')
                // this.user.workplace_time_period = localStorage.getItem('user.workplace_time_period')
                // this.user.avatar = localStorage.getItem('user.avatar')
                // this.user.cover = localStorage.getItem('user.cover')

                this.refreshToken()

                // console.log('Initialized user:', this.user)
            }
        },

        setToken(data) {
            console.log('setToken', data)

            this.user.access = data.access
            this.user.refresh = data.refresh
            this.user.isAuthenticated = true

            localStorage.setItem('user.access', data.access)
            localStorage.setItem('user.refresh', data.refresh)

            console.log('user.access: ', localStorage.getItem('user.access'))
        },

        removeToken() {
            console.log('removeToken')

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
            // this.user.avatar = null
            // this.user.cover = null

            localStorage.setItem('user.access', '')
            localStorage.setItem('user.refresh', '')
            localStorage.setItem('user.id', '')
            localStorage.setItem('user.name', '')
            localStorage.setItem('user.surname', '')
            localStorage.setItem('user.email', '')
            localStorage.setItem('user.date_of_birth', '')
            // localStorage.setItem('user.personal_phone', '')
            // localStorage.setItem('user.public_phone', '')
            // localStorage.setItem('user.address', '')
            // localStorage.setItem('user.workplace_company', '')
            // localStorage.setItem('user.workplace_position', '')
            // localStorage.setItem('user.workplace_city_town', '')
            // localStorage.setItem('user.workplace_description', '')
            // localStorage.setItem('user.workplace_time_period', '')
            // localStorage.setItem('user.avatar', '')
            // localStorage.setItem('user.cover', '')
        },

        setUserInfo(user) {
            console.log('setUserInfo', user)

            this.user.id = user.id
            this.user.name = user.name
            this.user.surname = user.surname
            this.user.email = user.email
            this.user.date_of_birth = user.date_of_birth
            // this.user.personal_phone = user.personal_phone
            // this.user.public_phone = user.public_phone
            // this.user.address = user.address
            // this.user.workplace_company = user.workplace_company
            // this.user.workplace_position = user.workplace_position
            // this.user.workplace_city_town = user.workplace_city_town
            // this.user.workplace_description = user.workplace_description
            // this.user.workplace_time_period = user.workplace_time_period
            // this.user.avatar = user.avatar
            // this.user.cover = user.cover

            localStorage.setItem('user.id', this.user.id)
            localStorage.setItem('user.name', this.user.name)
            localStorage.setItem('user.surname', this.user.surname)
            localStorage.setItem('user.email', this.user.email)
            localStorage.setItem('user.date_of_birth', this.user.date_of_birth)
            // localStorage.setItem('user.personal_phone', this.user.personal_phone)
            // localStorage.setItem('user.public_phone', this.user.public_phone)
            // localStorage.setItem('user.address', this.user.address)
            // localStorage.setItem('user.workplace_company', this.user.workplace_company)
            // localStorage.setItem('user.workplace_position', this.user.workplace_position)
            // localStorage.setItem('user.workplace_city_town', this.user.workplace_city_town)
            // localStorage.setItem('user.workplace_description', this.user.workplace_description)
            // localStorage.setItem('user.workplace_time_period', this.user.workplace_time_period)
            // localStorage.setItem('user.avatar', this.user.avatar)
            // localStorage.setItem('user.cover', this.user.cover)

            // console.log('User', this.user)
        },

        refreshToken() {
            axios.post('/api/refresh/', {
                refresh: this.user.refresh
            })
                .then((response) => {
                    this.user.access = response.data.access

                    localStorage.setItem('user.access', response.data.access)

                    axios.defaults.headers.common["Authorization"] = "Bearer " + response.data.access
                })
                .catch((error)=>{
                    console.log(error)

                    this.removeToken()
                })
        },
    }
})