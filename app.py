from venv import create
from website import create_app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)     #Running the flask server
