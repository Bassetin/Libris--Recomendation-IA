from lightfm import LightFM
from lightfm.data import Dataset

def criar_modelo():
    dataset = Dataset()
    dataset.fit(users=['lucas'], items=['harry potter', 'senhor dos aneis'])
    interacoes,  = dataset.buildinteractions([('lucas', 'harry potter')])
    modelo = LightFM(loss='warp')
    modelo.fit(interacoes, epochs=10)
    return modelo
