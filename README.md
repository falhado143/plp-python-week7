# Week 7 Assignment: Shopping List Manager

## Project Description

This project is a Python Shopping List Manager. It demonstrates how to create lists, add and remove items, check whether items exist, and generate a shopping list report.

## Files

- `list_warmup.py` — Practices basic list operations, indexing, adding items, removing items, and checking membership.
- `shopping_list.py` — Allows users to add, remove, and view shopping list items using a menu.
- `list_report.py` — Displays the shopping list, counts the items, and generates a simple report.
- `screenshots/` — Contains screenshots showing each program running.

## Why is it safer to check `in` before calling `.remove()`?

Checking `in` before calling `.remove()` helps prevent errors. If an item does not exist in a list, `.remove()` raises a `ValueError`. Checking first allows the program to display a helpful message instead of stopping unexpectedly.

## Author

PLP Student
