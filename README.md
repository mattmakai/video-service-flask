# Customer Service with Twilio Video

This is an example application demonstration a customer service use case
with Python and the [Flask](http://flask.pocoo.org/) web framework. In
addition, this project contains other third-party modules in the 
requirements.txt file that may be useful in creating application with Twilio.


## Deploy On Heroku
[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy?template=https://github.com/TwilioDevEd/video-service-flask)


## Running the Project on Your Machine
Development environment requirements:

* PostgreSQL with access to create a database such as "videoflask"
* [virtualenv](https://virtualenv.pypa.io/en/latest/) and 
  [pip](http://www.pip-installer.org/en/latest/) to install dependencies.

1. Create a new virtualenv.
    virtualenv videoflask
    source videoflask/bin/activate
    
1. Clone repository at https://github.com/TwilioDevEd/video-service-flask

git clone git@github.com:makaimc/aquarius-python-flask
Change into the new directory.

cd aquarius-python-flask
Install local dependencies.

pip install -r requirements.txt
Set environment variables.

export SECRET_KEY='super secret key'
export DATABASE_URL='postgresql://username:password@localhost/2faf'
export TWILIO_ACCOUNT_SID='authyapikey'
Create database and schema.

createdb 2faf
python create_db.py
Run the app.

python run.py
Open web browser and head to http://localhost:5000/ to see the app.


### Install Dependencies



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
ngrok -subdomain=chunky-danger-monkey 5000
```


## License
MIT
