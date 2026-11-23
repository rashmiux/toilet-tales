import json
s=open('template.html').read()
d=json.load(open('data.json'));r=json.load(open('roads.json'))
j=lambda o:json.dumps(o,ensure_ascii=False,separators=(',',':')).replace('</','<\\/')
open('index.html','w').write(s.replace('__DATA__',j(d)).replace('__ROADS__',j(r)))
