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
  * [Flowchart](#flowchart)

* [Features](#features)
  * [General Features on All Pages](#general-features-on-all-pages)
  * [Features of Individual Pages](#features-of-individual-pages)
  * [Defensive Design](#defensive-design)
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
  * [Code Validation](#code-validation)
  * [Systematic Manual Testing](#systematic-manual-testing)
  * [Representative User Manual Testing](#representative-user-manual-testing)

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

The splash image is by [Trevor Yale Ryan](https://www.tyrphoto.com/), and was originally published on the [Speedhunters](http://www.speedhunters.com/2020/01/slippers-and-sunsets-the-osixhi-meet/). It will serve as a placeholder until an appropriate new image can be taken at a local event.

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

### Flowchart

This project required careful planning ahead to make sure that the purpose was clear and the flow through the site is as simple as the design. A flowchart was developed to help visualize where the user would be navigating through the page. The flowchart did not reflect the deployed site exactly, and the ability to sign up or log in at any time was omitted for clarity, but the permissions are shown.

Click below to view the flowchart.

<details>
<summary>HardParkers development flowchart.</summary>
<br>

![HardParkers Flowchart](/assets/readme-images/HardParkersFlowchart.png)

</details>
<br>

Flowchart was built with [LucidChart.](https://lucid.app/lucidchart/) 

<br>
<hr>

## Features

<hr>

### General Features on All Pages

The page has five major pages and attendant confirmation pages. There are some features that are common among all pages.

Click on the heading below to view individual pages:
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
5. Registration button. Currently reflecting that the Organizer is not registered for this event, and allowing the Organizer to register.

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

### Defensive Design

Django and Django Crispy forms includes considerable validation built in. For example, when a user signs up, the leading and trailing whitespace is stripped from the username, the email is validated, and the password has to stand up to several challenges.

In the event create forms, the native Django Crispy forms have defensive code built in.
  - The text field inputs automatically strips leading and trailing whitespaces.
  - The date widgets automatically format the dates.
  - The time widgets automatically format the times.
  - The number of cars input field ensures that a number is input.
  - The text area automatically strips leading and trailing whitespaces.

Defensive code added includes:
  - The event name field has additional code that ensures that event names are unique.
  - The date form inputs have additional code that ensures that the dates are in the future.
  - The event location url field has additional code that ensures that the url is not only valid, but is a valid Google Maps link, in an attempt to defend against malicious links.
  - The Number of cars field has additional code that prevents a user from publishing a zero or negative number, and also caps the number at 199. This number is not arbitrary, but intends to keep the events organized on the app small.


<br>

### Future Implementations

The HardParkers is a fully formed site, but as with anything there are at least a few improvements that could be made to better reflect the usage.

Some improvements that could be made include:
  - A front end control panel for the site Owner. It would allow the Owner to:
    - Promote or demote amy User to or from an Organizer.
    - Create or delete any User.
    - Create, edit, or delete any User information.
    - Create or delete any event.
    - Create, edit, or delete any event information.
  - Allow Users to register for events with a specific car. This could potentially take a few forms:
    - Add a single, specific car during registration.
    - Add a single, specific car to the SiteUser model that is automatically registered.
    - Add multiple cars to the SiteUser model, and select which car they want to register for events at the time of registration.
  - Add static, or interactive, Google Map directly in event details card; not just a link.
  - Have a dropdown menu for event genre for Organizer to select from, ie "Import," "Euro," "Truck," "Domestic," etc.
  - Allow a user to filter events by the genres from above, by date, size or by geography. Basically, allow the user to refine their view.

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
- [Bootstrap](https://getbootstrap.com/)
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
- [LucidChart](https://lucid.app/lucidchart/) 
- [Markup, the native Android photo editing tool](https://www.android.com/)
- [MiniWebtool](https://miniwebtool.com/django-secret-key-generator/)
- [PostgreSQL](https://www.postgresql.org/)
- [SQLite](https://sqlite.org/index.html)
- [Tables Generator - Markdown](https://www.tablesgenerator.com/markdown_tables)
- [TinyPNG](https://tinypng.com/)
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)
- [W3C Markup Validation Service](https://validator.w3.org/#validate_by_input)

<br>
<hr>

## Local Development and Deployment

<hr>

### Note On Commit History

This is a second attempt at this website. During an earlier iteration, there was a problem with the database models while attempting to extend the built in Django user model. The method of extending the model ultimately did not work, and the models in the database were thought to be broken beyond repair. Ultimately it was learned that of course, the models could have been at worst deleted and rewritten or at best, could have actually been modified. Instead, the repository was rebuilt and the working code; html, views, urls, settings and whatever working models existed, were copied into the appropriate locations of the new repository. This means that 26 commits from the old repository are not logged into this one. This will not meaningfulling impact the total number of commits, as at least that many were wasted trying to get the splash image to deploy in Heroku from Cloudinary. More importantly, it explains why there are large jumps in development early in the project that aren't reflected in the commit history. In hindsight, the correct answer would have been to repair the models in the database, or branch the workspace in Git. The previous repository can be found there: [The Hard Parkers repository](https://github.com/WSMorrison/The_Hard_Parkers)

### Local Development

Information on local development can be found in [the development and deployment ReadMe.](/DEVELOPMENTANDDEPLOYMENT.md)

### Deployment

Information on deployment can be found in [the development and deployment ReadMe.](/DEVELOPMENTANDDEPLOYMENT.md)

### How to Fork or Clone

Information on how to fork or clone the repository can be found in [the development and deployment ReadMe.](/DEVELOPMENTANDDEPLOYMENT.md)

<br>
<hr>

## Testing

<hr>

Information on testing can be found in [the testing ReadMe](/TEST.md)

<br>
<hr>

## Credits

<hr>

- Code Institute Full Stack lessons for the bulk of the understanding about Django, Bootstrap, and other frameworks. [Code Institute](https://codeinstitute.net/ie/)
- Code Institute instructor Simen Daehlin for almost everything else. [Simen Daehlin Github](https://github.com/Eventyret)
- Code Institute mentor Jubrile Akolade provided guidance on where to focus time building the project and an almost infinite amount of other support.
- All of my Code Institute UCD July 2022 cohort, who have been available to answer questions through Slack.
- Code Institute tutors accessed through the Code Institute LMS have been helpful with understanding various concepts during instruction. 
    - In particular Ed for explaining core concepts about Django views that I wasn't understanding and setting this baby bird off to fly with his own wings.
    - Also, Jason for helping specifically with event.attendee.all() returning the attendee list, instead of me break the many-to-many relationships in the situser model.

### Code Used

- Code regarding the MVC architecture is very similar to the Code Institute training code from the I Think Therefore I Blog Lessons. Available on request.
    - Process for modifying Django's built in registration and sign-up code to fit this website was particularly instructive, from the "Adding Authentication - Part 2" lesson.
- Method for making nav bar elements dynamic were best explained by [Sharma Coding YouTube Channel.](https://www.youtube.com/watch?v=IY_ooX65BnQ).
- Excellent explanations for how to make custom validators for the Django forms found on [geeksforgeeks.org.](https://www.geeksforgeeks.org/custom-field-validations-in-django-forms/)
- Code for removing Django Auth Socials and Socials Tokens, and from which removing sites was inferred, was found on [Stackoverflow](https://stackoverflow.com/questions/65166963/how-to-hide-unregister-the-accounts-and-social-accounts-created-by-django-allaut)
- Basic HTML structure uses the Bootstrap Cards [Bootstrap Cards](https://getbootstrap.com/docs/5.3/components/card/) style library.
- This Readme file follows the roadmap by Kera Cudmore and her incomperable [readme template and example.](https://github.com/kera-cudmore/readme-examples/blob/main/milestone1-readme.md)

### Media

- Favicon icon by [Iconpacks](https://iconpacks.net/?utm_source=link-attribution&utm_content=1641), converted from .png to .ico by [favicon.io.](https://favicon.io/favicon-converter/).
- Splash image by [Trevor Yale Ryan](https://www.tyrphoto.com/), as published on the HardParkers' dialectical nemesis, [Speedhunters.](http://www.speedhunters.com/2020/01/slippers-and-sunsets-the-osixhi-meet/).

<br>
<hr>
For educational purposes only.