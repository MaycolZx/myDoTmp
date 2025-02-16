import yt_dlp

# URLS = ["https://www.youtube.com/watch?v=1vUD5duFdoc"]
#
# ydl_opts = {
#     "format": "m4a/bestaudio/best",
#     # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
#     "postprocessors": [
#         {  # Extract audio using ffmpeg
#             "key": "FFmpegExtractAudio",
#             "preferredcodec": "m4a",
#         }
#     ],
# }
#
# with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#     error_code = ydl.download(URLS)


# def download_audio_from_playlist(playlist_url, output_folder):
#     options = {
#         "format": "bestaudio/best",  # Descargar solo el mejor audio disponible
#         "outtmpl": f"{output_folder}/%(title)s.%(ext)s",  # Plantilla para el nombre del archivo
#         "postprocessors": [
#             {
#                 "key": "FFmpegExtractAudio",
#                 "preferredcodec": "mp3",  # Extraer en formato MP3
#                 "preferredquality": "192",  # Calidad de audio
#             }
#         ],
#         "noplaylist": False,  # Permitir descargas de playlists
#         "quiet": False,  # Mostrar mensajes de progreso
#     }
#
#     with yt_dlp.YoutubeDL(options) as ydl:
#         print(f"Iniciando la descarga de la playlist: {playlist_url}")
#         ydl.download([playlist_url])


def download_audio_from_playlist(playlist_url, output_folder):
    failed_downloads = []  # Lista para guardar canciones no procesadas

    # Opciones de yt-dlp
    options = {
        "format": "bestaudio/best",  # Descargar solo el mejor audio disponible
        "outtmpl": f"{output_folder}/%(title)s.%(ext)s",  # Plantilla para el nombre del archivo
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",  # Extraer en formato MP3
                "preferredquality": "192",  # Calidad de audio
            }
        ],
        "noplaylist": False,  # Permitir descargas de playlists
        "quiet": False,  # Mostrar mensajes de progreso
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        try:
            # Obtener información de la playlist
            playlist_info = ydl.extract_info(playlist_url, download=False)
            if "entries" not in playlist_info:
                print("No se pudo obtener información de la playlist.")
                return

            print(f"Playlist contiene {len(playlist_info['entries'])} canciones.")

            # Iterar sobre las canciones en la playlist
            for entry in playlist_info["entries"]:
                try:
                    print(f"Procesando: {entry['title']}")
                    ydl.download([entry["webpage_url"]])
                except Exception as e:
                    print(f"Error al procesar {entry['title']}: {e}")
                    failed_downloads.append(entry["title"])

        except Exception as e:
            print(f"Error al obtener información de la playlist: {e}")
            return

    # Resumen de canciones no procesadas
    if failed_downloads:
        print("\nCanciones no procesadas:")
        for song in failed_downloads:
            print(f"- {song}")
    else:
        print("\nTodas las canciones fueron procesadas exitosamente.")


playlist_url = (
    "https://www.youtube.com/playlist?list=PLSmFWG1obpNjY2Wc0DmCo_UiqlG4OpFtu"
)
output_folder = "./musicSec/"

download_audio_from_playlist(playlist_url, output_folder)
