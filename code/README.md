# Code samples

Runnable text versions of code that appears in the PDF notes, so you can copy, run and edit it instead of retyping from screenshots.

| Folder | Source | How it was extracted | Files | Status |
|---|---|---|---|---|
| `html/` | `html5-book.pdf` | Real code text read straight from the PDF | 16 | Reliable |
| `css/` | `css-book.pdf` | Real text; rules detected by pattern, braces balanced | 35 | Reliable, but a few snippets may be partial |
| `python/` | `python-book.pdf` | **OCR of VS Code screenshots**, then syntax-checked with `py_compile` | 21 pass, 6 in `_needs-review/` | Passing = valid syntax, not guaranteed identical |
| `javascript/` | `javascript-book.pdf` | **OCR of VS Code screenshots**, then syntax-checked with `node --check` | 10 pass, 6 in `_needs-review/` | Same caveat |

## Read this before trusting the OCR'd files

- The Python and JavaScript books show their code as **screenshots**, so these files were produced by optical character recognition. A file that passes a syntax check can still contain wrong **comments, variable names or string text** (for example `Lastname` for `lastname`).
- Files marked **Auto-repaired** had a small mechanical fix applied (restoring underscores, or replacing an unreadable first comment line) and are labelled in their header.
- Files in `_needs-review/` failed the syntax check. Compare them with the screenshot on the page named in the file header and fix by hand.
- **Not extracted:** SQL, Kotlin, React and Bootstrap code (screenshots in different editors, or mostly prose), so those still live only in the PDFs.
- The best long-term fix is for the author to commit the original lesson files (`Lesson1a.py`, `Lesson2c.py`, …) from the course folder, which would replace all OCR output.
