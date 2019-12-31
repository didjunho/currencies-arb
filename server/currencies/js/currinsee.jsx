import React from 'react';
import PropTypes, { array } from 'prop-types';

const CURRENCIES = ['CAD', 'HKD', 'ISK', 'PHP', 'DKK', 'HUF', 'CZK', 'GBP', 'RON', 'SEK', 'IDR',
  'INR', 'BRL', 'RUB', 'HRK', 'JPY', 'THB', 'CHF', 'EUR', 'MYR', 'BGN', 'TRY', 'CNY', 'NOK',
  'NZD', 'ZAR', 'USD', 'MXN', 'SGD', 'AUD', 'ILS', 'KRW', 'PLN'];
CURRENCIES.sort();

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
    const columns = [];
    let lastUpdated = '';
    columns.push(<th key="title" />);
    CURRENCIES.forEach(item =>
      columns.push(React.createElement('th', { key: item },
        item,
      )),
    );
    infoList.push(<tr key="top-row">{columns}</tr>);
    Object.entries(this.state.info).forEach(([key1, value]) => {
      if (key1 === 'updated') {
        lastUpdated = value.time;
        return;
      }
      const children = [];
      Object.entries(value).forEach(([key2, value2]) => {
        children.push(React.createElement('th', { key: key2, style: { fontWeight: 'normal' } },
          parseFloat(value2.toFixed(6)),
        ));
      });
      const row = React.createElement('tr', { className: 'info', key: key1 },
        <th>{key1}</th>,
        children,
      );
      infoList.push(row);
    });
    return (
      <div>
        <h2>Last Updated: {lastUpdated}</h2>
        <table>
          <tbody>
            {infoList}
          </tbody>
        </table>
      </div>
    );
  }
}

Currency.propTypes = {
  url: PropTypes.string.isRequired,
};

export default Currency;
