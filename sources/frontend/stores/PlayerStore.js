let VIEOFORMAT = 'data:image/jpeg;base64,';
let leftPlayerEl = () => document.getElementById('left-player');
let rightPlayerEl = () => document.getElementById('right-player');

function updateImageLeft(val) {leftPlayerEl().src = VIEOFORMAT + val;}

function updateImageRight(val) {rightPlayerEl().src = VIEOFORMAT + val;}

eel.expose(updateImageLeft);
eel.expose(updateImageRight);

class PlayerStore {
  constructor() {
    this.state = {
      isPlaying: false,
      haveLines: false,

      // Distortion tab
      isDistorded: true,

      // Depth tab
      isSGBM: true,
      depthMode: 'WLS',


      minDisparity: 2,
    };

    this.depthMods = ['Disparity', 'Colored', 'WLS'];
  }

  _resetDefaultOptions() {
    this.state.isPlaying = false;
    this.state.haveLines = false;
    this.state.isDistorded = true;
    this.state.isSGBM = true;
  }

  // MUTATIONS
  commitStartStream() {
    this.state.isPlaying = true;
    this.pythonStartLoop();
  }

  commitStopStream() {
    this._resetDefaultOptions();
    this.pythonStopLoop();
    setTimeout(() => {
      leftPlayerEl().src = '';
      rightPlayerEl().src = '';
    }, 100);
  }

  commitToggleLines() {
    this.state.haveLines = !this.state.haveLines;
    this.pythonToggleLines();
  }

  commitToggleDistortion() {
    this.state.isDistorded = !this.state.isDistorded;
    this.pythonToggleDistortion();
  }

  commitSwitchBlockmatcherMode() {
    this.state.isSGBM = !this.state.isSGBM;
    this.pythonSwitchBlockmatcherMode();
  }

  commitSwitchDepthMode(mode) {
    this.state.depthMode = mode;
    this.pythonSwitchDepthMode(mode);
  }

  // ACTIONS
  pythonStartLoop() {
    eel.start_loop()();
  }

  pythonStopLoop() {
    eel.stop_loop()();
  }

  pythonToggleLines() {
    eel.toggle_lines()();
  }

  pythonToggleDistortion() {
    eel.toggle_distortion()();
  }

  pythonSwitchBlockmatcherMode() {
    eel.switch_blockmatcher_mode()();
  }

  pythonSwitchDepthMode(mode) {
    eel.switch_depth_mode(mode)();
  }
}

