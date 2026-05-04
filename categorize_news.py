def get_category(title):
    title = title.lower()

    if "cricket" in title or "match" in title or "football" in title:
        return "Sports"

    elif "ai" in title or "technology" in title or "software" in title:
        return "Tech"

    elif "election" in title or "government" in title or "minister" in title:
        return "Politics"

    else:
        return "General"