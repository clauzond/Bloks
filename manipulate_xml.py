# Module à installer : xmltodict
import xmltodict
import json
import os


_a_ = "img/stock/_tiles/Tiled software/my_first_map.tmx"
_a2_ = "img/stock/_tiles/Tiled software/bloks.tsx"
_b_ = "img/stock/_tiles/Tiled software/p.json"

def xml_to_json(opendir,savedir="",action="save"):
    with open(opendir,mode='r',encoding='utf-8-sig') as xml_file:
        my_dict = xmltodict.parse(xml_file.read())
    xml_file.close()


    if action=="save":
        directory = "/".join(savedir.split('/')[:-1])
        if not os.path.exists(directory):
            os.mkdir(directory)
        f = open(savedir,'w+',encoding='utf-8-sig')
        data = json.dump(my_dict,f,ensure_ascii=False)
        f.close()



def convert_all():
    xml_to_json(_a_,"img/stock/_tiles/Tiled software/map.json",action="save")
    xml_to_json(_a2_,"img/stock/_tiles/Tiled software/bloks.json",action="save")