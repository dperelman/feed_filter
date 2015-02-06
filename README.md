# *_filter_title.py

Filter a feed's items based on their title.

    USAGE:
        <original_feed.xml >filtered_feed.xml  (rss|atom)_filter_title.py word...
        <original_feed.xml >filtered_feed.xml  (rss|atom)_filter_title.py --whitelist word...

The `word` arguments are a list of substrings that either must not
appear (default) or must appear (`--whitelist`) in the titles of the
output.

There are two variants of the script. `rss_filter_title.py` works on
[RSS][rss] feeds while `atom_filter_title.py` works on [ATOM][atom]
feeds.


[rss]: https://en.wikipedia.org/wiki/RSS
[atom]: https://en.wikipedia.org/wiki/Atom_%28standard%29
