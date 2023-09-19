<template>
  <div class="container m-3">
    
    <h3>Todo List</h3>
    <h5>Last time updated: 05-08-2023</h5>
  
    <div class="todoList">
      <div>
        <div class="row m-1" v-for="todo in todos" :key="todo.id">
          <div class="col-1">
          <input type="checkbox" class="affix" v-model="todo.status">
        </div>
          <p class="col-10">
            <span>{{ todo.description }}</span>
            <button @click="showEditModal(todo.id)">Edit</button>
            <button @click="confirmDelete(todo.id)">Delete</button>
          </p>
        </div>
      </div>
      <Modal v-if="showModal" @close="showModal = false"></Modal>
    </div>
    <Pagination :totalPages="totalPages" :currentPage="currentPage" @pageChanged="onPageChange" />
  </div>
</template>

<script>
import { ref, watchEffect } from 'vue'
import axios from 'axios'
import todosData from '../temp/todo.json'
import Pagination from '@/components/Pagination.vue'
import Modal from '@/components/Modal.vue'

export default {
  components: {
    Pagination,
    Modal
  },
  data() {
    return {
      todos: ref([]),
      currentPage: 1,
      totalPages: 1,
      showModal: false
    }
  },
  mounted() {
    this.get_data()
  },
  computed: {
    restaurant() {
      return this.$route.params.restaurant
    }
  },
  watch: {
    todos: {
      handler: (newTodos, oldTodos) => {
        if (oldTodos.length === 0) {
          return
        }
        console.log("Sending new Todos", newTodos) //send request to postgresql
      },
      deep: true
    }
  },
  methods: {
    onPageChange(page) {
      this.currentPage = page;
    },
    get_data() {
      this.todos = todosData.results //axios to read data from api
    },
    showEditModal(el) {
      this.showModal = true
    },
    confirmDelete(el) {
      this.showModal = true
    }
  }
}
</script>