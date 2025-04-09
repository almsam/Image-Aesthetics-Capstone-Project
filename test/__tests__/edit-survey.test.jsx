// src/app/__tests__/survey.test.jsx
import { expect, test, vi } from 'vitest';
import { render, screen } from '@testing-library/react';
import EditSurvey from '../../app/edit-survey/page';
import { useRouter } from 'next/navigation';

// Mock the useRouter hook from Next.js
vi.mock('next/navigation', () => ({
  useRouter: () => ({
    push: vi.fn(),
  }),
}));

test('Edit Survey Page', () => {
  render(<EditSurvey />);

  // Check if the "User Survey" header is displayed
  expect(screen.getByRole('heading', { name: /Edit Your Survey Information/i })).toBeDefined();

  // Check if the "Age" input field is displayed
  expect(screen.getByLabelText(/Age/i)).toBeDefined();

  // Check if the "Gender" input field is displayed
  expect(screen.getByLabelText(/Gender/i)).toBeDefined();
  
  // Check if the checkbox is displayed using getByRole
  const artsDegreeCheckbox = screen.getByRole('checkbox', {
    name: /Have you taken a Visual Arts Course\?/i,
  });
  expect(artsDegreeCheckbox).toBeDefined();

//   // Check if the "Submit" button is displayed
//   expect(screen.getByTestId('surveyButton')).toBeDefined();
});
