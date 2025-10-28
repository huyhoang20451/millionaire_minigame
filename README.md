# Millionaire Web Game

A web-based millionaire quiz game built with FastAPI and vanilla JavaScript, with a separate terminal-based version for debugging.

## Features

- 8 levels of multiple-choice questions (A, B, C, D)
- 3 support options (each can be used once per game):
  - **50/50**: Removes 2 wrong answers
  - **Change Question**: Get a new question for the current level
  - **AI Support**: Get an intelligent hint from Google Gemini AI that uses verified facts from the question's explanation to help you think through the answer (without giving it away directly)
- Questions stored in JSON format with explanations
- **Google Gemini AI Integration**: AI Support uses the question's explanation as factual context to provide accurate, helpful hints
- Visual progress tracker (web version)
- Responsive design (web version)
- **Terminal version for easy debugging**

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Set up Google Gemini API (for AI Support feature):
   - Get your API key from: https://makersuite.google.com/app/apikey
   - Create a `.env` file in the project root (copy from `.env.example`):
     ```bash
     cp .env.example .env
     ```
   - Add your API key to the `.env` file:
     ```
     GEMINI_API_KEY=your_actual_api_key_here
     ```
   - **Note**: The game will work without the API key, but AI Support will use a simple fallback mode instead of the intelligent Gemini-powered hints.

3. (Optional) Install python-dotenv if you want to use .env file:
```bash
pip install python-dotenv
```

## Running the Game

### Option 1: Web Version

1. Start the FastAPI server:
```bash
python main.py
```

Or using uvicorn directly:
```bash
uvicorn main:app --reload
```

2. Open your web browser and navigate to:
```
http://localhost:8000
```

### Option 2: Terminal Version (for debugging)

Run the game directly in your terminal:
```bash
python gamelogic.py
```

This version is perfect for:
- Testing game logic without a browser
- Debugging the core game mechanics
- Quick testing of questions and answers
- Development and troubleshooting

## Game Structure

### Files
- `gamelogic.py`: **Core game logic class** - Contains the `MillionaireGame` class with all game mechanics. Can be run standalone in terminal.
- `ai_support.py`: **Gemini AI Integration** - Handles Google Gemini API calls for intelligent AI hints using question explanations as factual context
- `main.py`: FastAPI web server that uses `MillionaireGame` class from `gamelogic.py`
- `questions.json`: Question database with 10 sample questions (each includes an explanation field used by AI)
- `templates/index.html`: Frontend HTML, CSS, and JavaScript
- `requirements.txt`: Python dependencies
- `.env.example`: Example environment variables file (copy to `.env` and add your API key)

### Question Format
Each question in `questions.json` has the following structure:
```json
{
  "id": 1,
  "level": 1,
  "question": "Question text?",
  "answer1": "Option A",
  "answer2": "Option B",
  "answer3": "Option C",
  "answer4": "Option D",
  "correct": 3,
  "explanation": "Academic explanation of the correct answer"
}
```

### API Endpoints

- `GET /`: Main game page
- `POST /api/start`: Start a new game session
- `POST /api/answer`: Submit an answer
- `POST /api/support`: Use a support option
- `GET /api/session/{session_id}`: Get session information

## How to Play

### Web Version
1. Click "Start Game" to begin
2. Read the question and select your answer (A, B, C, or D)
3. Use support options wisely:
   - **50/50**: Eliminates 2 incorrect answers
   - **Change Question**: Replaces current question with another from the same level
   - **AI Support**: Shows an academic explanation based on the question's context
4. Answer all 8 levels correctly to win!

### Terminal Version
1. Run `python gamelogic.py`
2. Press Enter to start
3. Choose your action:
   - Type A, B, C, or D to answer
   - Type S to access support menu
   - Type Q to quit
4. In support menu, choose:
   - 1 for 50/50
   - 2 for Change Question
   - 3 for AI Support
   - B to go back
5. Answer all 8 levels correctly to win!

## Debugging

The separation of game logic into `gamelogic.py` makes debugging easier:

1. **Test game logic independently**: Run `python gamelogic.py` to test without the web interface
2. **Import in other scripts**: You can import the `MillionaireGame` class for testing:
   ```python
   from gamelogic import MillionaireGame
   
   game = MillionaireGame()
   game.start_game()
   state = game.get_current_state()
   print(state)
   ```
3. **Unit testing**: The class-based design makes it easy to write unit tests
4. **Quick iteration**: Test question changes and game logic without restarting the web server

## Adding More Questions

Edit `questions.json` and add more questions with levels 1-8. The game will randomly select questions from the available pool for each level.

## Customization

- Modify the number of levels by changing the win condition in `main.py` (currently set to 8)
- Adjust styling in the `<style>` section of `templates/index.html`
- Add more support options in the backend logic

## Technologies Used

- **Backend**: FastAPI, Python
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Data Storage**: JSON file (questions.json)

## Future Enhancements

- User authentication and score tracking
- Database integration for question storage
- Sound effects and animations
- Timer for each question
- Different difficulty modes
- Multi-language support

## License

MIT License - Feel free to use and modify for your projects!
