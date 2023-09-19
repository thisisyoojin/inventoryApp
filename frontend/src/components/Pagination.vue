<template>
    <span>Total {{ totalPages }} pages</span>
    <ul class="pagination">
        <li class="page-item">
            <button class="page-link" :class="isInFirstPage?'disabled':''" @click="onClickFirstPage" :disabled="isInFirstPage">First</button>
        </li>
        <li class="page-item">
            <button class="page-link" :class="isInFirstPage?'disabled':''" @click="onClickPreviousPage" :disabled="isInFirstPage">Previous</button>
        </li>
        <li v-for="page in pages" :key="page.name" class="page-item">
            <button class="page-link" :class="page.isDisabled?'disabled':''" @click="onClickPage(page.name)" :disabled="page.isDisabled">
                {{ page.name }}
            </button>
        </li>
        <li class="page-item">
            <button class="page-link" :class="isInLastPage?'disabled':''" @click="onClickNextPage" :disabled="isInLastPage">Next</button>
        </li>
        <li class="page-item">
            <button class="page-link" :class="isInLastPage?'disabled':''" @click="onClickLastPage" :disabled="isInLastPage">Last</button>
        </li>
    </ul>
</template>
  
<script>
export default {
    props: {
        maxVisibleButtons: {
            type: Number,
            required: false,
            default: 5
        },
        totalPages: {
            type: Number,
            required: true
        },
        perPage: {
            type: Number,
            required: false,
            default: 15
        },
        currentPage: {
            type: Number,
            required: true
        }
    },
    computed: {
        startPage() {
            const pageOffset = Math.floor(this.maxVisibleButtons/2)
            if (this.currentPage <= pageOffset) {
                return 1;
            }
            if (this.currentPage >= (this.totalPages - pageOffset)) {
                return Math.max(1, this.totalPages - this.maxVisibleButtons + 1)
            } 
            return this.currentPage - pageOffset
        },
        pages() {
            const range = [];
            for (
                let i = this.startPage;
                i <= Math.min(this.startPage + this.maxVisibleButtons - 1, this.totalPages);
                i++
            ) {
                range.push({
                    name: i,
                    isDisabled: i === this.currentPage
                });
            }
            return range;
        },
        isInFirstPage() {
            return this.currentPage === 1;
        },
        isInLastPage() {
            return this.currentPage === this.totalPages;
        },
    },
    emits: ["pageChanged"],
    methods: {
        onClickFirstPage() {
            this.$emit('pageChanged', 1);
        },
        onClickPreviousPage() {
            this.$emit('pageChanged', Math.max(1, this.currentPage - 1));
        },
        onClickPage(page) {
            console.log(page)
            this.$emit('pageChanged', page);
        },
        onClickNextPage() {
            this.$emit('pageChanged', Math.min(this.totalPages, this.currentPage + 1));
        },
        onClickLastPage() {
            this.$emit('pageChanged', this.totalPages);
        }
    }
};
</script>