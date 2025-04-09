"use client";

import { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';
import { Button } from "../components/button";
import Navbar from '../components/Navbar';
import Cookies from 'js-cookie';

export default function AdminLogin() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [language, setLanguage] = useState('en'); // State for language
  const router = useRouter();

  // Load language preference from localStorage on initial render
  useEffect(() => {
    const savedLanguage = localStorage.getItem('language');
    if (savedLanguage) {
      setLanguage(savedLanguage);
    }
  }, []);

  // Update localStorage whenever the language changes
  const handleLanguageChange = (lang) => {
    setLanguage(lang);
    localStorage.setItem('language', lang);
  };

  // Translations for different languages
  const translations = {
    en: {
      loginTitle: 'Admin Login',
      username: 'Username',
      password: 'Password',
      errorMessage: 'Invalid credentials. Please try again.',
      loginButton: 'Login',
    },
    fr: {
      loginTitle: 'Connexion Admin',
      username: "Nom d'utilisateur",
      password: 'Mot de passe',
      errorMessage: 'Identifiants invalides. Veuillez réessayer.',
      loginButton: 'Connexion',
    },
  };

  const content = translations[language];

  const handleLogin = async (e) => {
    e.preventDefault();
    setError(''); // Clear previous error messages
  
    try {
      const response = await fetch("http://localhost:5000/api/admin-login", {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
      });
  
      const data = await response.json(); // Parse response JSON
      console.log("Login Response:", data); // Debug response
  
      if (response.ok) {
        // Store admin token in cookies
        document.cookie = `adminToken=${data.token}; path=/; Secure; SameSite=Strict`;
  
        // Redirect to admin dashboard
        router.push('/admin-dashboard');
      } else {
        setError(data.error || content.errorMessage);
      }
    } catch (err) {
      console.error("Login Error:", err);
      setError(content.errorMessage);
    }
  };
  

  return (
    <div className="min-h-screen bg-gradient-to-b from-gray-500 via-gray-300 to-gray-100 pb-10">
      {/* Pass language state to Navbar */}
      <Navbar language={language} onLanguageChange={handleLanguageChange} />
      <div className="min-h-screen flex justify-center items-center">
        <div className="bg-white p-8 rounded shadow-md w-96">
          <h2 className="text-2xl text-black font-semibold text-center mb-6">
            {content.loginTitle}
          </h2>
          <form onSubmit={handleLogin} className="space-y-4">
            <div>
              <label htmlFor="username" className="block text-gray-700">
                {content.username}
              </label>
              <input
                id="username"
                type="text"
                className="w-full p-2 border border-gray-300 rounded"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
              />
            </div>
            <div>
              <label htmlFor="password" className="block text-gray-700">
                {content.password}
              </label>
              <input
                id="password"
                type="password"
                className="w-full p-2 border border-gray-300 rounded"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
              />
            </div>
            {error && <p className="text-red-500 text-sm">{error}</p>}
            <div className="flex justify-center">
              <Button
                data-testid="loginButton"
                variant="outline"
                type="submit"
                className="w-auto justify-center text-black py-2 rounded hover:bg-gray-400"
              >
                {content.loginButton}
              </Button>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
}