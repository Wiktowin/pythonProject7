# pythonProject7
cd player
CD PLAYER

Этот проект представляет собой простую программу на языке Python, которая позволяет пользователю воспроизводить песни по заданному имени исполнителя. Программа использует Deezer API для поиска песен и получения их предварительных просмотров.
Вот общий обзор того, что делает программа:
1.Импортируются модули requests и webbrowser, которые позволяют отправлять HTTP-запросы и открывать URL-адреса веб-страниц.
2.Определяется функция play_song_by_artist, которая принимает два аргумента: artist_name (имя исполнителя) и num_songs (количество песен, которые нужно воспроизвести).
3.Формируется URL-адрес для отправки запроса к Deezer API с помощью заголовков и параметров.
4.Отправляется GET-запрос к Deezer API для поиска песен по имени исполнителя.
5.Полученные данные обрабатываются в формате JSON.
6.Если в данных есть раздел "data", извлекаются песни исполнителя и сохраняются в переменную artist_songs.
6.Если найдены песни исполнителя, выводятся их названия и имена исполнителей, а также предлагается выбрать песню для воспроизведения.
8.Пользователю предлагается ввести номер песни, которую он хочет воспроизвести
9.Если введенное значение является допустимым числом от 1 до num_songs, выбранная песня открывается в браузере с помощью модуля webbrowser.
10.Если введенное значение недопустимо, выводится сообщение об ошибке.
11.Если для указанного имени исполнителя не найдено песен, выводится сообщение об отсутствии песен.

      Пользователь должен ввести имя исполнителя, чтобы программа могла найти его песни и предложить пользователю выбрать одну из них для воспроизведения. По умолчанию программа выводит десять песен, но это число можно изменить, передав другое значение вторым аргументом функции play_song_by_artist.


This project is a simple Python program that allows the user to play songs by a given artist name. The program uses the Deezer API to find songs and get previews of them.
Here is a general overview of what the program does:
1. The requests and webbrowser modules are imported, which allow you to send HTTP requests and open web page URLs.
2. The play_song_by_artist function is defined, which takes two arguments: artist_name (the name of the artist) and num_songs (the number of songs to play).
3.A URL is generated to send a request to the Deezer API using headers and parameters.
4. Send a GET request to the Deezer API to search for songs by artist name.
5.The received data is processed in JSON format.
6.If the data has a "data" section, the artist's songs are extracted and stored in the artist_songs variable.
6.If an artist's songs are found, their titles and artist names are displayed, and you are prompted to select a song to play.
8.User is prompted to enter the number of the song he wants to play
9.If the entered value is a valid number between 1 and num_songs, the selected song is opened in the browser using the webbrowser module.
10.If the entered value is invalid, an error message is displayed.
11.If there are no songs found for the specified artist name, a message about the lack of songs is displayed.

       The user must enter the name of the artist so that the program can find his songs and prompt the user to select one of them to play. By default, the program outputs ten songs, but this number can be changed by passing a different value as the second argument to the play_song_by_artist function.

