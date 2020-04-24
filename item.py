class Item():


    def __init__(self,_id,_name,_description,_owned,_sellprice,_itemlevel,_imagedir,_statsdic):


        dic = {'id': _id,
        'name': _name,
        'description': _description,
        'owned': _owned,
        'sellprice': _sellprice,
        'itemlevel': _itemlevel,
        'image': _imagedir,
        'stats': _statsdic
        }

        self.dic = dic



    def add_to_inventory(self,inventory_dic,savedir=""):

        # On trie l'inventaire par id
        inventory_dic['itemlist'] = sorted(inventory_dic['itemlist'], key = lambda x: x['id'])

        if savedir != "":
            import json_manager as jm

            jm.save_file(inventory_dic,fulldir=savedir)

