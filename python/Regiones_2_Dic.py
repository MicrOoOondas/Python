import os
os.system('cls')
dic_region={'Tarapacá':'Norte',
            'Antofagasta':'Norte',
            'Atacama':'Norte',
            'Coquimbo':'Norte',
            'Valparaíso':'Central',
            'Libertador General Bernardo OHiggins':'Central',
            'Maule':'Central',
            'Biobío':'Central',
            'La Araucanía':'Sur',
            'Los Lagos':'Sur',
            'Aysén del General Carlos Ibáñez del Campo':'Sur',
            'Magallanes y de la Antártica Chilena':'Sur',
            'Metropolitana de Santiago':'Central',
            'Los Ríos':'Sur',
            'Arica y Parinacota':'Norte',
            'Ñuble':'Sur'}
dic_region2={}
for clave in dic_region.keys():
    dic_region2[clave]=dic_region2.get(clave,0)
print(dic_region2)