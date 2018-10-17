import React, { Component } from 'react';
import PropTypes from 'prop-types';
import logo from './logo.png';
import './App.css';

import { CartesianGrid, Label, Line, LineChart, ReferenceLine, Tooltip, XAxis, YAxis } from 'recharts';

const apiUrl = 'http://localhost:5000'

class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      ratio: props.ratio,
      results: [],
    }

    this.handleChange = this.handleChange.bind(this);
  }

  componentDidMount() {
    this.updateResults()
    this.interval = setInterval(() => this.updateResults(), 10000);
  }

  componentWillUnmount() {
    clearInterval(this.interval);
  }

  handleChange(event) {
    const ratio = event.target.value;
    this.setRatio(ratio);
    this.setState({ratio});
  }

  updateResults() {
    fetch(`${apiUrl}/results`)
      .then(res => res.json())
      .then(
        (result) => {
          this.setState({
            results: result
          });
        },
        (error) => {
          // this.setState({
          //   isLoaded: true,
          //   error
          // });
        }
      )
  }

  setRatio(ratio) {
    fetch(`${apiUrl}/set_ratio`, {method: 'POST', body: JSON.stringify({ratio})})
      .then(res => res.json())
      .then(
        (result) => {
          // this.setState({
          //   results: result
          // });
          console.log(result);
        },
        (error) => {
          // this.setState({
          //   isLoaded: true,
          //   error
          // });
        }
      )
  }

  render() {
    const data = this.state.results;
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
        </header>
        <div className="main">
          <div className="chart">
            <form className="setRatio">
              <div className="form-group">
                <label htmlFor="formControlRange">
                  <h2>Target population ratio ({this.state.ratio}%)</h2>
                </label>
                <input
                  type="range"
                  value={this.state.ratio}
                  onChange={this.handleChange}
                  className="form-control-range"
                  id="formControlRange"
                />
              </div>
            </form>
            <h2>Latest measurements</h2>
            <LineChart width={800} height={300} margin={{ top: 0, right: 30, left: 30, bottom: 30 }} data={data}>
              <ReferenceLine y={this.state.ratio} stroke="blue"/>
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

App.propTypes = {
  ratio: PropTypes.number,
};

App.defaultProps = {
  ratio: 50,
};

export default App;
