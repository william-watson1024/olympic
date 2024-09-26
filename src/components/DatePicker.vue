<template>
  <div class="date-picker-wrapper" ref="wrapper">
    <div
      class="date-picker-container"
      ref="container"
      @mousedown="onMouseDown"
      @mousemove="onMouseMove"
      @mouseup="onMouseUp"
      @mouseleave="onMouseUp"
    >
      <div
        class="date-container"
        v-for="(date, index) in dates"
        :key="index"
        :class="{ toggled: selectedDate === date }"
        @click="selectDate(date)"
      >
        {{ date }}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    dateText: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      dates: this.generateDates(new Date(2023, 6, 24), new Date(2023, 7, 11)),
      selectedDate: null,
      isDragging: false,
      startX: 0,
      scrollLeft: 0
    };
  },
  methods: {
    generateDates(startDate, endDate) {
      const dates = [];
      let currentDate = new Date(startDate);
      while (currentDate <= endDate) {
        dates.push(
          currentDate.toLocaleDateString("zh-CN", {
            month: "long",
            day: "numeric"
          })
        );
        currentDate.setDate(currentDate.getDate() + 1);
      }
      return dates;
    },
    selectDate(date) {
      this.selectedDate = date;
      this.$emit('date-selected', date)
    },
    onMouseDown(e) {
      this.isDragging = true;
      this.startX = e.pageX - this.$refs.container.offsetLeft;
      this.scrollLeft = this.$refs.container.scrollLeft;
      this.$refs.wrapper.style.cursor = 'grabbing'; // Change cursor to grabbing
    },
    onMouseMove(e) {
      if (!this.isDragging) return;
      e.preventDefault();
      const x = e.pageX - this.$refs.container.offsetLeft;
      const walk = (x - this.startX) * 2; // scroll-fast
      this.$refs.container.scrollLeft = this.scrollLeft - walk;
    },
    onMouseUp() {
      this.isDragging = false;
      this.$refs.wrapper.style.cursor = 'grab'; // Revert cursor
    }
  },
  mounted() {
    // Add event listeners to container for drag functionality
    this.$refs.container.addEventListener('mousedown', this.onMouseDown);
    this.$refs.container.addEventListener('mousemove', this.onMouseMove);
    this.$refs.container.addEventListener('mouseup', this.onMouseUp);
    this.$refs.container.addEventListener('mouseleave', this.onMouseUp);
  },
  beforeDestroy() {
    // Remove event listeners
    this.$refs.container.removeEventListener('mousedown', this.onMouseDown);
    this.$refs.container.removeEventListener('mousemove', this.onMouseMove);
    this.$refs.container.removeEventListener('mouseup', this.onMouseUp);
    this.$refs.container.removeEventListener('mouseleave', this.onMouseUp);
  }
};
</script>

<style>
.date-picker-wrapper {
  overflow: hidden;
  cursor: grab;
  margin-bottom: 50px;
}

.date-picker-container {
  display: flex;
  white-space: nowrap;
  user-select: none;
  overflow-x: auto; /* Make container scrollable */
  -ms-overflow-style: none;  /* IE and Edge */
scrollbar-width: none;  /* Firefox */
}

.date-container {
  display: inline-block;
  padding: 10px 20px;
  border-radius: 20px;
  background-color: #ffffff;
  color: #333;
  cursor: pointer;
  transition: background-color 0.3s, color 0.3s;
  border: 1px solid #dfdfdf;
  margin-right: 10px;
  margin-left: 10px;
}

.date-container:hover {
  opacity: 0.8;
}

.date-container.toggled {
  background-color: #333;
  color: #ffffff;
}
</style>
