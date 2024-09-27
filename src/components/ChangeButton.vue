<template>
    <div class="menu">
      <div
        v-for="(item, index) in menuItems"
        :key="index"
        :class="['menu-item', { active: activeIndex === index }]"
        @click="setActive(index)"
      >
        {{ item }}
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        menuItems: ['出赛名单', '比赛详情', '团队数据', '运动员数据'],
        activeIndex: 0, // 默认选中的菜单项
      };
    },
    methods: {
      setActive(index) {
        this.activeIndex = index;
      },
    },
  };
  </script>
  
  <style scoped>
  .menu {
    display: flex;
    width: 120%; /* 调整菜单宽度 */
    margin: 0 auto;
  }
  
  .menu-item {
    padding: 10px;
    cursor: pointer;
    font-size: 16px;
    font-weight: normal;
    border-bottom: 2px solid transparent;
  }
  
  .menu-item.active {
    font-size: 20px;
    font-weight: bold;
    border-bottom: 2px solid black; /* 激活状态的下边框 */
  }
  
  .menu-item:not(.active):hover {
    font-weight: normal;
    border-bottom: 2px solid gray; /* 悬停时的效果 */
  }
  </style>
  