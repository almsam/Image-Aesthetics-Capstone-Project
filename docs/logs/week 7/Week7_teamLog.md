# Weekly Team Log


## Date Range:

- Week 5 - Week 7
- [6/10/2024] - [20/10/2024]

## Features in the Project Plan Cycle:

1. Admin Login page: Initial design for the login page, so that functionality can start being implemented from the next sprint onwards
2. End-to-end tests and github workflows: Using playwright, an initial end to end test has been created to test user flow and routing in the webapp.
3. Image Database setup: Created a db which stores images, questions, users, and ratings. This will also be used to store information on the users and the ratings they give each image based on the question provided. Also added a github workflows file (.yml) to check the e2e tests before every merge.
4. Backend Functions: Various functions which allow us to fetch/insert data into the different databases have been created. Also various edit data functions have also been added to the backend functions.
5. Machine learning improvements: use a variety of mathematical & data science techniques should allow a much lower error with the CNN.
6. [Add more here]

## Associated Tasks from Project Board:


## Associated Tasks from Project Board:

| Task ID | Description        | Feature   | Assigned To | Status   |
| ------- | ------------------ | --------- | ----------- | -------- |
| 16  | Front End for admin login | Admin Login page | [Devstutya]  | [Complete] |
| 47  | Add appropriate end to end tests | End to end testing | [Devstutya]  | [Complete] |
| 47  | Add github workflows(.yml) file for CI/CD| CI/CD | [Devstutya]  | [Complete] |
| 35  | Create DFD0 and DFD1 | Database| [Zoe] | [Complete] |
| 33  | Database access methods | Database| [Zoe] | [Complete] |
| 30  | Make a python file that expands on preview.py, so we can rate the images | Prototype Python application | [Samira]  | [Complete] |
| 31  | Prove that we can use neural nets this way | Proof of concept CNN | [Samira]  | [Complete] |
| 31  | Make the app start at image i'ds other then 0 | Append CSV in prototype app | [Samira]  | [Complete] |
| 27  | Database for admins | Schema for the admin database. | [Shakthi] | [Complete] |
| 43  | Revamped tables | Changed fields in tables according to the guidelines provided by the client. | [Shakthi] | [Complete] |
| 48  | FastAPI Implementation | Use fastAPI to connect the backend and frontend. | [Shakthi] | [In progress] |
| 34   | Password verification | Back-end/ Database | [Saketh]  | [Complete] |
| 41  | Edit admin details  | Back-end/ Database | [Saketh]  | [Complete] |




### Alternatively, include image of the project board with tasks and status:

## Tasks for Next Cycle:

| Task ID | Description        | Estimated Time (hrs) | Assigned To |
| ------- | ------------------ | -------------------- | ----------- |
| [59]   | Implement functionality for admin login| [4]     | [Devsutya]  |
| [26]   | Create a user profile page, with their user details | [4]     | [Devsutya]  |
| [42]   | Create a user survey page, with the needed survey details | [4]     | [Devsutya]  |
| [55]   | imageDB query methods | [4] | [Zoe] |
| [56]   | imageDB delete methods | [4] | [Zoe] |
| [57]   | export rating data to csv| [4] | [Zoe] |
| [60]   | optimize CNN parameters | [3] | [Samira] |
| [61]   | make a better Pre train process | [3] | [Samira] |
| [62]   | Check the CNN for overfit | [2] | [Samira] |
| [63]   | plot ML paramiters | [2] | [Samira] |
| [48]   | FastAPI implementation | [6] | [Shakthi] |
| [64]   | Utilizing backend code in frontend | [-] | [Shakthi] |
| [45]   | Test db functionality with image ratings | [4]     | [Saketh]  |
| [64]   | Utilizing backend code in frontend | [-] | [Saketh] |



### Alternatively, include image of the project board with tasks and status:

![alt text](KanbanOct20.png "Title")

## Burn-up Chart (Velocity):

- Not required


## Completed Tasks:

| Task ID | Description        | Completed By |
| ------- | ------------------ | ------------ |
| [16]   | [Frontend for Admin login] | [Devstutya]   |
| [47]   | [End to end testing and CI/CD] | [Devstutya]   |
| [35]   | Create DFD0 and DFD1 | [Zoe] | [Complete] |
| [33]   | Database access methods | [Zoe] | [Complete] |
| 27  | Database for admins| [Shakthi] | [Complete] |
| 43  | Revamped tables | [Shakthi] | [Complete] |
| 34   | Password verification | [Saketh]  | [Complete] |
| 41  | Edit admin details  | [Saketh]  | [Complete] |

## In Progress Tasks/ To do:

| Task ID | Description        | Assigned To |
| ------- | ------------------ | ----------- |
| [26]   | Create a user profile page, with their user details | [Devsutya]  |
| [42]   | Create a user survey page, with the needed survey details | [Devsutya]  |
| [55]   | imageDB query methods | [4] | [Zoe] |
| [56]   | imageDB delete methods | [4] | [Zoe] |
| [57]   | export rating data to csv| [4] | [Zoe] |
| [48]   | FastAPI implementation | [6] | [Shakthi] |
| [45]   | Test db functionality with image ratings  | [Saketh]  |
| [64]   | Utilizing backend code in frontend | [Saketh] |

## Test Report / Testing Status:

All tests for features added this sprint are passing.

## Overview:

The team focused on making progress in the first few major features of the webapp for the project. These features include Admin login, and soon we will be working on implement image rating functionality, The Kanban Board has been populated with tasks, milestones have been added, and the dashboard visuals creation has been completed. The next cycle will focus on establishing a connection between our frontend and backend and completing at least 2 major features of our webapp.
