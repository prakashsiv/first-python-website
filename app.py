from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Bengaluru',
  'salary': 'Rs.1000000',
}, {
  'id': 2,
  'title': 'Data Scientist',
  'location': 'Hyderabad',
  'salary': 'Rs.1500000',
}, {
  'id': 3,
  'title': 'UI Developer',
  'location': 'Chennai',
  'salary': 'Rs.1200000',
}, {
  'id': 4,
  'title': 'DB Admin',
  'location': 'Remote',
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


##print(__name__)##here this will print __main__

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
