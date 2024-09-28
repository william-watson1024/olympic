import Vue from 'vue';
import Router from 'vue-router';
import HomePage from '@/HomePage.vue';
import MedalList from '@/MedalList.vue';
import MoreDetail from '@/MoreDetail.vue';
import MatchList from '@/MatchList.vue';


Vue.use(Router);

export default new Router({
  mode: 'history',  // Enables history mode for cleaner URLs
  routes: [
    {
      path: '/',
      name: 'HomePage',
      component: HomePage
    },
    {
      path: '/medals',
      name: 'MedalList',
      component: MedalList
    },
    {
        path: '/more',
        name: 'MoreDetail',
        component: MoreDetail
    },
    {
        path: '/matchList',
        name: 'MatchList',
        component: MatchList
    }
  ]
});
