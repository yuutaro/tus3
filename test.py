import socket
import threading

def handle_client(client_socket):
    while True:
        try:
            # クライアントからのメッセージを受け取る
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            # メッセージが "hello" の場合の応答
            if message.strip() == "hello":
                print("Received 'hello' from client")
                client_socket.send("hello!\n".encode('utf-8'))
            else:
                print("Received unknown message from client")
                client_socket.send("I only respond to 'hello'.\n".encode('utf-8'))
        except:
            break

    # 接続を閉じる
    client_socket.close()
    
# "[1,1,1,1,1,1,1,1],[2,2,2,2,2,2,2,2], ... ,[8,8,8,8,8,8,8,8]" -> int[8][8]
def StringToBoard(board_str):
	board = [[0 for i in range(8)] for j in range(8)]
	board_str = board_str.split(',')
	for i in range(8):
		board_str[i] = board_str[i].replace('[', '')
		board_str[i] = board_str[i].replace(']', '')
		board_str[i] = board_str[i].split(' ')
		for j in range(8):
			board[i][j] = int(board_str[i][j])
	return board

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 12345))
    server.listen(5)
    print("Server started on port 12345")

    while True:
        client_socket, addr = server.accept()
        print(f"Connection from {addr}")

        # 新しいスレッドを作成してクライアントを処理
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    main()