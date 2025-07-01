# CodeAlpha_ProjectName
Internship project work – includes code, reports, and documentation.

Create a stock portfolio tracking tool that allows users to add, remove, and track the performance of their stock investments. Utilize financial APIs for real-time stock data.

Step-by-Step Guide to Run Stock Portfolio Tracker

Install Python Make sure you have Python 3.7 or higher installed.
Download and install Python from: https://www.python.org/downloads/
Verify installation by running: python --version or python3 --version
Get the Project Files
Clone the GitHub repository if available: git clone https://github.com/yourusername/stock-portfolio-tracker.git cd stock-portfolio-tracker
Or download the project files manually and navigate to the folder in your terminal.
Create and Activate a Virtual Environment (Optional but recommended)
On Windows: python -m venv venv venv\Scripts\activate
On macOS/Linux: python3 -m venv venv source venv/bin/activate
Install Required Python Packages Run the following command in your terminal (make sure you're in the project folder or virtual environment): pip install ttkbootstrap yfinance matplotlib requests

Get API Keys

NewsAPI: Sign up at https://newsapi.org/ and get a free API key.
(ExchangeRate API used in the code is free and doesn't require an API key.)
Configure Your API Key
Open the project file stock_portfolio_tracker.py in a text editor.
Find the line with: NEWSAPI_KEY = "YOUR_NEWSAPI_KEY_HERE"
Replace "YOUR_NEWSAPI_KEY_HERE" with your actual NewsAPI key as a string.
Run the Application In the terminal (inside the project folder or virtual environment), run: python stock_portfolio_tracker.py

Using the App

Click Add Stock to enter a stock symbol (e.g., AAPL), number of shares, and buy price.
Select any stock in the list to view:
Its historical price chart (last 6 months).
The day’s highest and lowest prices.
Latest news headlines related to the stock.
Use Remove Selected to remove a stock.
Save your portfolio with Save Portfolio and load it with Load Portfolio.
Switch between light/dark theme using Toggle Theme.
The USD to INR exchange rate is displayed at the top.
How to run: Save this as stock_portfolio_tracker.py

Install required libraries (run in terminal or cmd): pip install ttkbootstrap yfinance matplotlib requests

Get your free NewsAPI key from https://newsapi.org/ and replace the NEWS_API_KEY in the code. python stock_portfolio_tracker.py


