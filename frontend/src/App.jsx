import React from 'react';
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
import Login from './Login';
import Expenses from './Expense';
import Registration from './Register'

const App = () => {
  return (
    <BrowserRouter>
        <Routes>
        <Route exact path="/get_my_expenses" element={<Expenses />} />
        <Route exact path="/registration" element={<Registration />} />
            </Routes>
  </BrowserRouter>

  );
};

export default App;