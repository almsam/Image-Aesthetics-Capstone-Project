"use client";
import React from 'react';

const AnimatedGrating = () => {
  return (
    <div className="grating-container">
      <div className="grating"></div>
      <style jsx>{`
        .grating-container {
          position: fixed;
          top: 0;
          left: 0;
          width: 100%;
          height: 100%;
          overflow: hidden;
          z-index: -1;
          background: linear-gradient(120deg, 
            rgba(255, 182, 193, 0.6) 0%, 
            rgba(147, 197, 253, 0.6) 100%
          );
        }
        
        .grating {
          position: absolute;
          top: -50%;
          left: -50%;
          width: 200%;
          height: 200%;
          background: repeating-linear-gradient(
            45deg,
            rgba(128, 90, 213, 0.2) 0px,
            rgba(128, 90, 213, 0.2) 2px,
            transparent 2px,
            transparent 20px
          ),
          repeating-linear-gradient(
            -45deg,
            rgba(255, 255, 255, 0.15) 0px,
            rgba(255, 255, 255, 0.15) 2px,
            transparent 2px,
            transparent 20px
          );
          animation: moveGrating 30s linear infinite;
          transform-origin: center;
        }
        
        @keyframes moveGrating {
          0% {
            transform: rotate(0deg);
          }
          100% {
            transform: rotate(360deg);
          }
        }
      `}</style>
    </div>
  );
};

export default AnimatedGrating;