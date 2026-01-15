import { useEffect, useState } from 'react';
import api from '../services/api';
// Importe seu Logo se quiser

// 1. Defina a "cara" dos dados que vêm do backend
interface Post {
    title: string;
    content: string; // ou 'content', confira no seu Swagger como está o nome
    id: number;
    owner_id: number
    owner: {
        email: string,
        name: string,
        age?: number,
        id: number,
        is_active: boolean
    }
}

interface UserProfile {
    email: string,
    name: string,
    age?: number,
    id: number,
    is_active: boolean
}

export default function Dashboard() {
  const [posts, setPosts] = useState<Post[]>([]);
  const [currentUser, setCurrentUser] = useState<UserProfile | null>(null);

  useEffect(() => {
    async function fetchPosts() {
      try {
        // TODO A: Faça a chamada GET para a rota de posts
        // Dica: A rota deve ser '/api/v1/posts/' (ou similar, cheque seu Swagger)
        // const response = await ...

        const response = await api.get('/api/v1/posts')
        
        // TODO A.1: Pegue os dados da resposta e jogue dentro do estado 'posts'
        // Dica: O array de posts costuma vir em response.data
        // setPosts(...)

        setPosts(response.data)

        // TODO B: Faça a chamada para descobrir quem sou eu
        // Dica: A rota geralmente é '/api/v1/users/me'
        // const responseMe = await ...

        const responseMe = await api.get('/api/v1/users/me')
        
        // TODO C: Salve os dados no estado 'currentUser'
        setCurrentUser(responseMe.data)
        
        console.log("Posts carregados!"); // Só pra gente debuggar
        
      } catch (error) {
        console.error("Erro ao buscar posts", error);
        alert("Erro ao carregar dashboard. Veja o console.");
      }
    }

    fetchPosts();
  }, []); // <--- Esse [] vazio diz: "Execute apenas UMA vez, quando nascer"

return (
    // 1. O Palco: Fundo escuro, altura total, texto branco
    <div className="min-h-screen bg-gray-900 text-white p-8">
      
      {/* Cabeçalho */}
      <div className="flex justify-between items-center mb-8 border-b border-gray-700 pb-4">
        <h1 className="text-3xl font-bold text-blue-500">
          NEXUS <span className="text-white text-lg">Dashboard</span>
        </h1>

        {/* TODO D: Mostre o email do usuário aqui */}
        {/* Lembre-se: O currentUser começa como null, então use a interrogação (?) */}
        {/* ou use a lógica: currentUser && <div>...</div> */}
        <div className="text-right">
          <p className="text-sm text-gray-400">Logado como</p>
          <p className="font-bold text-cyan-400">
             {currentUser?.email}
          </p>
        </div>
      </div>
      
      {/* 2. O Grid: Responsivo (1 col celular -> 3 col PC) */}
      <div className="grid gap-6 grid-cols-1 md:grid-cols-2 lg:grid-cols-3">
        
        {/* 3. O Loop: Transforma dados em Cards */}
        {posts.map((post) => (
          <div 
            key={post.id} // RG único do item
            // Classes: Fundo cinza, borda, arredondado.
            // Hover: Borda vira ciano, adiciona sombra neon.
            // Group: Permite que o hover daqui afete os filhos (título)
            className="p-6 bg-gray-800 rounded-xl border border-gray-700 hover:border-cyan-400 transition-all duration-300 hover:shadow-[0_0_15px_rgba(34,211,238,0.2)] group"
          >
            {/* Título: Fica ciano quando a caixa pai (group) sofre hover */}
            <h2 className="text-xl font-bold text-white group-hover:text-cyan-300 mb-2">
              {post.title}
            </h2>
            
            {/* Conteúdo: Limitado a 3 linhas (line-clamp) pra não quebrar o layout */}
            <p className="text-gray-400 text-sm mb-4 line-clamp-3">
              {post.content}
            </p>

            {/* Rodapé do Card: Linha fina em cima e email do dono */}
            <div className="mt-4 pt-4 border-t border-gray-700 flex justify-between items-center text-xs text-gray-500">
              <span>ID: {post.id}</span>
              {/* split('@')[0] pega só o nome antes do arroba */}
              <span className="text-blue-400">@{post.owner.email.split('@')[0]}</span>
            </div>
          </div>
        ))}
      </div>
      
      {/* 6. Condicional: Só aparece se a lista estiver vazia */}
      {posts.length === 0 && (
        <div className="text-center text-gray-500 mt-10">
          Nenhum dado encontrado no sistema. Vá ao Swagger criar posts!
        </div>
      )}
    </div>
  )};