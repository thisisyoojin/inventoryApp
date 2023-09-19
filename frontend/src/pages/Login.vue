<template>
    <div class="form">
        <div class="form-signin">
            <img class="mb-4" src="@/assets/logo.png" width="72" height="72">
            <h1 class="h3 mb-3 fw-normal">Please sign in</h1>
            <div class="form-floating">
                <input type="text" v-model.lazy="username" class="form-control" id="floatingInput"
                    placeholder="name@example.com">
                <label for="floatingInput">Username</label>
            </div>
            <div class="form-floating">
                <input type="password" v-model.lazy="password" class="form-control" id="floatingPassword"
                    placeholder="Password">
                <label for="floatingPassword">Password</label>
            </div>

            <button class="w-100 btn btn-lg btn-primary" @click="onClickLogin">Sign in</button>
            <p>Forgot password?</p>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    data() {
        return {
            username: '',
            password: ''
        }
    },
    emits: ['authSubmitted'],
    methods: {
        checkAuth() {
            // axios.get("") send request with id and password
            return {
                isUser: true,
                isAdmin: true
            }
        },
        async onClickLogin() {
            const returnedAuth = await this.checkAuth()
            this.$emit('authSubmitted', returnedAuth)
            this.$router.push('/')
        }
    }
}
</script>


<style>
.form {
    height: 100%;
    display: flex;
    align-items: center;
    padding-top: 40px;
    padding-bottom: 40px;
    background-color: #f5f5f5;
    text-align: center !important;
}

.form-signin {
    width: 100%;
    max-width: 330px;
    padding: 15px;
    margin: auto;
}

.form-signin .form-floating:focus-within {
    z-index: 2;
}

.form-signin input[type="email"] {
    margin-bottom: -1px;
    border-bottom-right-radius: 0;
    border-bottom-left-radius: 0;
}

.form-signin input[type="password"] {
    margin-bottom: 10px;
    border-top-left-radius: 0;
    border-top-right-radius: 0;
}
</style>