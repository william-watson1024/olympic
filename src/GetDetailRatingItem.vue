<template>
  <div class="backgrouond">
    <div id="app">
      <router-view></router-view>
    </div>
    <div>
      <ButtonGroup @button-selected="handleButtonSelected" />
    </div>
    <!-- 使用 DetailRatingItem 组件并传递 props -->
    <div class="container">
      <DetailRatingItem
        v-for="(item, index) in items"
        :key="index"
        :matchInfo="matchInfo"
        :match-number="matchNumber"
        :teams="{
            name: item.team1.name,
            flag: item.team1.flag,
            score: item.team1.score
        }"
        :matchTime="matchTime"
        :matchStatus="matchStatus"
      >
      </DetailRatingItem>
    </div>
  </div>
</template>

<script>
import DetailRatingItem from './components/DetailRatingItem.vue';
import axios from 'axios';
import ButtonGroup from './components/ButtonGroup.vue';

export default {
  components: {
    DetailRatingItem,
    ButtonGroup
  },
  data() {
    return {
      selectedDate: 'A组',
      items: [],
      matchInfo: '', // 初始化 matchInfo
      matchTime: '', // 初始化 matchTime
      matchStatus: '' // 初始化 matchStatus
    };
  },
  mounted() {
    this.fetchMatchList();
  },
  methods: {
    handleDateSelected(date) {
      const formattedDate = date.replace(/月|日/g, '').padStart(4, '0');
      this.selectedDate = formattedDate;
      this.fetchMatchList();
    },
    async fetchMatchList() {
      try {
        const response = await axios.get(`./json/${this.selectedDate}.json`);
        this.items = response.data;
        // 假设 response.data 中包含 matchInfo、matchTime 和 matchStatus
        this.matchInfo = response.data.matchInfo;
        this.matchTime = response.data.matchTime;
        this.matchStatus = response.data.matchStatus;
      } catch (error) {
        console.error('Error fetching match list:', error);
      }
    }
  },
  watch: {
    selectedDate() {
      this.fetchMatchList();
    }
  }
};
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  font-size: 14px;
  text-align: center;
  color: #2c3e50;
  
}
.backgrouond{
  background-image: url('@/assets/background/football.jpeg'); /* 设置背景图片 */
  background-size: cover; /* 背景图片覆盖整个容器 */
  background-position: center; /* 背景图片居中 */
  background-attachment: fixed; /* 背景图片固定 */

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
