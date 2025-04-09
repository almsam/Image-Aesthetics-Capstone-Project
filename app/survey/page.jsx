"use client";

import React, { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';
import { Button } from "../components/button";
import Navbar from '../components/Navbar';
import AnimatedGrating from '../components/AnimatedGrating';
import AsmrShapes from '../components/AsmrShapes';
import Cookies from 'js-cookie';

export default function Survey() {
  const [age, setAge] = useState('');
  const [gender, setGender] = useState('');
  const [email, setEmail] = useState('');
  const [artsDegree, setArtsDegree] = useState(false);
  const [errorMessage, setErrorMessage] = useState('');
  const [language, setLanguage] = useState('en'); // Initial state set to 'en' or any default
  const router = useRouter();

  // Translations for different languages
  const translations = {
    en: {
      surveyTitle: 'User Survey',
      surveyInstructions: 'Please complete this short survey to help us understand you better.',
      age: 'Age',
      ageHint: 'Must be between 18 and 125 years old.',
      gender: 'Gender',
      email: 'Email',
      artsDegree: 'Have you taken a Visual Arts Course?',
      submitButton: 'Submit',
      ageError: 'You must be between 18 and 125 years old to take this survey.',
      successMessage: 'Survey submitted successfully!',
      failureMessage: 'Failed to submit survey.',
      errorOccured: 'An error occurred while submitting your survey.',
    },
    fr: {
      surveyTitle: 'Enquête Utilisateur',
      surveyInstructions: 'Veuillez compléter ce court questionnaire pour nous aider à mieux vous comprendre.',
      age: 'Âge',
      ageHint: 'Doit avoir entre 18 et 125 ans.',
      gender: 'Genre',
      email: 'Email',
      artsDegree: 'Avez-vous suivi un cours d\'arts visuels?',
      submitButton: 'Soumettre',
      ageError: 'Vous devez avoir entre 18 et 125 ans pour répondre à cette enquête.',
      successMessage: 'Enquête soumise avec succès!',
      failureMessage: 'Échec de la soumission de l\'enquête.',
      errorOccured: 'Une erreur s\'est produite lors de la soumission de votre enquête.',
    },
  };

  const content = translations[language];

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

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Validate age
    if (age < 18 || age > 125) {
      setErrorMessage(age < 18 ? content.ageError : 'Age cannot be more than 125 years.');
      return; // Stop further execution
    }

    // Clear any previous error messages
    setErrorMessage('');

    // Submit the survey data
    try {
      const response = await fetch('http://localhost:5000/api/survey', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ age, gender, email, artsDegree }),
      });

      if (response.ok) {
        Cookies.set('isSurveyCompleted', true, {path: '/'});
        alert(content.successMessage);
        router.push('/user-dashboard');
      } else {
        alert(content.failureMessage);
      }
    } catch (error) {
      console.error('Error submitting survey:', error);
      alert(content.errorOccured);
    }
  };

  return (
    <div className="min-h-screen relative overflow-hidden bg-gradient-to-br from-fuchsia-200 via-violet-300 to-cyan-300">
      <AnimatedGrating />
      <AsmrShapes />
      <Navbar language={language} onLanguageChange={handleLanguageChange} />
      <div className="min-h-screen flex justify-center items-center relative z-10">
        <div className="bg-white/80 backdrop-blur-sm p-8 rounded-lg shadow-lg w-96">
          <h2 className="text-3xl text-black font-bold text-center mb-4">
            {content.surveyTitle}
          </h2>
          <p className="text-center text-black mb-6">
            {content.surveyInstructions}
          </p>
          <form onSubmit={handleSubmit} className="space-y-6">
            {/* Age Field */}
            <div>
              <label className="block text-black font-semibold" htmlFor="age">
                {content.age}
              </label>
              <p className="text-sm text-black/70 mb-1">{content.ageHint}</p>
              <input
                id="age"
                type="number"
                className="w-full p-2 border border-gray-300 rounded focus:border-indigo-500 focus:ring focus:ring-indigo-300 bg-white/90"
                value={age}
                onChange={(e) => setAge(e.target.value)}
                min="0"
                max="125"
                required
              />
            </div>
            {/* Gender Field */}
            <div>
              <label className="block text-black font-semibold" htmlFor="gender">
                {content.gender}
              </label>
              <input
                id="gender"
                type="text"
                className="w-full p-2 border border-gray-300 rounded focus:border-indigo-500 focus:ring focus:ring-indigo-300 bg-white/90"
                value={gender}
                onChange={(e) => setGender(e.target.value)}
                required
              />
            </div>
            {/* Email Field */}
            <div>
              <label className="block text-black font-semibold" htmlFor="email">
                {content.email}
              </label>
              <input
                id="email"
                type="email"
                className="w-full p-2 border border-gray-300 rounded focus:border-indigo-500 focus:ring focus:ring-indigo-300 bg-white/90"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
              />
            </div>
            {/* Arts Degree Field */}
            <div className="flex items-center space-x-2">
              <input
                id="artsDegree"
                type="checkbox"
                className="w-4 h-4 text-indigo-600 border-gray-300 rounded focus:ring-indigo-500"
                checked={artsDegree}
                onChange={(e) => setArtsDegree(e.target.checked)}
              />
              <label className="text-black font-semibold" htmlFor="artsDegree">
                {content.artsDegree}
              </label>
            </div>
            {/* Error Message */}
            {errorMessage && (
              <p className="text-red-600 text-sm text-center">{errorMessage}</p>
            )}
            {/* Submit Button */}
            <div className="flex justify-center">
              <button
                type="submit"
                className="bg-indigo-600 hover:bg-gradient-to-r hover:from-purple-500 hover:to-pink-500 transition-all duration-300 text-white py-3 px-6 rounded-lg shadow-lg transform hover:scale-105 hover:shadow-xl hover:shadow-indigo-200/50"
              >
                {content.submitButton}
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
}
