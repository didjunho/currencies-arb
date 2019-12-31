import React from 'react';
import PropTypes from 'prop-types';


class Currency extends React.Component {
  constructor(props) {
    // Initialize mutable state
    super(props);
    this.handleRequest = this.handleRequest.bind(this);
    this.state = { info: {} };
  }

  componentDidMount() {
    this.handleRequest(this.props.url, 'GET');
    setInterval(() => this.handleRequest(this.props.url, 'GET'), 5000);
  }

  handleRequest(url, methodType) {
    fetch(url, { method: methodType, credentials: 'same-origin' })
      .then((response) => {
        if (!response.ok) throw Error(response.statusText);
        return response.json();
      })
      .then((data) => {
        this.setState({
          info: data,
        });
      })
      .catch(error => console.log(error));
  }

  render() {
    const infoList = [];
    Object.entries(this.state.info).forEach(([key, value]) => {
      console.log(key, value);
      infoList.push(
        React.createElement('div', { className: 'info' },
          <div className="infoIn">
            {key} : {value}
          </div>,
        ),
      );
    });
    return (
      <div>
        {infoList}
      </div>
    );
  }
}

Currency.propTypes = {
  url: PropTypes.string.isRequired,
};

export default Currency;
