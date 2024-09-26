<template>

  <div>
    <div>
      <DatePicker @date-selected="handleDateSelected" />
      <p>选中的日期是: {{ selectedDate }}</p>
    </div>
    <!-- 使用 MatchTableItem 组件并传递 props -->
    <MatchTableItem :score="score" />
  </div>
</template>

<script>
import MatchTableItem from './components/MatchTableItem.vue';
import DatePicker from './components/DatePicker.vue';

export default {
  components: {
    MatchTableItem,
    DatePicker
  },
  data() {
    return {
      selectedDate: null,
    };
  },
  methods: {
    handleDateSelected(date) {
      const formattedDate = date.replace(/月|日/g, '').padStart(4, '0');
      this.selectedDate = formattedDate;
    },
    async fetchRankList() {
      try {
        const response = await axios.get('./json/medal.json'); // 确保路径正确
        console.log('Rank list:', response.data);
        this.items = response.data;
      } catch (error) {
        console.error('Error fetching rank list:', error);
      }
    },
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
  margin-top: 60px;
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