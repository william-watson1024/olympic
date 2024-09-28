<template>
  <div 
    class="country-card" 
    :style="{ backgroundColor: isHovered ? 'black' : color, color: isHovered ? 'white' : 'inherit' }" 
    @mouseover="isHovered = true" 
    @mouseleave="isHovered = false"
  >
    <div class="flag">
      <img :src="flagSrc" alt="Country Flag" />
    </div>
    <span v-html="countryName"></span>
    <div class="score">{{ score }}</div>
  </div>
</template>

<script>
export default {
  props: {
    flagSrc: { type: String, required: true },
    countryName: { type: String, required: true },
    score: { type: String, required: true },
    isHighlighted: { type: Boolean, default: false },
    // 新增 color 属性
    color: { type: String, default: 'white' } // 默认值为白色
  },
  data() {
    return {
      isHovered: false // 用于跟踪鼠标悬停状态
    };
  }
};
</script>

<style scoped>
.country-card {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 300px;
  height: 40px; 
  border-radius: 0 0 15px 15px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  padding: 10px;
  transition: background-color 0.3s, color 0.3s;
}

.flag img {
  width: 40px;
  height: auto;
}

.country-name {
  flex-grow: 1;
  margin-left: 10px;
  font-size: 16px;
  font-weight: bold;
}

.score {
  font-size: 16px;
  font-weight: bold;
}
</style>
