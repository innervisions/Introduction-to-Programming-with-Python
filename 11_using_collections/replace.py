info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
# info = '+'.join(info.split(':'))
info = info.replace(':', '+')
print(info)
