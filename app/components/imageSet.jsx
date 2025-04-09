import React, { useState } from 'react';

export default function ImageSet({ image1, image2, onSubmitChoice }) {
  const [selectedImageId, setSelectedImageId] = useState(null);

  const handleImageSelect = (imageId) => {
    setSelectedImageId(imageId);

    // Notify the parent component of the selected choice
    if (onSubmitChoice) {
      onSubmitChoice(imageId);
    }
  };

  return (
    <div className="flex flex-col items-center">
      <div className="flex space-x-4 mb-4">
        {/* Image 1 */}
        <div
          className={`w-60 h-75 rounded-lg shadow-md cursor-pointer border-4 ${
            selectedImageId === image1.id ? 'border-blue-500' : 'border-transparent'
          }`}
          onClick={() => handleImageSelect(image1.id)}
        >
          <img src={image1.url} alt="Image 1" className="w-full h-full object-cover rounded-lg" />
        </div>

        {/* Image 2 */}
        <div
          className={`w-60 h-75 rounded-lg shadow-md cursor-pointer border-4 ${
            selectedImageId === image2.id ? 'border-blue-500' : 'border-transparent'
          }`}
          onClick={() => handleImageSelect(image2.id)}
        >
          <img src={image2.url} alt="Image 2" className="w-full h-full object-cover rounded-lg" />
        </div>
      </div>
    </div>
  );
}
