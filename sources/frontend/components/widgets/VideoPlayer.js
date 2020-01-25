const videoPlayerTemplate = `
<div class="video-player-wrapper">
  <div class="video-player-container">
    <div>
      <img :id="id" src="" alt="" >
    </div>
  </div>
</div>
`;

Vue.component('VideoPlayer', {
  template: videoPlayerTemplate,
  props: {
    id: {type: String}
  },
  data: () => ({

  }),

  methods: {

  },
});
