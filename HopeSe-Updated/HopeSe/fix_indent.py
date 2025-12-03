#@author: Ankit
#@title: versionKill
#@version: 1.0
#@date: 2025-12-03

file_path = r'Backend\TextToSpeech.py'
with open(file_path, 'r') as f:
    lines = f.readlines()

# Line 41 (index 40) is the target
line_index = 40
print(f"Original line: {repr(lines[line_index])}")

if lines[line_index].strip().startswith('pygame.time.Clock().tick(10)'):
    # Check current indentation
    current_indent = len(lines[line_index]) - len(lines[line_index].lstrip())
    print(f"Current indentation: {current_indent}")
    
    if current_indent == 20:
        lines[line_index] = lines[line_index].replace('                    ', '                ', 1)
        print(f"Modified line: {repr(lines[line_index])}")
        
        with open(file_path, 'w') as f:
            f.writelines(lines)
        print("File updated.")
    else:
        print("Indentation is not 20 spaces, skipping.")
else:
    print("Line content does not match expected, skipping.")
