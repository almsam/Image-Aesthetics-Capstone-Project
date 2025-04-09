import { defineConfig } from 'vitest/config';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  test: {
    environment: 'jsdom',
    globals: true,
    include: ['test/**/*.test.jsx'],  // or use a more specific pattern if needed
    exclude: ['e2eTests/**/*'],       // Exclude Playwright tests
  },
});
