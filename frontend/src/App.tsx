import React, { useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Layout from './components/Layout';
import Shop from './pages/Shop';
import Roulette from './pages/Roulette';
import Profile from './pages/Profile';

declare global {
  interface Window {
    Telegram: {
      WebApp: {
        ready: () => void;
        expand: () => void;
        MainButton: {
          text: string;
          show: () => void;
          hide: () => void;
          onClick: (callback: () => void) => void;
        };
      };
    };
  }
}

function App() {
  useEffect(() => {
    // Initialize Telegram WebApp
    window.Telegram.WebApp.ready();
    window.Telegram.WebApp.expand();
  }, []);

  return (
    <Router>
      <Layout>
        <Routes>
          <Route path="/" element={<Shop />} />
          <Route path="/roulette" element={<Roulette />} />
          <Route path="/profile" element={<Profile />} />
        </Routes>
      </Layout>
    </Router>
  );
}

export default App; 