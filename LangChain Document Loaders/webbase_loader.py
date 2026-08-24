from langchain_community.document_loaders import WebBaseLoader

url = 'https://www.alibaba.com/trade/search?spm=a2700.galleryofferlist.the-new-header_fy23_pc_search_bar.keydown__Enter&tab=all&SearchText=alibaba&has4Tab=true&pid=hybrid&xp=Cj0KCQjwxvjRBhC2ARIsAI7KJa0l5Mp2kFpgMDPZICMq_B13uVbrUBdG9lh4HMXxtliNAoy1o1ZwQpIaApUGEALw_wcBsMbeanHAIqwcTEART57S-&cps_sk=q5c7g489&bm=cps&src=saf&pid=hybrid&tp1=Cj0KCQjwxvjRBhC2ARIsAI7KJa0l5Mp2kFpgMDPZICMq_B13uVbrUBdG9lh4HMXxtliNAoy1o1ZwQpIaApUGEALw_wcB.23761783162&gad_source=1'

loader = WebBaseLoader(url)

docs = loader.load()

print(len(docs))

print(docs[0].page_content)