import socketserver
from socketserver import BaseRequestHandler


class MyHandler(BaseRequestHandler):

    def handle(self) -> None:
        while True:
            msg = self.request.recv(1024).strip()
            if not msg:
                print("客户端已断开...")
                self.request.close()
                break
            print(dir(self.request))
            print(self.request)
            print("receive [{}] from [{}]:".format(msg, self.client_address[0]))
            # just send back the same data, but upper-cased
            self.request.send(msg.upper())
            self.finish()


if __name__ == '__main__':
    server = socketserver.TCPServer(("localhost", 9999), MyHandler)
    print("准备接受请求...")
    server.serve_forever()
