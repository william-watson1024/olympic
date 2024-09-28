import Vue from 'vue'
import ElementUI from 'element-ui';                      // 引入element-ui
import router from './router';
import 'element-ui/lib/theme-chalk/index.css';           // element-ui的css样式要单独引入
//mport GetMatchList from './GetMatchList.vue'
// import MedalList from './MedalList.vue';
// import MatchList from './MatchList.vue';
// import MoreDetail from './MoreDetail.vue';
// import HomePage from './HomePage.vue';
//import MainMatch_man from './MainMatch_man.vue';
// import App from './App.vue';
import DetailRating from './DetailRating.vue';

 
Vue.use(ElementUI);   // 这种方式引入了ElementUI中所有的组件
 
new Vue({
  el: '#app',
  router, // Ensure that router is passed here
  // render: h => h(App)
  render: h => h(DetailRating)
});


