'''
Chapter8, topic - SSH into a remote server
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & BASIC UNDERSTANDING
# =====================================================================
# SSH (Secure Shell) -> A secure, encrypted digital tunnel connecting your
#                       local terminal directly to a distant cloud server.
# SSH Client        -> The tool on your laptop that encrypts your commands.
# SSH Daemon (sshd) -> The server security guard listening on Port 22.
#
# =====================================================================
# 🎯 REAL-WORLD AGENCY VALUE
# =====================================================================
# 1. 24/7 Uptime   -> Production scripts must live on resilient cloud servers
#                     (AWS, DigitalOcean) instead of vulnerable local laptops.
# 2. Key-Pairs     -> The standard secure way to log in. Uses a Public Key 
#                     (the lock on the server) and a Private Key (your key file).
#
# =====================================================================
# 💻 CRITICAL COMMAND CHEAT SHEET
# =====================================================================
# Password Login   -> ssh username@IP_ADDRESS
# Private Key Login -> ssh -i path/to/key.pem username@IP_ADDRESS
# Custom Port Entry -> ssh -p 2222 -i path/to/key.pem username@IP_ADDRESS
# Direct Execution  -> ssh username@IP "cd /app && python3 script.py"
# Close Connection  -> exit
#
# =====================================================================
# ⚠️ COMMON PITFALLS & SOLUTIONS
# =====================================================================
# • Bad Permissions -> Run 'chmod 600 key.pem' to lock down loose keys.
# • Wrong Username   -> AWS defaults to 'ec2-user', Ubuntu servers use 'ubuntu'.
# • Hangs/Timeouts  -> The cloud dashboard firewall is blocking Port 22 traffic.
#
# =====================================================================
# 🎬 THE PRO SHORTCUTS & MINDSET
# =====================================================================
# • SSH Config Aliases -> You can write profiles inside `~/.ssh/config`
#                         to log in instantly using `ssh client-bot`.
# • Golden Rule        -> "SSH is just an encrypted pipeline that bends space;
#                         once the tunnel is open, remote folders behave 
#                         exactly like local folders."
# • Execution Tip      -> Standard scripts die when the SSH tunnel closes. 
#                         Always run production pipelines using Docker containers 
#                         or Background Services (Systemd).
# =====================================================================
