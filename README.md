# The Gram
## This is a photo posting website created using Django., 26/01/2018


## By **[Kepha Okari](https://github.com/kepha-okari)**

## Description
[This](https://kepha-gram.herokuapp.com/) is a photo posting website created using Django. A user with an account can:
* post images with captions
* view list of other users
* follow other users and see their posts on their timeline
* like a post
* comment on a post
* download an image

## User Stories
As a user I would like:
* to sign in to use the application
* to upload photos
* to see my profile with my posts
* to follow others and see their picture on my timeline
* to like a picture and leave a comment on it
* download a picture and save it to my machine

## Specifications
| Behavior        | Input           | Outcome  |
| ------------- |:-------------:| -----:|
| Display sign up for | N/A | Display sign up form when a user visits the site |
| Create an account | Fill the sign up form and **click submit** | Create an account and profile for the user and log the user into the site |
| Display current user's profile | **Click** the user icon | Display the current user's profile page with their posts |
| Upload a post | **Click** create post | Direct the user to a page with a form where the user can create and submit a post |
| See other users | **Click** compass icon | Direct the user to a page where they see a list of other users |
| Follow a user | **Click** follow link | Direct user to their timeline where they see the posts by the user he/she is following |
| Comment on post | **Click** comment link | Direct user to a page with a form for writing a comment |
| Like a post | **Click** heart icon | Redirect to the timeline page where the like count increases and the like button is disabled |
| Download an image post | **Click** download | Download the selected image onto the machine of the current user |

## Setup/Installation Requirements

### Prerequisites
* Python 3.6.2
* Virtual environment
* Postgres Database
* Internet


### Installation Process
1. Copy repolink
2. Run `git clone REPO-URL` in your terminal
3. Write `cd the-gram`
4. Create a virtual environment with `virtualenv virtual` or try `python3.6 -m venv virtual`
5. Create .env file `touch .env` and add the following:
```
SECRET_KEY=<your secret key>
DEBUG=True
```
6. Enter your virtual environment `source virtual/bin/activate`
7. Run `pip install -r requirements.txt` or `pip3 install -r requirements.txt`
8. Create Postgres Database

```
psql
CREATE DATABASE instagram
```
9. Change the database informatioin in `instagrama/settings.py`
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'instagram',
        'USER': *POSTGRES_USERNAME*,
        'PASSWORD': *POSTGRES_USERNAME*,
    }
}
```
10. Run `./manage.py runserver` or `python3.6 manage.py runserver` to run the application


## Known Bugs

No known bugs


## Technologies Used
- Python3.6
- Django
- Bootstrap
- Postgres Database
- CSS
- HTML
- Heroku

### License

**[MIT](./LICENSE)** (c) 2018 **[Kepha Okari](https://github.com/kepha-okari)** 
