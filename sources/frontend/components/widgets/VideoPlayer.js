const videoPlayerTemplate = `
<div :class="[!simplePlayer ? 'player-wrapper': 'simple-player-wrapper']">
  <div :class="[!simplePlayer ? 'player-container': 'simple-player-container']">
    <div>
      <img :id="id" src="" alt="" @click="mouseCoords">
    </div>
  </div>
</div>
`;

Vue.component('VideoPlayer', {
  template: videoPlayerTemplate,
  props: {
    id: {type: String},
  },
  data: () => ({
    tabsState: $Stores.tabs.state,
  }),
  computed: {
    simplePlayer() {
      return $Stores.tabs.simplePlayer();
    },
  },
  methods: {
    mouseCoords(e) {
      console.log(`x: ${e.offsetX}, y: ${e.offsetY}`)
    }
  },
});
