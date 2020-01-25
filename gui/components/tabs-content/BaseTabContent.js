const baseTabContentTemplate = `
<div class="tab-content">
  <div class="tab-content-header">
    <h2 class="debug">{{ title }}</h2>
    <div class="player-controler">
      <player-control/>
    </div>    
  </div>

  <div class="players-wrapper">
    <video-player id="left-player"/>
    <video-player id="right-player"/>
  </div>
  
  <div class="players-options">
    <slot></slot>
  </div>

</div>
`;

Vue.component('BaseTabContent', {
  template: baseTabContentTemplate,
  props: {
    title: {type: String, default: 'no title !'}
  },
  data: () => ({

  }),

  methods: {

  },
});
