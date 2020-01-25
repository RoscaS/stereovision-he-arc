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
    playerState: $Store.player.state,
  }),

  methods: {
    startLoop() {
      $Store.player.commitStartStream();
    },

    stopLoop() {
      $Store.player.commitStopStream();
    },
  },
});
