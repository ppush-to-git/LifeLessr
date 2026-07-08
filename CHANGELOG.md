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