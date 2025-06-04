get_data = {
    "valid_eco_news_id": 1,
    "200_response_body": {
        "status": 200,
        "id": 1,
        "title": "My Test Eco News",
        "content": "<p>My Test Eco News My Test Eco News</p>"
    },

    "400_empty_response": {
        "type": "about:blank",
        "title": "Internal Server Error",
        "status": 500,
        "detail": "Required path variable 'ecoNewsId' is not present.",
        "instance": "/eco-news/%20"
    },

    "400_string_id_response": {
        "status": 400,
        "message": "Wrong ecoNewsId. Should be 'Long'"
    },

    "404_zero_id_response": {
        "status": 404,
        "message": "Eco new doesn't exist by this id: 0"
    },
    "404_negative_id_response": {
        "status": 404,
        "message": "Eco new doesn't exist by this id: -1"
    },
    "404_not_exist_id_response": {
        "status": 404,
        "message": "Eco new doesn't exist by this id: 100"
    },
}
