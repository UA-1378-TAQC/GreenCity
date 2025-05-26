eco_news_invalid_page_values = [
    (-1, 400, "Page must be a positive number"),
    (-5, 400, "Page must be a positive number"),
    ("abc", 400, "Invalid value for page: must be an integer"),
    (1.5, 400, "Invalid value for page: must be an integer"),
    ("", 400, "Page must be a positive number"),
]
