"""
ref: https://developers.google.com/youtube/v3/quickstart/python
ref: https://developers.google.com/resources/api-libraries/documentation/youtube/v3/python/latest/
"""

import google.oauth2.credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

CLIENTS_SECRET_FILE = 'client_secret.json'
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'


def get_authenticated_service():
    flow = InstalledAppFlow.from_client_secrets_file(CLIENTS_SECRET_FILE, SCOPES)
    credentials = flow.run_console()
    return build(API_SERVICE_NAME, API_VERSION, credentials=credentials)


def process_playlist(playlist_id):
    # TODO: if result['nextPageToken'] exists, then there's more to page through
    """
    ref: https://developers.google.com/resources/api-libraries/documentation/youtube/v3/python/latest/youtube_v3.playlistItems.html

    Takes a Youtube playlist and processes it.

    :param playlist_id:
    :return:
    """
    yt_service = get_authenticated_service()
    result = yt_service.playlistItems().list(part='snippet', playlistId=playlist_id, maxResults=50).execute()
    return result
