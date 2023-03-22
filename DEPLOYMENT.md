
# Deployment

Back to Readme [here](README.md)

# Table Of Contents

- [Set Up Local GitHub Repository](#set-up-local-github-repository)
- [Repository Framework](#repository-framework)
- [ElephantSQL Database](#elephantsql-database)
- [AWS For Static Files and Images](#aws-for-static-files-and-images)
- [Gmail](#gmail)
- [Heroku Deployment](#heroku-deployment)
- [Update Repository](#update-repository)

<br>

## Set Up Local GitHub Repository

1. Go to https://github.com/Code-Institute-Org/gitpod-full-template.
2. Select use this template.
3. Add repository name within my GitHub. (This will generate a repository in my Git Hub with the appropriate files.)

## Repository Framework
1. Select the repository on GitHub and open with GitPod (green button).
2. Open GitPod workspace
3. pip3 install 'django<4' gunicorn <br>
4. pip3 install dj_database_url==0.5.0 psycopg2 <br>
5. pip3 freeze –local > requirements.txt
6. django-admin startproject **PROJECT NAME** .<br>
**Note:** (the dot on the end tell Django to create project in the current directory)
7. python3 manage.py startapp **APP NAME**
8. Go to settings located in project directory
9. Add **APP NAME** to installed apps
10. python3 manage.py migrate
11. Run python3 manage.py runserver to check basic skeleton is presenting


## ElephantSQL Database
1. Log in to ElephantSQL.com to access your dashboard
2. Click “Create New Instance”
3. Set up your plan
    * Give your plan a Name (this is commonly the name of the project)
    * Select the Tiny Turtle (Free) plan
    * You can leave the Tags field blank
4. Select “Select Region”
5. Select a data center near you <br>
If you receive a message saying "Error: No cluster available in your-chosen-data-center yet", choose another region.
6. Then click “Review” and then “Create instance”.
7. Return to the ElephantSQL dashboard and click on the database instance name for this project.
8. In the URL section, click the copy icon to copy the database URL to add to Heroku Config Vars.


## AWS For Static Files and Images
1. Create an S3 bucket to store all static files and images by navigating to the S3 dashboard in the AWS console and clicking on the "Create bucket" button.
2. Configure the bucket's permissions to allow public access to the static files and images. This can be done by navigating to the bucket's permissions tab and adding a new policy that grants read access to everyone.
3. Install the boto3 and django-storages packages in the Django project.
4. Update the Django project's settings to use S3 as the storage backend for static files and images. Then user these to update Heroku Config Vars.


## Gmail
1. Navigate to myaccount.google.com/security, scroll down to the Signing Into Google section.
2. Click on App Passwords.
3. Enter Gmail account password.
4. Click on "Select App" and input Django app name.
5. Click Generate.
6. Add generated app password into the EMAIL_HOST_PASSWORD value in your settings.py file and Heroku Config Vars.


## Heroku Deployment
1. In the console enter pip3 freeze > requirements.txt to update the requirements.txt file with necessary modules used in the code.
2. Log in to [Heroku](https://id.heroku.com/login) and create an account.
3. Click 'Create new app' button.
4. Enter a unique name for your app and select your region then click 'Create app'.
5. Go the 'Settings' tab.
6. Click 'Reveal Config Vars'.
7. In the Config Vars enter:

    AWS Environment Variables:
    * AWS_ACCESS_KEY_ID
    * AWS_SECRET_ACCESS_KEY
    * AWS_STORAGE_BUCKET_NAME

    <br>

    ElephantSQL Database Environment Variables:
    * DATABASE_URL

    <br>
    
    Gmail Environment Variables:
    * EMAIL_PASS
    * EMAIL_USER
    
    <br>
    
    Other Environment Variables:
    * PORT
    * DEBUG_VALUE
    * SECRET_KEY

    <br>
    
8. Go to the 'Deploy' tab.
9. Select 'GitHub' as the deployment method and click 'Connect to GitHub'.
10. Search for the GitHub Repository name and hit 'Connect'.
11. Click 'Automatic Deploys' to get Heroku to update automatically when GitPod changes are pushed to GitHub.
12. Click 'Deploy Branch' to launch the project to Heroku for the first time.
13. Click 'View' to go to live app.
14. Run game to test functionality and APIs are working.


## Update Repository
1. When adding a new feature create a separate branch to work in safely typing into the terminal "git branch 'name of required feature/update'".
2. Checkout the branch with "git checkout 'name of required feature/update'".
3. Make updates and test using "python manage.py runserver".
4. Once testing is complete add to Git staging area using "git add ."
5. Commit the changes and add a useful explanation of what action was done to track the history in GitHub using "git commit -m 'explanation of update'".
6. Once the feature is complete, fully tested, and ready to be added to the main branch first go to the main branch using "git checkout main".
7. Merge the feature branch into the main using "git merge 'name of required feature/update'".
8. Confirm merge was successful and then if it is not going to be re-used delete the feature branch using "git branch -d 'name of required feature/update'". (If deleting a branch with commits not merged to main delete with -D instead of -d)
9. Use "git push" to push the commits to GitHub. These will then appear in the live website if Heroku is set to automatic deplyment and linked to my Github.