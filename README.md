**FIFA 25 Players Rating Data Project**

This is a complete end-to-end data project, covering the entire pipeline from data extraction to analysis. The project extracts FIFA 25 player ratings, transforms and cleans the data, and loads it into a MySQL database for further analysis.

**Features**

- Data Extraction: Player data is scraped from the FIFA website using the crawl4ai package.

- Data Transformation & Cleaning: The extracted data is processed and cleaned using Python’s pandas library.

- Data Loading: The cleaned dataset is loaded into a MySQL database using SQLAlchemy, making it ready for analysis and visualization.

**Technologies Used**

- Python – for data processing and scripting

- Pandas – for data transformation and cleaning

- crawl4ai – for web scraping FIFA player ratings

- MySQL – database to store cleaned data

- SQLAlchemy – for database connection and data insertion

**Project Structure**
data/ # Contains extracted raw and processed data  
├── league_names.csv  
├── players_info.json  
└── players_rating.json

schemas/ # JSON schemas for extracting data
├── schema_info.json # Defines fields and selectors for player info extraction
└── schema_rating.json # Defines fields and selectors for player ratings extraction

scripts/ # Python scripts for extraction and transformation
├── extract_info.py
├── extract_ratings.py
└── transform_and_load.ipynb

sql_analysis/ # Questions for analysis
└── questions.txt

README.md # Project documentation
requirements.txt # Python dependencies
