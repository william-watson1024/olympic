<template>
  <div class="line-connector" ref="connector">
    <div class="connector-line"></div>
    <div class="column-semi semi-finals">
  <DrawLines 
    v-for="(match, index) in semiFinals" 
    :key="index" 
    :startPoint="quarterPositions[index].end" 
    :endPoint="match.end" 
  />
  <div v-for="(match, index) in semiFinals" :key="index" class="match-container-semi" ref="semiMatchContainers">
    <CombinedMatch
      :upperFlagSrc="match.upperFlagSrc"
      :upperCountryName="match.upperCountryName"
      :upperScore="match.upperScore"
      :lowerFlagSrc="match.lowerFlagSrc"
      :lowerCountryName="match.lowerCountryName"
      :lowerScore="match.lowerScore"
      @highlight="handleHighlight"
    />
    <div class="horizontal-line"></div>
  </div>
</div>

  </div>
</template>

<script>
export default {
  props: {
    startPoint: {
      type: Array,
      required: true,
      validator(value) {
        return value.length === 2;
      },
    },
    endPoint: {
      type: Array,
      required: true,
      validator(value) {
        return value.length === 2;
      },
    },
  },
  mounted() {
    this.drawLine();
  },
  methods: {
    drawLine() {
      const connectorLine = this.$refs.connector.querySelector('.connector-line');
      const start = this.startPoint;
      const end = this.endPoint;

      const x1 = start[0];
      const y1 = start[1];
      const x2 = end[0];
      const y2 = end[1];

      const length = Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));
      const angle = Math.atan2(y2 - y1, x2 - x1) * (180 / Math.PI);

      connectorLine.style.width = `${length}px`;
      connectorLine.style.transform = `rotate(${angle}deg)`;
      connectorLine.style.left = `${x1}px`;
      connectorLine.style.top = `${y1}px`;
    },
  },
};
</script>

<style scoped>
.line-connector {
  position: relative;
  width: 100%;
  height: 100%;
}
.connector-line {
  position: absolute;
  background: black;
  height: 2px;
  z-index: 9999;
}
</style>
