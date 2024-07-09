import socket
import pickle
import numpy as np

def main():
    # ソケット接続を確立
    host = 'localhost'
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))

        while True:
            try:
                # Javaプロセスからデータを受信
                data = s.recv(4096)
                if not data:
                    break

                # 受信したデータをnumpy配列に変換
                int_array = pickle.loads(data)
                
                # int配列をfloat配列に変換
                float_array = np.array(int_array, dtype=np.float64)

                # 変換した配列をJavaプロセスに送り返す
                s.sendall(pickle.dumps(float_array))

            except EOFError:
                break
            except Exception as e:
                print(f"Error: {e}")
                break

if __name__ == "__main__":
    main()