from flask import Blueprint, request, jsonify, render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from models.user import User
from models import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Support both JSON and form data
        if request.is_json:
            data = request.get_json()
        else:
            data = request.form

        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if not username or not email or not password:
            if request.is_json:
                return jsonify({'message': 'Missing fields'}), 400
            flash('Missing fields', 'danger')
            return redirect(url_for('auth.register'))

        if User.query.filter_by(email=email).first():
            if request.is_json:
                return jsonify({'message': 'Email already registered'}), 400
            flash('Email already registered', 'danger')
            return redirect(url_for('auth.register'))

        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(username=username, email=email, password=hashed_password)

        db.session.add(new_user)
        db.session.commit()

        if request.is_json:
            return jsonify({'message': 'User registered successfully'}), 201
        flash('User registered successfully! Please log in.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('signup.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
        else:
            data = request.form

        email = data.get('email')
        password = data.get('password')

        user = User.query.filter_by(email=email).first()

        if not user or not check_password_hash(user.password, password):
            if request.is_json:
                return jsonify({'message': 'Invalid credentials'}), 401
            flash('Invalid credentials', 'danger')
            return redirect(url_for('auth.login'))

        if request.is_json:
            return jsonify({'message': 'Login successful', 'user': {'username': user.username, 'email': user.email}}), 200
        flash('Login successful!', 'success')
        return redirect(url_for('dashboard'))  # Change to your dashboard route

    return render_template('login.html')