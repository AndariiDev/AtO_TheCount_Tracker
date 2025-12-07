# AtO_TheCount_Tracker
A minimal cli tool to track the position swaps of "The Count" fight in the Across the Obelisk DLC "Necropolis Of The Damned".

Requires python3. Should work on any OS (though I haven't explicitly looked into it yet either).

## Usage

To start, simply open your terminal (on Linux and Mac) or Powershell (on Windows) and type 'python3 main.py' while in the correct directory. If you rename main.py, adjust the command accordingly.

The program will ask you about the order first, so observe it for a turn and make notes before then entering it.
Example: if the pattern is fire (orange), blood (red), fire (orange), shadow (purple): you would type in (without the quotation marks) 'f b f s'. Anytime you play a card or something else (like a pet attack) makes the boss swap positions, go into your terminal where the program is running and press enter. 
To quit, press Ctrl+C. 

It's a braindead simple program, and it's terrible, but the boss was giving me headaches and I was tired of tracking it on a notepad.

## Future Plans / Roadmap

Eventually, I am planning to write a proper overlay in C# (the game is written in Unity). This script here is really no more than a stopgap solution while I try figuring out game modding (and C#).
