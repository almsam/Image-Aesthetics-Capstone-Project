

### Current Tasks (Provide sufficient detail)
  * #1: Add admin login page: Using next.js, I added an admin login page where admin can provide their username and password (username being an email address) to login.
  * #2: Implement Routing: Routing has been implemented for the home page and the admin login page.
  * #3: Add End to end testing and CI/CD: After researching, I chose playwright for end to end testing, and I created an end to end test to check user flow from the homepage to the admin login and vice versa. Also added a github workflows file (.yml) to check the e2e tests before every merge.
  * #4: Webapp functionality: Brainstormed about integration of frontend and backend in order to test functionality. We want to implement fastAPI to integrate our frontend and backend with ease, but initially for testing purposes we may test functionality without fastAPI to check whether db functionality is running as intended.

### Progress Update (since 6/5/2024) 
<table>
    <tr>
        <td><strong>TASK/ISSUE #</strong>
        </td>
        <td><strong>STATUS</strong>
        </td>
    </tr>
    <tr>
        <!-- Task/Issue # -->
        <td>Task A
        </td>
        <!-- Status -->
        <td>Complete
        </td>
    </tr>
    <tr>
        <!-- Task/Issue # -->
        <td>Task B
        </td>
        <!-- Status -->
        <td>Complete
        </td>
    </tr>
    <tr>
        <!-- Task/Issue # -->
        <td>Task C
        </td>
        <!-- Status -->
        <td>Complete
        </td>
    </tr>
    <tr>
        <!-- Task/Issue # -->
        <td>Task D
        </td>
        <!-- Status -->
        <td>In progress
        </td>
    </tr>
</table>

### Cycle Goal Review (Reflection: what went well, what was done, what didn't; Retrospective: how is the process going and why?)
I completed Task A and Task B as planned, but in task B I faced a couple errors due to unclean installation of dependencies which was sorted pretty quickly. Task C was done after a discussion within our group and the TA to try test the user flow within a feature of our webapp using end to end testing. Creating this test was a little tricky as I am new to playwright but I got it up and running with a worklows (.yml) file which will run the playwright tests everytime a change is comitted github. To get this .yml to not throw an error while merging branches I had to figure out how to automatically run the local server on every playwright test, and figuring this out took a whole day as well, but it was completed nonetheless. Finally Task D, where our group had a discussion on whether to use an RestAPI or not, we came to the conclusion that we should be using fastAPI for the benefits it brings to the project (as we're using python backend and Next.js frontend) and the ease of handling frontend-backend interactions, but due to a lack of time this wasn't implemented this week. This also delayed the testing of webapp functionality, which is why a subgroup of our team is going to start working on FastAPI and the remaining subgroup will start checking functionality without fastAPI (just to ensure our python backend functions and SQLite db are running as intended). Overall I would say I had a pretty productive cycle, and although there was a slight delay in the issue completion due to midterms, the most important front-end tasks were completed. 

### Next Cycle Goals (What are you going to accomplish during the next cycle)
  * Goal 1: Implement admin login functionality:  Over the next sprint, we will add functionality to the admin login which will store and fetch user info using our SQLite database. 
  * Goal 2: Create a FastAPI backend, to integrate Next.js frontend and the python backend
  * Goal 3: Establish a connection with our database, and store/fetch ratings of different images.
  * Goal 4: Create a user profile page, with their user details, and if time permits, a list of their highest rated images.