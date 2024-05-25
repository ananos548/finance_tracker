import React, { useState } from 'react';
import axios from 'axios';
import styled, { createGlobalStyle } from 'styled-components';

const GlobalStyle = createGlobalStyle`
  html, body {
    margin: 0;
    padding: 0;
    background-color: #fff; /* Установите цвет фона на белый */
    height: 100%;
  }
`;

const Container = styled.div`
  margin: 0 auto;
  padding: 20px;
  background-color: #fff;
  display: flex;
  flex-direction: column;
  align-items: center;
  color: black;
  height: 100%;
`;

const LoginForm = styled.form`
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

const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

axios.defaults.withCredentials = true;

const handleSubmit = async (event) => {
  event.preventDefault();
  try {
    const response = await axios.post('http://127.0.0.1:8081/auth/login', new URLSearchParams({ username, password }), {
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
      }
    });

    // Кука с токеном установлена автоматически благодаря withCredentials


  } catch (error) {
    console.error('Ошибка при попытке входа:', error);
  }
};

  return (
    <>
      <GlobalStyle />
      <Container>
        <h1>Авторизация</h1>
        <LoginForm onSubmit={handleSubmit}>
          <Input
            type="text"
            placeholder="Имя пользователя"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
          <Input
            type="password"
            placeholder="Пароль"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
          <Button type="submit">Войти</Button>
        </LoginForm>
      </Container>
    </>
  );
};

export default Login;