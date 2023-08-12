from .base_mongo import BaseMongo


class CharacterCollection(BaseMongo):
    def __init__(self):
        super().__init__(db_name='mydb', collection_name='character')
