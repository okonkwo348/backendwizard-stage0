import requests
from datetime import datetime, timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def profile_view(request):
    """Stage 0 Task: /me endpoint — returns profile info and a dynamic cat fact."""

    cat_fact_url = "https://catfact.ninja/fact"
    try:
        response = requests.get(cat_fact_url, timeout=5)
        response.raise_for_status()  # ensures non-200 raises an error
        cat_fact = response.json().get("fact", "Cats are awesome!")
    except requests.exceptions.RequestException:
        cat_fact = "Cat fact service is currently unavailable."

    data = {
        "status": "success",
        "user": {
            "email": "okonkwoemmanuel348@gmail.com",
            "name": "Okonkwo Emmanuel",
            "stack": "Python/Django"
        },
        "timestamp": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "fact": cat_fact
    }

    return Response(data)
