<template>
    <div class="container" >
      <div class="fieldone" :style="{ flexGrow: field1Grow}">{{ field1Content }}</div>
      <div class="fieldtwo" :style="{ flexGrow: field2Grow }">{{ field2Content }}</div>
      <div class="fieldtwo" :style="{ flexGrow: field3Grow }">{{ field3Content }}</div>
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
      field3Grow: {
        type: Number,
        default: 1
      },
      field1Content: {
        type: String,
        default: 'NO'
      },
      field2Content: {
        type: String,
        default: '姓名'
      },
      field3Content: {
        type: String,
        default: '位置'
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
    width: 300px;
    /* 边框阴影 */
    box-shadow: 0 0 5px #ccc;
    border-radius: 5px;
    margin-bottom: 5px;
    align-items: center;
    opacity: 1;
  }
  
  .field {
    padding: 5px;
    text-align: left;
  }
  .fieldone {
    padding: 5px;
    text-align: left;
    font-weight: bold;
    font-size: 13px;
  }
  .fieldtwo {
    padding: 5px;
    text-align: left;
    font-size: 11px;
  }

  </style>