# The Hardparkers

The HardParkers website is is a simple, streamlined, and mobile focused resource for automotive enthusiasts to find meets and shows they would like to attend in their area. It allows event organizers to publish their event details and for participants to register to attend, making it simple for organizers to get the word out and easy for enthusiasts to find events that match their interests.

This readme will discuss the testing of the app. Some of the information can also be found on the main ReadMe, but this Testing ReadMe will go into greater detail about the systematic manual testing.

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

### Representative User Manual Testing

In addition to formal manual testing, the site was shown to friends who would be representative as users for this website. Despite the Code Institute instruction suggesting that the website was too plain and not visually interesting, all representative user tester appreciated the simple and clear design. 

The printable attendee list printed smoothly and without needing any tweaking for a good, straightforward print. It was also tested for printing to a .pdf, which it did directly and without issue.

<br>
<hr>
For educational purposes only.