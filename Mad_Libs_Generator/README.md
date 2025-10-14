# Mad Libs Generator 🎭

Create hilarious stories by filling in nouns, verbs, and adjectives into fun story templates!

## 🎯 What This Script Does

This Python script generates entertaining Mad Libs stories. It randomly selects from 5 different story templates, prompts you for various types of words (nouns, verbs, adjectives, etc.), and creates a unique, often hilarious story based on your inputs!

## ✨ Features

- **No External Dependencies**: Uses only Python's standard library (`random`, `re`)
- **5 Story Templates**: Adventures, school days, interviews, cooking disasters, and vacations
- **Smart Placeholders**: Automatically detects and prompts for needed word types
- **Compact Hints**: Concise word type descriptions
- **Play Again Option**: Generate multiple stories in one session
- **Clean Output**: Beautiful formatted story presentation
- **Under 100 Lines**: Efficient code at just 84 lines!

## 🚀 Usage

Simply run the script:
```bash
python mad_libs_generator.py
```

The script will:
1. Randomly select a story template
2. Prompt you for various words (with helpful hints)
3. Generate and display your completed story
4. Offer to create another story

## 💡 Example Session

```bash
python mad_libs_generator.py
```

**Output:**
```
============================================================
🎭 MAD LIBS GENERATOR 🎭
============================================================

Story: The Epic Adventure
------------------------------------------------------------

Fill in the words:

adjective (describing word): sparkly
noun (thing): banana
verb (action): dance
place (location): moon
animal (animal): penguin
verb_ing (action+ing): singing
object (item): toaster
adverb (how): weirdly

============================================================
YOUR STORY:
============================================================

Once upon a time, a sparkly banana decided to dance to the moon. Along 
the way, they met a sparkly penguin who was singing. Together, they 
found a sparkly toaster and lived weirdly ever after!

============================================================

Create another story? (y/n): 
```

## 📚 Available Story Templates

### 1. The Epic Adventure
A classic hero's journey with unexpected twists!

### 2. The School Day
Hilarious school scenarios with wacky teachers and friends.

### 3. The Job Interview
An absurd interview that somehow leads to success.

### 4. The Cooking Disaster
Kitchen chaos with unpredictable ingredients and outcomes.

### 5. The Vacation
A bizarre trip to an unusual destination.

## 🎨 Word Types

The script prompts for these word types with concise hints:

- **noun**: thing
- **verb**: action
- **adjective**: describing word
- **adverb**: how
- **verb_ing**: action+ing
- **verb_past**: past action
- **animal**: animal
- **place**: location
- **object**: item
- **emotion**: feeling
- **food**: food
- **occupation**: job
- **number**: number

## 🛠️ How It Works

1. **Random Selection**: Chooses one of 5 story templates
2. **Extract Placeholders**: Uses regex to find required word types
3. **Get Inputs**: Prompts user with concise hints
4. **Generate & Display**: Replaces placeholders and shows the story

## ⚙️ Customization

### Add Your Own Story Templates
Edit the `STORY_TEMPLATES` list:
```python
{
    "title": "Your Story Title",
    "template": "Your story with {adjective} {noun} placeholders..."
}
```

### Add Custom Word Types
Update the `WORD_TYPES` dictionary:
```python
'your_type': 'description with examples'
```

## 🎮 Fun Tips

- **Be Creative**: The funnier your words, the better the story!
- **Mix It Up**: Try contrasting words (tiny elephant, angry happiness)
- **Play with Friends**: Take turns providing words without seeing the story
- **Theme It**: Use only food words, or only space-related words
- **Keep It Random**: Don't overthink—random words create the best stories!

## 🤝 Contributing
Issue #837 Mad Libs Generator

## ⚠️ Note

If you leave an input blank, it defaults to "thing" to keep the story flowing!
