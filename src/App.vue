<template>
  <div id="app">
 
    <div class="container">
    <RankItem
      :rank="1"
      flag="https://upload.wikimedia.org/wikipedia/en/a/a4/Flag_of_the_United_States.svg"
      countryName="美利坚合众国"
      :gold="40"
      :silver="44"
      :bronze="42"
      :total="126"
      @add="onAdd"
    />
  </div>
    
  </div>
  
</template>
 
<script>
  // 导入组件
  import RankItem from './components/RankItem.vue';
export default {
  name: 'app',
  data () {
    return {
    }
  },
  components:{
    RankItem
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