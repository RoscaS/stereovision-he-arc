const tabsTemplate = `
<div>
  <div class="tabs">
    <ul>
      <li v-for="tab in tabs" :key="tab"
          @click="changeTab(tab)"
          :class="{'is-active': activeTab === tab}">
        <a>{{ tab }}</a>
      </li>
    </ul>
  </div>
  <Loader :isActive="loading">
    <div class="tab-content content">
      
      <stereo-base v-if="activeTab === 'Base'"/>
      
      <stereo-calibration v-if="activeTab === 'Calibration'"/>
    </div>
  </Loader>
</div>
`;

Vue.component('Tabs', {
  template: tabsTemplate,
  data: () => ({
    tabs: ['Base', 'Calibration'],
    activeTab: 'Base',
    loading: false,
  }),

  methods: {
    changeTab(tab) {
      this.loading = true;
      this.stop_loop();
      eel.set_tab(tab)();

      setTimeout(() => {
        this.activeTab = tab;
        this.loading = false;
      }, 20);
    },

    stop_loop() {
      eel.stop_loop()();
      setTimeout(() => {
        leftEl().src = 'Empty';
        rightEl().src = 'Empty';
      }, 100);
    },
  },
});
