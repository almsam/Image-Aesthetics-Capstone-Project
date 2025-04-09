"use client";
import { useRouter } from "next/navigation";
import React, { useState, useEffect } from "react";
import Navbar from "../components/Navbar";
import Sidebar from "../components/adminSidebar";
import Cookies from "js-cookie";

export default function RatingDataPage() {
  const [ratingData, setRatingData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [exporting, setExporting] = useState(false);
  const [language, setLanguage] = useState("en");
  const [isAdmin, setIsAdmin] = useState(true);
  const router = useRouter();

  const translations = {
    en: {
      ratingTitle: "User Rating Data",
      exportData: "Export Data",
      exporting: "Exporting...",
      email: "User Email",
      question: "Question Number",
      imageId: "Image ID",
      loading: "Loading rating data...",
      error: "Error: ",
      noData: "No rating data available.",
    },
    fr: {
      ratingTitle: "Données d'évaluation des utilisateurs",
      exportData: "Exporter les données",
      exporting: "Exportation...",
      email: "Email de l'utilisateur",
      question: "Numéro de question",
      imageId: "ID de l'image",
      loading: "Chargement des données d'évaluation...",
      error: "Erreur: ",
      noData: "Aucune donnée d'évaluation disponible.",
    },
  };

  const content = translations[language];

  useEffect(() => {
    const savedLanguage = localStorage.getItem("language");
    if (savedLanguage) {
      setLanguage(savedLanguage);
    }
  }, []);

  useEffect(() => {
    const fetchRatingData = async () => {
      try {
        const response = await fetch("http://localhost:5000/api/ratings/fetch");
        if (!response.ok) {
          throw new Error(`${content.error}${response.status} - ${response.statusText}`);
        }
        const data = await response.json();
        setRatingData(data.ratings);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchRatingData();
  }, [content.error]);

  const handleExport = async () => {
    setExporting(true);
    try {
      const response = await fetch("http://localhost:5000/api/export", {
        method: "POST",
      });

      if (!response.ok) {
        throw new Error(`${content.error}${response.status} - ${response.statusText}`);
      }

      const blob = await response.blob();
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = "ratings.csv";
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
    } catch (err) {
      alert(`${content.error}${err.message}`);
    } finally {
      setExporting(false);
    }
  };

  const handleSignOut = () => {
    setIsAdmin(false);
    Cookies.remove("adminToken");
    router.push("/");
  };

  const handleLanguageChange = (lang) => {
    setLanguage(lang);
    localStorage.setItem("language", lang);
  };

  if (loading) {
    return <p className="text-center text-gray-500 mt-10">{content.loading}</p>;
  }

  if (error) {
    return <p className="text-center text-red-500 mt-10">{content.error}{error}</p>;
  }

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
          <div className="flex justify-between items-center mb-6">
            <h1 className="text-2xl font-bold">{content.ratingTitle}</h1>
            <button
              onClick={handleExport}
              disabled={exporting}
              className={`px-4 py-2 text-white font-bold rounded ${
                exporting ? "bg-gray-400 cursor-not-allowed" : "bg-blue-600 hover:bg-blue-700"
              }`}
            >
              {exporting ? content.exporting : content.exportData}
            </button>
          </div>

          {ratingData.length > 0 ? (
            <table className="w-full border-collapse border border-gray-300">
              <thead>
                <tr className="bg-gray-200">
                  <th className="border border-gray-300 p-2">{content.email}</th>
                  <th className="border border-gray-300 p-2">{content.question}</th>
                  <th className="border border-gray-300 p-2">{content.imageId}</th>
                </tr>
              </thead>
              <tbody>
                {ratingData.map((entry, index) => (
                  <tr key={index} className={index % 2 === 0 ? "bg-white" : "bg-gray-50"}>
                    <td className="border border-gray-300 p-2">{entry[1]}</td>
                    <td className="border border-gray-300 p-2">{entry[2]}</td>
                    <td className="border border-gray-300 p-2">{entry[3]}</td>
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
