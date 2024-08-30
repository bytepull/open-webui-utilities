"""
title: Youtube Video Transcript Retriever
author: Luca G
funding_url: https://github.com/open-webui
version: 1.0.0
license: MIT
"""

import re
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


class Tools:
    def __init__(self):
        pass

    async def get_video_transcript(
        self, url: str, __event_emitter__: Callable[[dict], Any] = None
    ) -> str:
        """
        Retrieves the transcript for a YouTube video given the video URL.
        :url: The URL of the YouTube video.
        :return: The transcript of the YouTube video.
        """

        emitter = EventEmitter(__event_emitter__)
        pattern = re.compile(
            r"https\:\/\/www.youtube.com/watch\?v=[A-Za-z0-9_-]+")

        if not (bool(pattern.match(url))):
            await emitter.emit(
                status="error",
                description=f"Wrong URL: {url}",
                done=True,
            )
            return ""

        video_id = url.split("v=")[1]

        if not (video_id):
            await emitter.emit(
                status="error",
                description=f"Cannot get video ID from URL: {url}",
                done=True,
            )
            return ""

        await emitter.emit("Fetching video transcript")

        formatter = TextFormatter()

        transcript = "video transcript not found"

        try:
            transcript = formatter.format_transcript(
                YouTubeTranscriptApi.get_transcript(
                    video_id, languages=["it", "en"])
            )
            await emitter.emit(
                status="complete",
                description="Transcript retrieved succesfully",
                done=True,
            )
        except Exception as e:
            print(e)
            await emitter.emit(
                status="error",
                description="Transcript not found",
                done=True,
            )
        finally:
            return transcript
