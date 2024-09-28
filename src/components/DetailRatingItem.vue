<template>
  <div class="match-container">
    <!-- 比赛信息 -->
    <div class="match-info">
      <span>{{ matchInfo + ',' + matchNumber }}</span>
    </div>

    <!-- 两支队伍对比 -->
    <div class="teams">
      <div class="team" v-for="team in teams" :key="team.name">
        <div class="nameflag">
          <img :src="team.flag" :alt="`${team.name}国旗`" class="flag">
          <span>{{ team.name }}</span>
        </div>
        <div>
          <span class="score">{{ team.score }}</span>
        </div>
      </div>
    </div>

    <!-- 比赛时间和状态 -->
    <div class="match-time-status">
      <span>{{ matchTime }}</span>
      <span>{{ matchStatus }}</span>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MatchComponent',
  props: {
    matchInfo: {
      type: String,
      required: true,
      default: 'B组'
    },
    matchNumber: {
      type: String,
      required: true,
      default: '比赛 4'
    },
    teams: {
      type: Array,
      required: true,
      default: () => ([
        { name: '伊拉克', flag: './country_images/FRA.png', score: 2 },
        { name: '乌克兰', flag: './country_images/AIN.png', score: 1 }
      ]),
      validator(value) {
        return value.every(team => 'name' in team && 'flag' in team && 'score' in team);
      }
    },
    matchTime: {
      type: String,
      required: true,
      default: '7月25日 1:00'
    },
    matchStatus: {
      type: String,
      required: true,
      default: '已结束'
    }
  }
}
</script>

<style scoped>
.match-container {
  background-color: white;
  border: 1px solid #ccc;
  width: 1000px;
  height: 140px;
  margin: 0 auto;
  border-radius: 8px;
}

.match-info {
  padding: 5px;
  text-align: left;
  font-weight: bold;
  margin-bottom: 20px;
}

.teams {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  margin-bottom: 5px;
  margin-top: 20px;
  border-bottom: #ccc 1px solid;
  border-top: #ccc 1px solid;
  padding: 5px;
}

.team {
  display: flex;
  justify-content: space-between;
  align-items: center;
  transition: background-color 0.3s, color 0.3s; /* 添加过渡效果 */
}

.match-container:hover {
  background-color: black; /* 背景变黑 */
  color: white; /* 字体变白 */
}

.flag {
  width: 24px;
  height: 16px;
  margin-right: 5px;
}

.score {
  font-weight: bold;
  margin-left: 5px;
}

.match-time-status {
  display: flex;
  justify-content: space-between;
  font-weight: bold;
  padding: 5px;
}

.nameflag {
  display: flex;
  align-items: center;
}
</style>
