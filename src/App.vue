<template>
  <div id="app">
    <div class="container">
      <RankItem
        v-for="(item, index) in items"
        :key="index"
        :rank="item.rank"
        :flag="item.flag"
        :countryName="item.countryname"
        :gold="item.gold"
        :silver="item.silver"
        :bronze="item.bronze"
        :total="item.count"
        @add="onAdd"
      />
    </div>
  </div>
</template>

<script>
import RankItem from './components/RankItem.vue';
import axios from 'axios';

export default {
  name: 'app',
  data () {
    return {
      items: []
    }
  },
  components: {
    RankItem
  },
  mounted() {
    this.fetchRankList();
  },
  methods: {
    async fetchRankList() {
      try {
        const response = await axios.get('./json/medal.json'); // 确保路径正确
        console.log('Rank list:', response.data);
        this.items = response.data;
      } catch (error) {
        console.error('Error fetching rank list:', error);
      }
    },
    onAdd() {
      console.log('Add event triggered');
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  font-size: 14px;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>