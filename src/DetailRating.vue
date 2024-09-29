<template>
  <div class="backgrouond">
    <div class="bread">
      <el-breadcrumb separator="/">
        <el-breadcrumb-item :to="{ path: '/' }">HomePage</el-breadcrumb-item>
        <el-breadcrumb-item
          ><a href="/matchList">MatchTable</a></el-breadcrumb-item
        >
        <el-breadcrumb-item
          ><a href="/mainMatch">Match</a></el-breadcrumb-item
        >
        <el-breadcrumb-item>MatchDetail</el-breadcrumb-item>
      </el-breadcrumb>
    </div>
    <BackButton @click="goBack" class="back-button" />
    <router-link to="/MainMatch" class="back-button">
      <img src="@/assets/logo/back.png" alt="Back" class="back-icon" />
    </router-link>

    <!-- 顶部比赛结果展示 -->
    <div class="match-summary">
      <div class="olympic-logo">
        <img src="./assets/logo/olympicsring.png" alt="Olympic Logo" />
      </div>
    </div>
    <!-- 中部比分统计 -->
    <div class="score-statistics">
      <div class="team-result">
        <img src="@/assets/background/ARG.png" alt="ARG" class="team-flag" />
        <h3 class="cname">{{ "阿根廷" }}</h3>
        <h2 class="score">{{ "1" }} - {{ "2" }}</h2>
        <h3 class="cname">{{ "摩洛哥" }}</h3>
        <img src="@/assets/background/MAR.png" alt="MAR" class="team-flag" />
      </div>
      <div class="half-time-score">
        <h4>半场比分: {{ "1-1" }}</h4>
      </div>
    </div>
    <change-button-vue
      @button-selected="handleButtonSelected"
    ></change-button-vue>
    <div class="choose" v-show="buttonSelected === 0">
      <div class="players-list">
        <div class="team-players">
          <div class="team-title">
            <div style="flex-direction: row; display: flex">
              <img
                :src="nationflag1"
                alt="国旗"
                style="height: 20px; width: 30px; margin-right: 15px"
              />
              <div class="team-name">{{ nation1 }}</div>
            </div>
            <div class="team-description">出场球员</div>
          </div>
          <ManPositionTitle
            class="man-position-title"
            field1Content="NO"
            field2Content="姓名"
            field3Content="位置"
          />
          <ManPosition
            class="man-position"
            v-for="(player, index) in items['ARG-MAR'][0].item0"
            :key="index"
            :field1Content="player.bib"
            :field2Content="player.name"
            :field3Content="player.position"
          />
        </div>

        <div class="team-players">
          <div class="team-title">
            <div style="flex-direction: row; display: flex">
              <img
                :src="nationflag2"
                alt="国旗"
                style="height: 20px; width: 30px; margin-right: 15px"
              />
              <div class="team-name">{{ nation2 }}</div>
            </div>
            <div class="team-description">出场球员</div>
          </div>
          <ManPositionTitle
            class="man-position-title"
            field1Content="NO"
            field2Content="姓名"
            field3Content="位置"
          />
          <ManPosition
            class="man-position"
            v-for="(player, index) in items['ARG-MAR'][1].item1"
            :key="index"
            :field1Content="player.bib"
            :field2Content="player.name"
            :field3Content="player.position"
          />
        </div>
      </div>
    </div>
    <div class="choose" v-show="buttonSelected === 1">
      <SituationItem class="situation"> </SituationItem>
      <SituationItem
        v-for="(item, index) in situation['events']"
        :key="index"
        :field1Content="item.time"
        :field2Content="item.event"
      />
    </div>
    <div
      class="choose"
      v-show="buttonSelected === 2"
      style="font-size: 100px; font-weight: bold"
    >
      <p>还没有做哦宝宝</p>
    </div>
    <div
      class="choose"
      v-show="buttonSelected === 3"
      style="font-size: 100px; font-weight: bold"
    >
      <p>还没有做哦宝宝</p>
    </div>
  </div>
</template>

<script>
// import DetailRatingItem from './components/DetailRatingItem.vue';
// import ButtonGroup from './components/ButtonGroup.vue';
import ChangeButtonVue from "./components/ChangeButton.vue";
import ManPosition from "./components/ManPosition.vue";
import ManPositionTitle from "./components/ManPositionTitle.vue";
// import CombinedMatch from './components/CombinedMatch.vue';
import SituationItem from "./components/SituationItem.vue";
import BackButton from "./components/BackButton.vue";
import axios from "axios";

export default {
  components: {
    // DetailRatingItem,
    // ButtonGroup,
    ChangeButtonVue,
    BackButton,
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
      situation: [],
    };
  },
  methods: {
    goBack() {
      this.$router.push({ name: "MaimMatch_mant" }); // Replace 'MatchList' with the actual route name if different
    },
    handleButtonSelected(index) {
      this.buttonSelected = index;
    },
    async fetchMatchList() {
      try {
        const response = await axios.get("./json/ARG-MAR.json");
        this.items = response.data;
      } catch (error) {
        console.error("Error fetching match list:", error.message);
        this.items = []; // 在发生错误时初始化 items 为空数组
      }
    },
    async fetchSituation() {
      try {
        const response = await axios.get("./json/ARG-MAR-situation.json");
        this.situation = response.data;
      } catch (error) {
        console.error("Error fetching match list:", error.message);
        this.situation = []; // 在发生错误时初始化 items 为空数组
      }
    },
  },
  mounted() {
    this.fetchMatchList();
    this.fetchSituation();
  },
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  font-size: 14px;
  text-align: center;
  color: #2c3e50;
}

.backgrouond {
  background-image: url("@/assets/background/flyFootball2.jpg");
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

.score-statistics {
  background-color: rgba(255, 255, 255, 0.5); /* 半透明背景 */
  border-radius: 10px;
  width: 52%;
  text-align: center;
  padding: 50px;
  margin-top: 50px;
  margin: 0 auto;
}

.situation {
  background-color: rgba(255, 255, 255, 0.5);
}

.team-result {
  display: flex;
  align-items: center;
  justify-content: center;
}

.team-flag {
  width: 150px; /* 设置国旗宽度 */
  height: auto;
  margin: 0 10px;
}

.cname {
  font-size: 2rem; /* 设置国家名称字体大小 */
}

.score {
  font-size: 2rem; /* 设置比分字体大小 */
  margin: 0 20px;
}

.match-summary {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 20px;
}

.olympic-logo img {
  margin-top: 20px;
  width: 300px; /* 设置奥运会标志宽度 */
}

.half-time-score {
  font-size: 1.5rem; /* 设置半场比分字体大小 */
}

.back-button {
  position: absolute;
  top: 60px;
  left: 20px;
  z-index: 10;
}

.back-icon {
  width: 24px;
  height: auto;
  margin-right: 8px;
}

/* 自定义面包屑导航的分隔符样式 */
.el-breadcrumb__separator {
  font-size: 16px;
  color: #999;
}

/* 自定义面包屑导航项的样式 */
.el-breadcrumb__item {
  font-size: 20px;
  color: #333;
}

/* 自定义面包屑导航项的链接样式 */
.el-breadcrumb__item a {
  color: #333;
  text-decoration: none;
}

/* 自定义面包屑导航项的链接悬停样式 */
.el-breadcrumb__item a:hover {
  color: #007bff;
}

/* 自定义面包屑导航项的激活样式 */
.el-breadcrumb__item.is-active {
  font-weight: bold;
}

/* 将面包屑导航定位在页面左上角 */
.el-breadcrumb {
  position: absolute;
  top: 20px;
  left: 20px;
}
</style>
