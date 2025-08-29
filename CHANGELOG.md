# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog],
and this project adheres to [Semantic Versioning].

## [Unreleased]

- /

## [0.1.1] - 2025-08-29

### Added

- 'Post processing' mechanism, which is a temporary feature that fixes a lot of parsing issues. Will be repurposed in newer versions

### Changed

- Example `.htm` file lies in `example/` folder
- Content within `<script>` and `<style>` tags is removed during parsing
- `<figcaption>` tags are now parsed and replaced with `> `

### Fixed

- Incorrect parsing of tag attributes
- `<img>`, `<sup>` and `<sub>` tags being skipped

## [0.1.0] - 2025-08-29

### Added

- More html tags to be recognized and removed during parsing

## [0.0.1] - 2025-08-29

- initial release

<!-- Links -->
[keep a changelog]: https://keepachangelog.com/en/1.0.0/
[semantic versioning]: https://semver.org/spec/v2.0.0.html

<!-- Versions -->
[unreleased]: https://github.com/vladcheck/ <!-- FIXME: Normal link -->
[0.1.1]: https://github.com/vladcheck/ <!-- FIXME: Normal link -->
[0.1.0]: https://github.com/vladcheck/ <!-- FIXME: Normal link -->
[0.0.1]: https://github.com/vladcheck/ <!-- FIXME: Normal link -->
