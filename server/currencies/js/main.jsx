import React from 'react';
import ReactDOM from 'react-dom';
import Currency from './currinsee';

// This method is only called once
ReactDOM.render(
  <Currency url="/api/get/" />,
  document.getElementById('reactEntry'),
);
