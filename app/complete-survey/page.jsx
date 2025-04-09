"use client";

import { useRouter } from 'next/navigation';

export default function CompleteSurvey() {
  const router = useRouter();

  const handleRedirect = () => {
    router.push('/survey');
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100">
      <div className="bg-white p-6 rounded-lg shadow-lg text-center">
        <h2 className="text-2xl font-semibold mb-4">Action Required</h2>
        <p className="mb-4">Please complete the survey before proceeding.</p>
        <button
          onClick={handleRedirect}
          className="px-4 py-2 bg-indigo-600 hover:bg-gradient-to-r hover:from-purple-500 hover:to-pink-500 transition-all duration-300 text-white font-semibold rounded shadow-lg transform hover:scale-105 hover:shadow-xl hover:shadow-indigo-200/50"
        >
          Go to Survey
        </button>
      </div>
    </div>
  );
}