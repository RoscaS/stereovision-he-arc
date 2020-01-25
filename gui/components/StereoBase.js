const stereoBaseTemplate = `
<div>
  <h1 class="tile">Stereo tests</h1>

  <videos-container @startStream="startStream()"
                    @stopStream="stopStream()"/>
    <button class="button is-primary" 
            @click="toggle_lines()" 
            v-if="isStreaming">
      Draw lines
    </button>
</div>
`;

Vue.component('StereoBase', {
  template: stereoBaseTemplate,
  data: () => ({
    isStreaming: false,
  }),

  methods: {
    toggle_lines() {
      eel.toggle_lines()();
    },
    startStream(e) {
      this.isStreaming = true;
    },
    stopStream(e) {
      this.isStreaming = false;
    },
  },
});
