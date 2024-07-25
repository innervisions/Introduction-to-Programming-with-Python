def all_caps(string):
    return (string.upper() if len(string) > 10 else string)

print(all_caps('hello world'))
print(all_caps('goodbye'))
print(all_caps("Sue Smith"))     # Sue Smith
print(all_caps("Sue Roberts"))   # SUE ROBERTS
print(all_caps("Joe Shea"))      # Joe Shea
print(all_caps("Joe Stevens"))   # JOE STEVENS
