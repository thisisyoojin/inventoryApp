import { createRouter, createWebHistory } from 'vue-router'
import SideNav from '@/components/SideNav.vue'
import Dashboard from '@/pages/Dashboard.vue'
import Todo from '@/pages/Todo.vue'
import Inventory from '@/pages/Inventory.vue'
import Itemhistory from '@/pages/Itemhistory.vue'
import Admin from '@/pages/Admin.vue'

const routes = [
    {
        path: '/',
        name: 'Dashboard',
        components: {
            default: Dashboard,
            SideNav: SideNav
        },
    },
    {
        path: '/:restaurant/inventory',
        name: 'Inventory',
        components: {
            default: Inventory,
            SideNav: SideNav
        },
    },
    {
        path: '/:restaurant/todo',
        name: 'Todo',
        components: {
            default: Todo,
            SideNav: SideNav
        },
    },
    {
        path: '/:restaurant/history',
        name: 'Itemhistory',
        components: {
            default: Itemhistory,
            SideNav: SideNav
        },
    },
    {
        path: '/admin',
        name: 'Admin',
        component: Admin
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router