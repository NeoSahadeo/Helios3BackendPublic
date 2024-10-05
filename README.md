# Helios3 Backend

The backend written in Python using Django's REST Framework.

## What is Helios3

Helios3 is the 3rd iteration of my line of password managers.
It is by far the most secure and the most sophisticated yet.

## Security

Default Django CSRF / middleware.

The database is encrypted using [Django-Cryptography](https://github.com/georgemarshall/django-cryptography), which
uses symmetrical encryption to store passwords.

Token managment is built with [Django-Rest-Knox](https://github.com/jazzband/django-rest-knox).

PBKDF2 is swapped out for the far better [Argon2-cffi](https://github.com/hynek/argon2-cffi)

All requests besides login requires an auth token.

### Future plans

- Add 2fa
