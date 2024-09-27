<template>
  <div class="page-container">
    <!-- 顶部导航栏 -->
    <div class="button-group-container">
      <ButtonGroup />
    </div>

    <!-- 比赛列表 -->
    <div class="match-summary">
      <DetailRatingItem
        v-for="(match, index) in matches"
        :key="index"
        :matchInfo="match.info"
        :teams="match.teams"
        :matchTime="match.time"
        :matchStatus="match.status"
      />
    </div>

    <!-- 比赛详情 -->
    <div class="match-details">
      <div class="team-info">
        <h3>ARG 阿根廷</h3>
      </div>
      <div class="match-info-center">
        <h2>阿根廷 1 - 2 摩洛哥</h2>
        <ChangeButton class="change-button"


         />
      </div>
      <div class="team-info">
        <h3>MAR 摩洛哥</h3>
      </div>
    </div>

    <!-- 球员列表 -->
    <div class="players-list">
      <div class="team-players">
        <h3>ARG 阿根廷出场球员</h3>
        <ManPositionTitle field1Content="NO" field2Content="姓名" field3Content="位置" />
        <ManPosition
          v-for="(player, index) in argPlayers"
          :key="index"
          :field1Content="player.no"
          :field2Content="player.name"
          :field3Content="player.position"
        />
      </div>
      <div class="team-players">
        <h3>MAR 摩洛哥出场球员</h3>
        <ManPositionTitle field1Content="NO" field2Content="姓名" field3Content="位置" />
        <ManPosition
          v-for="(player, index) in marPlayers"
          :key="index"
          :field1Content="player.no"
          :field2Content="player.name"
          :field3Content="player.position"
        />
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

export default {
  name: 'MatchPage',
  components: {
    ButtonGroup,
    DetailRatingItem,
    ChangeButton,
    ManPosition,
    ManPositionTitle,
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
        // 添加更多比赛数据
        {
          info: 'B组, 比赛 4',
          time: '7月25日 19:00',
          status: '未开始',
          teams: [
            { name: '巴西', flag: './country_images/BRA.png', score: 0 },
            { name: '西班牙', flag: './country_images/ESP.png', score: 0 },
          ],
        },
        {
          info: 'B组, 比赛 5',
          time: '7月26日 17:00',
          status: '进行中',
          teams: [
            { name: '法国', flag: './country_images/FRA.png', score: 2 },
            { name: '德国', flag: './country_images/GER.png', score: 2 },
          ],
        },
      ],
      argPlayers: [
        { no: 1, name: 'RULLI Geronimo', position: '守门员' },
        { no: 2, name: 'di CESARE Marco', position: '后卫' },
        { no: 3, name: 'SOLER Julio', position: '后卫' },
        // 其他球员
      ],
      marPlayers: [
        { no: 1, name: 'EL KAJOUI Munir', position: '守门员' },
        { no: 2, name: 'HAKIMI Achraf (C)', position: '后卫' },
        { no: 3, name: 'BOUKAMIR Mehdi', position: '后卫' },
        // 其他球员
      ],
    };
  },
};
</script>

<style scoped>
.page-container {
  padding: 20px;
}

.button-group-container {
  display: flex;
  justify-content: left;
  margin-bottom: 20px;
}

.match-summary {
  display: flex;
  justify-content: space-around;
  margin-bottom: 20px;
}

.match-summary .detail-rating-item {
  width: 30%; /* 调整每个比赛项目的宽度 */
}

.match-details {
  display: flex;
  justify-content: space-between;
  margin-bottom: 20px;
}

.change-button {
  display: flex;
  justify-content: left;
  margin-bottom: 20px;
}

.team-info {
  width: 30%;
  text-align: center;
}

.match-info-center {
  width: 40%;
  text-align: center;
  position: relative;
}

.match-info-center .change-button {
  position: absolute;
  left: 0;
  top: 100%; /* 移动到比分下方 */
}

.players-list {
  display: flex;
  justify-content: space-between;
}

.team-players {
  width: 45%;
  border: 1px solid #ddd;
  padding: 10px;
  background-color: #f9f9f9;
}

.team-players .man-position-title, .team-players .man-position {
  width: 100%;
  height: 40px; /* 增加高度 */
  line-height: 40px; /* 垂直居中 */
}
</style>
