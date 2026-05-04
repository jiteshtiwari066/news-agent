def search_news(news_list, keyword):
    results = []
    keyword = keyword.lower()

    for news in news_list:
        if keyword in news["title"].lower():
            results.append(news)

    return results