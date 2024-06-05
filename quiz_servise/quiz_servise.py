from flask import Flask, render_template, request, redirect, url_for, flash
import grpc
import auth_pb2
import auth_pb2_grpc

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# gRPC client setup
auth_channel = grpc.insecure_channel('localhost:50051')
auth_stub = auth_pb2_grpc.AuthServiceStub(auth_channel)

@app.route('/')
def home():
    return render_template('register.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    response = auth_stub.Login(auth_pb2.LoginRequest(username=username, password=password))

    if response.success:
        flash('Login successful!', 'success')
        return redirect(url_for('quiz'))  # Перенаправление на страницу с викториной
    else:
        flash(response.message, 'danger')
        return redirect(url_for('home'))

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']

    response = auth_stub.Register(auth_pb2.RegisterRequest(username=username, password=password))

    if response.success:
        flash('Registration successful!', 'success')
        return redirect(url_for('quiz'))  # Перенаправление на страницу с викторинами
    else:
        flash(response.message, 'danger')
        return redirect(url_for('home'))

@app.route('/quiz')
def quiz():
    # Здесь может быть логика для отображения страницы с викториной
    return render_template('quiz.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
