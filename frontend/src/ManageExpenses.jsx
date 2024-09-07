import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Link, useNavigate } from 'react-router-dom';
import styled from 'styled-components';

const Container = styled.div`
  margin: 0 auto;
  padding: 20px;
  background-color: #fff;
  display: flex;
  flex-direction: column;
  align-items: center;
  color: black;
`;

const ExpenseList = styled.ul`
  list-style: none;
  padding: 0;
  width: 100%;
  max-width: 600px;
`;

const ExpenseItem = styled.li`
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  margin-bottom: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
`;

const Button = styled.button`
  padding: 5px 10px;
  margin-left: 10px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
`;

const EditButton = styled(Button)`
  background-color: #28a745;
  color: white;

  &:hover {
    background-color: #218838;
  }
`;

const DeleteButton = styled(Button)`
  background-color: #dc3545;
  color: white;

  &:hover {
    background-color: #c82333;
  }
`;

const ManageExpenses = () => {
  const [expenses, setExpenses] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    fetchExpenses();
  }, []);

  axios.defaults.withCredentials = true;
  axios.defaults.baseURL = 'http://127.0.0.1:8081';

  const fetchExpenses = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:8081/finances/get_my_expenses');
      setExpenses(response.data);
    } catch (error) {
      console.error('Ошибка при получении расходов:', error);
    }
  };

  const handleDelete = async (expenseId) => {
    try {
      await axios.delete(`http://127.0.0.1:8081/finances/remove_expense/${expenseId}`);
      setExpenses(expenses.filter(expense => expense.id !== expenseId));
    } catch (error) {
      console.error('Ошибка при удалении расхода:', error);
    }
  };

  const handleEdit = (expenseId) => {
    navigate(`/edit-expense/${expenseId}`);
  };

  return (
    <Container>
      <h1>Мои расходы</h1>
      <ExpenseList>
        {expenses.map(expense => (
          <ExpenseItem key={expense.id}>
            <div>
              <strong>Сумма:</strong> {expense.amount} | <strong>Категория:</strong> {expense.category} | <strong>Источник:</strong> {expense.source}
            </div>
            <div>
              <EditButton onClick={() => handleEdit(expense.id)}>Изменить</EditButton>
              <DeleteButton onClick={() => handleDelete(expense.id)}>Удалить</DeleteButton>
            </div>
          </ExpenseItem>
        ))}
      </ExpenseList>
    </Container>
  );
};

export default ManageExpenses;