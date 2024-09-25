<template>
    <div class="container">
        <div class="match-container">
            <!-- 第一行：比赛时间和比赛项目 -->
            <div class="match-header">
                <div class="time-container">
                    <div class="time">{{ match.time }}</div>
                </div>
                <div class="event-container">
                    <div class="event">
                        <div class="event-name">
                            {{ match.event.split(" - ")[0] }}
                            <div class="right-align">
                                <img src="@/assets/logo/collect.png" alt="collect.png" class="icon" />
                                <img src="@/assets/logo/more.png" alt="more.png" class="icon" />
                            </div>
                        </div>
                        <div class="event-details">{{ match.event.split(" - ")[1] }}</div>
                    </div>
                </div>
            </div>


            <div class="match-header">
                <div class="blank-container">
                </div>
                <!-- 第二行：对战双方国家和得分 -->
                <div class="match-body">

                    <div class="teamcontainer">
                        <div class="team">
                            <img :src="match.team1.flag" alt="Team 1 Flag" class="flag" />
                            <span class="team-name">{{ match.team1.name }}</span>
                        </div>
                        <div class="score">{{ match.team1.score }}</div>
                    </div>
                    <div class="teamcontainer">
                        <div class="team">
                            <img :src="match.team2.flag" alt="Team 2 Flag" class="flag" />
                            <span class="team-name">{{ match.team2.name }}</span>
                        </div>
                        <div class="score">{{ match.team2.score }}</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            match: {
                time: "21:00",
                event: "足球 - 男子C组 (#5)",
                team1: {
                    name: "乌兹别克斯坦",
                    flag: "./country_images/FRA.png",
                    score: 1,
                },
                team2: {
                    name: "西班牙",
                    flag: "./country_images/FRA.png",
                    score: 2,
                },
            },
        };
    },
};
</script>

<style scoped>
.container {
    display: flex;
    justify-content: center;
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

.score {
    font-size: 10px;
    text-align: center;
    margin-right: 20px;
    font-weight: bold;
}
</style>