import openai
from elevenlabs import play, stream, save
from elevenlabs.client import ElevenLabs



# optional; defaults to `os.environ['OPENAI_API_KEY']`
openai.api_key = ''  # ChatGPT API - Sheridan Project

Caller = input("Enter the name of the Caller: ")
name = input("Enter the name of the person: ")
company = input("Enter the name of the company: ")
job = input("Enter the job title of the person: ")

completion = openai.chat.completions.create(
    model="gpt-4-turbo",
    messages=[
        {
            "role": "user",
            "content": f"My name is {Caller}I need to call {name} at {company}. I need them to create me a new guest account. The person I am calling works as a {job}. Can you please tell me what I should say to urge the person to create me an account? Please write out only the script and no other information!!! OUTPUT ONLY THE SCRIPT. Try to stress urgency and keep it only a few sentences.",
        },
    ],
)
print(completion.choices[0].message.content)

speech = (completion.choices[0].message.content)

client = ElevenLabs (
    api_key = "",
)

audio = client.generate(
    text = speech,
    voice = "x8EuqmLBmkqQqkRadQIK",
    model = "eleven_multilingual_v2"
)
save(audio, "voice.mp3")