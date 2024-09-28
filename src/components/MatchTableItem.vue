<template>
    <div class="container" @click="goToMatch">

        <div class="match-container">
            <!-- 第一行：比赛时间和比赛项目 -->
            <div class="match-header">
                <div class="time-container">
                    <div class="time">{{ this.time }}</div>
                </div>
                <div class="event-container">
                    <div class="event">
                        <div class="event-name">
                            {{ this.edisciplineName }}
                            <div class="right-align">
                                <img src="@/assets/logo/collect.png" alt="collect.png" class="icon" />
                                <img src="@/assets/logo/more.png" alt="more.png" class="icon" />
                            </div>
                        </div>
                        <div class="event-details">{{ this.event }}</div>
                    </div>
                </div>
            </div>


            <div class="match-header" v-if="this.team1.flag !== '' && this.team2.flag !== ''">
                <div class="blank-container">
                </div>
                <!-- 第二行：对战双方国家和得分 -->
                <div class="match-body" >
                    <div class="teamcontainer" >
                        <div class="team">
                            <img :src="this.team1.flag" alt="Team 1 Flag" class="flag" />
                            <span :class="{'team-name': true, 'bold': this.team1.winnerLoserTie === 'W'}">{{ this.team1.name }}</span>
                            <span class="team-winnerLoserTie">{{ this.team1.winnerLoserTie }}</span>
                        </div>
                        <div class="score">{{ this.team1.score }}</div>
                    </div>
                    <div class="teamcontainer" v-if="this.team1.flag && this.team2.flag">
                        <div class="team">
                            <img :src="this.team2.flag" alt="Team 2 Flag" class="flag" />
                            <span :class="{'team-name': true, 'bold': this.team2.winnerLoserTie === 'W'}">{{ this.team2.name }}</span>
                            <span class="team-winnerLoserTie">{{ this.team2.winnerLoserTie }}</span>
                        </div>
                        <div class="score">{{ this.team2.score }}</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        time: {
            type: String,
            default: "21:00"
        },
        event: {
            type: String,
            default: "男子C组 (#5)"
        },
        edisciplineName: {
            type: String,
            default: "足球"
        },
        team1: {
            name: "乌兹别克斯坦",
            flag: "./country_images/FRA.png",
            score: 1,
            winnerLoserTie : 0,
        },
        team2: {
            name: "西班牙",
            flag: "./country_images/FRA.png",
            score: 2,
            winnerLoserTie : 1,
        }
    },
     methods: {
    goToMatch() {
      // Emit event with match details
      this.$emit('match-selected', {
        time: this.time,
        event: this.event,
        edisciplineName: this.edisciplineName,
        team1: this.team1,
        team2: this.team2,
      });
    },
  },
};
</script>

<style scoped>
.container {
    display: flex;
    justify-content: center;
    margin-bottom: 20px;
    /* 水平居中 */
}

.icon {
    width: 20px;
    /* 根据需要调整图标大小 */
    height: 20px;
    /* 根据需要调整图标大小 */
    margin-left: 5px;
}

.match-container {
    display: flex;
    flex-direction: column;
    border: 1px solid #ccc;
    border-radius: 5px;
    font-size: 10px;
    width: 600px;
    background: #ffffff;
    opacity: 0.95;
}

.teamcontainer {
    display: flex;
    justify-content: space-between;
    align-items: center;

}

.time-container {
    flex-grow: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    border-right: 1px solid #ccc;
}

.blank-container {
    flex-grow: 1;
    display: flex;
    align-items: center;
    justify-content: center;
}

.event-container {
    flex-grow: 15;
    display: flex;
    align-items: center;
    justify-content: flex-start;
    padding: 0 10px;
}

.event-name {
    font-size: 1.5em;
    /* 放大字体 */
    font-weight: bold;
    /* 加粗 */
    display: flex;
    justify-content: space-between;
    /* 使内容两端对齐 */
    align-items: center;
}

.event-details {
    font-weight: normal;
    font-size: 0.875em;
    /* 正常小字 */
}

.match-header {
    display: flex;
    /* 设置靠左居中 */
    justify-content: flex-start;
    height: 50px;
    border-bottom: 1px solid #ccc;
}

.time {
    font-weight: bold;
}

.event {
    width: 100%;
    font-weight: bold;
}



.match-body {
    flex-grow: 7;
    display: grid;
}

.team {
    margin-left: 10px;
    display: flex;
    align-items: center;

}

.flag {
    width: 20px;
    height: auto;
    margin-right: 10px;
}
.bold{
    font-size:13px;
    font-weight: bold;
}
.score {
    font-size: 10px;
    text-align: center;
    margin-right: 20px;
    font-weight: bold;
}
.team-winnerLoserTie{
    font-size: 10px;
    text-align: center;
    margin-left: 10px;
}
</style>