const tabDepthTemplate = `
<div>
  <BaseTabContent :title="title">
  

    
  <div class="depth-options">
    <div class="depth-options-label">
      <div><b>Stereo matcher mode:</b></div>
      <div><b>Depth map mode:</b></div>
    </div>
    <div class="depth-radios-inputs">
    
      <div class="control">
        <label class="radio" @click="switchBlockmatcherMode()" >
          <input type="radio" name="SGBM" :checked="playerState.isSGBM">
          SGBM
        </label>
        <label class="radio" @click="switchBlockmatcherMode()" >
          <input type="radio" name="SBM" :checked="!playerState.isSGBM">
          SBM
        </label>
      </div>
      
      <div class="control">
        <label v-for="mode in depthMods" :key="mode.name" 
               @click="radioModeClick(mode)"
               class="radio">
          <input type="radio" :name="mode.name" :checked="isModeChecked(mode.name)">
          {{ mode.name }}
        </label>
      </div>
      
    </div>
  </div>
    
    
  </BaseTabContent>
</div>
`;

Vue.component('TabDepth', {
  template: tabDepthTemplate,
  data: () => ({
    title: 'Depth',
    playerState: $Stores.player.state,
  }),

  computed: {

    depthMods() {
      return $Stores.player.depthMods.map(i => {
        return {name: i, checked: this.playerState.depthMode === i};
      });
    },
    buttonText() {
      return this.playerState.isSGBM ? 'SBM' : 'SGBM';
    },
  },

  methods: {
    isModeChecked(modeName) {
      return modeName === this.playerState.depthMode;
    },
    switchBlockmatcherMode() {
      if (this.playerState.isPlaying) {
        $Stores.player.commitSwitchBlockmatcherMode();
      }
    },
    radioModeClick(mode) {
      $Stores.player.commitSwitchDepthMode(mode.name);
    },
  },
});
