# stepps
Behaviour analysis with STEPPS method by Jonah Berger

# Standard Words Checker
1. Get `dict` file that will be used as word reference
2. Create new `SWChecker` object and add `dict` file
3. Add sentence to `check` function to check and replace to standard word

>Example (using python 3.7.1):

~~~
dictFile = os.path.dirname(os.path.realpath(__file__))+"/improveDict.txt"
swChecker = SWChecker(dictFile)
text = "Saya adalah seorang atlit tauladan"
print(text)
stdText = swChecker.check(text)
print(stdText)
~~~