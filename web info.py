import builtwith

q="\[\"\[\033[1;33m\]" # Yellow Yellow
print (q)


url=input ("enter your target")

info = builtwith.parse("https://"+url)

print (info)