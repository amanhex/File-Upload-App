# Flask File Upload

This is a simple Flask web application that allows users to upload files, view and download them. The application is built using Flask framework and Python programming language.

## Getting Started

To run this application, you need to have Python 3 and Flask installed on your system. You can install Flask using pip, a package manager for Python.

```
pip install flask
```

## Usage

To run the application, navigate to the project directory and run the following command:

```
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

This will start the development server on port 5000. You can access the application by navigating to http://localhost:5000 in your web browser.


##  Features

- Users can upload files to the server.
- Users can view a list of uploaded files with their name, size and extension.
- Users can download uploaded files.
- Users can remove uploaded files.


##  File Structure

- app.py - Contains the Flask application code.
- static - Contains static assets like CSS files.
- templates - Contains HTML templates used by the Flask application.
- uploads - Contains uploaded files.


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
