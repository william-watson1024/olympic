<template>
  <div class="combined-match" @mouseover="$emit('mouseover')" @mouseleave="$emit('mouseleave')">
    <div class="upper-match" :class="{ highlighted: isHighlighted }">
      <UpperMatch 
        :flagSrc="upperFlagSrc" 
        :countryName="isUpperWinner ? `<strong>${upperCountryName}</strong>` : upperCountryName" 
        :score="upperScore" 
        :color="change_colorr"

      />
    </div>
    <div class="lower-match" :class="{ highlighted: isHighlighted }">
      <LowerMatch 
        :flagSrc="lowerFlagSrc" 
        :countryName="isLowerWinner ? `<strong>${lowerCountryName}</strong>` : lowerCountryName" 
        :score="lowerScore" 
        :color="change_colorr"
      />
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
    upperFlagSrc: { type: String, required: true },
    upperCountryName: { type: String, required: true },
    upperScore: { type: String, required: true },
    lowerFlagSrc: { type: String, required: true },
    lowerCountryName: { type: String, required: true },
    lowerScore: { type: Number, required: true },
    defaultColor: { type: String,  required: true,default:"white"} // 添加一个 props 参数
  },
  
  data() {
    return {
      isHighlighted: false,
      change_colorr: this.defaultColor // 使用 props 参数
    };
  },
  computed: {
    isUpperWinner() {
      return this.upperScore > this.lowerScore;
    },
    isLowerWinner() {
      return this.lowerScore > this.upperScore;
    }
  }
};
</script>
