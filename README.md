A simple, algorithim based Python program that lets you look up the definitions of possibly unknown words. 

This took me about ~1 hour total to make, the idea concieved after reading articles and finding how tedious looking up each word was and having to make sure it was the right usage.

Python's PyDict not only provides you with all the definitions of a word but does it entirely in a terminal format, so I combined it along with the BeautifulSoup parser to scrape
all the words from a webpage. The program then crosschecks all the words using a text file of the 10,000 most common words in English (credit to first20hours on GitHUb) in addition to a list of forbidden characters.

Enjoy using!

<img width="469" alt="image" src="https://github.com/JasonD2626/ObscureDictionary/assets/107736333/05c53d7f-2f28-4f5a-9a01-3b44012113c0">
**The user is prompted to enter a link (great article by the way)**

<img width="94" alt="image" src="https://github.com/JasonD2626/ObscureDictionary/assets/107736333/8b9092dd-9ec5-4ad5-b97d-df4f16e3c7c8">
**The program prints 'eurypterid' as a possible word of interest**

<img width="508" alt="image" src="https://github.com/JasonD2626/ObscureDictionary/assets/107736333/257a4340-3c24-465b-8c49-8807a8850efc">
**The user is then prompted to enter the number of the word whose definition they desire, and the program returns said definition**


