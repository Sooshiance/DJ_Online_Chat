# Real Time Chat Application

This is an Online chat application with Django that can integrate with Redis.

## Primary Configurations

If you wanna test this out :

- first fill up some settings like `SECRET_KEY` and `DEBUG` (I removed them for security reasons).

- create `migrations` folders in **user** and **chat** app and also create **__init__.py** in both migrations folders.

- If you have `Redis` server on your machine, You can activate it and uncomment the `CHANNEL_LAYERS` setting in `settings.py`.

- I assume that you don't have `Redis` or `Docker-CLi`; therefor I'd config the `CHANNEL_LAYERS` with `InMemoryChannelLayer`.

- If you have `Reids`, you can config the `CHANNEL_LAYERS` with it, just uncomment that setting and comment others.

- Run the regular `Django` commands like : 
<<python3 maage.py makemigration>>
<<python3 manage.py migrate>>
<<python3 manage.py createsuperuser>>

- If You have `Postgresql`, you can connect the app with it (I'v set the congurations in the end of `settings.py`).

- You can run <<python3 manage.py test>> to test the application integrity.

- Now if the `test` command have no issues you can run `python3 manage.py runserver`.

### Browser Test

If you'v done all those commands above, now you ready to launch your browsers : 

- Open 2 browsers like **Firefox** and **Chrome**

- **Firefox** go into `admin` panel and create a chat room.

- **Firefox** you can create new chat room if you signed as super user and go to this url `http://127.0.0.1:8000/create/room/`

- **Firefox** Second go into `register` page and add another account.

- **Chrome** in the first tab just go into `http://127.0.0.1:8000/user/` url and enter the new user credentials.

- Perfect, You're done! Select a room and start conversation in your localhost

#### Add Features

If you wanna add new features like timestamp you can add it to.

##### Docker Compose

I will add **docker compose** for Redis, in few days later.
