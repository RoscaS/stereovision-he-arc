class TabsStore {
  constructor() {
    this.state = {
      tabs: [
        'Initialization',
        'Calibration',
        'Distortion',
        'Tuning',
        'Depthmap',
      ],
      activeTab: 'Initialization',
    };
  }

  // MUTATIONS
  commitActiveTab(tab) {
    $Store.player.commitStopStream();
    this.state.activeTab = tab;
    this.pythonSetTab(tab);
  }

  // Actions
  pythonSetTab(tab) {
    eel.set_tab(tab)();
  }
}

