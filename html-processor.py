import re

# anoigma testpage arxeiou kai ekxorisi sti metavliti text
with open('testpage.txt','r',encoding='utf-8') as fp: 
  text = fp.read()

# vima 1 eksagogi kai ektiposi titlou
rexp1 = re.compile(r'<title>(.+?)</title>')
m = rexp1.search(text)
print(m.group(0))

#vima 2 apalifi sxolion
rexp2 = re.compile(r'<!.*?>',re.DOTALL)
text = rexp2.sub('',text)

#vima 3 apalifi script kai style
rexp3 = re.compile(r'(<script.+?</script>)|(<style.+?</style>)')
text = rexp3.sub('',text)

#vima 4 eksagogi kai ektiposi href apo <a>
rexp4 = re.compile(r'<a(.+?)</a>',re.DOTALL)
for m in rexp4.finditer(text):
  print(m.group(0))

#vima 5 apalifi tags
rexp5_1 = re.compile(r'<.+?>|</.+?>',re.DOTALL)
rexp5_2 = re.compile(r'<.+?/>',re.DOTALL) 
text = rexp5_1.sub('',text)
text = rexp5_2.sub('',text)

def func(m): #dilosi sinartisis pou metatrepei ola ta html entities simfona me ton pinaka

    if (m.group(0)=='&amp;'):
        return '&'
    elif (m.group(0)=='&gt;'):
        return '>'
    elif (m.group(0)=='&lt;'):
        return '<'
    else:
        return ' '
                   
# vima 6 metatropi ton html entities me xrisi tis sunartisis func              
rexp6 = re.compile(r'&(amp|gt|lt|nbsp);')
text = rexp6.sub(func,text) 
                   
# vima 7 metatropi sinexomenon xaraktiron whitespace se ena keno                   
rexp7 = re.compile(r'\s+') 
text = rexp7.sub(' ',text)
                   
# vima 8 ektiposi telikou keimenou meta apo tis epeksergasies                   
print(text6)                   
