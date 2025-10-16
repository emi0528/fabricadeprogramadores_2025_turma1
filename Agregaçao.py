class midia:
    def __init__(self , titulo: str, artista):
        self.titulo = titulo
        self.artista = artista
        
class musica(midia):
    def __repr__(self):
        return f"'{self.titulo}' por {self.artista}"

class Playlist:
    def __init__(self,nome: str,musicas: list[musica]):
        self.nome = nome
        self.musica = musica

    def tocar_todas(self):
        print(f"\n Tocando a Playlist '{self.nome}':")
        for musica in self.musica:
            print(f" Tocando agora: {musica}")

musica_1 = musica("Aventura na sul,Boaventura")
musica_2 = musica("Bolsa de ombro, Veigh")
musica_3 = musica("Love, Keyshia Cole")

daylist = Playlist("Sua plylist diaria" , [musica_1, musica_2, musica_3])
daylist.tocar_todas()