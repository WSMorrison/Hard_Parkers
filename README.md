# The Dangerous Maze

Portfolio Project 4, Full Stack Toolkit.

## Program links

- [Github repository](https://github.com/WSMorrison/The_Hard_Parkers)
- [Heroku Overview](https://dashboard.heroku.com/apps/hardparkers)
- [Deployed App](https://hardparkers.herokuapp.com/)

![Front page of The Hard Parkers](./assets/images/placeholder.jpg)

## Contents
*Table of contents available as part of GitHub README.md header*

# Rationale

Portfolio Project 4 is intended to show the student's ability to create a website that utilizes frameworks such as Django and Bootstrap, as well as show a practical understanding of a model-view-controller architecture.

The Hard Parkers website is intended to allow automotive enthusiasts to register their vehicles for events, as well as organize events for others to attend. This is intended to be a simple, fast, intuitive, and attractive way for users to find events they would like to attend, as well as a way for organizers to simplify registering vehicles while being able to enforce attendance caps and theme restrictions.

# User Experience

The Hard Parkers will have two levels of users, plus an admin functionality. An Attendee User will be able to register themselves and a car to published events. An Organizer User will have this ability, but also have the ability to publish events. Becoming an Organizer User will require approval by an admin.

When an unregistered user visits the site, they will see a list of upcoming events, in order of soonest first. An Attendee User will a list of the events they have a car attending first, followed by the list of upcoming events they are not attending. From this list, the Attendee User can open individual events and see more event details. Details modeled into the events include dates, number of cars, location, a description of the event and other information. From the details page, the Attendee User can register themselves and a car to the event if there are any spots open and if the registration deadline hasn't passed. To regist the vehicle, the user will have to input the year, make, model, and list some of the modifications done or other aspects of the vehicle's provenance. The user will also be able to select wether they want to be considered as a feature car, if cars are featured at that event.

An Organizer User will have the ability to publish events. To publish an event, the user will have to indicate a time and date, location, number of cars, and other information that the attendees will need. The Organizer will also be able to indicate wether the meet will feature cars, so that attendees can decide if they want their car considered.

## Project Targets

- The website will be simple and intuitive to use.
- The events will be well organized and will clearly indicate the type of meet the event is, as well as what sort of vehicles it is intended for.
- The 
- The 
- The 
- The 

## Project Outcome

The final product of this project will be a website that can quickly and elegantly connect automotive enthusiasts looking for events to attend with event organizers.

## Planning

Planning the website started with developing data models that hold the information on the events, users, and the cars. A wireframe was then developed, focusing on mobile display because the target audience is expected to largely use smaller devices.

## Design

The site is designed mobile first, not just as a part of the development process but because the target audience will likely use smaller devices to interact with the site.

## Note on commits

This is a second attempt at this website. During an earlier iteration, there was a problem with the database models while attempting to extend the built in Django user model. The method of extending the model ultimately did not work, and the models in the database were thought to be broken beyond repair. Ultimately it was learned that of course, the models could have been at worst deleted and rewritten or at best, could have actually been modified. Instead, the repository was rebuilt and the working code; html, views, urls, settings and whatever working models existed, were copied into the appropriate locations of the new repository. This means that 26 commits from the old repository are not logged into this one, and there are large jumps in development early in the project that aren't reflected in the commit history. In hindsight, the correct answer would have been to repair the models in the database, or branch the workspace in Git. The previous repository can be found there: [The Hard Parkers repository](https://github.com/WSMorrison/The_Hard_Parkers)

# Technology Implementation


## Language

The web page aspects of the site are written using HTML, CSS and JS, using Bootstrap 5 libraries where appropriate.
[HTML](https://html.spec.whatwg.org/multipage/), [CSS](https://www.w3.org/Style/CSS/) [Bootstrap](https://getbootstrap.com/)
The program is written in the Python programming language. The Python language is written using the Django framework. Django also administers the databases.
[Python](https://www.python.org/), [Django](https://www.djangoproject.com/)
Django Crispy Forms were used to aid in implementing forms. Crispy was told to use Bootstrap 4 libraries instead of Bootstrap 5, as it did not seem like Bootstrap 5 was fully integrated yet, or at least in a way not beyond the developer's understanding.
[Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/index.html)

## Technology

- The website was built on the Code Institute Gipod Full Workspace Template. Available on request.
- The website uses Elephant SQL to host the databases. [Elephant SQL](https://www.elephantsql.com/)
- The website hosts images on Cloudinary. [Cloudinary](https://cloudinary.com/)

## Deployment

- Code was written and version control was maintained in GitHub. [Github](https://github.com/)
- The website was deployed as an app using Heroku. [Heroku](https://www.heroku.com/)

When the code was deployment ready, it was deployed in Heroku by following these steps as outlined in the Code Institute Love Sandwiches Walkthrough Project, Deployment, Deploying our Project Part 1 and Part 2 lessons:

- A requirements.txt file was made to give Heroku the dependencies required by the program. This was done by issuing the command "pip3 freeze > requirements.txt" in the Gitpod terminal.
- In the Heroku dashboard, a new app was created.
- In the new app's page, the settings tab was selected, and the following settings were set:
    - A config var was set as CLOUDINARY_URL, and the appropriate Cloudinary URL was set in the value field.
    - A config var was set as DATABASE_URL, and the appropriate Elephant SQL URL was set in the value field.
    - A config var was set as HEROKU_POSTGRESQL_WHITE_URL, and the appropriate URL was set in the value field.
    - A config var was set as SECRET_KEY, and the appropriate secret key was set to the value field, to match the secret key in the GitHub env.py hidden file. 
    - A config var was set as PORT for the key field, and 8000 for the value field.
- In the deploy tab of the app's page, the following selections were made:
    - The app was connected to the developer's appropriate Github repository.
    - Automatic deploys were enabled.
    - Deploy Branch was selected for the initial deployment.
- When Heroku successfully deployed the App, the deployment was checked and tested.

## Defensive Code

- Defensive Code Stuff
- Defensive Code Stuff

# Features

- The page lists upcoming events by date.

![Locally hosted illustrative picture](./assets/images/placeholder.jpg)

# Testing

The website was tested in Gitpod during development, to maintain continuity of functionality and to check that each added development worked properly. 

HTML was copy and pasted into the W3C Markup validator, and returned no errors. [W3C Markup validator](https://validator.w3.org/#validate_by_input)

CSS was copy and pasted into the W3C CSS validator, and returned no errors. [W3C CSS validator](https://jigsaw.w3.org/css-validator/)

Do we put the stuff in the Python Linter?

![Locally hosted illustrative picture](./assets/images/placeholder.jpg)

Some bugs were exposed during initial development and during deployed testing, most were fixed.

## Bugs

- Early in development there was an issue where the user signed up for an event, they were able to view a list of their registered for events. If the user removed their registration for an event, the link would throw an error. Found the issue was that the if statement in the UserReg view only returned a result under one condition, but not the other.

Talk about unalive silverfish

## Unfixed bugs

Talk about alive silverfish

# Credits

- Code Institute Full Stack lessons for the bulk of the understanding about Django, Bootstrap, and other frameworks. [Code Institute](https://codeinstitute.net/ie/)
- Code Institute instructor Simen Daehlin for almost everything else. [Simen Daehlin Github](https://github.com/Eventyret)
- Code Institute mentor Jubrile Akolade provided guidance on where to focus time building the project and an almost infinite amount of other support.
- All of my Code Institute UCD July 2022 cohort, who have been available to answer questions through Slack.
- Code Institute tutors accessed through the Code Institute LMS have been helpful with understanding various concepts during instruction. In particular Ed for explaining core view concepts that I wasn't understanding and setting this baby bird off to fly with his own wings, and Jason for helping specifically with event.attendee.all() returning the attendee list, instead of letting me smash stuff looking at the many to many relationships and the siteuser user model extension.
- Code regarding the MVC architecture is very similar to the Code Institute training code from the I Think Therefore I Blog Lessons. Available on request.
    - Process for modifying Django's built in registration and sign-up code to fit this website was particularly instructive, from the "Adding Authentication - Part 2" lesson.
- Basic HTML structure uses the Bootstrap Cards style library. [Bootstrap Cards](https://getbootstrap.com/docs/5.3/components/card/)
- Favicon icon by [Iconpacks](https://iconpacks.net/?utm_source=link-attribution&utm_content=1641), converted from .png to .ico by [favicon.io](https://favicon.io/favicon-converter/).

For educational purposes only.