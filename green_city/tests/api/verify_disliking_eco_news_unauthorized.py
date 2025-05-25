def test_dislike_news_unauthorized(news_factory,dislike_news_factory):
    news_id = news_factory
    response = dislike_news_factory(news_id, auth_token=None)
    assert response.status_code == 401
