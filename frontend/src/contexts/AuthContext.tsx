import { createContext, useContext, useState, useEffect, ReactNode } from 'react';
import { api } from '../services/api';

interface User {
  id: number;
  email: string;
}

interface AuthContextData {
  signed: boolean;
  user: User | null;
  loading: boolean;
  signIn(credentials: object): Promise<void>;
  signOut(): void;
}

const AuthContext = createContext<AuthContextData>({} as AuthContextData);

export function AuthProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Quando o app inicia, checa se já existe um token salvo no navegador
    async function loadStorageData() {
      const storagedToken = localStorage.getItem('@TrelloClone:token');
      
      if (storagedToken) {
        try {
          // Opcional: Você pode criar uma rota GET /auth/me no FastAPI para validar o token e pegar os dados do user
          // Por enquanto, vamos simular mantendo o usuário ativo se houver token
          setUser({ id: 0, email: 'usuario@conectado.com' }); 
        } catch {
          signOut();
        }
      }
      setLoading(false);
    }
    loadStorageData();
  }, []);

  async function signIn(credentials: object) {
    // Envia o e-mail e senha para a rota do seu FastAPI
    const response = await api.post('/auth/login', credentials);
    const { access_token } = response.data;

    // Salva o token no localStorage do navegador do usuário
    localStorage.setItem('@TrelloClone:token', access_token);
    
    setUser({ id: 1, email: 'usuario@conectado.com' }); // Atualiza o estado global
  }

  function signOut() {
    localStorage.removeItem('@TrelloClone:token');
    setUser(null);
  }

  return (
    <AuthContext.Provider value={{ signed: !!user, user, loading, signIn, signOut }}>
      {children}
    </AuthContext.Provider>
  );
}

// Hook customizado para facilitar o uso nas páginas depois
export function useAuth() {
  return useContext(AuthContext);
}