

### Current Tasks (Provide sufficient detail)
  * #1: Launch front-end: Using React.js+Next.js, I setup a webapp which we will be using for this project. This is an initial setup, so it's rather simplistic, however over the next weeks, I will enhance design, implement routing, and add various pages (such as login/signup, a seperate user profile page, etc)
  * #2: Choose front-end testing frameworks and implement front-end tests: After researching, I chose vitest over Jest due to some babel dependencies causing errors in my system. Vitest seems to be a flexible framework and sicne I have worked with it earlier, I think it will work well for our current project.
  * #3: Project-proposal: Brainstormed about proposed solution and finalised our tech stack in Requirements, Testing, Requirement Verification.

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
</table>

### Cycle Goal Review (Reflection: what went well, what was done, what didn't; Retrospective: how is the process going and why?)
I completed Task A as planned, but there was some confusion which is also mentioned in a PR because there were 5000+ files changes, which was due to the duplication of a package-lock.json file (this issue will be resolved in the next couple of days). Task B took a significant amount of time, due to quite a few errors caused by dependencies (specifically while using Jest which requires babel). This led to me switching to vitest which led to me completing Task B (Front-end tests). An issue I faced with task B was that I couldn't test a component on my frontend as to test it thoroughly we would need a db connection setup (which couldn't be done due to time constraints and this will be done in teh next sprint). Task C was done after a discussion within our group to try find the most comfortable tech stack for each of us and we ensured our project proposal was the best possible solution while also being achievable.

### Next Cycle Goals (What are you going to accomplish during the next cycle)
  * Goal 1: Implement login/signup functionality:  Over the next sprint, we will add a login and signup page which will have full functionality and will store user info in our database. 
  * Goal 2: Establish a connection with our database, and store/fetch user ratings of different images.
  * Goal 3: Create a user profile page, with their user details, and if time permits, a list of their highest rated images.