import { useState } from 'react';
import api from '../services/api';
import { useNavigate } from 'react-router-dom';
// Importe o useNavigate do react-router-dom se quiser redirecionar depois (opcional agora)

export default function Login() {
  // Estados para guardar o que o usuário digita
  const navigate = useNavigate();
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  async function handleLogin(e: React.FormEvent) {
    e.preventDefault(); // Evita que a página recarregue
    setError('');

    try {

      // TODO 1: Crie um objeto FormData
      // O FastAPI exige que os campos sejam 'username' (para o email) e 'password'
      const dados = new FormData(); 
      dados.append('username', email); 
      dados.append('password', password); 
    
      // TODO 2: Faça o POST para '/auth/token' enviando esse formData
      const response = await api.post('api/v1/auth/token', dados)
      
      // TODO 3: Se der certo, pegue o 'access_token' da resposta e salve no localStorage

      const token = response.data.access_token;

      localStorage.setItem('token', token)
        
      navigate('/dashboard');
      
    } catch (err) {
      setError('Erro ao logar. Verifique os dados.');
      console.error(err);
    }
  }

  return (
    <div className="flex min-h-screen items-center justify-center bg-gray-900 text-white">
      <div className="w-full max-w-md space-y-8 rounded-xl bg-gray-800 p-10 shadow-2xl">
        <h2 className="text-center text-3xl font-bold text-blue-500">Login</h2>
        
        {/* Formulário chama a sua função aqui */}
        <form className="mt-8 space-y-6" onSubmit={handleLogin}>
          
          {/* Input de Email */}
          <input
            type="email"
            placeholder="Email"
            required
            className="w-full rounded p-2 bg-gray-700 border border-gray-600 focus:border-blue-500 outline-none"
            value={email}
            onChange={(e) => setEmail(e.target.value)} // Atualiza o estado
          />

          {/* Input de Senha */}
          <input
            type="password"
            placeholder="Senha"
            required
            className="w-full rounded p-2 bg-gray-700 border border-gray-600 focus:border-blue-500 outline-none"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />

          {error && <p className="text-red-500 text-center">{error}</p>}

          <button
            type="submit"
            className="w-full rounded bg-blue-600 p-2 font-bold hover:bg-blue-700 transition"
          >
            Entrar
          </button>
        </form>
      </div>
    </div>
  );
}