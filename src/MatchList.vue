<template>
  <div class="backgrouond">
    <!-- <pre>{{ items }}</pre> -->
    <div>
      <DatePicker @date-selected="handleDateSelected" />
    </div>
    <!-- 使用 MatchTableItem 组件并传递 props -->

    <div class="container">
      <MatchTableItem v-for="(item, index) in items" :key="index" :time="item.startDate" :event="item.event"
        :edisciplineName="item.disciplineName" :team1="{
          name: item.competitors[0].name,
          flag: item.competitors[0].noc,
          score: item.competitors[0].mark,
          winnerLoserTie: item.competitors[0].winnerLoserTie,
        }" :team2="{
          name: item.competitors[1].name,
          flag: item.competitors[1].noc,
          score: item.competitors[1].mark,
          winnerLoserTie: item.competitors[1].winnerLoserTie,
        }">
      </MatchTableItem>
    </div>
    <div style="height: 200px;"> </div>
  </div>
</template>

<script>
import MatchTableItem from './components/MatchTableItem.vue';
import DatePicker from './components/DatePicker.vue';
import axios from 'axios';

export default {
  components: {
    MatchTableItem,
    DatePicker
  },
  data() {
    return {
      selectedDate: '0725',
      items: []
    };
  },
  mounted() {
    this.fetchMatchList();
  },
  methods: {
    handleDateSelected(date) {
      const formattedDate = date.replace(/(\d+)月(\d+)日/, (match, p1, p2) => {
        const month = p1.padStart(2, '0');
        const day = p2.padStart(2, '0');
        return month + day;
      });
      this.selectedDate = formattedDate;
    },
    async fetchMatchList() {
      try {
        const response = await axios.get(`./json/${this.selectedDate}.json`);
        this.items = response.data;
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

.backgrouond {
  background-image: url('@/assets/background/football.jpeg');
  /* 设置背景图片 */
  background-size: cover;
  /* 背景图片覆盖整个容器 */
  background-position: center;
  /* 背景图片居中 */
  background-attachment: fixed;
  /* 背景图片固定 */
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