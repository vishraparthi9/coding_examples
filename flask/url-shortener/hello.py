from flask import Flask, render_template, request, redirect, url_for, flash, abort
import json
import os.path
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = '<provide a random string here>'

@app.route('/')
def home():
  # return 'Hello Flask!!'
  return render_template('home.html')

# The route name does not need to match the function name
@app.route('/your-url', methods=['GET', 'POST'])
def your_url():
  if request.method == 'POST':
    urls = {}

    # Check if urls.json file exist
    # If exist, load into urls dictionary to validate non-dup keys
    if os.path.exists('urls.json'):
      with open('urls.json') as url_file:
        urls = json.load(url_file)

    if request.form['code'] in urls.keys():
      flash('Shortname is already taken. Please select another short name')
      return redirect(url_for('home'))

    if 'url' in request.form.keys():
      urls[request.form['code']] = {'url': request.form['url']}
    else:
      f = request.files['file']
      # The below line is to make sure the user actually uplaoded a file and not a script
      # or a manicious file
      full_name = request.form['code'] + secure_filename(f.filename)
      f.save('./static/user_files/' + full_name)
      urls[request.form['code']] = {'file': full_name}

    with open('urls.json', 'w') as url_file:
      json.dump(urls, url_file)

    return render_template('your_url.html', code=request.form['code'])
  else:
    return redirect(url_for('home'))

@app.route('/<string:code>')
def redirect_to_url(code):
  if os.path.exists('urls.json'):
    with open('urls.json') as url_file:
      urls = json.load(url_file)
      if code in urls.keys():
        if 'url' in urls[code].keys():
          return redirect(urls[code]['url'])
        else:
          return redirect(url_for('static', filename='user_files/' + urls[code]['file']))
  
  return abort(404)

@app.errorhandler(404)
def page_not_found(error):
  return render_template('page_not_found.html'), 404