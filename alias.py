import requests
import json

description = input('Description: ')

url = 'https://app.anonaddy.com/api/v1/aliases'
payload = {
    "domain": "anonaddy.me",
    "description": description,
    "format": "uuid"}
    
headers = {
  'Content-Type': 'application/json',
  'X-Requested-With': 'XMLHttpRequest',
  'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiMTNjMjZmY2I3YTY4NDczYTlhMjBlMDI1Y2I5MGVmNmVmMjkxYTY2YTQ0OWM0NTNmYzRmNjNkYTg5OWRkNTQyZDA0MDc0NjQyOGMyOTQxOGEiLCJpYXQiOiIxNjA5MzQ0NzM2LjYxMjMwOSIsIm5iZiI6IjE2MDkzNDQ3MzYuNjEyMzE0IiwiZXhwIjoiMTc2NzExMTEzNi41OTQ1NDEiLCJzdWIiOiIyMmRjYWQ1Yy0yMWE1LTRhNjEtYmFlZS00NzNiNzJkNzMyZGMiLCJzY29wZXMiOltdfQ.vLSAlV8cgugj7J78aWj1FMy2Mr0JWZhqNoxekM6CmYPtBYuYhlgRndRTvX9k8vUnK3-I7XuW8YJIZhaeGavYOw899zMkEGNfOzpaqs1XEXyHy8ji8atCnATC6Vo6pLgeNQqyvzgJ1Ptt2yRa9XiQgPUxbyfKcJ7fChuisIQlFdMy5WjZR6q8Tracar6HOAVynXtUZkNWCg_yGIC9hS4LSfS6sDWx3898yV98983BzDqeDp_yQGpYID6FLsR9_L0Bl_XZq1Vd24QZIi-MnIFfXGFj2ZBGFpR-Qysgf1ZTFiewGboYIbqG9P1-9bdGQRoLBjUCiMt8vjmNQgU3bOzSv5wWZ0P5RqFd9Z9z-9jVFYu9HlW5rlvdLRNVtKR_H3j-6yv2yztH0TH0LNvLH8IItbd8eZ1OG9rtlu09pYMXhuX3rO1rxrAn-DUBNxT2orI-jcJybPe9Hui8hHpyDCUxCpycvoCSVyYHZCfOZv3r0MiOfidP-CzdoN2QGp2KBKwrXx4Tg0eZ7egFsBD77bqv0MiiPo-O0mqrCxF0HNWEhO_3grYvJtM-iHvQZxr2mi0UfZNem61T_wLfu6n_zlZp62UcnIaaiGNtFpvx3U2XyLI5pxu2fg-gwge0NBF4XVhuG6OgGd9ROPKgApJxfEqPbwwCa6uONYyo4l7ag2z0ulY'
}

response = requests.request('POST', url, headers=headers, json=payload)
print(response.json()['data']['email'])