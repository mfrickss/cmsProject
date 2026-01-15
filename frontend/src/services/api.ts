import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000', // O endereço do teu backend Docker
});

// Isso aqui é um "Interceptor": Toda vez que sair uma requisição,
// ele verifica se tem token salvo e anexa automaticamente.
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export default api;