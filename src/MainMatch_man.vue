<template>
  <div class="body">
    <div class="page-container">
      <div class="match-info-center">
        <!-- 返回按钮 -->
        <BackButton class="back-button" />

        <!-- 顶部比赛结果展示 -->
        <div class="match-summary">
          <div class="olympic-logo">
            <img src="./assets/logo/olympicsring.png" alt="Olympic Logo" />
          </div>
        </div>

        <!-- 按钮组 -->
        <ButtonGroup class="button-group"/>

        <!-- 多个评分项 -->
        <!-- 假设这是你的容器元素 -->
        <div class="rating-items-container">
          <DetailRatingItem v-for="index in 3" :key="index" class="rating-item" />
        </div>


        <!-- 中部比分统计 -->
        <div class="score-statistics">
          <div class="team-result">
            <img :src="matches[0].teams[0].flag" alt="ARG" class="team-flag" />
            <h3 class="cname">{{ matches[0].teams[0].name }}</h3>
            <h2 class="score">{{ matches[0].teams[0].score }} - {{ matches[0].teams[1].score }}</h2>
            <h3 class="cname">{{ matches[0].teams[1].name }}</h3>
            <img :src="matches[0].teams[1].flag" alt="MAR" class="team-flag" />
          </div>
          <div class="half-time-score">
            <h4>半场比分: {{ halfTimeScore }}</h4>
          </div>
        </div>

        <ChangeButton class="change-button" />
        <!-- 比赛详情 -->
        <div class="match-details"></div>
      </div>

      <!-- 下部参赛名单表格 -->
      <div class="players-list">
        <div class="team-players">
          <h3>ARG 阿根廷出场球员</h3>
          <ManPositionTitle class="man-position-title" field1Content="NO" field2Content="姓名" field3Content="位置" />
          <ManPosition class="man-position"
            v-for="(player, index) in argPlayers"
            :key="index"
            :field1Content="player.no"
            :field2Content="player.name"
            :field3Content="player.position"
          />
        </div>

        <div class="team-players">
          <h3>MAR 摩洛哥出场球员</h3>
          <ManPositionTitle class="man-position-title" field1Content="NO" field2Content="姓名" field3Content="位置" />
          <ManPosition class="man-position"
            v-for="(player, index) in marPlayers"
            :key="index"
            :field1Content="player.no"
            :field2Content="player.name"
            :field3Content="player.position"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ButtonGroup from './components/ButtonGroup.vue';
import DetailRatingItem from './components/DetailRatingItem.vue';
import ChangeButton from './components/ChangeButton.vue';
import ManPosition from './components/ManPosition.vue';
import ManPositionTitle from './components/ManPositionTitle.vue';
import BackButton from './components/BackButton.vue';

export default {
  name: 'MatchPage',
  components: {
    ButtonGroup,
    DetailRatingItem,
    ChangeButton,
    ManPosition,
    ManPositionTitle,
    BackButton,
  },
  data() {
    return {
      matches: [
        {
          info: 'B组, 比赛 3',
          time: '7月24日 21:00',
          status: '已结束',
          teams: [
            { name: '阿根廷', flag: './country_images/ARG.png', score: 1 },
            { name: '摩洛哥', flag: './country_images/MAR.png', score: 2 },
          ],
        },
      ],
      argPlayers: [
        { no: 1, name: 'RULLI Geronimo', position: '守门员' },
        { no: 2, name: 'di CESARE Marco', position: '后卫' },
        { no: 3, name: 'SOLER Julio', position: '后卫' },
        { no: 4, name: 'MARCOS Acuña', position: '中场' },
        { no: 5, name: 'DE PAUL Rodrigo', position: '中场' },
      ],
      marPlayers: [
        { no: 1, name: 'EL KAJOUI Munir', position: '守门员' },
        { no: 2, name: 'HAKIMI Achraf (C)', position: '后卫' },
        { no: 3, name: 'BOUKAMIR Mehdi', position: '后卫' },
        { no: 4, name: 'AMALLAH Azzedine', position: '中场' },
        { no: 5, name: 'ZIYECH Hakim', position: '前锋' },
      ],
      halfTimeScore: '1 - 1', // 示例半场比分
    };
  },
};
</script>

<style scoped>
.body {
  /*background-image: url('./assets/background/foot.jpeg');*/
  background-size: cover;
  height: 200vh;
  width: 100vw;
  margin: 0;
}

.page-container {
  padding: 20px;
}

.back-button {
  position: absolute;
  top: 20px;
  left: 20px;
  z-index: 10;
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

.cname{
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
  padding: 10px;
  text-align: center;
  margin-bottom: 20px;
  margin-top: 50px;
}

.match-info-center {
  background-color: #f0f0f082; /* 添加灰色背景 */
  padding: 10px;
}

.rating-items-container {
  display: flex;
  flex-direction: row;
  margin-top: 40px;
  margin-left: 100px;
  margin-right: 100px;
}


.rating-item {
  margin-right: 20px; /* 根据需要调整间距 */
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
</style>
