# Given a string s and a character c, return the number of occurrences of c in s.
# Ex: num_chars('oh heavens', 'h')
# => 2

def num_chars(phrase, letter)
  counter = 0
  split_phrase = phrase.split('')
  matches = split_phrase.map do |phrase_letter|
    phrase_letter == letter
  end
  matches.each do |result|
    counter += 1 if result == true
  end
  print counter
end


num_chars('she sells seashells down by the seashore', 's')
