import React from 'react';
import ReactDOM from 'react-dom';
import CssBaseline from '@material-ui/core/CssBaseline';
import { ThemeProvider } from '@material-ui/core/styles';
import Paperbase from './Paperbase';
import theme from './theme';

import server from './fakeserver';
console.log("Using fake server", server());

ReactDOM.render(
  <ThemeProvider theme={theme}>
    {/* CssBaseline kickstart an elegant, consistent, and simple baseline to build upon. */}
    <CssBaseline />
    <Paperbase />
  </ThemeProvider>,
  document.querySelector('#root'),
);
