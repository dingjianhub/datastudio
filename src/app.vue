<template>
    <div>
        {{msg}}
    </div>
</template>

<script>
export default {
    data(){
        return {msg: "这是app.vue"}
    }
}
</script>

<style scoped>
    div{
        background: gainsboro;
    }
</style>