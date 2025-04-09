import { render, screen, waitFor } from '@testing-library/react';
import { expect, test } from 'vitest';
import Page from '../../app/page';

test('renders page with heading', async () => {
  render(<Page />);
  
  // Check if the description is displayed
  expect(screen.getByText(/Help us discover the most aesthetically pleasing images/i)).toBeTruthy();
});
