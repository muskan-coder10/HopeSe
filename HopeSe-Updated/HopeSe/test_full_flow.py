#@author: Ankit
#@title: versionKill
#@version: 1.0
#@date: 2025-12-03

from dotenv import dotenv_values
import asyncio
import edge_tts
import pygame
import os

env_vars = dotenv_values(".env")
AssistantVoice = env_vars.get("AssistantVoice")

print(f"AssistantVoice from .env: '{AssistantVoice}'")

async def test_full_flow():
    print(f"Testing full flow with voice: '{AssistantVoice}'")
    try:
        communicate = edge_tts.Communicate("Hello, this is a test of the full flow.", AssistantVoice, pitch='+5Hz', rate='+13%')
        await communicate.save(r"Data\full_test.mp3")
        print("Generation successful.")
        
        pygame.mixer.init()
        pygame.mixer.music.load(r"Data\full_test.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        print("Playback successful.")
        pygame.mixer.quit()
        
    except Exception as e:
        print(f"Test failed: {e}")

if __name__ == "__main__":
    asyncio.run(test_full_flow())
