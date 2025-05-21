class NewsMapper:
    @staticmethod
    def map_news(data):
        return {
            "title": data.get("title"),
            "author": data.get("author", {}).get("name"),
            "tags": data.get("tags", []),
            "content": data.get("content"),
        }
