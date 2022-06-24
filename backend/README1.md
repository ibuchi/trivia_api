# Get the Project Up and Running

## Install Dependencies

1. **Python 3.10.4** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

2. **Virtual Environment** - When using Python for this project, I advise working in a virtual setting. This keeps the dependencies you have for each project tidy and separate. Instructions for setting up a virual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).

**Note:** install the virtual evironment in the flaskr folder

3. **PIP Dependencies** - Once your virtual environment is setup and running, install the required dependencies by navigating to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

### Run the Server

1. **Backend Server** - To run the backend server, navigate to `backend` folder and run the following commands on the windows command prompt while in the virtual environment.

```bash
set FLASK_APP=flaskr
set FLASK_ENV=development
flask run
```

On running the above command, the backend server will be set up at http://127.0.0.1:5000

2. **Front Server** - This project uses NPM to manage software dependencies. NPM Relies on the package.json file located in the `frontend` directory of this repository. After cloning, open your terminal and run:

```bash
npm install
```

The frontend app was built using create-react-app. In order to run the app in development mode use `npm start`. You can change the script in the `package.json` file.

```bash
npm start
```

Open [http://localhost:3000](http://localhost:3000) to view it in the browser. The page will reload if you make edits.

Note: Prior to starting the frontend server, launch the backend server first.

```

```

#### API Documentation

# Expected endpoints and behaviours

`GET '/categories'`

- Obtains a dictionary of categories with the corresponding category string as the value and the keys being the category ids.
- Returns: An object with a single key, categories, that contains an object of id: category_string key:value pairs and a true success value

```json
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "success": true
}
```

---

`GET '/questions?page=${integer}'`

- Obtains a paginated set of questions, the total number of questions, all of the categories, and the current category string.
- Request Arguments: `page` - integer
- Returns: An object containing 10 paginated questions, the total number of questions, an object with all categories, a true success value and the string for the current category

```json
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "currentCategory": "History",
  "questions": [
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    }
  ],
  "success": true,
  "totalQuestions": 39
}
```

---

`DELETE '/questions/${id}'`

- Deletes a specified question using the id of the question
- Request Arguments: `id` - integer
- Returns: Does not need to return anything besides the appropriate HTTP status code.

---

`POST '/questions'`

- Sends a post request in order to add a new question
- Request Body:

```json
{
  "question": "Heres a new question string",
  "answer": "Heres a new answer string",
  "difficulty": 1,
  "category": 3
}
```

---

`POST '/questions/search`

- Posts a request to search for a certain question using a search term.
  -Request Body:

```json
{
  "searchTerm": "this is the term the user is looing for"
}
```

- Returns: any array of questions, a number of totalQuestions that met the search term, a true success value and the current category string

```json
{
  "questions": [
    {
      "id": 1,
      "question": "This is a question",
      "answer": "This is an answer",
      "difficulty": 5,
      "category": 5
    }
  ],
  "totalQuestions": 100,
  "success": true,
  "currentCategory": "Entertainment"
}
```

---

`GET '/categories/${id}/questions'`

- Fetches questions for a cateogry specified by id request argument
- Request Arguments: `id` - integer
- Returns: An object with questions for the specified category, total questions, a true success value and current category string

```json
{
  "currentCategory": "History",
  "questions": [
    {
      "answer": "Escher",
      "category": 2,
      "difficulty": 1,
      "id": 16,
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    }
  ],
  "success": true,
  "totalQuestions": 4
}
```

`POST '/quizzes'`

- Sends a post request in order to get the next question
- Request Body:

```json
{
    'previous_questions': [1, 4, 20, 15]
    quiz_category': 'current category'
 }
```

- Returns: a single new question object and a true success value

```json
{
  "question": {
    "id": 2,
    "question": "This is a question",
    "answer": "This is an answer",
    "difficulty": 2,
    "category": 3
  },
  "success": true
}
```

## Testing

In the activated virtual environment, navigate to the backend folder and use the command below to test the API Endpoints.

```bash
python test_flaskr.py
```
