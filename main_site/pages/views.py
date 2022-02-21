import os
import requests
from django.shortcuts import render

filter_relation = {
        "Title contains": "title",
        "Genre is": "genres",
        "Language is": "languages",
        "Rating is equal or greater than": "imdb_rating",
        "Plot contains": "plot",
    }


def home(request):
    api_load_balancer_name = os.environ.get("API_LOAD_BALANCER_NAME", "localhost:8000")
    titles_response = requests.get(f"http://{api_load_balancer_name}/titles/")
    titles_response_is_ok = 200 <= titles_response.status_code <= 299
    titles = titles_response.json()
    titles_exists = True if len(titles) > 0 and titles_response_is_ok else False
    main_title = titles[0] if len(titles) >= 1 else None
    main_title_exists = True if main_title is not None else True
    context = {
        "website_name": os.environ.get("WEBSITE_NAME", "Series website"),
        "main_title": main_title,
        "titles": titles,
        "main_title_exists": main_title_exists,
        "titles_exists": titles_exists,
        "filter_options": ["Title contains", "Genre is", "Language is",
                           "Rating is equal or greater than", "Plot contains"],
        "menu_titles": titles[:5],
    }

    if request.method == "GET":
        key_filter = request.GET.get("key-filter")
        value_filter = request.GET.get("value-filter")

        if key_filter not in [None, ""] and value_filter not in ["", None]:
            url = f"http://{api_load_balancer_name}/titles/" + filter_relation[key_filter] + "/" + value_filter
            filtered_titles_response = requests.get(url)
            filtered_titles_response_is_ok = 200 <= filtered_titles_response.status_code <= 299
            filtered_titles = filtered_titles_response.json()
            filtered_titles_exists = True if len(filtered_titles) > 0 and filtered_titles_response_is_ok else False

            context["filtered"] = True
            context["filtered_titles"] = filtered_titles
            context["filtered_titles_exists"] = filtered_titles_exists

        return render(request, "home.html", context)
