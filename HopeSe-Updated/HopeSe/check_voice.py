#@author: Ankit
#@title: versionKill
#@version: 1.0
#@date: 2025-12-03

from dotenv import dotenv_values
import asyncio
import edge_tts

env_vars = dotenv_values(".env")
AssistantVoice = env_vars.get("AssistantVoice")

print(f"AssistantVoice from .env: '{AssistantVoice}'")

async def test_voice():
    print(f"Testing with voice: '{AssistantVoice}'")
    try:
        communicate = edge_tts.Communicate("Testing voice.", AssistantVoice)
        await communicate.save(r"Data\test_voice.mp3")
        print("Generation successful.")
    except Exception as e:
        print(f"Generation failed: {e}")

if __name__ == "__main__":
    asyncio.run(test_voice())
