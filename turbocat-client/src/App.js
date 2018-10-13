import React, { Component } from 'react';
import logo from './logo.png';
import './App.css';

import { CartesianGrid, Label, Line, LineChart, ReferenceLine, Tooltip, XAxis, YAxis } from 'recharts';

class App extends Component {
  render() {
    const data = [
      {name: '0m', percent: 50},
      {name: '15m', percent: 60},
      {name: '30m', percent: 65},
      {name: '45m', percent: 60},
      {name: '60m', percent: 50},
      {name: '75m', percent: 45},
      {name: '90m', percent: 50},
    ];
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
        </header>
        <div className="main">
          <div className="chart">
            <h1>Latest measurements</h1>
            <LineChart width={800} height={300} margin={{ top: 0, right: 30, left: 30, bottom: 30 }} data={data}>
              <ReferenceLine y={50} stroke="blue"/>
              <Line type="monotone" dataKey="percent" stroke="#483c6c" />
              <CartesianGrid stroke="#ccc" strokeDasharray="5 5" />
              <XAxis dataKey="name" padding={{right: 15}}>
                <Label value="Time of reading" offset={0} position="bottom" />
              </XAxis>
              <YAxis domain={[0, 100]}>
                <Label value="Population 1 %" offset={0} position="insideLeft" angle="-90" />
              </YAxis>
              <Tooltip />
            </LineChart>
          </div>
        </div>
      </div>
    );
  }
}

export default App;
