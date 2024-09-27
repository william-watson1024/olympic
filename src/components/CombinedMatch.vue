<template>
  <div class="combined-match">
    <UpperMatch 
      :flagSrc="upperFlagSrc" 
      :countryName="upperCountryName" 
      :score="upperScore" 
    />
    <LowerMatch 
      :flagSrc="lowerFlagSrc" 
      :countryName="lowerCountryName" 
      :score="lowerScore" 
    />
    <div :class="{'highlight': isHighlighted}" @mouseover="highlight(true)" @mouseleave="highlight(false)">
    </div>
  </div>
</template>

<script>
import UpperMatch from './UpperMatch.vue';
import LowerMatch from './LowerMatch.vue';

export default {
  components: {
    UpperMatch,
    LowerMatch
  },
  props: {
    upperFlagSrc: {
      type: String,
      required: true
    },
    upperCountryName: {
      type: String,
      required: true
    },
    upperScore: {
      type: Number,
      required: true
    },
    lowerFlagSrc: {
      type: String,
      required: true
    },
    lowerCountryName: {
      type: String,
      required: true
    },
    lowerScore: {
      type: Number,
      required: true
    },
    highlightMatch: {
      type: Boolean,
      default: false
    }
  },
   methods: {
    highlight(state) {
      this.$emit('highlight', this.upperCountryName, state);
    }
  }
};
</script>

<style scoped>
.combined-match {
  width: 300px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  border-radius: 15px;
  position: relative;
}

.highlight {
  border: 2px solid #ffcc00; /* 高亮效果 */
  position: absolute;
  top: -2px; /* 调整位置以覆盖边框 */
  left: -2px;
  right: -2px;
  bottom: -2px;
  z-index: 1; /* 确保高亮在上层 */
}
</style>
