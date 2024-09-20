import flet as ft
import requests


# Create a supabase account and get the url and key

URL:str = "https://jpwxxlrwtwbhmjtqzovc.supabase.co"
KEY:str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Impwd3h4bHJ3dHdiaG1qdHF6b3ZjIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjY4MDI3NTcsImV4cCI6MjA0MjM3ODc1N30.a8chRwkA_ghREiURSsSkJxCyS-vDDjAEyfACOo3VjVM"


#Creacion de conexiones a los endpoits para get y post

class Fetch:

    tasks: list[dict[str,str]] = []

    @staticmethod
    def fetch_all_tasks():
        url: str = "https://jpwxxlrwtwbhmjtqzovc.supabase.co/rest/v1/flet_tasks?select=*"
        params: dict[str,str] = {
            "apikey": KEY,
            "Authorization": f"Bearer {KEY}"
        }

        res = requests.get(url,headers=params)

        print(res.json())




def main(page: ft.Page):
    page.add()
    page.update()

if __name__ == '__main__':
    Fetch.fetch_all_tasks()
    ft.app(main)
