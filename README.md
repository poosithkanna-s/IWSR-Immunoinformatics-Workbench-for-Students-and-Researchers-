# IWSR-Immunoinformatics-Workbench-for-Students-and-Researchers-
Immunoinformatics web platform built with Flask: analyze protein antigen sequences, estimate antigen-receptor compatibility, and save your analyses in a personal account. Educational/research use only, not a medical tool.
# 🧬 Immunology Workbench (BIA0403)

A full-stack web application for exploring immunoinformatics. Registered
users can analyze protein sequences, compare antigen-receptor pairs, and
keep a history of their saved analyses.

## What it will include
- **Antigen analysis:** sequence composition, hydrophobicity, and candidate
  antigenic regions
- **Interaction estimates:** sequence-based antigen-receptor compatibility
- **User accounts:** secure registration and login, with per-user saved
  analyses
- **Persistent storage:** SQLAlchemy database (SQLite in development,
  PostgreSQL in production)
- **Teaching simulations:** clearly labelled, fictional immunological
  cases for learning

## Tech stack
Python · Flask · Flask-SQLAlchemy · Flask-Login · HTML/CSS

## Status
Active development. Currently a course project (BIA0403) being grown
into a deployed, login-enabled website. The scoring methods are
educational heuristics and are being replaced step by step with published,
benchmarked methods.

## Disclaimer
For educational and research purposes only. Not a medical device and not
a source of diagnosis or medical advice. Please do not enter real patient
data.

## Author
Poosith Kanna S · B.Tech Computer Science and Biosciences, SIMATS