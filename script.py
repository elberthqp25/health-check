import requests
import datetime
import os

def call_endpoint():
    """Función para llamar a un endpoint y registrar el resultado."""
    # Define la URL de tu endpoint
    # Reemplaza 'https://tu-endpoint-aqui.com' con la URL real
    endpoint_url = os.environ.get('ENDPOINT_URL', 'https://wsapiquposalmacenvirtual.coopelesca.com/swagger/ui/index') 

    try:
        # Realiza una solicitud GET al endpoint
        response = requests.get(endpoint_url)

        # Muestra la hora actual para el log
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Verifica si la solicitud fue exitosa (código de estado 200)
        if response.status_code == 200:
            print(f"[{current_time}] La llamada al endpoint fue exitosa. Código de estado: {response.status_code}")
        else:
            print(f"[{current_time}] Hubo un error al llamar al endpoint. Código de estado: {response.status_code}")
            print(f"Contenido de la respuesta: {response.text}")

    except requests.exceptions.RequestException as e:
        # Maneja cualquier error de conexión
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{current_time}] Ocurrió un error de conexión: {e}")

if __name__ == "__main__":
    call_endpoint()