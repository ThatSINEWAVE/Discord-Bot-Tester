<div align="center">

# Discord Bot Tester

The **Discord Bot Tester** is a convenient utility designed to facilitate the quick testing and updating of profile images, banners, names, and descriptions for multiple Discord bots. It simplifies the process by allowing you to run all your bots at once, ensuring that the desired updates are applied. This is particularly useful because certain bot attributes, such as profile images and descriptions, do not get updated unless the bot runs at least once.

</div>

<div align="center">

## ☕ [Support my work on Ko-Fi](https://ko-fi.com/thatsinewave)

</div>

## Files

- **runner.py**: Python script responsible for running the Discord bots, updating the log file, and handling user interaction.
- **bots.json**: JSON file containing the configuration details of your Discord bots.
- **log.json**: JSON file logging the status of bot runs.

## Note 
Make sure to replace placeholders such as `YOUR_BOT_NAME` and `YOUR_BOT_TOKEN` with actual bot names and tokens before using the utility.*

<div align="center">

## [Join my discord server](https://discord.gg/2nHHHBWNDw)

</div>

## Usage

### Prerequisites

- Python 3.x installed on your system.
- Dependencies installed via pip. You can install them by running:
  ```
  pip install -r requirements.txt
  ```

### Configuration

1. **bots.json**: This file contains the configuration details of your bots, including their names and tokens. Update this file with the appropriate information for each of your bots.

2. **log.json**: This file logs the status of each bot run, including whether it was successful or not, along with a timestamp.

### Running the Utility

1. Run the `runner.py` script:
   ```
   python runner.py
   ```

2. Follow the on-screen prompts to select the bots you want to run or stop.

### Customization

- You can customize the behavior of the utility by modifying the `runner.py` script according to your requirements.

## Contributions:

Contributions to this repository are not currently accepted. 
The list is based solely on my discoveries but If anyone wants to add other URLs and you have an extensive collection that you would like to add them to the repo feel free to submit a request.

## License

This repository is provided under the MIT License. 
By utilizing the contents of this repository, you agree to abide by the terms of this license.