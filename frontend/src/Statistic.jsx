import React, { useState } from 'react';
import axios from 'axios';
import styled from 'styled-components';

const StatisticContainer = styled.div`
  margin: 20px 0;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
  width: 80%;
  max-width: 600px;
`;

const StatisticTitle = styled.h2`
  font-size: 1.5em;
  margin-bottom: 20px;
`;

const StatisticItem = styled.div`
  margin-bottom: 10px;
`;

const StatisticForm = styled.form`
  display: flex;
  justify-content: space-between;
  margin-bottom: 20px;
`;

const Input = styled.input`
  padding: 5px;
  width: 45%;
`;

const Button = styled.button`
  padding: 5px 10px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
`;

const Statistic = () => {
  const [statistics, setStatistics] = useState(null);
  const [month, setMonth] = useState('');
  const [year, setYear] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.get('http://127.0.0.1:8001/finances/statistic', {
        params: new URLSearchParams({ month, year }),
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded'
        },
        withCredentials: true,
      });

      if (response.data && typeof response.data === 'object') {
        setStatistics(response.data);
      } else {
        console.error('Неверный формат данных:', response.data);
      }
    } catch (error) {
      console.error('Ошибка при получении статистики:', error);
    }
  };

  return (
    <StatisticContainer>
      <StatisticTitle>Статистика расходов</StatisticTitle>
      <StatisticForm onSubmit={handleSubmit}>
        <Input
          type="number"
          placeholder="Месяц (1-12)"
          value={month}
          onChange={(e) => setMonth(e.target.value)}
        />
        <Input
          type="number"
          placeholder="Год (например, 2024)"
          value={year}
          onChange={(e) => setYear(e.target.value)}
        />
        <Button type="submit">Получить статистику</Button>
      </StatisticForm>
      {statistics ? (
        <div>
          {statistics["Сумма расходов за месяц"] !== undefined && (
            <StatisticItem>
              <strong>Сумма расходов за месяц:</strong> {statistics["Сумма расходов за месяц"]}
            </StatisticItem>
          )}
          {statistics["Статистика по категориям"] && typeof statistics["Статистика по категориям"] === 'object' && (
            <>
              <StatisticItem><strong>Статистика по категориям:</strong></StatisticItem>
              <ul>
                {Object.entries(statistics["Статистика по категориям"]).map(([category, amount]) => (
                  <li key={category}>{category}: {amount}</li>
                ))}
              </ul>
            </>
          )}
          {statistics["Самые большие траты в: "] !== undefined && (
            <StatisticItem>
              <strong>Самые большие траты:</strong> {statistics["Самые большие траты в: "]}
            </StatisticItem>
          )}
          {Object.keys(statistics).length === 0 && (
            <p>Данные не найдены.</p>
          )}
        </div>
      ) : (
        <p>Введите месяц и год, чтобы увидеть статистику.</p>
      )}
    </StatisticContainer>
  );
};

export default Statistic;