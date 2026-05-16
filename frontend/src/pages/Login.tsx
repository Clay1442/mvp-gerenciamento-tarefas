import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';
import './Login.css'; 

export const Login: React.FC = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const { signIn } = useAuth();
  const navigate = useNavigate();

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    try {
      await signIn({ email, password });
      navigate('/board'); // Redireciona após o login
    } catch (error) {
      alert('E-mail ou senha incorretos!');
    }
  }

  return (
    <div className="login-container">
      <form onSubmit={handleSubmit} className="login-form">
        <h2>Login </h2>
        <input 
          type="email" 
          placeholder="Seu e-mail" 
          value={email}
          onChange={e => setEmail(e.target.value)}
          className="login-input"
          required
        />
        <input 
          type="password" 
          placeholder="Sua senha" 
          value={password}
          onChange={e => setPassword(e.target.value)}
          className="login-input"
          required
        />
        <button type="submit" className="login-button">Entrar</button>
        <p>Não tem conta? <Link to="/register">Cadastre-se</Link></p>
      </form>
    </div>
  );
};
