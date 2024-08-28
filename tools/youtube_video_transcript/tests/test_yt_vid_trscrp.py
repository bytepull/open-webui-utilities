import sys
sys.path.append('../')
import asyncio
from youtube_video_transcript import Tools


url = 'https://www.youtube.com/watch?v=0D03dMtyHe0'
tool = Tools()
print(asyncio.run(tool.get_video_transcript(url)))