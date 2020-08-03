## Weather Mini Challenge

Suppose you live in Ribeirão Preto. Should you take an umbrella?

You tell us!

If the air humidity on a given day is **greater** than **70%**, it is a good idea to take an umbrella with you.
Your goal is to fetch the Ribeirão Preto air humidity forecast for the next **five** days from https://openweathermap.org/api and display the following message template:

_You should take an umbrella in these days: ...._

For instance, if on the next five days air humidity will be greater than 70% on Monday, Tuesday and Wednesday, you must display the message:

_You should take an umbrella in these days: Monday, Tuesday and Wednesday._

## How to run

Add openweathermap api key to conf.ini:
API_KEY=YOUR_API_KEY

Install requirements:
python3 -m pip install -U -r requirements.txt

To run the server you need to set an environment variable:

for linux/mac:
export FLASK_APP=app.py

for windows:
set FLASK_APP=app.py

And to run the app in development mode:
flask run

To run the tests:
pytest
