<template>
    <div class="contanier">
        <!-- <button @click="getDatas" >获取数据</button> -->
        <div>
            <ul>
                <li><router-link to="/home">home</router-link></li>
            </ul>
        </div>
        <router-view></router-view>
    </div>
    
</template>

<script>

export default {
}
</script>

