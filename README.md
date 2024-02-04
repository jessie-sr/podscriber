# Pod🎧Scriber

PodScriber is a Python-based podcast transcription tool that utilizes the OpenAI Speech-To-Text API to transcribe podcasts and outputs the transcriptions as a `.txt` file.

## Features

- **OpenAI Speech-To-Text API Integration**: Leverages the power of OpenAI's API to accurately transcribe podcasts.
- **Segmented Transcription**: Splits the `.mp3` podcast files into 10-minute chunks for efficient processing.
- **Transcription Concatenation**: Concatenates transcribed segments to form the complete transcription.
- **Improved Readability**: Includes a function `format_transcription` to enhance the readability of the output, making it easier to follow different speakers in the podcast.

## How it Works

1. **Client Creation**: Initializes a client to interact with the OpenAI API.
2. **File Loading**: Loads the target `.mp3` file using the provided `file_path`.
3. **File Segmentation**: Splits the audio file into 10-minute segments and counts the total number of chunks.
4. **Transcription**: Calls the OpenAI Speech-to-Text API to transcribe each 10-minute segment.
5. **Concatenation**: Joins the individual transcriptions to form the complete transcription.
6. **Output**: Writes the complete transcription to a `.txt` file.

## Testing

The project includes `openai-test.py` to facilitate testing of the API call functionality independently.

## Usage

1. Clone the repository to your local machine.
2. Install the required dependencies.
3. Run `podscriber.py` with the path to your podcast file as an argument.

## Dependencies

- Python 3
- OpenAI API
- PyDub

## Contribution

Contributions to PodScriber are welcome! Feel free to fork the repository, make your changes, and submit a pull request.

