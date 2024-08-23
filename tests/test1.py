import re
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter


url = 'https://www.youtube.com/watch?v=K3Fq4iLi6Xg'

pattern = re.compile(r'https\:\/\/www.youtube.com/watch\?v=[A-Za-z0-9]+')
        
print(bool(pattern.match(url)))

video_id = url.split("v=")[1]

print(video_id)

# retrieve the available transcripts
# transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

formatter = TextFormatter()
transcript = formatter.format_transcript(YouTubeTranscriptApi.get_transcript(video_id, languages=['it', 'en']))[:20]

# print((transcript_list))
print(transcript)

# if transcript_list.manually_created:
#     print(transcript_list.manually_created)
# elif transcript_list.generated:
#     print(transcript_list.generated)
# else:
#     print('Not found')

# iterate over all available transcripts
# for transcript in transcript_list:
#     if hasattr(transcript, "language_code") and transcript.language_code == 'it':
#         print('italian')
#         print(formatter.format_transcript(transcript.fetch())[:20])
#     elif transcript.is_translatable:
#         print(transcript.language)
#         print(formatter.format_transcript(transcript.translate('it').fetch())[:20])
#     else:
#         print('Not found')


# text_formatted = formatter.format_transcript(transcript)

# print(text_formatted)