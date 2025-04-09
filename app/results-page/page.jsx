"use client";
import { useEffect, useState } from "react";
import { useRouter } from 'next/navigation';
import Navbar from "../components/Navbar";
import Sidebar from "../components/userSidebar";
import AnimatedGrating from "../components/AnimatedGrating";
import AsmrShapes from "../components/AsmrShapes";

export default function ResultsPage() {
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [language, setLanguage] = useState('en');
  const router = useRouter();

  const translations = {
    en: {
      title: "Results",
      loading: "Loading results...",
      noResults: "No results available.",
      viewAiImages: "View AI generated aesthetic images",
      goToGeneration: "Go to Image Generation",
      exitToDashboard: "Exit to Dashboard"
    },
    fr: {
      title: "Résultats",
      loading: "Chargement des résultats...",
      noResults: "Aucun résultat disponible.",
      viewAiImages: "Voir les images générées par l'IA",
      goToGeneration: "Aller à la génération d'images",
      exitToDashboard: "Retour au tableau de bord"
    }
  };

  const content = translations[language];

  useEffect(() => {
    const savedLanguage = localStorage.getItem('language');
    if (savedLanguage) {
      setLanguage(savedLanguage);
    }
  }, []);

  const handleLanguageChange = (lang) => {
    setLanguage(lang);
    localStorage.setItem('language', lang);
  };

  const imagePairs = [
    [{ id: 1, url: "/img 1L.png" }, { id: 2, url: "/img 1R.png" }],
    [{ id: 3, url: "/img 2L.png" }, { id: 4, url: "/img 2R.png" }],
    [{ id: 5, url: "/img 3L.png" }, { id: 6, url: "/img 3R.png" }],
    [{ id: 7, url: "/img 4L.png" }, { id: 8, url: "/img 4R.png" }],
    [{ id: 9, url: "/img 5L.png" }, { id: 10, url: "/img 5R.png" }],
    [{ id: 11, url: "/img 6L.png" }, { id: 12, url: "/img 6R.png" }],
    [{ id: 13, url: "/img 7L.png" }, { id: 14, url: "/img 7R.png" }],
    [{ id: 15, url: "/img 8L.png" }, { id: 16, url: "/img 8R.png" }],
    [{ id: 17, url: "/img 9L.png" }, { id: 18, url: "/img 9R.png" }],
    [{ id: 19, url: "/img 10L.png" }, { id: 20, url: "/img 10R.png" }],
    [{ id: 21, url: "/img 11L.png" }, { id: 22, url: "/img 11R.png" }],
    [{ id: 23, url: "/img 12L.png" }, { id: 24, url: "/img 12R.png" }],
    [{ id: 25, url: "/img 13L.png" }, { id: 26, url: "/img 13R.png" }],
    [{ id: 27, url: "/img 14L.png" }, { id: 28, url: "/img 14R.png" }],
    [{ id: 29, url: "/img 15L.png" }, { id: 30, url: "/img 15R.png" }],
    [{ id: 31, url: "/img 16L.png" }, { id: 32, url: "/img 16R.png" }],
    [{ id: 33, url: "/img 17L.png" }, { id: 34, url: "/img 17R.png" }],
    [{ id: 35, url: "/img 18L.png" }, { id: 36, url: "/img 18R.png" }],
    [{ id: 37, url: "/img 19L.png" }, { id: 38, url: "/img 19R.png" }],
    [{ id: 39, url: "/img 20L.png" }, { id: 40, url: "/img 20R.png" }],
    [{ id: 41, url: "/img 21L.png" }, { id: 42, url: "/img 21R.png" }],
    [{ id: 43, url: "/img 22L.png" }, { id: 44, url: "/img 22R.png" }],
    [{ id: 45, url: "/img 23L.png" }, { id: 46, url: "/img 23R.png" }],
    [{ id: 47, url: "/img 24L.png" }, { id: 48, url: "/img 24R.png" }],
    [{ id: 49, url: "/img 25L.png" }, { id: 50, url: "/img 25R.png" }],
    [{ id: 51, url: "/img 26L.png" }, { id: 52, url: "/img 26R.png" }],
    [{ id: 53, url: "/img 27L.png" }, { id: 54, url: "/img 27R.png" }],
    [{ id: 55, url: "/img 28L.png" }, { id: 56, url: "/img 28R.png" }],
    [{ id: 57, url: "/img 29L.png" }, { id: 58, url: "/img 29R.png" }],
    [{ id: 59, url: "/img 30L.png" }, { id: 60, url: "/img 30R.png" }],
    [{ id: 61, url: "/img 31L.png" }, { id: 62, url: "/img 31R.png" }],
    [{ id: 63, url: "/img 32L.png" }, { id: 64, url: "/img 32R.png" }],
    [{ id: 65, url: "/img 33L.png" }, { id: 66, url: "/img 33R.png" }],
    [{ id: 67, url: "/img 34L.png" }, { id: 68, url: "/img 34R.png" }],
    [{ id: 69, url: "/img 35L.png" }, { id: 70, url: "/img 35R.png" }],
    [{ id: 71, url: "/img 36L.png" }, { id: 72, url: "/img 36R.png" }],
    [{ id: 73, url: "/img 37L.png" }, { id: 74, url: "/img 37R.png" }],
    [{ id: 75, url: "/img 38L.png" }, { id: 76, url: "/img 38R.png" }],
    [{ id: 77, url: "/img 39L.png" }, { id: 78, url: "/img 39R.png" }],
    [{ id: 79, url: "/img 40L.png" }, { id: 80, url: "/img 40R.png" }],
    [{ id: 81, url: "/img 41L.png" }, { id: 82, url: "/img 41R.png" }],
    [{ id: 83, url: "/img 42L.png" }, { id: 84, url: "/img 42R.png" }],
    [{ id: 85, url: "/img 43L.png" }, { id: 86, url: "/img 43R.png" }],
    [{ id: 87, url: "/img 44L.png" }, { id: 88, url: "/img 44R.png" }],
    [{ id: 89, url: "/img 45L.png" }, { id: 90, url: "/img 45R.png" }],
    [{ id: 91, url: "/img 46L.png" }, { id: 92, url: "/img 46R.png" }],
    [{ id: 93, url: "/img 47L.png" }, { id: 94, url: "/img 47R.png" }],
    [{ id: 95, url: "/img 48L.png" }, { id: 96, url: "/img 48R.png" }],
    [{ id: 97, url: "/img 49L.png" }, { id: 98, url: "/img 49R.png" }],
    [{ id: 99, url: "/img 50L.png" }, { id: 100, url: "/img 50R.png" }],
    [{ id: 101, url: "/img 51L.png" }, { id: 102, url: "/img 51R.png" }],
    [{ id: 103, url: "/img 52L.png" }, { id: 104, url: "/img 52R.png" }],
    [{ id: 105, url: "/img 53L.png" }, { id: 106, url: "/img 53R.png" }],
  ];  

  useEffect(() => {
    const fetchResults = async () => {
      try {
        const response = await fetch("http://localhost:5000/api/ratings/results");
        if (response.ok) {
          const data = await response.json();
          console.log(data); // This will log the full response
          if (data.stats) {
            setResults(data.stats); // Extract the stats array from the response
          } else {
            setError('No stats available.');
          }
        } else {
          throw new Error("Failed to fetch results.");
        }
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };
    fetchResults();
  }, []);

  const findImageUrlById = (id) => {
    for (const pair of imagePairs) {
      for (const image of pair) {
        if (image.id === id) {
          return image.url;
        }
      }
    }
    return null;
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
        <div className="container mx-auto px-4 py-8">
          <main className="bg-white/80 backdrop-blur-sm p-8 rounded-lg shadow-lg">
            <h2 className="text-3xl font-bold text-center mb-8 text-black">{content.title}</h2>
            {loading ? (
              <div className="text-center">
                <p className="text-lg text-black">{content.loading}</p>
              </div>
            ) : error ? (
              <div className="text-center">
                <p className="text-red-600">{error}</p>
              </div>
            ) : results.length === 0 ? (
              <div className="text-center">
                <p className="text-lg text-black">{content.noResults}</p>
              </div>
            ) : (
              <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
                {results.map((result, index) => (
                  <div
                    key={index}
                    className="bg-white/90 backdrop-blur-sm p-6 rounded-lg shadow-lg max-w-xs mx-auto"
                  >
                    <h3 className="text-lg font-semibold mb-4 text-black">{`Image ID: ${result.image_id}`}</h3>
                    <img
                      src={findImageUrlById(result.image_id)}
                      alt={`Image ${result.image_id}`}
                      className="mb-4 w-40 h-auto"
                    />
                    <p className="text-sm text-black">{`Percentage: ${result.percentage}`}</p>
                  </div>
                ))}
              </div>
            )}

            <div className="mt-10 text-center">
              <p className="text-xl font-semibold mb-4 text-black">{content.viewAiImages}</p>
              <button
                onClick={() => router.push('/image-gen')}
                className="bg-indigo-600 hover:bg-gradient-to-r hover:from-purple-500 hover:to-pink-500 transition-all duration-300 text-white py-3 px-6 rounded-lg shadow-lg transform hover:scale-105 hover:shadow-xl hover:shadow-indigo-200/50 mb-6"
              >
                {content.goToGeneration}
              </button>

              <div className="mt-6">
                <button
                  onClick={() => router.push('/user-dashboard')}
                  className="bg-indigo-600 hover:bg-gradient-to-r hover:from-purple-500 hover:to-pink-500 transition-all duration-300 text-white py-3 px-6 rounded-lg shadow-lg transform hover:scale-105 hover:shadow-xl hover:shadow-indigo-200/50"
                >
                  {content.exitToDashboard}
                </button>
              </div>
            </div>
          </main>
        </div>
      </div>
    </div>
  );
}