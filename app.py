import requests
from flask import Flask
from flask_cors import CORS
import random



app = Flask(__name__)
CORS(app)

@app.route("/movies", methods=["GET"])
def index():

    url = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=true&language=es&page=1&sort_by=popularity.desc"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0Yzk5ZDM4OTY5YjJjNWMyZDYxMmVjMTJjMzVjN2FiOCIsInN1YiI6IjY2NDM3M2I4Y2QxZWJjOTVjZGI5YjVlNyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.ddqNN6ElsNZUfysbJqkEyIBFvecFFfuS_GaFScbq-68"
    }

    response = requests.get(url, headers=headers)

    return response.json()



@app.route("/moviesVideo/<id>", methods=["GET"])
def  videoMovie(id):
    url = f"https://api.themoviedb.org/3/movie/{id}/videos?language=en-US"

    headers = {        
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0Yzk5ZDM4OTY5YjJjNWMyZDYxMmVjMTJjMzVjN2FiOCIsInN1YiI6IjY2NDM3M2I4Y2QxZWJjOTVjZGI5YjVlNyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.ddqNN6ElsNZUfysbJqkEyIBFvecFFfuS_GaFScbq-68"
    }
    response = requests.get(url, headers=headers)

    return response.json()


@app.route("/movies/tendencias", methods=['GET'])
def tendencias():
    import requests

    url = "https://api.themoviedb.org/3/trending/movie/day?language=en-US"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0Yzk5ZDM4OTY5YjJjNWMyZDYxMmVjMTJjMzVjN2FiOCIsInN1YiI6IjY2NDM3M2I4Y2QxZWJjOTVjZGI5YjVlNyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.ddqNN6ElsNZUfysbJqkEyIBFvecFFfuS_GaFScbq-68"
    }

    response = requests.get(url, headers=headers)

    return response.json()


@app.route("/categoriaPelicula/<int:genero_id>", methods=["GET"])
def videoMoviesByCategory(genero_id):
    # Define el endpoint de la API para descubrir películas por categoría
    url = f"https://api.themoviedb.org/3/discover/movie?with_genres={genero_id}&language=es&page=1"
    
    # Establece los encabezados de la solicitud
    headers = {        
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0Yzk5ZDM4OTY5YjJjNWMyZDYxMmVjMTJjMzVjN2FiOCIsInN1YiI6IjY2NDM3M2I4Y2QxZWJjOTVjZGI5YjVlNyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.ddqNN6ElsNZUfysbJqkEyIBFvecFFfuS_GaFScbq-68"
    }
    
    # Realiza la solicitud a la API
    response = requests.get(url, headers=headers)
    
    # Devuelve los datos en formato JSON
    return response.json()





@app.route('/buscarPelicula/<movie_name>', methods=['GET'])
def buscar_pelicula(movie_name):
    url = f"https://api.themoviedb.org/3/search/movie?query={movie_name}&include_adult=false&language=es&page=1"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0Yzk5ZDM4OTY5YjJjNWMyZDYxMmVjMTJjMzVjN2FiOCIsInN1YiI6IjY2NDM3M2I4Y2QxZWJjOTVjZGI5YjVlNyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.ddqNN6ElsNZUfysbJqkEyIBFvecFFfuS_GaFScbq-68"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Error fetching data: {response.status_code}"}




@app.route('/peliculaDetalle/<id>', methods=['GET'])
def detalle_pelicula(id):
    print(id)
    url = f"https://api.themoviedb.org/3/movie/{id}?language=es"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0Yzk5ZDM4OTY5YjJjNWMyZDYxMmVjMTJjMzVjN2FiOCIsInN1YiI6IjY2NDM3M2I4Y2QxZWJjOTVjZGI5YjVlNyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.ddqNN6ElsNZUfysbJqkEyIBFvecFFfuS_GaFScbq-68"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Error fetching data: {response.status_code}"}



if __name__ == "__main__":
    app.run(debug=True)



