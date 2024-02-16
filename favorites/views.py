import os
import dotenv
from rest_framework.views import APIView, status, Response, Request
from rest_framework_simplejwt.authentication import JWTAuthentication
import requests


dotenv.load_dotenv()


class MovieSearchView(APIView):
    authentication_classes = [JWTAuthentication]

    def get(self, req: Request) -> Response:

        url = "https://api.themoviedb.org/3/movie/changes"

        headers = {
            "accept": "application/json",
            "Authorization": "Bearer " + os.getenv("API_KEY")
        }

        try:
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                return Response(response.text.json(), status.HTTP_200_OK)
            else:
                response.raise_for_status()
        except requests.exceptions.RequestException as error:
            print(error)
            return Response({'message': 'Movie not found.'}, status.HTTP_400_BAD_REQUEST)
