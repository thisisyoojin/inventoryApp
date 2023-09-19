<script>
import SideNav from '@/components/SideNav.vue';
import Inventory from '@/pages/Inventory.vue';
import ItemHistory from '@/pages/ItemHistory.vue';
import Todo from '@/pages/Todo.vue';

export default {
  components: {
    SideNav,
    Inventory,
    Todo,
    ItemHistory
  },
  mounted() {
    console.log(this.currentRestaurant)
  },
  computed: {
    currentTab() {
      return this.$route.params.tab
    },
    currentRestaurant() {
      return this.$route.params.restaurant
    }
  }
}
</script>

<template>
  <div>Dashboard</div>
</template>
