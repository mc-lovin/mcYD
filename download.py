from apiclient.discovery import build
from apiclient.errors import HttpError

YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def fetch_url_for_song(song_name, DEVELOPER_KEY):
  try:
    return youtube_search(song_name, DEVELOPER_KEY)
  except HttpError, e:
    print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)


def youtube_search(song_name, DEVELOPER_KEY):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  search_response = youtube.search().list(
    q=song_name,
    part="id,snippet",
    maxResults=1
  ).execute()

  for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":
      return search_result["id"]["videoId"], search_result["snippet"]["title"]
