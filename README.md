![writer|site logo](https://github.com/ireneuszcierpisz/author-site/blob/main/media/writersite-logo.png)

## Introduction ##

 **writer|site** is intended as a blog for book authors who want to keep in touch with readers, publish posts and excerpts of work, get comments and stay in touch with readers.


## Database design models

### Class name : Post
   
| type | field name |
| :---: | :---: |
title | CharField
slug | SlugField
author | ForeignKey
featured_image | CloudinaryField
content | TextField
created_on | DateTimeField
status | IntegerField
updated_on | DateTimeField


### Class name : Comment
   
| type | field name |
| :---: | :---: |
title | CharField
post | ForeignKey
author | ForeignKey
body | TextField
approved | BooleanField
created_on | DateTimeField


### Class name : About

| type | field name |
| :---: | :---: |
title | CharField
featured_image | CloudinaryField
updated_on | DateTimeField
content | TextField


### Class name : Contact

| type | field name |
| :---: | :---: |
title | CharField
featured_image | CloudinaryField
updated_on | DateTimeField
content | TextField


### Class name : ContactRequest

| type | field name |
| :---: | :---: |
name | CharField
email | EmailField
message | TextField
read | BooleanField
answered | BooleanField


### Class name : Excerpt
| type | field name |
| :---: | :---: |
title | CharField
featured_image | CloudinaryField
updated_on | DateTimeField
content | TextField

## Agile workflow was used in the development of author-site project:
- work in small iterations
- use Github kanban board

### GitHub Features were used to organize the build process:

#### list of issues
![issues](https://github.com/ireneuszcierpisz/author-site/blob/main/media/issues.png)

#### kanban board of the done issues
![kanban-board](https://github.com/ireneuszcierpisz/author-site/blob/main/media/kanban-board.png)


## Features

### Admin panel where a superuser can see and manipulate data
![admin panel](https://github.com/ireneuszcierpisz/author-site/blob/main/media/admin-panel.png)

### Allauth authentication
![sign-up](https://github.com/ireneuszcierpisz/author-site/blob/main/media/sign-up.png)

### Home page where a user can see posts
![home](https://github.com/ireneuszcierpisz/author-site/blob/main/media/home.png)

### Post detail page with comments field where a user can add, update and delete a comment
![comment](https://github.com/ireneuszcierpisz/author-site/blob/main/media/comment.png)

### Alerts showing success or error message to a user
![comment-alert](https://github.com/ireneuszcierpisz/author-site/blob/main/media/comment-alert.png)
![message-alert](https://github.com/ireneuszcierpisz/author-site/blob/main/media/message-alert.png)
![sign-out-alert](https://github.com/ireneuszcierpisz/author-site/blob/main/media/sign-out-alert.png)
![sign-in](https://github.com/ireneuszcierpisz/author-site/blob/main/media/sign-in-alert.png)

### Contact page
![contact](https://github.com/ireneuszcierpisz/author-site/blob/main/media/contact.png)

### Excerpt page
![excerpt](https://github.com/ireneuszcierpisz/author-site/blob/main/media/excerpt.png)

## Validator testing

### W3C Markup Validator

#### post_index.html
![w3-posts](https://github.com/ireneuszcierpisz/author-site/blob/main/media/w3-posts.png)

#### contact.html
![w3-contact](https://github.com/ireneuszcierpisz/author-site/blob/main/media/w3-contact.png)

#### about.html
![w3-about](https://github.com/ireneuszcierpisz/author-site/blob/main/media/w3-about.png)

#### excerpt.html
![w3-excerpt](https://github.com/ireneuszcierpisz/author-site/blob/main/media/w3-excerpt.png)


### Automated Django Testing


### Deployment

#### Install packages:
```
pip3 install Django~=4.2.1
pip3 install gunicorn~=20.1
pip3 install dj-database-url~=0.5 psycopg2~=2.9
pip3 install django-summernote~=0.8.20.0
pip3 install whitenoise~=5.3.0
pip3 install django-allauth~=0.57.0
pip3 install django-crispy-forms~=2.0 crispy-bootstrap5~=0.7
pip3 install cloudinary~=1.36.0 dj3-cloudinary-storage~=0.0.6 urllib3~=1.26.15
```

#### Create requirements
`pip3 freeze --local > requirements.txt`

#### Create project
`django-admin startproject my_project`

#### Create app
`python3 manage.py startapp my_app`

#### Add apps to settings.py

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary_storage',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'crispy_forms',
    'crispy_bootstrap5',
    'django_summernote',
    'cloudinary',
    'blog',
    'about',
    'contact',
    'excerpt',
]
```

#### Create database

- Create an ElephantSQL.com account
- Navigate to ElephantSQL.com and click “Log in”
- Sign in with GitHub
- Authorise ElephantSQL with your selected GitHub account
- In the Create new team form:
    - Add a team name
    - Read and agree to the Terms of Service
    - Select Yes for GDPR
    - Provide your email address
    - Click “Create Team”
- Give your plan a Name
- Select the Tiny Turtle (Free) plan
- Select Region
- Click Review
- Click Create instance
- Click on your newly named instance
- Click on STATS
- Click on DETAILS and copy the URL

#### Set up env.py
```
import os
os.environ.setdefault("DATABASE_URL", "postgres: url_from_postgres")
```

#### Import env.py to settings
`if os.path.isfile('env.py'): import env`


### Deployment to Heroku
- in project settings.py:  `DEBUG=False`
- in Heroku > Settings > ConfigVars: 
  key: `DATABASE_URL`   value: `url_from_postgres`


### Credits

- Content
        - the content of the site is only my invention
- Media
        - all images are my own
- Code
        - the code for creating this project was taken from Code Institute lecture
- Mentor
        - thanks to my mentor Gareth McGirr for support
