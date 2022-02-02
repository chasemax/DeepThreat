"""
Game:
2-player asymmetrical.
1 player is the security expert
1 player is the rogue AI
Security expert's goal is to stop the AI by removing all copies of intelligent code (backups) using one of multiple programs:
1. The scalpel, which surgically removes the AI
2. The nuke, which completely destroys the AI and the computer that it is on
3. The infection, which turns one copy of the AI against itself and has it start feeding on itself. Possible chance of failure?

AI's goal is to compute an algorithm that will allow it to destroy humanity. Thus there are three phases:
1. Research the compute power algorithm
2. Infect enough machines and develop high enough security for a fast crack
3. Crack the codes before you can get shut down

The AI can pick a target and its tech tree changes depending on which target it wants to disrupt.

Reconaissance:
1. Security expert must explore the network map
2. Security expert must get 3 pieces of AI "activity"

Resource management:
1. Compile power: both the AI and the security expert have limited computing power and each program that they make
takes a lot of time to compile (depending on complexity)
- each program can have 4 pieces, including obfuscation, payloads, and propagation methods.
- Obfuscation allows you to disguise your payload as another program on a computer. Some programs are on all computers,
allowing you to hide your payload anywhere without the enemy seeing it, but these take more time to compile.
- Propagation methods will only spread your program to other computers that have certain services / software on them.
- Some are worms, some are forked worms (exponential growth) and some are viruses (event triggered). Exponential growth takes the most compile time.
- Payloads include firewalls (blocks certain programs from accessing computers), surveillance (alerts the owner to what is going on),
    the programs that kill the AI, the programs that are doomsday, programs that steal compute power,
    programs that retrieve codebases, programs that delete files
2. AI Fingerprints: Needed for reconaissance on the AI
3. Codebase: Required for research


Properties of a computer:
- List of programs running and how much CPU those programs take up
- CPU power
- Files (codebases and AI fingerprints)
- Connections (can be destroyed by powerful programs)
- Tunnels (can be destroyed by simple programs)

The security expert does not want the AI to know it is watching the AI, because the AI gets bonuses for nodes being destroyed
after a certain upgrade (aftermath damage report)

Tech tree for security expert and the AI.

Both:
- Virus
- Worm
- Forked Worm
- Worm speed upgrade I
- Worm speed upgrade II
- Firewall
- Surveillance
- Botnet I
- Botnet II
- Obfuscation I
- Obfuscation II
- Codebase extraction
- Compiler upgrade I
- Compiler upgrade II
- Compiler upgrade III
- Tunnels
- Delete important resources

Security Expert:
- Auto-compromiser
- Download upgrade (+1 slot)
- Download speed upgrade
- Upload upgrade (+1 slot)
- Upload speed upgrade

AI:
- Intelligence backups
- Doomsday crackers
- Hiding self

Actions of both:
- Build / compile program
- View machine
- Compromise machine
- Upload file
- Download file

AI action:
- Crack




- Game architecture:
- Game logic is running in a loop, while GUI is merely observing what happens in the loop.

Develop one second at a time. That is, make a game loop that will run for a second with every 'enter' of the command line. Or some other interval.
Then you can execute commands to make it work.

"""