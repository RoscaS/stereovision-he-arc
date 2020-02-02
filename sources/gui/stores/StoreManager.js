class StoreManager {
  constructor() {
    this.tabs = new TabsStore();
    this.player = new PlayerStore();
  }

}

const $Stores = new StoreManager();
