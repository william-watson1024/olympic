<template>
  <div class="background">
    <el-container class="container">
      <!-- 顶部标题 -->
      <el-header class="header-background">
        <h2 style="margin-top: 10px;">2024 巴黎奥运会中国运动员风采</h2>
      </el-header>

      <el-main>
        <!-- 抽屉：运动员详细信息 -->
        <el-drawer
          title="运动员详情"
          :visible.sync="drawerVisible"
          :before-close="handleClose"
        >
          <el-image :src="currentAthlete?.image" fit="cover"></el-image>
          <h3>{{ currentAthlete?.title }}</h3>
          <p>简介：{{ currentAthlete?.brief }}</p>
          <el-divider></el-divider>
          <p>更新时间：{{ currentAthlete?.operate_time }}</p>
        </el-drawer>

        <!-- 固定图片展示 -->
        <el-carousel trigger="click" height="600px">
          <el-carousel-item v-for="(image, index) in images" :key="index">
            <img :src="image.src" style="width: 100%; height: auto" />
          </el-carousel-item>
        </el-carousel>

        <!-- 折叠面板：运动员信息列表 -->
        <el-collapse v-model="activeNames" class="collapsed-container">
          <el-collapse-item
            v-for="(athlete, index) in paginatedAthletes"
            :key="index"
            :name="index.toString()"
            class="collapsed-item"
          >
            <template #title>
              <span style="font-size: 30px; text-align: center">{{
                athlete.title
              }}</span>
              <!-- 仅展示姓名 -->
            </template>

            <el-image
              :src="athlete.image"
              fit="cover"
              class="athlete-image"
            ></el-image>
            <p style="font-size: 30px">项目：{{ athlete.brief }}</p>
            <p style="font-size: 30px">参赛时间：{{ athlete.operate_time }}</p>
            <el-divider></el-divider>
            <el-link :href="athlete.url" target="_blank" style="font-size: 30px"
              >点击查看运动员最新精彩资讯</el-link
            >
          </el-collapse-item>
        </el-collapse>

        <!-- 分页 -->
        <el-pagination 
          background
          layout="prev, pager, next"
          :total="athletes.length"
          :page-size="pageSize"
          @current-change="handlePageChange"
          style="margin-top: 20px; padding: 10px"
        ></el-pagination>
      </el-main>

      <el-footer class="footer-background">
        <p style="margin-top: 10px;">2024 Copyright @2024 All rights reserved</p>
      </el-footer>
    </el-container>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      athletes: [], // 存放运动员信息
      currentPage: 1, // 当前页码
      pageSize: 10, // 每页展示个运动员
      activeNames: [], // 折叠面板的活动项
      drawerVisible: false, // 抽屉的显示状态
      currentAthlete: null, // 当前选择的运动员信息
      images: [
        { src: require("./assets/athletes/run.jpg") },
        { src: require("./assets/athletes/lift.jpeg") },
        { src: require("./assets/athletes/arrow.jpg") },
        { src: require("./assets/athletes/fight.jpg") },
      ],
    };
  },
  computed: {
    // 分页后的运动员数据
    paginatedAthletes() {
      const start = (this.currentPage - 1) * this.pageSize;
      return this.athletes.slice(start, start + this.pageSize);
    },
  },
  mounted() {
    this.fetchAthletes(); // 组件挂载后获取数据
  },
  methods: {
    // 获取运动员数据
    fetchAthletes() {
      axios
        .get("./json/getHandDataList.json")
        .then((response) => {
          this.athletes = response.data; // 将返回的运动员数据赋值给 athletes
        })
        .catch((error) => {
          console.error("Error fetching athletes:", error);
        });
    },
    // 分页切换时更新当前页码
    handlePageChange(page) {
      this.currentPage = page;
    },
    // 打开抽屉并显示运动员详细信息
    openDrawer(athlete) {
      this.currentAthlete = athlete;
      this.drawerVisible = true;
    },
    // 关闭抽屉
    handleClose(done) {
      this.drawerVisible = false;
      done();
    },
  },
};
</script>

<style scoped>
/* Overall Background */
.background {
  background-image: url("./assets/background/post.jpg");
  background-size: cover;
  background-position: center;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

/* Container Styling */
.container {
  max-width: 1200px;
  margin: 0 auto;
  flex-grow: 1;
  padding: 20px; /* Adds space around content */
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1); /* Soft shadow for elegance */
}

/* Header Design */
.header-background {
  background: linear-gradient(to right, #0033A0, #D62828); /* Olympic colors */
  color: black;
  text-align: center;
  font-size: 20px;
  font-weight: bold;
  letter-spacing: 2px;
}

/* Footer Design */
.footer-background {
  background: #3770ea;
  color: white;
  text-align: center;
  margin-top: auto;
  font-size: 20px;
}

/* Athlete Carousel */
.el-carousel-item img {
  width: 100%;
  height: auto;
  object-fit: cover;
  border-radius: 10px;
  transition: transform 0.3s ease;
}

.el-carousel-item img:hover {
  transform: scale(1.05); /* Adds a zoom effect on hover */
}

/* Athlete Collapse Panels */
.collapsed-container {
  margin-top: 50px;
  background-color: rgba(255, 255, 255, 0.7);
  padding: 20px;
  border-radius: 10px;
}

.collapsed-item {
  background: rgba(255, 255, 255, 0.8);
  margin-bottom: 15px;
  border-radius: 10px;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
}

.athlete-image {
  width: 50%; /* Reduce width for better balance */
  margin: 20px auto; /* Center image */
  border-radius: 10px;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease;
}

.athlete-image:hover {
  transform: scale(1.05);
}

p {
  font-size: 1.2em;
  line-height: 1.6;
  color: #333;
}

/* Pagination */
.el-pagination {
  justify-content: center;
}

/* Drawer Styling */
.el-drawer {
  background-color: rgba(255, 255, 255, 0.9);
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
}

.el-drawer h3 {
  font-size: 1.8em;
  font-weight: bold;
  color: #0033A0;
}

.el-drawer p {
  font-size: 1.2em;
  color: #333;
}

/* Button Styling */
.el-link {
  font-weight: bold;
  color: #D62828; /* A bold red for links */
}

.el-link:hover {
  text-decoration: underline;
}


</style>
