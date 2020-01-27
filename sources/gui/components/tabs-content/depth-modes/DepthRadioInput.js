const depthRadioInputTemplate = `
<div class="depth-options">
  <div class="depth-options-label">
    <div><b>Stereo matcher mode:</b></div>
    <div><b>Depth map mode:</b></div>
  </div>
  <div class="depth-radios-inputs">
    <div class="control">
      <label class="radio" >
        <input :disabled="!playerState.isPlaying" 
               type="radio" 
               name="SGBM" 
               @click="switchBlockmatcherMode()"
               :checked="playerState.isSGBM">
        SGBM
      </label>
      <label class="radio" >
        <input :disabled="!playerState.isPlaying" 
               type="radio" 
               name="SBM" 
               @click="switchBlockmatcherMode()"
               :checked="!playerState.isSGBM">
        SBM
      </label>
    </div>
    
    <div class="control">
      <label v-for="mode in depthMods" :key="mode.name" 
             @click="radioModeClick(mode)"
             class="radio">
        <input :disabled="!playerState.isPlaying" 
               type="radio" 
               :name="mode.name" 
               :checked="isModeChecked(mode.name)">
        {{ mode.name }}
      </label>
    </div>
  </div>
</div>
`;

Vue.component('DepthRadioInput', {
  template: depthRadioInputTemplate,
  data: () => ({
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
      if (this.playerState.isPlaying) {
        $Stores.player.commitSwitchDepthMode(mode.name);
      }
    },
  },
});
