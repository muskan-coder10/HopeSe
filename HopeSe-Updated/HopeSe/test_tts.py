
#@author: Ankit
#@title: versionKill
#@version: 1.0
#@date: 2025-12-03

import asyncio
import edge_tts
import pygame
import os

async def test_edge_tts():
    print("Testing edge_tts...")
    try:
        communicate = edge_tts.Communicate("Hello, this is a test.", "en-US-AriaNeural")
        await communicate.save(r"Data\test_speech.mp3")
        print("edge_tts generation successful.")
    except Exception as e:
        print(f"edge_tts failed: {e}")

def test_pygame():
    print("Testing pygame playback...")
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(r"Data\test_speech.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        print("pygame playback successful.")
    except Exception as e:
        print(f"pygame failed: {e}")

if __name__ == "__main__":
    if not os.path.exists("Data"):
        os.makedirs("Data")
    
    asyncio.run(test_edge_tts())
    if os.path.exists(r"Data\test_speech.mp3"):
        test_pygame()
    else:
        print("Skipping pygame test because speech file was not generated.")
