def find_intersection(strArr)
  result = []
  str1 = strArr.first.split
  str2 = strArr.last.split

  all = str1 + str2
  all = all.map { |item| item.delete(',')}
  all.each do |item|
    if all.count(item) > 1
      result << item
    end
  end

  if result.length.zero?
    false
  else
    result.uniq.join(',')
  end
end


puts find_intersection(["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"])
