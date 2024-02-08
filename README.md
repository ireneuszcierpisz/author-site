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

