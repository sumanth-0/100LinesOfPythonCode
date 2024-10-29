## NOTE

You need to make a .env file in the same directory as this file. It consists of the following environment variable-
```
API_KEY = <your google api key>
```

You need to get valid API key for Books API by following steps -

### 1. Go to Google Cloud Console: [Google Cloud Console](https://console.cloud.google.com/).

   Create a New Project:
   Click on the project drop-down on the top-left.
   Click on "New Project," name it (e.g., "Book Search"), and click "Create."

### 2. Enable the Google Books API:
   
   In the Google Cloud Console, navigate to APIs & Services > Library.
   Search for "Google Books API" and click on it.
   Click the "Enable" button.
   
### 3. Create Credentials:

   Navigate to APIs & Services > Credentials.
   Click on "Create Credentials" and select "API Key."
   
Your new API key will be generated. Copy it and put it in the .env file.
