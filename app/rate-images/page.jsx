"use client";
import { useState, useEffect } from "react";
import Navbar from "../components/Navbar";
import Sidebar from "../components/userSidebar";
import ImageSet from "../components/imageSet";
import Link from "next/link";
import AnimatedGrating from "../components/AnimatedGrating";
import AsmrShapes from "../components/AsmrShapes";

export default function RateImages() {
  const [language, setLanguage] = useState("en");
  const [numQuestions, setNumQuestions] = useState(0);
  const [inputValue, setInputValue] = useState("");
  const [choices, setChoices] = useState({});
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  
  // Translations for the page
  const translations = {
    en: {
      pageTitle: "Rate Images",
      subheading: "Compare and choose the image you find more aesthetically pleasing",
      instructions: "Click on the image you prefer for each pair, and submit your choices at the end.",
      questionPrompt: "How many questions would you like to answer? (with a limit of 50)",
      placeholder: "Enter number of questions",
      setQuestions: "Set Questions",
      submitChoices: "Submit All Choices",
      successMessage: "All choices submitted successfully!",
      failureMessage: "Failed to submit choices.",
      errorMessage: "An error occurred while submitting your choices.",
      previous: "Previous",
      next: "Next",
    },
    fr: {
      pageTitle: "Noter les images",
      subheading: "Comparez et choisissez l'image que vous trouvez la plus esthétique",
      instructions: "Cliquez sur l'image que vous préférez pour chaque paire, puis soumettez vos choix à la fin.",
      questionPrompt: "Combien de questions souhaitez-vous répondre ? (limite de 50)",
      placeholder: "Entrez le nombre de questions",
      setQuestions: "Définir les questions",
      submitChoices: "Soumettre tous les choix",
      successMessage: "Tous les choix ont été soumis avec succès !",
      failureMessage: "Échec de la soumission des choix.",
      errorMessage: "Une erreur s'est produite lors de la soumission de vos choix.",
      previous: "Précédent",
      next: "Suivant",
    },
  };

  const content = translations[language];

  // Image pairs array with 100 images (50 pairs)
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
  ];  
  
   // Check if the language preference is already stored in localStorage
   useEffect(() => {
    const savedLanguage = localStorage.getItem("language");
    if (savedLanguage) {
      setLanguage(savedLanguage); // Set the language from localStorage if available
    }
  }, []);

  // Store the selected language in localStorage when it changes
  const handleLanguageChange = (lang) => {
    setLanguage(lang);
    localStorage.setItem("language", lang); // Save the selected language to localStorage
  };

  const handleChoiceChange = (selectedImageId) => {
    // Save the selected choice for the current question
    setChoices((prevChoices) => ({
      ...prevChoices,
      [currentQuestionIndex]: selectedImageId,
    }));
  };

  const handleSetQuestions = () => {
    const parsedValue = parseInt(inputValue, 10);
    if (isNaN(parsedValue) || parsedValue <= 0 || parsedValue > imagePairs.length) {
      alert(content.failureMessage);
      return;
    }
    setNumQuestions(parsedValue);
    setCurrentQuestionIndex(0); // Reset to the first question
  };

  const handleSubmitAll = async () => {
    const formattedChoices = Object.entries(choices).map(([pairIndex, selectedImageId]) => ({
      pairIndex: parseInt(pairIndex, 10),
      selectedImageId,
      userId: 1, // Replace with actual user ID if needed
    }));

    if (formattedChoices.length !== numQuestions) {
      alert(content.failureMessage);
      return;
    }

    try {
      const response = await fetch("http://localhost:5000/api/ratings", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ choices: formattedChoices }),
      });

      if (response.ok) {
        alert(content.successMessage);
      } else {
        alert(content.failureMessage);
      }
    } catch (error) {
      console.error(error);
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
        <main className="flex-1 p-10 relative">
          <div className="bg-white/80 backdrop-blur-sm p-8 rounded-lg shadow-lg mb-8">
            <h2 className="text-3xl font-semibold mb-8 text-black">{content.pageTitle}</h2>
            <h3 className="text-2xl font-semibold mb-6 text-black">{content.subheading}</h3>
            <p className="text-lg text-gray-600 mb-6">{content.instructions}</p>

            {numQuestions === 0 && (
              <div className="flex items-center mb-8">
                <p className="text-lg font-semibold text-black mb-2">{content.questionPrompt}</p>
                <input
                  type="number"
                  placeholder={content.placeholder}
                  value={inputValue}
                  onChange={(e) => setInputValue(e.target.value)}
                  className="border border-gray-400 rounded px-4 py-2 mr-4 ml-4"
                />
                <button
                  onClick={handleSetQuestions}
                  className="px-4 py-2 bg-indigo-600 hover:bg-gradient-to-r hover:from-purple-500 hover:to-pink-500 transition-all duration-300 text-white font-semibold rounded shadow-lg transform hover:scale-105 hover:shadow-xl hover:shadow-indigo-200/50"
                >
                  {content.setQuestions}
                </button>
              </div>
            )}

            {numQuestions > 0 && (
              <div>
                <div className="bg-white/90 backdrop-blur-sm p-8 rounded-lg text-center">
                  <p data-testid="question-counter" className="text-black">{`Question ${currentQuestionIndex + 1} of ${numQuestions}`}</p>
                  <ImageSet
                    image1={imagePairs[currentQuestionIndex][0]}
                    image2={imagePairs[currentQuestionIndex][1]}
                    selectedImageId={choices[currentQuestionIndex] || null}
                    onSubmitChoice={handleChoiceChange}
                  />
                </div>

                <div className="flex justify-between mt-8">
                  <button
                    data-testid="previous-button"
                    onClick={() => setCurrentQuestionIndex((prev) => Math.max(prev - 1, 0))}
                    disabled={currentQuestionIndex === 0}
                    className="px-4 py-2 bg-indigo-600 hover:bg-gradient-to-r hover:from-purple-500 hover:to-pink-500 transition-all duration-300 text-white font-semibold rounded shadow-lg transform hover:scale-105 hover:shadow-xl hover:shadow-indigo-200/50 disabled:opacity-50"
                  >
                    {content.previous}
                  </button>
                  <button
                    data-testid="next-button"
                    onClick={() => setCurrentQuestionIndex((prev) => Math.min(prev + 1, numQuestions - 1))}
                    disabled={currentQuestionIndex === numQuestions - 1}
                    className="px-4 py-2 bg-indigo-600 hover:bg-gradient-to-r hover:from-purple-500 hover:to-pink-500 transition-all duration-300 text-white font-semibold rounded shadow-lg transform hover:scale-105 hover:shadow-xl hover:shadow-indigo-200/50 disabled:opacity-50"
                  >
                    {content.next}
                  </button>
                </div>

                {currentQuestionIndex === numQuestions - 1 && (
                  <div className="flex justify-center">
                    <Link href="/results-page">
                      <button
                        data-testid="submit-button"
                        onClick={handleSubmitAll}
                        className="px-6 py-3 bg-indigo-600 hover:bg-gradient-to-r hover:from-purple-500 hover:to-pink-500 transition-all duration-300 text-white font-semibold rounded-lg shadow-lg transform hover:scale-105 hover:shadow-xl hover:shadow-indigo-200/50"
                      >
                        {content.submitChoices}
                      </button>
                    </Link>
                  </div>
                )}
              </div>
            )}
          </div>
        </main>
      </div>
    </div>
  );
}