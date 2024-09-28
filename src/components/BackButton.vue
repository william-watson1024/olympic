<template>
  <div class="back-button-container">
    <router-link to="/matchList" class="back-button"> <!-- Update this path -->
      <img src="@/assets/logo/back.png" alt="Back" class="back-icon" />
    </router-link>
  </div>
</template>

<style scoped>
.back-button-container {
  display: flex;
  justify-content: flex-start;
  align-items: center;
  margin: 10px;
}

.back-button {
  display: inline-flex;
  align-items: center;
}

.back-icon {
  width: 24px;
  height: auto;
  margin-right: 8px;
}
</style>

<script>
export default {
  name: 'BackButton',
  // Add other properties or methods as needed
};
</script>
