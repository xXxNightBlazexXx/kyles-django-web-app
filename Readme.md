# MOBILE GAMES WEB APP

## Project Status
This project is on hold for development, and is more of a concept at the moment, I need to set up multiple APIs to pull the game data from the stores I am most interested in viewing.

## What this project is
This project stores and showcases game stores data in reports that allow users to see what games are the most popular and drill down based upon they preferences e.g. (Free, Paid, Genre, Etc.)

## Dev setup
- Run the requirements.txt (pip install -r requirements.txt)
- Install tailwindcss using NPM (npm install -D tailwindcss)
- npx tailwindcss -i ./static/src/input.css -o ./static/src/output.css --watch (This command will watch for html changes to know what css styles to bring in)
- Populate the database
    - run the import_mobile_games.py
    - perform migrations
- python manage.py runserver
