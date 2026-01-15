import React from 'react';

interface LogoProps {
  className?: string;
}

export default function Logo({ className = "w-12 h-12" }: LogoProps) {
  return (
    <svg 
      viewBox="0 0 100 100" 
      fill="none" 
      xmlns="http://www.w3.org/2000/svg" 
      className={className}
    >
      {/* Fundo: Hexágono Tecnológico (Hollow Knight Vibe) */}
      <path 
        d="M50 5 L93.3 30 V80 L50 105 L6.7 80 V30 Z" 
        className="fill-gray-900 stroke-blue-500 stroke-2"
      />
      
      {/* Olhos: Fusão Spidey (Forma) + Tech (Cor) */}
      <path 
        d="M35 45 C35 45 25 35 20 50 C15 65 25 70 35 70 C45 70 40 55 35 45 Z" 
        className="fill-white"
      />
      <path 
        d="M65 45 C65 45 75 35 80 50 C85 65 75 70 65 70 C55 70 60 55 65 45 Z" 
        className="fill-white"
      />

      {/* A "Cortada" / Glitch (Vôlei + Futurismo) */}
      <path 
        d="M10 60 L90 40" 
        className="stroke-cyan-400 stroke-[4] opacity-80"
        strokeLinecap="round"
      />
      
      {/* Detalhe da Teia/Conexão (Sutil no topo) */}
      <circle cx="50" cy="25" r="5" className="fill-blue-500 animate-pulse" />
    </svg>
  );
}