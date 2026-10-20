# Dev Course Notes

A collection of beginner-friendly PDF study notes covering web development, programming, databases, data/AI, Linux and introductory cybersecurity.

> This is a restructured version of the original `Programming-Languages` repository: same notes, clearer layout, plus runnable code samples. See [MIGRATION.md](MIGRATION.md) for where every file moved.

**40 PDFs · 486 pages**

## Suggested learning path

```
Web track       HTML → CSS → Bootstrap → JavaScript → React
Backend / data  Python → SQL & databases → Data, AI & ML
Systems         Linux → Cybersecurity (read the safety note below first)
Mobile          Kotlin & Android (independent; some Python or JavaScript helps)
```

If you are brand new, start with `1-web/01-html`, then `1-web/02-css`, and do `2-programming/01-python` in parallel.

## What's inside

### 1. Web development

| Path | Topic | Pages |
|---|---|---|
| `01-html/html5-book.pdf` | HTML5 (Book 1) | 45 |
| `02-css/css-book.pdf` | CSS (Book 2) | 44 |
| `03-bootstrap/01-introduction.pdf` | Introduction | 2 |
| `03-bootstrap/02-get-started.pdf` | Get started | 2 |
| `03-bootstrap/03-containers.pdf` | Containers | 1 |
| `03-bootstrap/04-grid-system.pdf` | Grid system | 5 |
| `03-bootstrap/05-buttons.pdf` | Buttons | 3 |
| `03-bootstrap/06-images.pdf` | Images | 1 |
| `03-bootstrap/07-badges.pdf` | Badges | 1 |
| `03-bootstrap/08-cards.pdf` | Cards | 2 |
| `03-bootstrap/09-navbar.pdf` | Navbar | 7 |
| `03-bootstrap/10-carousel.pdf` | Carousel | 4 |
| `04-javascript/javascript-book.pdf` | JavaScript (Book 5) | 46 |
| `05-react/01-app-file-structure.pdf` | App file structure | 3 |
| `05-react/02-app-js-component.pdf` | App.js component | 5 |
| `05-react/03-snippets-cheatsheet.pdf` | Snippets cheatsheet | 3 |
| `05-react/04-components.pdf` | Components | 4 |
| `05-react/05-variables.pdf` | Variables | 3 |
| `05-react/06-hooks.pdf` | Hooks | 5 |
| `05-react/07-router.pdf` | Router | 8 |

### 2. Programming

| Path | Topic | Pages |
|---|---|---|
| `01-python/python-book.pdf` | Python (Book 3) | 62 |
| `02-kotlin-android/01-android-introduction.pdf` | Android introduction | 2 |
| `02-kotlin-android/02-hello-world.pdf` | Hello World app | 3 |
| `02-kotlin-android/03-app-structure.pdf` | App structure | 8 |
| `02-kotlin-android/04-view-groups-and-views.pdf` | View groups and views | 6 |
| `02-kotlin-android/kotlin-book.pdf` | Kotlin (Book 6) | 53 |

### 3. Data and databases

| Path | Topic | Pages |
|---|---|---|
| `01-sql-databases/sql-book.pdf` | SQL (Book 4) | 46 |
| `01-sql-databases/ten-uses-of-a-database.pdf` | 10 uses of a database | 12 |
| `01-sql-databases/sql-injection-sqlmap-online.pdf` | SQL injection with SQLMap (online lab) | 7 |
| `01-sql-databases/sql-injection-sqlmap-local.pdf` | SQL injection with SQLMap (local lab) | 7 |
| `02-data-ai-ml/01-intro-data-science.pdf` | Intro to data science | 6 |
| `02-data-ai-ml/02-intro-ai.pdf` | Intro to AI | 3 |
| `02-data-ai-ml/03-pandas-seaborn.pdf` | Pandas and Seaborn | 2 |
| `02-data-ai-ml/04-regex.pdf` | Regular expressions | 3 |
| `02-data-ai-ml/05-robotics.pdf` | Robotics | 4 |
| `02-data-ai-ml/06-machine-learning.pdf` | Machine learning | 5 |
| `02-data-ai-ml/07-ml-models.pdf` | ML models | 2 |

### 4. Systems and security

| Path | Topic | Pages |
|---|---|---|
| `01-linux/linux-basics.pdf` | Linux basics | 48 |
| `02-cybersecurity/01-ethical-hacking-intro.pdf` | Ethical hacking introduction | 9 |
| `02-cybersecurity/02-extract-images-binwalk.pdf` | Extracting hidden data from images (binwalk) | 4 |

### Code samples

Runnable `.html`, `.css`, `.py` and `.js` files extracted from the notes live in [`code/`](code/README.md). Read that README first: the Python and JavaScript files come from OCR and are labelled by how much you can trust them.

## Safety note for the security material

The SQL injection and binwalk notes are for **learning on systems you own or have written permission to test**. Practise on your own machine or deliberately vulnerable labs (for example DVWA). Running these tools against anyone else's system can be illegal.

## Credits and licence

**Licence: not yet chosen.** Until the repository owner adds a `LICENSE` file, all rights are reserved by default, so please ask before reposting or reusing the notes.

Several PDFs carry **MODCOM Institute of Technology** branding, which suggests they come from that institute's course. See [NOTICE.md](NOTICE.md) for details and the attribution still to be confirmed.

## Contributing

Corrections are welcome: fix a typo, replace an OCR'd code file with the original, or add a missing lesson. Please keep the numbering convention (`01-`, `02-`, …) and add new PDFs to the table above.
