from app import app, db
from flask import request, jsonify, render_template
from models import User, Dish, Booking
from datetime import datetime

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/menu')
def menu():
    dishes = Dish.query.all()
    return render_template('menu.html', dishes=dishes)

@app.route('/booking', methods=['POST'])
def book_table():
    data = request.get_json()
    new_booking = Booking(
        user_id=data['user_id'],
        date=datetime.strptime(data['date'], '%Y-%m-%d %H:%M:%S'),
        status='booked',
        table_number=data['table_number']
    )
    db.session.add(new_booking)
    db.session.commit()
    return jsonify({"message": "Booking successful"}), 201

@app.route('/dishes', methods=['GET'])
def get_dishes():
    dishes = Dish.query.all()
    return jsonify([{
        "id": dish.id,
        "name": dish.name,
        "description": dish.description,
        "price": dish.price
    } for dish in dishes])

@app.route('/order', methods=['POST'])
def order_food():
    data = request.get_json()
    # Process the order here
    return jsonify({"message": "Order placed successfully"}), 201

