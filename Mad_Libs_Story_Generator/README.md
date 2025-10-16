# Mad Libs Story Generator

A fun interactive Python program that creates hilarious stories by filling in story templates with user-inputted words.

## 🎯 Features

- **Interactive Story Creation**: Choose from multiple story templates
- **User Input Collection**: Prompts for nouns, verbs, adjectives, and other word types
- **Multiple Story Templates**: Three different story themes to choose from
- **Colorful Output**: Uses emojis and formatting for an engaging experience
- **Replay Option**: Create multiple stories in one session
- **Error Handling**: Graceful handling of invalid inputs and interruptions

## 🚀 How to Run

```bash
python mad_libs_story_generator.py
```

## 🎮 How to Play

1. **Choose a Story**: Select from available story templates (1-3)
2. **Fill in the Blanks**: Enter words when prompted (nouns, verbs, adjectives, etc.)
3. **Enjoy Your Story**: Read the hilarious result of your word choices
4. **Play Again**: Create more stories or quit when you're done

## 📖 Available Story Templates

1. **The Crazy Adventure** - A tale of discovery and adventure
2. **The Silly School Day** - A humorous school scenario  
3. **The Magical Kitchen** - A whimsical cooking story

## 🎯 Example Usage

```
🎭 Welcome to the Mad Libs Story Generator! 🎭
Create hilarious stories by filling in the blanks!

📚 Available story templates:
1. The Crazy Adventure
2. The Silly School Day
3. The Magical Kitchen

Choose a story (1-3) or 'q' to quit: 1

📝 Let's create: The Crazy Adventure
========================================
Enter a adjective: silly
Enter a noun: elephant
Enter a verb: dance
Enter a place: park
Enter a time period: morning
Enter a verb: jump
Enter a adverb: quickly
Enter a adjective: purple
Enter a noun: banana
Enter a adjective: magical
Enter a object: spoon
Enter a verb: fly

🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉
📖 The Crazy Adventure
🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉

Once upon a time, there was a silly elephant who loved to dance in the park. 
Every morning, they would jump quickly with their purple banana. 
One day, they discovered a magical spoon that could fly!

🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉
```

## 🛠️ Technical Details

- **Language**: Python 3.x
- **Dependencies**: None (uses only built-in modules)
- **Code Style**: Follows PEP 8 guidelines
- **Lines of Code**: Under 100 lines (compliant with project requirements)
- **Structure**: Object-oriented design with clear method separation

## 📝 Code Structure

- `MadLibsGenerator` class: Main game logic
- `story_templates`: Predefined story templates with placeholders
- `get_user_input()`: Handles user input collection
- `collect_words()`: Gathers all required words for a template
- `generate_story()`: Fills templates with user words
- `display_story()`: Formats and displays the completed story
- `play_game()`: Main game loop with menu system

## 🎨 Customization

You can easily add new story templates by adding them to the `story_templates` list in the `__init__` method. Each template should have:

- `title`: The story name
- `template`: The story text with `{placeholder}` markers
- `words_needed`: List of tuples with (placeholder_name, word_type_description)

Example:
```python
{
    "title": "Your Story Title",
    "template": "Your story with {placeholder1} and {placeholder2}...",
    "words_needed": [
        ("placeholder1", "noun"),
        ("placeholder2", "adjective")
    ]
}
```

## 🧪 Testing

The project includes comprehensive unit tests to ensure all functionality works correctly.

### Running Tests

```bash
python test_mad_libs.py
```

### Test Coverage

The test suite includes the following test cases:

#### **Core Functionality Tests**
- **Initialization Test**: Verifies that all 3 story templates load correctly
- **Template Structure Test**: Ensures each template has required fields (title, template, words_needed)
- **User Input Test**: Tests input collection and whitespace handling
- **Story Generation Test**: Validates template filling with user words

#### **Template-Specific Tests**
- **The Crazy Adventure**: Tests the first story template with sample words
- **The Silly School Day**: Validates the school scenario template
- **The Magical Kitchen**: Verifies the kitchen story template

#### **Game Flow Tests**
- **Quit Functionality**: Tests immediate quit and graceful exit
- **Invalid Input Handling**: Ensures error messages display for invalid choices
- **Play Again Feature**: Validates replay logic

#### **Display Tests**
- **Story Display**: Verifies formatted output with emojis and decorations
- **Word Collection**: Tests the interactive prompt system

### Expected Output

When tests run successfully, you should see:
```
🧪 Mad Libs Story Generator - Test Suite
==================================================

🔍 Running Unit Tests...
test_collect_words ... ok
test_crazy_adventure_template ... ok
test_display_story ... ok
test_generate_story ... ok
test_get_user_input ... ok
test_get_user_input_strips_whitespace ... ok
test_initialization ... ok
test_invalid_input_handling ... ok
test_kitchen_template ... ok
test_quit_game_immediately ... ok
test_school_day_template ... ok
test_story_template_structure ... ok

----------------------------------------------------------------------
Ran 12 tests in X.XXXs

OK

📖 Generated Story: The Crazy Adventure
------------------------------
Once upon a time, there was a silly elephant who loved to dance in the park...
✅ Manual test completed successfully!
```

### Manual Testing

You can also test the program interactively by running:
```bash
python mad_libs_story_generator.py
```

Try these test scenarios:
1. **Happy Path**: Choose story 1, fill in all prompts, play again with story 2
2. **Quit Early**: Press 'q' at the story selection menu
3. **Invalid Input**: Enter '99' or 'abc' to test error handling
4. **Replay**: Complete a story and choose 'y' to create another, then 'n' to quit

## 🤝 Contributing

This project is part of the 100LinesOfPythonCode repository. Feel free to suggest improvements or add new story templates!

## 📄 Requirements

- Python 3.6 or higher
- No external dependencies required

## 🎭 About Mad Libs

Mad Libs is a phrasal template word game where players are asked for a list of words to substitute for blanks in a story before reading aloud. The game is frequently played as a party game or as a pastime.
