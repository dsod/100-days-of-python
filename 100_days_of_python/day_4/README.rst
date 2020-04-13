So what is the deal with collections.deques (decks) vs. regular lists?
I know, from the documentation, that decks are faster at removing and adding elements to the start and end of the collection.
Today i explore the differences and limitations of the deck collection to get a better understanding of when, and when not to use it.

TL;DR
As it turns out, because decks uses a linked-list implementation, it is much fast at adding and popping values from the left / [0] compared to lists.
This is because the linked-list implementation doesn't have to move any other elements in memory when adding elements to the beginning.

I did not find decks faster for appending, extending or popping elements to/from the end of the collection.
After some googling i found out that it depends on if the list has to be moved in-memory or not. (https://stackoverflow.com/a/23487658)
The deck append performance are more consistens because the collection never have to be moved.

I also noted a few limitations with decks; Slicing and sorting (method), which are not supported.