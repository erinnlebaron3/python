


url = '    https://google.com   '

print(url.strip())
answer = https://google.com

#  pretty common reason why you would use strip and a few of the functions that are similar to it



url = '    https://google.com   '

print(url.strip('https://'))
answer = google.com

# lstrip = strip from left
# rstrip = strip from right
# url is variable


url = '    https://google.com   '

print(url.lstrip('https://'))
answer = google.com




url = '    https://google.com   '
url = url.lstrip('https://')
url = url.rstrip('.com')

print(url.capitalize())