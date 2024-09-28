<template>
  <div class="backgrouond">
    <change-button-vue @button-selected="handleButtonSelected"></change-button-vue>
    <div class="choose" v-show="buttonSelected === 0">
      <div class="players-list">
        <div class="team-players">
          <div class="team-title">
            <div style="flex-direction: row;display: flex;">
              <img :src="nationflag1" alt="国旗" style="height: 20px;width: 30px;margin-right:15px;">
              <div class="team-name">{{ nation1 }}</div>
            </div>
            <div class="team-description">出场球员</div>
          </div>
          <ManPositionTitle class="man-position-title" field1Content="NO" field2Content="姓名" field3Content="位置" />
          <ManPosition class="man-position" v-for="(player, index) in items['ARG-MAR'][0].item0" :key="index"
            :field1Content="player.bib" :field2Content="player.name" :field3Content="player.position" />
        </div>

        <div class="team-players">
          <div class="team-title">
            <div style="flex-direction: row;display: flex;">
              <img :src="nationflag2" alt="国旗" style="height: 20px;width: 30px;margin-right:15px;">
              <div class="team-name">{{ nation2 }}</div>
            </div>
            <div class="team-description">出场球员</div>
          </div>
          <ManPositionTitle class="man-position-title" field1Content="NO" field2Content="姓名" field3Content="位置" />
          <ManPosition class="man-position" v-for="(player, index) in items['ARG-MAR'][1].item1" :key="index"
            :field1Content="player.bib" :field2Content="player.name" :field3Content="player.position" />
        </div>
      </div>
    </div>
    <div class="choose" v-show="buttonSelected === 1">
      <SituationItem> </SituationItem>
      <SituationItem v-for="(item, index) in situation['events']" :key="index"
        :field1Content="item.time" :field2Content="item.event" />
    </div>
    <div class="choose" v-show="buttonSelected === 2" style="font-size: 100px;font-weight: bold;">
      <p>还没有做哦宝宝</p>
    </div>
    <div class="choose" v-show="buttonSelected === 3" style="font-size: 100px;font-weight: bold;">
      <p>还没有做哦宝宝</p>
    </div>

  </div>
</template>

<script>
// import DetailRatingItem from './components/DetailRatingItem.vue';
// import ButtonGroup from './components/ButtonGroup.vue';
import ChangeButtonVue from './components/ChangeButton.vue';
import ManPosition from './components/ManPosition.vue';
import ManPositionTitle from './components/ManPositionTitle.vue';
// import CombinedMatch from './components/CombinedMatch.vue';
import SituationItem from './components/SituationItem.vue';
import axios from 'axios';


export default {
  components: {
    // DetailRatingItem,
    // ButtonGroup,
    ChangeButtonVue,
    ManPosition,
    ManPositionTitle,
    SituationItem,
    // CombinedMatch
  },
  data() {
    return {
      nation1: "ARG 阿根廷",
      nation2: "MAR 摩洛哥",
      nationflag1: ".\\country_images\\ARG.png",
      nationflag2: ".\\country_images\\MAR.png",
      buttonSelected: 0,
      items: [],
      situation:[],
    };

  },
  methods: {
    handleButtonSelected(index) {
      this.buttonSelected = index;
    },
    async fetchMatchList() {
      try {
        const response = await axios.get('./json/ARG-MAR.json');
        this.items = response.data;
      } catch (error) {
        console.error('Error fetching match list:', error.message);
        this.items = []; // 在发生错误时初始化 items 为空数组
      }
    },
    async fetchSituation() {
      try {
        const response = await axios.get('./json/ARG-MAR-situation.json');
        this.situation = response.data;
      } catch (error) {
        console.error('Error fetching match list:', error.message);
        this.situation = []; // 在发生错误时初始化 items 为空数组
      }
    },
  },
  mounted() {
    this.fetchMatchList();
    this.fetchSituation();
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
  /* background-image: url('@/assets/background/sea.jpg'); */
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
}

.choose {
  justify-content: center;
  display: flex;
  align-items: center;
  flex-direction: column;
  width: 100%;
  height: 100%;
}

.team-players {
  width: 50%;
  /* 调整为45%以留出间距 */
  border: 1px solid #ddd;
  padding: 10px;
  background-color: #f9f9f969;
}

.team-players .man-position-title,
.team-players .man-position {
  width: 100%;
  height: 40px;
  line-height: 40px;
}

.team-title {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 15px;
}

.team-name {
  font-weight: bold;
}

.team-description {
  text-align: right;
}

.players-list {
  display: flex;
  justify-content: space-between;
  margin-top: 40px;
  overflow-y: auto;
  /* 支持上下滚动 */
  width: 50%;

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