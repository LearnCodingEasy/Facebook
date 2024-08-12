<template>
  <div class="wrapper_component_add_post" @click.self="closeAddPost">
    <div class="inner_component_add_post">
      <dov class="post_title">Create Post</dov>
      <span class="icon_close">
        <fa :icon="['fas', 'xmark']" @click.self="closeAddPost"></fa>
      </span>
      <form v-on:submit.prevent="submitAddPostForm" method="post">
        <!-- Post Body Text -->
        <div class="post_body">
          <textarea
            v-model="body"
            class="form-control"
            placeholder="What's on your mind, Hossam?"
          ></textarea>
        </div>

        <!-- <div class="post_is_private form-check">
          <input
            class="form-check-input"
            type="checkbox"
            value=""
            id="flexCheckDefault"
            v-model="is_private"
          />
          <label class="form-check-label" for="flexCheckDefault"> Privates </label>
        </div> -->
        <!-- Post Video -->
        <div class="show_video_post">
          <div id="previewVideo" v-if="urlVideo">
            <video controls :src="urlVideo"></video>
          </div>
        </div>

        <!-- Post Image -->
        <div class="show_image_post">
          <div id="preview" v-if="url">
            <img :src="url" class="img-thumbnail" />
          </div>
        </div>

        <div class="row">
          <div class="col">
            <div class="choose_image">
              <label for="image" class="form-label d-flex justify-content-center">
                <fa :icon="['fas', 'image']" class="fa-fw fa-5x"></fa>
              </label>
              <input
                type="file"
                ref="file"
                @change="handleFileUpload"
                class="form-control"
                placeholder="image"
                id="image"
              />
            </div>
          </div>
          <div class="col">
            <div class="choose_video">
              <label for="video" class="form-label d-flex justify-content-center">
                <fa :icon="['fas', 'video']" class="fa-fw fa-5x"></fa>
              </label>
              <input
                type="file"
                ref="fileVideo"
                @change="handleFileUploadVideo"
                class="form-control"
                id="video"
              />
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col">
            <template v-if="errors.length > 0">
              <div
                class="transition ease-in-out delay-2000 duration-500 bg-danger text-white rounded-lg p-3"
              >
                <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
              </div>
            </template>
          </div>
        </div>
        <div class="wrapper_sand_post">
          <button class="btn btn-primary w-50 m-auto d-block">Post</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
//
import { useToastStore } from '@/stores/toast'

export default {
  props: {
    user: Object,
    posts: Array
  },
  setup() {
    const toastStore = useToastStore()
    return {
      toastStore
    }
  },
  data() {
    return {
      post: [],
      body: '',
      // Post  image
      selectedFile: null,
      url: null,
      // Post Video
      selectedFileVideo: null,
      urlVideo: null,
      is_private: false,
      //
      errors: []
    }
  },

  methods: {
    // For Upload Image to Post Store and for Post
    handleFileUpload(event) {
      let file = event.target.files[0]
      console.log('file Image: ', file)
      this.url = URL.createObjectURL(file)
      this.selectedFile = event.target.files[0]
    },
    // For Upload Video to Post Store and for Post
    handleFileUploadVideo(event) {
      let file = event.target.files[0]
      console.log('file Video: ', file)
      this.urlVideo = URL.createObjectURL(file)
      this.selectedFileVideo = event.target.files[0]
    },
    submitAddPostForm() {
      console.log('submitForm', this.body)

      let formData = new FormData()

      // formData.append('image', this.$refs.file.files[0])
      // formData.append('is_private', this.is_private)
      console.log('formData: ', formData)
      // Add Image [  ] إضافة الصور إذا تم تحديدها
      if (this.selectedFile) {
        // formData.append('image', this.$refs.file.files[0])
        formData.append('image', this.selectedFile)
      }
      // Add Image [  ] إضافة الصور إذا تم تحديدها
      if (this.selectedFileVideo) {
        // formData.append('image', this.$refs.file.files[0])
        formData.append('video', this.selectedFileVideo)
      }
      if (this.body == '') {
        this.toastStore.showToast(5000, 'Type Post Text.', 'bg-danger')
        this.errors.push('Type Post Text')
      } else if (this.body !== '') {
        formData.append('body', this.body)
      }

      if (this.errors.length === 0) {
        axios
          .post('/api/posts/post_create/', formData, {
            headers: {
              'Content-Type': 'multipart/form-data'
            }
          })
          .then((response) => {
            console.log('Data Is Send To Django: ', response.data)

            this.post.unshift(response.data)
            this.body = ''
            this.url = null
            this.urlVideo = null
            // this.is_private = false
            // this.$refs.file.value = null
            this.selectedFile = null
            this.selectedFileVideo = null
            // this.url = null

            if (this.user) {
              console.log('this.user: ', this.user)
              this.user.posts_count += 1
            }
          })
          .catch((error) => {
            console.log('error', error)
          })
      }
    },
    closeAddPost() {
      // Emit the 'close' event when the close button is clicked
      this.$emit('close_add_post')
    }
  }
}
</script>

<style lang="scss"></style>
