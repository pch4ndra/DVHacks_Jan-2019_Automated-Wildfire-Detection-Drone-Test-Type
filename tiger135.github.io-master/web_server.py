#! /usr/bin/python

from flask import Flask, render_template, send_from_directory, jsonify, request
 
app = Flask(__name__, static_url_path='/static')

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('static/js', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('static/css', path)

@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('static/img', path)

@app.route('/assets/<path:path>')
def send_assets(path):
    return send_from_directory('static/assets', path)

@app.route('/sdk/<path:path>')
def send_sdk(path):

    return send_from_directory('static/sdk', path)

@app.route('/DVHacks_website/<path:path>')
def send_website(path):

    return send_from_directory('static/DVHacks_website', path)

@app.route('/mark')
def mark():
  #print("hello")
  return app.send_static_file('markers-clustering.html')

@app.route('/data/destination')
def destination():
	return jsonify(lat=37.7,lon=-122)

@app.route('/data/locations')
def locations():
    fin = open("marker_locations.txt","r")
    ret = fin.read()
    fin.close()
    return ret

@app.route('/data/center')
def center():
	center = [37.7,-122]
	return jsonify(center)

@app.route('/route')
def route():
	#print(request.args.get('lat'),request.args.get('lon'))
	return render_template('routing-from-my-location.html',lat=request.args.get('lat'),lon=request.args.get('lon'))

@app.route('/')
def home():
  return app.send_static_file('index.html')
 
@app.route('/about')
def about():
  return app.send_static_file('about.html')

@app.route('/histogram/laps')
def lap_histogram():
  return app.send_static_file('lap_histogram.html')
	
@app.route('/scatter/lap-duration')
def lap_duration_scatter():
  return app.send_static_file('scatter.html')
 
@app.route('/')
def reports():
  return app.send_static_file('reports.html')
	
if __name__ == '__main__':
  app.run(ssl_context=('cert.pem', 'key.pem'),host="0.0.0.0",debug=True)


