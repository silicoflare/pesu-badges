<template>
    <div class="w-[15rem] h-[15rem] m-auto p-5 text-2xl flex flex-col justify-center items-center border-2 border-black" 
    @click="navigator.clipboard.writeText(`<img src='https://pesu-badges-api.vercel.app/badge/${name}' width='98px' height='30px' />`)">
        <img :src='`https://pesu-badges-api.vercel.app/badge/${name}`' width="98px" height="30px" class="w-max h-auto"/><br>
        <span>{{ name }}</span>
    </div>
</template>

<script>
    export default {
        props: ['name']
    }
</script>