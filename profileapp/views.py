import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import datetime, timezone

@api_view(['GET'])
def profile_view(request):
    try:
        response=requests.get("https://catfact.ninja/fact", timeout=5)
        response.raise_for_status()
        cat_data = response.join()
        cat_fact = cat_data.get("fact", "Cats are wonderful creature!")
    except requests.exceptions.RequestException:
        cat_fact = "Could not fetch a cat fact right now, please try again later."

    current_time = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

    data = {
        "status":"success",
        "user":{
            "email":"okonkwopaul348@.com",
            "name":"Okonkwo Emmanuel",
            "stack":"Python/Django"
        },
        "timestamp":current_time,
        "fact": cat_fact
    }

    return Response(data)

