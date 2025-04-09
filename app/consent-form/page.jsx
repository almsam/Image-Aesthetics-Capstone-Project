"use client";
import { useRouter } from "next/navigation";
import Navbar from "../components/Navbar";
import React, { useState, useEffect } from "react";
import AnimatedGrating from "../components/AnimatedGrating";
import AsmrShapes from "../components/AsmrShapes";

export default function ConsentPage() {
  const [language, setLanguage] = useState("en");
  const router = useRouter(); // Initialize router for navigation

  // Load language from localStorage on initial render
  useEffect(() => {
    const savedLanguage = localStorage.getItem("language");
    if (savedLanguage) {
      setLanguage(savedLanguage);
    }
  }, []);

  const translations = {
    en: {
      title: "Consent Form",
      description:
        "Before proceeding with the survey, please read and agree to the consent form.",
      download: "Download Consent Form",
      consent: "I Consent",
      noConsent: "I Do Not Consent",
      redirectSurvey: "Redirecting to the survey...",
      redirectHome: "Redirecting to the homepage...",
    },
    fr: {
      title: "Formulaire de Consentement",
      description:
        "Avant de poursuivre l'enquête, veuillez lire et accepter le formulaire de consentement.",
      download: "Télécharger le formulaire de consentement",
      consent: "Je consens",
      noConsent: "Je ne consens pas",
      redirectSurvey: "Redirection vers l'enquête...",
      redirectHome: "Redirection vers la page d'accueil...",
    },
  };

  const content = translations[language];

  // Function to handle consent and navigate to the survey
  const handleConsent = () => {
    alert(content.redirectSurvey); // Optional alert to confirm consent
    router.push("/survey"); // Redirect to survey page
  };

  // Function to handle denial and navigate to homepage
  const handleNoConsent = () => {
    alert(content.redirectHome); // Optional alert to confirm rejection
    router.push("/"); // Redirect to homepage
  };

  return (
    <div className="min-h-screen relative overflow-hidden bg-gradient-to-br from-fuchsia-200 via-violet-300 to-cyan-300">
      <AnimatedGrating />
      <AsmrShapes />
      <Navbar language={language} onLanguageChange={setLanguage} />
      <div className="container mx-auto py-20 px-4 text-center relative z-10">
        <h1 className="text-4xl md:text-5xl font-extrabold mb-6 text-black">
          {content.title}
        </h1>
        <p className="text-lg md:text-xl mb-4 text-black">{content.description}</p>
        
        {/* Download Consent Form */}
        <a
          href="/sample_consentform.pdf"
          download="consent-form.pdf"
          className="bg-indigo-600 hover:bg-gradient-to-r hover:from-purple-500 hover:to-pink-500 transition-all duration-300 text-white py-3 px-6 rounded-lg shadow-lg mb-6 inline-block transform hover:scale-105 hover:shadow-xl hover:shadow-indigo-200/50"
        >
          {content.download}
        </a>

        <div className="mt-8 flex justify-center space-x-6">
          {/* I Consent Button */}
          <button
            onClick={handleConsent}
            className="bg-indigo-600 hover:bg-gradient-to-r hover:from-purple-500 hover:to-pink-500 transition-all duration-300 text-white py-3 px-6 rounded-lg shadow-lg transform hover:scale-105 hover:shadow-xl hover:shadow-indigo-200/50"
          >
            {content.consent}
          </button>

          {/* I Do Not Consent Button */}
          <button
            onClick={handleNoConsent}
            className="bg-red-600 hover:bg-gradient-to-r hover:from-red-500 hover:to-pink-500 transition-all duration-300 text-white py-3 px-6 rounded-lg shadow-lg transform hover:scale-105 hover:shadow-xl hover:shadow-red-200/50"
          >
            {content.noConsent}
          </button>
        </div>
      </div>
    </div>
  );
}
