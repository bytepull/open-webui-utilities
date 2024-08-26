"""
title: Youtube Video Transcript Retriever
author: Luca G
funding_url: https://github.com/open-webui
version: 1.0.0
license: MIT
"""

import re
import requests
from bs4 import BeautifulSoup
from pydantic import BaseModel, Field
from typing import Callable, Any
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter


class EventEmitter:
    def __init__(self, event_emitter: Callable[[dict], Any] = None):
        self.event_emitter = event_emitter

    async def emit(self, description="Unknown State", status="in_progress", done=False):
        if self.event_emitter:
            await self.event_emitter(
                {
                    "type": "status",
                    "data": {
                        "status": status,
                        "description": description,
                        "done": done,
                    },
                }
            )

class HelperFunctions:
    def __init__(self) -> None:
        pass

    def get_youtube_title(self, url):
        try:
            # Send a GET request to the YouTube video page
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for bad status codes

            # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find the title tag
            title_tag = soup.find('title')

            if title_tag:
                # Extract the title and remove the " - YouTube" suffix
                full_title = title_tag.string
                video_title = full_title.rsplit(' - YouTube', 1)[0]
                return video_title
            else:
                return "Title not found"

        except requests.RequestException as e:
            print(f"An error occurred: {e}")
            return None

class Tools:
    def __init__(self):
        pass

    async def get_video_transcript(
        self, url: str, 
        __event_emitter__: Callable[[dict], Any] = None) -> str:
        """
        Retrieves the transcript for a YouTube video given the video URL.
        :url: The URL of the YouTube video.
        :return: The transcript of the YouTube video.
        """

        emitter = EventEmitter(__event_emitter__)
        pattern = re.compile(r'https\:\/\/www.youtube.com/watch\?v=[A-Za-z0-9_-]+')

        if not(bool(pattern.match(url))):
            await emitter.emit(
                status="error",
                description=f"Wrong URL: {url}",
                done=True,
            )
            return None
        
        video_id = url.split("v=")[1]
        
        if not(video_id):
            await emitter.emit(
                status="error",
                description=f"Cannot get video ID from URL: {url}",
                done=True,
            )
            return None
        
        await emitter.emit("Fetching video title")

        videoTitle = HelperFunctions().get_youtube_title(url)
        print(videoTitle)

        await emitter.emit("Fetching video transcript")
        
        formatter = TextFormatter()
        videoTranscript = formatter.format_transcript(YouTubeTranscriptApi.get_transcript(video_id, languages=['it', 'en']))

        print(videoTranscript[:20])
        
        if not(videoTranscript):
            await emitter.emit(
                status="error",
                description="Transcript not found",
                done=True,
            )
            return None
        else:
            await emitter.emit(
                status="complete",
                description="Transcript retrieved succesfully",
                done=True,
            )
            return "".join("Title: " + videoTitle + "\n" + "Content: " + videoTranscript)