<template>
    <div class="input-group mb-3">
        <input type="text" class="form-control" placeholder="Search" aria-label="Search"
            aria-describedby="search" v-model.lazy="keyword">
        <div class="input-group-append">
            <span class="input-group-text" id="search" @click="onClickSearch">Search</span>
        </div>
    </div>
</template>

<script>

export default {
    data() {
        return {
            keyword: '',
            searchData: []
        }
    },
    props: {
        endpoint: {
            type: String,
            required: true
        }
    },
    watch: {
        keyword: {
            handler(newKeyword) {
                console.log(this.endpoint)
                this.searchData = [{
                    "item_id": 5,
                    "item_name": "searchResult",
                    "restaurant_id": 1,
                    "seller_id": null,
                    "current_count": 13,
                    "created_on": "2023-07-21"
                }]
            },
            deep: true
        }
    },
    emits: ["keywordChanged"],
    methods: {
        onClickSearch() {
            this.$emit("keywordChanged", this.searchData)
            this.keyword = ''
        }
    }
}

</script>