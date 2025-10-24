# Install the library if not already installed
# pip install wikipedia
import wikipedia

def fetch_summary(topic, sentences=3):
    try:
        # Set language (optional, default is 'en')
        wikipedia.set_lang("en")
        
        # Fetch summary
        summary = wikipedia.summary(topic, sentences=sentences, auto_suggest=True, redirect=True)
        print(f"\n📖 Summary of '{topic}':\n")
        print(summary)
    
    except wikipedia.exceptions.DisambiguationError as e:
        print(f"⚠️ Topic '{topic}' is ambiguous. Possible options:")
        for option in e.options[:5]:
            print(" -", option)
    
    except wikipedia.exceptions.PageError:
        print(f"❌ Topic '{topic}' not found on Wikipedia.")
    
    except Exception as e:
        print("🌐 An error occurred:", e)


if __name__ == "__main__":
    print("🔍 Wikipedia Summary Fetcher")
    print("Type 'exit' to quit\n")
    
    while True:
        topic = input("Enter a topic to fetch summary: ").strip()
        if topic.lower() == 'exit':
            print("Goodbye 👋")
            break
        if not topic:
            print("Please enter a valid topic.")
            continue
        
        fetch_summary(topic)
        print("-" * 500)
