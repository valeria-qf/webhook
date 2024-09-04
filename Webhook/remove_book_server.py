from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class BookServerHandler(BaseHTTPRequestHandler):
    books = [
        "Interestellar",
        "O Senhor dos Anéis",
        "Forrest Gump"
    ]

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        try:
            data = json.loads(post_data)
            book_title = data.get('title')

            if not book_title:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                response = {"status": "error", "message": "Título do livro não fornecido"}
                self.wfile.write(json.dumps(response).encode('utf-8'))
                print("Erro: Título do livro não fornecido")
                return

            if book_title not in self.books:
                self.send_response(404)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                response = {"status": "error", "message": "Livro não encontrado na lista"}
                self.wfile.write(json.dumps(response).encode('utf-8'))
                print("Erro: Livro não encontrado na lista")
                return

            self.books.remove(book_title)
            print(f"Livro removido: {book_title}")

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {"status": "success", "message": "Livro removido com sucesso"}
            self.wfile.write(json.dumps(response).encode('utf-8'))
            print("Resposta enviada com sucesso")

        except json.JSONDecodeError:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {"status": "error", "message": "Erro ao processar o JSON"}
            self.wfile.write(json.dumps(response).encode('utf-8'))
            print("Erro ao processar o JSON")

def run(server_class=HTTPServer, handler_class=BookServerHandler, port=5000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Servidor rodando na porta {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run(port=5001)
