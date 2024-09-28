<template>
  <div class="backgrouond">
    <change-button-vue>

    </change-button-vue>
    <DetailRatingItem>

    </DetailRatingItem>
    <ButtonGroup>

    </ButtonGroup>
    <ManPositionTitle>

    </ManPositionTitle>
    <ManPosition>

    </ManPosition>
    <ManPosition :opacity="1">

    </ManPosition>
    
    <CombinedMatch>
      upperFlagSrc="path/to/upperFlag.png" 
      upperCountryName="Country A" 
      :upperScore="90"
      lowerFlagSrc="path/to/lowerFlag.png" 
      lowerCountryName="Country B" 
      :lowerScore="85" 
    </CombinedMatch>

  </div>
</template>

<script>
import DetailRatingItem from './components/DetailRatingItem.vue';
import ButtonGroup from './components/ButtonGroup.vue';
import ChangeButtonVue from './components/ChangeButton.vue';
import ManPosition from './components/ManPosition.vue';
import ManPositionTitle from './components/ManPositionTitle.vue';
import CombinedMatch from './components/CombinedMatch.vue';
export default {
  components: {
    DetailRatingItem,
    ButtonGroup,
    ChangeButtonVue,
    ManPosition,
    ManPositionTitle,
    CombinedMatch
  },
  data() {
    return {

    };
  },
  methods: {

  },
};
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  font-size: 14px;
  text-align: center;
  color: #2c3e50;

}

.backgrouond {
  background-image: url('@/assets/background/sea.jpg');
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
}

h1,
h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>