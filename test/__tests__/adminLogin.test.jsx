// src/app/__tests__/adminLogin.test.jsx
import { expect, test } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import AdminLogin from '../../app/admin-login/page';
import Navbar from '../../app/components/Navbar';
import { useRouter } from 'next/navigation';

vi.mock('next/navigation', () => ({
  useRouter: () => ({
    push: vi.fn(),
  }),
}));

test('AdminLogin Page', () => {
  render(<AdminLogin />);

  // Check if the "Admin Login" header is displayed
  expect(screen.getByRole('heading', { name: /Admin Login/i })).toBeDefined();

  // Check if the "Username" input field is displayed
  expect(screen.getByLabelText(/Username/i)).toBeDefined();

  // Check if the "Password" input field is displayed
  expect(screen.getByLabelText(/Password/i)).toBeDefined();

  // Check if the "Login" button is displayed
  expect(screen.getByTestId('loginButton')).toBeDefined();
});

test('Navbar displays Sign Out button when isAdmin is true', () => {
  const mockSignOut = vi.fn();

  render(<Navbar isAdmin={true} onSignOut={mockSignOut} />);

  // Check if the "Sign Out" button is displayed
  const signOutButton = screen.getByRole('button', { name: /Sign Out/i });
  expect(signOutButton).toBeInTheDocument();

  // Simulate clicking the "Sign Out" button
  fireEvent.click(signOutButton);

  // Ensure the sign-out function is called
  expect(mockSignOut).toHaveBeenCalledTimes(1);
});