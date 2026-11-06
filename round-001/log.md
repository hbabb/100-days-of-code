# 100 Days Of Code - Log

## Day 1 — November 5, 2026

**Focus:** Python (work tools)

### **Progress:**

- Designed `pile_report.py`, a tkinter tool that converts EOR pile/pole files (`.csv`, `.xls`, `.xlsx`) into our standard PNEZD CSV for QGIS QA/QC and machine control.
- The GE picks which columns build the Pile ID and which hold Northing, Easting, Top_Elev, and Color/Profile, so one tool handles every EOR layout with no code changes.
- Pile ID columns are joined with `_`, and every `.` is replaced with `_`. Values pass through at their original precision.
- Added a startup check that stops and shows the `pip` install command if `openpyxl` or `xlrd` is missing.
- Set up the private `geomatics-toolkits` repo with a README for the pile report tool and the project structure builder.

### **Lessons:**

- Working through the problem with AI helped. It caught edge cases I hadn't thought of, like the encoding difference between a standard CSV and one saved by Excel on Windows.
- This was my second time using tkinter. It's cool, but so far it's been more of a pain to work with than web development.
- Building a simple program that does advanced spreadsheet processing was easier than I expected. I'm excited to see what else I can learn and build in my new career.
- I'm starting to enjoy building desktop apps. I can see myself doing native builds in the future, especially in Go, and maybe Rust. Who knows where this goes.

**Code:** Private work repo (`geomatics-toolkits`)
