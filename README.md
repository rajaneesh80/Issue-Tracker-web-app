Issuetracker

[![Build Status](https://travis-ci.org/rajaneesh80/Issue-Tracker-web-app.svg?branch=master)](https://travis-ci.org/rajaneesh80/Issue-Tracker-web-app)

<hr>
<h2> Raj_Issuetracking_Web_App </h2>

I used to use Jira at work; we are small team did need such a big app for a small group;
maybe in future, I will make this app alternative to Jira for a small team to report the issue and allocate the work in an organization.

<hr>

<h2> Overview </h2>

A web application created in Python 3.7 and Django-version-2.2.5.

<ul>

<li>This is a web application that allow users to create issues, comment on issues, and show the status of an issue (‘to do,’ ‘doing,’ or ‘done’). </li>

<li> Issues come in two varieties – ‘bugs’ (fix for free), and ‘features’ (only develop if offered enough money or enough people shows the intrest). </li>

<li> To help prioritize the work, users are able to upvote bugs (signifying ‘I have this too’), and upvote feature requests (signifying ‘I want to have this too’).</li>

<li> While upvoting bugs is free, to upvote a feature request, users need to pay some money to pay for development time in working on it. </li>

<li> This is a full stack web application (frontend and backend) that provides CRUD (Create, Read, Update, Delete) functionality to a database hosted in the cloud on Heroku platform as a service.</li>

</ul>

<hr>

<h2> UX </h2>

This website was created with the intention to create user report the issuees.
Details of the UX design is available in the 'Wire-Frame' folder. 
This document outlines how I approached the design of the user interface of the main pages of the web application.

<h3> __User Profile Page: Navigation bar > My Issues__ </h3>

The My Issue page shows the user's username, the issues the user added and its details.

It also allows users to perform CRUD (Create, Read, Update and Delete) on any issue.  

<ul>

<h3> View details about the issues added: </h3> 

<li> Click on the issue you want to read about </li>

<h3> Adding an issue:: </h3> 
<li> Click on the button 'Add Issue' </li>
<li> Fill out the form </li>

<h3> __User Edit Profile Page: Navigation bar > Edit Profile __ </h3>

<h3> Editing an username , first and last name, email, change password:: </h3> 
<li> User can change username , first and last name,  </li>
<li> User can change email if its not all ready registered  </li>
<li> User can change password by cliking the  provided hyper link</li>

<h3> Editing an issue:: </h3> 
<li> Click on the issue that needs to be edited </li>
<li> Click on the button 'Edit' </li>
<li> Fill out the form </li>

<h3> Deleting an issue:: </h3> 
<li> Click on the issue that needs to be deleted</li>
<li> Click on the button 'Delete' </li>

<h3> Buy a featur:: </h3> 
<li>  Click on the feature you want to buy </li>
<li> Click on the button 'Add to cart'</li>
<li>On the navigation bar click on 'Cart' </li>
<li> The 'Cart' page displays your order </li>
<li> Click on the button 'Checkout</li>
<li>Review your order and fill out the form  </li> 

<hr>

<h3> A demo of this site is available:- <a href="https://raj-issuetracker.herokuapp.com/" rel="nofollow">here</a> </h3> 


</ul>

<hr>

<h2> Features </h2> 

<li> User authentication - Register, Login, Logout </li>

<li> User Profile </li>

<li> Search bar </li>

<li> Full CRUD functionality </li>

<li> E-commerce </li>

<h3> A demo of this site is available:- <a href="https://raj-issuetracker.herokuapp.com/" rel="nofollow">here</a> </h3> 

<hr>

<h2>Technologies Used </h2>

<h3> Built With </h3>

Python Django-Python framework PostgreSQL database
Heroku container-based cloud  ervice (PaaS) for deployment
AWS - S3 to store imaegs and static files 
HTML5, CSS3 and JavaScript
Stripe for paymemt 
Bootstrap CSS framework to style and create responsive design
other Front end languages that give the application structure, style and interactivity


<ul>
<li><a href="https://www.python.org/" rel="nofollow">Python-Version 3.7.3</a>
<ul>
<li>The project uses <strong>Python</strong> for backend development.</li>
</ul>
</li>

<li><a href="https://www.djangoproject.com/" rel="nofollow">Django-version-2.2.5</a>
<ul>
<li>The project uses <strong>Django</strong> for backend development.</li>
</ul>
</li>


<li><a href="https://www.postgresql.org/" rel="nofollow">postgres</a>
<ul>
<li>The project uses <strong>Postgres</strong> SQL database to store the data from user</li>
</ul>
</li>


<li><a href="https://getbootstrap.com/docs/4.3/getting-started/introduction/" rel="nofollow">Bootstrap v4.1.3</a>
<ul>
<li>The project uses <strong>Bootstrap</strong> to speed up the development.</li>
</ul>
</li>

<li><a href="https://fontawesome.com/" rel="nofollow">Font Awesome v5.3.1</a>
<ul>
<li>The project uses <strong>Font Awesome</strong> for icons.</li>
</ul>
</li>
 
<li><a href="https://code.jquery.com/jquery-3.3.1.min.js" rel="nofollow">JQuery v3.3.1</a>
 
 <ul>
<li>The project uses <strong>JQuery</strong> for better user experiences as well as to speed up the development.</li>
</ul>
</li>


<li><a href="https://getbootstrap.com/docs/4.3/components/forms/#validation" rel="nofollow"> HTML5, Bootstra4 and Javascripts /</a>
 
<ul>
<li>The project uses <strong> HTML5, Bootstra4 and Javascripts</strong> for form Validation.</li>
</ul>

</li>

<li> <a href="https://signin.aws.amazon.com/" rel="nofollow"> AWS /</a>

<ul>
<li>The project uses <strong> AWS - S3 </strong> to store the imaegs and static files.</li>
</ul>

<li> <a href="https://dashboard.heroku.com" rel="nofollow"> Heroku /</a>

<ul>
<li>The project uses <strong> Heroku </strong>  container-based cloud  ervice (PaaS) for deployment </li>
</ul>

<hr>

<h2> Testing </h2>

Automated tests are located in the Issues app in test_models.py, test_forms.py and test_views.py. These 13 tests passed as per screenshot in Testing folder. To run the test:
`python3 manage.py test`

Manual testing was undertaken for this application and satisfactorily passed. A sample of the tests conducted are as follows:

1.	Testing navigation buttons and hyperlinks throughout the page.

2.	Testing the CRUD functionality: adding and editing Issues, Comments.

3.	Testing the responsiveness of the application on different browsers and then using different devices.

4.  Testing ecommerce functionality: generating order transactions with Add to Cart, Checkout and payments with Stripe test card details.

5. Testing image upload to AWS S3 bucket.

<h3> All the user functionality  testing has also been undertaken:-</h3>

 <h4> Login page:-</h4>

    * Left username and password required fields blank > Output: 'Please Fill out this field'. (Passed)
    * Entered a non existent username > Output: 'Your username or password are incorrect'. (Passed)
    * Entered a wrong password > Output: 'Your username or password are incorrect'. (Passed)
    * Entered a correct username and password > Output: 'You have successfully logged in'. (Passed)

<h4> Registration page:-</h4>

    * Left username, email address, password and password confirmation > Output: 'Please Fill out this field'. (Passed)
    * Entered a username not allowed. < Output: 'Enter a valid username. This value may contain only English letters, numbers, and @/./+/-/_ characters.'
    * Tried to log in without providing an email address > Output: 'Email addresses must be unique.' (Passed)
    * Entered an email address without @ > Output: 'Please include an @ in the email address' (Passed)
    * Entered an email address already registered > Output: 'Email addresses must be unique'. (Passed)
    * Entered an username that already exists > Output: 'A user with that username already exists.' (Passed)
    * Entered a wrong password confirmation > Output: 'Passwords do not match'. (Passed)
    * Entered correctly an username, email address, password and password confirmation > Output: 'You have successfully logged in'. (Passed)

 <h4> Create, Read, Update and Delete Issues:-</h4>

- <strong> Create: </strong>
    * Left name and description fields blank > Output: 'Please Fill out this field'. (Passed)
    * Entered a name, description and selected the type of issue (which is by default a bug, so it will never be blank) > Output: 'New issue created successfully!'. (Passed)
    * When a new issue is created, the issue is saved in the database and the page is redirected to 'My Issues' page where the issue is displayed. (Passed)
    * Issue is also displayed on 'All Issues' page.

- <strong> Read

- <strong> Edit Issue: </strong>
    * Left name and description fields blank > Output: 'Please Fill out this field'. (Passed)
    * Entered a different name, description and type of issue > Output: 'Your issue was updated successfully!'. (Passed)
    * When an issue is edited, the issue is saved is updated in the database and the page is redirected to 'My Issues' page where the issue is displayed. (Passed)
    * Issue is also displayed on 'All Issues' page. (Passed)

- <strong> Delete Issue: </strong>
    * When clicking on Delete button the issue is deleted from the database, and from the pages 'My Issues' and 'All Issues'. (Passed)

<h4> Create and Update Comments:-</h4>

- <strong> Create Comment: </strong>
    * Clicked on the button 'Comment' > Brings to another page with a form. (Passed)
    * Left the input field blank > 'Please Fill out this field'. (Passed)
    * Entered a comment. The comment is saved in the database, and the page is redirected to the previous page where the comment is displayed with the username, date and time. (Passed)

- <strong> Edit a Comment: </strong>
    * Clicked on the button 'Edit' > Brings to another page with a form. (Passed)
    * Left the input field blank > 'Please Fill out this field'. (Passed)
    * Entered a new comment > Back to details page, comment saved. (Passed)

 <h4> Upvote:-</h4>

    * Clicked on the button 'Upvote' the page is redirected to 'Issues' page and displayes the message 'Upvoted successfully!' (Passed)
    * Upvote is saved in the database and displayed in the badge placed in the accordion. (Passed)
    * The upvoted issue is displayed on the top of the issues that have less upvotes. (Passed)

<h4>  Cart :-</h4>

    * Clicked on the button 'Add to cart' the page is redirected to 'Issues' page and displays the message 'Feature added to cart'
    * Cart page: Feature is added to cart. (Passed)

 <h4> Checkout :-</h4>

    * Proceeded with checkout, the product overview is displayed (Passed)
    * Proceed with payment by filling out the form and using Stripe's test card number 4242 4242 4242 4242 (Passed)

<hr>

## Deployment

1. Make sure requirements.txt and Procfile exist
`pip3 freeze --local requirements.txt`
`echo web: python app.py > Procfile`

2. Create Heroku App, Select Postgres add-on, download Heroku CLI toolbelt, login to heroku (Heroku login), git init, connect git to heroku (heroku git remote -a <project>), git add ., git commit, git push heroku master.

3. `heroku ps:scale web=1`

4. In heroku app settings set the config vars to add DATABASE_URL, STRIPE API key and secret, AWS key and secret

<h2> Author </h2>

<p>
Rajaneesh Singh Bhadauria - This project was completed as part of Code Institute’s Mentored Online Full Stack Web Development course in 2019.
</p>

<h2> Acknowledgements </h2> 


Plus I have used lots other online avilable Django courses on YouTube and online blogs for various Django topics such as AWS S3 integration etc,

The Accounts, Cart and Checkout apps are based upon the sample apps from the User Authentication and Authorisation and Ecommerce mini project components of the Full Stack Frameworks with Django module.

<hr>

<h4> A demo of this site is available:- <a href="https://raj-issuetracker.herokuapp.com/" rel="nofollow">here</a> </h4>

<hr>










