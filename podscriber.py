import requests

from pydub import AudioSegment
from openai import OpenAI

def transcribe_audio(file_path):
    # Initialize OpenAI client
    client = OpenAI()

    # Load the entire podcast
    podcast = AudioSegment.from_mp3(file_path)

    # PyDub handles time in milliseconds
    ten_minutes = 10 * 60 * 1000

    # Calculate the number of chunks
    total_length = len(podcast)
    num_chunks = total_length // ten_minutes + (1 if total_length % ten_minutes > 0 else 0)

    # Initialize an empty string to hold the full transcript
    full_transcript = ""

    # for i in range(num_chunks):
    for i in 1:
        # Extract a 10-minute chunk
        start = i * ten_minutes
        end = min(start + ten_minutes, total_length)
        chunk = podcast[start:end]

        # Export chunk to a temporary file
        chunk_file_name = f"temp_chunk_{i}.mp3"
        chunk.export(chunk_file_name, format="mp3")

        # Open the chunk for transcription
        with open(chunk_file_name, "rb") as audio_file:
            transcript = client.audio.transcriptions.create(
                model="whisper-1", 
                file=audio_file, 
                response_format="text"
            )

        # Append the transcript of this chunk to the full transcript
        full_transcript += transcript + " "  # Add a space between segments

        # Optional: Delete the temporary chunk file here if desired

    return full_transcript

# Usage example
file_path = "/Users/jessiesun/leaning-into-your-culture.mp3"
transcript = transcribe_audio(file_path)

output_file = "transcript.txt"
with open(output_file, "w") as file:
    file.write(transcript)

print(f"Transcription completed. Transcript saved to {output_file}.")
