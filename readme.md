# kssb-menu
Scrape the KSSB food menu.

The goal of this project is to allow someone to supply a day, and you will get whatever is on the menu for that day.

The main problem with this, though, is the webpage is hard to parse. Getting easier as more is discovered, but here we are.

I also want to set this thing up so it can run on my server and 'ding' me with whatever is on the menu for that day. Maybe I can charge people for this service too. :).

## What we can do so far
* Get the page itself.
* Find the class the menu items themselves are in. Wordpress does some good after all!
* The menu prints now (including its items).

## What still must be done
* Do something with that information (ask the user for a day, etc).
* Make another repo for, say, alerts via Telegram? I'd do MMS but I don't want to pay for that at the moment.
