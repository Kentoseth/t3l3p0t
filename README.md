# t3l3p0t
Telegram honeypot using an actual user (and not a bot). Perfect for monitoring phishing/scams from groups.

You can use this tool to catch phishing and other scams being sent to users that are in your groups.

You can run any number of these honeypots, but you will need to run each one separately. This is because each instance is running an actual user, using [telegram-cli](https://github.com/vysheng/tg) .

## Contents
 * [Requirements](#requirements)
 * [Installation](#installation)
 * [Usage](#usage)
 * [Contribute](#contribute)
 * [License](#license)
 * [Queries](#queries)

## Requirements

You will need the following:

 * System that is able to install: [telegram-cli](https://github.com/vysheng/tg) & [pytg](https://github.com/luckydonald/pytg)
 * Python3
 * At least 2 Telegram accounts (master/normal account and 1/more honeypot accounts)
 
## Installation

 * Create a folder: `mkdir myfolder` && go into the folder `cd myfolder/`
 * Install [telegram-cli](https://github.com/vysheng/tg#installation) in `myfolder/`
   * The cli is a client like any other Telegram client
   * You may need to validate usage of your account using the original app (or it can validate via SMS/call)
 * Install [pytg](https://github.com/luckydonald/pytg#install)
   * Recommended to use a `venv`
   * Tested on Python3.6 only
 * Copy the `run.py` file from this repo into `myfolder/`
   * No need for complicated `git clone` or anything else
   
## Usage

 * Obtain the username of your master account and set it as an environment variable:
   * `export ID="@myadmin123"`
 * Whilst in `myfolder/` , start the cli-client:
   * `tg/bin/telegram-cli -k tg/tg-server.pub --json -P 4458`
 * Open another terminal and `cd /path/to/myfolder`
 * Run the script: `python run.py`
 * Send a message to your honeypot account from any other dummy account:
   * It will forward that message to your master account
 * Profit!
 
## Contribute

You know the drill. Fork the repo and open a PR.

## License

AGPLv3+

If you need an alternate license, contact me and we can arrange something.

## Queries

Just open an issue and I'll look into it.
