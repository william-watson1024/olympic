<template>
  <div class="match-container" @click="goToMat">
    <!-- 比赛信息 -->
    <div class="match-info">
      <span>{{ matchInfo}}</span>
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
  name: 'DetailRating',

  props: {
     matDetails: {
    type: Object, // Ensure the type matches the expected input
    required: false,
    },
    matchInfo: {
      type: String,
      required: true,
      default: 'B组, 比赛 4'
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
  },
  methods: {
    goToMat() {
    this.$router.push({
      name: 'DetailRating',
      params: {
        matDetails: {
          matchInfo: this.matchInfo,
          teams: this.teams,
          matchTime: this.matchTime,
          matchStatus: this.matchStatus,
        }
      }
    });
    },
  }
}
</script>

<style scoped>
.match-container {
  background-color: white;
  border: 1px solid #ccc;
  width: 250px;
  height: 140px;
  margin-right: 10px;
  border-radius: 8px;
  background-color: white;
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
  font-size: 20px;
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
