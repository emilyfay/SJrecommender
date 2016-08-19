# SJrecommender
recommends recent scientific articles based on user's interests

includes the following:
- make_article_db.py to initialize the sqlite database to store articles in
- elsevierAPI_loop.py to search for papers by publication date in the Elsevier / Science Direct API and add them to the database
- SJreader_functions.py contains functions to score articles based on match to keywords
- user_test.ipynb is a Jupyter notebook for recommending articles from the database based on user-selected keywords
