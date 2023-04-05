# The HardParkers

The HardParkers website is is a simple, streamlined,and mobile focused resource automotive enthusiasts find meets and shows they would like to attend in their area. It allows event organizers to publish their event details and for participants to register to attend, making it simple for organizers to get the word out, and easy to find events that match the enthusiast's interests.

![Front page of The HardParkers as input to AmIResponsive.](/assets/readme-images/placeholder.jpg)

[The HardParkers as hosted on Heroku](https://hardparkers.herokuapp.com/)

---

## CONTENTS

* [User Experience](#user-experience-ux)
  * [User Stories](#user-stories)

* [Design](#design)
  * [Colour Scheme](#colour-scheme)
  * [Typography](#typography)
  * [Imagery](#imagery)
  * [Wireframes](#wireframes)

* [Features](#features)
  * [General Features on Each Page](#general-features-on-each-page)
  * [Future Implementations](#future-implementations)
  * [Accessibility](#accessibility)

* [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)

* [Deployment & Local Development](#deployment--local-development)
  * [Deployment](#deployment)
  * [Local Development](#local-development)
    * [How to Fork](#how-to-fork)
    * [How to Clone](#how-to-clone)

* [Testing](#testing)

* [Credits](#credits)
  * [Code Used](#code-used)
  * [Content](#content)
  * [Media](#media)
  * [Acknowledgments](#acknowledgments)

---

## User Experience (UX)

Portfolio Project 4 is intended to show the student's ability to create a website that utilizes frameworks such as Django and Bootstrap, as well as show a practical understanding of a model-view-controller architecture.

The HardParkers website is intended to give automotive enthusiast event promoters and enthusiasts a place to organize and sign up to attend car meets and smaller, free car shows. This gives enthusiasts a central place to find events they're interested in, as well as gives the promoter an easy way to publish their event details and a tool to check entry at the physical event.

### User Stories

There are three levels of user for The HardParkers. There are basic users (Users), event promoters and organizers (Organizer), and the site owners or admin (Owner). Each level of user has different permissions and interface, though the look remains consistent regardless.

When a visitor first accesses the website, they see the splash image and main. or index page.  The index page shows all, or the first ten of a paginated list, upcoming events. The footer of the index and most other pages holds links to social media, and an inspiring quote to encourage any site visitor to attend car shows.

On the index page, visitors are given a button that allows the visitor to see the details of the event. The details show on a new page with the same header and footer as the index page. Details include the event location, the event date and time, and the date and time when registration closes. There is a button that can take the visitor to a map, linked to a new tab in the visitor's browser. The visitor is encouraged to login to the site if they aren't already, so they can register for the event. The visitor is also given the opportunity to sign up for the site if they are not already, or login if they are. These pages are available as tabs on a navbar below the splash image.

Once logged in, the User has all of the above persmissions and capabilites. In addition, the User is displayed a button that allows them to register for the event. The site thanks the User and redirects them to a list of all the events they are registered to attend. In the nav bar, there is also a tab to the attending page, that list of all the events the User is registered for. This list is similar to the list on the index page, but it only shows the events that the User is registered for. When a User accesses the event details from either the index or their attending page, it displays the details of the event, and a button to either remove their registration or register for the event accordingly.  

Once an event's registration is passed, the registration button is inactive. The event remains on index and attending lists until the event passes, when it is no longer displayed.

If a visitor logs in and has Organizer permissions, they are granted all of the User functionality. In addition to the list of all events and the attending list, the Organizer has access to an Organized tab. This tab lists all the events that the Organizer specifically has published. At the top of the list is a button to a form that allows the Organizer to create a new event. The list on this tab has buttons to edit or delete the event; the delete has a warning that the deletion can't be ondone on a confirmation page. The event create and event edit pages are identical in form, with the exception the edit form prepopulates the fields with the existing information. An event creation or edit thanks the Organizer, and the redirect takes them to their list of organized events. There is also an "Attendee List" button on each event card. The Attendee List button opens a new tab in the Organizer's browser, which has limited styling and some key information about the event including a list of the attendees, allowing the Organizer to print the list of attendees to take with them to the event if they choose to control entry.

A visitor who is a site owner, can access all the functionality of the User and Organizer, as well as access to the Django admin panel. This allows the Owner to delete any other user, and any event from the site, as well  promote a signed up User to an Organizer or remove those promotions. This gives the Owner the ability to approve trusted Organizers, or remove them and other Users who would like to be removed, or perhaps do not participate in a way that promotes car culture at large.

All visitors are welcome and the site is responsive for use on mobile, tablet, and even large screen devices such as laptop or desktop computers. However, the majority of Users will be accessing the site from a mobile device by a huge margin. And due to the nature of the events, it's likely if not intended that Organizers will use the site from their mobile device as well. For this reason, the site is intentionally very simple in design, with simple colors and high contrast buttons so that it is easy to see, read, and use.

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

Wireframes were built in Balsamiq's online application. One wireframe was made for all size of device, as it was intentional from the beginning that the site remain cohesive and similar across all platforms. Like many popular social media platforms, the site is geared around a vertical scroll.

<details>
<summary>Index Page Wireframe</summary>
<br>

![Main, index page](/assets/readme-images/WF1Index.png)

</details>

<details>
<summary>Index Page Wireframe</summary>
<br>

![Your Events page](/assets/readme-images/WF2YourEvents.png)

</details>

<details>
<summary>Index Page Wireframe</summary>
<br>

![Your Organized Events page](/assets/readme-images/WF3Organized.png)

</details>

<details>
<summary>Index Page Wireframe</summary>
<br>

![Event Detail page](/assets/readme-images/WF4Detail.png)

</details>

<details>
<summary>Index Page Wireframe</summary>
<br>

![Event Create and Edit pages](/assets/readme-images/WF5Create.png)

</details>

<details>
<summary>Index Page Wireframe</summary>
<br>

![Attendee printable page](/assets/readme-images/WF6Attendee.png)

</details>
<br>

<hr>

## Features

<hr>

👩🏻‍💻 View an example of a completed user experience section [here](https://github.com/kera-cudmore/TheQuizArms#Features)

This section can be used to explain what pages your site is made up of.

### General features on each page

If there is a feature that appears on all pages of your site, include it here. Examples of what to include would the the navigation, a footer and a favicon.

I then like to add a screenshot of each page of the site here, i use [amiresponsive](https://ui.dev/amiresponsive) which allows me to grab an image of the site as it would be displayed on mobile, tablet and desktop, this helps to show the responsiveness of the site.

### Future Implementations

What features would you like to implement in the future on your site? Would you like to add more pages, or create login functionality? Add these plans here.

### Accessibility

Be an amazing developer and get used to thinking about accessibility in all of your projects!

This is the place to make a note of anything you have done with accessibility in mind. Some examples include:

Have you used icons and added aria-labels to enable screen readers to understand these?
Have you ensured your site meets the minimum contrast requirements?
Have you chosen fonts that are dyslexia/accessible friendly?

Code Institute have an amazing channel for all things accessibility (a11y-accessibility) I would highly recommend joining this channel as it contains a wealth of information about accessibility and what we can do as developers to be more inclusive.

## Technologies Used

👩🏻‍💻 View an example of a completed Technologies Used section [here](https://github.com/kera-cudmore/Bully-Book-Club#Technologies-Used)

### Languages Used

Make a note here of all the languages used in creating your project. For the first project this will most likely just be HTML & CSS.

### Frameworks, Libraries & Programs Used

Add any frameworks, libraries or programs used while creating your project.

Make sure to include things like git, GitHub, the program used to make your wireframes, any programs used to compress your images, did you use a CSS framework like Bootstrap? If so add it here (add the version used).

A great tip for this section is to include them as you use them, that way you won't forget what you ended up using when you get to the end of your project.

## Deployment & Local Development

👩🏻‍💻 View an example of a completed Deployment & Local Development section [here](https://github.com/kera-cudmore/TheQuizArms#Deployment)

### Deployment

Include instructions here on how to deploy your project. For your first project you will most likely be using GitHub Pages.

### Local Development

The local development section gives instructions on how someone else could make a copy of your project to play with on their local machine. This section will get more complex in the later projects, and can be a great reference to yourself if you forget how to do this.

#### How to Fork

Place instructions on how to fork your project here.

#### How to Clone

Place instructions on how to clone your project here.

## Testing

Start as you mean to go on - and get used to writing a TESTING.md file from the very first project!

Testing requirements aren't massive for your first project, however if you start using a TESTING.md file from your first project you will thank yourself later when completing your later projects, which will contain much more information.
  
Use this part of the README to link to your TESTING.md file - you can view the example TESTING.md file [here](milestone1-testing.md)

## Credits

👩🏻‍💻 View an example of a completed Credits section [here](https://github.com/kera-cudmore/BookWorm#Credits)

The Credits section is where you can credit all the people and sources you used throughout your project.

### Code Used

If you have used some code in your project that you didn't write, this is the place to make note of it. Credit the author of the code and if possible a link to where you found the code. You could also add in a brief description of what the code does, or what you are using it for here.

### Content

Who wrote the content for the website? Was it yourself - or have you made the site for someone and they specified what the site was to say? This is the best place to put this information.

###  Media

If you have used any media on your site (images, audio, video etc) you can credit them here. I like to link back to the source where I found the media, and include where on the site the image is used.
  
###  Acknowledgments

If someone helped you out during your project, you can acknowledge them here! For example someone may have taken the time to help you on slack with a problem. Pop a little thank you here with a note of what they helped you with (I like to try and link back to their GitHub or Linked In account too). This is also a great place to thank your mentor and tutor support if you used them.