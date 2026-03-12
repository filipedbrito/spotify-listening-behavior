import time


def get_artists_genres(sp, artist_ids):

    artists_data = []

    for i, artist_id in enumerate(artist_ids):

        print(f"Buscando artista {i+1}/{len(artist_ids)}")

        try:

            artist = sp.artist(artist_id)

            artists_data.append({
                "artist_id": artist["id"],
                "artist_name": artist["name"],
                "genres": artist.get("genres", [])
            })

        except Exception as e:

            print("Erro com artista:", artist_id)
            print(e)

        time.sleep(0.3)

    return artists_data