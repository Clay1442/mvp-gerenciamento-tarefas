import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { register } from '../services/authService';
import './Register.css';

export const Register: React.FC = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    try {
      await register({ email, password });
      alert('Cadastro realizado com sucesso! Faça seu login.');
      navigate('/'); // Vai para a tela de login
    } catch (error) {
      alert('Erro ao cadastrar. O e-mail pode já estar em uso.');
    }
  }

  return (
    <div className="register-container">
      <form onSubmit={handleSubmit} className="register-form">
        <h2>Criar Conta</h2>
        <input 
          type="email" 
          placeholder="Escolha um e-mail" 
          value={email}
          onChange={e => setEmail(e.target.value)}
          className="register-input"
          required
        />
        <input 
          type="password" 
          placeholder="Crie uma senha" 
          value={password}
          onChange={e => setPassword(e.target.value)}
          className="register-input"
          required
        />
        <button type="submit" className="register-button">Cadastrar</button>
        <p>Já tem conta? <Link to="/">Voltar ao Login</Link></p>
      </form>
    </div>
  );
};
