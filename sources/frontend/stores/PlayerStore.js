let vieoFormat = 'data:image/jpeg;base64,';
let leftPlayerEl = () => document.getElementById('left-player');
let rightPlayerEl = () => document.getElementById('right-player');

function updateImageLeft(val) {leftPlayerEl().src = vieoFormat + val;}

function updateImageRight(val) {rightPlayerEl().src = vieoFormat + val;}

eel.expose(updateImageLeft);
eel.expose(updateImageRight);

class PlayerStore {
  constructor() {
    this.state = {
      isPlaying: false,
      haveLines: false,

      // Distortion tab
      isDistorded: false,
    };
  }

  // MUTATIONS
  commitStartStream() {
    this.state.isPlaying = true;
    this.pythonStartLoop();
    this.pythonEelTest();
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

  _resetDefaultOptions() {
    this.state.isPlaying = false;
    this.state.haveLines = false;
    this.state.isDistorded = false;

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

    pythonEelTest() {
    eel.print_something()();
  }

}

