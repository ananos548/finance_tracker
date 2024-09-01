import React, { useState, useEffect } from 'react';
import axios from 'axios';
import styled, { createGlobalStyle } from 'styled-components';
import { Link } from 'react-router-dom'; // Импортируем компонент Link из react-router-dom

const GlobalStyle = createGlobalStyle`
  html, body {
    margin: 0;
    padding: 0;
    background-color: #fff;
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

const LinkButton = styled(Link)`
  color: #007bff;
  text-decoration: none;
  cursor: pointer;
`;

const Login = ({ onLogin }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [loading, setLoading] = useState(true);

  axios.defaults.withCredentials = true;

  useEffect(() => {
    const checkAuthStatus = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8081/auth/current_user');
        if (response.data) {
          setIsAuthenticated(true);
        }
      } catch (error) {
        console.error('Ошибка при проверке авторизации:', error);
      } finally {
        setLoading(false);
      }
    };

    checkAuthStatus();
  }, []);

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post('http://127.0.0.1:8081/auth/login', new URLSearchParams({ username, password }), {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded'
        }
      });

      // Предполагается, что после успешной авторизации сервер вернет информацию о пользователе


      // Перезагрузить страницу после успешного входа
      window.location.reload();

    } catch (error) {
      console.error('Ошибка при попытке входа:', error);
    }
  };

  if (loading) return <p>Загрузка...</p>;

  if (isAuthenticated) {
    return (
      <>
        <GlobalStyle />
        <Container>
          <h1>Вы уже авторизованы</h1>
        </Container>
      </>
    );
  }

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
        {/* Используем компонент Link для создания ссылки */}
        <p>
          <LinkButton to="/registration">Регистрация</LinkButton>
        </p>
      </Container>
    </>
  );
};

export default Login;