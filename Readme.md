# MOBILE GAMES WEB APP

## What this project is
This project houses some information about the developer as well current projects. Additionally showcasing some web-app development skills using Python, Django, Datatables, and TailwindCSS

## Dev setup
- Run the requirements.txt (pip install -r requirements.txt)
- Install tailwindcss using NPM (npm install -D tailwindcss)
- npx tailwindcss -i ./static/src/input.css -o ./static/src/output.css --watch (This command will watch for html changes to know what css styles to bring in)
- Populate the database
    - run the import_mobile_games.py
    - perform migrations
- python manage.py runserver