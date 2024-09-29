<template>
  <div class="body">
    <div class="page-container">
      <div class="match-info-center">
        <!-- <pre>{{ selectedGroup }}</pre>
        <pre>{{ lwz }}
        </pre> -->
        <div class="bread">
          <el-breadcrumb separator="/">
            <el-breadcrumb-item :to="{ path: '/' }"
              >HomePage</el-breadcrumb-item
            >
            <el-breadcrumb-item
              ><a href="/matchList">MatchTable</a></el-breadcrumb-item
            >
            <el-breadcrumb-item>Match</el-breadcrumb-item>
          </el-breadcrumb>
        </div>

        <!-- 返回按钮 -->
        <BackButton @click="goBack" class="back-button" />
        <router-link to="/matchList" class="back-button">
          <img src="@/assets/logo/back.png" alt="Back" class="back-icon" />
        </router-link>

        <!-- 顶部比赛结果展示 -->
        <div class="match-summary">
          <div class="olympic-logo">
            <img src="./assets/logo/olympicsring.png" alt="Olympic Logo" />
          </div>
        </div>
        <div class="top-group">
          <!-- 按钮组 -->
          <ButtonGroup
            @button-selected="handleSelectedGroup"
            class="button-group"
          />

          <!-- 多个评分项 -->
          <!-- 假设这是你的容器元素 -->
          <div class="gridLayout" v-if="selectedGroup !== null">
            <div class="rating-items-container">
              <DetailRatingItem
                v-for="(match, index) in lwz"
                :key="index"
                :matchInfo="match.info"
                :teams="match.teams"
                :matchTime="match.time"
                :matchStatus="match.status"
                @mat-selected="navigateToMatch"
              />
            </div>
          </div>
        </div>
        <!-- 中部比分统计 -->
        <div class="score-statistics">
          <div class="team-result">
            <img
              src="@/assets/background/ARG.png"
              alt="ARG"
              class="team-flag"
            />
            <h3 class="cname">{{ "阿根廷" }}</h3>
            <h2 class="score">{{ "1" }} - {{ "2" }}</h2>
            <h3 class="cname">{{ "摩洛哥" }}</h3>
            <img
              src="@/assets/background/MAR.png"
              alt="MAR"
              class="team-flag"
            />
          </div>
          <div class="half-time-score">
            <h4>半场比分: {{ "1-1" }}</h4>
          </div>
        </div>

        <ChangeButton class="change-button" />
        <!-- 比赛详情 -->
        <div class="match-details"></div>
      </div>

      <div class="match-schedule">
        <div class="header-text">足球比赛对阵表</div>

        <div class="match-layout">
          <div class="column-qur left">
            <div class="final-label">1/4决赛</div>
            <CombinedMatch
              class="quarter-match"
              v-for="(match, index) in quarterFinals"
              :key="'quarter-' + index"
              :Match="edCountry === match.upperCountryName"
              :upperFlagSrc="match.upperFlagSrc"
              :upperCountryName="match.upperCountryName"
              :upperScore="match.upperScore"
              :lowerFlagSrc="match.lowerFlagSrc"
              :lowerCountryName="match.lowerCountryName"
              :lowerScore="match.lowerScore"
              :penaltyScore="match.penalty ? match.penaltyScore : ''"
              @mouseover="handleMouseOver"
              @mouseleave="handsleMouseLeave"
            />
          </div>
          <div class="column-semi center">
            <div class="final-label">半决赛</div>
            <CombinedMatch
              class="semi-match"
              v-for="(match, index) in semiFinals"
              :key="'semi-' + index"
              :Match="edCountry === match.upperCountryName"
              :upperFlagSrc="match.upperFlagSrc"
              :upperCountryName="match.upperCountryName"
              :upperScore="match.upperScore"
              :lowerFlagSrc="match.lowerFlagSrc"
              :lowerCountryName="match.lowerCountryName"
              :lowerScore="match.lowerScore"
              defaultColor="azure"
              @mouseover="handleMouseOver"
              @mouseleave="handleMouseLeave"
            />
          </div>
          <div class="column right">
            <div class="final-container">
              <div class="final-label">决赛</div>
              <CombinedMatch
                :Match="edCountry === '法国'"
                upperFlagSrc="././/public/country_images/FRA.png"
                upperCountryName="法国"
                :upperScore="3"
                lowerFlagSrc="././/public/country_images/ESP.png"
                lowerCountryName="西班牙"
                :lowerScore="5"
                defaultColor="#fbfd8f"
                @mouseover="handleMouseOver"
                @mouseleave="handleMouseLeave"
              />
            </div>
            <div class="bronze-medal">
              <div class="bronze-label">铜牌赛</div>
              <CombinedMatch
                :Match="edCountry === '埃及'"
                upperFlagSrc="././/public/country_images/EGY.png"
                upperCountryName="埃及"
                :upperScore="0"
                lowerFlagSrc="././/public/country_images/MAR.png"
                lowerCountryName="摩洛哥"
                :lowerScore="6"
                defaultColor="gold"
                @mouseover="handleMouseOver"
                @mouseleave="handleMouseLeave"
              />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ButtonGroup from "./components/ButtonGroup.vue";
import DetailRatingItem from "./components/DetailRatingItem.vue";
//import ChangeButton from './components/ChangeButton.vue';
//import ManPosition from './components/ManPosition.vue';
//import ManPositionTitle from './components/ManPositionTitle.vue';
import CombinedMatch from "./components/CombinedMatch.vue";
import BackButton from "./components/BackButton.vue";
import axios from "axios";

export default {
  name: "MatchPage",
  components: {
    ButtonGroup,
    DetailRatingItem,
    CombinedMatch,
    //ChangeButton,
    //ManPosition,
    //ManPositionTitle,
    BackButton,
  },
  data() {
    return {
      selectedGroup: "男子B组",
      lwz: [],

      quarterFinals: [
        {
          upperFlagSrc: "././/public/country_images/FRA.png",
          upperCountryName: "法国",
          upperScore: 1,
          lowerFlagSrc: "././/public/country_images/ARG.png",
          lowerCountryName: "阿根廷",
          lowerScore: 0,
        },
        {
          upperFlagSrc: "././/public/country_images/EGY.png",
          upperCountryName: "埃及",
          upperScore: "1(5)",
          lowerFlagSrc: "././/public/country_images/PAR.png",
          lowerCountryName: "巴拉圭",
          lowerScore: "1(4)",
          penalty: true,
          penaltyScore: "(5):(4)",
        },
        {
          upperFlagSrc: "././/public/country_images/MAR.png",
          upperCountryName: "摩洛哥",
          upperScore: 4,
          lowerFlagSrc: "././/public/country_images/USA.png",
          lowerCountryName: "美国",
          lowerScore: 0,
        },
        {
          upperFlagSrc: "././/public/country_images/JPN.png",
          upperCountryName: "日本",
          upperScore: 0,
          lowerFlagSrc: "././/public/country_images/ESP.png",
          lowerCountryName: "西班牙",
          lowerScore: 3,
        },
      ],
      semiFinals: [
        {
          upperFlagSrc: "././/public/country_images/FRA.png",
          upperCountryName: "法国",
          upperScore: 3,
          lowerFlagSrc: "././/public/country_images/EGY.png",
          lowerCountryName: "埃及",
          lowerScore: 1,
        },
        {
          upperFlagSrc: "././/public/country_images/MAR.png",
          upperCountryName: "摩洛哥",
          upperScore: 1,
          lowerFlagSrc: "././/public/country_images/ESP.png",
          lowerCountryName: "西班牙",
          lowerScore: 2,
        },
      ],

      argPlayers: [
        { no: 1, name: "RULLI Geronimo", position: "守门员" },
        { no: 2, name: "di CESARE Marco", position: "后卫" },
        { no: 3, name: "SOLER Julio", position: "后卫" },
        { no: 4, name: "MARCOS Acuña", position: "中场" },
        { no: 5, name: "DE PAUL Rodrigo", position: "中场" },
      ],
      marPlayers: [
        { no: 1, name: "EL KAJOUI Munir", position: "守门员" },
        { no: 2, name: "HAKIMI Achraf (C)", position: "后卫" },
        { no: 3, name: "BOUKAMIR Mehdi", position: "后卫" },
        { no: 4, name: "AMALLAH Azzedine", position: "中场" },
        { no: 5, name: "ZIYECH Hakim", position: "前锋" },
      ],
      halfTimeScore: "1 - 1", // 示例半场比分
    };
  },
  mounted() {
    this.fetchMatchList();
  },
  methods: {
    async fetchMatchList() {
      try {
        const response = await axios.get(`./json/${this.selectedGroup}.json`);
        this.lwz = response.data;
      } catch (error) {
        console.error("Error fetching match list:", error);
      }
    },
    navigateToMatch(matDetails) {
      // Use Vue Router to navigate to the MainMatch_mant page
      this.$router.push({
        name: "DetailRating", // Ensure this matches your route name
        params: { matDetails },
      });
    },
    handleSelectedGroup(index) {
      this.selectedGroup = index;
    },
    handleMouseOver() {
      this.isHighlighted = true;
    },
    handleMouseLeave() {
      this.isHighlighted = false;
    },
    goBack() {
      this.$router.push({ name: "MatchList" }); // Replace 'MatchList' with the actual route name if different
    },
  },
  watch: {
    selectedGroup() {
      this.fetchMatchList();
    },
  },
};
</script>

<style scoped>
.body {
  /*background-image: url('./assets/background/foot.jpeg');*/
  background-size: cover;
  margin: 0;
}

.page-container {
  background-image: url("@/assets/background/run.jpeg");
  background-size: cover; /* 背景图片覆盖整个容器 */
  background-position: center; /* 背景图片居中 */
  background-attachment: fixed; /* 背景图片固定 */
  min-height: 100vh;
  padding: 20px;
}

.back-button {
  position: absolute;
  padding: auto;
  top: 60px;
  left: 20px;
  z-index: 10;
}

.top-group {
  padding: 50px;
  border-radius: 10px;
}

.button-group {
  margin-top: 40px;
  margin-left: 100px;
}

.match-summary {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 20px;
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

.half-time-score {
  font-size: 1.5rem; /* 设置半场比分字体大小 */
}

.olympic-logo img {
  width: 300px; /* 设置奥运会标志宽度 */
}

.score-statistics {
  background-color: rgba(255, 255, 255, 0.8); /* 半透明背景 */
  border-radius: 10px;
  width: 65%;
  text-align: center;
  padding: 50px;
  margin-top: 50px;
}

.match-info-center {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  flex: center;
  flex-direction: column;
  padding: 10px;
}

.rating-items-container {
  display: grid;
  grid-template-columns: repeat(3, 1fr); /* 每行两个列 */
  gap: 20px; /* 调整间距 */
  margin-top: 40px;
  margin-left: 100px;
  margin-right: 100px;
  justify-content: space-between;
}

.rating-item {
  margin: 10px; /* 根据需要调整间距 */
}

.change-button {
  margin-top: 40px;
}

.players-list {
  display: flex;
  justify-content: space-between;
  margin-top: 40px;
  overflow-y: auto; /* 支持上下滚动 */
  max-height: 400px; /* 设置最大高度 */
}

.team-players {
  width: 50%; /* 调整为45%以留出间距 */
  border: 1px solid #ddd;
  padding: 10px;
  background-color: #f9f9f969;
}

.team-players h3 {
  text-align: center;
}

.team-players .man-position-title,
.team-players .man-position {
  width: 100%;
  height: 40px;
  line-height: 40px;
}

.match-layout {
  display: flex; /* 使用 flexbox 布局 */
  justify-content: center;
  align-items: center;
  height: 800px; /* 固定高度 */
  width: 1200px; /* 固定宽度 */
  margin: 0 auto; /* 水平居中 */
  background-size: cover;
  background-image: url("./assets/background/line.jpeg");
  background-position: center 4px;
  font-family: "Arial", sans-serif;
  color: #333;
}

.quarter-match {
  margin-bottom: 60px;
}

.semi-match {
  margin-top: 60px;
  margin-bottom: 120px;
}

.column-qur {
  margin-top: 40px;
  margin-left: 40px;
  display: flex;
  flex-direction: column;
}

.column-semi {
  display: flex;
  flex-direction: column;
}

.right {
  flex: 1;
  position: relative;
}

.left {
  margin-right: 20px;
}

.center {
  margin: 0 20px;
  justify-content: space-between;
}

.right {
  margin-left: 20px;
  align-items: center;
}

.final-container {
  margin-top: 160px; /* Adjust this to increase space */
  margin-left: auto; /* Center it based on the column */
  margin-right: auto;
}

.final-label,
.bronze-label {
  background-color: white;
  border-radius: 10px 10px 0 0;
  padding: 5px;
  text-align: center;
  font-weight: bold;
  margin-bottom: 5px;
  width: 100px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

.bronze-medal {
  margin-top: 80px; /* Adjust spacing as needed */
}

.column > * {
  margin-bottom: 30px;
}

.navigation-label-qur {
  background-color: rgba(184, 115, 51, 0.8);
  border-radius: 10px;
  padding: 5px;
  text-align: center;
  font-weight: bold;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
  width: 100px; /* 可以根据需要调整 */
  margin: 0 auto;
}

.navigation-label-semi {
  background-color: #c0c0c0;
  border-radius: 10px;
  padding: 5px;
  text-align: center;
  font-weight: bold;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
  width: 100px; /* 可以根据需要调整 */
  margin: 0 auto;
}

.navigation-label-fin {
  background-color: #ffd700;
  border-radius: 10px;
  padding: 5px;
  text-align: center;
  font-weight: bold;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
  width: 100px; /* 可以根据需要调整 */
  margin: 0 auto;
}

.match-layout {
  display: flex;
  justify-content: space-between;
  position: relative; /* 添加此行 */
}

.left,
.center,
.right {
  flex: 1;
  position: relative;
}

.center {
  margin: 0;
}

.header-image {
  display: block;
  margin: 0 auto;
  width: 50%; /* 可根据需要调整 */
}

.header-text {
  text-align: center;
  font-size: 30px;
  margin-top: 10px;
  margin-bottom: 50px;
  font-weight: bold;
}

.navigation-layout {
  display: flex;
  justify-content: space-between;
  position: absolute; /* 改为绝对定位 */
  top: 0; /* 设置在顶部 */
  left: 0; /* 确保靠左 */
  right: 0; /* 确保靠右 */
  margin-bottom: 20px; /* 调整与比赛框的间距 */
  z-index: 1; /* 确保在其他元素上方 */
}

.gridLayout {
  display: grid;
  /* grid-template-columns: repeat(3, 1fr); 每行两个列 */
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
