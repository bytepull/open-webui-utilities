# Open WebUI Utilities

Prompts, Tools and Functions to use with Open WebUI

Documentation:
- [Open WebUI](https://docs.openwebui.com/)
- [Open WebUI - GitHub](https://github.com/open-webui/)
- [Ollama](https://ollama.com/)
- [Youtube Transcript API](https://pypi.org/project/youtube-transcript-api/)
- [Youtube Transcript API - GitHub](https://github.com/jdepoix/youtube-transcript-api/tree/master)

To run Open WebUI container with Docker:
`docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main`
