
class StoreManager {
  constructor() {
    this.tabs = new TabsStore();
    this.player = new PlayerStore();
  }

}

const $Store = new StoreManager();
