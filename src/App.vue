<template>
  <div id="app">
    {{msg}}
 
    <!--图标-->
    <div>
      <el-row>
        <el-button>默认按钮</el-button>
        <el-button type="primary">主要按钮</el-button>
        <el-button type="success">成功按钮</el-button>
        <el-button type="info">信息按钮</el-button>
        <el-button type="warning">警告按钮</el-button>
        <el-button type="danger">危险按钮</el-button>
        <el-button type="primary" icon="el-icon-search">搜索</el-button>
      </el-row>
    </div>
    <div>
        <rank-item 
          :rank="1" 
          flag="https://upload.wikimedia.org/wikipedia/en/a/a4/Flag_of_the_United_States.svg"
          countryName="美利坚合众国" 
          :gold="40" 
          :silver="44" 
          :bronze="42" 
          :total="126"
          @add="onAdd">
        </rank-item>
      </div>
    <!-- 日期选择器 -->
    <DatePicker></DatePicker>
    <!-- 文件上传 -->
    <UploadFile></UploadFile>
    
  </div>
  
</template>
 
<script>
  // 导入组件
  import DatePicker from './components/DatePicker.vue'
  import UploadFile from './components/UploadFile.vue'
  import RankItem from './components/RankItem.vue';
export default {
  name: 'app',
  data () {
    return {
      msg: '测试msg'
    }
  },
  components:{
    DatePicker,
    UploadFile
  }
}
</script>
 
<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
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