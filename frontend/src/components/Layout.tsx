import React, { ReactNode } from 'react';
import { Link, useLocation } from 'react-router-dom';
import { ShoppingCartIcon } from '@heroicons/react/24/outline';

interface LayoutProps {
  children: ReactNode;
}

export default function Layout({ children }: LayoutProps) {
  const location = useLocation();

  return (
    <div className="min-h-screen bg-gray-900 text-white">
      {/* Header */}
      <header className="fixed top-0 left-0 right-0 bg-gray-800 shadow-lg z-10">
        <div className="container mx-auto px-4 py-3 flex justify-between items-center">
          <div className="flex items-center space-x-4">
            <img
              src="https://via.placeholder.com/40"
              alt="Avatar"
              className="w-10 h-10 rounded-full"
            />
            <h1 className="text-xl font-bold">Store</h1>
          </div>
          <button className="relative">
            <ShoppingCartIcon className="h-6 w-6" />
            <span className="absolute -top-1 -right-1 bg-red-500 text-white text-xs rounded-full h-4 w-4 flex items-center justify-center">
              0
            </span>
          </button>
        </div>
      </header>

      {/* Main Content */}
      <main className="container mx-auto px-4 pt-20 pb-20">
        {children}
      </main>

      {/* Navigation */}
      <nav className="fixed bottom-0 left-0 right-0 bg-gray-800 shadow-lg">
        <div className="container mx-auto px-4 py-3">
          <div className="flex justify-around">
            <Link
              to="/"
              className={`flex flex-col items-center ${
                location.pathname === '/' ? 'text-blue-500' : 'text-gray-400'
              }`}
            >
              <span className="text-sm">Магазин</span>
            </Link>
            <Link
              to="/roulette"
              className={`flex flex-col items-center ${
                location.pathname === '/roulette' ? 'text-blue-500' : 'text-gray-400'
              }`}
            >
              <span className="text-sm">Рулетка</span>
            </Link>
            <Link
              to="/profile"
              className={`flex flex-col items-center ${
                location.pathname === '/profile' ? 'text-blue-500' : 'text-gray-400'
              }`}
            >
              <span className="text-sm">Профиль</span>
            </Link>
          </div>
        </div>
      </nav>
    </div>
  );
} 