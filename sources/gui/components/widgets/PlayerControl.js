const playerControlTemplate = `
<div>
  <button class="button" 
          :class="playerState.isPlaying ? 'is-danger' : 'is-success'" 
          @click="playerState.isPlaying ? stopLoop() : startLoop()">
          {{ playerState.isPlaying ? 'Stop stream' : 'Start stream' }}
  </button>
</div>
`;

Vue.component('PlayerControl', {
  template: playerControlTemplate,
  data: () => ({
    playerState: $Stores.player.state,
  }),

  methods: {
    startLoop() {
      console.log("ICI")
      $Stores.player.commitStartStream();
    },

    stopLoop() {
      console.log("La")
      $Stores.player.commitStopStream();
    },
  },
});
