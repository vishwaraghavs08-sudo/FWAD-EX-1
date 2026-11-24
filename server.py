from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


HOST = "127.0.0.1"
PORT = 8000


def main() -> None:
    web_directory = Path(__file__).resolve().parent
    handler = partial(SimpleHTTPRequestHandler, directory=str(web_directory))

    with ThreadingHTTPServer((HOST, PORT), handler) as server:
        print(f"Serving pages at http://{HOST}:{PORT} (press Ctrl+C to stop)")
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")


if __name__ == "__main__":
    main()