import React, { Component } from "react";
import "./App.css";
import SpotifyList from "./SpotifyList";

class App extends Component {
  render() {
    return (
      <div className="App">
        <header />
        <SpotifyList />
      </div>
    );
  }
}

export default App;
