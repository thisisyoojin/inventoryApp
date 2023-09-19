<template>
  <div class="inventory">
    <div class="row p-3">
      <h3 class="col">Inventory Check</h3>
      <Search endpoint="/inventory" @keywordChanged="onKeywordChanged"/>
    </div>
    <div class="itemsList">
      <div class="container text-centered">
        <div class="row m-1" v-if="displayedItems.length>0" v-for="item in displayedItems" :key="item.item_id">
          <p class="col-5" v-on:click="set_count(1)">{{ item.item_name }}</p>
          <div class="row col-4"></div>
          <input type="number" class="col-3" v-model.lazy="item.current_count">
        </div>
        <div v-else>
          <span>There is no search result</span>
        </div>
      </div>
    </div>
    <Pagination :totalPages="totalPages" :currentPage="currentPage" @pageChanged="onPageChange" />
  </div>
</template>

<script>
import { ref } from 'vue'
import axios from 'axios'
import itemsData from '../temp/item.json'
import Pagination from '@/components/Pagination.vue'
import Search from '@/components/Search.vue'
import Constant from '@/helpers/constants'

export default {
  components: {
    Pagination,
    Search
  },
  data() {
    return {
      items: ref([]),
      filteredItems: ref([]),
      currentPage: 1,
      perPage: Constant.PER_PAGE,
      totalPages: 1,
      searchKeyword: ''
    }
  },
  mounted() {
    this.get_data();
  },
  computed: {
    restaurant() {
      return this.$route.params.restaurant
    },
    displayedItems() {
      const startIndex = this.perPage * (this.currentPage - 1)
      const endIndex = startIndex + this.perPage
      if (this.searchKeyword) {
        return this.filteredItems.slice(startIndex, endIndex)
      }
      return this.items.slice(startIndex, endIndex)
    }
  },
  watch: {
    items: {
      handler(newItems, oldItems) {
        if (oldItems.length === 0) {
          return
        }
        console.log("Sending to postgresql", newItems.length) //send it to postgresql
      },
      deep: true
    }
  },
  methods: {
    onKeywordChanged(searchResult) {
      this.filteredItems = searchResult
    },
    onPageChange(page) {
      this.currentPage = page;
    },
    get_data() {
      this.items = itemsData.results
      this.totalPages = Math.floor(this.items.length/this.perPage) + 1
      // axios({
      //   method: 'get',
      //   url: 'http://127.0.0.1:8000/items/',
      //   auth: {
      //     username: 'admin',
      //     password: 'test1234'
      //   }
      // }).then(response => this.items = response.data);
    },
    set_count(id) {
      console.log(this.items)
      // axios({
      //   method: 'patch',
      //   url: `http://127.0.0.1:8000/items/${id}/`,
      //   auth: {
      //     username: 'admin',
      //     password: 'test1234'
      //   },
      //   data: {
      //     'count': this.items[id-1].count + 1
      //   }
      // }).then(() => { this.items = this.get_items() });
    }
  }
}
</script>
