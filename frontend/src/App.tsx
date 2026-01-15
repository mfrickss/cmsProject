import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard"; // <--- Certifique-se que criou esse arquivo (mesmo vazio)

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        {/* Quando a URL for apenas '/', mostre o Login */}
        <Route path="/" element={<Login />} />
        
        {/* Quando a URL for '/dashboard', mostre o Dashboard */}
        <Route path="/dashboard" element={<Dashboard />} />
      </Routes>
    </BrowserRouter>
  );
}