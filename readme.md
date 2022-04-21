# kssb-menu
Scrape the KSSB food menu.

The goal of this project is to allow someone to supply a day, and you will get whatever is on the menu for that day.

The main problem with this, though, is the webpage is hard to parse. Getting easier as more is discovered, but here we are.

I also want to set this thing up so it can run on my server and 'ding' me with whatever is on the menu for that day. Maybe I can charge people for this service too. :).

## What we can do so far

* Get the page itself.
* Find the class the menu items themselves are in. Wordpress does some good after all!
* Print out the headers I.E. `Monday`, `Tuesday` etc...

## What still must be done
* Get what is in the menu body. Parsing issues are annoying.
* Do something with that information (ask the user for a day, etc) once fixed.