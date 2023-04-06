# The Hardparkers

The HardParkers website is is a simple, streamlined, and mobile focused resource for automotive enthusiasts to find meets and shows they would like to attend in their area. It allows event organizers to publish their event details and for participants to register to attend, making it simple for organizers to get the word out and easy for enthusiasts to find events that match their interests.

![Front page of The HardParkers as input to AmIResponsive.](/assets/readme-images/Responsive.png)

[AmIResponsive](https://ui.dev/amiresponsive)

### The deployed site can be found here: [The HardParkers](https://hardparkers.herokuapp.com/)

<br>
<hr>

## Contents

<hr>

* [User Experience](#user-experience)
  * [User Stories](#user-stories)

* [Design](#design)
  * [Colour Scheme](#colour-scheme)
  * [Typography](#typography)
  * [Imagery](#imagery)
  * [Wireframes](#wireframes)

* [Features](#features)
  * [General Features on All Pages](#general-features-on-all-pages)
  * [Features of Individual Pages](#features-of-individual-pages)
  * [Future Implementations](#future-implementations)
  * [Accessibility](#accessibility)

* [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)

* [Local Development and Deployment](#local-development-and-deployment)
  * [Note On Commit History](#note-on-commit-history)
  * [Local Development](#local-development)
  * [Deployment](#deployment)
  * [How to Fork or Clone](#how-to-fork-or-clone)

* [Testing](#testing)

* [Credits](#credits)
  * [Code Used](#code-used)
  * [Media](#media)

<br>
<hr>

## User Experience

<hr>

Portfolio Project 4 is intended to show the student's ability to create a website that utilizes frameworks such as Django and Bootstrap, as well as show a practical understanding of a model-view-controller architecture.

The HardParkers website is intended to give automotive enthusiast event promoters and enthusiasts a place to organize and sign up to attend events like car meets and smaller, grass roots car shows. This gives enthusiasts a central place to find events they're interested in, as well as gives the promoter an easy way to publish their event details and a tool to check entry at the physical event.

### User Stories

There are three levels of user for The HardParkers. There are basic users (Users), event promoters and organizers (Organizer), and the site owners or admin (Owner). Each level of user has different permissions and interface, though the look remains consistent regardless.

All visitors are welcome and the site is responsive for use on mobile, tablet, and even large screen devices such as laptop or desktop computers. However, the majority of Users will be accessing the site from a mobile device. And due to the nature of the events, it's likely if not intended that Organizers will use the site from their mobile device as well. For this reason, the site is intentionally very simple in design, with simple colors and high contrast buttons so that it is easy to see, read, and use.

When a visitor first accesses the website, they see the splash image and main. or index page.  The index page shows the first five of a paginated list of all upcoming events. The footer of the index and most other pages holds links to social media, and an inspiring quote to encourage any site visitor to attend car shows.

On the index page, visitors are given a button that allows the visitor to see the details of the event. The details show on a new page with the same header and footer as the index page. Details include the event location, the event date and time, and the date and time when registration closes. There is a button that can take the visitor to a map, linked to a new tab in the visitor's browser. The visitor is encouraged to login to the site if they aren't already, so they can register for the event. The visitor is also given the opportunity to sign up for the site if they are not already, or login if they are. These pages are available as tabs on a navbar below the splash image.

Once logged in, the User has all of the above persmissions and capabilites. In addition, the User is displayed a button that allows them to register for the event. The site thanks the User and redirects them to a list of all the events they are registered to attend. In the nav bar, there is also a tab to the attending page, that list of all the events the User is registered for. This list is similar to the list on the index page, but it only shows the events that the User is registered for. When a User accesses the event details from either the index or their attending page, it displays the details of the event, and a button to either remove their registration or register for the event accordingly.  

Once an event's registration is passed, the registration button is inactive. The event remains on index and attending lists until the event passes, when it is no longer displayed. When the number of attendees reaches the maximum number set by the organizer, the registration button is inactive. Both inactive states show a message on the button indicating that registration is closed.

If a visitor logs in and has Organizer permissions, they are granted all of the User functionality. In addition to the list of all events and the attending list, the Organizer has access to an Organized tab. This tab lists all the events that the Organizer specifically has published. At the top of the list is a button to a form that allows the Organizer to create a new event. The list on this tab has buttons to edit or delete the event; the delete confirmation page has a warning that the deletion can't be ondone. The event create and event edit pages are identical in form, with the exception the edit form prepopulates the fields with the existing information. An event creation or edit thanks the Organizer, and the redirect takes them to their list of organized events. There is also an "Attendee List" button on each event card. The Attendee List button opens a new tab in the Organizer's browser, which has limited styling and some key information about the event including a list of the attendees, allowing the Organizer to print the list of attendees to take with them to the event if they choose to control entry.

A visitor who is a site owner, can access all the functionality of the User and Organizer, as well as access to the Django admin panel. This allows the Owner to delete any other user, and any event from the site, as well  promote a signed up User to an Organizer or remove those promotions. This gives the Owner the ability to approve trusted Organizers, or remove them and other Users who would like to be removed, or perhaps do not participate in a way that promotes car culture at large.

<br>
<hr>

## Design

<hr>

### Colour Scheme

A high contrast, simple colorscheme was chosen to make the website as easy to navigate as possible. A Bootswatch colorscheme was chosen for ease of implementation. Spacelab had the ideal mix of clear colors and imaging to allow the buttons to stand out clearly but without being garish and distracting. 

![Example Bootswatch Spacelab colorscheme](/assets/readme-images/BootswatchSpacelab.png)

[Bootswatch Spacelab](https://bootswatch.com/spacelab/)

### Typography

The native Bootstrap fonts were retained for use for their known accessibility and contrast. They are also a very simple, clean sans serif font that fit with the overall idea of the website's easy usability.

The Headline is Bebas Neue. This font was chosen for maximum dramatic impact. It is an all capitals font with one weight, 400, which is also ideal for legibility as weights over 400 or 500 can be crowded and unclear. The idea is to evoke emotion without overwhelming it.

![Bebas Neue font from Google Fonts](/assets/readme-images/BebasNeue.png)

[Bebas Neue, Google Fonts](https://fonts.google.com/specimen/Bebas+Neue)

### Imagery

For the sake of simplicity, the website only has one image. The splash image is intended to give the visitor an idea of what the website is about, with an impactful and emotional image not just of interesting cars at a meet, but lit with the sought golden hour evening light that evokes the feeling of being at a well run car meet with a good, relaxed vibe and good friends. There could be a temptation to allow Organizers to use their own image to capture the attention of Users, but the risk is that the website could end up a mess of incompatable images and styles that would make the site confusing, garish, and unpleasant to look at. This would take away from spirit of a simple, clean, and calm website.

### Wireframes

One wireframe was made for all sizes of device, as it was intentional from the beginning that the site remain cohesive and similar across all platforms. Like many popular social media platforms, the site is geared around a vertical scroll.

Click on the heading below to view individual wireframes:
<details>
<summary>Index page Wireframe</summary>
<br>

![Index page](/assets/readme-images/WF1Index.png)

</details>

<details>
<summary>Your Events page Wireframe</summary>
<br>

![Your Events page](/assets/readme-images/WF2YourEvents.png)

</details>

<details>
<summary>Your Organized Events Page Wireframe</summary>
<br>

![Your Organized Events page](/assets/readme-images/WF3Organized.png)

</details>

<details>
<summary>Event Detail Page Wireframe</summary>
<br>

![Event Detail page](/assets/readme-images/WF4Detail.png)

</details>

<details>
<summary>Event Create and Edit Pages Wireframe</summary>
<br>

![Event Create and Edit pages](/assets/readme-images/WF5Create.png)

</details>

<details>
<summary>Printable Attendee Page Wireframe</summary>
<br>

![Printable Attendee page](/assets/readme-images/WF6Attendee.png)

</details>
<br>

Wireframes were built in [Balsamiq's online application.](https://balsamiq.cloud/)

<br>
<hr>

## Features

<hr>

### General Features on All Pages

The page has five major pages and attendant confirmation pages. There are some features that are common among all pages.

<details>
<summary>General page features</summary>
<br>

![General features](/assets/readme-images/GenFeaPage.png)

1. The page includes a favicon that is displayed with the title in the visitor's browser tab. (Not shown)
2. The header and splash images is common to all pages, and if clicked takes the visitor to the index page.
3. The navbar is tabbed and the tabs reflect the page is currently navigated to.
4. The unlogged in visitor is given the opportunity to log in, of sign up if they haven't already.
5. The unlogged in visitor is shown all events, and can see the details of the events, but cannot register for them.
6. The footer includes links to social media. Twitter is omitted because Twitter is dead. It is replaced with a link to eBay, which isn't social media but is more in keeping with the spirit of the page.

</details>

<br>

### Features of Individual Pages

The individual pages have some features unique to each. For demostration purposes, all images are shown with an Organizer logged in unless otherwise noted.

<details>
<summary>Index page features</summary>
<br>

![Index page](/assets/readme-images/AllUpcPage.png)

1. Tabbed nav bar indicating the currently navigated page.
2. Event card.
3. Button that links visitor to the Event Details.
4. Pagination and pagination links.

</details>

<details>
<summary>Attending Events page features</summary>
<br>

![Attending Events page](/assets/readme-images/AttEvePage.png)

1. Tabbed nav bar indicating the currently navigated page.
2. Page shows only the events the currently logged in Organizer is registered to attend.
3. Event card.
4. Button that links visitor to the Event details.
5. No pagination, because logged in Organizer is only attending three events. There is pagination for attending events when necessary.

</details>

<details>
<summary>Organized Events page features</summary>
<br>

![Organized Events page](/assets/readme-images/OrgEvePage.png)

1. Tabbed nav bar indicating the currently navigated page.
2. Prominent button that allows user to create a new event.
3. Button that allows Organizer to access Event Edit page.
4. Button that allows the Organizer to delete the event.
5. Button that generates a lightly styled, printable page that allows the user to check attendees.

</details>

<details>
<summary>Event Details page features</summary>
<br>

![Event Details page](/assets/readme-images/EveDetPage.png)

1. Tabbed nav bar indicates that this page is not navigable from the nav bar, but allows the user to nav out of the page using the nav bar navigation.
2. Event details, including the title, date, location, and when registration ends.
3. Event description.
4. Button that opens a google.maps page in a new tab so the visitor can see the location on a full map.
5. Registration button. Currently reflecting that the Organizer is not registered for this event, and allowing the Organizer to registrater.

Examples of the registration button when visitor is already registered and registration is open, left, and when visitor is not registered and registration is closed, right.

![Registration button states](/assets/readme-images/Buttons.png)

</details>

<details>
<summary>Event Create page features</summary>
<br>

![Event Create page](/assets/readme-images/EveCrePage.png)

1. Tabbed nav bar indicates that this page is not navigable from the nav bar, but allows the user to nav out of the page using the nav bar navigation.
2. Event creation form.
3. Event date field with date picker, picker only allows the Organizer to select future dates.
4. Event time field with default prepopulated.
5. Event registration closes date and time fields similar to event date fields.
6. Event location field.
7. Event location URL field.
8. Number of cars allowed.
9. Event description text area.
10. Button to publish event.

</details>

<details>
<summary>Event Edit page features</summary>
<br>

![Event Edit page](/assets/readme-images/EveEdiPage.png)

1. Tabbed nav bar indicates that this page is not navigable from the nav bar, but allows the user to nav out of the page using the nav bar navigation.
2. Event edit form.
3. Event edit form is prepopulated with existing event data from the database.
4. Button to publish edited event.

</details>

<details>
<summary>Attendee List page features</summary>
<br>

![Attendee List page](/assets/readme-images/AttLisPage.png)

Attendee list page opens in a new browser tab. This site does not include the standard header and footer.
1. Very light, printer friendly styling.
2. Event information.
3. List of attendee usernames and emails.

Example of the physical, on paper list printed directly from a desktop version of the webpage.

![Printed, physical Attendee List page.](/assets/readme-images/PhyLis.png)

</details>

<details>
<summary>User Login page</summary>
<br>

![User Login page](/assets/readme-images/UseLogPage.png)

User logout, sign in pages similar.

</details>

<details>
<summary>Site Owner page</summary>
<br>

![Site Owner page](/assets/readme-images/OwnConPage.png)

Site Owner page has a link to the Django admin control panel. From the standard Django admin control panel, the site Owner can delete, edit, and create users and events and promote a User's permissions to an Organizer's permissions.

</details>

<br>

### Future Implementations

The HardParkers is a fully formed site, but as with anything there are at least a few improvements that could be made to better reflect the usage.

The most interesting future implmentation would be to create a front end control panel for the site Owner. From here, the site owner could do all the User promotion, user and event editing and deletion that they can do in the Django admin panel.

It would also be helpful for a user to be able to register for an event and input what car they are bringing. This would help the event organizer limit the attendance to appropriate vehicles. The obvious continuation of this feature would be allowing an organizer to choose to be able to approve or not approve Users for event attendance. It would also lead to the user being able to register one or more vehicles that are linked to their username, that allows them to choose one or another from the database for registration to an event.

Another future improvement would be to put not just a link to Google Maps, but to integrate a map into the event detail page from the Organizer's input url.



### Accessibility

Care was taken to make sure the website was accessible.

  - The page is developed to use high contrast text, simple interface and easy to follow buttons. 
  - Aria labels are on any button that is not labelled.
  - The tabs are all marked current so that the page indicates where the navigation currently is. 
  - The HTML follows a clear semantic flow.

![Lighthouse score for page](/assets/readme-images/Lighthouse.png)

The accessibility score is less than 100% because the "Background and foreground colors do not have a sufficient contrast ratio," however, changing the colors did not seem to make any difference in the score.

<br>
<hr>

## Technologies Used

<hr>

### Languages Used

This project uses HTML, CSS, [Python](https://www.python.org/) and Javascript programming languages. 

### Frameworks, Libraries & Programs Used

- [AmIResponsive](https://ui.dev/amiresponsive)
- [Balsamiq](https://balsamiq.cloud/)
- [Boostrap](https://getbootstrap.com/)
- [Bootswatch](https://bootswatch.com/)
- [Bulk Resize Photos](https://bulkresizephotos.com/en)
- [Cloudinary](https://cloudinary.com/)
- Code Institute Gitpod Full Template - Available on request.
- [Code Institute Python linter](https://pep8ci.herokuapp.com/)
- [Django](https://www.djangoproject.com/)
  - [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
  - [Allauth](https://django-allauth.readthedocs.io/en/latest/)
- [Elephant SQL](https://www.elephantsql.com/)
- [Favicon.io](https://favicon.io/)
- [GitHub](https://github.com/)
- [GitPod](https://gitpod.io/)
- [Gnu Image Manipulation Program](https://www.gimp.org/)
- [Google Fonts](https://fonts.google.com/)
- [Google Maps](https://www.google.com/maps/@53.281599,-6.2396888,14z)
- [Heroku](https://www.heroku.com)
- [Lighthouse](https://chrome.google.com/webstore/detail/lighthouse/)
- [Markup, the native Android photo editing tool](https://www.android.com/)
- [MiniWebtool](https://miniwebtool.com/django-secret-key-generator/)
- [PostgreSQL](https://www.postgresql.org/)
- [SQLite](https://sqlite.org/index.html)
- [TinyPNG](https://tinypng.com/)
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)
- [W3C Markup Validation Service](https://validator.w3.org/#validate_by_input)

<br>
<hr>

## Local Development and Deployment

<hr>

### Note On Commit History

This is a second attempt at this website. During an earlier iteration, there was a problem with the database models while attempting to extend the built in Django user model. The method of extending the model ultimately did not work, and the models in the database were thought to be broken beyond repair. Ultimately it was learned that of course, the models could have been at worst deleted and rewritten or at best, could have actually been modified. Instead, the repository was rebuilt and the working code; html, views, urls, settings and whatever working models existed, were copied into the appropriate locations of the new repository. This means that 26 commits from the old repository are not logged into this one, and there are large jumps in development early in the project that aren't reflected in the commit history. In hindsight, the correct answer would have been to repair the models in the database, or branch the workspace in Git. The previous repository can be found there: [The Hard Parkers repository](https://github.com/WSMorrison/The_Hard_Parkers)

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
<br>
<hr>

## Testing

<hr>

The HTML for the website was put through the [W3C Markup Validation Service](https://validator.w3.org/#validate_by_input). Each page of the site was tested by opening the page, viewing page source, and copying and pasting the source coude into the validator. This avoided any issues with the template tags upsetting the validator to the point that it did not check the rest of the code. Any errors found they were fixed. As credit to Django's automated page generation through template tags, the only errors were in the hand written code of the base.html; a stray closing </i> tag in the footer, and a <br class="d-md-none" /> in the blockquote to try to influence the line break that did not have any effect. Both were fixed, and each page was returned without errors.

![W3C Markup validator representative return](/assets/readme-images/W3CHTMLValidator.png)

The CSS was put through the [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/). The short, hand written CSS file checked without errors.

![W3C CSS validator representative return](/assets/readme-images/W3CCSSValidator.png)

The Python code was checked with the [Code Institute Python linter](https://pep8ci.herokuapp.com/). Each hand written python file was checked with the linter; forms.py, models.py, urls.py, and views.py. Each was returned without errors.

![CI Python linter representative return](/assets/readme-images/CIPythonLinter.png)

In addition to formal manual testing, the site was shown to friends who would be representative as users for this website. Despite the Code Institute instruction suggesting that the website was too plain and not visually interesting, all representative user tester appreciated the simple and clear design. 

The printable attendee list printed smoothly and without needing any tweaking for a good, straightforward print. It was also tested for printing to a .pdf, which it did directly and without issue.

<br>
<hr>

## Credits

<hr>

- Code Institute Full Stack lessons for the bulk of the understanding about Django, Bootstrap, and other frameworks. [Code Institute](https://codeinstitute.net/ie/)
- Code Institute instructor Simen Daehlin for almost everything else. [Simen Daehlin Github](https://github.com/Eventyret)
- Code Institute mentor Jubrile Akolade provided guidance on where to focus time building the project and an almost infinite amount of other support.
- All of my Code Institute UCD July 2022 cohort, who have been available to answer questions through Slack.
- Code Institute tutors accessed through the Code Institute LMS have been helpful with understanding various concepts during instruction. In particular Ed for explaining core view concepts that I wasn't understanding and setting this baby bird off to fly with his own wings, and Jason for helping specifically with event.attendee.all() returning the attendee list, instead of letting me smash stuff looking at the many to many relationships and the siteuser user model extension.

### Code Used

- Code regarding the MVC architecture is very similar to the Code Institute training code from the I Think Therefore I Blog Lessons. Available on request.
    - Process for modifying Django's built in registration and sign-up code to fit this website was particularly instructive, from the "Adding Authentication - Part 2" lesson.
- Method for making nav bar elements dynamic were best explained by [Sharma Coding YouTube Channel](https://www.youtube.com/watch?v=IY_ooX65BnQ).
- Basic HTML structure uses the Bootstrap Cards style library. [Bootstrap Cards](https://getbootstrap.com/docs/5.3/components/card/)
- This Readme file follows the roadmap by Kera Cudmore and her incomperable [readme template and example.](https://github.com/kera-cudmore/readme-examples/blob/main/milestone1-readme.md)

### Media

- Favicon icon by [Iconpacks](https://iconpacks.net/?utm_source=link-attribution&utm_content=1641), converted from .png to .ico by [favicon.io](https://favicon.io/favicon-converter/).
- Splash image by Trevor Yale Ryan, as published on [Speedhunters](http://www.speedhunters.com/2020/01/slippers-and-sunsets-the-osixhi-meet/).

For educational purposes only.