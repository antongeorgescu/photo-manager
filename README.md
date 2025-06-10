# Photo Manager Pipeline


## Handling Multimedia Files with ffmpeg

FFmpeg is a powerful, open-source software suite used for handling multimedia data—specifically video, audio, and image processing. It’s widely used by developers, video editors, and media professionals for tasks like conversion, compression, streaming, and analysis.

---
### What FFmpeg Can Do
Here are some of its most common capabilities:

* Convert between media formats (e.g., .mov to .mp4)
* Extract audio from video files
* Resize, crop, or rotate videos
* Merge or split video/audio files
* Analyze metadata (e.g., duration, codec, creation date)
* Stream media over networks
* Generate thumbnails from videos

---
### Key Tools in FFmpeg

| Tool        | Purpose                                     |
|------------------|----------------------------------------|
| ffmpeg      | Main tool for processing audio/video        |
| ffprobe     | Extracts metadata and stream info           |
| ffplay      | Lightweight media player for quick previews |

---
### Examples of Command
* Convert a .mov file to .mp4:

    ffmpeg -i input.mov output.mp4

* Extract audio from a video:

    ffmpeg -i video.mp4 -q:a 0 -map a audio.mp3

---
### Install ffmpeg
The FFmpeg binaries can be downloaded from https://www.gyan.dev/ffmpeg/builds/ under "release builds" section


