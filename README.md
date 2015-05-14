# Customer Service with Twilio Video

This is an example application demonstration a customer service use case
with Python and the [Flask](http://flask.pocoo.org/) web framework. In
addition, this project contains other third-party modules in the 
requirements.txt file that may be useful in creating application with Twilio.


## Deploy On Heroku
[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy?template=https://github.com/TwilioDevEd/video-service-flask)

When deploying from the commandline instead of the Heroku Deploy button, use 
the following commands from the root of the project directory.

        heroku create

        heroku config:set SECRET_KEY='something super secret'
        heroku config:set TWILIO_ACCOUNT_SID='ACxxxxxxxxxxxxxxxx'
        heroku config:set TWILIO_AUTH_TOKEN='xxxxxxxxxxxxxxxxxxx'
        heroku config:set DATABASE_URL='postgresql://user:passwd@localhost/videoflask'
        
        heroku addons:add heroku-postgresql

        git push heroku master

        heroku run python create_db.py


## Running the Project on Your Machine
Development environment requirements:

* [PostgreSQL](http://www.postgresql.org/) with access to create a 
  database such as "videoflask"
* [virtualenv](https://virtualenv.pypa.io/en/latest/) and 
  [pip](http://www.pip-installer.org/en/latest/) to install dependencies.

1. Create a new virtualenv.

        virtualenv videoflask
        source videoflask/bin/activate


1. Clone repository at https://github.com/TwilioDevEd/video-service-flask

        git clone git@github.com:TwilioDevEd/video-service-flask


1. Change into the new directory.

        cd video-service-flask


1. Install local dependencies.

        pip install -r requirements.txt


1. Set environment variables. Make sure to replace the values with your
   own environment settings.

        export DEBUG=True
        export SECRET_KEY='super secret key'
        export DATABASE_URL='postgresql://user:passwd@localhost/videoflask'
        export TWILIO_ACCOUNT_SID='ACxxxxxxxxxxxxxxxxxxxx'
        export TWILIO_AUTH_TOKEN='ACxxxxxxxxxxxxxxxxxxxx'


1. Create database and schema.

        createdb videoflask
        python create_db.py


1. Run the app.

        python run.py


Open web browser and head to http://localhost:5000/ to see your local app
running.



### Exposing Webhooks to Twilio
You will likely need to expose your local Flask web application on the 
public Internet to work with Twilio. We recommend using 
[ngrok](https://ngrok.com/docs) to accomplish this. Use ngrok to expose 
a local port and get a publicly accessible URL you can use to accept 
oncoming calls or texts to your Twilio numbers.

The following example would expose your local Flask application running on 
port 5000 at `http://meow-danger-cat.ngrok.com` (reserved subdomains 
are a paid feature of ngrok):

```bash
ngrok -subdomain=meow-danger-cat 5000
```


## License
MIT
