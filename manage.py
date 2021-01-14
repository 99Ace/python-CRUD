from flask import Flask, render_template, redirect, url_for, request
import random

app = Flask('app')
data = [
  { #item
    '_id' : '00001',
    'user' : 'Ace',
    'gender': 'Male',
    'status': 'supervisor'
  },
  { #item
    '_id' : '00002',
    'user' : 'Mary',
    'gender': 'Female',
    'status': 'staff'  
  },
  { #item
    '_id' : '00003',
    'user' : 'John',
    'gender': 'Male',
    'status': 'staff'  
  }
]
# create a route
@app.route('/')
def index():
  # load in data
  # pass data to index.html
  return render_template('index.html', users=data)
# Create route
@app.route('/create')
def create():
  return render_template('create.html')
@app.route('/create', methods=["POST"])
def insert():
  #get info from html form submission
  new_id = str( random.randint(1, 10000 ))
  new_user = request.form.get('user')
  new_gender = request.form.get('gender')
  # put info into a new set of data
  new_data = {
    '_id' : new_id,
    'user': new_user,
    'gender': new_gender,
  }
  # save into current database
  data.append(new_data)
  return redirect(url_for('index'))

# Update route
@app.route('/update/<user_id>')
def update(user_id):
  count = 0
  length= len(data)
  while count < length:
    if data[count]['_id'] == user_id:
      return render_template('update.html', user=data[count])
    count = count + 1
  return redirect(url_for('index'))

@app.route('/update/<user_id>', methods=['POST'])
def update_user(user_id):  
  count = 0
  length= len(data)
  while count < length:
    if data[count]['_id'] == user_id:
      data[count]['user'] = request.form.get('user')
      data[count]['gender'] = request.form.get('gender')
    count = count + 1
  return redirect(url_for('index'))

# Delete route
@app.route('/delete/<user_id>')
def delete(user_id):
  count = 0
  length= len(data)
  while count < length:
    if data[count]['_id'] == user_id:
      return render_template('delete.html', user=data[count])
    count = count + 1
  return redirect(url_for('index'))
  # return render_template('delete.html')
  
@app.route('/confirm_delete/<user_id>')
def confirm_delete(user_id):
  # delete it
  count = 0
  length= len(data)
  while count < length:
    if data[count]['_id'] == user_id:
      print(data[count])
      del data[count]
      break
    count = count + 1
  return redirect( url_for('index'))

app.run(host='0.0.0.0', port=8080)
