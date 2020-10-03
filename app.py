#./app.py
import route, run from bottle
import os

@route('/')
def main():
	return"Hello world"

if 'DYNO' in os.enivron:
	run(host='0.0.0.0', port=os.environ.get('PORT', 9000))
else:
	run(host="localhost", port=9000, debug=True, reloader=True)