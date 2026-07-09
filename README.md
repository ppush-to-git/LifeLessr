# LifeLessr

LifeLessr is a GeoGuessr-inspired web application where players identify the real-world locations behind fictional media.

Instead of guessing locations from Street View, players are presented with content from games, music, anime, movies, or TV series and must locate the real-world city, region, or country associated with that media.

The long-term vision is to build a unified gameplay engine that supports multiple media categories while rewarding both geographical intuition and media knowledge.

---

## Preview

*Screenshots coming soon.*

---

## Current Status

LifeLessr is currently in the playable prototype stage.

The current prototype includes:

- Interactive map-based gameplay
- Random screenshot selection
- Metadata-driven dataset
- Session-based game state
- Multi-round gameplay
- Distance-based scoring
- End game screen
- Replay functionality

---

## Roadmap

### Core Engine

- [x] Flask project setup
- [x] Random media selection
- [x] Session management
- [x] Multi-round game loop
- [x] Score system
- [x] UI improvements
- [x] Interactive map (Leaflet.js)
- [x] Distance-based scoring
- [ ] PostgreSQL integration

### Planned Features

- [ ] User authentication
- [ ] User profiles
- [ ] Statistics dashboard
- [ ] Leaderboards
- [ ] Daily challenges
- [ ] Community submissions
- [ ] Admin dashboard

### Planned Categories

- [x] Games
- [ ] Music
- [ ] Anime
- [ ] Movies
- [ ] TV Series

---

## Tech Stack

### Current

- Python
- Flask
- SQLite
- HTML
- CSS
- JavaScript
- Leaflet.js
- Geoapify Geocoding API

### Planned

- PostgreSQL
- Docker
- Cloud Storage

---

## Setup

1. Clone the repository.

2. Create a `.env` file in the project root by copying `.env.example`.

3. Replace the placeholder values:

   - `SECRET_KEY` – Any random secret string for Flask sessions.
   - `GEOAPIFY_API_KEY` – Your Geoapify API key.

4. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Start the application:

   ```bash
   python app.py
   ```

6. Open your browser:

   ```
   http://127.0.0.1:5000
   ```

> **Note:** The Geoapify API key is only required for the dataset utility scripts (such as coordinate generation). The game itself reads from the pre-generated SQLite database included in the repository.

---

## Future Vision

LifeLessr is intended to become a platform where players explore the real-world inspirations behind fictional media.

Planned categories include:

- Games → Real-world city inspirations
- Music → Artist or band origins
- Anime → Real-world locations
- Movies → Filming locations
- TV Series → Story settings and filming locations

Every category will share the same gameplay engine while using category-specific datasets and scoring.

---

## Contributing

Contributions, suggestions, and feedback are always welcome.

If you'd like to improve the project or add support for new media, feel free to open an issue or submit a pull request.

---

## Project Status

LifeLessr is a personal learning project and portfolio piece. The architecture, gameplay, and feature set will continue to evolve as new categories, features, and gameplay improvements are added.