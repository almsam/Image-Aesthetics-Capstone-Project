import React, { useState } from 'react';
import { FaEdit, FaStar, FaDatabase, FaImages } from 'react-icons/fa'; // Import icons from react-icons library
import { useRouter } from 'next/navigation'; // Import useRouter for navigation

const Sidebar = () => {
  // State to manage the open/close state of the sidebar
  const [isOpen, setIsOpen] = useState(false);
  const router = useRouter(); // Initialize the router



  const handleRatingData = () => {
    router.push('/ratingdata-page'); // Navigate to Rate Images page
  };
  
  const handleViewImagesets = () => {
    router.push('/view-imagesets'); // Navigate to View Imagesets page
  };

  const handleViewSurveyData = () => {
    router.push('/survey-data'); // Navigate to View Survey Data page
  }

  return (
    <div className="flex">
      {/* Sidebar */}
      <div
        className={`bg-gray-900 text-white 
                    fixed h-screen transition-all 
                    duration-300 z-10 
                    ${isOpen ? 'w-64' : 'w-0 overflow-hidden'
          }`}>
        {/* Sidebar content */}
        <div className="flex flex-col items-center">
          <h3 className="text-2xl font-semibold mt-4 text-gray-200">Admin Menu</h3>
          <div className="mt-4 space-y-4">
            <button
              className="flex items-center w-full p-3 rounded-lg hover:bg-gray-700 hover:text-yellow-400 transition duration-200"
              onClick={handleRatingData}
            >
              <FaStar className="mr-3 text-yellow-400" /> Export rating data
            </button>
            <button
              className="flex items-center w-full p-3 rounded-lg hover:bg-gray-700 hover:text-yellow-400 transition duration-200"
              onClick={handleViewImagesets}
            >
              <FaImages className="mr-3 text-yellow-400" /> View Imagesets
            </button>
            <button
              className="flex items-center w-full p-3 rounded-lg hover:bg-gray-700 hover:text-yellow-400 transition duration-200"
              onClick={handleViewSurveyData}
            >
              <FaDatabase className="mr-3 text-yellow-400" /> View Survey Data
            </button>
          </div>
        </div>
      </div>
      {/* Main content */}
      <div className={`bg-gray-900 flex-1 p-4 ${isOpen ? 'ml-64' : 'ml-0'}`}>
        {/* Button to toggle sidebar */}
        <div className="ml-auto">
          <button
            className="bg-gray-700 hover:bg-blue-700 
                       text-white font-bold py-4 px-6 rounded"
            onClick={() => setIsOpen(!isOpen)}>
            {isOpen ? (
              <svg
                className="h-8 w-8"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor">
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M6 18L18 6M6 6l12 12" />
              </svg>
            ) : (
              <svg
                className="h-8 w-8"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor">
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M4 6h16M4 12h16m-7 6h7" />
              </svg>
            )}
          </button>
        </div>
      </div>
    </div>
  );
};

export default Sidebar;
