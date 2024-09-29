import Vue from 'vue';
import Router from 'vue-router';
import HomePage from '@/HomePage.vue';
import MedalList from '@/MedalList.vue';
import MoreDetail from '@/MoreDetail.vue';
import MatchList from '@/MatchList.vue';
import MainMatch_man from '@/MainMatch_man.vue';
import DetailRating from '@/DetailRating.vue';
import OlympicAthletes from '@/OlympicAthletes.vue';


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
    },
    {
        path: '/mainMatch',
        name: 'MainMatch_mant',
        component: MainMatch_man
    },
    {
        path: '/rating',
        name: 'DetailRating',
        component: DetailRating

    },
    {
        path: '/Athletes',
        name: 'OlympicAthletes',
        component: OlympicAthletes
    }
  ]
});
