from app import app

server = app.server

if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=5001, debug=True, threaded=True)
