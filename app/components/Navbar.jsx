import Link from 'next/link';
import { useState } from 'react';

export default function Navbar({ isAdmin, onSignOut, language, onLanguageChange }) {
  return (
    <nav className="bg-gray-900 p-4 shadow-md relative z-50">
      <div className="container mx-auto flex justify-between items-center">
        {/* Logo or Site Name */}
        
          <button className="text-white text-2xl font-semibold bg-transparent border-none cursor-default">
            Image Aesthetics
          </button>

        {/* Language Toggle */}
        <div className="flex space-x-4 items-center">
          <button
            onClick={() => onLanguageChange('en')}
            className={`py-1 px-3 rounded ${
              language === 'en' ? 'bg-blue-500 text-white' : 'text-gray-300 hover:bg-gray-600'
            }`}
          >
            EN
          </button>
          <button
            onClick={() => onLanguageChange('fr')}
            className={`py-1 px-3 rounded ${
              language === 'fr' ? 'bg-green-500 text-white' : 'text-gray-300 hover:bg-gray-600'
            }`}
          >
            FR
          </button>

          {/* Admin or Login Button */}
          {isAdmin ? (
            <button
              data-testid="signOutButton"
              onClick={onSignOut}
              className="text-white bg-gray-800 px-4 py-2 rounded hover:bg-gray-500"
            >
              Sign Out
            </button>
          ) : (
            <Link href="/admin-login">
              <button
                data-testid="NavLoginButton"
                className="text-white bg-gray-800 px-4 py-2 rounded hover:bg-gray-500"
              >
                Admin Login
              </button>
            </Link>
          )}
        </div>
      </div>
    </nav>
  );
}
