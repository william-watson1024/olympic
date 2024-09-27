<template>
  <div class="country-card">
    <div class="flag">
      <img :src="flagSrc" alt="Country Flag" />
    </div>
    <div class="country-name">{{ countryName }}</div>
    <div class="score">{{ score }}</div>
  </div>
</template>

<script>
export default {
  props: {
    flagSrc: {
      type: String,
      required: true
    },
    countryName: {
      type: String,
      required: true
    },
    score: {
      type: String,
      required: true
    }
  }
};
</script>

<style scoped>
.country-card {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 300px;
  height: 20px; /* 将高度降低 */
  background-color: white;
  border-radius: 0 0 15px 15px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  padding: 10px;
}

.flag img {
  width: 40px; /* 缩小国旗的宽度 */
  height: auto;
  border: 2px solid #ccc; /* Adjust color as needed */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
  border-radius: 5px; /* Optional: round corners */
}

.country-name {
  flex-grow: 1;
  margin-left: 10px; /* 调整左边距以确保国家名称靠左 */
  font-size: 16px; /* 调整国家名称的大小 */
  font-weight: bold;
  text-align: left; /* 确保国家名称靠左对齐 */
}

.score {
  font-size: 16px; /* 调整得分字体大小 */
  font-weight: bold;
  color: #333;
}
</style>
