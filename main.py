
import requests
import webbrowser


def play_random_song_by_artist(artist_name, num_songs):
    url = "https://deezerdevs-deezer.p.rapidapi.com/search"
    headers = {
        "X-RapidAPI-Key": "027cd83b71msha642256f80cb07cp119bb0jsn0b02d88ec97b",
        "X-RapidAPI-Host": "deezerdevs-deezer.p.rapidapi.com"}
    params = {
        "q": artist_name}

    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    if 'data' in data:
        songs = data['data']
        artist_songs = [song for song in songs if song['artist']
        ['name'].lower() == artist_name.lower()]

    if artist_songs:
        for i, song in enumerate(artist_songs[:num_songs], start=1):
                        song_url = song['preview']
                        print(f"{i}. {song['title']} by {song['artist']['name']}")

            selected_song = input("Enter the number of the song you want to play (1-10): ")
        if selected_song.isdigit()
                and 1 <= int(selected_song) <= num_songs:
            song_index = int(selected_song) - 1
            selected_song_url = artist_songs[song_index]['preview']
            webbrowser.open(selected_song_url)
            return

        print("Invalid song number.")
        return

    print("No songs found for the artist.")


artist = input("Enter the artist name: ")
play_song_by_artist(artist,10)
