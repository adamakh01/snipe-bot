# Snipe Bot

This fun little Discord bot tracks the Math SI leaders' snipe (picture) count when their user account is mentioned with a picture in the #leaders-in-the-wild channel on the Math SI server :p.

## Tech Stack
TBD

## Quick Start

### Prerequistes
1. Make sure you have Python's uv installed.
2. Follow the instructions here: https://pydevtools.com/handbook/how-to/how-to-install-uv/
3. Create a Bot on the Discord Developer Portal (if you haven't created a bot yet):

   1. Navigate to the Discord Developer Portal
   2. Click the "Create" button and then "Build a bot for your server or community"
   3. Get your token by clicking "Reset Token" to generate a new Token. NOTE: You can't view the token again unless you generate a new one, so keep it safe!
  

### Running the Bot

  1. Install dependencies using uv:
  
     ```bash
     uv sync
     ```
 2. Make sure you initialize a ```.env``` file with your generated Discord bot token:
    ```bash
    DISCORD_TOKEN=[yourTokenNoQuotes]
    ```
 3. Run ```bot.py``` to verify everything is properly connected:
    ```bash
    uv run bot.py
    ```
