const tabDistortionTemplate = `
<div>
  <BaseTabContent :title="title">
  
    <button class="button is-primary is-small" 
            @click="toggleLines()" 
            :disabled="!playerState.isPlaying">
            
      {{buttonLinesText}}
    </button>  
    
    <button class="button is-primary is-small" 
            @click="toggleDistortion()" 
            :disabled="!playerState.isPlaying">
            
      {{buttonDistortionText}}
    </button>

  </BaseTabContent>
</div>
`;

Vue.component('TabDistortion', {
  template: tabDistortionTemplate,
  data: () => ({
    title: 'Distortion',
    playerState: $Store.player.state,
  }),

  computed: {
    buttonLinesText() {
      return this.playerState.haveLines ? 'Hide lines' : 'Draw lines';
    },
    buttonDistortionText() {
      return this.playerState.isDistorded ? 'Distorded' : 'Undistorded';
    },
  },

  methods: {
    toggleLines() {
      $Store.player.commitToggleLines();
    },
    toggleDistortion() {
      $Store.player.commitToggleDistortion();
    },
  },
});

