## [v0.3.1] - Bugfix/Project polish

### Added
- `.env.example` for easier project setup
- `requirements.txt`

### Changed
- Switched to a cleaner map tile provider
- Improved README with setup instructions and project overview

### Fixed
- Fixed image renaming script to prevent filename conflicts
- Fixed a bug that made the polyline go around the whole map instead of taking the shortest path

## [v0.3.0] - Implemented playable map-guessing gameplay

### Added
- Leaflet-based interactive map gameplay
- Distance calculation using the Haversine formula
- Distance-based scoring system
- Round result screen with answer visualization
- Game helper modules (distance and scoring)

### Changed
- Replaced text-based guessing with map-based location selection
- Refactored gameplay flow to support map guessing and result screens
- Improved game progression across multiple rounds
- Updated project structure for better maintainability

## [v0.2.0] - Migrated from list-based data fetching to SQLite

### Added
- Metadata-based dataset structure
- Dataset importer
- Image serving route for dataset assets
- Database helper functions
- Environment variable support for secrets and API keys

### Changed
- Replaced filesystem image pool with SQLite queries
- Reduced session storage to image IDs
- Standardized image paths for cross-platform compatibility
- Refactored gameplay to fetch images from the database