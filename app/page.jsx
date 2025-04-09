"use client";
import Navbar from './components/Navbar';
import ImageSet from './components/imageSet';
import Typewriter from 'typewriter-effect';
import Link from 'next/link';
import React, { useState, useEffect } from 'react';
import AnimatedGrating from './components/AnimatedGrating';
import AsmrShapes from './components/AsmrShapes';
import Cookies from 'js-cookie';

export default function Page() {
  const [language, setLanguage] = useState('en');

  // Load language from localStorage on initial render
  useEffect(() => {
    const savedLanguage = localStorage.getItem('language');
    if (savedLanguage) {
      setLanguage(savedLanguage);
    }

    // Reset cookie on initial render
    Cookies.remove('isSurveyCompleted');
  }, []);

  // Update localStorage whenever the language changes
  const handleLanguageChange = (lang) => {
    setLanguage(lang);
    localStorage.setItem('language', lang);
  };

  const translations = {
    en: {
      welcome: 'Welcome to Image Aesthetics',
      description: 'Help us discover the most aesthetically pleasing images',
      survey: 'Take Survey',
      survey_instructions: 'Your ratings will help us improve our image selection algorithm. In order to start, fill out the survey below.',
      post_survey_redirect: 'After taking this survey, you will be redirected to the user dashboard'
    },
    fr: {
      welcome: "Bienvenue à l'esthétique de l'image",
      description: 'Aidez-nous à découvrir les images les plus esthétiques',
      survey: "Participer à l'enquête",
      survey_instructions: "Vos évaluations nous aideront à améliorer notre algorithme de sélection d'images. Pour commencer, remplissez le questionnaire ci-dessous.",
      post_survey_redirect: 'Après avoir répondu à cette enquête, vous serez redirigé vers le tableau de bord utilisateur.'
    }
  };

  const content = translations[language];

  return (
    <div className="min-h-screen relative overflow-hidden bg-gradient-to-br from-fuchsia-200 via-violet-300 to-cyan-300">
      <AnimatedGrating />
      <AsmrShapes />
      <Navbar language={language} onLanguageChange={handleLanguageChange} />
      <div className="container mx-auto py-20 px-4 text-center relative z-10">
        <h1 className="text-4xl md:text-6xl font-extrabold mb-8 text-black">
          <Typewriter
            options={{
              strings: [content.welcome],
              autoStart: true,
              loop: true,
              delay: 75,
            }}
          />
        </h1>
        <p className="text-lg md:text-2xl mb-6 text-black font-semibold">
          {content.description}
        </p>
        <p className="text-sm md:text-lg mb-12 text-black">
          {content.survey_instructions}
        </p>
        <Link href="/consent-form">
          <button className="bg-indigo-600 hover:bg-gradient-to-r hover:from-purple-500 hover:to-pink-500 transition-all duration-300 text-white py-3 px-6 rounded-lg shadow-lg transform hover:scale-105 hover:shadow-xl hover:shadow-indigo-200/50">
            {content.survey}
          </button>
        </Link>
        <p className="text-sm md:text-base mt-6 text-black">
          
        </p>
      </div>
    </div>
  );
}
