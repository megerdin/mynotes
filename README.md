# ReaderEditor GitHub

**Version: V9.4.18**

A lightweight, single-file browser-based Reader/Editor for HTML, source code, configuration files, and plain-text documents.

ReaderEditor is designed for reading, editing, navigating, and managing text-based documents directly in a modern web browser, with particular attention to large documents, mobile use, pagination, and responsive editing.

## Overview

ReaderEditor combines:

- HTML Reader mode
- HTML Raw/Source mode
- Source-code reading and editing
- Syntax highlighting
- Plain-text / TXT editing
- Paginated document viewing
- Current-page navigation
- Current-page editing
- GitHub repository browsing
- GitHub file opening
- GitHub Save
- GitHub Save As
- Local file opening
- New document creation
- Session persistence
- CLI code-block conversion
- Reader/editor mode switching

The application is distributed as a **single self-contained HTML file**.

No build system is required.

## Current Version

```text
ReaderEditor GitHub V9.4.18
```

The application version is defined internally by:

```javascript
const APP_VERSION='9.4.18';
```

The version is displayed automatically in the application interface.

## Document & Source-Code Support

ReaderEditor is not limited to HTML.

It can be used as a browser-based reader/editor for many types of **source code, configuration files, markup, and plain text**.

Typical examples include:

- JavaScript
- HTML
- CSS
- JSON
- XML
- Bash / Shell
- Python
- SQL
- YAML
- Markdown
- Plain text
- Other text-based source and configuration files

The exact highlighting behaviour depends on the language/highlighting support available in the current application implementation.

## Syntax Highlighting

ReaderEditor provides syntax highlighting to make source code easier to read and understand.

The highlighting system is integrated with the application's paginated Reader architecture rather than unnecessarily processing the complete document on every page navigation.

This is particularly important for large source files, where repeatedly highlighting the entire document can increase CPU and memory usage.

The current approach is designed to:

- Highlight source content for reading
- Work with the application's paginated Reader
- Avoid unnecessary whole-document processing during normal page navigation
- Keep large source files practical to use
- Return to editable source content when entering edit mode
- Restore highlighting when leaving edit mode
- Preserve the existing pagination and editing architecture

The application therefore works as both a **source-code reader** and a **source-code editor**, rather than being limited to HTML document editing.

## HTML Reader Mode

HTML documents can be opened and displayed using the Reader interface.

The Reader uses browser-native HTML rendering while maintaining the application's pagination and navigation system.

Supported HTML content can include:

- Headings
- Paragraphs
- Lists
- Tables
- Code blocks
- Images
- Diagrams
- Other normal HTML content

Imported HTML is cleaned before being placed into the Reader content area. Unwanted executable or embedded elements such as scripts and external import elements are removed.

## HTML Raw / Source Mode

HTML documents can also be viewed and edited as source text.

This allows the underlying HTML document to be edited directly rather than only through the rendered Reader view.

## Plain-Text / TXT Support

Plain-text files can be opened and edited without converting them into HTML.

The application maintains a dedicated plain-text editing path so that large text and source-code documents remain efficient.

## Pagination

ReaderEditor uses a horizontal paginated reading model.

The application keeps track of:

- Current page
- Total page count
- Page width
- Page position
- Page navigation

The pagination engine caches page metrics and page-count calculations where possible, avoiding unnecessary recalculation during normal navigation.

## Current-Page Editing

When editing a paginated document, ReaderEditor works with the current page rather than unnecessarily creating a second complete copy of the document.

This is important for large documents because duplicating the entire DOM can significantly increase memory usage and reduce performance.

The current-page editing system temporarily creates an editing host around the relevant page content and restores the original document structure when editing ends.

For source-code and plain-text documents, dedicated editing paths are used where appropriate.

## Editing Workflow

ReaderEditor separates the reading/highlighting experience from the editing experience.

A typical source-code workflow is:

```text
Open source file
      ↓
Reader / syntax-highlighted view
      ↓
Navigate through pages
      ↓
Enter Edit mode
      ↓
Edit source content
      ↓
Exit Edit mode
      ↓
Reader / syntax-highlighted view
```

This allows code to remain visually readable during normal use while keeping the underlying source content editable.

## Editing Tools

The editor provides several editing utilities.

### CLI+

The **CLI+** button converts selected text into a CLI/code block.

Keyboard shortcut:

```text
Ctrl + Alt + C
```

The toolbar button and keyboard shortcut use the same conversion path.

### CLI-

The **CLI-** button converts selected CLI/code blocks back into normal text.

Keyboard shortcut:

```text
Ctrl + Alt + N
```

The toolbar button and keyboard shortcut use the same underlying conversion function.

## GitHub Integration

ReaderEditor can work directly with GitHub repositories.

Available operations include:

- Test GitHub connection
- Browse repository files
- Open an existing GitHub file
- Save changes back to GitHub
- Save a document as a new GitHub file

A GitHub token is required for operations that need repository write access.

Public files may be opened without a token where GitHub permits read-only access.

## Local Files

Local documents can be opened directly from the browser.

The application supports:

- HTML files
- Source-code files
- Configuration files
- Plain-text files

A new document can also be created directly inside ReaderEditor.

## Session Persistence

ReaderEditor maintains the active working session locally so that the application can restore the current document/session state after a browser reload.

The session system is designed to work with both GitHub and local documents.

## Performance

Performance is a core part of the ReaderEditor architecture.

The application avoids unnecessarily duplicating the complete document DOM when entering current-page editing.

The Reader pagination engine also caches page metrics and page-count calculations where possible.

The plain-text and source-code editing paths have dedicated handling so that large text/code documents remain practical to work with.

### V9.4.16 Performance Baseline

V9.4.16 established the current stable performance architecture.

A major performance improvement came from ensuring imported HTML content is placed directly into the Reader's expected content structure instead of introducing an unnecessary large wrapper around the document.

This avoided unnecessary DOM nesting and restored current-page editing performance to the established V70-level behaviour.

V9.4.18 retains that performance architecture.

## Architecture

ReaderEditor is intentionally distributed as a single HTML file.

```text
ReaderEditor_GitHub_v9.4.18.html
│
├── HTML
├── CSS
└── JavaScript
    ├── Reader
    ├── Pagination
    ├── Syntax highlighting
    ├── Source-code handling
    ├── Editing
    ├── GitHub integration
    ├── Local file handling
    ├── Session persistence
    └── Document conversion
```

There is no required:

- Node.js build process
- npm installation
- JavaScript bundler
- Framework
- Database

The application can be hosted as a static HTML application.

## Browser Compatibility

ReaderEditor is intended for modern browsers supporting standard browser APIs including:

- DOMParser
- File API
- Clipboard/browser editing APIs
- IndexedDB
- Fetch API
- Contenteditable
- Modern CSS multi-column layout

Recommended browsers include current versions of:

- Chrome
- Chromium
- Edge
- Safari
- Firefox

## GitHub Pages

Because ReaderEditor is a static HTML application, it can be hosted using GitHub Pages.

A typical repository can contain:

```text
repository/
└── index.html
```

The ReaderEditor HTML file can therefore be used directly as the repository's `index.html`.

## Running Locally

Download or clone the repository and open the HTML file in a modern browser.

No installation is required.

For example:

```text
ReaderEditor_GitHub_v9.4.18.html
```

can be opened directly in the browser.

## Security Notes

GitHub authentication is performed from the browser using the GitHub API.

Do not commit a personal GitHub access token into this repository or hard-code a token into the HTML source.

For public repositories, a token may not be necessary for read-only operations.

For write operations, use an appropriate GitHub token with the minimum permissions required.

## Version History

### V9.4.18

Current release.

Changes:

- Corrected the application version flag to `9.4.18`
- CLI button renamed to **CLI+**
- Added **CLI-** button
- CLI+ retains `Ctrl + Alt + C`
- CLI- retains `Ctrl + Alt + N`
- CLI- button uses the same conversion function as the keyboard shortcut
- Source-code syntax highlighting retained
- Highlighting is integrated with the paginated Reader workflow
- Existing Reader/editor performance architecture preserved
- Existing pagination preserved
- Existing GitHub functionality preserved
- Existing local-file functionality preserved
- Existing session persistence preserved

### V9.4.17

Introduced the CLI+ / CLI- toolbar terminology and functionality.

### V9.4.16

Established the current performance baseline by correcting the HTML import/content structure used by the Reader.

This prevented unnecessary DOM nesting and restored current-page editing performance to the established V70-level behaviour.

## Development Principles

ReaderEditor is deliberately kept as a compact, self-contained browser application.

When modifying the application:

1. Preserve existing functionality.
2. Make the smallest necessary change.
3. Keep the pagination engine stable.
4. Avoid unnecessary DOM duplication.
5. Preserve GitHub and local-file behaviour.
6. Increment the application version for every released change.
7. Test both mouse and keyboard paths when editing controls provide both.
8. Keep previously stable versions available for rollback.
9. Test source-code highlighting with realistic document sizes.
10. Avoid whole-document processing when a page-local operation is sufficient.

## Current Release

```text
ReaderEditor GitHub V9.4.18
```

File:

```text
ReaderEditor_GitHub_v9.4.18.html
```

This version is the current working release.
