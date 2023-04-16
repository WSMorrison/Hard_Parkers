# The Hardparkers

The HardParkers website is is a simple, streamlined, and mobile focused resource for automotive enthusiasts to find meets and shows they would like to attend in their area. It allows event organizers to publish their event details and for participants to register to attend, making it simple for organizers to get the word out and easy for enthusiasts to find events that match their interests.

This readme will discuss the testing of the app. Some of the information can also be found on the main ReadMe, but this Testing ReadMe will go into greater detail about the systematic manual testing.

The site was tested as an unlogged-in visitor, as a logged-in basic user (User), as a logged-in event promoter and organizer (Organizer), and as a logged in the site owner or admin (Owner). Much of the functionality was the same or similar, but permissions were different and there were different aspects of the project that required different aspects of testing.

The main ReadMe can be found [here.](/README.md)

### The deployed site can be found here: [The HardParkers](https://hardparkers.herokuapp.com/)

<br>
<hr>

## Contents

<hr>

* [Testing](#testing)
    * [Responsiveness](#responsiveness)
    * [Accessibility](#accessibility)
    * [Code Validation](#code-validation)
    * [Systematic Manual Testing](#systematic-manual-testing)
    * [Representative User Manual Testing](#representative-user-manual-testing)

<br>
<hr>

## Testing

<hr>

### Responsiveness

![Front page of The HardParkers as input to AmIResponsive.](/assets/readme-images/Responsive.png)

[AmIResponsive](https://ui.dev/amiresponsive)

### Accessibility

Care was taken to make sure the website was accessible.

  - The page is developed to use high contrast text, simple interface and easy to follow buttons. 
  - Aria labels are on any button that is not labelled.
  - The tabs are all marked current so that the page indicates where the navigation currently is. 
  - The HTML follows a clear semantic flow.

![Lighthouse score for page](/assets/readme-images/Lighthouse.png)

The accessibility score is less than 100% because the "Background and foreground colors do not have a sufficient contrast ratio," however, changing the colors did not seem to make any difference in the score.

### Code Validation

The HTML for the website was put through the [W3C Markup Validation Service](https://validator.w3.org/#validate_by_input). Each page of the site was tested by opening the page, viewing page source, and copying and pasting the source coude into the validator. This avoided any issues with the template tags upsetting the validator to the point that it did not check the rest of the code. Any errors found they were fixed. As credit to Django's automated page generation through template tags, the only errors were in the hand written code of the base.html; a stray closing italic tag in the footer, and an attempt at a responsive break in the blockquote to try to influence the line break that did not have any effect. Both were fixed, and each page was returned without errors.

![W3C Markup validator representative return](/assets/readme-images/W3CHTMLValidator.png)

The CSS was put through the [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/). The short, hand written CSS file checked without errors.

![W3C CSS validator representative return](/assets/readme-images/W3CCSSValidator.png)

The Python code was checked with the [Code Institute Python linter](https://pep8ci.herokuapp.com/). Each hand written python file was checked with the linter; forms.py, models.py, urls.py, and views.py. Each was returned without errors.

![CI Python linter representative return](/assets/readme-images/CIPythonLinter.png)

### Systematic Manual Testing

The following tables will describe the systematic manual testing done to ensure that the app is working properly.

#### Unlogged-in User

The following features were tested as an unlogged-in user:

| Element                 | Action   | Expected Result                                                        | Outcome |
|-------------------------|----------|------------------------------------------------------------------------|---------|
| **Index Page** |
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
| Details button          | Hover    | Indicate link                                                          | Pass    |
| Details button          | Click    | Navigate to eventview page and display details of correct event record | Pass    |
| Log In tab - nav bar    | Hover    | Indicate link                                                          | Pass    |
| Log In tab - nav bar    | Click    | Navigate to Log In page as site tab                                    | Pass    |
| Sign Up tab - nav bar   | Hover    | Indicate link                                                          | Pass    |
| Sign Up tab - nav bar   | Click    | Navigate to Sign Up page as site tab                                   | Pass    |
| **Log In page:** |
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
| Remember Me checkbox | Clicked | Remembers user                              | Pass [^1] |
| Log In button        | Hover   | Indicate link                               | Pass      |
| Log In button        | Click   | Logs user in, navigates to main, index page | Pass      |
| Sign Up Here link    | Hover   | Indicate link                               | Pass      |
| Sign Up Here link    | Click   | Navigate to Sign Up tab                     | Pass      |
| **Sign Up page:** |
| Nav bar              | Display | Indicate navigated tab                      | Pass |
| Username Field       | Hover   | Indicates textfield                         | Pass |
| Username Field       | Input   | Cleans input                                | Pass |
| Username Field       | Input   | Validates input                             | Pass |
| Unsername Field      | Input   | Accepts input                               | Pass |
| E-mail Field         | Display | Indicates optional                          | Pass |
| E-mail Field         | Hover   | Indicates textfield                         | Pass |
| E-mail Field         | Input   | Cleans input                                | Pass |
| E-mail Field         | Input   | Validates input                             | Pass |
| E-mail Field         | Input   | Accepts input                               | Pass |
| Password Field       | Hover   | Indicates textfield                         | Pass |
| Password Field       | Input   | Cleans input                                | Pass |
| Password Field       | Input   | Validates input                             | Pass |
| Password Field       | Input   | Accepts input                               | Pass |
| Password Again Field | Hover   | Indicates textfield                         | Pass |
| Password Again Field | Input   | Cleans input                                | Pass |
| Password Again Field | Input   | Validates input                             | Pass |
| Password Again Field | Input   | Accepts input                               | Pass |
| Password Again Field | Input   | Checks Password Again against Password      | Pass |
| Sign Up button       | Hover   | Indicate link                               | Pass |
| Sign Up button       | Click   | Adds user to database                       | Pass |
| Sign Up button       | Click   | Logs user in, navigates to main, index page | Pass |
| Log In Here link     | Hover   | Indicate link                               | Pass |
| Log In Here link     | Click   | Navigate to Log In tab                      | Pass |
| **Details page** |
| Details page           | Display | Title for correct event record                                     | Pass |
| Details page           | Display | Location for correct event record                                  | Pass |
| Details page           | Display | Date for correct event record                                      | Pass |
| Details page           | Display | Registration close date for correct event record                   | Pass |
| Details page           | Display | Username of event organizer                                        | Pass |
| Details page           | Display | Number of cars able to register                                    | Pass |
| Details page           | Display | About this event text box                                          | Pass |
| Location Map button    | Hover   | Indicate link                                                      | Pass |
| Location Map button    | Click   | Open google maps link in new browser tab, for correct event record | Pass |
| Login to register link | Hover   | Indicate link                                                      | Pass |
| Login to register link | Click   | Navigate to Log In page as site tab                                | Pass |

[^1]: Depending on browser settings.

#### Basic Site User

The following features were tested while logged in as a User.

| Element                 | Action   | Expected Result                                                        | Outcome |
|-------------------------|----------|------------------------------------------------------------------------|---------|
| **Index Page** |
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
| **Attending Events page** |
| Nav Bar                 | Display  | Indicated navigated tab                                                | Pass    |
| Attending Events tab    | Display  | Display attending events                                               | Pass    |
| Attending Events tab    | Display  | Display attending events with the soonest first                        | Pass    |
| Attending Events tab    | Display  | Display selected details of appropriate event record                   | Pass    |
| Attending Events tab    | Paginate | Paginate after 5 events                                                | Pass    |
| Attending Events tab    | Paginate | Navigate through pagination pages                                      | Pass    |
| Attending Events tab    | Display  | Display Details button                                                 | Pass    |
| Details button          | Hover    | Indicate link                                                          | Pass    |
| Details button          | Click    | Navigate to eventview page and display details of correct event record | Pass    |
| **Log Out Page** |
| Nav bar         | Display | Indicate navigated tab            | Pass |
| Log Out button  | Hover   | Indicate link                     | Pass |
| Log Out button  | Click   | Log user out                      | Pass |
| Log Out button  | Click   | Redirect user to main, index page | Pass |
| **Details page** |
| Details page         | Display | Title for correct event record                                     | Pass |
| Details page         | Display | Location for correct event record                                  | Pass |
| Details page         | Display | Date for correct event record                                      | Pass |
| Details page         | Display | Registration close date for correct event record                   | Pass |
| Details page         | Display | Username of event organizer                                        | Pass |
| Details page         | Display | Number of cars able to register                                    | Pass |
| Details page         | Display | About this event text box                                          | Pass |
| Location Map button  | Hover   | Indicate link                                                      | Pass |
| Location Map button  | Click   | Open google maps link in new browser tab, for correct event record | Pass |
| Register Now! button | Hover   | Indicate link                                                      | Pass |
| Register Now! button | Click   | Add user to correct event record attendee list                     | Pass |
| Register Now! button | Click   | Redirect user to thank you page                                    | Pass |



#### Event Organizer

#### Site Owner

### Representative User Manual Testing

In addition to formal manual testing, the site was shown to friends who would be representative as users for this website. Despite the Code Institute instruction suggesting that the website was too plain and not visually interesting, all representative user tester appreciated the simple and clear design. 

The printable attendee list printed smoothly and without needing any tweaking for a good, straightforward print. It was also tested for printing to a .pdf, which it did directly and without issue.

<br>
<hr>
For educational purposes only.