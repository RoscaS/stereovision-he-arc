const videoContainerTemplate = `
<div class="box">
  <button class="button" 
          :class="isStreaming ? 'is-danger' : 'is-success'" 
          @click="isStreaming ? stop_loop() : start_loop()">
          {{ isStreaming ? 'Stop stream' : 'Start stream' }}
  </button>
  <div class="videos-container">
    <div class="columns">
      <div class="column">
        <img id="test-left" src="" alt="">
      </div>
      <div class="column">
        <img id="test-right" src="" alt="">
      </div>
    </div>
  </div>
</div>
`;

let leftEl = () => document.getElementById('test-left');
let rightEl = () => document.getElementById('test-right');

Vue.component('VideosContainer', {
  template: videoContainerTemplate,
  data: () => ({
    tabs: ['Test', 'Calibration'],
    activeTab: 'Test',

    isStreaming: false,
  }),

  methods: {
    start_loop() {
      eel.start_loop()();
      this.isStreaming = true;
      this.$emit('startStream');
    },

    stop_loop() {
      eel.stop_loop()();
      this.$emit('stopStream');
      this.isStreaming = false;
      setTimeout(() => {
        leftEl().src = 'Empty';
        rightEl().src = 'Empty';
      }, 100);
    },
  },
  mounted() {
    const format = 'data:image/jpeg;base64,';

    function updateImageLeft(val) {leftEl().src = format + val;}
    function updateImageRight(val) {rightEl().src = format + val;}

    eel.expose(updateImageLeft);
    eel.expose(updateImageRight);
  },

});
