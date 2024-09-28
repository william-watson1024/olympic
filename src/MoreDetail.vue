<template>
  <!-- Class名导致样式错误  TODO 已解决-->

  <div class="medalListcontainer">
    <div id="medalListTop">
      <img
        src="@/assets/logo/detaillogo.jpg"
        alt="Olympic Logo"
        class="olympic-logo"
        style="width: 100px; height: 100px"
      />

      <div class="top" style="display: flex; justify-content: center">
        <div
          class="topContainer"
          style="
            border-radius: 10px;
            background-color: rgba(255, 255, 255, 0.05);
            display: flex;
            justify-content: center;
            width: 600px;
          "
        >
          <div class="header">
            <div class="title" style="color: white; justify-content: center">
              <h1>MoreDetail For Paris Olympics</h1>
              <h2>巴黎奥运会更多精彩瞬间</h2>
            </div>
          </div>
        </div>
      </div>
      <div
        style="
          display: flex;
          justify-content: flex-start;
          align-items: center;
          margin: 10px;
        "
      >
        <router-link to="/" style="display: inline-flex; align-items: center">
          <img
            src="@/assets/logo/back.png"
            alt="Back"
            style="width: 24px; height: auto; margin-right: 8px"
          />
        </router-link>
      </div>
    </div>

    <div class="container_second">
      <div class="image-container">
        <img src="@/assets/more/1/1.jpeg" alt="描述图片" />
      </div>
      <div class="text-container">
        <h1>2024年巴黎奥运会中国体育代表团成立大会的盛况</h1>
        <p>
          7月13日，在北京举行的这一大会标志着中国体育代表团正式成军，准备出征即将在法国巴黎举行的奥运会。
          照片中，我们可以看到中国体育代表团的成员们聚集一堂，他们的脸上写满了期待和决心。他们在国旗下庄严宣誓，将全力以赴，为国家争光。代表团成员包括了教练员、运动员以及后勤保障团队等，他们将共同协作，在奥运会上展现出中国体育的力量。
          在大会现场，中国国旗高高挂起，象征着国家的荣誉和体育精神。代表团的成立也意味着紧张而有序的备战工作进入了最后阶段，运动员们将开始他们最后的冲刺训练，以确保在奥运会上能够发挥出最佳状态。
          这次成立大会不仅是对运动员们的鼓舞和激励，也是向全国人民展示中国体育代表团的决心和信心。中国体育代表团将在巴黎奥运会上参与多个项目的比赛，力争取得优异成绩，展现中国运动员的风采。
          这张照片记录下了中国体育历史上的重要时刻，也预示着中国代表团在巴黎奥运会上的美好前景。随着代表团的成立，中国运动员们将踏上新的征程，为国家荣誉而战。
        </p>
      </div>
    </div>
    <div class="container_second">
      <div class="text-container">
        <h1>巴黎奥运会乒乓球男子单打的颁奖仪式</h1>
        <p>
          中国选手樊振东荣获冠军，站在中间。在比赛过程中，樊振东以4比1的比分战胜了瑞典选手莫雷高德，后者在决赛中获得亚军，站在左边。法国选手菲利克斯·勒布伦在铜牌战中以4比0战胜巴西选手雨果·卡尔德拉诺，获得季军。
          樊振东的夺冠之路并非一帆风顺，他在半决赛中以4比0战胜法国选手菲利克斯·勒布伦，而莫雷高德则在另一场半决赛中获胜。最终的决赛中，樊振东以出色的表现赢得了金牌，这是他职业生涯中的重要里程碑。
          瑞典选手莫雷高德虽然在决赛中失利，但之前的比赛中他曾以4比2战胜中国选手王楚钦，显示了强大的实力。法国选手菲利克斯·勒布伦在晋级半决赛的过程中以4比3战胜中国台北选手林昀儒，表现同样令人印象深刻。
        </p>
      </div>
      <div class="image-container">
        <img src="@/assets/more/2/2.jpeg" alt="描述图片" />
      </div>
    </div>
    <div class="container_second">
      <div class="image-container">
        <img src="@/assets/more/3/3.jpeg" alt="描述图片" />
      </div>
      <div class="text-container">
        <h1>
          中国射击运动员刘宇坤在巴黎奥运会男子50米步枪三姿决赛后的颁奖仪式上
        </h1>
        <p>
          8月1日，刘宇坤以463.6环的成绩勇夺冠军，为中国队再添一枚宝贵的金牌。他的表现不仅展现了他个人的卓越才能，也彰显了中国射击队在该项目上的强大实力和深厚底蕴。
          刘宇坤在资格赛中就展现出了稳定的竞技状态，以第一名的成绩晋级决赛。在决赛中，他以出色的发挥，特别是在跪姿和卧姿项目中的精准射击，为自己赢得了领先优势。在最后的立姿比赛中，他成功超越了此前领先的挪威选手海格，最终以1.8环的优势锁定胜局。
          在颁奖仪式上，刘宇坤身披五星红旗，站在最高领奖台上，他的脸上洋溢着胜利的喜悦。他手中的金牌在阳光下闪闪发光，这是对他辛勤训练和卓越表现的最好奖赏。在刘宇坤的两侧，分别是获得银牌的乌克兰选手库里什和获得铜牌的印度选手库萨莱。这一刻，不仅是刘宇坤个人的荣耀，也是整个中国体育代表团的骄傲。
        </p>
      </div>
    </div>
    <div class="container_second">
      <div class="text-container">
        <h1>
          中国女子拳击运动员李倩在2024年巴黎奥运会女子拳击75公斤级决赛中获胜后的庆祝场景
        </h1>
        <p>
          8月11日，李倩以4比1的比分战胜了巴拿马选手雅蒂娜·美比奇·拜隆，夺得了金牌。
          这一刻，她实现了个人职业生涯的大满贯，也为中国体育代表团在本届奥运会上摘得了第39枚金牌。
          李倩的夺冠之路充满艰辛，她曾在2016年里约奥运会和2020年东京奥运会上分别获得铜牌和银牌。
          这次在巴黎奥运会上，她终于实现了自己长久以来的梦想，登上了奥运会的最高领奖台。照片中，李倩高举双臂，脸上洋溢着胜利的喜悦和释然的笑容，她的这份坚持和努力，让她在34岁这个对许多运动员来说可能已经退役的年龄，依然能够站在奥运会的决赛场上并最终夺冠。
          这张照片记录了中国女子拳击的辉煌时刻，也展现了李倩不屈不挠、勇攀高峰的体育精神。她的成功，无疑将激励更多年轻运动员为梦想而努力奋斗。
        </p>
      </div>
      <div class="image-container">
        <img src="@/assets/more/4/4.jpeg" alt="描述图片" />
      </div>
    </div>
    <div class="container_second">
      <div class="image-container">
        <img src="@/assets/more/5/5.jpeg" alt="描述图片" />
      </div>
      <div class="text-container">
        <h1>
          中国田径运动员杨家玉在巴黎奥运会女子20公里竞走决赛中冲线后庆祝胜利的瞬间
        </h1>
        <p>
          8月1日，杨家玉以1小时29分34秒的成绩夺得冠军，为中国队再添一枚宝贵的金牌。她在比赛中展现了卓越的竞技状态和坚忍不拔的精神，最终以领先第二名西班牙选手佩雷斯36秒的优势率先冲过终点线。
          照片中，杨家玉身披五星红旗，激动地向观众致意。她的脸上洋溢着胜利的喜悦，手臂高举，向世界展示着中国田径的力量和风采。在她的身后，我们可以看到其他完成比赛的选手们，她们同样展现出了顽强的竞技精神和对运动的热爱。
          这一刻，不仅是杨家玉个人的荣耀，也是整个中国田径队的骄傲。她的夺冠不仅实现了个人职业生涯的大满贯，也为中国田径在国际舞台上赢得了更多的尊重和认可。新华社记者李颖和许畅在现场记录下了这一激动人心的时刻，让远在千里之外的中国观众也能感受到这份喜悦和荣耀。
        </p>
      </div>
    </div>
    <div class="container_second">
      <div class="text-container">
        <h1>中国艺术体操队的姑娘们在巴黎奥运会上夺冠的辉煌瞬间</h1>
        <p>
          7月27日，由丁欣怡、郭崎琪、郝婷、黄张嘉洋和王澜静组成的中国队在艺术体操集体全能决赛中以69.800分的成绩赢得了冠军，实现了中国艺术体操队在奥运会上的首次金牌突破。这一历史性的胜利不仅标志着中国艺术体操队的崛起，也展现了中国运动员在这一领域的卓越才能和辛勤努力。
          照片中，中国队的姑娘们面带灿烂的笑容，手中高举着象征荣誉的花束，她们的眼中闪烁着激动的泪光。背景中，我们可以看到巴黎奥运会的艺术体操赛场，装饰着奥运五环和“PARIS
          2024”的字样，彰显了这一成就的国际性和重要性。
          这次夺冠是中国艺术体操队多年努力的结果，她们在赛场上展现了精湛的技艺和无与伦比的艺术表现力。她们的表演《共生共舞》和《凤鸣凌霄》不仅征服了评委，也赢得了全世界观众的心。这一刻，她们不仅是中国的骄傲，也是亚洲乃至全世界艺术体操运动的杰出代表。
        </p>
      </div>
      <div class="image-container">
        <img src="@/assets/more/6/6.jpeg" alt="描述图片" />
      </div>
    </div>
    <div class="container_second">
      <div class="image-container">
        <img src="@/assets/more/7/7.jpeg" alt="描述图片" />
      </div>
      <div class="text-container">
        <h1>
          中国队女子4x100米自由泳接力队的四位杰出选手杨浚瑄、程玉洁、张雨霏、吴卿风在2024年巴黎奥运会的颁奖仪式上欢庆的瞬间
        </h1>
        <p>
          她们的脸上洋溢着自豪和喜悦，因为她们在这项竞争激烈的赛事中以3分30秒30的成绩获得了季军，并且打破了亚洲纪录。
          图片中，背景是2024年巴黎奥运会的标志性字样“PARIS
          2024”，这不仅彰显了这一历史性时刻的地点，也体现了她们在国际舞台上取得的卓越成就。新华社的字样“XPORA
          NEWS”表明这张照片是由新华社的记者拍摄，记录下了这一激动人心的时刻。
          四位选手从左至右依次是杨浚瑄、程玉洁、张雨霏、吴卿风，她们的手臂相互搭在队友的肩上，展现出团队的凝聚力和默契。她们的奖牌在阳光下闪闪发光，这是对她们辛勤训练和团队合作精神的最好证明。
          这张照片不仅记录了中国队在巴黎奥运会上的辉煌成就，也展现了中国运动员的风采和体育精神。她们的这一成绩不仅是个人的荣耀，也是整个国家的骄傲。
        </p>
      </div>
    </div>
    <div class="container_second">
      <div class="text-container">
        <h1>中国体操运动员刘洋在巴黎奥运会上夺冠的瞬间</h1>
        <p>
          2024年8月4日，刘洋在男子吊环决赛中以15.300分的成绩成功卫冕，为中国体操队夺得了本届奥运会的首枚金牌，这也是中国代表团的第18金。
          照片中，刘洋站在领奖台上，高举双臂，脸上洋溢着胜利的喜悦。他身穿印有五星红旗的比赛服，彰显着中国运动员的骄傲。背景中的观众席上，人们热情地欢呼着，庆祝这一激动人心的时刻。新华社的字样“XINJIRIA
          NEWS”表明这张照片是由新华社记者在比赛现场拍摄的，记录下了中国体操的辉煌瞬间。
          刘洋的这次夺冠不仅是他个人的荣耀，也是中国体操队实力的体现。他以流畅的动作、稳定的发挥和完美的落地赢得了裁判和观众的一致认可。这一刻，刘洋不仅捍卫了自己“吊环王”的称号，也为国家赢得了荣誉。
          这张照片是刘洋运动生涯中的一个高光时刻，也是中国体操在国际舞台上的又一次辉煌展现。刘洋的卫冕成功，再次证明了他在吊环项目上的统治力，同时也激励着更多的中国年轻运动员在国际赛场上勇攀高峰。
        </p>
      </div>
      <div class="image-container">
        <img src="@/assets/more/8/8.jpeg" alt="描述图片" />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MoreDetail",
};
</script>

<style scoped>
.medalListcontainer {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  font-size: 14px;
  text-align: center;
  color: #2c3e50;
  background-image: url("@/assets/background/moredetail.jpg");
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
}

.container_second {
  display: flex;
  flex-direction: row;
  align-items: center;
  padding: 50px;
}

.image-container {
  width: 80%;
  /* 缩小图片容器的宽度 */
  padding: 10px;
  width: 600px;
}

.image-container img {
  border-radius: 6px;
  max-width: 80%;
  border-radius: 8px;
  width: 600px;
}

.text-container {
  background-color: rgba(255, 255, 255, 0.7);
  border-radius: 6px;
  width: 600px;
  /* 缩小文字容器的宽度 */
  padding: 10px;
}

.text-container h1 {
  font-size: 20px;
  /* 缩小标题字体大小 */
  margin-bottom: 10px;
}

.text-container p {
  font-size: 13px;
  /* 缩小段落字体大小 */
  line-height: 1.5;
  color: rgb(7, 35, 59);
}

body {
  transform: scale(1.25);
  /* 125% 缩放 */
  transform-origin: 0 0;
  /* 缩放从左上角开始 */
}
</style>
