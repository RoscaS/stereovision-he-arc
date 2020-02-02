const tabInitializationTemplate = `
<div>
  <BaseTabContent :title="title">
  
    <button class="button is-primary is-small" 
            @click="toggleLines()" 
            :disabled="!playerState.isPlaying">
            
      {{buttonText}}
    </button>

  </BaseTabContent>
</div>
`;

Vue.component('TabInitialization', {
  template: tabInitializationTemplate,
  data: () => ({
    title: 'Initialization',
    playerState: $Stores.player.state,
  }),

  computed: {
    buttonText() {
      return this.playerState.haveLines ? 'Hide lines' : 'Draw lines';
    },
  },

  methods: {
    toggleLines() {
      if (this.playerState.isPlaying) {
        $Stores.player.commitToggleLines();
      }
    },
  },
});

