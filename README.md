# Spotify Song Preview Downloader
Download a 30 second preview of most songs on Spotify, similar to when you send a Spotify link in Discord.
# Requirements
- [Python](https://www.python.org/downloads/)
- Requests library: ```pip install requests```
# Use
Note: This code uses my personal Spotify API token. I don't expect this project to get a lot of use, but just in case it is misued you can learn how to get your own token [here](https://developer.spotify.com/documentation/web-api/tutorials/getting-started#create-an-app).
1. The method for choosing which song to download is currently under development, currently you need the song ID. You can get the song ID by copying the URL of the song from Spotify and using the string that comes after "track/". For example, if the song URL is "https://open.spotify.com/track/3ow0TQVttXQF8rLckmXgRx", the song ID is ```3ow0TQVttXQF8rLckmXgRx```.
2. Enter the song ID into the code, under the ```artist_id``` variable, or use the example song already there.
3. Run the script ```python main.py```
4. An mp3 file should be downloaded to the same folder as the Python script, or you will get an error message, as Spotify doesn't assign every song a downloadable preview.
