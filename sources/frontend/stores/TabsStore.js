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
    this.pythonSetLoopingStrategy(tab);
  }

  // Actions
  pythonSetLoopingStrategy(tab) {
    eel.set_looping_strategy(tab)();
  }
}

