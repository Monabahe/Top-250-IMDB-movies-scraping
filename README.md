# Top 250 imdb Movies Web Scraping

## Project Overview
The **Top 250 Movies Web Scraping** project involves extracting information about the top 250 movies from a popular movie website using Python. The project utilizes web scraping techniques to gather data such as movie titles, ratings, and release years, which are then cleaned, processed, and visualized to provide insights into the top-rated movies.

## Tools Used
- **Python**: Programming language used for web scraping and data analysis.
- **BeautifulSoup**: For parsing HTML and extracting data from web pages.
- **Requests**: For sending HTTP requests to access web page content.
- **Pandas**: For data manipulation and cleaning.
- 
## Project Steps

### 1. Web Scraping Setup
- Installed and configured the necessary libraries: BeautifulSoup, Requests, Pandas, Matplotlib, and Seaborn.
- Identified the target movie website (e.g., IMDb) and the structure of the HTML content to locate the necessary data fields (e.g., movie title, rating, release year, reviews, poster link).

### 2. Data Extraction
- Sent HTTP requests to access the movie web page.
- Used BeautifulSoup to parse the HTML content and extract relevant data such as:
  - Movie titles.
  - Ratings.
  - Release years.
  - Reviews
  - movie link
  - Additional details like directors and genres if available.
- Collected the data into a structured format for further processing.

### 3. Data Storage
- Stored the extracted data in a Pandas DataFrame for easy manipulation and analysis.
- Saved the data to a CSV file to ensure persistence and for future reference.

### 4. Data Cleaning
- Inspected the DataFrame for missing values, duplicates, and incorrect data types.
- Performed data cleaning tasks including:
  - Removing duplicates.
  - Filling or dropping missing values.
  - Converting data types to appropriate formats (e.g., release year, rating).
  - Standardizing text data for consistency.

### 5. Insights and Findings
- Analyzed the visualizations to derive insights about the top 250 movies.
- Identified patterns and trends, such as the distribution of ratings and the most prolific years for top-rated movies.
- Summarized findings in a clear and concise manner to provide a useful overview of the top-rated movies.

## Repository Structure
- `web scraping movies/`: Contains the web scraping script.
- `imdb_moviesdata/`: Stores the extracted and cleaned csv file.
- `README.md`: Project description and overview.


## Conclusion
This project demonstrates the use of web scraping to gather and analyze data on the top 250 movies. By leveraging Python libraries for data extraction, cleaning, and visualization, the project provides a detailed and actionable overview of the highest-rated movies.

---

Feel free to contribute to this project by suggesting improvements, reporting issues, or submitting pull requests. Happy scraping!
