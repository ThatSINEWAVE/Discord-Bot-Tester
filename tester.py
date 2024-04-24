import time
import json
import threading
import discord
import logging
import asyncio
import os


# Suppress discord.py logs (or set your desired log level)
logging.getLogger('discord').setLevel(logging.CRITICAL)


class DiscordBotClient(discord.Client):
    def __init__(self, bot_name, bot_token, log_file):
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.bot_name = bot_name
        self.bot_token = bot_token
        self.log_file = log_file

    async def on_ready(self):
        print(f'{self.bot_name} is ready!')
        self.log_to_file("success")

    async def on_message(self, message):
        if message.content == '!stop':
            if message.author == self.user:
                await message.channel.send("Stopping the bot...")
                await self.logout()

    def log_to_file(self, status):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        log_data = {"bot_name": self.bot_name, "status": status, "timestamp": timestamp}
        if os.path.isfile(self.log_file) and os.stat(self.log_file).st_size != 0:
            with open(self.log_file, "r") as f:
                logs = json.load(f)
        else:
            logs = []

        logs.append(log_data)
        with open(self.log_file, "w") as f:
            json.dump(logs, f, indent=2)


async def start_bot(bot_name, bot_token, log_file):
    try:
        client = DiscordBotClient(bot_name, bot_token, log_file)
        await client.start(bot_token)
    except Exception as e:
        print(f"Failed to start bot {bot_name}: {e}")
        client.log_to_file("failure")


def start_all_bots(bot_info, log_file):
    threads = []
    for bot in bot_info:
        bot_name = bot['name']
        bot_token = bot['token']
        thread = threading.Thread(target=start_bot, args=(bot_name, bot_token, log_file))
        thread.start()
        threads.append((bot_name, thread))
        time.sleep(1)  # Wait 1 second before starting the next bot
    return threads


def stop_bot(bot_clients, bot_name):
    for bot_client in bot_clients:
        if bot_client.bot_name == bot_name:
            bot_client.logout()
            return
    print(f"No bot found with name {bot_name}")


async def main():
    with open('bots.json') as file:
        bot_info = json.load(file)

    log_file = "log.json"

    print("Select which bots to run:")
    print("0. All bots")
    for i, bot in enumerate(bot_info, 1):
        print(f"{i}. {bot['name']}")

    choice = input("Enter your choice: ")
    if choice == "0":
        bot_clients = await asyncio.gather(*(start_bot(bot['name'], bot['token'], log_file) for bot in bot_info))
        while True:
            stop_choice = input("Enter bot name to stop or 'all' to stop all bots: ")
            if stop_choice == 'all':
                for bot_client in bot_clients:
                    bot_client.logout()
                break
            else:
                stop_bot(bot_clients, stop_choice)
    elif choice.isdigit() and 1 <= int(choice) <= len(bot_info):
        bot_index = int(choice) - 1
        bot = bot_info[bot_index]
        await start_bot(bot['name'], bot['token'], log_file)
        while True:
            stop_choice = input("Enter 'stop' to stop the bot: ")
            if stop_choice == 'stop':
                break
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    asyncio.run(main())
