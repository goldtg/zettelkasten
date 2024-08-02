# import re

# #html코드 삭제
# def clean_html(raw_html):
#   cleanr = re.compile('<.*?>')
#   cleantext = re.sub(cleanr, '', raw_html)
#   return cleantext


# #문서 본문 없는 경우 건너뜀
# def WikiDocumentSentences(out, id, title, tags, text):
#     header = '\n{0}{1}'.format(title, "|||".join(tags))
#     text = clean(text)

#     if text.isspace() or len(compact(text,structure=False))==0:
#         return
#     out.reserve(len(header) + len(text))
#     print(header, file=out)
#     for line in compact(text, structure=False):
#         print(line, file=out)




