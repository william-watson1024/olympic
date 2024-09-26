<template>
  <div>
    <!-- 顶部导航栏 -->
    <header class="header">
      <div class="logo">
        <img src="@/assets/logo/paris.webp" alt="Logo" />
      </div>
      <nav>
        <ul class="nav-links">
          <li><a href="#">Medal</a></li>
          <li><a href="#">Schedule</a></li>
          <li><a href="#">News</a></li>
          <li><a href="#">Match table</a></li>
          <li><a href="#">More</a></li>
        </ul>
      </nav>
      <div class="search-container">
        <input type="text" placeholder="Search" />
        <button class="search-icon">🔍</button>
      </div>
    </header>

    <!-- 主内容区 -->
    <main class="main-content">
      <div class="image-container">
        <!-- 图片区域 -->
        <img src="@/assets/background/main.jpg" alt="Main Image" />
      </div>
      <div class="opening-ceremony">
        <h1>The opening ceremony</h1>
      </div>
    </main>

    <!-- 底部版权信息 -->
    <footer class="footer">
      <p>Copyright @2024 All rights reserved</p>
    </footer>
  </div>
</template>

<script>
export default {
  name: "HomePage",
};
</script>

<style scoped>
/* 顶部导航栏样式 */
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #002a7f;
}

.logo img {
  height: 100px;
}

.nav-links {
  display: flex;
  list-style-type: none;
}

.nav-links li {
  margin: 0 15px;
}

.nav-links a {
  color: white;
  text-decoration: none;
  font-size: 18px;
  padding: 40px;
}

.search-container {
  display: flex;
  align-items: center;
}

.search-container input {
  padding: 5px;
  font-size: 16px;
}

.search-icon {
  background-color: transparent;
  border: none;
  color: white;
  font-size: 20px;
  margin-left: 5px;
  cursor: pointer;
}

/* 主内容样式 */
.main-content {
  text-align: center;
  margin-top: 0px;
}

.image-container img {
  padding: 0;
  width: 100%;
  height: 550px;
}

.opening-ceremony h1 {
  font-family: "Arial Black", Gadget, sans-serif;
  color: #0c3b87;
  margin-top: 20px;
}

/* 底部版权信息样式 */
.footer {
  background-color: #002a7f;
  color: white;
  text-align: center;
  padding: 10px 0;
  margin-top: 20px;
}
</style>
