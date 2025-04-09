// @ts-check
import { test, expect } from '@playwright/test';

test.describe('Navigation Tests', () => {

  test('should navigate from homepage to admin login page', async ({ page }) => {
    // Navigate to the homepage
    await page.goto('http://localhost:3001'); // Replace with your homepage URL if needed

    // Click on the Admin Login button
    await page.click('[data-testid="NavLoginButton"]');

    // Expect the URL to be the admin login page
    await expect(page).toHaveURL("http://localhost:3001/admin-login");

    // Check for a specific element on the admin login page to confirm navigation
    await expect(page.getByRole('heading', { name: 'Admin Login' })).toBeVisible();
  });

  test('should navigate from homepage to consent page', async ({ page }) => {
    // Navigate to the homepage
    await page.goto('http://localhost:3001'); // Replace with your homepage URL if needed

    // Click on the Take Survey button
    await page.click('button:text("Take Survey")'); // Adjust this selector as needed

    // Expect the URL to be the survey page
    await expect(page).toHaveURL("http://localhost:3001/consent-form");

    // Check for a specific element on the survey page to confirm navigation
    await expect(page.getByRole('heading', { name: 'Consent Form' })).toBeVisible();
  });

  test('should navigate from consent page to survey page', async ({ page }) => {
    // Navigate to the consent page directly
    await page.goto('http://localhost:3001/consent-form'); // Replace with your consent URL if needed

    // Click on the I Consent button to go to the survey page
    await page.click('button:text("I Consent")'); // Adjust this selector as needed

    // Expect the URL to be the survey page
    await expect(page).toHaveURL("http://localhost:3001/survey");

    // Check for a specific element on the survey page to confirm navigation
    await expect(page.getByRole('heading', { name: 'User Survey' })).toBeVisible();
  });

  test('should have document title', async ({ page }) => {
    await page.goto('http://localhost:3001');
    const title = await page.title();
    expect(title).toBeTruthy();
  });


});



