# GPU Stock Checker
A Python script that uses Selenium and Discord to automatically refresh a webpage every few minutues and checks for the stock of items. When the item is in stock, a message will be sent to a Discord channel with a link to the item.
## Installation and Usage
1. Ensure you have Google Chrome installed and verify the version.
2. Go to <a href="https://chromedriver.chromium.org/downloads">ChromeDriver</a> and download the version that supports your version of Chrome.
3. When the download is finished, extract the files, and set your driver variable equal to the path of the ChromeDriver.exe application.
    * As an example, mine is: `driver = webdriver.Chrome('D:\Chromedriver\chromedriver_win32\chromedriver.exe', options=op)`
    * You can then set the driver to `get()` any webpage that you would like it to load.
4. If you would like to use Discord to send alerts, you would will need the following:
    * A Discord server.
    * A Discord bot.

This is the longest part of the set up, and I would advise you do your own research on how to set up Discord properly, as there is a lot of functionality that you can either permit or restrict from the bot based on your preferences. You can also use another messaging service such as Slack to send messages, it does not need to be Discord.

5. Whichever messaging service that you choose to use, be sure to hide your key in an `.env` file as an environment variable, and do not push that to GitHub. It should remain private.
6. Find whatever CSS element that you would like to check for (I used `find_elements_by_xpath` but there are several ways you could do this).
7. Finally, just check if that element is on the page every time Selenium refreshes; if it is, then we know nothing has changed; if it is not, then we know the page has been updated (item is in stock) and we should send a message!

## Description
A friend of mine is trying to find specifically a 3080 or 3080Ti Founders Edition card, and from my research it seems like Best Buy is the best chance for snagging one of these.  However, this script could be made to be used in an endless amount of ways, regarding anything that you need to be automated and continually checked (change the website, change what you're looking for on that webpage, choose to send a message, an email, etc).

### Additional Information
* Python 3.9.7
* Google Chrome Version 95.0.4638.69
