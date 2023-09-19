<script>
import Login from '@/pages/Login.vue'

const sessionStorage = window.sessionStorage;

export default {
  components: {
    Login
  },
  data() {
    return {
      isLogin: false
    }
  },
  mounted() {
    this.checkAuth()
  },
  methods: {
    checkAuth() {
      const isUser = sessionStorage.getItem('isUser')
      this.isLogin = isUser ? isUser : false
    },
    getUserAuth(auth) {
      sessionStorage.setItem('isUser', auth.isUser)
      sessionStorage.setItem('isAdmin', auth.isAdmin)
      this.isLogin = auth.isUser
    }
  }
}
</script>

<template>
    <div v-if="isLogin" class="view row">
      <router-view class="col-3" name="SideNav"></router-view>
      <router-view class="col" style="min-width: 20%;"/>
    </div>
    <div v-else class="view">
      <Login @authSubmitted="getUserAuth"/>
    </div>
</template>

<style>
.view {
  height: 100%;
  width: 100%;
}
</style>