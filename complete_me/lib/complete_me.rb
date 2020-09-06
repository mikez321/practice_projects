require './lib/node'

class CompleteMe
  attr_reader :root

  def initialize
    @root = Node.new(" ")
    @word_count = 0
  end

  def insert(word, current_node = @root, original_word = word)
    if current_node.word?
      new_node = Node.new(current_node.name)
      new_node.word = true
      current_node.add(new_node)
      current_node.word = false
    elsif
      word == ""
      if current_node.leaf?
        current_node.word = true
        @word_count += 1
        "added new word #{current_node.name}"
      else
        new_node = Node.new(current_node.name)
        new_node.word = true
        current_node.add(new_node)
        @word_count += 1
        "added new word #{current_node.name}"
      end
    elsif
      current_node.children.keys.include?((current_node.name + word[0]).strip)
      current_node = current_node.children[(current_node.name + word[0]).strip]
      new_word = drop_first_letter(word)
      insert(new_word, current_node, original_word)
    else
      split_word = word.split('')
      new_name = (current_node.name + split_word.shift).delete(' ')
      new_word = split_word.join
      new_node = Node.new(new_name)
      current_node.add(new_node)
      insert(new_word, new_node, original_word)
    end
    # if current_node.word?
    #   new_node = Node.new(current_node.name)
    #   new_node.word
    #   current_node.add(new_node)
    #
    #   split_word = word.split('')
    #   new_name = (current_node.name + split_word.shift).delete(' ')
    #   new_node = Node.new(new_name)
    #   current_node.add(new_node)
    #   new_word = split_word.join
    #   insert(new_word, new_node, original_word)
    # elsif
    #   word == "" && !current_node.leaf?
    #   new_node = Node.new(current_node.name)
    #   new_node.word
    #   current_node.add(new_node)
    #   @word_count += 1
    #   "added new word #{new_node.name}"
    # elsif
    #   current_node.name == original_word && word == ""
    #   current_node.word
    #   @word_count += 1
    #   "added new word #{current_node.name}"
    # elsif
    #   current_node.children.keys.include?((current_node.name + word[0]).strip)
    #   split_word = word.split('')
    #   current_node = current_node.children[(current_node.name + word[0]).strip]
    #   split_word.shift
    #   new_word = split_word.join
    #   insert(new_word, current_node, original_word)
    # else
    #   split_word = word.split('')
    #   new_name = (current_node.name + split_word.shift).delete(' ')
    #   new_node = Node.new(new_name)
    #   current_node.add(new_node)
    #   new_word = split_word.join
    #   insert(new_word, new_node, original_word)
    # end
  end

  def count
    @word_count
  end

  def suggest(string, current_node = @root)
    if string == ""
      #return all words under final node

      current_node.all_words
    elsif
      current_node.children.keys.include?(string[0])
      split_string = string.split('')
      next_node = current_node.children[split_string[0]]
      split_string.shift
      new_string = split_string.join
      suggest(new_string, next_node)
    else
      split_string = string.split('')
      new_string = (current_node.name + split_string.shift).delete(' ')
      next_node = current_node.children[new_string]
      next_string = split_string.join
      suggest(next_string, next_node)
    end
  end

  def populate(source)
    words = source.split("\n")
    words.each do |word|
      insert(word)
    end
  end

  def drop_first_letter(word)
    split = word.split('')
    split.shift
    split.join('')
  end
end
