"use client";

import React, { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';
import { Button } from "../components/button";
import Navbar from '../components/Navbar';
import Sidebar from '../components/userSidebar';
import AnimatedGrating from '../components/AnimatedGrating';
import AsmrShapes from '../components/AsmrShapes';

export default function EditSurvey() {
  const [age, setAge] = useState('');
  const [gender, setGender] = useState('');
  const [artsDegree, setArtsDegree] = useState(false);
  const [errorMessage, setErrorMessage] = useState('');
  const [language, setLanguage] = useState('en'); // State for language
  const router = useRouter();

  // Translations for different languages
  const translations = {
    en: {
      surveyTitle: 'Edit Your Survey Information',
      age: 'Age',
      gender: 'Gender',
      artsDegree: 'Have you taken a Visual Arts Course?',
      submitButton: 'Save Changes',
      ageError: 'You must be at least 18 years old to take this survey.',
      successMessage: 'Survey information updated successfully!',
      errorMessage: 'An error occurred while updating your information.',
    },
    fr: {
      surveyTitle: 'Modifier vos informations d’enquête',
      age: 'Âge',
      gender: 'Genre',
      artsDegree: 'Avez-vous suivi un cours d’arts visuels?',
      submitButton: 'Enregistrer les modifications',
      ageError: 'Vous devez avoir au moins 18 ans pour répondre à cette enquête.',
      successMessage: 'Les informations de l’enquête ont été mises à jour avec succès!',
      errorMessage: 'Une erreur est survenue lors de la mise à jour de vos informations.',
    },
  };

  const content = translations[language];

  // Load language preference from localStorage on component mount
  useEffect(() => {
    const savedLanguage = localStorage.getItem('language');
    if (savedLanguage) {
      setLanguage(savedLanguage);
    }
  }, []);

  // Save language preference to localStorage
  const handleLanguageChange = (lang) => {
    setLanguage(lang);
    localStorage.setItem('language', lang);
  };

  // Fetch user data from the API when component mounts
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('http://localhost:5000/api/survey'); // Replace with your API endpoint
        const data = await response.json();
        setAge(data.age);
        setGender(data.gender);
        setArtsDegree(data.artsDegree);
      } catch (error) {
        console.error("Error fetching survey data:", error);
      }
    };

    fetchData();
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Validate age
    if (age < 18) {
      setErrorMessage(content.ageError);
      return;
    }

    // Clear previous error messages
    setErrorMessage('');

    // Submit updated survey data
    try {
      const response = await fetch('http://localhost:5000/api/survey', {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ age, gender, artsDegree }),
      });

      if (response.ok) {
        alert(content.successMessage);
        router.push('/user-dashboard');
      } else {
        alert(content.errorMessage);
      }
    } catch (error) {
      console.error("Error updating survey data:", error);
      alert(content.errorMessage);
    }
  };

  return (
    <div className="min-h-screen flex relative overflow-hidden bg-gradient-to-br from-fuchsia-200 via-violet-300 to-cyan-300">
      <AnimatedGrating />
      <AsmrShapes />
      
      {/* Sidebar with proper z-index */}
      <div className="relative z-10">
        <Sidebar language={language} onLanguageChange={handleLanguageChange} />
      </div>

      <div className="flex-1 relative z-10">
        <Navbar language={language} onLanguageChange={handleLanguageChange} />
        <div className="flex justify-center items-center min-h-[calc(100vh-4rem)]">
          {/* Survey Form */}
          <div className="bg-white/80 backdrop-blur-sm p-8 rounded-lg shadow-lg w-96">
            <h2 className="text-3xl text-gray-800 font-bold text-center mb-4">
              {content.surveyTitle}
            </h2>
            <form onSubmit={handleSubmit} className="space-y-6">
              {/* Age Field */}
              <div>
                <label className="block text-gray-700 font-semibold" htmlFor="age">
                  {content.age}
                </label>
                <input
                  id="age"
                  type="number"
                  className="w-full p-2 border border-gray-300 rounded focus:border-indigo-500 focus:ring focus:ring-indigo-300"
                  value={age}
                  onChange={(e) => setAge(e.target.value)}
                  min="0"
                  required
                />
              </div>
              {/* Gender Field */}
              <div>
                <label className="block text-gray-700 font-semibold" htmlFor="gender">
                  {content.gender}
                </label>
                <input
                  id="gender"
                  type="text"
                  className="w-full p-2 border border-gray-300 rounded focus:border-indigo-500 focus:ring focus:ring-indigo-300"
                  value={gender}
                  onChange={(e) => setGender(e.target.value)}
                  required
                />
              </div>
              {/* Arts Degree Field */}
              <div className="flex items-center">
                <input
                  id="artsDegree"
                  type="checkbox"
                  className="mr-2 focus:ring-indigo-500"
                  checked={artsDegree}
                  onChange={(e) => setArtsDegree(e.target.checked)}
                />
                <label htmlFor="artsDegree" className="text-gray-700">
                  {content.artsDegree}
                </label>
              </div>
              {/* Submit Button */}
              <div className="flex justify-center">
                <Button
                  type="submit"
                  id="surveyButton"
                  className="bg-blue-500 text-white py-2 px-4 rounded-lg hover:bg-indigo-900 transition duration-300"
                >
                  {content.submitButton}
                </Button>
              </div>
            </form>
            {errorMessage && (
              <p className="text-red-500 text-center mt-4 border border-red-300 bg-red-50 p-2 rounded">
                {errorMessage}
              </p>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}