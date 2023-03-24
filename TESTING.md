# Testing

Back to Readme [here](README.md)

# Table Of Contents

- [Python Unit Testing](#python-unit-testing)
- [HTML Validation Testing](#html-validation-testing)
- [CSS Validation Testing](#css-validation-testing)
- [JS Validation Testing](#js-validation-testing)
- [Python Validation Testing](#python-validation-testing)
- [Lighthouse Testing](#lighthouse-testing)
- [User Testing](#user-testing)

<br>

___

## Python Unit Testing

Unit Testing coverage rounded to 100%.
![Home Unit Tests](readme-assets/testing/python/total-border.png)

<br>
See below for details on each app:

<details>
      <summary style="font-weight:bold">Home App</summary>
   
Home app covered to 100%:

![Home Unit Tests](readme-assets/testing/python/home.png)<br>

___

</details>

<details>
      <summary style="font-weight:bold">Diary App</summary>

Diary app covered to 100%:

![Diary Unit Tests](readme-assets/testing/python/diary.png)<br>

___

</details>

<details>
      <summary style="font-weight:bold">To-Do List App</summary>

To-Do List app covered to 100%:

![To-Do List Unit Tests](readme-assets/testing/python/to-do-list.png)<br>

___

</details>

<details>
      <summary style="font-weight:bold">User Profile App</summary>

User Profile app covered to 100%:

![User Profile App Unit Tests](readme-assets/testing/python/user-profile.png)<br>

___

</details>

<details>
      <summary style="font-weight:bold">Site Updates App</summary>

Site Updates app covered to 100%:

![Site Updates App Unit Tests](readme-assets/testing/python/site-updates.png)<br>

___

</details>

<details>
      <summary style="font-weight:bold">Travel App Views</summary>

Travel App Views covered to 78%:

![Travel App Views Unit Tests](readme-assets/testing/python/travel-app.png)

Error pages 404 was unit tested and 403 was also covered by other unit testing.

Error pages 400 and 500 were not unit tested but were manually tested in User Tesing. 

In addition to unit testing error pages 404 and 403 were also tested manually in User Tesing.
<br>

___

</details>

<details>
      <summary style="font-weight:bold">Travel App Settings</summary>

Travel App Settings covered to 98%:

![Travel App Settings Unit Tests](readme-assets/testing/python/settings.png)

Unit testing was all run through sqlite3 and no access was granted for ElephantSQL therfore this line could not be covered.

<br>

___

</details>

<details>
      <summary style="font-weight:bold">Manage.py</summary>

Manage.py covered to 83%:

![Manage.py Unit Tests](readme-assets/testing/python/manage.png)

Unit testing did not cover except ImportError. This has no negative impact on functionality.

<br>

</details>

___


## HTML Validation Testing

See below html validation results for each page:

<details>
      <summary style="font-weight:bold">Home</summary>
<br>

Login:

![Login](readme-assets/testing/html/home/login.png)

___

Login Required:

![Login Required](readme-assets/testing/html/home/login-required.png)

___

Register:

![Register](readme-assets/testing/html/home/register.png)

___

Home:

![Home](readme-assets/testing/html/home/home.png)

___

Password Reset:

![Password Reset](readme-assets/testing/html/home/password-reset.png)

___

Password Email Sent

![Password Email Sent](readme-assets/testing/html/home/password-email-sent.png)

___

Password Reset Set Password

![Password Reset Set Password](readme-assets/testing/html/home/password-reset-set-password.png)

___

Password Reset Confirmation

![Password Reset Confirmation](readme-assets/testing/html/home/password-reset-confirmation.png)

___

</details>

<details>
      <summary style="font-weight:bold">Planner</summary>
<br>

Map:

![Map](readme-assets/testing/html/planner/map.png)

___

Country Info:

![Country Info](readme-assets/testing/html/planner/country-info.png)

___

Diary Posts:

![Diary Posts](readme-assets/testing/html/planner/diary-post.png)

___

Add / Update Diary:

![Add / Update Diary](readme-assets/testing/html/planner/add-diary.png)

___

Delete Diary:

![Delete Diary](readme-assets/testing/html/planner/diary-delete.png)

___

Diary Tags:

![Diary Tags:](readme-assets/testing/html/planner/tags.png)

___

</details>

<details>
      <summary style="font-weight:bold">To-Do List</summary>
<br>

Add To-Do List:

![Add To-Do List:](readme-assets/testing/html/to-do-list/add-to-do-list.png)

___

Update To-Do List:

![Update To-Do List:](readme-assets/testing/html/to-do-list/update-to-do-list.png)

___

To-Do List Items:

![To-Do List Items:](readme-assets/testing/html/to-do-list/to-do-items.png)

___

</details>

<details>
      <summary style="font-weight:bold">Profile</summary>
<br>

Profile:

![Profile:](readme-assets/testing/html/profile/profile.png)

___

Profile Update:

![Profile Update:](readme-assets/testing/html/profile/update-profile.png)

___

</details>

<details>
      <summary style="font-weight:bold">Site Updates</summary>
<br>

Site Updates:

![Site Updates:](readme-assets/testing/html/site-updates/site-updates.png)

___

Site Update Detail:

![Site Update Detail:](readme-assets/testing/html/site-updates/site-update-detail.png)

___

Add / Update Comment:

![Add/Update Comment:](readme-assets/testing/html/site-updates/update-comment.png)

___

Delete Comment:

![Delete Comment:](readme-assets/testing/html/site-updates/confirm-comment-delete.png)

___

</details>

___

## CSS Validation Testing

<details>
      <summary style="font-weight:bold">Main</summary>
<br>

![Main](readme-assets/testing/css/css-main.png)<br>

___

</details>

<details>
      <summary style="font-weight:bold">Login</summary>
<br>

![Login](readme-assets/testing/css/css-login.png)<br>

___

</details>

<details>
      <summary style="font-weight:bold">White Background</summary>
<br>

![White Background](readme-assets/testing/css/css-white-bg.png)<br>

___

</details>

<details>
      <summary style="font-weight:bold">Off-White Background</summary>
<br>

![Off-White Background](readme-assets/testing/css/css-off-white-bg.png)<br>

___

</details>

<details>
      <summary style="font-weight:bold">Site Update Grey Background</summary>
<br>

![Site Update Grey Background](readme-assets/testing/css/css-update-grey-bg.png)<br>

</details>

___

## JS Validation Testing

<details>
      <summary style="font-weight:bold">JSHint Validations</summary>
<br>
   
No Errors idendified in JSHint:

![JSHint:](readme-assets/testing/js/js-validation.png)

___

</details>

___

## Python Validation Testing

<details>
      <summary style="font-weight:bold">Home</summary>
<br>
   
Views:

![Views](readme-assets/testing/python-pep8/home/home-views.png)

___

URLs:

![URLs](readme-assets/testing/python-pep8/home/home-urls.png)

___

Forms:

![Forms](readme-assets/testing/python-pep8/home/home-urls.png)

___

</details>

<details>
      <summary style="font-weight:bold">Home Unit Tests</summary>
<br>
   
Views:

![Views](readme-assets/testing/python-pep8/home-test/home-test-views.png)

___

URLs:

![URLs](readme-assets/testing/python-pep8/home-test/home-test-urls.png)

___

Forms:

![Forms](readme-assets/testing/python-pep8/home-test/home-test-forms.png)

___

</details>

<details>
      <summary style="font-weight:bold">Diary</summary>
<br>
   
Views:

![Views](readme-assets/testing/python-pep8/diary/diary-view.png)

___

URLs:

![URLs](readme-assets/testing/python-pep8/diary/diary-urls.png)

___

Forms:

![Forms](readme-assets/testing/python-pep8/diary/diary-form.png)

___

Models:

![Models](readme-assets/testing/python-pep8/diary/diary-models.png)

___

</details>

<details>
      <summary style="font-weight:bold">Diary Unit Tests</summary>
<br>
   
Views:

![Views](readme-assets/testing/python-pep8/diary-test/diary-test-views.png)

___

URLs:

![URLs](readme-assets/testing/python-pep8/diary-test/diary-test-urls.png)

___

Models:

![Models](readme-assets/testing/python-pep8/diary-test/diary-test-models.png)

___

</details>

<details>
      <summary style="font-weight:bold">Profile</summary>
<br>
   
Views:

![Views](readme-assets/testing/python-pep8/profile/profile-views.png)

___

URLs:

![URLs](readme-assets/testing/python-pep8/profile/profile-urls.png)

___

Models:

![Models](readme-assets/testing/python-pep8/profile/profile-models.png)

___

Signals:

![Signals](readme-assets/testing/python-pep8/profile/profile-signals.png)

___

Forms:

![Forms](readme-assets/testing/python-pep8/profile/profile-forms.png)

___

</details>

<details>
      <summary style="font-weight:bold">Profile Unit Tests</summary>
<br>
   
Views:

![Views](readme-assets/testing/python-pep8/profile-test/profile-test-views.png)

___

URLs:

![URLs](readme-assets/testing/python-pep8/profile-test/profile-test-urls.png)

___

Models:

![Models](readme-assets/testing/python-pep8/profile-test/profile-test-models.png)

___

</details>

<details>
      <summary style="font-weight:bold">Site Updates</summary>
<br>
   
Views:

![Views](readme-assets/testing/python-pep8/site-updates/site-updates-views.png)

___

URLs:

![URLs](readme-assets/testing/python-pep8/site-updates/site-updates-urls.png)

___

Models:

![Models](readme-assets/testing/python-pep8/site-updates/site-updates-models.png)

___

Forms:

![Models](readme-assets/testing/python-pep8/site-updates/site-updates-forms.png)

___

</details>

<details>
      <summary style="font-weight:bold">Site Updates Unit Tests</summary>
<br>
   
Views:

![Views](readme-assets/testing/python-pep8/site-updates-test/site-updates-test-views.png)

___

URLs:

![URLs](readme-assets/testing/python-pep8/site-updates-test/site-updates-test-urls.png)

___

Models:

![Models](readme-assets/testing/python-pep8/site-updates-test/site-updates-test-models.png)

___

Forms:

![Models](readme-assets/testing/python-pep8/site-updates-test/site-updates-test-forms.png)

___

</details>

<details>
      <summary style="font-weight:bold">To-Do List</summary>
<br>
   
Views:

![Views](readme-assets/testing/python-pep8/to-do-list/to-do-list-views.png)

___

URLs:

![URLs](readme-assets/testing/python-pep8/to-do-list/to-do-list-urls.png)

___

Models:

![Models](readme-assets/testing/python-pep8/to-do-list/to-do-list-models.png)

___

Forms:

![Forms](readme-assets/testing/python-pep8/to-do-list/to-do-list-forms.png)

___

</details>

<details>
      <summary style="font-weight:bold">To-Do List Unit Tests</summary>
<br>
   
Views:

![Views](readme-assets/testing/python-pep8/to-do-list-test/to-do-list-test-views.png)

___

URLs:

![URLs](readme-assets/testing/python-pep8/to-do-list-test/to-do-list-test-urls.png)

___

Models:

![Models](readme-assets/testing/python-pep8/to-do-list-test/to-do-list-test-models.png)


</details>

___

## Lighthouse Testing

<details>
      <summary style="font-weight:bold">All Lighthouse Scores</summary>

Login:

![Login](readme-assets/testing/lighthouse/lighthouse-login.png)<br>

___

Register:

![Register](readme-assets/testing/lighthouse/lighthouse-register.png)<br>

___

Profile:

![Profile](readme-assets/testing/lighthouse/lighthouse-profile.png)<br>

___

Home:

![Home](readme-assets/testing/lighthouse/lighthouse-home.png)<br>

___

Map:

![Map](readme-assets/testing/lighthouse/lighthouse-map.png)<br>

___

Country Info:

![Country Info](readme-assets/testing/lighthouse/lighthouse-country-info.png)<br>

___

Forms:

![Forms](readme-assets/testing/lighthouse/lighthouse-form.png)<br>

___

List Items:

![List Items](readme-assets/testing/lighthouse/lighthouse-list-items.png)<br>

___

Diary:

![Diary](readme-assets/testing/lighthouse/lighthouse-diary.png)<br>

___

Diary Tags:

![Diary Tags](readme-assets/testing/lighthouse/lighthouse-dairy-tags.png)<br>

___

Site Updates:

![Site Updates](readme-assets/testing/lighthouse/lighthouse-site-updates.png)<br>

___

Update Detail:

![Update Detail](readme-assets/testing/lighthouse/lighthouse-update-detail.png)<br>

___

</details>

___


## User Testing

### User Stories Acceptance Criteria
Each User Story documented (as an issue) in the Project Iterations [here](https://github.com/Joe-Collins-1986?query=is%3Aclosed&tab=projects) has Acceptance Criteria documented on GitHub which needed to be achieved before marking the User Sory to complete.

To view these access the User Story Issues in Iterations 1-5

Example Screenshot of Iteration On GitHub:

![Example Screenshot Of an Iteration](readme-assets/testing/user-testing/user-stories/kanban.png)

Example Screenshot of User Story in Iteration:

![Example Screenshot Of a User Story](readme-assets/testing/user-testing/user-stories/user-story.png)

### User Testing Checklist

In addition to the User Story Acceptance Criteria a checklist was developed to check each page after all features were developed prior to sharing project content.

To record this checklist [tabletomarkdown.com](https://tabletomarkdown.com/convert-spreadsheet-to-markdown/) was used to quickly convert data to Markdown Tables tables.

<details>
      <summary style="font-weight:bold">Navbar</summary>
<br>
   
| REF | TEST         | EXPECTATION                                                                      | Pass/Fail |
| --- | ------------ | -------------------------------------------------------------------------------- | --------- |
| A1  | Logo         | Directed to Home page if logged in, Login page in not.                           | P         |
| A2  | Home         | Directed to Home page if logged in, Login page in not.                           | P         |
| A3  | Planner      | Directed to Map page if logged in, Login Required page in not.                   | P         |
| A4  | Site Updates | Directed to Site Updates page if logged in or not.                               | P         |
| A5  | Login        | Only shown if user is not logged in. Direct to Login page.                       | P         |
| A6  | Register     | Only shown if user is not logged in. Direct to Register page.                    | P         |
| A7  | Profile      | Only shown if user is logged in. Direct to Profile page.                         | P         |
| A8  | Logout       | Only shown if user is logged in. Logs user out and directs to Login page.        | P         |
| A9  | Admin        | Only shown if user is logged in with a Superuser account. Directs to Admin page. | P         |

___

</details>

<details>
      <summary style="font-weight:bold">Footer/Menu Social Media Links</summary>
<br>
   
**Note:** The client is fictional and therefore the social sites do not exist so the footer links will only take the user to the overall social media site specified e.g. twitter.

| REF | TEST                      | EXPECTATION                                                                                                                 | Pass/Fail |
| --- | ------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------- |
| B1  | Facebook                  | Shows if logged in or not. Directed to Facebook - but not to client account as this does not exist.                         | P         |
| B2  | Instagram                 | Shows if logged in or not. Directed to Instagram - but not to client account as this does not exist.                        | P         |
| B3  | Twitter                   | Shows if logged in or not. Directed to Twitter - but not to client account as this does not exist.                          | P         |
| B4  | Pinterest                 | Shows if logged in or not. Directed to Pinterest - but not to client account as this does not exist.                        | P         |
| B5  | Expandable Menu Facebook  | Shows if logged in or not when menu is expanded. Directed to Facebook - but not to client account as this does not exist.   | P         |
| B6  | Expandable Menu Instagram | Shows if logged in or not when menu is expanded.  Directed to Instagram - but not to client account as this does not exist. | P         |
| B7  | Expandable Menu Twitter   | Shows if logged in or not when menu is expanded. Directed to Twitter - but not to client account as this does not exist.    | P         |
| B8  | Expandable Menu Pinterest | Shows if logged in or not when menu is expanded. Directed to Pinterest - but not to client account as this does not exist.  | P         |

___

</details>

<details>
      <summary style="font-weight:bold">Register</summary>
<br>
   
| REF | TEST                               | EXPECTATION                                                                 | Pass/Fail |
| --- | ---------------------------------- | --------------------------------------------------------------------------- | --------- |
| C1  | Blank Username                     | Notified field required.                                                    | P         |
| C2  | Pre-Existing Username              | Notified username already exists and new name needed.                       | P         |
| C3  | Invalid Username                   | Field highlighted and instruction text highlighted.                         | P         |
| C4  | Blank Email                        | Notified field required.                                                    | P         |
| C5  | Invalid Email                      | Notified why email is not acceptable.                                       | P         |
| C6  | Invalid Password                   | Notified why password is not acceptable.                                    | P         |
| C7  | Blank Confirmation                 | Notified field required.                                                    | P         |
| C8  | Non Matching Password Confirmation | Notified passwords do not match.                                            | P         |
| C9  | Sign Up Button                     | Submits the form - if valid directed to home. No additional login required. | P         |
| C10 | Sign In Link                       | Directed to Login Page.                                                     | P         |

___

</details>

<details>
      <summary style="font-weight:bold">Login and Login Required</summary>
<br>
   
| REF | TEST                  | EXPECTATION                                                                                                          | Pass/Fail |
| --- | --------------------- | -------------------------------------------------------------------------------------------------------------------- | --------- |
| D1  | Blank Username        | Notified field required.                                                                                             | P         |
| D2  | Blank Password        | Notified field required.                                                                                             | P         |
| D3  | Invalid Password/User | Notified password does not link to username.                                                                         | P         |
| D4  | Sign In Button        | Submits the form - if valid directed to home or the page the user tried to access when redirected to login required. | P         |
| D5  | Sign Up Link          | Directed to Register page.                                                                                           | P         |
| D6  | Password Reset        | Directed to Password Reset page.                                                                                     | P         |

___

</details>

<details>
      <summary style="font-weight:bold">Password Reset</summary>
<br>
   
Test the full Reset password process across all relevent pages.

| REF | TEST                                                  | EXPECTATION                                                                                                     | Pass/Fail                                                                                                                                                                                                                                                                                                                      |
| --- | ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| E1  | Email Blank                                           | Notified field required.                                                                                        | P                                                                                                                                                                                                                                                                                                                              |
| E2  | Invalid Email                                         | Notified why email is not acceptable.                                                                           | P                                                                                                                                                                                                                                                                                                                              |
| E3  | Sign Up Link                                          | Directed to Register page.                                                                                      | P                                                                                                                                                                                                                                                                                                                              |
| E4  | Email Success On Valid Email                          | Success Email Screen Shown.                                                                                     | P                                                                                                                                                                                                                                                                                                                              |
| E5  | Email Success page Password Reset Link                | Directed to back to password reset provide email page.                                                          | P                                                                                                                                                                                                                                                                                                                              |
| E6  | Email Success Sign Up Link                            | Directed to Login page.                                                                                         | P                                                                                                                                                                                                                                                                                                                              |
| E7  | Password Reset Email Received                         | Email with link to reset page is received and link directs to reset password page.                              | P - Note BT Internet has placed restriction against spam emails which can effect BT Internet email address oweners getting the reset email.<br><br>If this was to be established as a commercial website BT could be contacted and registered with to stop this occuring.<br><br>Other email providers worked fine in testing. |
| E8  | On Reset page Blank Password or Password Confirmation | Notified field required.                                                                                        | P                                                                                                                                                                                                                                                                                                                              |
| E9  | On Reset page Invalid Password                        | Notified why password is not acceptable.                                                                        | P                                                                                                                                                                                                                                                                                                                              |
| E10 | On Reset page Non Matching Password Confirmation      | Notified passwords do not match.                                                                                | P                                                                                                                                                                                                                                                                                                                              |
| E11 | Password Reset - Password Reset Button                | On successful completion button directs to Password Updated page with link to Login page Via Sign In Here link. | P                                                                                                                                                                                                                                                                                                                              |

___

</details>

<details>
      <summary style="font-weight:bold">Summary Site Updates</summary>
<br>
   
Summary Site Updates section that appears on the bottom of Register, Login, Login Required, Password Resets and Home pages.

| REF | TEST                     | EXPECTATION                                                                                                                                                 | Pass/Fail |
| --- | ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| F1  | 3 Updates                | Page shows latest 3 updates.                                                                                                                                | P         |
| F2  | Hover on Update          | Update goes blue on hover.                                                                                                                                  | P         |
| F3  | Select Update Or Comment | If logged in directed to Update Detail page, if not logged in directed to Login Required page. Then after login go straight to Update Detail page. (See D4) | P         |
| F4  | See All Updates Button   | If logged in or not logged in direct to Site Updates posts page.                                                                                            | P         |

___

</details>


<details>
      <summary style="font-weight:bold">Home</summary>
<br>
   
| REF | TEST                 | EXPECTATION                                                                                                                                      | Pass/Fail |
| --- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | --------- |
| G1  | Parallax Image       | Parallax on image scroll. Content move at different speeds - moutains, trees, welcome text.                                                      | P         |
| G2  | Arrow Flash          | Arrow flashing on load to direct users to scroll.                                                                                                | P         |
| G3  | Planner Button       | If logged in planner button directs to Map page. If not logged in direcs to Login Required page then on completion directs to Map page. (See D4) | P         |
| G4  | Site Updates Section | See Summary Updates. F1-F4                                                                                                                       | P         |                                                                                          | P         |

___

</details>

<details>
      <summary style="font-weight:bold">Map</summary>
<br>
   
| REF | TEST                                     | EXPECTATION                                                                                                                                                                                 | Pass/Fail |
| --- | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| H1  | Hover Over Countries                     | The country name appears in the top right corner when hovering over the country on the map.                                                                                                 | P         |
| H2  | Select Map Country                       | Directs to Country Info page when a country is selected on the map.                                                                                                                         | P         |
| H3  | Country Dropdown Alphabetical            | All country dropdown country options appear in alphabetical order.                                                                                                                          | P         |
| H4  | Select Dropdown Country                  | Directs to Country Info page when a country is selected on all countries dropdown.                                                                                                          | P         |
| H5  | Country Status Updated - Map Update      | When a country status is updated on the Country Info page and the Map page is returned to the country on the map shows in a different colour - green- wish list or yellow - visited.        | P         |
| H6  | Country Status Updated - Dropdown Update | When a country status is updated on the Country Info page and the Map page is returned dropdowns appear for visited or wish list if the user has set these statuses on at least on country. | P         |
| H7  | Visit/Wish List Disappears               | If the user changes the status to no longer have any wish list or visited countries the respective dropdown will disappear.                                                                 | P         |
| H8  | Select Visit or Wish List Dropdown       | Directs to Country Info page when a country is selected on dropdowns.                                                                                                                       | P         |
| H9  | Pie Chart Shows Header                   | Shows percentage visited. Does not account for wish list.                                                                                                                                   | P         |
| H10 | Pie Chart                                | Pie Chart reflects the number of wish lists, visited and not visted countries with the respective colour to align with the legend.                                                          | P         |
| H11 | Pie Chart - Small Screen                 | The Pie Chart disappears for small screens.                                                                                                                                                 | P         |

___

</details>

<details>
      <summary style="font-weight:bold">Country Info</summary>
<br>
   
| REF | TEST                        | EXPECTATION                                                                                                                                                    | Pass/Fail |
| --- | --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| I1  | Back Button                 | The globe icon on the top left of the screen is fixed to always show and directs back to the Map page.                                                         | P         |
| I2  | Country Flag                | The country selected shows the correct flag.                                                                                                                   | P         |
| I3  | Header Image                | The country selected shows the correct header image.                                                                                                           | P         |
| I4  | About                       | The country selected shows the correct about info.                                                                                                             | P         |
| I5  | Info Stats                  | The country selected shows the correct info stats (Capital, Currency, Language, Population).                                                                   | P         |
| I6  | Visited Selected            | Visited form defaults to 'Not Visited' until the user selects a status for the country and provides a dropdown list of 'Not Visited', 'Visited' & 'Wish List'. | P         |
| I7  | Visited Selected Re-Visited | The status remains from previous selection when re-visited the country.                                                                                        | P         |
| I8  | Visited Selected Submit     | When visited is selected and submitted the page returns to the visited status form and shows the applied status.                                               | P         |
| I9  | Visited Updates Map Colour  | See H5.                                                                                                                                                        | P         |
| I10 | Add To-Do List              | Add To-Do List button directs to Add To-Do List form.                                                                                                          | P         |
| I11 | Select To-Do List Title     | Directs to task To-Do List Item Manager page.                                                                                                                  | P         |
| I12 | Edit To-Do List             | Add To-Do List button directs to Add To-Do List form.                                                                                                          | P         |
| I13 | To-Do List Order            | To Do Lists are ordered by created date. The order is not ammended by update.                                                                                  | P         |
| I14 | Delete To-Do List           | Deletes To-Do List  and returns to the To-Do List  section. No confirmation required.                                                                          | P         |
| I15 | View Diary Button           | Directs to the Diary page.                                                                                                                                     | P         |

___

</details>

<details>
      <summary style="font-weight:bold">Add To-Do List Form / Edit To-Do List Form</summary>
<br>
   
| REF | TEST                 | EXPECTATION                                                                                                                                                       | Pass/Fail |
| --- | -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| J1  | Title Blank          | Notified field required.                                                                                                                                          | P         |
| J2  | Description Optional | Form can be submitted with or without a description.                                                                                                              | P         |
| J3  | Cancel Button        | Directs back to Country Info page for correct country and navigates back to To-Do List section.                                                                   | P         |
| J4  | Submit Button        | On valid form - adds/edits To-Do List and directs back to Country Info page for correct country and navigates back to To-Do List section showing new/edited list. | P         |
| J5  | Edit To-Do List      | Existing content is populated in fields.                                                                                                                          | P         |

___

</details>

<details>
      <summary style="font-weight:bold">To-Do List Items Manager</summary>
<br>
   
| REF | TEST                            | EXPECTATION                                                                                              | Pass/Fail |
| --- | ------------------------------- | -------------------------------------------------------------------------------------------------------- | --------- |
| K1  | Title                           | Title is for the selected To-Do List.                                                                    | P         |
| K2  | Description                     | Description is for the selected To-Do List. If no description added only the title shows.                | P         |
| K3  | Add New Task Form - Blank Entry | Notified field required.                                                                                 | P         |
| K4  | Back Button                     | Directs back to Country Info page for correct country and navigates back to To-Do List section.          | P         |
| K5  | Add Button                      | Creates a item and presents it at the top to the page.                                                   | P         |
| K6  | List Item Order                 | List items presented in the order they were created.                                                     | P         |
| K7  | Close Button On Item            | Put a line through the item title, darkens the item box and moves the item  below the open items.        | P         |
| K8  | Open Button On Item             | Resets the original formatting and moves the item back to it's original position above all closed items. | P         |
| K9  | Delete Button On Item           | Deletes the item. No confirmation required.                                                              | P         |

___

</details>