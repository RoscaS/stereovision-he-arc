const tabsTemplate = `
<div class="tabs-wrapper">
  <div class="tabs">
    <ul>
      <li v-for="tab in tabsList" :key="tab"
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
    tabsList: $Stores.tabs.tabsList,
    tabsState: $Stores.tabs.state,
  }),

  methods: {
    setTab(tab) {
      $Stores.tabs.commitActiveTab(tab);
    },
  },
});
