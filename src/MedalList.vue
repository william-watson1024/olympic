<template>
  <div id="medalList">
    <!-- Back button to navigate to HomePage -->
    <div class="back-button">
      <router-link to="/" class="back-link">
        <img src="@/assets/logo/back.png" alt="Back" class="back-image" />
      </router-link>
    </div>

    <img src="@/assets/logo/olympicsring.png" alt="Olympic Logo" class="olympic-logo" />

    <div class="top">
      <h1>Medals For Paris Olympics</h1>
      <h2>巴黎奥运会奖牌榜</h2>
    </div>

    <div class="headerContainer">
      <!-- Existing code for medal table -->
    </div>

    <div class="container">
      <RankItem v-for="(item, index) in items" :key="index" :rank="item.rank" :flag="item.flag"
                :countryName="item.countryname" :gold="item.gold" :silver="item.silver"
                :bronze="item.bronze" :total="item.count" />
    </div>
  </div>
</template>

<script>
import RankItem from './components/RankItem.vue';
import axios from 'axios';

export default {
  name: 'medalList',
  components: {
    RankItem
  },
  data() {
    return {
      items: []
    };
  },
  mounted() {
    this.fetchRankList();
  },
  methods: {
    async fetchRankList() {
      try {
        const response = await axios.get('./json/medal.json');
        this.items = response.data;
      } catch (error) {
        console.error('Error fetching rank list:', error);
      }
    }
  }
};
</script>

<style>
#medalList {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  font-size: 14px;
  text-align: center;
  color: #2c3e50;
  background-image: url('@/assets/background/sea.jpg');
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
}

.back-button {
  text-align: left; /* Align the back button to the left */
  margin: 10px; /* Add some margin for spacing */
}

.back-link {
  color: #42b983; /* Link color */
  text-decoration: none; /* Remove underline */
  font-size: 18px; /* Font size */
}

.back-image {
  width: 90px; /* Set width of the image */
  height: auto; /* Maintain aspect ratio */
}

/* Other existing styles */
.container {
  width: 100%;
  max-width: 800px;
  margin: 0 auto;
}

.headerContainer {
  width: 100%;
  max-width: 800px;
  margin: 0 auto;
  display: flex;
  justify-content: center;
}

.header-row {
  width: 600px;
  padding: 10px;
  align-items: center;
  background-color: rgba(255, 255, 255, 0);
  border-radius: 8px;
  margin-bottom: 5px;
  color: white;
  font-weight: bold;
}

.rank-item-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.flag-img {
  border-radius: 20%;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
  border: 1px solid #ccc;
}

h1,
h2 {
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
