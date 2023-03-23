# Testing

Back to Readme [here](README.md)

# Table Of Contents

- [Python Unit Testing](#python-unit-testing)
- [HTML Validation Testing](#html-validation-testing)
- [CSS Validation Testing](#css-validation-testing)
- [JS Validation Testing](#js-validation-testing)
- [Python Validation Testing]((#python-validation-testing))
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

