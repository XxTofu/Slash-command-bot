🍽️ Rays Restaurant Discord Bot

A powerful and fun moderation + utility Discord bot built using discord.py (slash commands / app_commands).

Designed for community servers, this bot handles moderation, automatic welcomes, and interactive fun commands — all using Discord’s built-in permission system for secure and reliable moderation.

🚀 Features
👋 Welcome System

Automatically welcomes new members when they join the server.

Sends a friendly welcome message in a specific channel

Automatically assigns a predefined role

Example message:

“Welcome @user to Rays's restaurant hope you enjoy!”

🛡️ Moderation System (Permission-Based)

Uses Discord's built-in permissions instead of hardcoded roles for better security and flexibility.

Commands
Command	Description
/clear <amount>	Deletes 1–100 messages (limit enforced)
/ban <member> [reason]	Bans a member
/unban <member>	Unbans a member
/kick <member> [reason]	Kicks a member
✅ Safety Features

Uses Discord permission checks (manage_messages, ban_members, kick_members)

Prevents kicking or banning members with equal or higher roles

Prevents kicking yourself

Checks bot permissions before executing actions

Ephemeral moderation confirmations

100 message limit on /clear to prevent abuse

📅 Utility Commands
Command	Description
/joined <member>	Shows when a user joined the server
/git	Displays the bot owner's GitHub profile
💕 Fun Commands
/ship

Generates:

A custom ship name

Random love compatibility percentage (1–100%)

Example:

Ship Name: Aleon  
❤️ @Alex has a 87% compatibility with @Leon ❤️
/rob

Displays a user’s avatar

Detects default Discord avatars

Role-restricted access

⚙️ Built With

discord.py

Slash Commands (app_commands)

Permission-based moderation system

Role hierarchy protection logic

🔐 Required Bot Permissions


✅ Manage Messages

✅ Kick Members

✅ Ban Members

✅ Manage Roles

✅ Read Messages

✅ Send Messages
