"use client";
import { useRouter } from "next/navigation";
import { useState, useEffect } from "react";
import Navbar from "../components/Navbar";
import Sidebar from "../components/adminSidebar";
import Cookies from "js-cookie";


export default function AdminImageViewer() {
  const [language, setLanguage] = useState("en");
  const [filterText, setFilterText] = useState("");
  const [filteredImages, setFilteredImages] = useState([]);
  const [isAdmin, setIsAdmin] = useState(true); // Assume admin is logged in
  const router = useRouter();

  // Translation content
  const translations = {
    en: {
      pageTitle: "Admin Image Viewer",
      subheading: "View and manage all uploaded images as well as AI generated images",
      searchPlaceholder: "Search by image name or ID...",
    },
    fr: {
      pageTitle: "Visionneuse d'images Admin",
      subheading: "Afficher et gérer toutes les images téléchargées ainsi que les images générées par l'IA",
      searchPlaceholder: "Rechercher par nom d'image ou ID...",
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

  // Add the new generated images also to be displayed
  imagePairs.push([{ id: 101, url: "/generated_image_quality_100.png" }]);
  imagePairs.push([{ id: 102, url: "/generated_image_quality_200.png" }]);
  imagePairs.push([{ id: 103, url: "/generated_image_quality_300.png" }]);
  imagePairs.push([{ id: 104, url: "/generated_image_quality_400.png" }]);
  imagePairs.push([{ id: 105, url: "/generated_image_quality_500.png" }]);
  imagePairs.push([{ id: 106, url: "/generated_image_quality_600.png" }]);
  imagePairs.push([{ id: 107, url: "/generated_image_quality_700.png" }]);
  imagePairs.push([{ id: 108, url: "/generated_image_quality_800.png" }]);
  imagePairs.push([{ id: 109, url: "/generated_image_quality_900.png" }]);
  imagePairs.push([{ id: 110, url: "/generated_image_quality_1000.png" }]);
  imagePairs.push([{ id: 111, url: "/generated_image_quality_1100.png" }]);
  imagePairs.push([{ id: 112, url: "/generated_image_quality_1200.png" }]);
  
  // Flatten the image pairs array into a single array of images
  const flattenedImages = imagePairs.flat();

  // Language handling with localStorage
  useEffect(() => {
    const savedLanguage = localStorage.getItem("language");
    if (savedLanguage) {
      setLanguage(savedLanguage);
    }
  }, []);

  const handleSignOut = () => {
      setIsAdmin(false);
      Cookies.remove("adminToken");
      router.push("/");
    };
  
    const handleLanguageChange = (lang) => {
      setLanguage(lang);
      localStorage.setItem("language", lang);
    };

  // Handle search/filter logic
  useEffect(() => {
    const lowerCaseFilter = filterText.toLowerCase();
    setFilteredImages(
      flattenedImages.filter(
        (img) =>
          img.url.toLowerCase().includes(lowerCaseFilter) ||
          img.id.toString().includes(lowerCaseFilter)
      )
    );
  }, [filterText]);

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
        <main className="flex-1 p-8">
          <h2 className="text-3xl font-semibold mb-4">{content.pageTitle}</h2>
          <h3 className="text-xl text-gray-700 mb-6">{content.subheading}</h3>

          {/* Search bar */}
          <div className="mb-6">
            <input
              type="text"
              placeholder={content.searchPlaceholder}
              value={filterText}
              onChange={(e) => setFilterText(e.target.value)}
              className="w-full px-4 py-2 border border-gray-400 rounded shadow-sm"
            />
          </div>

          {/* Image grid */}
          <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-6 gap-4">
            {filteredImages.map((image) => (
              <div
                key={image.id}
                className="bg-white border border-gray-300 shadow rounded-lg p-4 text-center"
              >
                <img
                  src={image.url}
                  alt={`Image ${image.id}`}
                  className="w-full h-32 object-cover rounded mb-3"
                />
                <p className="text-sm text-gray-600">{`ID: ${image.id}`}</p>
              </div>
            ))}
          </div>

          {/* Empty state */}
          {filteredImages.length === 0 && (
            <p className="text-center text-gray-600 mt-6">No images found.</p>
          )}
        </main>
      </div>
    </div>
  );
}
