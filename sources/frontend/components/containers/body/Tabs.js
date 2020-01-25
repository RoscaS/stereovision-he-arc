const tabsTemplate = `
<div class="tabs-wrapper">
  <div class="tabs">
    <ul>
      <li v-for="tab in tabsState.tabs" :key="tab"
          @click="setTab(tab)"
          class="tab"
          :class="{'is-active': tab === tabsState.activeTab}">
        <a>{{ tab }}</a>
      </li>
    </ul>
  </div>
  <div class="tabs-content debug">
    <tabs-content/>
  </div>
</div>
`;

Vue.component('Tabs', {
  template: tabsTemplate,
  data: () => ({
    tabsState: $Store.tabs.state,
  }),

  methods: {
    setTab(tab) {
      $Store.tabs.commitActiveTab(tab);
    },
  },
});
