const { NextResponse } = require('next/server');

function middlewareSurvey(req) {
  console.log('Survey Middleware executed');

  const isSurveyCompleted = req.cookies.get('isSurveyCompleted');
  const surveyCompletedQuery = req.nextUrl.searchParams.get('surveyCompleted');

  console.log('isSurveyCompleted:', isSurveyCompleted);
  console.log('surveyCompletedQuery:', surveyCompletedQuery);

  if (!isSurveyCompleted && !surveyCompletedQuery) {
    const url = req.nextUrl.clone();
    url.pathname = '/complete-survey';
    url.search = ''; // Clear any query parameters
    return NextResponse.redirect(url);
  }

  return NextResponse.next();
}

module.exports = { middlewareSurvey };
