const { NextResponse } = require('next/server');

function middlewareAdmin(req) {
  console.log('Admin Middleware executed');

  const adminRoutes = [
    '/admin-dashboard',
    '/survey-data',
    '/view-imagesets',
    '/ratingdata-page',
  ];

  const adminToken = req.cookies.get('adminToken');
  console.log("adminToken in Middleware:", adminToken);

  if (adminRoutes.includes(req.nextUrl.pathname) && !adminToken && req.nextUrl.pathname !== '/admin-login') {
    console.log("Redirecting to /admin-login (No adminToken)");
    return NextResponse.redirect(new URL('/admin-login', req.url));
  }

  return NextResponse.next();
}

module.exports = { middlewareAdmin };
