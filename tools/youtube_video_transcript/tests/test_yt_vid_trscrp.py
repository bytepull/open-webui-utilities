import sys
sys.path.append('../tools')
import asyncio
from youtube_video_transcript import Tools


url = 'https://www.youtube.com/watch?v=LMzS3nXU-w4'
tool = Tools()
print(asyncio.run(tool.get_video_transcript(url)))