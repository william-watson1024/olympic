<template>
  <div id="medalList">
    <img src="@/assets/logo/olympicsring.png" alt="Olympic Logo" class="olympic-logo" style="width: 200px; height: 100px;">
    <div class="top" style="display: flex;justify-content: center;">
    <div class="topContainer" style="border-radius: 10px; background-color: rgba(255, 255, 255, 0.3);display: flex;justify-content: center;width:600px;">
      <div class="header">
        <div class="title" style="color: white;">
          <h1>Medals For Paris Olympics</h1>
          <h2>巴黎奥运会奖牌榜</h2>
        </div>
      </div>
    </div>
  </div>
    <div class="headerContainer">
      <!-- 表头行 -->
      <div class="header-row" align="middle" type="flex">
        <el-row align="middle" type="flex" justify="center">
        <!-- 排名 -->
        <el-col :span="4">
          <span>排名</span>
        </el-col>
        <!-- 国旗 -->
        <el-col :span="2">
          <span>NOC</span>
        </el-col>
        <!-- 国家名称 -->
        <el-col :span="8">
          <span>国家</span>
        </el-col>
        <!-- 奖牌数量 -->
        <el-col :span="2">
          <span>金</span>
        </el-col>
        <el-col :span="2">
          <span>银</span>
        </el-col>
        <el-col :span="2">
          <span>铜</span>
        </el-col>
        <el-col :span="2">
          <span>总数</span>
        </el-col>
        <el-col :span="2">
        </el-col>
      </el-row>
      </div>
    </div>
      <div class="container">
      <!-- 列表项 -->
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
  name: 'medalList',
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
    onAdd() {
      console.log('Add event triggered');
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
}
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

.container {
  width: 100%;
  max-width: 800px;
  margin: 0 auto;

}
.headerContainer {
  width: 100%;
  max-width: 800px;
  margin: 0 auto;
  /* 居中对齐 */
  display: flex;
  justify-content: center;
}

.header-row {
  width: 600px; /* 固定宽度 */
  padding: 10px;
  align-items: center;
  background-color: rgba(255, 255, 255, 0);
  border-radius: 8px;
  margin-bottom: 5px;
  color: white;
  font-weight: bold;
  
  
}

.header-item {
  flex: 1;
  text-align: center;
}

.rank-item-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.rank-col {
  display: flex;
  justify-content: center;
  align-items: center;
}

.flag-col {
  display: flex;
  justify-content: center;
  align-items: center;
}

.flag-img {
  border-radius: 20%;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
  border: 1px solid #ccc;
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