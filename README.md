# PROJECT 4 - Budapest Gourmet

## Overview

My chosen project was to create a Battleships game that can be played inside the Python Terminal window.
The game was created using the Code Institute's Python Essentials Template and deployed on Heroku, displayed in a browser-based terminal window.

![Image of deployed project from Am I responsive](./readme_files/responsive.png)

The live game can be found here : <a href = "https://table-booking-system-sb.herokuapp.com//">Budapest Gourmet</a>

#  
## Table of Contents

1. [UX](#ux)
    - [Project Goals](#project-goals)
    - [User Goals](#User-goals)
    - [User Stories](#user-stories)
    - [Design Choices](#design-choices)

2. [Features](#features)
    - [Existing Features](#existing-features)
        - [Landing Page](#landing-page)
        - [Menu Page](#product-page)
        - [About Page](#about-page)
        - [Contact Page](#contact-page)
        - [Register Page](#register-page)
        - [Login Page](#login-page)
        - [Booking Page](#login-page)
        - [Admin Product Managment](#admin-product-managment)
        - [Django allauth features](#django-allauth-features)
    - [Features Left to Implement](#features-left-to-implement)
    - [Defensive Design](#defensive-design)

3. [Information Architecture](#information-architecture)
    - [Database Choice](#database-choice)
    - [Data Modeling](#data-modeling)

4. [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Libraries and Packages](#libraries-and-packages)
    - [Tools](#tools)
    - [Databases](#databases)

5. [Testing](#testing)

6. [Deployment](#deployment)
    - [Local Deployment](#local-deployment)
    - [Remote Deployment to Heroku ](#remote-deployment)

7. [Credits](#credits)

8. [Disclaimer](#disclaimer)

# UX
## Project Goals
### Target Audience
- People who are looking for authentic Hungarian dining experience.
- People who are looking for a unique venue for a birthday party.
- People who seek experiences such as wine tasting.

### Visitor / User Goals
- Find information about the restaurant such as its location, hours of operation, and contact information.
- View the menu and see pictures, prices and possibly ingredients.
- Make a reservation in a simple and user-friendly way. See the availability of tables at certain times.
- Read reviews or testimonials from previous visitors.
- Plan a private event based on the information on the options, pricing, and process to book the venue.

### Business Goals (Site Owner's Goals)
- Increase online table reservations
- Improve Brand Awareness
- Promote Specials and Events
- Expand Customer Base

<div><a href="#table-of-contents">Back to top</a></div>

## User Stories

- Viewing and Navigation

- As Site User I want to see the restaurant's operating hours, menu, and contact information, so I can make an informed decision before booking a table.

| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Site User | access the website on any device | Use the website anytime and anywhere |
| Site User | Easily see what services are offered | Find the service I want to use |  
| Site User | All the important services are accesible from nav bar| Don't need to scroll to find important information |
| Site User | Have a Book now icon on the nav bar | Quickly and easily make a booking |

<br/>

- Registration and User Accounts

| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Site User | Easily and quickly sign up/ sign in | Access the registered user features |
| Site User | Save user information |  Log in quicker next time |
| Site User | Secure my information with a password | Other users can't access my account |
| Site User | Reset forgotten login information | Recover access to my account |


<br/>

- Making a booking

| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Site User | Select a time and date for my booking | The table is available when I arrive |
| Site User | Specify the number of guests | The staff can prepare |
| Site User | Add special requests/ notes to my booking | The staff can prepare |
| Site User | Receive a comfirmation of my booking | I know the booking is made |
| Site User | Modifiy or cancel my booking | Make changes when necessary |
| Site User | View other bookings | Know when the reataurant is busy or quiet |
| Site User | Leave feedback and ratings | Staff can improve service and potential customers can make informed decisions |
| Site Admin/ Staff | View and manage all bookings | Know when the restaurant is busy or quiet |
| Site Admin/ Staff | View customer details | Provide a personalised service |
| Site Admin/ Staff | Monitor table avaliability | Accomodate customers without a booking |
| Site Admin/ Staff | Receive notifications of new/amended bookings | Monitor changes without constantly checking for new bookings |

<br/>


<div><a href="#table-of-contents">Back to top</a></div>

## Design
### Wireframes
Wireframes were created with...
You can find the wireframes...

### Brand Identity
- Vision: To be recognised as a great destination for authentic Hungarian cuisine.
- Mission: To deliver an outstanding dining experience by serving high-quality, traditional Hungarian dishes made from the finest local ingredients, and by providing exceptional service in a warm and welcoming environment.
- Values: Authenticity: Staying true to the traditional recipes. Hospitality: Creating a warm, welcoming environment. Sustainability: Use local suppliers wherever possible.

### Color Scheme


### Typography


- Icons: [Bootstrap Icons](https://icons.getbootstrap.com/) were used accross the site.
- Favicon: The favicon was sourced from [www.flaticon.com](https://www.flaticon.com/).


# Features

## Existing Features
This website is composed of a single application: 

## Landing Page
Landing Page is designed as a single page website 

### Navbar
Navbar is fixed at the top of pages across the site to help with navigating the site. The navbar contains  
- Site Menu & My Account dropdown: The site menu collapses to toggle icon less than 992px width. My Account dropdown is included to toggle menu for smaller screen.
- Cart icon: The number next to the cart icon shows the total of items added to the cart.


Navbar for larger screensizes (width > 992px)

Navbar for smaller screensizes (width < 992px)

Navbar for authenticated users


### About Us & 

### Contact Form

### Footer
The footer section consists of Social Media icons.
1. General Info and Quick Links: The first footer section includes the shop address and its opening hours and quick links to the pages within the site.
<div align="center"><img src = "https://github.com/AsunaMasuda/FloweryDays/blob/master/readme_materials/footer1.png" width=700></div>

2. Social media icons: In this milestone project, Social Media icons are linked to my personal social media accounts, but in a real settting they should be linked to business pages on social media, such as Facebook, Instragram, Twitter, Pinterest etc, for social media marketing purposes.
<div align="center"><img src = "https://github.com/AsunaMasuda/FloweryDays/blob/master/readme_materials/footer2.png" width=700></div>

<div><a href="#table-of-contents">Back to top</a></div>

##  Page

###  Page

###  Page


## Page


## Page
### Page

### Page


## Page
### Page


## Admin/ Staff Management


## Django-allauth features
Base template for allauth has `Back to Home` button at the end of the page, for easy navigation for users.
- Sign Up: The users will be asked to fill out `E-mail`, `User Name` and `Password` to create an account. When the sign up form is submitted, a verification email will be sent to the user's email address to complete the sign up process.
- Log In: Users will be asked to input `User Name` or `Email`, and `Password` to login. If the user successfully logged in, a success message will pop up and redirect to the landing page.
- Log out: Log out page is accessible from the site menu. After the user successfully signed out button on the sign out page, a success message will appear and redirect to the landing page.
- Forgot password: Forgot password page is accessible from Sign In page. Users will be asked to put in an email address which they have used for their registration to the site. An email with a link to reset the password will be sent after submitting the form.

<div><a href="#table-of-contents">Back to top</a></div>

## Features Left to Implement
There are some of features left to implement in the future which I could not add to the project this time due to time constraints. These features are great to be added for a more complete online shop service which would lead to higher customer satisfaction.
### 1.
At the moment, all the authenticated users can leave reviews to any products if they are logged in. It should be limited to those who actually purchased the product for the validity of the reviews.
### 2. 
This function would be very helpful when there are many products in results. This was not implemented this time due to the time constraints and there are not that many products used in this project.
### 3. 


## Defensive Design
### Error views 

### Form Validation
- Django Form Validation

### Booking Form Validation


# Information Architecture
## Database choice
- Development phase


- Deployment phase


## Data Modeling


### Table Booking App


# Technologies Used
The main frontend development was created using HTML, CSS, JavaScript and their libraries. The main backend development was powered by Python and Django.

## Languages
- HTML, CSS, JavaScript, Python

## Libraries and Packages
- [Django](https://www.djangoproject.com/)
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)
- [Bootstrap (v4.5.1)](https://www.bootstrapcdn.com/)
- [JQuery](https://jquery.com/)
- [Font Awesome](https://fontawesome.com/)
- [Google Fonts](https://fonts.google.com/)

## Tools
- Git/GitHub
- Gitpod
- [PIP](https://pip.pypa.io/en/stable/installing/)

## Databases
- [PostgreSQL](https://www.postgresql.org/) - database used for development.
- [ElephantSQL](https://www.elephantsql.com)- database used for deployment.

# Testing


<div><a href="#table-of-contents">Back to top</a></div>

# Deployment
## Heroku Deployment 

 
### Automatic Deploy on Heroku
You can enable automatic deploy in the following steps that pushes update to Heroku everytime you push to github.
1. Go to Deploy in Heroku dashboard.
2. At `Automatic deploys`, choose a github repository you want to deploy.
3. Click `Enable Automatic Deploys`.


## Local Deployment
For local deployment, you need to have an IDE (I used Gitpod for this project) and you need to install the following:
- Git, Python3, PIP3


2. Set up environment variable in your selected IDE, or you can create `.env` file in your root directory and add `.env` to `.gitignore` file, and add the followings to the `.env` file.
```
    
```
3. Install all the required packages with `pip3 install -r requirements.txt`
4. Migrate the models to crete a database using in your IDE with `python3 manage.py makemigrations` and `python3 manage.py migrate`

6. Create a superuser for the Postgres database by running with `python3 manage.py createsuperuser`
7. Now you can access the app using the command `python3 manage.py runserver`

<div><a href="#table-of-contents">Back to top</a></div>

# Credits

### Content & Code


### Images & Media
- The icons in this website were provided by [Font Awesome](https://fontawesome.com/).


### Acknowledgements
- Thanks to: my Code Institute Mentor.
- Code Institute Slack Community.

### Disclaimer
This website is created for educational purpose only.