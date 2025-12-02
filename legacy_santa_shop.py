from flask import Flask, request
import urllib.request
import json
import webbrowser
import random
import threading
import time

# 🎅 HO HO HO! WELCOME TO THE LEGACY SANTA SHOP MONOLITH (FLASK EDITION)! 🎅
# This script is powered by Christmas Spirit and the Flask Framework.
# It's much cleaner now, but still a monolith! 🌟
 
app = Flask(__name__)
PORT = 8000
API_URL = "http://localhost:3000/products"

def fetch_products():
    """
    Fetches the list of magical products from the North Pole API.
    (aka json-server running on localhost:3000)
    
    Returns:
        list: A list of dictionaries containing product details.
    """
    try:
        # 🦌 Dasher! Dancer! Prancer! Fetch that data!
        with urllib.request.urlopen(API_URL) as response:
            data = response.read()
            return json.loads(data)
    except Exception as e:
        print(f"❌ Oh no! The elves dropped the database: {e}")
        return []

# ==========================================
# 🎄 SECTION 1: SEARCH LOGIC 🎄
# ==========================================
def search_products(products, query):
    """
    Searches for products that match the query string.
    It's like looking for a needle in a haystack, but the haystack is snow
    and the needle is a present! 🎁
    
    Args:
        products (list): The list of products to search through.
        query (str): The search term (e.g., "sleigh").
        
    Returns:
        list: A list of products that match the name or description.
    """
    if not query:
        return products
    
    print(f"🔍 Elf Scout searching for: {query}")
    filtered = []
    for p in products:
        # Case-insensitive search because Santa doesn't care about capitalization
        if query.lower() in p['name'].lower() or query.lower() in p['description'].lower():
            filtered.append(p)
            
    return filtered

# ==========================================
# ❄️ SECTION 2: CATEGORY FILTER LOGIC ❄️
# ==========================================
def filter_products_by_category(products, category):
    """
    Filters products by their category.
    Sorting the toys into the right sacks! 🎒
    
    Args:
        products (list): The list of products.
        category (str): The category to filter by (e.g., "tech", "food").
        
    Returns:
        list: A list of products in that category.
    """
    if not category or category == "all":
        return products
        
    print(f"📂 Elf Sorter filtering by category: {category}")
    filtered = []
    for p in products:
        if p['category'].lower() == category.lower():
            filtered.append(p)
            
    return filtered

# ==========================================
# 🎨 SECTION 3: RENDER ITEMS ON SCREEN 🎨
# ==========================================
def render_page(products, search_query="", current_category="all"):
    """
    Generates the HTML for the shop page.
    This is where the magic happens! We mix HTML, CSS, and Python 
    into a delicious holiday fruitcake of code. 🍰
    
    Args:
        products (list): The products to display.
        search_query (str): The current search term to keep in the input box.
        current_category (str): The current selected category.
        
    Returns:
        str: The full HTML string.
    """
    
    # 🎶 Jingle bells, HTML smells... 🎶
    
    # Generate product cards HTML
    cards_html = ""
    if not products:
        cards_html = "<div class='no-results'>❄️ Brrr... No products found here! Just snow. ❄️</div>"
    else:
        for p in products:
            # SURPRISE! Random "Naughty or Nice" rating for each product
            naughty_or_nice = random.choice(["😇 Nice", "😈 Naughty", "🌟 Super Nice"])
            
            cards_html += """
            <div class="card">
                <div class="card-header">
                    <span class="category-tag">""" + str(p['category']) + """</span>
                    <span class="stock-tag">📦 """ + str(p['stock']) + """ left</span>
                </div>
                <h2>""" + str(p['name']) + """</h2>
                <p class="description">""" + str(p['description']) + """</p>
                <div class="price-row">
                    <span class="price">$""" + str(p['price']) + """</span>
                    <span class="rating">""" + str(naughty_or_nice) + """</span>
                </div>
                <button class="buy-btn">Add to Sleigh 🛷</button>
            </div>
            """

    # The Monolithic HTML Template
    # (Students: This is what we call "Server Side Rendering" in the old days!)
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>🎅 Santa's Legacy Shop</title>
        <style>
            /* 🎨 CSS MAGIC STARTS HERE */
            body {
                font-family: 'Comic Sans MS', 'Chalkboard SE', sans-serif; /* Classic dev humor font */
                background-color: #f0f8ff;
                color: #2c3e50;
                margin: 0;
                padding: 20px;
                background-image: url('https://www.transparenttextures.com/patterns/snow.png');
            }
            
            h1 {
                text-align: center;
                color: #c0392b;
                text-shadow: 2px 2px #fff;
                font-size: 3em;
                margin-bottom: 10px;
            }
            
            .subtitle {
                text-align: center;
                color: #27ae60;
                margin-bottom: 40px;
                font-style: italic;
            }

            /* Controls Section */
            .controls {
                background: white;
                padding: 20px;
                border-radius: 15px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.1);
                max-width: 800px;
                margin: 0 auto 40px auto;
                display: flex;
                gap: 10px;
                flex-wrap: wrap;
                justify-content: center;
                border: 2px solid #c0392b;
            }
            
            input[type="text"], select {
                padding: 10px;
                border: 2px solid #bdc3c7;
                border-radius: 5px;
                font-size: 16px;
            }
            
            button.search-btn {
                background-color: #27ae60;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 5px;
                cursor: pointer;
                font-size: 16px;
                transition: transform 0.2s;
            }
            
            button.search-btn:hover {
                transform: scale(1.05);
                background-color: #2ecc71;
            }

            /* Grid Layout */
            .grid {
                display: grid;
                grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
                gap: 30px;
                max-width: 1200px;
                margin: 0 auto;
            }
            
            /* Product Card */
            .card {
                background: white;
                border-radius: 15px;
                padding: 20px;
                box-shadow: 0 10px 20px rgba(0,0,0,0.05);
                transition: transform 0.3s ease;
                border-bottom: 5px solid #c0392b;
                position: relative;
                overflow: hidden;
            }
            
            .card:hover {
                transform: translateY(-10px);
            }
            
            .card-header {
                display: flex;
                justify-content: space-between;
                margin-bottom: 15px;
            }
            
            .category-tag {
                background: #e74c3c;
                color: white;
                padding: 5px 10px;
                border-radius: 20px;
                font-size: 0.8em;
                text-transform: uppercase;
                font-weight: bold;
            }
            
            .stock-tag {
                color: #7f8c8d;
                font-size: 0.9em;
            }
            
            h2 {
                margin: 0 0 10px 0;
                color: #2c3e50;
            }
            
            .description {
                color: #7f8c8d;
                line-height: 1.5;
                height: 60px; /* Fixed height for alignment */
            }
            
            .price-row {
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-top: 20px;
            }
            
            .price {
                font-size: 1.5em;
                color: #27ae60;
                font-weight: bold;
            }
            
            .buy-btn {
                width: 100%;
                margin-top: 15px;
                padding: 10px;
                background: #c0392b;
                color: white;
                border: none;
                border-radius: 8px;
                cursor: pointer;
                font-size: 1.1em;
            }
            
            .buy-btn:hover {
                background: #e74c3c;
            }

            .no-results {
                text-align: center;
                font-size: 2em;
                color: #95a5a6;
                grid-column: 1 / -1;
                padding: 50px;
            }

            /* ❄️ SURPRISE: CSS SNOWFALL ANIMATION ❄️ */
            .snowflake {
                color: #fff;
                font-size: 1em;
                font-family: Arial;
                text-shadow: 0 0 1px #000;
            }
            
            @-webkit-keyframes snowflakes-fall{0%{top:-10%}100%{top:100%}}@-webkit-keyframes snowflakes-shake{0%{-webkit-transform:translateX(0px);transform:translateX(0px)}50%{-webkit-transform:translateX(80px);transform:translateX(80px)}100%{-webkit-transform:translateX(0px);transform:translateX(0px)}}@keyframes snowflakes-fall{0%{top:-10%}100%{top:100%}}@keyframes snowflakes-shake{0%{transform:translateX(0px)}50%{transform:translateX(80px)}100%{transform:translateX(0px)}}.snowflake{position:fixed;top:-10%;z-index:9999;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;cursor:default;-webkit-animation-name:snowflakes-fall,snowflakes-shake;-webkit-animation-duration:10s,3s;-webkit-animation-timing-function:linear,ease-in-out;-webkit-animation-iteration-count:infinite,infinite;-webkit-animation-play-state:running,running;animation-name:snowflakes-fall,snowflakes-shake;animation-duration:10s,3s;animation-timing-function:linear,ease-in-out;animation-iteration-count:infinite,infinite;animation-play-state:running,running}.snowflake:nth-of-type(0){left:1%;-webkit-animation-delay:0s,0s;animation-delay:0s,0s}.snowflake:nth-of-type(1){left:10%;-webkit-animation-delay:1s,1s;animation-delay:1s,1s}.snowflake:nth-of-type(2){left:20%;-webkit-animation-delay:6s,.5s;animation-delay:6s,.5s}.snowflake:nth-of-type(3){left:30%;-webkit-animation-delay:4s,2s;animation-delay:4s,2s}.snowflake:nth-of-type(4){left:40%;-webkit-animation-delay:2s,2s;animation-delay:2s,2s}.snowflake:nth-of-type(5){left:50%;-webkit-animation-delay:8s,3s;animation-delay:8s,3s}.snowflake:nth-of-type(6){left:60%;-webkit-animation-delay:6s,2s;animation-delay:6s,2s}.snowflake:nth-of-type(7){left:70%;-webkit-animation-delay:2.5s,1s;animation-delay:2.5s,1s}.snowflake:nth-of-type(8){left:80%;-webkit-animation-delay:1s,0s;animation-delay:1s,0s}.snowflake:nth-of-type(9){left:90%;-webkit-animation-delay:3s,1.5s;animation-delay:3s,1.5s}
        </style>
    </head>
    <body>
        <!-- Snowflakes container -->
        <div class="snowflakes" aria-hidden="true">
          <div class="snowflake">❅</div><div class="snowflake">❅</div><div class="snowflake">❆</div>
          <div class="snowflake">❄</div><div class="snowflake">❅</div><div class="snowflake">❆</div>
          <div class="snowflake">❄</div><div class="snowflake">❅</div><div class="snowflake">❆</div>
          <div class="snowflake">❄</div>
        </div>

        <h1>🎅 Santa's Legacy Shop 🎅</h1>
        <div class="subtitle">"Refactor me before Christmas or the code freezes!"</div>

        <div class="controls">
            <form method="GET" action="/">
                <label>🔍 Search:</label>
                <input type="text" name="q" value=\"""" + search_query + """\" placeholder="Search toys...">
                
                <label>📂 Category:</label>
                <select name="category">
                    <option value="all" """ + ('selected' if current_category == 'all' else '') + """>All Categories</option>
                    <option value="transport" """ + ('selected' if current_category == 'transport' else '') + """>Transport</option>
                    <option value="clothing" """ + ('selected' if current_category == 'clothing' else '') + """>Clothing</option>
                    <option value="food" """ + ('selected' if current_category == 'food' else '') + """>Food</option>
                    <option value="tech" """ + ('selected' if current_category == 'tech' else '') + """>Tech</option>
                    <option value="crafts" """ + ('selected' if current_category == 'crafts' else '') + """>Crafts</option>
                </select>
                
                <button type="submit" class="search-btn">Find Gifts! 🎁</button>
            </form>
        </div>

        <div class="grid">
            """ + cards_html + """
        </div>
        
        <footer style="text-align: center; margin-top: 50px; color: #7f8c8d;">
            <p>Made with ❤️ and ☕ by the North Pole Dev Team (Legacy Division)</p>
        </footer>
    </body>
    </html>
    """
    return html

@app.route("/")
def home():
    """
    Handles the HTTP requests. 
    Think of this as the Head Elf directing traffic in the workshop. 🚦
    """
    # Extract search and filter params from the request URL
    # Flask makes this super easy!
    search_query = request.args.get('q', '')
    category_filter = request.args.get('category', 'all')
    
    print(f"🎄 Request: Search='{search_query}', Category='{category_filter}'")

    # 1. Fetch Data
    all_products = fetch_products()
    
    # 2. Apply Search (Section 1)
    searched_products = search_products(all_products, search_query)
    
    # 3. Apply Filter (Section 2)
    final_products = filter_products_by_category(searched_products, category_filter)
    
    # 4. Render (Section 3)
    html_content = render_page(final_products, search_query, category_filter)
    
    return html_content

def open_browser():
    """Wait a moment for the server to start, then open the browser."""
    time.sleep(1.5)
    webbrowser.open(f"http://localhost:{PORT}")

# ==========================================
# 🚀 MAIN ENTRY POINT 🚀
# ==========================================
if __name__ == "__main__":
    print(f"🎅 Santa's Flask Server is starting up on port {PORT}...")
    print(f"🔗 Open your browser at: http://localhost:{PORT}")
    print("⚠️  Make sure json-server is running! (npx json-server db.json --port 3000)")
    
    # Open the browser automatically for the user (Surprise!)
    # We run this in a separate thread so it doesn't block the server start
    threading.Thread(target=open_browser).start()
    
    # Run the Flask app
    app.run(port=PORT, debug=True)
