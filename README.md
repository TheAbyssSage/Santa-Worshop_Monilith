# 🎅 Santa's Legacy Shop (Monolith)

Ho Ho Ho! Welcome to the legacy codebase of the North Pole. 
This project is a monolithic Python script that renders the shop interface. 
Your mission, should you choose to accept it, is to refactor this into a modern **Vite + TypeScript** application!

## 🛠️ Setup Instructions

### 1. Start the Fake API
We need the product data to be available. We use `json-server` for this.

```bash
npx json-server db.json --port 3000
```
*Keep this terminal running!*

### 2. Install Dependencies
We are using **Flask** to run the legacy shop. Install it first:

```bash
pip3 install flask
```

### 3. Run the Legacy Python App
Open a new terminal window and run the Python script:

```bash
python3 legacy_santa_shop.py
```

This will start a web server at `http://localhost:8000` and should automatically open your browser.



## 🏗️ How the Legacy App Works

This script is a **Monolith**, meaning the logic, data fetching, and UI rendering are all mixed together in one file.

### 1. The Architecture
*   **The Server:** Uses **Flask** to create a web server on port `8000`.
*   **The Data:** Uses `urllib` to fetch raw JSON data from `json-server` (port `3000`).
*   **The View:** The HTML is generated as a giant string inside Python (Server-Side Rendering).

### 2. The Logic Pipeline
When you visit the page, the app follows this pipeline:
1.  **Fetch**: Gets all products from the API.
2.  **Search**: Filters the list based on the `?q=` query parameter.
3.  **Filter**: Further filters based on the `?category=` parameter.
4.  **Render**: Loops through the remaining products, assigns a random "Naughty/Nice" rating, and generates the HTML.

### 3. Why Refactor?
*   **No Separation of Concerns:** The HTML (View) is hardcoded inside the Python logic.
*   **Full Page Reloads:** Every search or filter forces the browser to reload the entire page.
*   **Modern Goal:** Move the **Logic** to TypeScript and the **View** to TS components for a snappy experience!

## 🎯 Refactoring Goals

The current application is a "Monolith" - the backend logic and frontend rendering are mixed together in one file.
Your goal is to separate them:

1.  **Frontend**: Create a Vite (with TypeScript) app.
2.  **API**: Continue using the `json-server` as your backend.
3.  **Features to Port**:
    *   Fetching data from the API.
    *   Rendering the product grid.
    *   Search functionality.
    *   Category filtering.
    *   *Bonus*: Keep the "Naughty or Nice" randomizer!

Good luck, and may the code be with you! 🎄 Now go and develop some Luke SkyScraper skillzzz!!!
