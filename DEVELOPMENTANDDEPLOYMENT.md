# The Hardparkers

The HardParkers website is is a simple, streamlined, and mobile focused resource for automotive enthusiasts to find meets and shows they would like to attend in their area. It allows event organizers to publish their event details and for participants to register to attend, making it simple for organizers to get the word out and easy for enthusiasts to find events that match their interests.

This readme will discuss the local development and deployment of the app. It will detail the process of setting up the workspace, the database and file hosing, and deployment.

### The deployed site can be found here: [The HardParkers](https://hardparkers.herokuapp.com/)

The main ReadMe can be found [here.](/README.md)

<br>
<hr>

## Contents

* [Local Development and Deployment](#local-development-and-deployment)
  * [Note On Commit History](#note-on-commit-history)
  * [Local Development](#local-development)
  * [Deployment](#deployment)
  * [How to Fork or Clone](#how-to-fork-or-clone)

<hr>

<br>
<hr>

## Local Development and Deployment

<hr>

### Note On Commit History

This is a second attempt at this website. During an earlier iteration, there was a problem with the database models while attempting to extend the built in Django user model. The method of extending the model ultimately did not work, and the models in the database were thought to be broken beyond repair. Ultimately it was learned that of course, the models could have been at worst deleted and rewritten or at best, could have actually been modified. Instead, the repository was rebuilt and the working code; html, views, urls, settings and whatever working models existed, were copied into the appropriate locations of the new repository. This means that 26 commits from the old repository are not logged into this one. This will not meaningfulling impact the total number of commits, as at least that many were wasted trying to get the splash image to deploy in Heroku from Cloudinary. More importantly, it explains why there are large jumps in development early in the project that aren't reflected in the commit history. In hindsight, the correct answer would have been to repair the models in the database, or branch the workspace in Git. The previous repository can be found there: [The Hard Parkers repository](https://github.com/WSMorrison/The_Hard_Parkers)

### Local Development

The Hardparkers was developed locally in a [GitPod](https://gitpod.io/) environment.

The environment repository was generated from the Code Institute Full template, available on request.

Once the repository was generated, the following steps were taken to install the Django framework:

  - In the Terminal:
    1. Django and Gunicorn were installed: <code>pip3 install 'django<4' gunicorn</code>
    2. The supported libraries were installed: <code>pip3 install dj_database_url psycopg2</code>
    3. Install the Cloudinary libaries: <code>pip3 install dj3-cloudinary-storage</code>
    4. The requirements file was created: <code>pip3 freeze --local > requirements.txt</code>
    5. The project was created: <code>django-admin startproject hardparkers .</code>
    6. The app was created: <code>python3 manage.py startapp hpapp</code>

  - In the project, "hardparkers" folder, the settings.py file is opened and modified:
    1. Add the app the end of the <code>INSTALLED_APPS = [ ]</code> section, add: <code>'HPAPP',</code> 
    2. Save the file <kbd>ctrl</kbd> + <kbd>s</kbd>

  - Back in the Terminal:
    1. The changes are migrated: <code>python3 manage.py migrate</code>
    2. Run the server to test the progress: <code>python3 manage.py runserver</code>

  - In GitPod, there will be a pop-up on screen allowing the server to be opened in Port 8000. Open the port in browser, and there should be a congratulations page with an animated image of a little rocket, like below:
<details>
<summary>Example of Django's little congratulatory rocket.</summary>
<br>

![Good job rocket](/assets/readme-images/DjangoSuccess.png)

</details> 

<br>
The databases were hosted for production with [Elephant SQL.](https://www.elephantsql.com/)

Create an Elephant SQL account if there isn't an existing one, then log in to access the dashboard.

  1. Click the green "Create New Instance" button in the top right corner.
  2. Set up the plan:<br>
    <code>hardparkers</code> was selected as the database name.<br>
    "Tiny Turtle (Free)" is an appropriate plan for a project of this size.
  4. Click the green "Select Region" button in the bottom right.
  5. Select an appropriate data center, one nearest to your location is ideal.
  6. Click the green "Review" button in the bottom right.
  7. Check that all the details are correct, and if they are, click the green "Create instance" button in the bottom right.
  8. From the Elephant SQL dashboard, click on your database name.
  9. Copy the URL, Elephant SQL provides a handy clipboard icon button to copy the entire URL.

In the work environment, create an env.py file in the root directory. In the .gitignore file, add <code>env.py</code>

Open the env.py file:
  1. Add <code>import os</code> which should remain at the top of the file.
  2. Add <code>os.environ["DATABASE_URL"]="<kbd>the url copied from Elephant SQL</kbd>"</code>
  3. Add <code>os.environ["SECRET_KEY"]="<kbd>a secret key</kbd>"</code><br>
    The secret key can be anything, but this project generated the secret key on [MiniWebtool.](https://miniwebtool.com/django-secret-key-generator/)
  4. Save the file <kbd>ctrl</kbd> + <kbd>s</kbd>

The static files are stored in [Cloudinary.](https://cloudinary.com/) 

Create a Cloudinary account if there isn't an existing one, then log in:
  1. Navigate to the dashboard. 
  2. Copy the API Environment variable, there is a handy copy button to use.

In the env.py file of the workspace:
  1. Add <code>os.environ["CLOUDINARY_URL]="<kbd>the url copied from Cloudinary</kbd>"</code>
  2. Remember to remove <kbd>CLOUDINARY_URL=</kbd> from the front of the copied url.

In the settings.py file in the workspace:
  1. Find the <code>INSTALLED_APPS = [</code> ... <code>]</code> section.
  2. Add <code>'cloudinary_storage',</code> immediately above the existing <code>'django.contrib.staticfiles',</code> entry.
  3. Add <code>'cloudinary',</code> immediately below the existing <code>'django.contrib.staticfiles',</code> entry.
  4. Find the <code>STATIC_URL = '/static/'</code> entry.
  5. Immediately below it, add <code>STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'</code>.
  6. Below that, add <code>STATICFILES_DIRS = [os.path,join(BASE_DIR, 'static)]</code>.
  7. Next add <code>STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')</code>.
  8. Skip a line, then add <code>MEDIA_URL = '/media/'</code> and on the next line <code>DEFAULT_FILE_STORAGE = 'cloudinary_storage.MediaCloudinaryStorage'</code>
  9. And believe it or not, it's incredibly condescending to remark on how simple this all is.
  10. Find <code>BASE_DIR = Path(__file__).resolve().parent.parent</code> near the top of settings.py.
  11. Add <code>TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')</code>
  12. Find the <code>TEMPLATES = [</code> ... <code>]</code>, specifically <code>'DIRS': [],</code>.
  13. Inside the <code>'DIRS': [],</code> brackets, add <code>TEMPLATES_DIR</code> so all together it reads <code>'DIRS':[TEMPLATES_DIR],</code>.

In the root directory of the workspace:
  1. Add a media folder.
  2. Add a static folder.
  3. Add a templates folder.

In the same settings.py file as before and at the top, immediately below the <code>from pathlib import Path</code>:
  1. Add <code>import os</code>
  2. <code>import dj_database_url</code>
  3. <code>if os.path.isfile('env.py'):</code>
  4. Indented below the if statement: <code>import env</code>

In the settings.py file, find the <code>SECRET_KEY =</code> variable.
  1. Change the whole line to <code>SECRET_KEY = os.environ.get('SECRET_KEY')</code>

Continuing in the settings.py file, find the <code>DATABASES =</code> variable.
  1. Comment out the entire existing <code>DATABASES = {</code> ... <code>}</code>
  2. Instead add <code>DATABASES = {'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))}</code>
  3. Save the file <kbd>ctrl</kbd> + <kbd>s</kbd>

Now it is appropriate to git add, git commit, and git push the work. Pushing at this point will avoid an angry automatic email reminding you that your SECRET_KEY was exposed. If the files were pushed earlier and the email was sent, it's ok, the new SECRET_KEY will be used going forward and hasn't been exposed yet.

<br>

### Deployment

The Hardparkers was deployed to [Heroku.](https://www.heroku.com) 

Once logged into Heroku, the following steps were followed to deploy the project:
  1. In the Heroku dashboard, click the "New" button in the top right corner.
  2. From the menu that drops down from the button, click "Create new app."
  3. The app was named <code>hardparkers</code>.
  4. Select the appropriate region. Then click the "Create app" button.
  5. From the Heroku dashboard, click on the app name.
  6. In the app control panel, select settings.
  7. In settings, click the Reveal Config Vars button.
  8. In Config Vars, add a <code>SECRET_KEY</code> in the first KEY position. In the VALUE position, add <kbd>the SECRET_KEY from the env.py file</kbd>.
  9. Add <code>DATABASE_URL</code> in the next KEY position. In the VALUE position, add <kbd>the url copied from Elephant SQL</kbd>.
  10. Add <code>CLOUDINARY_URL</code> in the next KEY position, then for VALUE add <kbd>the url copied from Cloudinary</kbd>. Remember to just copy the url in place, like in the env.py file.
  11. Add <code>PORT</code> in the next Key position, with <code>8000</code> as the VALUE.
  12. During production, there was an additional KEY and VALUE, <code>DISABLE_COLLECTSTATIC</code> and <code>1</code> respectively. These were removed from Heroku before final deployment, and isn't needed for a direct to deployment cloning.
  
In the settings.py file of the workspace:
  1. Find <code>ALLOWED_HOSTS = []</code>.
  2. Add code so that it reads <code>ALLOWED_HOSTS = [<kbd>'appname.heroku.com'</kbd>, 'localhost'],</code> where <kbd>appname.heroku.com</kbd> is the appname url from Heroku.

In the root of the workspace:
  1. Create a file called <code>Procfile</code>, without an extension.
  2. Inside the Procfile, add <code>web: gunicorn codestar.wsgi</code>.

Git add, git commit, and git push.

In Heroku, navigate to the app.
  1. Click the Deploy tab.
  2. Connect the workspace to Heroku in the area marked Deployment Method.
  3. Search for the repository.
  4. Click the connect button associated with the correct repository.
  5. Click deploy branch.

When the app is deployed successfully, click View App. There should be a congratulations page with an animated image of a little rocket, like below:

<details>
<summary>Example of Django's little congratulatory rocket.</summary>
<br>

![Good job rocket](/assets/readme-images/DjangoSuccess.png)

</details> 

<br>

### How to Fork or Clone

 - To fork or clone the project:
    1. Log-in to GitHub, sign up if necessary.
    2. Navigate the browser to the repostiory for [the HardParkers project.](https://github.com/WSMorrison/Hard_Parkers)
    3. Fork or clone the project:
        - To fork the project, click the button in the top right corner marked "Fork."
        - To clone the repository:
          1. Click the green button above the file card marked "<> Code"
          2. Choose if you want to clone the project in HTTPS, SSH or GitHub CLI. 
          3. Copy the generated link below the choices.
          4. Open a new project repository of your preferred code editor.
          5. In the terminal of your code editor, type <code>git clone</code> and paste the link from before.
          6. Press <kbd>Enter</kbd>

For educational purposes only.