"""A lesson on continue and break."""

shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

# for item in shopping_list:
#     if item != "spam":
#         print("Buy {}".format(item))

for item in shopping_list:
    if item == 'spam':
        # break
        continue
    print("Buy " + item)
