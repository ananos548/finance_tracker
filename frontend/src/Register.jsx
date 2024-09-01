import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import styled from 'styled-components';

const Container = styled.div`
  margin: 0 auto;
  padding: 20px;
  background-color: white;
  display: flex;
  flex-direction: column;
  align-items: center;
  color: black;
  height: 100vh;
`;

const Form = styled.form`
  display: flex;
  flex-direction: column;
  align-items: center;
`;

const Input = styled.input`
  margin-bottom: 10px;
  padding: 5px;
  width: 200px;
`;

const Button = styled.button`
  padding: 8px 15px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
`;

const Registration = () => {
  const [formData, setFormData] = useState({
    username: '',
    password: '',
    email: '',
  });
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    const checkAuthStatus = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8081/auth/current_user', {
          withCredentials: true // Include credentials for CORS
        });
        if (response.data) {
          // Пользователь авторизован, перенаправляем на главную страницу
          navigate('/get_my_expenses');
        }
      } catch (error) {
        console.error('Ошибка при проверке авторизации:', error);
      }
    };

    checkAuthStatus();
  }, [navigate]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://127.0.0.1:8081/auth/registration',
        formData,
        {
          headers: {
            'Content-Type': 'application/json'
          },
          withCredentials: true // Include credentials for CORS
        }
      );

      if (response.status !== 200) {
        throw new Error('Ошибка регистрации');
      }

      console.log('User ID:', response.data.user_id);
      navigate('/get_my_expenses');
    } catch (error) {
      setError(error.message);
    }
  };

  return (
    <Container>
      <h2>Регистрация</h2>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <Form onSubmit={handleSubmit}>
        <div>
          <label>Имя пользователя:</label>
          <Input type="text" name="username" value={formData.username} onChange={handleChange} required />
        </div>
        <div>
          <label>Пароль:</label>
          <Input type="password" name="password" value={formData.password} onChange={handleChange} required />
        </div>
        <div>
          <label>Email:</label>
          <Input type="email" name="email" value={formData.email} onChange={handleChange} required />
        </div>
        <Button type="submit">Зарегистрироваться</Button>
      </Form>
    </Container>
  );
};

export default Registration;