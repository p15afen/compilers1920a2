import re

# anoigma testpage arxeiou kai ekxorisi sti metavliti text
with open('testpage.txt','r',encoding='utf-8') as fp: 
  text = fp.read()

# vima 1 eksagogi kai ektiposi titlou
rexp1 = re.compile(r'<title>(.+?)</title>')
  m = repx.search(text)
    print(m.group(0))

#vima 2 apalifi sxolion
rexp2 = re.compile(r'<!.*?>',re.DOTALL)
  text1 = repx2.sub('', text)

#vima 3 apalifi script kai style
rexp3 = re.compile(r'(<script.+?</script>)|(<style.+?</style>)')
  text2 = repx3.sub('',text1)


#vima 4 eksagogi kai ektiposi href apo <a>
repx4 = re.compile(r"<a(.+?)</a>',re.DOTALL)
  for m in repx4.finditer(text2):
    print(m.group(0))

#vima 5 apalifi tags
repx5 = re.compile(r'<.+?>')
  text3 = repx5.sub('', text2)

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
  text4 = rexp6.sub(func,text3) 
                   
# vima 7 metatropi sinexomenon xaraktiron whitespace se ena keno                   
rexp7 = re.compile(r'\s+') 
  text5 = rexp7.sub(' ',text4)
                   
# vima 8 ektiposi telikou keimenou meta apo tis epeksergasies                   
print(text5)                   
