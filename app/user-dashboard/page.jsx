"use client";
import { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';
import Navbar from '../components/Navbar';
import Sidebar from '../components/userSidebar'; // Import Sidebar component
import { FaClipboardList, FaEdit, FaImage, FaSignOutAlt } from 'react-icons/fa';
import AnimatedGrating from '../components/AnimatedGrating';
import AsmrShapes from '../components/AsmrShapes';

export default function UserDashboard() {
  const router = useRouter();
  
  // Retrieve language from localStorage or default to 'en'
  const storedLanguage = typeof window !== "undefined" ? localStorage.getItem('language') : 'en';
  const [language, setLanguage] = useState(storedLanguage || 'en'); 

  // Translations for different languages
  const translations = {
    en: {
      dashboardTitle: 'Your User Dashboard',
      welcomeMessage: 'Welcome to Aesthetix!',
      description: 'This is a sample user page. Features to be added.',
      imageAlt: 'Dashboard Preview',
      editSurveyButton: 'Edit Survey Info',
      rateImagesButton: 'Rate Images',
      exitButton: 'Logout',
    },
    fr: {
      dashboardTitle: 'Votre Tableau de Bord Utilisateur',
      welcomeMessage: 'Bienvenue sur Aesthetix!',
      description: 'Ceci est une page utilisateur d\'exemple. Fonctionnalités à ajouter.',
      imageAlt: 'Aperçu du Tableau de Bord',
      editSurveyButton: 'Modifier les Infos de l\'Enquête',
      rateImagesButton: 'Noter les Images',
      exitButton: 'Quitter',
    },
  };

  const content = translations[language];

  // Save language choice to localStorage
  const handleLanguageChange = (lang) => {
    setLanguage(lang);
    if (typeof window !== "undefined") {
      localStorage.setItem('language', lang); // Store in localStorage
    }
  };

  // Handle edit survey click
  const handleEditSurveyClick = () => {
    router.push("/edit-survey");
  };

  // Handle rate images click
  const handleRateImagesClick = () => {
    router.push("/rate-images");
  };

  // Handle exit button click
  const handleExitClick = () => {
    router.push("/");
  };

  useEffect(() => {
    // When the page loads, we check if the language is stored in localStorage
    const storedLanguage = localStorage.getItem('language');
    if (storedLanguage) {
      setLanguage(storedLanguage); // If found, set the language
    }
  }, []);

  return (
    <div className="min-h-screen flex relative overflow-hidden bg-gradient-to-br from-fuchsia-200 via-violet-300 to-cyan-300">
      <AnimatedGrating />
      <AsmrShapes />
      
      {/* Sidebar */}

      <div className="relative z-10">
        <Sidebar language={language} />
      </div>
      <div className="flex-1 relative z-10">
        {/* Navbar with language toggle */}
        <Navbar language={language} onLanguageChange={handleLanguageChange} />

        {/* Main Content */}
        <main className="flex-1 p-8">
        <div className="p-6 mb-8 bg-white/80 backdrop-blur-sm rounded-lg">
            <h2 className="text-4xl font-bold text-black">{content.dashboardTitle}</h2>
            <h3 className="text-2xl font-semibold mt-2 text-black">{content.welcomeMessage}</h3>
          </div>
          
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 p-6">
            {/* Edit Survey Card */}
            <div 
              onClick={handleEditSurveyClick}
              className="bg-white/80 backdrop-blur-sm p-6 rounded-lg shadow-lg hover:shadow-xl transition-all duration-300 cursor-pointer transform hover:scale-105"
            >
              <FaEdit className="text-4xl mb-4 text-indigo-600" />
              <h3 className="text-xl font-semibold text-black mb-2">{content.editSurveyButton}</h3>
              <p className="text-black/70">Update your survey information and preferences.</p>
            </div>

            {/* Rate Images Card */}
            <div 
              onClick={handleRateImagesClick}
              className="bg-white/80 backdrop-blur-sm p-6 rounded-lg shadow-lg hover:shadow-xl transition-all duration-300 cursor-pointer transform hover:scale-105"
            >
              <FaImage className="text-4xl mb-4 text-indigo-600" />
              <h3 className="text-xl font-semibold text-black mb-2">{content.rateImagesButton}</h3>
              <p className="text-black/70">Rate images and help improve our algorithm.</p>
            </div>

            {/* Exit Card */}
            <div 
              onClick={handleExitClick}
              className="bg-white/80 backdrop-blur-sm p-6 rounded-lg shadow-lg hover:shadow-xl transition-all duration-300 cursor-pointer transform hover:scale-105"
            >
              <FaSignOutAlt className="text-4xl mb-4 text-indigo-600" />
              <h3 className="text-xl font-semibold text-black mb-2">{content.exitButton}</h3>
              <p className="text-black/70">Logout and return to the homepage.</p>
            </div>
          </div>
        </main>
      </div>
    </div>
  );
}