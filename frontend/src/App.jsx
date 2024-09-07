import React from 'react';
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
import Login from './Login';
import Expenses from './Expense';
import Registration from './Register';
import ManageExpenses from './ManageExpenses';
import EditExpense from './EditExpense';


const App = () => {
  return (
    <BrowserRouter>
        <Routes>
        <Route exact path="/get_my_expenses" element={<Expenses />} />
        <Route exact path="/registration" element={<Registration />} />
        <Route exact path="/manage-expenses" element={<ManageExpenses />} />
        <Route exact path="/edit-expense/:id" element={<EditExpense />} />
            </Routes>
  </BrowserRouter>

  );
};

export default App;