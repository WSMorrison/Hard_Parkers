# The Hardparkers

The HardParkers website is is a simple, streamlined, and mobile focused resource for automotive enthusiasts to find meets and shows they would like to attend in their area. It allows event organizers to publish their event details and for participants to register to attend, making it simple for organizers to get the word out and easy for enthusiasts to find events that match their interests.

This ReadMe will discuss the testing of the app. Some of the information can also be found on the main ReadMe, but this Testing ReadMe will go into greater detail about the systematic manual testing.

The site was tested as an unlogged-in visitor, as a logged-in basic user (User), as a logged-in event promoter and organizer (Organizer), and as a logged in the site owner or admin (Owner). Much of the functionality was the same or similar, but permissions were different and there were different aspects of the project that required different aspects of testing.

The main ReadMe can be found [here.](/README.md)

### The deployed site can be found here: [The HardParkers](https://hardparkers.herokuapp.com/)

<br>
<hr>

## Contents

<hr>

- [Testing](#testing)
  - [Responsiveness](#responsiveness)
  - [Accessibility](#accessibility)
  - [Code Validation](#code-validation)
  - [Systematic Manual Testing](#systematic-manual-testing)
    - [Unlogged-in user](#unlogged-in-user)
      - [Index page](#index-page-unlogged-in-user)
      - [Log In page](#log-in-page-unlogged-in-user)
      - [Sign Up page](#sign-up-page-unlogged-in-user)
      - [Details page](#details-page-unlogged-in-user)
    - [Basic Site User](#basic-site-user)
      - [Index page](#index-page-user)
      - [Attending Events page](#attending-events-page-user)
      - [Log Out page](#log-out-page-organizer)
      - [Details page](#details-page-user)
      - [Thank you for registering page](#thank-you-for-registering-page-user)
      - [Thank you for unregistering page](#thank-you-for-unregistering-page-user)
    - [Event Organizer](#event-organizer)
      - [Index page](#index-page-organizer)
      - [Attending Events page](#attending-events-page-organizer)
      - [Organized Events page](#organized-events-page-organizer)
      - [LogOut page](#log-out-page-organizer)
      - [Details page](#details-page-organizer)
      - [Thank you for registering page](#thank-you-for-registering-page-organizer)
      - [Thank you for unregistering page](#thank-you-for-unregistering-page-organizer)
      - [Create Event page](#create-event-page-organizer)
      - [Attendee page](#attendee-page-organizer)
      - [Edit Event page](#edit-event-page-organizer)
      - [Delete Event confirmation page](#delete-event-confirmation-page-organizer)
      - [Thank you for creating your event page](#thank-you-for-creating-your-event-page-organizer)
      - [Thank you for deleting your event page](#thank-you-for-deleting-your-event-page-organizer)
    - [Site Owner](#site-owner)
      - [Index page](#index-page-owner)
      - [Attending Events page](#attending-events-page-owner)
      - [Organized Events page](#organized-events-page-owner)
      - [Owner Control Panel page](#owner-control-panel-page-owner)
      - [LogOut page](#log-out-page-owner)
      - [Details page](#details-page-owner)
      - [Thank you for registering page](#thank-you-for-registering-page-owner)
      - [Thank you for unregistering page](#thank-you-for-unregistering-page-owner)
      - [Create Event page](#create-event-page-owner)
      - [Attendee page](#attendee-page-owner)
      - [Edit Event page](#edit-event-page-owner)
      - [Delete Event confirmation page](#delete-event-confirmation-page-owner)
      - [Thank you for creating your event page](#thank-you-for-creating-your-event-page-owner)
      - [Thank you for deleting your event page](#thank-you-for-deleting-your-event-page-owner)
      - [Admin Panel](#admin-panel-owner)
  - [Representative User Manual Testing](#representative-user-manual-testing)
  - [Bugs](#bugs)
      - [Fixed bugs](#fixed-bugs)
      - [Unfixed bugs](#unfixed-bugs)

<br>
<hr>

## Testing

<hr>

## Responsiveness

The page was checked for responsiveness by using [AmIResponsive.](https://ui.dev/amiresponsive)

![Front page of The HardParkers as input to AmIResponsive.](/assets/readme-images/Responsive.png)

## Accessibility

Care was taken to make sure the website was accessible.

  - The page is developed to use high contrast text, simple interface and easy to follow buttons. 
  - Aria labels are on any button that is not labelled.
  - The tabs are all marked current so that the nav bar indicates where the user is currently navigated. 
  - The HTML follows a clear semantic flow.

Accessibility was checked by using Google Chrome [Lighthouse.](https://chrome.google.com/webstore/detail/lighthouse/)

![Lighthouse score for page](/assets/readme-images/Lighthouse.png)

The accessibility score is less than 100% because the "Background and foreground colors do not have a sufficient contrast ratio," however, changing the colors did not seem to make any difference in the score.

## Code Validation

The HTML for the website was put through the [W3C Markup Validation Service](https://validator.w3.org/#validate_by_input). Each page of the site was tested by opening the page, viewing page source, and copying and pasting the source code into the validator. This avoided any issues with the template tags upsetting the validator to the point that it did not check the rest of the code. Any errors found were fixed. As credit to Django's automated page generation through template tags, the only errors were in the hand written code of the base.html; a stray closing italic tag in the footer, and an attempt at a responsive break in the blockquote to try to influence the line break that did not have any effect. Both were fixed, and each page was returned without errors.

![W3C Markup validator representative return](/assets/readme-images/W3CHTMLValidator.png)

The CSS was put through the [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/). The short, hand written CSS file checked without errors.

![W3C CSS validator representative return](/assets/readme-images/W3CCSSValidator.png)

The Python code was checked with the [Code Institute Python linter](https://pep8ci.herokuapp.com/). Each hand written python file was checked with the linter; forms.py, models.py, urls.py, and views.py. Each was returned without errors.

![CI Python linter representative return](/assets/readme-images/CIPythonLinter.png)

<br>
<hr>

## Systematic Manual Testing

<hr>

The following tables will describe the systematic manual testing done to ensure that the app is working properly.

<hr>

### Unlogged-in User

<hr>

The following features were tested as an unlogged-in user:

#### Index page (Unlogged-in User):

| Element                 | Action   | Expected Result                                                        | Outcome |
|-------------------------|----------|------------------------------------------------------------------------|---------|
| Splash Image            | Hover    | Indicate link                                                          | Pass    |
| Splash Image            | Click    | Navigate to home tab                                                   | Pass    |
| Nav Bar                 | Display  | Show All, Log In, Sign Up tabs                                         | Pass    |
| Nav Bar                 | Display  | Indicate navigated tab                                                 | Pass    |
| Footer                  | Display  | Display social meda links                                              | Pass    |
| Footer                  | Display  | Display famous Socrates quote                                          | Pass    |
| Social media links      | Hover    | Indicate link                                                          | Pass    |
| Social media links      | Click    | Open appropriate social media in new browser tab                       | Pass    |
| All Upcoming Events tab | Display  | Display upcoming events                                                | Pass    |
| All Upcoming Events tab | Display  | Display upcoming events with the soonest first                         | Pass    |
| All Upcoming Events tab | Display  | Display selected details of appropriate event record                   | Pass    |
| All Upcoming Events tab | Paginate | Paginate after 5 events                                                | Pass    |
| All Upcoming Events tab | Paginate | Navigate through pagination pages                                      | Pass    |
| All Upcoming Events tab | Display  | Display Details button                                                 | Pass    |
| All Upcoming Events tab | Display  | Does not display events that happened before today                     | Pass    |
| Details button          | Hover    | Indicate link                                                          | Pass    |
| Details button          | Click    | Navigate to eventview page and display details of correct event record | Pass    |
| Log In tab - nav bar    | Hover    | Indicate link                                                          | Pass    |
| Log In tab - nav bar    | Click    | Navigate to Log In page as site tab                                    | Pass    |
| Sign Up tab - nav bar   | Hover    | Indicate link                                                          | Pass    |
| Sign Up tab - nav bar   | Click    | Navigate to Sign Up page as site tab                                   | Pass    |

#### Log In page (Unlogged-in User):

| Element              | Action  | Expected Result                             | Outcome   |
|----------------------|---------|---------------------------------------------|-----------|
| Header and footer    | Display | Consistent with all other pages             | Pass      |
| Nav Bar              | Display | Indicate navigated tab                      | Pass      |
| Username Field       | Hover   | Indicate textfield                          | Pass      |
| Username Field       | Input   | Cleans input                                | Pass      |
| Username Field       | Input   | Validates input                             | Pass      |
| Username Field       | Input   | Accepts good input                          | Pass      |
| Password Field       | Hover   | Incidcates textfield                        | Pass      |
| Password Field       | Input   | Cleans input                                | Pass      |
| Password Field       | Input   | Validates input                             | Pass      |
| Password Field       | Input   | Accepts good input                          | Pass      |
| Password Field       | Input   | Obscures keystrokes                         | Pass      |
| Remember Me checkbox | Click   | Checks box                                  | Pass      |
| Remember Me checkbox | Clicked | Remembers user (When allowed by browser)    | Pass      |
| Log In button        | Hover   | Indicate link                               | Pass      |
| Log In button        | Click   | Logs user in, navigates to index page       | Pass      |
| Sign Up Here link    | Hover   | Indicate link                               | Pass      |
| Sign Up Here link    | Click   | Navigate to Sign Up tab                     | Pass      |

#### Sign Up page (Unlogged-in User):

| Element              | Action  | Expected Result                             | Outcome |
|----------------------|---------|---------------------------------------------|---------|
| Header and footer    | Display | Consistent with all other pages             | Pass    |
| Nav bar              | Display | Indicate navigated tab                      | Pass    |
| Username Field       | Hover   | Indicates textfield                         | Pass    |
| Username Field       | Input   | Cleans input                                | Pass    |
| Username Field       | Input   | Validates input                             | Pass    |
| Unsername Field      | Input   | Accepts input                               | Pass    |
| E-mail Field         | Display | Indicates optional                          | Pass    |
| E-mail Field         | Hover   | Indicates textfield                         | Pass    |
| E-mail Field         | Input   | Cleans input                                | Pass    |
| E-mail Field         | Input   | Validates input                             | Pass    |
| E-mail Field         | Input   | Accepts input                               | Pass    |
| Password Field       | Hover   | Indicates textfield                         | Pass    |
| Password Field       | Input   | Cleans input                                | Pass    |
| Password Field       | Input   | Validates input                             | Pass    |
| Password Field       | Input   | Accepts input                               | Pass    |
| Password Again Field | Hover   | Indicates textfield                         | Pass    |
| Password Again Field | Input   | Cleans input                                | Pass    |
| Password Again Field | Input   | Validates input                             | Pass    |
| Password Again Field | Input   | Accepts input                               | Pass    |
| Password Again Field | Input   | Checks Password Again against Password      | Pass    |
| Sign Up button       | Hover   | Indicate link                               | Pass    |
| Sign Up button       | Click   | Adds user to database                       | Pass    |
| Sign Up button       | Click   | Logs user in, navigates to main, index page | Pass    |
| Log In Here link     | Hover   | Indicate link                               | Pass    |
| Log In Here link     | Click   | Navigate to Log In tab                      | Pass    |

#### Details page (Unlogged-in User)

| Element                | Action  | Expected Result                                                    | Outcome |
|------------------------|---------|--------------------------------------------------------------------|---------|
| Header and footer      | Display | Consistent with all other pages                                    | Pass    |
| Details page           | Display | Title for correct event record                                     | Pass    |
| Details page           | Display | Location for correct event record                                  | Pass    |
| Details page           | Display | Date for correct event record                                      | Pass    |
| Details page           | Display | Registration close date for correct event record                   | Pass    |
| Details page           | Display | Username of event organizer                                        | Pass    |
| Details page           | Display | Number of cars able to register                                    | Pass    |
| Details page           | Display | About this event text box                                          | Pass    |
| Location Map button    | Hover   | Indicate link                                                      | Pass    |
| Location Map button    | Click   | Open Google Maps link in new browser tab, for correct event record | Pass    |
| Login to register link | Hover   | Indicate link                                                      | Pass    |
| Login to register link | Click   | Navigate to Log In page as site tab                                | Pass    |

<hr>

### Basic Site User

<hr>

The following features were tested while logged in as a User.

#### Index page (User):

| Element                 | Action   | Expected Result                                                        | Outcome |
|-------------------------|----------|------------------------------------------------------------------------|---------|
| Splash Image            | Hover    | Indicate link                                                          | Pass    |
| Splash Image            | Click    | Navigate to home tab                                                   | Pass    |
| Nav Bar                 | Display  | Show All, Attending, Log Out tabs                                      | Pass    |
| Nav Bar                 | Display  | Indicate navigated tab                                                 | Pass    |
| Footer                  | Display  | Display social meda links                                              | Pass    |
| Footer                  | Display  | Display famous Socrates quote                                          | Pass    |
| Social media links      | Hover    | Indicate link                                                          | Pass    |
| Social media links      | Click    | Open appropriate social media in new browser tab                       | Pass    |
| All Upcoming Events tab | Display  | Display upcoming events                                                | Pass    |
| All Upcoming Events tab | Display  | Display upcoming events with the soonest first                         | Pass    |
| All Upcoming Events tab | Display  | Display selected details of appropriate event record                   | Pass    |
| All Upcoming Events tab | Paginate | Paginate after 5 events                                                | Pass    |
| All Upcoming Events tab | Paginate | Navigate through pagination pages                                      | Pass    |
| All Upcoming Events tab | Display  | Display Details button                                                 | Pass    |
| All Upcoming Events tab | Display  | Does not display events that happened before today                     | Pass    |
| Details button          | Hover    | Indicate link                                                          | Pass    |
| Details button          | Click    | Navigate to eventview page and display details of correct event record | Pass    |

#### Attending Events page (User):

| Element                 | Action   | Expected Result                                                        | Outcome |
|-------------------------|----------|------------------------------------------------------------------------|---------|
| Header and footer       | Display  | Consistent with all other pages                                        | Pass    |
| Nav Bar                 | Display  | Indicated navigated tab                                                | Pass    |
| Attending Events tab    | Display  | Display attending events                                               | Pass    |
| Attending Events tab    | Display  | Display attending events with the soonest first                        | Pass    |
| Attending Events tab    | Display  | Display selected details of appropriate event record                   | Pass    |
| Attending Events tab    | Paginate | Paginate after 5 events                                                | Pass    |
| Attending Events tab    | Paginate | Navigate through pagination pages                                      | Pass    |
| Attending Events tab    | Display  | Display Details button                                                 | Pass    |
| All Upcoming Events tab | Display  | Does not display events that happened before today                     | Pass    |
| Details button          | Hover    | Indicate link                                                          | Pass    |
| Details button          | Click    | Navigate to eventview page and display details of correct event record | Pass    |

#### Log Out page (User):

| Element           | Action  | Expected Result                   | Outcome |
|-------------------|---------|-----------------------------------|---------|
| Header and footer | Display | Consistent with all other pages   | Pass    |
| Nav bar           | Display | Indicate navigated tab            | Pass    |
| Log Out button    | Hover   | Indicate link                     | Pass    |
| Log Out button    | Click   | Log user out                      | Pass    |
| Log Out button    | Click   | Redirect user to main, index page | Pass    |

#### Details page (User):

| Element              | Action  | Expected Result                                                    | Outcome |
|----------------------|---------|--------------------------------------------------------------------|---------|
| Header and footer    | Display | Consistent with all other pages                                    | Pass    |
| Details page         | Display | Title for correct event record                                     | Pass    |
| Details page         | Display | Location for correct event record                                  | Pass    |
| Details page         | Display | Date for correct event record                                      | Pass    |
| Details page         | Display | Registration close date for correct event record                   | Pass    |
| Details page         | Display | Username of event organizer                                        | Pass    |
| Details page         | Display | Number of cars able to register                                    | Pass    |
| Details page         | Display | About this event text box                                          | Pass    |
| Location Map button  | Hover   | Indicate link                                                      | Pass    |
| Location Map button  | Click   | Open Google Maps link in new browser tab, for correct event record | Pass    |

If registered for event and event is in the future:

| Element              | Action  | Expected Result                                                    | Outcome |
|----------------------|---------|--------------------------------------------------------------------|---------|
| Remove Me button     | Hover   | Indicate link                                                      | Pass    |
| Remove Me button     | Click   | Remove user from correct event record attendee list                | Pass    |
| Remove Me button     | Click   | Redirect user to thank you page                                    | Pass    |

If not registered for event and event and Registration Closed Date are in the future:

| Element              | Action  | Expected Result                                                    | Outcome |
|----------------------|---------|--------------------------------------------------------------------|---------|
| Register Now! button | Hover   | Indicate link                                                      | Pass    |
| Register Now! button | Click   | Add user to correct event record attendee list                     | Pass    |
| Register Now! button | Click   | Redirect user to thank you page                                    | Pass    |

If not registered, Registration Closed Date has passed, and event date is in the future:

| Element              | Action  | Expected Result                                                    | Outcome |
|----------------------|---------|--------------------------------------------------------------------|---------|
| Registration button  | Renders | Inactive                                                           | Pass    |
| Registration button  | Display | Registration closed                                                | Pass    |
| Registration button  | Hover   | No action                                                          | Pass    |
| Registration button  | Click   | No action                                                          | Pass    |

If not registered, event has reached maximum registration, and event date is in the future:

| Element              | Action  | Expected Result                                                    | Outcome |
|----------------------|---------|--------------------------------------------------------------------|---------|
| Registration button  | Renders | Inactive                                                           | Pass    |
| Registration button  | Display | Registration closed                                                | Pass    |
| Registration button  | Hover   | No action                                                          | Pass    |
| Registration button  | Click   | No action                                                          | Pass    |

#### Thank you for registering page (User):

| Element                          | Action  | Expected Result                                  | Outcome |
|----------------------------------|---------|--------------------------------------------------|---------|
| Header and footer                | Display | Consistent with all other pages                  | Pass    |
| Thank you for registering page   | Display | Thank correct site user for registering          | Pass    |
| Thank you for registering page   | Display | Confirm user is registered for event             | Pass    |
| View Your Events! button         | Hover   | Indicate link                                    | Pass    |
| View Your Events! button         | Click   | Navigate user to list of their registered events | Pass    |

#### Thank you for unregistering page (User):

| Element                          | Action  | Expected Result                                  | Outcome |
|----------------------------------|---------|--------------------------------------------------|---------|
| Header and footer                | Display | Consistent with all other pages                  | Pass    |
| Thank you for unregistering page | Display | Thank correct site user for unregistering        | Pass    |
| Thank you for registering page   | Display | Confirm user is no longer registered for event   | Pass    |
| Check Out Other Events! button   | Hover   | Indicate link                                    | Pass    |
| Check Out Other Events! button   | Click   | Navigate user to list of all upcoming events     | Pass    |

<hr>

### Event Organizer

<hr>

The following features were tested while logged in as an Organizer.

#### Index page (Organizer):

| Element                 | Action   | Expected Result                                                        | Outcome |
|-------------------------|----------|------------------------------------------------------------------------|---------|
| Splash Image            | Hover    | Indicate link                                                          | Pass    |
| Splash Image            | Click    | Navigate to home tab                                                   | Pass    |
| Nav Bar                 | Display  | Show All, Attending, Log Out tabs                                      | Pass    |
| Nav Bar                 | Display  | Indicate navigated tab                                                 | Pass    |
| Footer                  | Display  | Display social meda links                                              | Pass    |
| Footer                  | Display  | Display famous Socrates quote                                          | Pass    |
| Social media links      | Hover    | Indicate link                                                          | Pass    |
| Social media links      | Click    | Open appropriate social media in new browser tab                       | Pass    |
| All Upcoming Events tab | Display  | Display upcoming events                                                | Pass    |
| All Upcoming Events tab | Display  | Display upcoming events with the soonest first                         | Pass    |
| All Upcoming Events tab | Display  | Display selected details of appropriate event record                   | Pass    |
| All Upcoming Events tab | Paginate | Paginate after 5 events                                                | Pass    |
| All Upcoming Events tab | Paginate | Navigate through pagination pages                                      | Pass    |
| All Upcoming Events tab | Display  | Display Details button                                                 | Pass    |
| Details button          | Hover    | Indicate link                                                          | Pass    |
| Details button          | Click    | Navigate to eventview page and display details of correct event record | Pass    |

#### Attending Events page (Organizer):

| Element                 | Action   | Expected Result                                                        | Outcome |
|-------------------------|----------|------------------------------------------------------------------------|---------|
| Header and footer       | Display  | Consistent with all other pages                                        | Pass    |
| Nav Bar                 | Display  | Indicate navigated tab                                                 | Pass    |
| Attending Events tab    | Display  | Display attending events                                               | Pass    |
| Attending Events tab    | Display  | Display attending events with the soonest first                        | Pass    |
| Attending Events tab    | Display  | Display selected details of appropriate event record                   | Pass    |
| Attending Events tab    | Paginate | Paginate after 5 events                                                | Pass    |
| Attending Events tab    | Paginate | Navigate through pagination pages                                      | Pass    |
| Attending Events tab    | Display  | Display Details button                                                 | Pass    |
| Details button          | Hover    | Indicate link                                                          | Pass    |
| Details button          | Click    | Navigate to eventview page and display details of correct event record | Pass    |

#### Organized Events page (Organizer):

| Element                 | Action    | Expected Result                                        | Outcome |
|-------------------------|-----------|--------------------------------------------------------|---------|
| Header and footer       | Display   | Consistent with all other pages                        | Pass    |
| Nav Bar                 | Display   | Indicate navigated tab                                 | Pass    |
| Organize New Event card | Display   | Display separated card for creating a new event        | Pass    |
| Organize New Event card | Display   | Display Create Event button                            | Pass    |
| Create Event button     | Hover     | Indicate link                                          | Pass    |
| Create Event button     | Click     | Navigate to create event form                          | Pass    |
| Organized Events tab    | Display   | Display organized events                               | Pass    |
| Organized Events tab    | Display   | Display organized events with the soonest events first | Pass    |
| Organized Events tab    | Display   | Display selected details of appropriate event record   | Pass    |
| Organized Events tab    | Paginate  | Paginate after 5 events                                | Pass    |
| Organized Events tab    | Paginate  | Navigate through pagination pages                      | Pass    |
| Organized Events tab    | Display   | Display Attendee List button on event cards            | Pass    |
| Attendee List button    | Hover     | Indicate link                                          | Pass    |
| Attendee List button    | Click     | Navigate to attendee list page in new browser tab      | Pass    |
| Organized Events tab    | Display   | Display Edit button on event cards                     | Pass    |
| Edit button             | Hover     | Indicate link                                          | Pass    |
| Edit button             | Click     | Navigate to event edit form                            | Pass    |
| Organized Events tab    | Display   | Display Delete button on event cards                   | Pass    |
| Delete button           | Hover     | Indicate link                                          | Pass    |
| Delete button           | Click     | Navigate to delete confirmation page                   | Pass    |

#### Log Out page (Organizer):

| Element           | Action  | Expected Result                   | Outcome |
|-------------------|---------|-----------------------------------|---------|
| Header and footer | Display | Consistent with all other pages   | Pass    |
| Nav bar           | Display | Indicate navigated tab            | Pass    |
| Log Out button    | Hover   | Indicate link                     | Pass    |
| Log Out button    | Click   | Log user out                      | Pass    |
| Log Out button    | Click   | Redirect user to main, index page | Pass    |

#### Details page (Organizer):

| Element              | Action  | Expected Result                                                    | Outcome |
|----------------------|---------|--------------------------------------------------------------------|---------|
| Header and footer    | Display | Consistent with all other pages                                    | Pass    |
| Details page         | Display | Title for correct event record                                     | Pass    |
| Details page         | Display | Location for correct event record                                  | Pass    |
| Details page         | Display | Date for correct event record                                      | Pass    |
| Details page         | Display | Registration close date for correct event record                   | Pass    |
| Details page         | Display | Username of event organizer                                        | Pass    |
| Details page         | Display | Number of cars able to register                                    | Pass    |
| Details page         | Display | About this event text box                                          | Pass    |
| Location Map button  | Hover   | Indicate link                                                      | Pass    |
| Location Map button  | Click   | Open Google Maps link in new browser tab, for correct event record | Pass    |

If registered for event and event is in the future:

| Element              | Action  | Expected Result                                                    | Outcome |
|----------------------|---------|--------------------------------------------------------------------|---------|
| Remove Me button     | Hover   | Indicate link                                                      | Pass    |
| Remove Me button     | Click   | Remove user from correct event record attendee list                | Pass    |
| Remove Me button     | Click   | Redirect user to thank you page                                    | Pass    |

If not registered for event and event and Registration Closed Date are in the future:

| Element              | Action  | Expected Result                                                    | Outcome |
|----------------------|---------|--------------------------------------------------------------------|---------|
| Register Now! button | Hover   | Indicate link                                                      | Pass    |
| Register Now! button | Click   | Add user to correct event record attendee list                     | Pass    |
| Register Now! button | Click   | Redirect user to thank you page                                    | Pass    |

If not registered, Registration Closed Date has passed, and event date is in the future:

| Element              | Action  | Expected Result                                                    | Outcome |
|----------------------|---------|--------------------------------------------------------------------|---------|
| Registration button  | Renders | Inactive                                                           | Pass    |
| Registration button  | Display | Registration closed                                                | Pass    |
| Registration button  | Hover   | No action                                                          | Pass    |
| Registration button  | Click   | No action                                                          | Pass    |

If not registered, event has reached maximum registration, and event date is in the future:

| Element              | Action  | Expected Result                                                    | Outcome |
|----------------------|---------|--------------------------------------------------------------------|---------|
| Registration button  | Renders | Inactive                                                           | Pass    |
| Registration button  | Display | Registration closed                                                | Pass    |
| Registration button  | Hover   | No action                                                          | Pass    |
| Registration button  | Click   | No action                                                          | Pass    |

#### Thank you for registering page (Organizer):

| Element                          | Action  | Expected Result                                  | Outcome |
|----------------------------------|---------|--------------------------------------------------|---------|
| Header and footer                | Display | Consistent with all other pages                  | Pass    |
| Thank you for registering page   | Display | Thank correct site user for registering          | Pass    |
| Thank you for registering page   | Display | Confirm user is registered for event             | Pass    |
| View Your Events! button         | Hover   | Indicate link                                    | Pass    |
| View Your Events! button         | Click   | Navigate user to list of their registered events | Pass    |

#### Thank you for unregistering page (Organizer):

| Element                          | Action  | Expected Result                                  | Outcome |
|----------------------------------|---------|--------------------------------------------------|---------|
| Header and footer                | Display | Consistent with all other pages                  | Pass    |
| Thank you for unregistering page | Display | Thank correct site user for unregistering        | Pass    |
| Thank you for registering page   | Display | Confirm user is no longer registered for event   | Pass    |
| Check Out Other Events! button   | Hover   | Indicate link                                    | Pass    |
| Check Out Other Events! button   | Click   | Navigate user to list of all upcoming events     | Pass    |

#### Create Event page (Organizer):

| Element                        | Action  | Expected Result                                                                   | Outcome   |
|--------------------------------|---------|-----------------------------------------------------------------------------------|-----------|
| Header and footer              | Display | Consistent with all other pages                                                   | Pass      |
| Form                           | Display | Form label: Add your event here.                                                  | Pass      |
| Event Name field               | Display | Label: Your event name:                                                           | Pass      |
| Event Name field               | Hover   | Indicates textfield                                                               | Pass      |
| Event Name field               | Input   | Cleans input                                                                      | Pass      |
| Event Name field               | Input   | Validates input                                                                   | Pass      |
| Event Name field               | Input   | Accepts input                                                                     | Pass      |
| Event Name field               | Input   | Checks event name against other event names in event objects to ensure its unique | Pass      |
| Event Name field               | Input   | Prevents form from posting and tells user if field is blank or invalid            | Pass      |
| Event Name field               | Input   | Prevents form from posting and tells user if name is not unique                   | Pass      |
| Event Date field               | Display | Label: The event date:                                                            | Pass      |
| Event Date field               | Input   | Option for manual input or date picker                                            | Pass      |
| Event Date field               | Input   | Date picker checks manual input date is in the future                             | Pass      |
| Event Date field               | Input   | Date picker excludes dates in the past                                            | Pass      |
| Event Date field               | Input   | Prevents form from posting and tells user if field is invalid or blank            | Pass      |
| Event Date field               | Input   | Prevents form from posting and tells user if date is not in the future            | Pass      |
| Event Time field               | Display | Label: At time:                                                                   | Pass      |
| Event Time field               | Display | Placeholder is default time as design nudge                                       | Pass      |
| Event Time field               | Input   | Accepts default placeholder time unedited                                         | Pass      |
| Event Time field               | Input   | Validates time                                                                    | Pass      |
| Event Time field               | Input   | Prevents form from posting and tells user if field is invalid or blank            | Pass      |
| Registration Closes field      | Display |  Label: Registration closes:                                                      | Pass      |
| Registration Closes field      | Input   | Option for manual input of date picker                                            | Pass      |
| Registration Closes field      | Input   | Date picker checks manual input date is in the future                             | Pass      |
| Registration Closes field      | Input   | Date picker excludes dates in the past                                            | Pass      |
| Registration Closes field      | Input   | Prevents form from posting and tells user if field is invalid or blank            | Pass      |
| Registration Closes field      | Input   | Prevents form from posting if date is not in the future                           | Pass      |
| Reg. Closes Time field         | Display | Label: At time:                                                                   | Pass      |
| Reg. Closes Time field         | Display | Placeholder is default time as design nudge                                       | Pass      |
| Reg. Closes Time field         | Input   | Accepts default placeholder time undedited                                        | Pass      |
| Reg. Closes Time field         | Input   | Validates time                                                                    | Pass      |
| Reg. Closes Time field         | Input   | Prevents form from posting and tells user if field is invalid or blank            | Pass      |
| Location field                 | Display | Label: The location:                                                              | Pass      |
| Location field                 | Hover   | Indicates charfield                                                               | Pass      |
| Location field                 | Input   | Cleans input                                                                      | Pass      |
| Location field                 | Input   | Validates input                                                                   | Pass      |
| Location field                 | Input   | Accepts input                                                                     | Pass      |
| Location field                 | Input   | Prevents form from posting and tells user if field is invalid or blank            | Pass      |
| Location URL field             | Display | Label: Share Google Maps link here:                                               | Pass      |
| Location URL field             | Display | Placeholder is default as design nudge                                            | Pass      |
| Location URL field             | Input   | Prevents form from posting and tells user if field is invalid or blank            | Pass      |
| Location URL field             | Input   | Defends against any input that does not start with "https://goo.gl/maps/"         | Pass      |
| Number of Cars field           | Display | Label: How many cars may register?                                                | Pass      |
| Number of Cars field           | Input   | Cleans input                                                                      | Pass      |
| Number of Cars field           | Input   | Validates input as integer and greater than 0                                     | Pass      |
| Number of Cars field           | Input   | Accepts input                                                                     | Pass      |
| Number of Cars field           | Input   | Prevents form from posting and tells user if field is invalid or blank            | Pass      |
| Event Description field        | Display | Label: Briefly describe your event:                                               | Pass      |
| Event Description field        | Input   | Cleans input                                                                      | Pass      |
| Event Description field        | Input   | Validates input                                                                   | Pass      |
| Event Description field        | Input   | Accepts input                                                                     | Pass      |
| Event Description field        | Input   | Prevents form from posting and tells user if field is invalid or blank            | Pass      |
| Publish Your Event button      | Hover   | Indicates link                                                                    | Pass      |
| Publish Your Event button      | Click   | Adds new event record to database                                                 | Pass      |
| Publish Your Event button      | Click   | Redirects user to thank you for organizing page                                   | Pass      |

#### Attendee page (Organizer):

| Element       | Action  | Expected Result                                                    | Outcome |
|---------------|---------|--------------------------------------------------------------------|---------|
| Attendee page | Open    | Opens in new browser tab                                           | Pass    |
| Attendee page | Display | Very basic Hard Parkers header                                     | Pass    |
| Attendee page | Display | Event title                                                        | Pass    |
| Attendee page | Display | Event location                                                     | Pass    |
| Attendee page | Display | Total number of registered attendees                               | Pass    |
| Attendee page | Display | Maximum number of attendees                                        | Pass    |
| Attendee page | Display | List or registered users and usernames, alphabetically by username | Pass    |
| Attendee page | Display | Footer with only famous Socrates quote                             | Pass    |

#### Edit Event page (Organizer):

| Element                        | Action  | Expected Result                                                                   | Outcome   |
|--------------------------------|---------|-----------------------------------------------------------------------------------|-----------|
| Header and footer              | Display | Consistent with all other pages                                                   | Pass      |
| Form                           | Display | Form label: Edit eventname here. with appropriate event name from event record    | Pass      |
| Event Name field               | Display | Label: Your event name:                                                           | Pass      |
| Event Name field               | Display | Placeholder is original information from appropriate event record                 | Pass      |
| Event Name field               | Hover   | Indicates textfield                                                               | Pass      |
| Event Name field               | Input   | Cleans input                                                                      | Pass      |
| Event Name field               | Input   | Validates input                                                                   | Pass      |
| Event Name field               | Input   | Accepts input                                                                     | Pass      |
| Event Name field               | Input   | Checks event name against other event names in event objects to ensure its unique | Pass      |
| Event Name field               | Input   | Prevents form from posting and tells user if field is blank or invalid            | Pass      |
| Event Name field               | Input   | Prevents form from posting and tells user if name is not unique                   | Pass      |
| Event Date field               | Display | Label: The event date:                                                            | Pass      |
| Event Date field               | Display | Placeholder is original information from appropriate event record                 | Pass      |
| Event Date field               | Input   | Option for manual input or date picker                                            | Pass      |
| Event Date field               | Input   | Date picker checks manual input date is in the future                             | Pass      |
| Event Date field               | Input   | Date picker excludes dates in the past                                            | Pass      |
| Event Date field               | Input   | Prevents form from posting and tells user if field is invalid or blank            | Pass      |
| Event Date field               | Input   | Prevents form from posting and tells user if date is not in the future            | Pass      |
| Event Time field               | Display | Label: At time:                                                                   | Pass      |
| Event Time field               | Display | Placeholder is original information from appropriate event record                 | Pass      |
| Event Time field               | Input   | Accepts default placeholder time unedited                                         | Pass      |
| Event Time field               | Input   | Validates time                                                                    | Pass      |
| Event Time field               | Input   | Prevents form from posting and tells user if field is invalid or blank            | Pass      |
| Registration Closes field      | Display | Label: Registration closes:                                                       | Pass      |
| Registration Closes field      | Display | Placeholder is original information from appropriate event record                 | Pass      |
| Registration Closes field      | Input   | Option for manual input of date picker                                            | Pass      |
| Registration Closes field      | Input   | Date picker checks manual input date is in the future                             | Pass      |
| Registration Closes field      | Input   | Date picker excludes dates in the past                                            | Pass      |
| Registration Closes field      | Input   | Prevents form from posting and tells user if field is invalid or blank            | Pass      |
| Registration Closes field      | Input   | Prevents form from posting if date is not in the future                           | Pass      |
| Reg. Closes Time field         | Display | Label: At time:                                                                   | Pass      |
| Reg. Closes Time field         | Display | Placeholder is original information from appropriate event record                 | Pass      |
| Reg. Closes Time field         | Input   | Accepts default placeholder time undedited                                        | Pass      |
| Reg. Closes Time field         | Input   | Validates time                                                                    | Pass      |
| Reg. Closes Time field         | Input   | Prevents form from posting and tells user if field is invalid or blank            | Pass      |
| Location field                 | Display | Label: The location:                                                              | Pass      |
| Location field                 | Display | Placeholder is original information from appropriate event record                 | Pass      |
| Location field                 | Hover   | Indicates charfield                                                               | Pass      |
| Location field                 | Input   | Cleans input                                                                      | Pass      |
| Location field                 | Input   | Validates input                                                                   | Pass      |
| Location field                 | Input   | Accepts input                                                                     | Pass      |
| Location field                 | Input   | Prevents form from posting and tells user if field is invalid or blank            | Pass      |
| Location URL field             | Display | Label: Share Google Maps link here:                                               | Pass      |
| Location URL field             | Display | Placeholder is original information from appropriate event record                 | Pass      |
| Location URL field             | Input   | Prevents form from posting and tells user if field is invalid or blank            | Pass      |
| Location URL field             | Input   | Defends against any input that does not start with "https://goo.gl/maps/"         | Pass      |
| Number of Cars field           | Display | Label: How many cars may register?                                                | Pass      |
| Number of Cars field           | Display | Placeholder is original information from appropriate event record                 | Pass      |
| Number of Cars field           | Input   | Cleans input                                                                      | Pass      |
| Number of Cars field           | Input   | Validates input as integer and greater than 0                                     | Pass      |
| Number of Cars field           | Input   | Accepts input                                                                     | Pass      |
| Number of Cars field           | Input   | Prevents form from posting and tells user if field is invalid or blank            | Pass      |
| Event Description field        | Display | Label: Briefly describe your event:                                               | Pass      |
| Event Description field        | Display | Placeholder is original information from appropriate event record                 | Pass      |
| Event Description field        | Input   | Cleans input                                                                      | Pass      |
| Event Description field        | Input   | Validates input                                                                   | Pass      |
| Event Description field        | Input   | Accepts input                                                                     | Pass      |
| Event Description field        | Input   | Prevents form from posting and tells user if field is invalid or blank            | Pass      |
| Publish Your Event button      | Hover   | Indicates link                                                                    | Pass      |
| Publish Your Event button      | Click   | Adds new event record to database                                                 | Pass      |
| Publish Your Event button      | Click   | Redirects user to thank you for organizing page                                   | Pass      |

#### Delete Event confirmation page (Organizer):

| Element                        | Action  | Expected Result                                               | Outcome |
|--------------------------------|---------|---------------------------------------------------------------|---------|
| Header and footer              | Display | Consistent with all other pages                               | Pass    |
| Event delete confirmation page | Display | Display confirmation of deleting the appropriate event record | Pass    |
| Take Me Back button            | Hover   | Indicate link                                                 | Pass    |
| Take Me Back button            | Click   | Redirects user to the Organized Events page                   | Pass    |
| Delete Event button            | Hover   | Indicate link                                                 | Pass    |
| Delete Event button            | Click   | Deletes appropriate event record from database                | Pass    |
| Delete Event button            | Click   | Redirects user to Thank You page                              | Pass    |

#### Thank you for creating your event page (Organizer):

| Element                       | Action  | Expected Result                                                     | Outcome |
|-------------------------------|---------|---------------------------------------------------------------------|---------|
| Header and Footer             | Display | Consistent with all other pages                                     | Pass    |
| Event creation thank you page | Display | Display thank you for appropriate user and appropriate event record | Pass    |
| Events Organized button       | Hover   | Indicate link                                                       | Pass    |
| Events Organized button       | Click   | Redirects user to the Organized Events page                         | Pass    |

#### Thank you for deleting your event page (Organizer):

| Element                     | Action  | Expected Result                                | Outcome |
|-----------------------------|---------|------------------------------------------------|---------|
| Header and footer           | Display | Consistent with all other pages                | Pass    |
| Event delete thank you page | Display | Thanks appropriate user for deleting event     | Pass    |
| Events Organized button     | Hover   | Indicate link                                  | Pass    |
| Events Organized button     | Click   | Redirects user to the Organized Events page    | Pass    |

You deserve a break.<br>
[Enjoy this bit of stand up comedy.](https://www.youtube.com/watch?v=dLECCmKnrys)
It's six and a half minutes but it's absolutely worth it.

<hr>

### Site Owner

<hr>

The following features were tested while logged in as the site Owner.

#### Index page (Owner):

| Element                 | Action   | Expected Result                                                        | Outcome |
|-------------------------|----------|------------------------------------------------------------------------|---------|
| Splash Image            | Hover    | Indicate link                                                          | Pass    |
| Splash Image            | Click    | Navigate to home tab                                                   | Pass    |
| Nav Bar                 | Display  | Show All, Attending, Log Out tabs                                      | Pass    |
| Nav Bar                 | Display  | Indicate navigated tab                                                 | Pass    |
| Footer                  | Display  | Display social meda links                                              | Pass    |
| Footer                  | Display  | Display famous Socrates quote                                          | Pass    |
| Social media links      | Hover    | Indicate link                                                          | Pass    |
| Social media links      | Click    | Open appropriate social media in new browser tab                       | Pass    |
| All Upcoming Events tab | Display  | Display upcoming events                                                | Pass    |
| All Upcoming Events tab | Display  | Display upcoming events with the soonest first                         | Pass    |
| All Upcoming Events tab | Display  | Display selected details of appropriate event record                   | Pass    |
| All Upcoming Events tab | Paginate | Paginate after 5 events                                                | Pass    |
| All Upcoming Events tab | Paginate | Navigate through pagination pages                                      | Pass    |
| All Upcoming Events tab | Display  | Display Details button                                                 | Pass    |
| Details button          | Hover    | Indicate link                                                          | Pass    |
| Details button          | Click    | Navigate to eventview page and display details of correct event record | Pass    |

#### Attending Events page (Owner):

| Element                 | Action   | Expected Result                                                        | Outcome |
|-------------------------|----------|------------------------------------------------------------------------|---------|
| Header and footer       | Display  | Consistent with all other pages                                        | Pass    |
| Nav Bar                 | Display  | Indicate navigated tab                                                 | Pass    |
| Attending Events tab    | Display  | Display attending events                                               | Pass    |
| Attending Events tab    | Display  | Display attending events with the soonest first                        | Pass    |
| Attending Events tab    | Display  | Display selected details of appropriate event record                   | Pass    |
| Attending Events tab    | Paginate | Paginate after 5 events                                                | Pass    |
| Attending Events tab    | Paginate | Navigate through pagination pages                                      | Pass    |
| Attending Events tab    | Display  | Display Details button                                                 | Pass    |
| Details button          | Hover    | Indicate link                                                          | Pass    |
| Details button          | Click    | Navigate to eventview page and display details of correct event record | Pass    |

#### Organized Events page (Owner):

| Element                 | Action    | Expected Result                                        | Outcome |
|-------------------------|-----------|--------------------------------------------------------|---------|
| Header and footer       | Display   | Consistent with all other pages                        | Pass    |
| Nav Bar                 | Display   | Indicate navigated tab                                 | Pass    |
| Organize New Event card | Display   | Display separated card for creating a new event        | Pass    |
| Organize New Event card | Display   | Display Create Event button                            | Pass    |
| Create Event button     | Hover     | Indicate link                                          | Pass    |
| Create Event button     | Click     | Navigate to create event form                          | Pass    |
| Organized Events tab    | Display   | Display organized events                               | Pass    |
| Organized Events tab    | Display   | Display organized events with the soonest events first | Pass    |
| Organized Events tab    | Display   | Display selected details of appropriate event record   | Pass    |
| Organized Events tab    | Paginate  | Paginate after 5 events                                | Pass    |
| Organized Events tab    | Paginate  | Navigate through pagination pages                      | Pass    |
| Organized Events tab    | Display   | Display Attendee List button on event cards            | Pass    |
| Attendee List button    | Hover     | Indicate link                                          | Pass    |
| Attendee List button    | Click     | Navigate to attendee list page in new browser tab      | Pass    |
| Organized Events tab    | Display   | Display Edit button on event cards                     | Pass    |
| Edit button             | Hover     | Indicate link                                          | Pass    |
| Edit button             | Click     | Navigate to event edit form                            | Pass    |
| Organized Events tab    | Display   | Display Delete button on event cards                   | Pass    |
| Delete button           | Hover     | Indicate link                                          | Pass    |
| Delete button           | Click     | Navigate to delete confirmation page                   | Pass    |

#### Owner Control Panel page (Owner):

| Element                  | Action  | Expected Result                                           | Outcome |
|--------------------------|---------|-----------------------------------------------------------|---------|
| Header and Footer        | Display | Consistent with all other pages                           | Pass    |
| Owner Control Panel page | Display | Display a message that user will be accessing admin panel | Pass    |
| Admin Panel button       | Hover   | Indicate link                                             | Pass    |
| Admin Panel button       | Click   | Redirects user to admin panel                             | Pass    |

#### Log Out page (Owner):

| Element           | Action  | Expected Result                   | Outcome |
|-------------------|---------|-----------------------------------|---------|
| Header and footer | Display | Consistent with all other pages   | Pass    |
| Nav bar           | Display | Indicate navigated tab            | Pass    |
| Log Out button    | Hover   | Indicate link                     | Pass    |
| Log Out button    | Click   | Log user out                      | Pass    |
| Log Out button    | Click   | Redirect user to main, index page | Pass    |

#### Details page (Owner):

| Element              | Action  | Expected Result                                                    | Outcome |
|----------------------|---------|--------------------------------------------------------------------|---------|
| Header and footer    | Display | Consistent with all other pages                                    | Pass    |
| Details page         | Display | Title for correct event record                                     | Pass    |
| Details page         | Display | Location for correct event record                                  | Pass    |
| Details page         | Display | Date for correct event record                                      | Pass    |
| Details page         | Display | Registration close date for correct event record                   | Pass    |
| Details page         | Display | Username of event organizer                                        | Pass    |
| Details page         | Display | Number of cars able to register                                    | Pass    |
| Details page         | Display | About this event text box                                          | Pass    |
| Location Map button  | Hover   | Indicate link                                                      | Pass    |
| Location Map button  | Click   | Open Google Maps link in new browser tab, for correct event record | Pass    |

If registered for event and event is in the future:

| Element              | Action  | Expected Result                                                    | Outcome |
|----------------------|---------|--------------------------------------------------------------------|---------|
| Remove Me button     | Hover   | Indicate link                                                      | Pass    |
| Remove Me button     | Click   | Remove user from correct event record attendee list                | Pass    |
| Remove Me button     | Click   | Redirect user to thank you page                                    | Pass    |

If not registered for event and event and Registration Closed Date are in the future:

| Element              | Action  | Expected Result                                                    | Outcome |
|----------------------|---------|--------------------------------------------------------------------|---------|
| Register Now! button | Hover   | Indicate link                                                      | Pass    |
| Register Now! button | Click   | Add user to correct event record attendee list                     | Pass    |
| Register Now! button | Click   | Redirect user to thank you page                                    | Pass    |

If not registered, Registration Closed Date has passed, and event date is in the future:

| Element              | Action  | Expected Result                                                    | Outcome |
|----------------------|---------|--------------------------------------------------------------------|---------|
| Registration button  | Renders | Inactive                                                           | Pass    |
| Registration button  | Display | Registration closed                                                | Pass    |
| Registration button  | Hover   | No action                                                          | Pass    |
| Registration button  | Click   | No action                                                          | Pass    |

If not registered, event has reached maximum registration, and event date is in the future:

| Element              | Action  | Expected Result                                                    | Outcome |
|----------------------|---------|--------------------------------------------------------------------|---------|
| Registration button  | Renders | Inactive                                                           | Pass    |
| Registration button  | Display | Registration closed                                                | Pass    |
| Registration button  | Hover   | No action                                                          | Pass    |
| Registration button  | Click   | No action                                                          | Pass    |

#### Thank you for registering page (Owner):

| Element                          | Action  | Expected Result                                  | Outcome |
|----------------------------------|---------|--------------------------------------------------|---------|
| Header and footer                | Display | Consistent with all other pages                  | Pass    |
| Thank you for registering page   | Display | Thank correct site user for registering          | Pass    |
| Thank you for registering page   | Display | Confirm user is registered for event             | Pass    |
| View Your Events! button         | Hover   | Indicate link                                    | Pass    |
| View Your Events! button         | Click   | Navigate user to list of their registered events | Pass    |

#### Thank you for unregistering page (Owner):

| Element                          | Action  | Expected Result                                  | Outcome |
|----------------------------------|---------|--------------------------------------------------|---------|
| Header and footer                | Display | Consistent with all other pages                  | Pass    |
| Thank you for unregistering page | Display | Thank correct site user for unregistering        | Pass    |
| Thank you for registering page   | Display | Confirm user is no longer registered for event   | Pass    |
| Check Out Other Events! button   | Hover   | Indicate link                                    | Pass    |
| Check Out Other Events! button   | Click   | Navigate user to list of all upcoming events     | Pass    |

#### Create Event page (Owner):

| Element                        | Action  | Expected Result                                                                   | Outcome   |
|--------------------------------|---------|-----------------------------------------------------------------------------------|-----------|
| Header and footer              | Display | Consistent with all other pages                                                   | Pass      |
| Form                           | Display | Form label: Add your event here.                                                  | Pass      |
| Event Name field               | Display | Label: Your event name:                                                           | Pass      |
| Event Name field               | Hover   | Indicates textfield                                                               | Pass      |
| Event Name field               | Input   | Cleans input                                                                      | Pass      |
| Event Name field               | Input   | Validates input                                                                   | Pass      |
| Event Name field               | Input   | Accepts input                                                                     | Pass      |
| Event Name field               | Input   | Checks event name against other event names in event objects to ensure its unique | Pass      |
| Event Name field               | Input   | Prevents form from posting and tells user if field is blank or invalid            | Pass      |
| Event Name field               | Input   | Prevents form from posting and tells user if name is not unique                   | Pass      |
| Event Date field               | Display | Label: The event date:                                                            | Pass      |
| Event Date field               | Input   | Option for manual input or date picker                                            | Pass      |
| Event Date field               | Input   | Date picker checks manual input date is in the future                             | Pass      |
| Event Date field               | Input   | Date picker excludes dates in the past                                            | Pass      |
| Event Date field               | Input   | Prevents form from posting and tells user if field is invalid or blank            | Pass      |
| Event Date field               | Input   | Prevents form from posting and tells user if date is not in the future            | Pass      |
| Event Time field               | Display | Label: At time:                                                                   | Pass      |
| Event Time field               | Display | Placeholder is default time as design nudge                                       | Pass      |
| Event Time field               | Input   | Accepts default placeholder time unedited                                         | Pass      |
| Event Time field               | Input   | Validates time                                                                    | Pass      |
| Event Time field               | Input   | Prevents form from posting and tells user if field is invalid or blank            | Pass      |
| Registration Closes field      | Display |  Label: Registration closes:                                                      | Pass      |
| Registration Closes field      | Input   | Option for manual input of date picker                                            | Pass      |
| Registration Closes field      | Input   | Date picker checks manual input date is in the future                             | Pass      |
| Registration Closes field      | Input   | Date picker excludes dates in the past                                            | Pass      |
| Registration Closes field      | Input   | Prevents form from posting and tells user if field is invalid or blank            | Pass      |
| Registration Closes field      | Input   | Prevents form from posting if date is not in the future                           | Pass      |
| Reg. Closes Time field         | Display | Label: At time:                                                                   | Pass      |
| Reg. Closes Time field         | Display | Placeholder is default time as design nudge                                       | Pass      |
| Reg. Closes Time field         | Input   | Accepts default placeholder time undedited                                        | Pass      |
| Reg. Closes Time field         | Input   | Validates time                                                                    | Pass      |
| Reg. Closes Time field         | Input   | Prevents form from posting and tells user if field is invalid or blank            | Pass      |
| Location field                 | Display | Label: The location:                                                              | Pass      |
| Location field                 | Hover   | Indicates charfield                                                               | Pass      |
| Location field                 | Input   | Cleans input                                                                      | Pass      |
| Location field                 | Input   | Validates input                                                                   | Pass      |
| Location field                 | Input   | Accepts input                                                                     | Pass      |
| Location field                 | Input   | Prevents form from posting and tells user if field is invalid or blank            | Pass      |
| Location URL field             | Display | Label: Share Google Maps link here:                                               | Pass      |
| Location URL field             | Display | Placeholder is default as design nudge                                            | Pass      |
| Location URL field             | Input   | Prevents form from posting and tells user if field is invalid or blank            | Pass      |
| Location URL field             | Input   | Defends against any input that does not start with "https://goo.gl/maps/"         | Pass      |
| Number of Cars field           | Display | Label: How many cars may register?                                                | Pass      |
| Number of Cars field           | Input   | Cleans input                                                                      | Pass      |
| Number of Cars field           | Input   | Validates input as integer and greater than 0                                     | Pass      |
| Number of Cars field           | Input   | Accepts input                                                                     | Pass      |
| Number of Cars field           | Input   | Prevents form from posting and tells user if field is invalid or blank            | Pass      |
| Event Description field        | Display | Label: Briefly describe your event:                                               | Pass      |
| Event Description field        | Input   | Cleans input                                                                      | Pass      |
| Event Description field        | Input   | Validates input                                                                   | Pass      |
| Event Description field        | Input   | Accepts input                                                                     | Pass      |
| Event Description field        | Input   | Prevents form from posting and tells user if field is invalid or blank            | Pass      |
| Publish Your Event button      | Hover   | Indicates link                                                                    | Pass      |
| Publish Your Event button      | Click   | Adds new event record to database                                                 | Pass      |
| Publish Your Event button      | Click   | Redirects user to thank you for organizing page                                   | Pass      |

#### Attendee page (Owner):

| Element       | Action  | Expected Result                                                    | Outcome |
|---------------|---------|--------------------------------------------------------------------|---------|
| Attendee page | Open    | Opens in new browser tab                                           | Pass    |
| Attendee page | Display | Very basic Hard Parkers header                                     | Pass    |
| Attendee page | Display | Event title                                                        | Pass    |
| Attendee page | Display | Event location                                                     | Pass    |
| Attendee page | Display | Total number of registered attendees                               | Pass    |
| Attendee page | Display | Maximum number of attendees                                        | Pass    |
| Attendee page | Display | List or registered users and usernames, alphabetically by username | Pass    |
| Attendee page | Display | Footer with only famous Socrates quote                             | Pass    |

#### Edit Event page (Owner):

| Element                        | Action  | Expected Result                                                                   | Outcome   |
|--------------------------------|---------|-----------------------------------------------------------------------------------|-----------|
| Header and footer              | Display | Consistent with all other pages                                                   | Pass      |
| Form                           | Display | Form label: Edit eventname here. with appropriate event name from event record    | Pass      |
| Event Name field               | Display | Label: Your event name:                                                           | Pass      |
| Event Name field               | Display | Placeholder is original information from appropriate event record                 | Pass      |
| Event Name field               | Hover   | Indicates textfield                                                               | Pass      |
| Event Name field               | Input   | Cleans input                                                                      | Pass      |
| Event Name field               | Input   | Validates input                                                                   | Pass      |
| Event Name field               | Input   | Accepts input                                                                     | Pass      |
| Event Name field               | Input   | Checks event name against other event names in event objects to ensure its unique | Pass      |
| Event Name field               | Input   | Prevents form from posting and tells user if field is blank or invalid            | Pass      |
| Event Name field               | Input   | Prevents form from posting and tells user if name is not unique                   | Pass      |
| Event Date field               | Display | Label: The event date:                                                            | Pass      |
| Event Date field               | Display | Placeholder is original information from appropriate event record                 | Pass      |
| Event Date field               | Input   | Option for manual input or date picker                                            | Pass      |
| Event Date field               | Input   | Date picker checks manual input date is in the future                             | Pass      |
| Event Date field               | Input   | Date picker excludes dates in the past                                            | Pass      |
| Event Date field               | Input   | Prevents form from posting and tells user if field is invalid or blank            | Pass      |
| Event Date field               | Input   | Prevents form from posting and tells user if date is not in the future            | Pass      |
| Event Time field               | Display | Label: At time:                                                                   | Pass      |
| Event Time field               | Display | Placeholder is original information from appropriate event record                 | Pass      |
| Event Time field               | Input   | Accepts default placeholder time unedited                                         | Pass      |
| Event Time field               | Input   | Validates time                                                                    | Pass      |
| Event Time field               | Input   | Prevents form from posting and tells user if field is invalid or blank            | Pass      |
| Registration Closes field      | Display | Label: Registration closes:                                                       | Pass      |
| Registration Closes field      | Display | Placeholder is original information from appropriate event record                 | Pass      |
| Registration Closes field      | Input   | Option for manual input of date picker                                            | Pass      |
| Registration Closes field      | Input   | Date picker checks manual input date is in the future                             | Pass      |
| Registration Closes field      | Input   | Date picker excludes dates in the past                                            | Pass      |
| Registration Closes field      | Input   | Prevents form from posting and tells user if field is invalid or blank            | Pass      |
| Registration Closes field      | Input   | Prevents form from posting if date is not in the future                           | Pass      |
| Reg. Closes Time field         | Display | Label: At time:                                                                   | Pass      |
| Reg. Closes Time field         | Display | Placeholder is original information from appropriate event record                 | Pass      |
| Reg. Closes Time field         | Input   | Accepts default placeholder time undedited                                        | Pass      |
| Reg. Closes Time field         | Input   | Validates time                                                                    | Pass      |
| Reg. Closes Time field         | Input   | Prevents form from posting and tells user if field is invalid or blank            | Pass      |
| Location field                 | Display | Label: The location:                                                              | Pass      |
| Location field                 | Display | Placeholder is original information from appropriate event record                 | Pass      |
| Location field                 | Hover   | Indicates charfield                                                               | Pass      |
| Location field                 | Input   | Cleans input                                                                      | Pass      |
| Location field                 | Input   | Validates input                                                                   | Pass      |
| Location field                 | Input   | Accepts input                                                                     | Pass      |
| Location field                 | Input   | Prevents form from posting and tells user if field is invalid or blank            | Pass      |
| Location URL field             | Display | Label: Share Google Maps link here:                                               | Pass      |
| Location URL field             | Display | Placeholder is original information from appropriate event record                 | Pass      |
| Location URL field             | Input   | Prevents form from posting and tells user if field is invalid or blank            | Pass      |
| Location URL field             | Input   | Defends against any input that does not start with "https://goo.gl/maps/"         | Pass      |
| Number of Cars field           | Display | Label: How many cars may register?                                                | Pass      |
| Number of Cars field           | Display | Placeholder is original information from appropriate event record                 | Pass      |
| Number of Cars field           | Input   | Cleans input                                                                      | Pass      |
| Number of Cars field           | Input   | Validates input as integer and greater than 0                                     | Pass      |
| Number of Cars field           | Input   | Accepts input                                                                     | Pass      |
| Number of Cars field           | Input   | Prevents form from posting and tells user if field is invalid or blank            | Pass      |
| Event Description field        | Display | Label: Briefly describe your event:                                               | Pass      |
| Event Description field        | Display | Placeholder is original information from appropriate event record                 | Pass      |
| Event Description field        | Input   | Cleans input                                                                      | Pass      |
| Event Description field        | Input   | Validates input                                                                   | Pass      |
| Event Description field        | Input   | Accepts input                                                                     | Pass      |
| Event Description field        | Input   | Prevents form from posting and tells user if field is invalid or blank            | Pass      |
| Publish Your Event button      | Hover   | Indicates link                                                                    | Pass      |
| Publish Your Event button      | Click   | Adds new event record to database                                                 | Pass      |
| Publish Your Event button      | Click   | Redirects user to thank you for organizing page                                   | Pass      |

#### Delete Event confirmation page (Owner):

| Element                        | Action  | Expected Result                                               | Outcome |
|--------------------------------|---------|---------------------------------------------------------------|---------|
| Header and footer              | Display | Consistent with all other pages                               | Pass    |
| Event delete confirmation page | Display | Display confirmation of deleting the appropriate event record | Pass    |
| Take Me Back button            | Hover   | Indicate link                                                 | Pass    |
| Take Me Back button            | Click   | Redirects user to the Organized Events page                   | Pass    |
| Delete Event button            | Hover   | Indicate link                                                 | Pass    |
| Delete Event button            | Click   | Deletes appropriate event record from database                | Pass    |
| Delete Event button            | Click   | Redirects user to Thank You page                              | Pass    |

#### Thank you for creating your event page (Owner):

| Element                       | Action  | Expected Result                                                     | Outcome |
|-------------------------------|---------|---------------------------------------------------------------------|---------|
| Header and Footer             | Display | Consistent with all other pages                                     | Pass    |
| Event creation thank you page | Display | Display thank you for appropriate user and appropriate event record | Pass    |
| Events Organized button       | Hover   | Indicate link                                                       | Pass    |
| Events Organized button       | Click   | Redirects user to the Organized Events page                         | Pass    |

#### Thank you for deleting your event page (Owner):

| Element                     | Action  | Expected Result                                | Outcome |
|-----------------------------|---------|------------------------------------------------|---------|
| Header and footer           | Display | Consistent with all other pages                | Pass    |
| Event delete thank you page | Display | Thanks appropriate user for deleting event     | Pass    |
| Events Organized button     | Hover   | Indicate link                                  | Pass    |
| Events Organized button     | Click   | Redirects user to the Organized Events page    | Pass    |

#### Admin Panel (Owner):

| Capability                 | Outcome |
|----------------------------|---------|
| Create user                | Pass    |
| Edit user                  | Pass    |
| Delete user                | Pass    |
| Create event               | Pass    |
| Edit event                 | Pass    |
| Delete event               | Pass    |
| Filter events by date      | Pass    |
| Filter events by organizer | Pass    |
| Filter events by attendee  | Pass    |
| Add user to event          | Pass    |
| Remove user from event     | Pass    |
| Promote user to organizer  | Pass    |
| Demote organizer to user   | Pass    |

<br>
<hr>

### Representative User Manual Testing

<hr>

In addition to formal manual testing, the site was shown to friends who would be representative as users for this website. Most of these testers are active in the car community, or at least adjacent enough to the car community to provide relevant, valuable feedback.

- Despite the Code Institute instruction suggesting the website is too visually plain, representative user testers appreciated the simple and clear design.
- Representative user testers were able to visit the site, view event lists and event details.
- Navigation was clear and easy to follow.
- Users were able to sign up for user accounts.
- Users were able to register for events they liked.
- Users were able to view a list of events they were registered for.
- Users were able to unregister for events they decided they didn't like.
- Users given the persmissions were able to create events and edit events easily.
- Some input was given about the map URL field and the defensive design was adjusted to make it more simple.
- The printable attendee list printed without any formatting adjustments for a straightforward print. It was also tested for printing to a .pdf, which it did directly and without issue.

<br>
<hr>

### Bugs

<hr>

Several bugs were found during development, and most were fixed.

#### Fixed Bugs

The following bugs were fixed during development:

1. Tabs did not initially reflect the page the user was currently navigated to.
    - Troubleshooting found that django could check what requests were being resolved inside template tags, and turn on and off a class of "active." 
    - The code was well explained by [Sharma Coding YouTube Channel.](https://www.youtube.com/watch?v=IY_ooX65BnQ)
2. The Attending Events page did not list the events in order.
    - Troubleshooting found that the ordering code had been left out of the view.
    - Duplicated the .orderby('eventdate') code from the EventsList view in the YourEventsList view. 
3. Eventedit and Eventcreate crashed the site with error 500 if form data didn't match the expected database values.
    - Troubleshooting found that form would not check if the form was valid before saving.
    - Added code to validate the data before saving, and if the data is not valid, it returns prompts on the filled out form to the user.
4. Static images do not display with debug set to false.
    - Troubleshooting found that despite collecting static files, the media files could not be found in Cloudinary.
    - Stumped two different CI tutors with the problem across 4-5 hours of help.
    - Ultimately just hard coded the Cloudinary hosted image, which is an inelegant solution but solved the issue.
5. Heroku deployments fail to push during Heroku automatic and manual deployments.
    - Troubleshooting found that sometimes it do be that way.
    - Just kept making attempts until it works. Was told that this is just how Heroku is sometimes.
6. The Organized Events list page did not list the events in order.
    - Troubleshooting found that the same issue was repeated; leaving out the ordering code.
    - Duplicated the .orderby('eventdate') code from the EventsList and YourEventsList views in the EventOrg view.
7. Signing up new user accounts returned error 500.
    - Troubleshooting found that the signup was attempting to send verification emails.
    - Set ACCOUNT_EMAIL_VERIFICATION = 'none' in settings.py
8. User unreg confirmation page thanked the user for registering instead of unregistering.
    - Troubleshooting found that the event unreg button called the wrong view.
    - Changed the url and call, and realized that it's probably a good sign that this could be refacctored to do it all with one page of code, but this is due any minute now.
9. User unreg confirmation page throws an error instead of passing the user to Upcoming Events list
    - Troubleshooting found issue in button url.
    - Fixed the code.
10. Admin panel showed Socials, Social Tokens, and Sites which are unused.
    - Troubleshooting found these could be excluded in the project level urls.py.
    - Added code to import the appropriate objects, and added admin.site.unregister() with the appropriate objects.
11. Attendee list would return an error instead of the page.
    - Troubleshooting found event.attendee() would not return a list.
    - Replaced with event.attendee.all() to return a list.
12. Attendee list page listed attendees in order of signup, which is essentially arbitrary and would be useless to an organizer.
    - Troubleshooting found that it would be simple to list attendees in alphabetical order.
    - Added .order_by('username') to AttendeeList view.
13. Representative user manual testing found that using a mobile Google Maps app generates a different share link than desktop site, preventing the url from being accepted in the event forms.
    - Troubleshooting found that the app link begins with 'https://maps.app.goo.gl/' instead of 'https://goo.gl/maps/'.
    - Added 'https://maps.app.goo.gl/' to custom validator.

#### Unfixed Bugs:

The following bugs have not yet been fixed:

1. Event description does not maintian user input formatting when displayed on the site.
    - Troubleshooting found that the forms would likely need to be restructured.
2. Event date and Event time are not on the same line in the event create or event edit forms. The same problem exists with the Event Registration Close date and time.
    - Troubleshooting found that the used Crispy Forms and Django forms scheme using Meta object prevents helper.layout from working.
    - The form could be hardcoded or restructured without Crispy forms.
3. Representative user manual testing failed to post an event and instead returned a blank form on one known occasion.
    - Could not duplicate the error on subsequent attempts; but form error codes and confirmation pages should prevent this.


<hr>
For educational purposes only.