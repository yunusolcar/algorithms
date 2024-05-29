# Writing a string in reverse
# 1
text = input("Enter a text: ")

reversed = text[::-1]

print(reversed)
# hello my name is gustava fring    ->  gnirf avatsug si eman ym olleh


# 2
def reverse(string):
    reversed_string = ""
    for char in string:
        reversed_string = char + reversed_string
    return reversed_string


my_string = input("Enter a text: ")
reversed = reverse(my_string)
print("reversed text: ", reversed)
# hello my name is gustava fring    ->  gnirf avatsug si eman ym olleh
