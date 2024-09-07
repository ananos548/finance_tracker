import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams, useNavigate } from 'react-router-dom';
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

const Form = styled.form`
  display: flex;
  flex-direction: column;
  width: 100%;
  max-width: 400px;
`;

const Input = styled.input`
  margin-bottom: 10px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;

`;

const Select = styled.select`
  margin-bottom: 10px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 16px;
  appearance: none;
  background-repeat: no-repeat;
  background-position: right 10px center;
  background-size: 12px;
`;

const Option = styled.option`
  background-color: #fff; /* Белый фон для опций */
  color: #333; /* Темный текст для опций */
  padding: 10px;

  &:hover {
    background-color: #f0f0f0; /* Легкий серый фон при наведении */
  }
`;

const Button = styled.button`
  padding: 10px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  margin-top: 10px;

  &:hover {
    background-color: #0056b3;
  }
`;

const EditExpense = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const [amount, setAmount] = useState('');
  const [categoryId, setCategoryId] = useState('');
  const [source, setSource] = useState('');
  const [categories, setCategories] = useState([]);
  const [error, setError] = useState(null);

  axios.defaults.withCredentials = true;
  axios.defaults.baseURL = 'http://127.0.0.1:8081';

  // Функция для загрузки категорий при рендеринге
useEffect(() => {
  const fetchCategories = async () => {
    try {
      const response = await axios.get('finances/get_categories');
      console.log('Категории:', response.data); // Проверь, что категории загружаются
      setCategories(response.data);
    } catch (error) {
      console.error('Ошибка при получении категорий:', error);
      setError('Ошибка при загрузке категорий.');
    }
  };

  fetchCategories();
}, []);

  const handleSave = async (e) => {
    e.preventDefault();
    try {
      await axios.patch(`http://127.0.0.1:8081/finances/edit_expense/${id}`, {
        amount: parseInt(amount, 10),
        category_id: parseInt(categoryId, 10),
        source,
      });
      alert('Расход успешно изменен');
      navigate('/manage-expenses');
    } catch (error) {
      console.error('Ошибка при сохранении изменений:', error);
      setError('Ошибка при сохранении изменений.');
    }
  };

  return (
    <Container>
      <h1>Изменить расход</h1>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <Form onSubmit={handleSave}>
        <Input
          type="number"
          placeholder="Сумма"
          value={amount}
          onChange={(e) => setAmount(e.target.value)}
        />
        <Select
          value={categoryId}
          onChange={(e) => setCategoryId(e.target.value)}
        >
          <option value="">Выберите категорию</option>
          {categories.map((category) => (
            <option key={category.id} value={category.id}>
              {category.title}
            </option>
          ))}
        </Select>
        <Input
          type="text"
          placeholder="Источник"
          value={source}
          onChange={(e) => setSource(e.target.value)}
        />
        <Button type="submit">Сохранить изменения</Button>
      </Form>
    </Container>
  );
};

export default EditExpense;