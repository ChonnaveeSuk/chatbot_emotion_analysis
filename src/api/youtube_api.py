from googleapiclient.discovery import build

def get_video_details(api_key, video_id):
    youtube = build('youtube', 'v3', developerKey=api_key)
    request = youtube.videos().list(
        part='snippet,contentDetails,statistics',
        id=video_id
    )
    response = request.execute()
    return response

