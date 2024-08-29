import sys
sys.path.append('../')
from youtube_video_transcript import Tools
import asyncio


url = input("Enter youtube URL:")
tool = Tools()
print(asyncio.run(tool.get_video_transcript(url)))