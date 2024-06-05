from concurrent import futures
import grpc
import auth_pb2
import auth_pb2_grpc


class AuthService(auth_pb2_grpc.AuthServiceServicer):
    def Register(self, request, context):
        response = auth_pb2.RegisterResponse()

        if user_exists_reg(request.username):
            response.success = False
            response.message = "User already exists"
        else:
            # Регистрируем пользователя
            response.success = True
            response.message = "User registered successfully"
            # Добавляем пользователя в файл
            add_user_to_file(request.username, request.password)

        return response


    def Login(self, request, context):
        response = auth_pb2.LoginResponse()

        if user_exists_log(request.username, request.password):
            response.success = True
            response.message = "Login successful"
        else:
            response.success = False
            response.message = "Invalid username or password"

        return response


def add_user_to_file(username, password):
    with open('users.txt', 'a') as file:
        file.write(f'{username}:{password}\n')


def user_exists_reg(username):
    with open('users.txt', 'r') as file:
        for line in file:
            if line.strip().split(':')[0] == username:
                return True
        return False



def user_exists_log(username, password):
    with open('users.txt', 'r') as file:
        for line in file:
            stored_username, stored_password = line.strip().split(':')
            if stored_username == username and stored_password == password:
                return True
    return False


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    auth_pb2_grpc.add_AuthServiceServicer_to_server(AuthService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
