<template>
  <div class="container">
    <div class="RankItem">
      <el-row align="middle" type="flex">
        <!-- 排名 -->
        <el-col :span="2">
          <span>{{ rank }}</span>
        </el-col>
        
        <!-- 国旗 -->
        <el-col :span="2">
          <img :src="flag" alt="flag" class="flag-img" />
        </el-col>
        
        <!-- 国家名称 -->
        <el-col :span="8">
          <span>{{ countryName }}</span>
        </el-col>
        
        <!-- 奖牌数量 -->
        <el-col :span="2">
          <span>{{ gold }}</span>
        </el-col>
        <el-col :span="2">
          <span>{{ silver }}</span>
        </el-col>
        <el-col :span="2">
          <span>{{ bronze }}</span>
        </el-col>
        <el-col :span="2">
          <span>{{ total }}</span>
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    rank: Number,
    flag: String,
    countryName: String,
    gold: Number,
    silver: Number,
    bronze: Number,
    total: Number
  }
}
</script>

<style scoped>
.container {
  display: flex;
  justify-content: center; /* 水平居中 */
}

.RankItem {
  width: 1000px; /* 固定宽度 */
  border: 1px solid #ccc; /* 可选：添加边框以更好地查看效果 */
  padding: 10px;
  align-items: center;
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
}

.flag-img {
  width: 100%; /* 确保国旗图片适应列宽 */
}
</style>