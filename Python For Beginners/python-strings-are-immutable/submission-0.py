def remove_fourth_character(word: str) -> str:
    first_ = word[:3]
    last_ = word[4:]
    return first_+last_
# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
