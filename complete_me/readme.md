[Complete Me](https://backend.turing.io/module1/projects/complete_me) is a Turing project exploring the Tries data structure.  It was recommended to me by an alumni named Kyle who said he uses this project when it is time to learn a new language!

_Just to mention, this actually ended up being a really good way to practice using recursion.  Unlike when I built a binary search tree and used iteration, many methods in this project use recursion.  It was a challenge to figure out at first, but I found myself thinking recursively.  I was actually quite proud of my method used to return all words under any given node.  It is much shorter and looks a whole lot nicer than a similar method I used to traverse my binary search tree._

```
def all_words(collected_words = [])
  if word?
    collected_words << name
  else
    children.values.each do |node|
      node.all_words(collected_words)
    end
  end
  collected_words
end
```
