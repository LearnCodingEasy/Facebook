<script setup>
// import TheWelcome from '../components/TheWelcome.vue'
</script>

<template>
  <main>
    <div class="container">
      <div class="wrapper_index_page flex flex-row">
        <!-- Left -->
        <div class="left basis-1/4 md:basis-0 lg:basis-1/4">
          <div class="wrapper_left">
            <div class="inner_left">
              <ul>
                <!-- user -->
                <li class="li_user">
                  <a class="" href="#">
                    <span class="img">
                      <img src="../assets/image/user.png" class="" alt="" />
                    </span>
                    <span class="text"> User Name </span>
                  </a>
                </li>
                <!-- Find friends -->
                <li>
                  <a class="nav-link" href="#">
                    <span class="img friends"></span>
                    <span class="text"> Find friends</span>
                  </a>
                </li>
                <!-- Memories -->
                <li>
                  <a class="" href="/">
                    <span class="icon memories"> </span>
                    <span class="text"> Memories</span>
                  </a>
                </li>
                <!-- Saved -->
                <li>
                  <a class="" to="/">
                    <span class="icon saved"> </span>
                    <span class="text"> Saved</span>
                  </a>
                </li>
                <!-- Groups -->
                <li>
                  <a class="" href="/">
                    <span class="icon groups"> </span>
                    <span class="text"> groups</span>
                  </a>
                </li>
                <!-- Video -->
                <li>
                  <a class="" href="/">
                    <span class="icon video"> </span>
                    <span class="text"> Video</span>
                  </a>
                </li>
                <!-- Ads Manager -->
                <li>
                  <a class="" href="/">
                    <span class="icon ads_manager"> </span>
                    <span class="text"> Ads Manager</span>
                  </a>
                </li>
                <!-- Climate Science Centre -->
                <li>
                  <a class="" href="/">
                    <span class="icon climate_science_centre"> </span>
                    <span class="text"> Climate Science Centre</span>
                  </a>
                </li>
                <!-- Events -->
                <li>
                  <a class="" href="/">
                    <span class="icon events"> </span>
                    <span class="text"> Events</span>
                  </a>
                </li>
                <!-- Feeds -->
                <li>
                  <a class="" href="/">
                    <span class="icon feeds"> </span>
                    <span class="text"> Feeds</span>
                  </a>
                </li>
                <!-- Fundraisers -->
                <li>
                  <a class="" href="/">
                    <span class="icon fundraisers"> </span>
                    <span class="text"> Fundraisers</span>
                  </a>
                </li>
                <!-- Gaming Video -->
                <li>
                  <a class="" href="/">
                    <span class="icon gaming_video"> </span>
                    <span class="text"> Gaming Video</span>
                  </a>
                </li>
                <!--  -->
                <!-- Marketplace -->
                <li>
                  <a class="" href="/">
                    <span class="icon marketplace"> </span>
                    <span class="text"> Marketplace</span>
                  </a>
                </li>
                <!-- messages -->
                <li>
                  <a class="" href="/">
                    <span class="icon messages"> </span>
                    <span class="text"> Messages</span>
                  </a>
                </li>
                <!-- Messenger Kids -->
                <li>
                  <a class="" href="/">
                    <span class="icon messenger_kids"> </span>
                    <span class="text"> Messenger Kids</span>
                  </a>
                </li>
                <!-- Orders and payments -->
                <li>
                  <a class="" href="/">
                    <span class="icon orders_and_payments"> </span>
                    <span class="text"> Orders and payments</span>
                  </a>
                </li>
                <!-- Pages -->
                <li>
                  <a class="" href="/">
                    <span class="icon pages"> </span>
                    <span class="text"> Pages</span>
                  </a>
                </li>
                <!-- Play games -->
                <li>
                  <a class="" href="/">
                    <span class="icon play_games"> </span>
                    <span class="text"> Play games</span>
                  </a>
                </li>
                <!-- Recent ad activity -->
                <li>
                  <a class="" href="/">
                    <span class="icon recent_ad_activity"> </span>
                    <span class="text"> Recent ad activity</span>
                  </a>
                </li>
              </ul>
            </div>
          </div>
        </div>
        <!-- Center -->
        <div class="content basis-1/2 lg:basis-1/2 md:basis-1/2 sm:basis-full">
          <div class="wrapper_creat_story">
            <div class="inner_creat_story">
              <div class="wrapprt_swiper">
                <div class="inner_swiper">
                  <swiper
                    ref="swiperRef"
                    :slidesPerView="3"
                    :spaceBetween="30"
                    :pagination="{
                      type: 'progressbar'
                    }"
                    :navigation="true"
                    :modules="[Pagination, Navigation]"
                    class="mySwiper"
                  >
                    <swiper-slide
                      style="
                        transition-duration: 0ms;
                        transform: translate3d(0px, 0px, 0px);
                        transition-delay: 0ms;
                      "
                    >
                      <div class="creat_story">
                        <div class="user_create_story">
                          <div class="img">
                            <!-- :src="userStore.user.avatar" -->
                            <img src="" class="" alt="" />
                          </div>
                          <div class="icon">
                            <span class="">
                              <fa :icon="['fas', 'plus']"></fa>
                            </span>
                          </div>
                          <div class="text">
                            <span class=""> Create Story </span>
                          </div>
                        </div>
                      </div>
                    </swiper-slide>
                    <swiper-slide>Slide 2</swiper-slide>
                    <swiper-slide>Slide 3</swiper-slide>
                    <swiper-slide>Slide 4</swiper-slide>
                    <swiper-slide>Slide 5</swiper-slide>
                    <swiper-slide>Slide 6</swiper-slide>
                    <swiper-slide>Slide 7</swiper-slide>
                    <swiper-slide>Slide 8</swiper-slide>
                    <swiper-slide>Slide 9</swiper-slide>
                  </swiper>
                </div>
              </div>
            </div>
          </div>
          <!-- User Create Post -->
          <div class="wrapper_user_add_post_image_video">
            <div class="inner_user_add_post_image_video">
              <div class="content">
                <div class="">
                  <!-- AddPostForm -->
                </div>
                <div class="post">
                  <div class="user">
                    <div class="img">
                      <img src="../assets/image/user.png" class="" alt="" />
                    </div>
                  </div>
                  <div class="input">
                    <div class="like_input">
                      <input
                        @click="toggleAddPost"
                        type="text"
                        placeholder="What's on your mind, Hossam?"
                        readonly
                      />
                    </div>
                  </div>
                </div>
                <div class="live_video_photo_or_video_feeling_or_activity flex items-center">
                  <div class="live_video basis-1/3">
                    <span class="icon">
                      <img src="../assets/image/add_Live_video.png" class="" alt="" />
                    </span>
                    <span class="text"> Live video </span>
                  </div>
                  <div class="photo_or_video basis-1/3">
                    <span class="icon">
                      <img src="../assets/image/add_Photo_video.png" class="" alt="" />
                    </span>
                    <span class="text"> Photo/video </span>
                  </div>
                  <div class="feeling_or_activity basis-1/3">
                    <span class="icon">
                      <img src="../assets/image/add_Feeling_activity.png" class="" alt="" />
                    </span>
                    <span class="text"> Feeling/activity </span>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <!-- All Posts Item -->
          <!-- 1 -->
          <div class="wapper_item_post">
            <div class="wrapper_post_image_video">
              <div class="inner_post_image_video">
                <div class="content">
                  <div class="user_data_and_option_post">
                    <div class="user_data">
                      <div class="img">
                        <img src="../assets/image/user.png" class="" alt="" />
                      </div>
                      <div class="user_info">
                        <a class="user_view_profile" href="/">
                          <div class="user_name">post created_by name</div>
                        </a>
                        <div class="add_at_trand">
                          <span class="trand"> Suggested for you </span>
                          <span class="add_at">
                            <span class="time_post_trand"> 10 minutes ago</span>
                            <span class="icone_post_trand">
                              <i class="fas fa-globe fa-fw"></i>
                            </span>
                          </span>
                        </div>
                      </div>
                    </div>
                    <div class="option_post">
                      <div class="option">
                        <i class="fas fa-ellipsis-h fa-fw"></i>
                      </div>
                      <div class="close">
                        <i class="fas fa-times fa-fw"></i>
                      </div>
                    </div>
                  </div>
                  <div class="post_content">
                    <!-- v-if="post.body" -->
                    <div class="post_text">
                      <p class="text-base font-normal">
                        Lorem ipsum dolor sit amet consectetur adipisicing elit. Assumenda doloribus
                        quis cum, earum qui deserunt. Maxime quasi tenetur fugiat consequatur.
                        Voluptates perferendis officia impedit deleniti blanditiis unde quisquam
                        labore sint.
                      </p>
                    </div>
                    <!-- v-if="post.image" -->
                    <div class="post_img_or_video">
                      <div>
                        <a href="/">
                          <img src="../assets/image/suits_arbice_1.jpg" class="img-fluid" />
                        </a>
                      </div>
                    </div>
                    <!-- v-if="post.video" -->
                    <!-- <div class="post_img_or_video">
                        <div>
                          <a href="/">
                            <video
                              src="/video/Facebook.mp4"
                              class="img-fluid"
                              controls
                            />
                          </a>
                        </div>
                      </div> -->
                    <!--  -->
                    <div class="post_count_like_comment_share">
                      <div class="count_like flex items-center">
                        <span class="icon_like">
                          <img src="../assets/image/like.png" class="image_like" alt="" />
                        </span>
                        <span class="icon_heart">
                          <img src="../assets/image/heart.png" class="image_heart" alt="" />
                        </span>
                        <span class="userlikethisPost">
                          <span class="count_like_number">
                            <span @mouseover="getAllUserLikePost(post.id)">
                              You And 700 Others
                            </span>
                          </span>
                        </span>
                      </div>
                      <div class="count_comment_share">
                        <div class="comment">
                          <span class="count_like">5 </span>
                          <span class="icon_comment"> <i class="fas fa-comment fa-fw"></i> </span>
                          <span class="text_comment"> comments </span>
                        </div>
                        <div class="share">
                          <span class="count_like">1 </span>
                          <span class="icon_share"><i class="fas fa-share fa-fw"></i> </span>
                          <span class="text_share">shares </span>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="wrapper_add_like_coment_send_share">
                    <div class="inner_add_like_coment_send_share">
                      <div class="add_like">
                        <div class="like" @click="likePost(post.id)">
                          <span class="icon like">
                            <!-- <i class="fas fa-thumbs-up"></i> -->
                            <!-- <img src="/image/home_content_post.png" class="" alt=""> -->
                          </span>
                          <span class="text"> like </span>
                        </div>
                      </div>
                      <!-- Togle Show   -->
                      <div class="add_comment" @click="toggleAddCommentPost(post.id)">
                        <div class="comment">
                          <span class="icon comment">
                            <!-- <i class="fas fa-comment fa-fw"></i> -->
                          </span>
                          <span class="text"> comment </span>
                        </div>
                      </div>

                      <div class="add_send">
                        <div class="send">
                          <span class="icon send">
                            <!-- <i class="fab fa-whatsapp fa-fw"></i> -->
                          </span>
                          <span class="text"> send </span>
                        </div>
                      </div>
                      <div class="add_share">
                        <div class="share">
                          <span class="icon share">
                            <!-- <i class="fas fa-share fa-fw"></i> -->
                          </span>
                          <span class="text"> share </span>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <!-- 2 -->
          <div class="wapper_item_post">
            <div class="wrapper_post_image_video">
              <div class="inner_post_image_video">
                <div class="content">
                  <div class="user_data_and_option_post">
                    <div class="user_data">
                      <div class="img">
                        <img src="../assets/image/user.png" class="" alt="" />
                      </div>
                      <div class="user_info">
                        <a class="user_view_profile" href="/">
                          <div class="user_name">post created_by name</div>
                        </a>
                        <div class="add_at_trand">
                          <span class="trand"> Suggested for you </span>
                          <span class="add_at">
                            <span class="time_post_trand"> 10 minutes ago</span>
                            <span class="icone_post_trand">
                              <i class="fas fa-globe fa-fw"></i>
                            </span>
                          </span>
                        </div>
                      </div>
                    </div>
                    <div class="option_post">
                      <div class="option">
                        <i class="fas fa-ellipsis-h fa-fw"></i>
                      </div>
                      <div class="close">
                        <i class="fas fa-times fa-fw"></i>
                      </div>
                    </div>
                  </div>
                  <div class="post_content">
                    <!-- v-if="post.body" -->
                    <div class="post_text">
                      <p class="text-base font-normal">
                        Lorem ipsum dolor sit amet consectetur adipisicing elit. Assumenda doloribus
                        quis cum, earum qui deserunt. Maxime quasi tenetur fugiat consequatur.
                        Voluptates perferendis officia impedit deleniti blanditiis unde quisquam
                        labore sint.
                      </p>
                    </div>
                    <!-- v-if="post.image" -->
                    <div class="post_img_or_video">
                      <div>
                        <a href="/">
                          <img src="../assets/image/Asser_Yassin.jpg" class="img-fluid" />
                        </a>
                      </div>
                    </div>
                    <!-- v-if="post.video" -->
                    <!-- <div class="post_img_or_video">
                        <div>
                          <a href="/">
                            <video
                              src="/video/Facebook.mp4"
                              class="img-fluid"
                              controls
                            />
                          </a>
                        </div>
                      </div> -->
                    <!--  -->
                    <div class="post_count_like_comment_share">
                      <div class="count_like flex items-center">
                        <span class="icon_like">
                          <img src="../assets/image/like.png" class="image_like" alt="" />
                        </span>
                        <span class="icon_heart">
                          <img src="../assets/image/heart.png" class="image_heart" alt="" />
                        </span>
                        <span class="userlikethisPost">
                          <span class="count_like_number">
                            <span @mouseover="getAllUserLikePost(post.id)">
                              You And 700 Others
                            </span>
                          </span>
                        </span>
                      </div>
                      <div class="count_comment_share">
                        <div class="comment">
                          <span class="count_like">5 </span>
                          <span class="text_comment"> comments </span>
                        </div>
                        <div class="share">
                          <span class="count_like">1 </span>
                          <span class="icon_share">shares </span>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="wrapper_add_like_coment_send_share">
                    <div class="inner_add_like_coment_send_share">
                      <div class="add_like">
                        <div class="like" @click="likePost(post.id)">
                          <span class="icon like">
                            <!-- <i class="fas fa-thumbs-up"></i> -->
                            <!-- <img src="/image/home_content_post.png" class="" alt=""> -->
                          </span>
                          <span class="text"> like </span>
                        </div>
                      </div>
                      <!-- Togle Show   -->
                      <div class="add_comment" @click="toggleAddCommentPost(post.id)">
                        <div class="comment">
                          <span class="icon comment">
                            <!-- <i class="fas fa-comment fa-fw"></i> -->
                          </span>
                          <span class="text"> comment </span>
                        </div>
                      </div>

                      <div class="add_send">
                        <div class="send">
                          <span class="icon send">
                            <!-- <i class="fab fa-whatsapp fa-fw"></i> -->
                          </span>
                          <span class="text"> send </span>
                        </div>
                      </div>
                      <div class="add_share">
                        <div class="share">
                          <span class="icon share">
                            <!-- <i class="fas fa-share fa-fw"></i> -->
                          </span>
                          <span class="text"> share </span>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <!-- Message -->
          <!-- v-if="showMessage" -->
          <div class="wrapper_message">
            <div class="inner_message">
              <div class="box">
                <div class="message_user_data_option">
                  <div class="user_data">
                    <!-- :to="{name: 'ProfileView', params: { id: otherUserOnChat.id }}" -->
                    <RouterLink to="/" class="user_data_link">
                      <!-- عرض بيانات الشخص الآخر -->
                      <!-- v-if="otherUserOnChat" -->
                      <div class="friend_chat_data" v-if="otherUserOnChat">
                        <div class="user_img">
                          <!-- :src="otherUserOnChat.get_avatar" -->
                          <img src="" alt="Avatar" />
                        </div>
                        <div class="user_name">
                          <!-- {{ otherUserOnChat.name }} -->
                          otherUserOnChat.name
                        </div>
                      </div>
                    </RouterLink>
                  </div>
                  <div class="option">
                    <span class="icon_call">
                      <fa :icon="['fas', 'phone']"></fa>
                    </span>
                    <span class="icon_video">
                      <fa :icon="['fas', 'video']"></fa>
                    </span>
                    <!-- @click="toggleShowMessage" -->
                    <span class="icon_minus" @click="toggleShowMessage">
                      <fa :icon="['fas', 'minus']"></fa>
                    </span>
                    <!-- @click="toggleShowMessage" -->
                    <span class="icon_cloose" @click="toggleShowMessage">
                      <fa :icon="['fas', 'times']"></fa>
                    </span>
                  </div>
                </div>
                <div class="message_body">
                  <div class="main-center">
                    <div class="all_message">
                      <!-- v-for="message in activeConversation.messages"
                        v-bind:key="message.id" -->
                      <template>
                        <!-- v-if="message.created_by.id == userStore.user.id" -->
                        <div class="wrapper_myMessage">
                          <div class="inner_myMessage">
                            <div class="content">
                              <p class="text-sm">
                                <!-- {{ message.body }} -->
                                message.body
                              </p>
                            </div>
                            <div class="time">
                              <!-- {{ message.created_at_formatted }} -->
                              message.created_at_formatted ago
                            </div>
                          </div>
                          <div class="my_image">
                            <!-- :src="message.created_by.get_avatar" -->
                            <img src="" class="" />
                          </div>
                        </div>
                        <!-- v-else -->
                        <div class="wrapper_yourMessage">
                          <div class="your_image">
                            <!-- :src="message.created_by.get_avatar" -->
                            <img src="" class="img-fluid" />
                          </div>
                          <div class="inner_myMessage">
                            <div class="content">
                              <p class="text-sm">
                                <!-- {{ message.body }} -->
                                message.body
                              </p>
                            </div>
                            <span class="text-xs text-gray-500 leading-none">
                              <!-- {{ message.created_at_formatted }} -->
                              message.created_at_formatted ago</span
                            >
                          </div>
                        </div>
                      </template>
                    </div>
                    <div class="wrapper_form">
                      <form v-on:submit.prevent="submitForm">
                        <div class="div_textarea">
                          <textarea
                            v-model="body"
                            class="form-control"
                            placeholder="What do you want to say?"
                          ></textarea>
                        </div>
                        <div class="border-t border-gray-100 flex justify-between">
                          <button class="btn btn-primary">
                            <fa :icon="['fas', 'paper-plane']"></fa>
                          </button>
                        </div>
                      </form>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- right -->
        <div class="right basis-1/4 md:basis-0 lg:basis-1/4">
          <div class="wrapper_right">
            <div class="inner_right">
              <div class="user_control">
                <div class="title">
                  <span class="text"> Your Pages and profiles </span>
                  <span class="icon">
                    <i class="fas fa-ellipsis-h fa-fw"></i>
                  </span>
                </div>
                <div class="user">
                  <div class="img">
                    <img src="../assets/image/user.png" class="" alt="" />
                  </div>
                  <div class="user_info">
                    <span class=""> User Name </span>
                  </div>
                </div>
                <div class="Switch_to_Page">
                  <div class="icon"></div>
                  <div class="info">
                    <span class=""> Switch to Page </span>
                  </div>
                </div>
                <div class="Create_promotion">
                  <div class="icon">
                    <!-- <fa :icon="['fas', 'rectangle-ad']"></fa> -->
                  </div>
                  <div class="info">
                    <span class=""> Create promotion </span>
                  </div>
                </div>
              </div>
              <div class="user_Contacts">
                <div class="">
                  <div class="">
                    <div class="Contacts_top">
                      <span class="text">
                        <span class=""> Contacts </span>
                      </span>
                      <span class="options">
                        <span class="icon_search">
                          <fa :icon="['fas', 'magnifying-glass']"></fa>
                          <!-- <i class="fas fa-search fa-fw"></i> -->
                        </span>
                        <span class="icon_dot">
                          <fa :icon="['fas', 'ellipsis']"></fa>
                          <!-- <i class="fas fa-ellipsis-h fa-fw"></i> -->
                        </span>
                      </span>
                    </div>
                    <div class="Contacts_friends">
                      <div class="friends">
                        <!-- v-if="conversations.length" 
                        v-for="conversation in conversations"
                        v-bind:key="conversation.id"
                        v-on:click="setActiveConversation(conversation.id)"
                        -->
                        <div class="">
                          <!-- v-for="user in conversation.users"
                          v-bind:key="user.id" -->
                          <div class="single_friend">
                            <!-- v-if="user.id !== userStore.user.id" -->
                            <div class="friend_img">
                              <img src="../assets/image/user.png" class="img-fluid" />
                            </div>
                            <!-- v-if="user.id !== userStore.user.id" -->
                            <div class="friend_name">
                              <!-- @click="funShowMessage" -->
                              <span class="name"> user.name </span>
                            </div>
                          </div>
                          <!-- v-for="user in conversation.users"
                          v-bind:key="user.id" -->
                          <div class="single_friend">
                            <!-- v-if="user.id !== userStore.user.id" -->
                            <div class="friend_img user_is_active_now">
                              <img src="../assets/image/user.png" class="img-fluid" />
                            </div>
                            <!-- v-if="user.id !== userStore.user.id" -->
                            <div class="friend_name">
                              <!-- @click="funShowMessage" -->
                              <span class="name"> user.name </span>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>
<script>
// Import Swiper Vue.js components
import { Swiper, SwiperSlide } from 'swiper/vue'
// Import Swiper styles
import 'swiper/css'
import 'swiper/css/pagination'
import 'swiper/css/navigation'
// import required modules
import { Pagination, Navigation } from 'swiper/modules'

export default {
  setup() {
    return {
      modules: [Pagination, Navigation]
    }
  },
  components: {
    Swiper,
    SwiperSlide
  }
}
</script>
