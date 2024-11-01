# iTubeKENYA - Music Distribution System

1.Welcome to **iTubeKENYA**, a Command Line Interface (CLI) application designed to manage music distribution in the Kenyan music industry. This application allows users to add artists, genres, producers, and songs, and to list them efficiently using a structured database.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
  - [Commands](#commands)
- [Database Structure](#database-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features
- **Add Artists**: Register new artists along with their details.
- **Manage Genres**: Create and manage different music genres.
- **List Artists**: View all registered artists with their details.
- **Add Songs**: Add songs associated with artists and genres.
- **List Songs**: Retrieve and display songs filtered by genre.
- **Integrated Database**: Utilizes SQLAlchemy ORM for seamless database interaction.

## Technologies Used
- **Python**: Programming language used to build the application.
- **Click**: For creating the command-line interface.
- **SQLAlchemy**: ORM library for database management.
- **SQLite**: Lightweight database engine for storage.
- **Pipenv**: For managing dependencies and virtual environments.

## Installation

### Prerequisites
- Python 3.6 or later
- Pip (Python package manager)
- Pipenv (to manage virtual environments)

### Steps to Install
1. Clone the repository:
   ```bash
   git clone https://github.com/Justonm/iTubeKENYA.git
   cd iTubeKENYA

2.Install Pipenv if you haven't already: 
        pip install pipenv
3.Create a virtual environment and install the dependencies:
        pipenv install
4.Activate the virtual environment:
        pipenv shell
5.Initialize the database:
        python cli.py init
Usage
Commands
To see a list of available commands, run:
        python cli.py --help
Initialize the Database
        python cli.py init
Initializes the SQLite database for the application.
        python cli.py add-new-artist <name> <stage_name> <genre> <location>
Adds a new artist to the database.
        Example: python cli.py add-new-artist "Nyashinski" "Shinski" "Afrobeat" "Nairobi"
List All Artists
        python cli.py list-all-artists
List All Artists
        python cli.py list-all-artists
Displays all artists along with their genres and locations.
Add New Song
        python cli.py add-new-song <title> <release_date> <artist_id> <producer_id> <genre_name>
Adds a new song associated with an artist and genre.
Example:
        python cli.py add-new-song "Breeze" "2024-01-01" 1 1 "Afrobeat"
Where 1 represents the ID of the artist and producer.
List Songs by Genre
        python cli.py list-songs <genre>
Lists all songs under the specified genre.
        python cli.py list-songs "Afrobeat"
    Example:
        python cli.py list-songs "Afrobeat"
Database Structure
The application uses a SQLite database with the following tables:

Artists

id: Integer (Primary Key)
name: String
stage_name: String
bio: Text
location: String
genre_id: Integer (Foreign Key referencing Genres)
Genres

id: Integer (Primary Key)
name: String
Producers

id: Integer (Primary Key)
name: String
location: String
Music

id: Integer (Primary Key)
title: String
release_date: Date
artist_id: Integer (Foreign Key referencing Artists)
producer_id: Integer (Foreign Key referencing Producers)
genre_id: Integer (Foreign Key referencing Genres)
Contributing
Contributions are welcome! If you have suggestions for improvements or would like to add features, feel free to create a pull request.

Fork the repository.
Create your feature branch (git checkout -b feature/AmazingFeature).
Commit your changes (git commit -m 'Add some AmazingFeature').
Push to the branch (git push origin feature/AmazingFeature).
Open a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for more details.

Contact
For any inquiries, you can reach out to:

Justus - justusmutuku.student@moringaschool.com
GitHub - [Justonm](https://github.com/Justonm)
Thank you for checking out iTubeKENYA! We hope you find it useful in managing the Kenyan music distribution landscape.    


 

