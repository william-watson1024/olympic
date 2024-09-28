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
  components: {
  },
  data() {
    return {
      selectedButton: null,
      buttons: ['直播', '男子A组', '男子B组', '男子C组', '男子D组', '男子四分之一决赛', '男子半决赛', '男子决赛']
    };
  },
  methods: {
    selectButton(index) {
      this.selectedButton = index;  // Update selectedButton based on button index
      this.$emit('button-selected', this.buttons[index])

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
