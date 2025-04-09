"use client";
import React, { useState, useEffect } from 'react';

const AsmrShapes = () => {
  const [shapes, setShapes] = useState([]);

  useEffect(() => {
    // Generate shapes only on the client side
    const generatedShapes = Array.from({ length: 15 }, (_, i) => ({
      id: i,
      size: Math.random() * 100 + 50,
      duration: Math.random() * 20 + 15,
      delay: Math.random() * -20,
      initialX: Math.random() * 100,
      initialY: Math.random() * 100,
    }));
    setShapes(generatedShapes);
  }, []); // Empty dependency array means this runs once on mount

  return (
    <div className="shapes-container">
      {shapes.map((shape) => (
        <div
          key={shape.id}
          className="floating-shape"
          style={{
            '--size': `${shape.size}px`,
            '--duration': `${shape.duration}s`,
            '--delay': `${shape.delay}s`,
            '--initialX': `${shape.initialX}%`,
            '--initialY': `${shape.initialY}%`,
          }}
        />
      ))}
      <style jsx>{`
        .shapes-container {
          position: fixed;
          top: 0;
          left: 0;
          width: 100%;
          height: 100%;
          overflow: hidden;
          z-index: 0;
          opacity: 0.4;
        }

        .floating-shape {
          position: absolute;
          width: var(--size);
          height: var(--size);
          border-radius: 40%;
          background: radial-gradient(
            circle at 30% 30%,
            rgba(255, 255, 255, 0.4),
            rgba(255, 255, 255, 0.1)
          );
          left: var(--initialX);
          top: var(--initialY);
          animation: float var(--duration) ease-in-out infinite;
          animation-delay: var(--delay);
          backdrop-filter: blur(5px);
          transform-origin: center center;
        }

        .floating-shape:nth-child(3n) {
          background: radial-gradient(
            circle at 30% 30%,
            rgba(147, 51, 234, 0.2),
            rgba(147, 51, 234, 0.05)
          );
        }

        .floating-shape:nth-child(3n + 1) {
          background: radial-gradient(
            circle at 30% 30%,
            rgba(219, 39, 119, 0.2),
            rgba(219, 39, 119, 0.05)
          );
        }

        @keyframes float {
          0% {
            transform: translate(0, 0) rotate(0deg) scale(1);
          }
          33% {
            transform: translate(30px, -50px) rotate(120deg) scale(1.1);
          }
          66% {
            transform: translate(-20px, 20px) rotate(240deg) scale(0.9);
          }
          100% {
            transform: translate(0, 0) rotate(360deg) scale(1);
          }
        }

        .floating-shape:nth-child(even) {
          animation-direction: reverse;
        }
      `}</style>
    </div>
  );
};

export default AsmrShapes; 