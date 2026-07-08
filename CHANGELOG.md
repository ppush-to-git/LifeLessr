## [v0.2.0] - Migrated from list-based data fetching to SQLite

### Added
- Metadata-based dataset structure
- Dataset importer
- Image serving route for dataset assets
- Added database helper functions

### Changed
- Replaced filesystem image pool with SQLite queries
- Reduced session storage to image IDs
- Standardized image paths for cross-platform compatibility
- Refactored gameplay to fetch images from the database
