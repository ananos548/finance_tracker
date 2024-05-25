import React from 'react';
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
import Login from './Login';
import Expenses from './Expense';

const App = () => {
  return (
    <BrowserRouter>
        <Routes>
        <Route exact path="/login" element={<Login />} />
        <Route exact path="/get_my_expenses" element={<Expenses />} />
            </Routes>
  </BrowserRouter>

  );
};

export default App;