<template>
  <div class="container">
    <div class="fieldone" :style="{ flexGrow: field1Grow }">{{ field1Content }}</div>
    <div class="fieldtwo" :style="{ flexGrow: field2Grow }">{{ field2Content }}</div>
  </div>
</template>

<script>
export default {
  name: 'FlexGrowComponent',
  props: {
    field1Grow: {
      type: Number,
      default: 1
    },
    field2Grow: {
      type: Number,
      default: 15
    },
    field1Content: {
      type: String,
      default: '时间'
    },
    field2Content: {
      type: String,
      default: ' '
    },
    containerOpacity: {
      type: Number,
      default: 1
    }
  }
}
</script>

<style scoped>
.container {
  display: flex;
  background-color: white;
  box-shadow: 0 0 5px #ccc;
  border-radius: 5px;
  margin-bottom: 5px;
  align-items: center;
  opacity: 1;
  width: 900px;
  height: 50px;
}

.fieldone{
  display: flex;
  justify-content: center;
  align-items: center;
  height: inherit;
  text-align: center;
  font-weight: bold;
  font-size: 13px;
  width: 80px;
  border-right: #ccc 1px solid;
}
.fieldtwo {
  display: flex;
  justify-content: left;
  margin-left: 10px;
  align-items: center;
  height: inherit;
  text-align: left;
  width: 200px;
  font-size: 11px;
}

</style>