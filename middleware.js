const { middlewareSurvey } = require('./middlewareSurvey');
const { middlewareAdmin } = require('./middlewareAdmin');
const { NextResponse } = require('next/server');

function middleware(req) {
  console.log('Global Middleware executed');

  // Apply Survey Middleware for user routes
  const userPaths = ['/rate-images', '/image-gen', '/user-dashboard', '/results-page', '/edit-survey'];
  if (userPaths.some(path => req.nextUrl.pathname.startsWith(path))) {
    const response = middlewareSurvey(req);
    if (response) return response;
  }

  // Apply Admin Middleware for admin routes
  const adminPaths = ['/admin-dashboard', '/survey-data', '/view-imagesets', '/ratingdata-page'];
  if (adminPaths.some(path => req.nextUrl.pathname.startsWith(path))) {
    const response = middlewareAdmin(req);
    if (response) return response;
  }

  return NextResponse.next();
}

module.exports = { middleware };

// Specify the paths where the middleware should apply
module.exports.config = {
  matcher: [
    '/rate-images/:path*', 
    '/image-gen/:path*', 
    '/user-dashboard/:path*', 
    '/results-page/:path*', 
    '/edit-survey/:path*', 
    '/admin-dashboard/:path*', 
    '/survey-data/:path*', 
    '/view-imagesets/:path*', 
    '/ratingdata-page/:path*'
  ],
};
