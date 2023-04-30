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

I chose range of grays, whites, blues, and a touch of warm orange to create a comforting and inviting ambiance.
- The background color of the website is a soft dark gray: #5C6771
- The navigation bar's background color is a medium-gray: #808080
- The navigation links themselves are a vibrant blue: #007bff
- The brand and hero text is white (#fff) and its hover effect uses warm orange color:#D4672C
- Different colors to indicate various types of messages: blue (#2196F3) for informational messages, green (#4CAF50) for success messages, orange (#FF9800) for warning messages, and red (#F44336) for error messages.

### Typography

- Fonts: Merienda, Roboto and Playfair Display.
- Icons: [Bootstrap Icons](https://icons.getbootstrap.com/) were used accross the site.
- Favicon: The favicon was sourced from [www.flaticon.com](https://www.flaticon.com/).


# Features

## Existing Features
This website is composed of a single application: 

## Landing Page
The Landing Page is designed as a single page website 

### Navbar

The Navbar is fixed at the top of pages across the site to help with navigating the site. The navbar contains: 
- Brand Logo, Site Menu, Account Menu and Book a Table button. The menu collapses to toggle icon less than 992px width.

<div align="center"><img src = "https://github.com/jpg" width=700></div>

Navbar for larger screensizes (width > 992px)

Navbar for smaller screensizes (width < 992px)

<div align="center"><img src = "https://github.com/jpg" width=700></div>

Navbar for authenticated users

<div align="center"><img src = "https://github.com/jpg" width=700></div>


### Hero Image and Hero Text

The next feature of the Landing Page is the Hero Image and Hero Text. The image is a full width picture of the restaurant interior and the Hero Text is located at the center of it. It's white text with an orange hover effect.

### Why Choose Us?

A list of main selling points for the restaurant, laid out in a horizontal line.

<div align="center"><img src = "https://github.com/why-us.jpg" width=700></div>

### Featured Dish

A picture and the description of the current signature dish, side by side.

<div align="center"><img src = "https://github.com/featured-dish.jpg" width=700></div>

### Events & News

Pictures and description of any regular events and news about the restaurant.

<div align="center"><img src = "https://github.com/events-news.jpg" width=700></div>

### Footer
The footer section contains the Social Media icons.I included icons for Twitter, Facebook, Instagram and Pinterest. Currently they take the user back to the homepage but on the deployed website of the actual business they would take the user to the relevant social media pages.

<div align="center"><img src = "https://github.com/footer.jpg" width=700></div>

<div><a href="#table-of-contents">Back to top</a></div>

## Menu Page

 Contains the restaurant menu in 3 vertical tables, one for the Starters, Main Courses amd Desserts each.

<div align="center"><img src = "https://github.com/menu.jpg" width=700></div>

## Gallery Page

Contains images of three selected dishes in each of the categories included in the menu.Next to each image there is a card containing the name, a short description and the price of each dish. The images and description cards are arranged in a horizontal, responsive row.

<div align="center"><img src = "https://github.com/gallery.jpg" width=700></div>

## About Page

Divided into the following sections:

- About Us: A brief description of the business and its mission.

- Welcome mssage, also includes an image of the restaurant's interior.

<div align="center"><img src = "https://github.com/about-top.jpg" width=700></div>

- Reserve your table: A brief description of the reservation process and a button taking the customer to the Login or Booking page. 

- Opening Times: 

- Where to find Us: An embedded section of Google Maps showing the supposed location of the restaurant. This section would also contain the address, phone number, email address and other details of the restaurant but this is a fictional business, invented for the purpose of the project.

<div align="center"><img src = "https://github.com/about-bottom.jpg" width=700></div>

## Contact Page

Contains the contact form of the restaurant. The form has fields for the Name, Email, Subject and Message as well as the Submit and Clear Form Buttons.
The form was styled using Bootstrap and Django Crispy Forms. This is the case with all other forms found on the website.

<div align="center"><img src = "https://github.com/contact.jpg" width=700></div>

## Register Page

Contains the Sign Up form. The form has 6 fields in the following vertical order. 1 - Username, 2 - Email, 3 - First Name, 4 - Last Name, 5 - Password, 6 - Password (again). This and all other user forms (except for the Booking form) are imported with the Django Allauth package and modified to better fit the needs of the site.
There are also two buttons, one for signing in for existing users and a submit button for signing up.

<div align="center"><img src = "https://github.com/signup.jpg" width=700></div>

## Login Page

This page contains the Sign In form, again styled using Crispy Forms. It contains two fields, one for the Username and another for the Password. This page also includes a Sign In button for submitting the data and a Sign Up button redirecting the visitor to the Register page. Upon signing in the user is redirected to the Index page.

<div align="center"><img src = "https://github.com/signin.jpg" width=700></div>

## Book a Table Page

This page can be acessed by clicking the Book a Table button, located in the Navbar. Another similar button can found o the About page. For the purpose of the project only registered site users can make a booking after signing in.
The table contains the Booking form. This is a bespoke form created for the purpose of the project.
It has fields for selecting the date and time of the booking, the number of guests and one of the 5 tables. Data validation is included for every input field.

<div align="center"><img src = "https://github.com/booking-form.jpg" width=700></div>

The user can not make a booking for the past or for a time outside the opening hours. The number of guests can't be less than 1 or greater than 25 which is considered to be the full capacity of the restaurant. Bookings can be made for 30 minute intervals and it's not possible to make two bookings for the same table at the same time.
Special requests can be used to warn about allergies and dietary or any other needs.
There is a button beneath the form for submitting the information. Entering invalid data results in warning messages appearing and pointing out the error to the user and prompting them to correct the relevant details. Upon entering and submitting valid data the user is redirected to the Booking Confirmation page where they can check if they entered the correct details.

<div align="center"><img src = "https://github.com/booking-confirmation.jpg" width=700></div>

From here it's possible to access the booking list, which is also accessible from the booking form page. The bookings list has different views depending on whether the user is a customer or a member of staff (Admin user). The customer can view all the bookings (except for the name of the other customers) but only edit or delete bookings made by themselves. The Admin user can access, edit and delete all the bookings contained within the list.

<div align="center"><img src = "https://github.com/booking-list.jpg" width=700></div>

Next to each booking in the list there are two buttons, one for editing and one for deleting the relevant booking. These buttons are a requirement for the CRUD functionality which is understandably an essential requirement for the project. The unauthorised user clicking either of these buttons triggers a warning message informing them that they don't have a permission for these actions. However they are free to edit or delete any bookings made by themselves.
Clicking the Edit button takes the user to the Update Booking page. This page is page is almost identical to the Booking page except for the text making it clear that the user is updating a previous booking rather than making a new one. The contained form also looks identical to the original Booking Form. Upon amending the original booking details shown in the form and clicking the Update Booking button the user is taken back to the Booking Confirmation page.

<div align="center"><img src = "https://github.com/booking-update.jpg" width=700></div>

The other option available to the user on the Bookings List page is to delete one of their bookings. Upon clicking the red Delete button the user is taken to the Delete Reservation page. Here they are given another prompt to confirm that they wish to delete the selected booking or want to return to the Bookings List page. Deleting the selected booking also results in the user being redirected to the Bookings List, which will no longer include the deleted booking.

<div align="center"><img src = "https://github.com/booking-delete.jpg" width=700></div>

The Bookings List page looks slightly different when viewed by the Admin User. They can see the names and details of all the customers on the list and edit or delete any booking. This is necessary so that they can make changes if asked by the customers via other ways such as a phone call or in person.

<div align="center"><img src = "https://github.com/admin-bookings-list.jpg" width=700></div>

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