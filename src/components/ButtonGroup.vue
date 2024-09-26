<template>
    <div class="button-group">
      <button
        v-for="(button, index) in buttons"
        :key="index"
        :class="{ active: selectedButton === index }"
        @click="selectButton(index)"
        class="button"
      >
        {{ button }}
      </button>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        selectedButton: null,
        buttons: ['直播', 'A组', 'B组', 'C组', 'D组', '1/4决赛', '半决赛', '决赛']
      };
    },
    methods: {
      selectButton(index) {
        this.selectedButton = index;
      }
    }
  };
  </script>
  
  <style scoped>
  .button-group {
    display: flex;
    gap: 10px;
  }
  
  .button {
    padding: 10px 20px;
    border: 1px solid #ccc;
    background-color: white;
    border-radius: 10px;
    cursor: pointer;
    transition: background-color 0.3s, color 0.3s;
  }
  
  .button.active {
    background-color: black;
    color: white;
  }
  
  .button:hover {
    background-color: #f0f0f0;
  }
  </style>
  