"use client";
import { useRouter } from 'next/navigation';
import { useState, useEffect } from 'react';
import Navbar from '../components/Navbar';
import Sidebar from '../components/adminSidebar'; // Import Sidebar component
import { FaClipboardList, FaImages, FaFileExport } from "react-icons/fa";
import Cookies from 'js-cookie';

export default function AdminDashboard() {
  const [isAdmin, setIsAdmin] = useState(true); // Assume admin is logged in
  const [language, setLanguage] = useState('en'); // Language state
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
      dashboardTitle: 'Your Admin Dashboard',
      welcomeMessage: 'Welcome to Aesthetix!',
      description: 'This is a sample admin page. Features to be added.',
      surveyButton: 'View Survey Data',
      exportButton: 'View and Export Rating Data',
      viewImagesButton: 'View Images',
    },
    fr: {
      dashboardTitle: 'Votre Tableau de Bord Admin',
      welcomeMessage: 'Bienvenue sur Aesthetix!',
      description: 'Ceci est une page d’administration d’exemple. Fonctionnalités à ajouter.',
      surveyButton: 'Voir les données de l’enquête',
      exportButton: 'Voir et Exporter les Données de Notation',
      viewImagesButton: 'Voir les Images',
    },
  };

  const content = translations[language];

  const handleSignOut = () => {
    setIsAdmin(false);
     // Remove admin authentication token
    Cookies.remove('adminToken');
    router.push("/");
  };

  // Route to survey data page
  const handleSurveyDataClick = () => {
    router.push("/survey-data");
  };

  // Route to images page
  const handleImagesClick = () => {
    router.push("/view-imagesets");
  };

  //Routes to ratings data page
  const handleRatingsDataClick = () => {
    router.push("/ratingdata-page");
  };


  return (
    <div className="min-h-screen flex">
      <Sidebar language={language} />

      <div className="flex-1">
        <Navbar
          isAdmin={isAdmin}
          onSignOut={handleSignOut}
          language={language}
          onLanguageChange={handleLanguageChange}
        />

        <main className="flex-1 p-8">
          <div className="p-6 mb-8 text-black">
            <h2 className="text-4xl font-bold">{content.dashboardTitle}</h2>
            <h3 className="text-2xl font-semibold mt-2">{content.welcomeMessage}</h3>
          </div>

          <div className="p-6">
            <p className="text-lg text-gray-700">{content.description}</p>

            {/* Grid Layout for Admin Actions */}
            <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mt-6">
              
              {/* View Survey Data */}
              <div 
                onClick={handleSurveyDataClick} 
                className="cursor-pointer bg-white shadow-lg p-6 rounded-lg hover:shadow-xl transition border border-gray-200"
              >
                <FaClipboardList className="text-blue-500 text-4xl mb-4" />
                <h3 className="text-lg font-semibold">{content.surveyButton}</h3>
                <p className="text-gray-600 text-sm mt-2">Manage all collected survey responses.</p>
              </div>

              {/* View & Export Ratings Data */}
              <div 
                onClick={handleRatingsDataClick} 
                className="cursor-pointer bg-white shadow-lg p-6 rounded-lg hover:shadow-xl transition border border-gray-200"
              >
                <FaFileExport className="text-green-500 text-4xl mb-4" />
                <h3 className="text-lg font-semibold">{content.exportButton}</h3>
                <p className="text-gray-600 text-sm mt-2">Analyze and export rating data for insights.</p>
              </div>

              {/* View Images */}
              <div 
                onClick={handleImagesClick} 
                className="cursor-pointer bg-white shadow-lg p-6 rounded-lg hover:shadow-xl transition border border-gray-200"
              >
                <FaImages className="text-purple-500 text-4xl mb-4" />
                <h3 className="text-lg font-semibold">{content.viewImagesButton}</h3>
                <p className="text-gray-600 text-sm mt-2">Browse and manage uploaded images.</p>
              </div>

            </div>
          </div>          
        </main>
      </div>
    </div>
  );
}