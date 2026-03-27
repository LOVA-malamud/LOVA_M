#!/usr/bin/env python3
import sys
import subprocess
import shlex

def speak():
    # Check if text was provided as arguments
    if len(sys.argv) > 1:
        text = " ".join(sys.argv[1:])
    else:
        # If no arguments, read from stdin (allows piping)
        print("Reading from terminal (Ctrl+D to finish, Ctrl+C to cancel):")
        try:
            text = sys.stdin.read().strip()
        except KeyboardInterrupt:
            print("\nCancelled.")
            return

    if not text:
        print("Error: No text provided to speak.")
        return

    # Use the macOS 'say' command
    try:
        # shlex.quote is used to safely handle special characters in the text
        subprocess.run(["say", text], check=True)
    except FileNotFoundError:
        print("Error: 'say' command not found. This tool only works on macOS.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    speak()
