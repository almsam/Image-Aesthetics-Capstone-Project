"use client";
import { useRouter } from 'next/navigation';
import React, { useState, useEffect } from "react";
import Navbar from "../components/Navbar";
import Sidebar from "../components/adminSidebar"; // Import Sidebar component
import Cookies from 'js-cookie';


export default function SurveyDataPage() {
  const [isAdmin, setIsAdmin] = useState(true); // Assume admin is logged in
  const [surveyData, setSurveyData] = useState([]); // To hold the survey data
  const [loading, setLoading] = useState(true); // For loading state
  const [error, setError] = useState(null); // For error state
  const [language, setLanguage] = useState('en'); // State for language
  const router = useRouter(); // For routing

  // Translations for different languages
  const translations = {
    en: {
      surveyTitle: 'Survey Data',
      age: 'Age',
      gender: 'Gender',
      email: 'Email',
      artsDegree: 'Visual Arts Course?',
      actions: 'Actions',
      delete: 'Delete',
      loading: 'Loading survey data...',
      error: 'Error: ',
      noData: 'No survey data available.',
      confirmDelete: 'Are you sure you want to delete this entry?',
      deleteError: 'Error deleting entry: ',
    },
    fr: {
      surveyTitle: 'Données de l\'enquête',
      age: 'Âge',
      gender: 'Genre',
      email: 'Email',
      artsDegree: 'Cours d\'arts visuels?',
      actions: 'Actions',
      delete: 'Supprimer',
      loading: 'Chargement des données de l\'enquête...',
      error: 'Erreur: ',
      noData: 'Aucune donnée d\'enquête disponible.',
      confirmDelete: 'Êtes-vous sûr de vouloir supprimer cette entrée?',
      deleteError: 'Erreur lors de la suppression de l\'entrée: ',
    },
  };

  const content = translations[language];

  const handleSignOut = () => {
      setIsAdmin(false);
       // Remove admin authentication token
      Cookies.remove('adminToken');
      router.push("/");
    };

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

  // Fetch survey data from the API
  useEffect(() => {
    const fetchSurveyData = async () => {
      try {
        const response = await fetch("http://localhost:5000/api/survey"); // Adjust the URL if your Flask server is running on a different host/port
        if (!response.ok) {
          throw new Error(`Error: ${response.status} - ${response.statusText}`);
        }
        const data = await response.json(); // Parse the JSON response
        setSurveyData(data); // Update the state with the fetched data
      } catch (err) {
        setError(err.message); // Set the error message
      } finally {
        setLoading(false); // Set loading to false when done
      }
    };

    fetchSurveyData(); // Call the function
  }, []);

  // Backend has been updated to support DELETE requests
  const handleDelete = async (email) => {
    if (!window.confirm(content.confirmDelete)) return;

    try {
      const response = await fetch(`http://localhost:5000/api/survey/${email}`, {
        method: "DELETE",
      });
      if (!response.ok) {
        throw new Error(content.deleteError);
      }
      setSurveyData(surveyData.filter((entry) => entry.email !== email));
    } catch (err) {
      alert(content.deleteError + err.message);
    }
  };

  // Display a loading message while fetching data
  if (loading) {
    return <p className="text-center text-gray-500 mt-10">{content.loading}</p>;
  }

  // Display an error message if an error occurs
  if (error) {
    return <p className="text-center text-red-500 mt-10">{content.error}{error}</p>;
  }

  // Render the survey data
  return (
    <div className="min-h-screen flex">
      <Sidebar language={language} onLanguageChange={handleLanguageChange} />
      <div className="flex-1">
        <Navbar
                  isAdmin={isAdmin}
                  onSignOut={handleSignOut}
                  language={language}
                  onLanguageChange={handleLanguageChange}
                />
        <div className="min-h-screen bg-gradient-to-b from-gray-500 via-gray-300 to-gray-100 p-10">
          <h1 className="text-2xl font-bold mb-6 text-center">{content.surveyTitle}</h1>
          {surveyData.length > 0 ? (
            <table className="w-full border-collapse border border-gray-300">
              <thead>
                <tr className="bg-gray-200">
                  <th className="border border-gray-300 p-2">{content.age}</th>
                  <th className="border border-gray-300 p-2">{content.gender}</th>
                  <th className="border border-gray-300 p-2">{content.email}</th>
                  <th className="border border-gray-300 p-2">{content.artsDegree}</th>
                  <th className="border border-gray-300 p-2">{content.actions}</th>
                </tr>
              </thead>
              <tbody>
                {surveyData.map((entry, index) => (
                  <tr key={entry.email} className={index % 2 === 0 ? "bg-white" : "bg-gray-50"}>
                    <td className="border border-gray-300 p-2">{entry.age}</td>
                    <td className="border border-gray-300 p-2">{entry.gender}</td>
                    <td className="border border-gray-300 p-2">{entry.email}</td>
                    <td className="border border-gray-300 p-2">{entry.artsDegree ? "Yes" : "No"}</td>
                    <td className="border border-gray-300 p-2 text-center">
                      <button
                        onClick={() => handleDelete(entry.email)}
                        className="bg-red-500 text-white px-3 py-1 rounded hover:bg-red-600"
                      >
                        {content.delete}
                      </button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          ) : (
            <p className="text-center text-gray-600 mt-10">{content.noData}</p>
          )}
        </div>
      </div>
    </div>
  );
}