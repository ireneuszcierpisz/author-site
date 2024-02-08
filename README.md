![CI logo](logo_small.png)

##Introduction##

 **writer|site** is intended as a blog for book authors who want to keep in touch with readers, publish posts and excerpts of work, get comments and stay in touch with readers.


## Database design models

| Class name |
| :---: |
| Post |
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

| Class name |
| :---: |
| Comment |
| type | field name |
| :---: | :---: |
title | CharField
post | ForeignKey
author | ForeignKey
body | TextField
approved | BooleanField
created_on | DateTimeField


| Class name |
| :---: |
| About |
| type | field name |
| :---: | :---: |
title | CharField
featured_image | CloudinaryField
updated_on | DateTimeField
content | TextField


| Class name |
| :---: |
| Contact |
| type | field name |
| :---: | :---: |
title | CharField
featured_image | CloudinaryField
updated_on | DateTimeField
content | TextField

| Class name |
| :---: |
| ContactRequest |
| type | field name |
| :---: | :---: |
name | CharField
email | EmailField
message | TextField
read | BooleanField
answered | BooleanField


| Class name |
| :---: |
| Excerpt |
| type | field name |
| :---: | :---: |
title | CharField
featured_image | CloudinaryField
updated_on | DateTimeField
content | TextField

