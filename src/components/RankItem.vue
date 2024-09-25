<template>
    <div class="rank-item">
      <el-row align="middle" type="flex">
        <!-- 排名 -->
        <el-col :span="2">
          <span>{{ rank }}</span>
        </el-col>
        
        <!-- 国旗 -->
        <el-col :span="2">
          <img :src="flag" alt="flag" class="flag-img" />
        </el-col>
        
        <!-- 国家名称 -->
        <el-col :span="8">
          <span>{{ countryName }}</span>
        </el-col>
        
        <!-- 数值显示 -->
        <el-col :span="12">
          <span>{{ gold }}</span>&nbsp;&nbsp;
          <span>{{ silver }}</span>&nbsp;&nbsp;
          <span>{{ bronze }}</span>&nbsp;&nbsp;
          <span>{{ total }}</span>
        </el-col>
        
        <!-- 操作按钮 -->
        <el-col :span="2">
          <el-button type="primary" icon="el-icon-plus" size="mini" @click="handleClick"></el-button>
        </el-col>
      </el-row>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      rank: {
        type: Number,
        default: 1
      },
      flag: {
        type: String,
        default: '' // 国旗的URL
      },
      countryName: {
        type: String,
        default: '国家'
      },
      gold: {
        type: Number,
        default: 0
      },
      silver: {
        type: Number,
        default: 0
      },
      bronze: {
        type: Number,
        default: 0
      },
      total: {
        type: Number,
        default: 0
      }
    },
    methods: {
      handleClick() {
        this.$emit('add'); // 触发添加事件
      }
    }
  }
  </script>
  
  <style scoped>
  .rank-item {
    display: flex;
    align-items: center;
    padding: 10px;
    background-color: #fff;
    border-radius: 8px;
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
  }
  
  .flag-img {
    width: 30px;
    height: 20px;
  }
  
  .el-button {
    margin-left: 10px;
  }
  </style>
  