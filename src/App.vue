<template>
  <div>
    <div>
      <DatePicker @date-selected="handleDateSelected" />
      <p>选中的日期是: {{ selectedDate }}</p>
    </div>
    <!-- 使用 MatchTableItem 组件并传递 props -->

    <div class="container">
      <MatchTableItem v-for="(item, index) in items" :key="index" :time="item.startDate" :event="item.event" :disciplineName="item.disciplineName"      
        :team1="{
        name: item.competitors[0].name,
        flag: item.competitors[0].noc,
        score: item.competitors[0].mark
        }"
        :team2="{
        name: item.competitors[1].name,
        flag: item.competitors[1].noc,
        score: item.competitors[1].mark
        }"
        />
    </div>
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
      const formattedDate = date.replace(/月|日/g, '').padStart(4, '0');
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