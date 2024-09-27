<script setup>
import { RouterLink } from 'vue-router'

//
import { onMounted } from 'vue'
import { useUserStore } from '@/stores/user'
import { useRouter } from 'vue-router'

const userStore = useUserStore()
userStore.initStore()
const router = useRouter()

onMounted(() => {
  // Perform any necessary operations on component mount
  if (!userStore.user.access) {
    console.log('User Data: ', userStore.user.access)
    // Replace '/login' with your actual login route
    router.push('/login')
  } else {
    // Set default Authorization header for axios
    axios.defaults.headers.common['Authorization'] = `Bearer ${userStore.user.access}`
    // console.log('User Data: ', userStore.user)
  }
})
</script>
<template>
  <div class="wrapper_profile_page" v-if="userStore.user.isAuthenticated">
    <div class="inner_profile_page">
      <div class="contant container m-auto">
        <!-- user cover -->
        <div class="wrapper_user_cover">
          <div class="inner_user_cover" v-if="userStore.user.cover">
            <img :src="userStore.user.cover" class="img-fluid rounded-start" alt="" />
          </div>
          <div class="inner_user_cover" v-else>
            <img src="../../assets/image/404.JPG" class="" alt="" />
          </div>
          <div class="control_user_cover" v-if="userStore.user.id === user.id">
            <div class="button_control_user_cover">
              <span class="icon"> <fa :icon="['fas', 'camera']"></fa> </span>
              <span class="text"> Edit cover photo </span>
            </div>
          </div>
        </div>
        <!-- main container User Datelse -->
        <div class="main-container">
          <!-- user_name_edite_profile -->
          <div class="wrapper_user_name_edite_profile">
            <prime_card class="inner_user_name_edite_profile">
              <template #header>
                <div class="left">
                  <div class="image">
                    <div class="img">
                      <img
                        :src="userStore.user.avatar"
                        v-if="userStore.user.avatar"
                        class=""
                        alt=""
                      />
                      <img src="./../../assets/image/user.png" v-else class="" alt="" />
                      <span class="icon" v-if="userStore.user.id === user.id">
                        <fa :icon="['fas', 'camera']"></fa>
                      </span>
                    </div>
                  </div>
                  <div class="name_friends">
                    <div class="user_name">{{ userStore.user.name }}</div>
                    <div class="user_friends_count">
                      <!-- <RouterLink
                      :to="{ name: 'FriendsView', params: { id: user.id } }"
                      class="text-xs text-gray-500"
                      >{{ user.friends_count }} friends</RouterLink 
                      >
                      -->
                    </div>
                    <div class="user_friends">
                      <span
                        class=""
                        v-for="singleFriend in friends_siven"
                        v-bind:key="singleFriend.id"
                      >
                        <img :src="singleFriend.get_avatar" class="" alt="" />
                      </span>
                    </div>
                  </div>
                </div>
              </template>
              <template #content>
                <div class="right">
                  <div class="wrapper_button_edit_progile">
                    <div class="inner_button_edit_progile">
                      <!-- اذا كان مللك الصفحة -->
                      <div class="is_owner" v-if="userStore.user.id === user.id">
                        <botton class="Add_to_story btn btn-primary">
                          <span class="icon"> <fa :icon="['fas', 'plus']"></fa> </span>
                          <span class="text"> Add to story </span>
                        </botton>
                        <RouterLink
                          class="Edit_profile btn"
                          v-if="userStore.user.id === user.id"
                          to="EditProfileView"
                        >
                          <!-- <botton class=" btn"> -->
                          <span class="icon"> <fa :icon="['fas', 'pen']"></fa> </span>
                          <span class="text"> Edit profile </span>
                          <!-- </botton> -->
                        </RouterLink>
                      </div>
                      <!-- اذا كان زائر  -->
                      <div class="is_visitor" v-if="userStore.user.id !== user.id">
                        <!-- ارسال طلب صداقة -->
                        <button
                          @click="sendFriendshipRequest"
                          class="btn btn-primary Add_friend"
                          v-if="can_send_friendship_request"
                        >
                          <span class="icon"><fa :icon="['fas', 'plus']"></fa></span>
                          <span class="text">Add friend</span>
                        </button>
                        <!-- اذا تم ارسال طلب صداقة -->
                        <!-- v-if="!can_send_friendship_request" -->
                        <button
                          class="btn btn-primary Add_friend"
                          v-if="can_send_friendship_request"
                        >
                          <span class="icon"><fa :icon="['fas', 'plus']"></fa></span>
                          <span class="text">Wate Accepted friend</span>
                        </button>
                        <!-- اذا كان من الاصدقاء -->
                        <button class="btn btn-primary is_friend" v-if="isFriend">
                          <span class="icon"><fa :icon="['fas', 'user-check']"></fa></span>
                          <span class="text"> friend</span>
                        </button>
                        <!-- ارسال رساله -->
                        <button class="btn-primary message_friend" @click="sendDirectMessage">
                          <span class="icon"><fa :icon="['fab', 'facebook-messenger']"></fa></span>
                          <span class="text"> Message</span>
                        </button>
                      </div>
                      <botton class="toggle_see_frindes btn">
                        <span class="icon"> <fa :icon="['fas', 'angle-up']"></fa> </span>
                      </botton>
                    </div>
                  </div>
                </div>
              </template>
            </prime_card>
          </div>
          <!-- all_data_profile -->
          <div class="wrapper_all_data_profile">
            <div class="inner_all_data_profile">
              <div class="wrapper_tabs_choose">
                <prime_card>
                  <template #header>
                    <div class="control_tabs_choose">
                      <ul class="tabs_choose p-3">
                        <!-- Posts -->
                        <li @click="activeTab = '1'" :class="[activeTab === '1' ? 'activeLi' : '']">
                          <span class="text">Posts</span>
                        </li>
                        <!-- About -->
                        <li @click="activeTab = '2'" :class="[activeTab === '2' ? 'activeLi' : '']">
                          <span class="text">About</span>
                        </li>
                        <!-- Friends -->
                        <li @click="activeTab = '3'" :class="[activeTab === '3' ? 'activeLi' : '']">
                          <span class="text">Friends</span>
                        </li>
                        <!-- Photos -->
                        <li @click="activeTab = '4'" :class="[activeTab === '4' ? 'activeLi' : '']">
                          <span class="text">Photos</span>
                        </li>
                        <!-- Videos -->
                        <li @click="activeTab = '5'" :class="[activeTab === '5' ? 'activeLi' : '']">
                          <span class="text">Videos</span>
                        </li>
                        <!-- Chick-in -->
                        <li @click="activeTab = '6'" :class="[activeTab === '6' ? 'activeLi' : '']">
                          <span class="text">Chick-in</span>
                        </li>
                        <!-- More -->
                        <li @click="activeTab = '7'" :class="[activeTab === '7' ? 'activeLi' : '']">
                          <span class="text"> More </span>
                          <span class="icon">
                            <fa :icon="['fas', 'sort-down']"></fa>
                          </span>
                        </li>
                      </ul>
                      <div class="more">
                        <span class=""> <fa :icon="['fas', 'ellipsis']"></fa> </span>
                      </div>
                    </div>
                  </template>
                </prime_card>
                <div class="tabs_content">
                  <!-- posts -->
                  <div class="posts" v-if="activeTab === '1'">
                    <div class="wrapper_user_owner_posts">
                      <div class="inner__user_owner_posts">
                        <div class="row grid grid-cols-3 gap-4">
                          <div class="col-5">
                            <!-- Intro -->
                            <div class="div_intro">
                              <prime_card>
                                <template #header>
                                  <h3 class="title">Intro</h3>
                                </template>
                                <template #content>
                                  <div class="buttons">
                                    <button>Add Bio</button>
                                    <button>Edit details</button>
                                    <button>Add Featured</button>
                                  </div>
                                </template>
                              </prime_card>
                            </div>
                            <!-- Pohotos -->
                            <div class="photos">
                              <div class="link_text">
                                <span
                                  @click="activeTab = '4'"
                                  :class="[activeTab === '4' ? 'activeLi' : '']"
                                  >Pohotos</span
                                >
                              </div>
                              <div class="link_photo">
                                <span
                                  @click="activeTab = '4'"
                                  :class="[activeTab === '4' ? 'activeLi' : '']"
                                >
                                  See All Photos
                                </span>
                              </div>
                            </div>
                            <!-- Friends -->
                            <div class="frinds">
                              <div class="wrapper_frindes_name_count">
                                <div class="frindes_name_count">
                                  <div
                                    class="friends_title"
                                    @click="activeTab = '3'"
                                    :class="[activeTab === '3' ? 'activeLi' : '']"
                                  >
                                    Friends
                                  </div>
                                  <span>{{ user.friends_count }} friends</span>
                                </div>
                                <div class="friends_linke">
                                  <span
                                    @click="activeTab = '3'"
                                    :class="[activeTab === '3' ? 'activeLi' : '']"
                                    >See all friends</span
                                  >
                                </div>
                              </div>
                              <div class="user_friends">
                                <div
                                  class="box_single_friend"
                                  v-for="singleFriend in friends_nine"
                                  v-bind:key="singleFriend.id"
                                >
                                  <div class="friend_img">
                                    <img :src="singleFriend.get_avatar" class="" alt="" />
                                  </div>
                                  <div class="friend_name">{{ singleFriend.name }}</div>
                                </div>
                              </div>
                            </div>
                          </div>
                          <div class="col-7 col-span-2">
                            <!-- All Posts Item -->
                            <!-- <ItemPosts :posts="posts"></ItemPosts> -->
                            <!-- Card 1 -->
                            <prime_card class="wapper_item_post">
                              <template #header>
                                <div class="user_data_and_option_post">
                                  <div class="user_data">
                                    <div class="img">
                                      <img src="../../assets/image/user.png" class="" alt="" />
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
                                      <!-- <i class="fas fa-ellipsis-h fa-fw"></i> -->
                                      <i
                                        class="text-lg text-surface-500 dark:text-surface-400 pi pi-ellipsis-h"
                                      ></i>
                                    </div>
                                    <div class="close">
                                      <!-- <i class="fas fa-times fa-fw"></i> -->
                                      <i
                                        class="text-lg ml-4 text-surface-500 dark:text-surface-400 pi pi-times"
                                      ></i>
                                    </div>
                                  </div>
                                </div>
                              </template>
                              <template #content>
                                <div class="post_content">
                                  <!-- v-if="post.body" -->
                                  <div class="post_text">
                                    <p class="text-base font-normal">
                                      Lorem ipsum dolor sit amet consectetur adipisicing elit.
                                      Assumenda doloribus quis cum, earum qui deserunt. Maxime quasi
                                      tenetur fugiat consequatur. Voluptates perferendis officia
                                      impedit deleniti blanditiis unde quisquam labore sint.
                                    </p>
                                  </div>
                                  <!-- v-if="post.image" -->
                                  <div class="post_img_or_video">
                                    <div>
                                      <a href="/">
                                        <img
                                          src="../../assets/image/Asser_Yassin.jpg"
                                          class="img-fluid"
                                        />
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
                                        <img
                                          src="../../assets/image/like.png"
                                          class="image_like"
                                          alt=""
                                        />
                                      </span>
                                      <span class="icon_heart">
                                        <img
                                          src="../../assets/image/heart.png"
                                          class="image_heart"
                                          alt=""
                                        />
                                      </span>
                                      <span class="userlikethisPost">
                                        <span class="count_like_number">
                                          <!-- @mouseover="getAllUserLikePost(post.id)" -->
                                          <span> You And 700 Others </span>
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
                              </template>
                              <template #footer>
                                <div class="wrapper_add_like_coment_send_share">
                                  <div class="inner_add_like_coment_send_share">
                                    <div class="add_like">
                                      <!-- @click="likePost(post.id)" -->
                                      <div class="like">
                                        <span class="icon like">
                                          <!-- <i class="fas fa-thumbs-up"></i> -->
                                          <!-- <img src="/image/home_content_post.png" class="" alt=""> -->
                                        </span>
                                        <span class="text"> like </span>
                                      </div>
                                    </div>
                                    <!-- Togle Show   -->
                                    <!-- @click="toggleAddCommentPost(post.id)" -->
                                    <div class="add_comment">
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
                              </template>
                            </prime_card>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <!-- About -->
                  <div class="about" v-if="activeTab === '2'">
                    <div class="wrapper_about_user">
                      <div class="inner_about_user">
                        <div class="control_about_link">
                          <div class="card-title h2">About</div>
                          <ul>
                            <!-- Overview -->
                            <li
                              @click="activeTabAbout = '1'"
                              :class="[activeTabAbout === '1' ? 'activeLiAbout' : '']"
                            >
                              <span class="text">Overview</span>
                            </li>
                            <!-- Work and education -->
                            <li
                              @click="activeTabAbout = '2'"
                              :class="[activeTabAbout === '2' ? 'activeLiAbout' : '']"
                            >
                              <span class="text">Work and education</span>
                            </li>
                            <!-- Places lived -->
                            <li
                              @click="activeTabAbout = '3'"
                              :class="[activeTabAbout === '3' ? 'activeLiAbout' : '']"
                            >
                              <span class="text">Places lived</span>
                            </li>
                            <!-- Contact and basic info -->
                            <li
                              @click="activeTabAbout = '4'"
                              :class="[activeTabAbout === '4' ? 'activeLiAbout' : '']"
                            >
                              <span class="text">Contact and basic info</span>
                            </li>
                            <!-- Family and relationships -->
                            <li
                              @click="activeTabAbout = '5'"
                              :class="[activeTabAbout === '5' ? 'activeLiAbout' : '']"
                            >
                              <span class="text">Family and relationships</span>
                            </li>
                            <!-- Details about you -->
                            <li
                              @click="activeTabAbout = '6'"
                              :class="[activeTabAbout === '6' ? 'activeLiAbout' : '']"
                            >
                              <span class="text">Details about you</span>
                            </li>
                            <!-- Life events -->
                            <li
                              @click="activeTabAbout = '7'"
                              :class="[activeTabAbout === '7' ? 'activeLiAbout' : '']"
                            >
                              <span class="text">Life events</span>
                            </li>
                          </ul>
                        </div>
                        <div class="control_about_view">
                          <div class="about_overview" v-if="activeTabAbout === '1'">
                            <div class="button_overview">
                              <!-- Add a workplace -->
                              <button
                                @click="toggleShowAddAWorkplace"
                                v-if="showAddAWorkpolace != true"
                              >
                                <span class="icon">
                                  <fa :icon="['fas', 'plus-circle']"></fa>
                                </span>
                                <span class="text">Add a workplace</span>
                              </button>
                              <div class="wrapper_add_a_workplace" v-if="showAddAWorkpolace">
                                <form class="space-y-6" v-on:submit.prevent="submitFormWorkplace">
                                  <!-- Company -->
                                  <div class="row">
                                    <div class="col">
                                      <div class="form-floating mb-3">
                                        <input
                                          type="text"
                                          id="workplace_company"
                                          v-model="formWorkplace.workplace_company"
                                          placeholder="Company"
                                          class="form-control"
                                        />
                                        <label for="workplace_company" class="form-label"
                                          >Company</label
                                        >
                                      </div>
                                    </div>
                                  </div>
                                  <!-- Position -->
                                  <div class="row">
                                    <div class="col">
                                      <div class="form-floating mb-3">
                                        <input
                                          type="text"
                                          id="workplace_position"
                                          v-model="formWorkplace.workplace_position"
                                          placeholder="Position"
                                          class="form-control"
                                        />
                                        <label for="workplace_position" class="form-label"
                                          >Position</label
                                        >
                                      </div>
                                    </div>
                                  </div>
                                  <!-- City/Town -->
                                  <div class="row">
                                    <div class="col">
                                      <div class="form-floating mb-3">
                                        <input
                                          type="text"
                                          id="workplace_city_town"
                                          v-model="formWorkplace.workplace_city_town"
                                          placeholder="Position"
                                          class="form-control"
                                        />
                                        <label for="workplace_city_town" class="form-label"
                                          >City/Town</label
                                        >
                                      </div>
                                    </div>
                                  </div>
                                  <!-- Description -->
                                  <div class="row">
                                    <div class="col">
                                      <div class="form-floating mb-3">
                                        <textarea
                                          class="form-control"
                                          placeholder="Description"
                                          id="workplace_description"
                                          v-model="formWorkplace.workplace_description"
                                          style="height: 100px"
                                        ></textarea>

                                        <label for="workplace_description" class="form-label"
                                          >Description</label
                                        >
                                      </div>
                                    </div>
                                  </div>
                                  <!-- Time Period -->
                                  <div class="row">
                                    <div class="col">
                                      <div class="form-floating mb-3">
                                        <input
                                          type="month"
                                          name="workplace_time_period"
                                          id="workplace_time_period"
                                          class="form-control"
                                          v-model="formWorkplace.workplace_time_period"
                                        />

                                        <label for="workplace_time_period" class="form-label"
                                          >Year</label
                                        >
                                      </div>
                                    </div>
                                  </div>
                                  <div class="row">
                                    <div class="col">
                                      <div class="mb-3">
                                        <label class="form-label" for="email">E-mail</label>
                                        <input
                                          type="email"
                                          id="email"
                                          v-model="formWorkplace.email"
                                          placeholder="Your e-mail address"
                                          class="form-control"
                                        />
                                      </div>
                                    </div>
                                  </div>
                                  <div class="d_flex">
                                    <button class="btn btn-primary">Save</button>
                                    <button class="btn btn-danger" @click="toggleHideAddAWorkplace">
                                      Cansel
                                    </button>
                                  </div>
                                </form>
                              </div>
                              <!-- Add secondary school -->
                              <button>
                                <span class="icon">
                                  <fa :icon="['fas', 'plus-circle']"></fa>
                                </span>
                                <span class="text">Add secondary school</span>
                              </button>
                              <!-- Add university -->
                              <button>
                                <span class="icon">
                                  <fa :icon="['fas', 'plus-circle']"></fa>
                                </span>
                                <span class="text">Add university</span>
                              </button>
                              <!-- Add current city -->
                              <button>
                                <span class="icon">
                                  <fa :icon="['fas', 'plus-circle']"></fa>
                                </span>
                                <span class="text">Add current city</span>
                              </button>
                              <!-- Add home town -->
                              <button>
                                <span class="icon">
                                  <fa :icon="['fas', 'plus-circle']"></fa>
                                </span>
                                <span class="text">Add home town</span>
                              </button>
                              <!-- Add a relationship status -->
                              <button>
                                <span class="icon">
                                  <fa :icon="['fas', 'plus-circle']"></fa>
                                </span>
                                <span class="text">Add a relationship status</span>
                              </button>
                              <!-- Add a relationship status -->
                              <button>
                                <span class="icon">
                                  <fa :icon="['fas', 'plus-circle']"></fa>
                                </span>
                                <span class="text">Add a relationship status</span>
                              </button>
                              <div class="user_phone_number">
                                <div class="phone_number_data">
                                  <span class="icon"><fa :icon="['fas', 'phone']"></fa></span>
                                  <span class="span_phone_number_data">
                                    <span class=""> {{ user.personal_phone }} </span>
                                    <span class=""> Mobile </span>
                                  </span>
                                </div>
                                <div class="phone_number_control">
                                  <span class="icon lock"><fa :icon="['fas', 'lock']"></fa></span>
                                  <span class="icon pen"><fa :icon="['fas', 'pen']"></fa></span>
                                </div>
                              </div>
                            </div>
                          </div>
                          <div class="about_overview" v-if="activeTabAbout === '2'">
                            <div class="button_overview">
                              <!-- Work -->
                              <h2 class="h4 font-bold">Work</h2>
                              <button>
                                <span class="icon">
                                  <fa :icon="['fas', 'plus-circle']"></fa>
                                </span>
                                <span class="text">Add Work</span>
                              </button>
                              <!-- University -->
                              <h2 class="h4 font-bold">University</h2>
                              <button>
                                <span class="icon">
                                  <fa :icon="['fas', 'plus-circle']"></fa>
                                </span>
                                <span class="text">Add University</span>
                              </button>
                              <!-- High School -->
                              <h2 class="h4 font-bold">High School</h2>
                              <button>
                                <span class="icon">
                                  <fa :icon="['fas', 'plus-circle']"></fa>
                                </span>
                                <span class="text">High School </span>
                              </button>
                            </div>
                          </div>
                          <div class="about_overview" v-if="activeTabAbout === '3'">
                            <div class="button_overview">
                              <!-- Places lived -->
                              <h2 class="h2">Places lived</h2>
                              <button>
                                <span class="icon">
                                  <fa :icon="['fas', 'plus-circle']"></fa>
                                </span>
                                <span class="text">Add current city</span>
                              </button>
                              <button>
                                <span class="icon">
                                  <fa :icon="['fas', 'plus-circle']"></fa>
                                </span>
                                <span class="text">Add home town</span>
                              </button>
                              <button>
                                <span class="icon">
                                  <fa :icon="['fas', 'plus-circle']"></fa>
                                </span>
                                <span class="text">Add city </span>
                              </button>
                            </div>
                          </div>
                          <div class="about_overview" v-if="activeTabAbout === '4'">
                            <div class="button_overview">
                              <h2 class="h4 font-bold">Contact info</h2>
                              <div class="user_phone_number mt-3">
                                <div class="phone_number_data">
                                  <span class="icon"><fa :icon="['fas', 'phone']"></fa></span>
                                  <span class="span_phone_number_data">
                                    <span class=""> {{ user.personal_phone }} </span>
                                    <span class=""> Mobile </span>
                                  </span>
                                </div>
                                <div class="phone_number_control">
                                  <span class="icon lock"><fa :icon="['fas', 'lock']"></fa></span>
                                  <span class="icon pen" v-if="userStore.user.id == user.id"
                                    ><fa :icon="['fas', 'pen']"></fa
                                  ></span>
                                </div>
                              </div>
                              <div class="user_phone_number mt-3">
                                <div class="phone_number_data" v-if="activeTabEditeEmail === '1'">
                                  <span class="image"
                                    ><img src="../../assets/iamge/icon/email.png" class="" alt=""
                                  /></span>
                                  <span class="span_phone_number_data">
                                    <span class=""> {{ user.email }} </span>
                                    <span class=""> Email </span>
                                  </span>
                                </div>
                                <div class="phone_number_data" v-if="activeTabEditeEmail === '2'">
                                  <form v-on:submit.prevent="submitFormEditeProfileEmail">
                                    <prime_float_label class="mt-5">
                                      <prime_input_text
                                        id="emailAddress"
                                        v-model="formEditeProfileEmail.email"
                                        class="block w_100"
                                      />
                                      <label for="emailAddress" class="text-base"
                                        >Your E-mail Address
                                      </label>
                                    </prime_float_label>
                                    <!-- 
                                    @click="activeTabEditeEmail = '1'"
                                      :class="[activeTabEditeEmail === '1' ? 'activeLi' : '']"
                                      -->
                                    <prime_button
                                      label="Save"
                                      icon="pi pi-check"
                                      iconPos="right"
                                      severity="success"
                                    />
                                  </form>
                                </div>
                                <div class="phone_number_control">
                                  <span class="icon lock"><fa :icon="['fas', 'lock']"></fa></span>
                                  <span
                                    class="icon pen"
                                    v-if="userStore.user.id == user.id"
                                    @click="activeTabEditeEmail = '2'"
                                    :class="[activeTabEditeEmail === '2' ? 'activeLi' : '']"
                                    ><fa :icon="['fas', 'pen']"></fa
                                  ></span>
                                </div>
                              </div>
                              <h2 class="h4 font-bold mt-3">Websites and social links</h2>
                              <div class="user_phone_number mt-3">
                                <div class="phone_number_data">
                                  <span class="image">
                                    <img
                                      src="../../assets/iamge/icon/website.png"
                                      class=""
                                      alt=""
                                    />
                                  </span>
                                  <span class="span_phone_number_data">
                                    <span class="" v-if="user.website"> {{ user.website }} </span>
                                    <span class=""> Website </span>
                                  </span>
                                </div>
                                <div class="phone_number_control">
                                  <span class="icon lock"><fa :icon="['fas', 'lock']"></fa></span>
                                  <span class="icon pen" v-if="userStore.user.id == user.id"
                                    ><fa :icon="['fas', 'pen']"></fa
                                  ></span>
                                </div>
                              </div>
                            </div>
                          </div>
                          <div class="about_overview" v-if="activeTabAbout === '5'">
                            <form v-on:submit.prevent="submitFormEditeProfileName">
                              <prime_float_label class="mt-5">
                                <prime_input_text
                                  id="userName"
                                  v-model="formEditeProfileName.name"
                                  class="block w_100"
                                />
                                <label for="userName" class="text-base">User Name </label>
                              </prime_float_label>
                              <!-- 
                                    @click="activeTabEditeEmail = '1'"
                                      :class="[activeTabEditeEmail === '1' ? 'activeLi' : '']"
                                      -->
                              <prime_button
                                label="Save"
                                icon="pi pi-check"
                                iconPos="right"
                                severity="success"
                              />
                            </form>
                          </div>
                          <div class="about_overview" v-if="activeTabAbout === '6'"></div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <!-- Friends -->
                  <div class="friends" v-if="activeTab === '3'">
                    <div class="wrapper_user_friends">
                      <div class="inner_user_friends">
                        <div class="header_user_friends">
                          <div class="title">
                            <h3 class="font_bold h4">Friends</h3>
                          </div>
                          <div class="options">
                            <div class="friends_search">
                              <input type="text" class="form-control" placeholder="Search" />
                            </div>
                            <div class="links">
                              <!-- Friend requests -->
                              <!-- <RouterLink
                                class="nav-link"
                                :to="{ name: 'FriendsView', params: { id: userStore.user.id } }"
                              >
                                Friend requests
                              </RouterLink> -->
                              <!-- Find friends -->
                              <!-- <RouterLink
                                class="nav-link"
                                :to="{ name: 'FriendsView', params: { id: userStore.user.id } }"
                              >
                                Find friends
                              </RouterLink> -->
                            </div>
                            <div class="icon">
                              <span class=""> <fa :icon="['fas', 'ellipsis-h']"></fa> </span>
                            </div>
                          </div>
                        </div>
                        <div class="main_user_friends">
                          <div class="control_toggle_show_fran">
                            <ul>
                              <!-- All friends -->
                              <li
                                @click="activeTabFriend = '1'"
                                :class="[activeTabFriend === '1' ? 'activeLiFriend' : '']"
                              >
                                <span class="text">All friends</span>
                              </li>
                              <!-- Recently added -->
                              <li
                                @click="activeTabFriend = '2'"
                                :class="[activeTabFriend === '2' ? 'activeLiFriend' : '']"
                              >
                                <span class="text">Recently added</span>
                              </li>
                              <!-- Following -->
                              <li
                                @click="activeTabFriend = '3'"
                                :class="[activeTabFriend === '3' ? 'activeLiFriend' : '']"
                              >
                                <span class="text">Following</span>
                              </li>
                            </ul>
                          </div>
                          <div class="contant_user_friends">
                            <div class="frinds_overview" v-if="activeTabFriend === '1'">
                              <div class="inner_frinds_overview">
                                <div
                                  class="single_user_friend"
                                  v-for="frind in friends_accepted"
                                  v-bind:key="frind"
                                  @click="windowReload"
                                >
                                  <RouterLink
                                    :to="{
                                      name: 'ProfileView',
                                      params: { id: frind.id }
                                    }"
                                  >
                                    <div class="friend_data">
                                      <div class="img">
                                        <img :src="frind.get_avatar" class="" alt="" />
                                      </div>
                                      <div class="friend_data_name_discribshin">
                                        <div class="name">{{ frind.name }}</div>
                                        <div class="discribshin">discribshin</div>
                                      </div>
                                    </div>
                                    <div class="friend_option">
                                      <span class="">
                                        <fa :icon="['fas', 'ellipsis-h']"></fa>
                                      </span>
                                    </div>
                                  </RouterLink>
                                </div>
                              </div>
                            </div>
                            <div class="frinds_overview" v-if="activeTabFriend === '2'">
                              <div class="inner_frinds_overview">
                                <div
                                  class="single_user_friend"
                                  v-for="frind in friends_accepted"
                                  v-bind:key="frind"
                                  @click="windowReload"
                                >
                                  <RouterLink
                                    :to="{
                                      name: 'ProfileView',
                                      params: { id: frind.id }
                                    }"
                                  >
                                    <div class="friend_data">
                                      <div class="img">
                                        <img :src="frind.get_avatar" class="" alt="" />
                                      </div>
                                      <div class="friend_data_name_discribshin">
                                        <div class="name">{{ frind.name }}</div>
                                        <div class="discribshin">discribshin</div>
                                      </div>
                                    </div>
                                    <div class="friend_option">
                                      <span class="">
                                        <fa :icon="['fas', 'ellipsis-h']"></fa>
                                      </span>
                                    </div>
                                  </RouterLink>
                                </div>
                              </div>
                            </div>
                            <div class="frinds_overview" v-if="activeTabFriend === '3'"></div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <!-- Photos -->
                  <div class="photos" v-if="activeTab === '4'">
                    Photos
                    <div class="card flex justify-center">
                      <AutoComplete
                        v-model="selectedCountry"
                        optionLabel="name"
                        :suggestions="filteredCountries"
                        @complete="search"
                      >
                        <template #option="slotProps">
                          <div class="flex items-center">
                            <img
                              :alt="slotProps.option.name"
                              src="https://primefaces.org/cdn/primevue/images/flag/flag_placeholder.png"
                              :class="`flag flag-${slotProps.option.code.toLowerCase()} mr-2`"
                              style="width: 18px"
                            />
                            <div>{{ slotProps.option.name }}</div>
                          </div>
                        </template>
                      </AutoComplete>
                    </div>
                  </div>
                  <!-- Videos -->
                  <div class="videos" v-if="activeTab === '5'">Videos</div>
                  <!-- Chick-in -->
                  <div class="chick_in" v-if="activeTab === '6'">Chick-in</div>
                  <!-- More -->
                  <div class="More" v-if="activeTab === '7'">More</div>
                </div>
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
import { useUserStore } from '@/stores/user'

export default {
  name: 'ProfileView',

  setup() {
    return {}
  },

  data() {
    return {
      // User Opene Facebook His Data
      user: {
        id: ''
      },
      // التنقل بين التابات
      activeTab: '1',
      activeTabAbout: '1',
      // Edite Profile Name
      formEditeProfileName: {
        name: ''
      },
      errorsEditeProfileName: [],
      // Edite Profile Email
      activeTabEditeEmail: '1',
      formEditeProfileEmail: {
        email: ''
      },
      errorsEditeProfileEmail: [],

      //
      //
      //
      //

      posts: [],
      can_send_friendship_request: null,
      activeTabFriend: '1',
      isFriend: false,
      friends_accepted: [],
      friends_siven: [],
      friends_nine: [],
      // User Waiting
      userSendToBeFriend: false,
      friends_waiting: [],
      // Edite  Profile
      // formWorkplace: {
      //   workplace_company: this.userStore.user.workplace_company,
      //   workplace_position: this.userStore.user.workplace_position,
      //   workplace_city_town: this.userStore.user.workplace_city_town,
      //   workplace_description: this.userStore.user.workplace_description,
      //   workplace_time_period: this.userStore.user.workplace_time_period,
      //   email: this.userStore.user.email
      // },
      errorsWorkplace: [],
      showAddAWorkpolace: false,
      //
      countries: null,
      selectedCountry: null,
      filteredCountries: null
      //
    }
  },

  mounted() {
    // التأكد من أن بيانات المستخدم موجودة قبل محاولة الوصول إليها
    const userStore = useUserStore()
    if (userStore.user && userStore.user.name) {
      this.formEditeProfileName.name = userStore.user.name
    }

    if (userStore.user && userStore.user.email) {
      this.formEditeProfileEmail.email = userStore.user.email
    }
    this.getProfile()
    // this.getFriends()
    // this.getFriendsSiven()
    // this.getFriendsNine()
    // this.getFriendsAccepted()
    // this.getFriendsWaiteng()
    // CountryService.getCountries().then((data) => (this.countries = data))
  },

  watch: {
    '$route.params.id': {
      handler: function () {
        this.getProfile()
      },
      deep: true,
      immediate: true
    }
  },

  methods: {
    getProfile() {
      axios
        .get(`/api/profile/${this.$route.params.id}/`)
        .then((response) => {
          this.user = response.data.user
          console.log('this.user: ', this.user.id)
          // For Test
          // console.log('profile user: ', response.data.user)
          // this.$toast.add({
          //   severity: 'success',
          //   summary: `Welcome`,
          //   detail: `${response.data.user.name}`,
          //   life: 3000
          // })
        })
        .catch((error) => {
          console.error('error', error)
          this.$toast.add({
            severity: 'error',
            summary: `Error Profile`,
            detail: `${error.message}`,
            life: 3000
          })
        })
    },
    submitFormEditeProfileName() {
      console.log(`Yes`)
    },
    submitFormEditeProfileEmail() {
      console.log(`Yes`)
      // this.errorsEditeProfile = []

      // if (this.formEditeProfileEmail.email === '') {
      //   this.errorsEditeProfile.push('Your e-mail is missing')
      //   this.$toast.add({
      //     severity: 'error',
      //     summary: 'User Name missing',
      //     detail: 'Your name is missing',
      //     life: 3000
      //   })
      // }
      // if (this.errorsEditeProfile.length === 0) {
      //   let formData = new FormData()
      //   console.log(`Yes`)
      //   formData.append('email', this.formEditeProfile.email)
      //   axios
      //     .post('/api/editprofile/', formData, {
      //       headers: {
      //         'Content-Type': 'multipart/form-data'
      //       }
      //     })
      //     .then((response) => {
      //       if (response.data.message === 'information updated') {
      //         this.$toast.add({
      //           severity: 'success',
      //           summary: 'Email Updated',
      //           detail: 'Your It Is Email Updated',
      //           life: 3000
      //         })
      //         this.userStore.setUserInfo({
      //           id: this.userStore.user.id,
      //           email: this.formEditeProfile.email
      //         })
      //       } else {
      //         this.$toast.add({
      //           severity: 'error',
      //           summary: 'Try Again',
      //           detail: `${response.data.message}. Please try again`,
      //           life: 3000
      //         })
      //       }
      //     })
      //     .catch((error) => {
      //       console.log('error', error)
      //     })
      // }
    },
    // ________________________________________
    // ________________________________________
    // ________________________________________
    // ________________________________________
    // ________________________________________
    search(event) {
      setTimeout(() => {
        if (!event.query.trim().length) {
          this.filteredCountries = [...this.countries]
        } else {
          this.filteredCountries = this.countries.filter((country) => {
            return country.name.toLowerCase().startsWith(event.query.toLowerCase())
          })
        }
      }, 250)
    },

    sendDirectMessage() {
      console.log('sendDirectMessage')
      axios
        .get(`/api/chat/${this.$route.params.id}/get-or-create/`)
        .then((response) => {
          console.log(response.data)

          this.$router.push('/chat')
        })
        .catch((error) => {
          console.log('error', error)
        })
    },
    sendFriendshipRequest() {
      axios
        .post(`/api/friends/${this.$route.params.id}/request/`)
        .then((response) => {
          // console.log('data', response.data)

          this.can_send_friendship_request = false

          if (response.data.message == 'request already sent') {
            // this.toastStore.showToast(5000, 'The request has already been sent!', 'bg-red-300')
          } else {
            // this.toastStore.showToast(5000, 'The request was sent!', 'bg-emerald-300')
          }
        })
        .catch((error) => {
          console.log('error', error)
        })
    },
    getFriends() {
      axios
        .get(`/api/friends/${this.$route.params.id}/`)
        .then((response) => {
          // console.log('friends data', response.data)
          // console.log('friends data id', response.data.user.id)
          // تحقق مما إذا كان هناك أصدقاء موجودون
          if (response.data.friends.length > 0) {
            // تحقق من وجود المستخدم الحالي بين الأصدقاء
            // const isFriend = response.data.friends.some(
            //   (friend) => friend.id === this.currentUser.id
            // )
            // this.isFriend = true
            // console.log('User Is Friend: ', this.isFriend)
          }
        })
        .catch((error) => {
          console.log('error', error)
        })
    }
    //
    // getFriendsSiven() {
    //   axios
    //     .get(`/api/friends/${this.$route.params.id}/`)
    //     .then((response) => {
    //       // console.log('friends data', response.data)
    //       const allFriends = response.data.friends

    //       // تحقق مما إذا كان هناك أصدقاء موجودون
    //       if (allFriends.length > 0) {
    //         this.friends_siven = this.getRandomFriends(allFriends, 7)
    //       }
    //     })
    //     .catch((error) => {
    //       console.log('error', error)
    //     })
    // },
    // getFriendsNine() {
    //   axios
    //     .get(`/api/friends/${this.$route.params.id}/`)
    //     .then((response) => {
    //       // console.log('friends data', response.data)
    //       const allFriends = response.data.friends

    //       // تحقق مما إذا كان هناك أصدقاء موجودون
    //       if (allFriends.length > 0) {
    //         this.friends_nine = this.getRandomFriends(allFriends, 9)
    //       }
    //     })
    //     .catch((error) => {
    //       console.log('error', error)
    //     })
    // },
    // getRandomFriends(friendsArray, count) {
    //   return friendsArray
    //     .map((value) => ({ value, sort: Math.random() }))
    //     .sort((a, b) => a.sort - b.sort)
    //     .map(({ value }) => value)
    //     .slice(0, count)
    // },
    // getFriendsAccepted() {
    //   axios
    //     .get(`/api/friends_accepted/${this.$route.params.id}/`)
    //     .then((response) => {
    //       this.friends_accepted = response.data.friends
    //       // console.log('Friends Accepted: ', response.data.friends)
    //       // console.log('response.data.friends_accepted: ', response.data.friends.id)
    //       let allFriends = response.data.friends
    //       allFriends.forEach((element) => {
    //         // console.log('allFriends: ', allFriends)
    //         // console.log('element: ', element.id)
    //         // console.log('this.$route.params.id: ', this.$route.params.id)
    //         if (element.id == this.$route.params.id) {
    //           // console.log(`Yes`)
    //         } else {
    //           // console.log(`No`)
    //         }
    //         // element.onclick = function () {
    //         //   // Print The Element Click To It
    //         //   console.log(this)
    //         //   // Removing Class Active From All Element
    //         //   allLis.forEach((element) => {
    //         //     element.classList.remove('active')
    //         //   })
    //         //   // Adding Class Active To Dive Have The Sima Data Elemen
    //         //   allDiv.forEach((ele) => {
    //         //     return ele.getAttribute('data-name') === this.getAttribute('data-text')
    //         //       ? ele.classList.add('active')
    //         //       : ele.classList.remove('active')
    //         //   })
    //         //   // Adding Class Active To This Element
    //         //   this.classList.add('active')
    //         // }
    //       })
    //       for (let index = 0; index < response.data.friends; index++) {
    //         console.log('index: ', [index])
    //         // const element = response.data.friends[index]
    //         // console.log('element: ', element)
    //       }
    //       this.user = response.data.user
    //       // console.log('response.data.user: ', response.data.user)
    //       // console.log(`user I Viset `, this.$route.params.id)
    //     })
    //     .catch((error) => {
    //       console.log('error', error)
    //     })
    // },
    // getFriendsWaiteng() {
    //   axios
    //     .get(`/api/friends_waiting/${this.$route.params.id}/`)
    //     .then((response) => {
    //       this.friends_waiting = response.data.friends
    //       this.userSendToBeFriend = true
    //       // console.log('Friends Waiting : ', response.data.friends)
    //       this.user = response.data.user
    //     })
    //     .catch((error) => {
    //       console.log('error', error)
    //     })
    // },
    // windowReload() {
    //   window.location.reload()
    // },
    // toggleShowAddAWorkplace() {
    //   this.showAddAWorkpolace = true
    // },
    // toggleHideAddAWorkplace() {
    //   this.showAddAWorkpolace = false
    // }
    // submitFormWorkplace() {
    //   this.errorsWorkplace = []

    //   if (this.formWorkplace.workplace_description === '') {
    //     this.errorsWorkplace.push('Your description is missing')
    //   }

    //   if (this.errorsWorkplace.length === 0) {
    //     let formData = new FormData()
    //     formData.append('workplace_company', this.formWorkplace.workplace_company)
    //     formData.append('workplace_position', this.formWorkplace.workplace_position)
    //     formData.append('workplace_city_town', this.formWorkplace.workplace_city_town)
    //     formData.append('workplace_description', this.formWorkplace.workplace_description)
    //     formData.append('workplace_time_period', this.formWorkplace.workplace_time_period)
    //     formData.append('email', this.formWorkplace.email)
    //     console.log('formData: ', formData)

    //     axios
    //       .post('/api/editprofile/', formData, {
    //         headers: {
    //           'Content-Type': 'multipart/form-data'
    //         }
    //       })
    //       .then((response) => {
    //         console.log('response.data.message: ', response.data.message)
    //         if (response.data.message === 'information updated') {
    //           // this.toastStore.showToast(5000, 'The information was saved', 'bg-emerald-500')
    //           this.userStore.setUserInfo({
    //             id: this.userStore.user.id,
    //             workplace_company: this.formWorkplace.workplace_company,
    //             workplace_position: this.formWorkplace.workplace_position,
    //             workplace_city_town: this.formWorkplace.workplace_city_town,
    //             workplace_description: this.formWorkplace.workplace_description,
    //             workplace_time_period: this.formWorkplace.workplace_time_period
    //           })
    //           // this.$router.back()
    //         } else {
    //           // this.toastStore.showToast(
    //           //   5000,
    //           //   `${response.data.message}. Please try again`,
    //           //   'bg-red-300'
    //           // )
    //         }
    //       })
    //       .catch((error) => {
    //         console.log('error', error)
    //       })
    //   }
    // }
  }
}
</script>

<!-- 
send
accepted
rejected
waiting
-->
