"use client";
import { useRouter } from "next/navigation";
import Navbar from "../components/Navbar";
import Sidebar from "../components/userSidebar";
import { useState, useEffect } from "react";
import AnimatedGrating from "../components/AnimatedGrating";
import AsmrShapes from "../components/AsmrShapes";

export default function ImageGenPage() {
  const router = useRouter();
  const [ratings, setRatings] = useState({});
  const [language, setLanguage] = useState("en");

  // Translations for different languages
  const translations = {
    en: {
      pageTitle: "AI Generated Aesthetic Images",
      submitRating: "Submit Rating",
      exitToDashboard: "Exit to Dashboard",
      errorSubmitting: "Error submitting ratings:",
      successSubmitting: "Ratings submitted successfully!",
    },
    fr: {
      pageTitle: "Images Esthétiques Générées par l'IA",
      submitRating: "Soumettre la Note",
      exitToDashboard: "Retour au Tableau de Bord",
      errorSubmitting: "Erreur lors de la soumission des notes :",
      successSubmitting: "Notes soumises avec succès !",
    },
  };

  const content = translations[language];

  // Load language preference from localStorage on initial render
  useEffect(() => {
    const savedLanguage = localStorage.getItem("language");
    if (savedLanguage) {
      setLanguage(savedLanguage);
    }
  }, []);

  // Update localStorage whenever the language changes
  const handleLanguageChange = (lang) => {
    setLanguage(lang);
    localStorage.setItem("language", lang);
  };

  const handleRatingChange = (index, value) => {
    const ratingValue = parseInt(value, 10);
    if (ratingValue >= 1 && ratingValue <= 10) {
      setRatings((prevRatings) => ({ ...prevRatings, [index]: ratingValue }));
    } else {
      setRatings((prevRatings) => ({ ...prevRatings, [index]: 0 }));
    }
  };

  const submitRatings = async () => {
    const choices = Object.entries(ratings).map(([pairIndex, rating]) => ({
      pairIndex: parseInt(pairIndex, 10),
      selectedImageId: rating,
    }));

    try {
      const response = await fetch("http://127.0.0.1:5000/api/ratings", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ choices }),
      });

      if (!response.ok) {
        const errorData = await response.text();
        console.error("Server Error:", errorData);
        alert(content.errorSubmitting + " " + errorData);
        return;
      }

      const data = await response.json();
      alert(content.successSubmitting);
      setRatings({}); // Clear input after submission
    } catch (error) {
      console.error(content.errorSubmitting, error);
      alert(content.errorSubmitting + " " + error.message);
    }
  };

  return (
    <div className="min-h-screen relative overflow-hidden bg-gradient-to-br from-fuchsia-200 via-violet-300 to-cyan-300 flex">
      <AnimatedGrating />
      <AsmrShapes />
      <Sidebar language={language} />
      <div className="flex-1 flex flex-col relative z-10">
        <Navbar language={language} onLanguageChange={handleLanguageChange} />
        <main className="container mx-auto p-10 text-center">
          <h2 className="text-3xl md:text-4xl font-bold mb-8 text-black">
            {content.pageTitle}
          </h2>
          <div className="grid md:grid-cols-3 gap-6">
            {[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12].map((imageId) => (
              <div
                key={`image-${imageId}`}
                className="bg-white p-6 rounded-lg shadow-lg flex flex-col items-center"
              >
                <h3 className="text-lg font-semibold mb-4">
                  Generated Image {imageId}
                </h3>
                <img
                  src={`/generated_image_quality_${imageId}00.png`}
                  alt={`Generated ${imageId}`}
                  className="mb-4 w-60 h-auto object-contain"
                />
                <input
                  type="number"
                  min="1"
                  max="12"
                  className="w-16 p-1 border rounded text-center mb-4 bg-white/90"
                  onChange={(e) => handleRatingChange(imageId, e.target.value)}
                />
                <button
                  className="bg-indigo-600 hover:bg-gradient-to-r hover:from-purple-500 hover:to-pink-500 transition-all duration-300 text-white py-2 px-4 rounded-lg shadow-lg transform hover:scale-105 hover:shadow-xl hover:shadow-indigo-200/50"
                  onClick={submitRatings}
                >
                  {content.submitRating}
                </button>
              </div>
            ))}
          </div>
          <div className="mt-10">
            <button
              onClick={() => router.push("/user-dashboard")}
              className="bg-indigo-600 hover:bg-gradient-to-r hover:from-purple-500 hover:to-pink-500 transition-all duration-300 text-white py-2 px-4 rounded-lg shadow-lg transform hover:scale-105 hover:shadow-xl hover:shadow-indigo-200/50"
            >
              {content.exitToDashboard}
            </button>
          </div>
        </main>
      </div>
    </div>
  );
}
