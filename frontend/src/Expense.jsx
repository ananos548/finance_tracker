import React, { useEffect, useState } from 'react';
import axios from 'axios';
import styled from 'styled-components';
import { PieChart, Pie, Tooltip, Legend } from 'recharts';
import { Link } from 'react-router-dom';
import Login from './Login';
import Statistics from './Statistic'; // Импортируем компонент Statistics

const Container = styled.div`
  margin: 0 auto;
  padding: 20px;
  background-color: #fff;
  display: flex;
  flex-direction: column;
  align-items: center;
  color: black;
  position: relative;
`;

const UserInfo = styled.div`
  position: absolute;
  top: 20px;
  right: 20px;
  background-color: #f8f9fa;
  padding: 10px;
  border-radius: 5px;
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
  align-items: center;
`;

const LogoutButton = styled.button`
  margin-top: 10px;
  padding: 5px 10px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
`;

const ExpenseCard = styled.div`
  padding: 20px;
  margin-bottom: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
  width: 80%;
  max-width: 400px;
`;

const ManageLink = styled(Link)`
  margin-top: 20px;
  padding: 10px 15px;
  background-color: #28a745;
  color: white;
  text-decoration: none;
  border-radius: 4px;
  &:hover {
    background-color: #218838;
  }
`;

const Expenses = () => {
  const [expenses, setExpenses] = useState([]);
  const [loading, setLoading] = useState(true);
  const [user, setUser] = useState(null);

  useEffect(() => {
    fetchUser();
    fetchExpenses();
  }, []);

  axios.defaults.withCredentials = true;
  axios.defaults.baseURL = 'http://127.0.0.1:8081';

  const fetchUser = async () => {
    try {
      const response = await axios.get('/auth/current_user');
      setUser(response.data);
    } catch (error) {
      console.error('Ошибка при получении информации о пользователе:', error);
    }
  };

  const fetchExpenses = async () => {
    try {
      const response = await axios.get('/finances/get_my_expenses');
      setExpenses(response.data);
    } catch (error) {
      if (error.response && error.response.status === 401) {
        console.error('Пользователь не авторизован:', error);
      } else {
        console.error('Ошибка при получении расходов:', error);
      }
    } finally {
      setLoading(false);
    }
  };

  const handleLogout = async () => {
    try {
      await axios.post('/auth/logout');
      setUser(null);
      window.location.reload();
    } catch (error) {
      console.error('Ошибка при выходе из системы:', error);
    }
  };

  const calculateCategoryTotal = () => {
    const categoryTotal = {};
    expenses.forEach(expense => {
      if (categoryTotal[expense.category]) {
        categoryTotal[expense.category] += expense.amount;
      } else {
        categoryTotal[expense.category] = expense.amount;
      }
    });
    return categoryTotal;
  };

  const totalExpenses = expenses.reduce((acc, expense) => acc + expense.amount, 0);
  const categoryTotal = calculateCategoryTotal();

  return (
    <Container>
      {user ? (
        <UserInfo>
          <div>Пользователь: {user.username}</div>
          <LogoutButton onClick={handleLogout}>Выход</LogoutButton>
        </UserInfo>
      ) : (
        <Login />
      )}
      <Statistics /> {/* Добавляем компонент Statistics здесь */}
      <h1 style={{ fontSize: '2.5em' }}>Расходы</h1>
      <PieChart width={600} height={400}>
        <Pie
          dataKey="value"
          data={Object.entries(categoryTotal).map(([category, amount]) => ({ name: category, value: amount }))}
          cx={300}
          cy={200}
          outerRadius={120}
          fill="#8884d8"
          label
        />
        <Tooltip />
        <Legend />
      </PieChart>
      {loading ? (
        <p>Загрузка...</p>
      ) : (
        expenses.map((expense, index) => (
          <ExpenseCard key={index}>
            <div><strong>Источник:</strong> {expense.source}</div>
            <div><strong>Сумма:</strong> {expense.amount}</div>
            <div><strong>Категория:</strong> {expense.category}</div>
          </ExpenseCard>
        ))
      )}
      <ManageLink to="/manage-expenses">Управление расходами</ManageLink>
    </Container>
  );
};

export default Expenses;
