const tabsContentTemplate = `
<div>
  <div v-if="tabsState.activeTab === 'Initialization'">
    <tab-initialization/>
  </div>
  <div v-if="tabsState.activeTab === 'Calibration'">
    <tab-calibration/>
  </div>
  <div v-if="tabsState.activeTab === 'Distortion'">
    <tab-distortion/>
  </div>
  <div v-if="tabsState.activeTab === 'Tuning'">
    <p>Tuning</p>
  </div>
  <div v-if="tabsState.activeTab === 'Depth'">
    <tab-depth/>
  </div>

</div>
`;

Vue.component('TabsContent', {
  template: tabsContentTemplate,
  data: () => ({
    tabsState: $Stores.tabs.state,
  }),

  methods: {},
});
