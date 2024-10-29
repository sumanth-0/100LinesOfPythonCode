// Fortune messages categorized by types
const fortunes = {
    humorous: [
      "Keep your friends close, but your snacks closer, {name}.",
      "{name}, a wise person once said: 'Never trust a fortune cookie.'",
      "Today is the perfect day to procrastinate, {name}.",
      "{name}, remember: a sense of humor is your best accessory!",
      "When life gives you lemons, {name}, trade them for cookies."
    ],
    inspirational: [
      "An unexpected event will bring you good fortune, {name}.",
      "Happiness is on the horizon, {name}. Prepare to be delighted!",
      "Your potential is endless, {name}. Believe in yourself!",
      "You will achieve your goals if you start today, {name}!",
      "{name}, remember: Success is no accident. It's hard work and persistence!"
    ],
    advice: [
      "{name}, remember: a watched pot never boils, but a watched cookie gets eaten!",
      "Start where you are, use what you have, and do what you can, {name}.",
      "Patience is a virtue, {name}. Good things are worth waiting for.",
      "The key to happiness, {name}, is keeping a smile on your face.",
      "Balance is key, {name}. Find joy in both work and play."
    ]
  };
  
  // Function to generate a random fortune
  function generateFortune(name, category) {
    const selectedFortunes = fortunes[category];
    const randomIndex = Math.floor(Math.random() * selectedFortunes.length);
    return selectedFortunes[randomIndex].replace("{name}", name);
  }
  
  // Function to display the fortune in the UI
  function displayFortune() {
    const name = document.getElementById('name').value.trim();
    const category = document.getElementById('category').value;
    const fortuneResult = document.getElementById('fortuneResult');
  
    // Simple validation to check if the name field is filled
    if (!name) {
      fortuneResult.innerText = 'Please enter your name to receive a fortune!';
      fortuneResult.style.color = 'red';
      return;
    }
  
    // Generate and display the fortune message
    const fortuneMessage = generateFortune(name, category);
    fortuneResult.innerText = fortuneMessage;
    fortuneResult.style.color = '#333';  // Reset color in case of error
  }
  