import os
import threading
import http.server
import ssl

def domake():
    server_address = ('localhost', 8444)
    httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)

    # 建立 SSLContext
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile='./localhost.crt', keyfile='./localhost.key')

    # 使用 wrap_socket 包裝 socket
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

    print(os.getcwd())
    print("8444 HTTPS server started")
    httpd.serve_forever()

# 利用執行緒啟動 HTTPS 伺服器
make = threading.Thread(target=domake)
make.start()
