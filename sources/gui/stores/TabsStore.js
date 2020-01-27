class TabsStore {
  constructor() {
    this.state = {
      activeTab: 'Initialization',
    };
    this.tabsList = [
      'Initialization',
      // 'Calibration',
      'Distortion',
      // 'Tuning',
      'Depth',
    ];
    this.twoPlayers = [
      'Initialization',
      'Distortion',
    ];
  }

  // GETTERS
  simplePlayer() {
    return !this.twoPlayers.includes(this.state.activeTab);
  }

  // MUTATIONS
  commitActiveTab(tab) {
    $Stores.player.commitStopStream();
    this.state.activeTab = tab;
    this.pythonSetLoopingStrategy(tab);
  }

  // ACTIONS
  pythonSetLoopingStrategy(tab) {
    eel.set_looping_strategy(tab)();
  }
}

