require './lib/node'

class CompleteMe
  attr_reader :root

  def initialize
    @root = Node.new(" ")
    @word_count = 0
  end

  def insert(word, current_node = @root)
    if word == ""
      #increase word count

      @word_count += 1
      "added new word #{current_node.name}"
    elsif
      #move to next node matching tree

      current_node.children.keys.include?(word[0])
      move = move_node(word, current_node)
      insert(move['word'], move['node'])
    else
      # create a new node if it doesn't already exist

      split_word = word.split('')
      new_name = (current_node.name + split_word.shift).delete(' ')
      new_node = Node.new(new_name)
      current_node.add(new_node)
      new_word = split_word.join
      insert(new_word, new_node)
    end
  end

  def count
    @word_count
  end

  def suggest(word, current_node = @root)
    if word == ""
      #return all words under final node

      current_node.all_words
    elsif
      #move to the next node matching the word

      current_node.children.keys.include?(word[0])
      move = move_node(word, current_node)
      suggest(move['word'], move['node'])
    else
      #alter existing word to move to next word in the tree

      split_word = word.split('')
      new_word = (current_node.name + split_word.shift).delete(' ')
      next_node = current_node.children[new_word]
      next_word = split_word.join
      suggest(next_word, next_node)
    end
  end

  def move_node(word, current_node)
    split_word = word.split('')
    next_node = current_node.children[split_word[0]]
    split_word.shift
    new_word = split_word.join
    {"word" => new_word, "node" => next_node}
  end

  def populate(source)
    words = source.split("\n")
    words.each do |word|
      insert(word)
    end
  end
end
