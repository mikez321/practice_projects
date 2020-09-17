"""Use a break statement for finding items in a list."""

# If you're searching for something in a big list, you'll stop
# searching once you've found it.  So that's a good use case
# for a break!

shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

item_to_find = 'albatross'
found_at = None

# we will use the len() function which is the length of our list
for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        # a break isn't 100% needed but it will stop the method from continuing
        break

if found_at:
    print("Item found at position {}".format(found_at))
else:
    print("{} was not found in the list.".format(item_to_find))
