Issuetracker

[![Build Status](https://travis-ci.org/rajaneesh80/Issue-Tracker-web-app.svg?branch=master)](https://travis-ci.org/rajaneesh80/Issue-Tracker-web-app)

<hr>
<h2> Raj_Issuetracking_Web_App </h2>
<hr>

<h2> Overview </h2>

A web application created in Python and Django-version-2.2.5.

<ul>

<li>This is a web application that allow users to create issues, comment on issues, and show the status of an issue (‘to do,’ ‘doing,’ or ‘done’). </li>

<li> Issues come in two varieties – ‘bugs’ (fix for free), and ‘features’ (only develop if offered enough money). </li>

<li> To help prioritize the work, users are able to upvote bugs (signifying ‘I have this too’), and upvote feature requests (signifying ‘I want to have this too’).</li>

<li> While upvoting bugs is free, to upvote a feature request, users need to pay some money to pay for development time in working on it. </li>

<li> This is a full stack web application (frontend and backend) that provides CRUD (Create, Read, Update, Delete) functionality to a database hosted in the cloud on Heroku platform as a service.</li>

</ul>

<hr>

<h2> UX </h2>

This website was created with the intention to create user report the issuees.
Details of the UX design is available in the 'Wire-Frame' folder. 
This document outlines how I approached the design of the user interface of the main pages of the web application.

<hr>

<h2> Features <h2> 

<h3> Users can <h3>  :

<ul>

<li> View list of all Issues sorted by newest descending and search by keyword.</li>
<li> Add New Issue.</li>
<li>Add New Comment to an Issue.</li>
<li>Edit the  Old Comment to an Issue.</li>
<li>Upvote Bugs for free.</li>
<li>Upvote Features by adding the desired quantity of upvotes of an issue to the cart and using the checkout functionality to submit a payment</li>
<li>View list of Issues created by current logged in user (My Issues)</li>
<li> Save Issue and view list of Saved Issues</li>
<li></li>
</ul>

<h3> A demo of this site is available:- <a href="https://raj-issuetracker.herokuapp.com/" rel="nofollow">here</a> </h3> 

<hr>

<div>
<h2> Getting started / Deployment </h2>

<p>

This project was deployed at Heroku
Create requirements.txt

pip3 freeze --local requirements.txt

Create Procfile

echo web: python app.py > Procfile

Create Heroku App

Set Config Vars adding IP and PORT on Heroku app settings

IP 0.0.0.0
PORT 5000
Login to Heroku on the terminal

Heroku login
Deploy to Heroku

Scale the app's web process to 1 dyno: heroku ps:scale web=1
git remote add https://git.heroku.com/Issue-Tracker-web-app.git
git push heroku master

<h4> A demo of this site is available:- <a href="https://raj-issuetracker.herokuapp.com/" rel="nofollow">here</a> </h4>

</ul>

</p>

</div>

<hr>
<h2>Technologies Used </h2>

<h3> Built With </h3>

Python Django-Python framework Postgres SQL database
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



<hr>

<h2> Testing </h2>

All the CRUD actions were tested and are working as it should. When updating a recipe the same is duplicated, this will be fixed later. I've added a delete button on the card so it can be deleted easily instead of the need to go to the recipe page to do so. The responsiveness was tested on every page. Every link was tested and works properly. All forms handle empty input fields


<h2> Author </h2>
<p>
Rajaneesh Singh Bhadauria - This project was completed as part of Code Institute’s Mentored Online Full Stack Web Development course in 2019.
</p>

<h2> Content </h2> 



<h2> Media </h2> 

<ul>

<li> The images used in this site were obtained from: <a href="" rel="nofollow"> .com/ </a> </li>

</ul>

<h2> Content </h2> 

<ul>

<li>

The content for  was taken from the <a href=""> Jira </a>

</li>

</ul>

<h2> Acknowledgements </h2> 

<ul>

<li> I work Jira at work, we are small team may be in future I will make this app alternative to Jira for small team to report the issue and allocate the work in team </li>

</ul>






