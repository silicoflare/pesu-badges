<template>
    <div class="flex flex-col justify-center text-center font-2xl p-10 font-['Montserrat']">
        <h1 class="text-7xl font-['Zilla_Slab']">PESU Badges</h1>
        <br>
        <p class="text-2xl">
            Badges of PESU and its clubs to flex on your GitHub README!!
        </p>
        <br><br>
        <div class="grid grid-cols-4 gap-5 text-center justify-center">
            <Badge v-for="f in data" :name="f" />
        </div>
    </div>
</template>

<script>
    import axios from 'axios';
    import Badge from './components/Badge.vue';

    export default {
        data() {
            return {
                data: null,
            }
        },
        components: {
            Badge
        },
        mounted() {
            const apiUrl = 'https://pesu-badges-api.vercel.app/badgelist';

            axios.get(apiUrl)
            .then(response => {
                this.data = response.data['files'];
                console.log(response.data['files']);
            })
            .catch(error => {
                console.error('Error fetching data:', error);
            });
  },
    }
</script>