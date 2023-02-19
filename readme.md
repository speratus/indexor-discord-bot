# Dewey (Formerly, Indexor)
Dewey is a Discord bot that searches the web for you. Dewey gets the best results from around the web and returns them
directly to your Discord channel.

Unlike other web searching Discord bots, Dewey is not restricted to getting results from a single search engine. Instead,
Dewey is powered by the metasearch engine [SearXNG](https://github.com/searxng/searxng) to get results from many sources 
simultaneously.

In addition to Dewey's current features, there are many exciting features planned for future updates, including:
* Multiple pages of results
* Results caching for faster response times
* Support for getting results from specific search engines
* User-Added search engines (Anything powered by the OpenSearch standard)
* Server and User based custom configurations
* Direct messaging the bot to get answers from anywhere on the web
* Support for other message platforms such as Slack, Telegram, Matrix.org, and others.

## Installation
The easiest way to get Access to Dewey is to follow this invite link to invite Dewey to join any Discord Server you own.

[Invite Dewey to your Server](https://discord.com/api/oauth2/authorize?client_id=1056051428575170752&permissions=2147485696&scope=bot)

Want to get Dewey running on your own? Follow the instructions below to get started:

#### Prerequisites
* A new Discord Bot and associated token
* A SearXNG instance running somewhere accessible to wherever you will have Dewey running. **DEWEY WILL NOT RESPOND
    UNLESS YOU HAVE CONFIGURED SEARXNG CORRECTLY**

### Installing Dewey
The quickest way to install Dewey is to pull the Docker image:
```bash
docker pull speratus/dewey
docker run -d -e DISCORD_TOKEN=<REPLACE_WITH_YOUR_TOKEN> -e ENGINE_URL=<URL_TO_SEARXNG> speratus/dewey
```

Make sure your `ENGINE_URL` variable has the format `https://example.com` or `http://127.0.0.1`. IP Addresses are 
acceptable to Dewey as long as the HTTP scheme is specified at the beginning

## Configuring a SearXNG Instance
Follow the instructions in [SearXNG's documentation](https://docs.searxng.org/admin/index.html) to set up a working 
instance. I recommend using their [Docker image](https://docs.searxng.org/admin/installation-docker.html).

Once you have a SearXNG instance running, there are two additional configuration rules required to enable Dewey to use
your SearXNG Instance:
1. The limiter feature must be disabled. This is usually disabled by default, so you will likely not need to worry about
    this one.
2. Make sure that the `json` format is enabled. [Enable JSON formatting](https://docs.searxng.org/admin/installation-docker.html)
3. In some cases, you may need to disable the SoundCloud search engine

Because the limiter needs to be disabled for Dewey to function, I **HIGHLY** recommend that you do not expose your
SearXNG instance to the public internet.

Once You have put these settings in place, replace the `ENGINE_URL` variable above with the address of your SearXNG
instance and Dewey will communicate with it.

**NOTE**: Both SearXNG and Dewey will work correctly if you use an IP address instead of a domain name.

## Software Dependencies

* [discord.py](https://discordpy.readthedocs.io/en/stable/)
* [indexor_core](https://github.com/speratus/indexor-core)

Indexor Core is a generic library I built to enable the core features to be abstracted for use in bots for other
messaging services.
