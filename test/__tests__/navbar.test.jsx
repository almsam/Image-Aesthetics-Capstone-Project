// src/app/__tests__/navbar.test.jsx
import { expect, test } from 'vitest';
import { render, screen } from '@testing-library/react';
import Navbar from '../../app/components/Navbar';

test('Navbar', () => {
  render(<Navbar />);

  // Check if the "Login" link is displayed
  expect(screen.getByRole('link', { name: 'Admin Login' })).toBeDefined();
});
