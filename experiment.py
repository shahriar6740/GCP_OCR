
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

l1 = ['GAU', 'CAPORAL', 'NE', '2O CIGARETTLE', 'SENIOR', 'SERVICE', 'GAULOISES', 'in', '10', 'Embassy', 'Dark Drive', 'Marlhuro', 'SILK', 'CUT', 'SUIL', 'Extra Mild', 'NELSON', "PLAYER'S", 'FILTER VIRGINIA', 'CIGARETTES', 'NUMBER 3', 'NFIO', 'CITANES', 'KIN', '20 CLASS A SARETTES', 'FILTER TIPPED', 'BENSON HEDGES', 'BOUT FILTAE', 'CSPECIAL V', 'INTERNATIONAL', 'ORIGINAL RED', 'alamy', '20', 'LUCKY', 'STRIKE', 'DUNHILL', 'alamy', "PLAYER'S", 'CONSULATE', "AYER'S", 'N6', 'the cegistered t', 'trade mark', 'Ltd. London', 'PLAYE', 'London Paris New York', 'Filter Virginia', 'SOBR/ANIE in COLOUR', 'Special Filler', 'Monthed Fesh', 'Kings', 'BENSON HEDGES', 'CIGARETTES', 'T VIRGINIA', '20', 'SPECIAL VROA', 'SENIOR', 'SERVICE', 'ST MORITZ', 'N°6', 'Dark Drive', 'Rothmans', 'KING SIZE', 'Woodbine', 'CIGARETTES', 'SILK', 'CUT', 'VIRGINIA', 'Cadets', 'BY APPOINTMENT TO HIS ROYAL 1GHNESS', 'THE PRINCE OF THE NETHERLANDS', 'TUMAC TORACCO COMPANYNY', 'SALLANERITO', 'TETER TIPPES', 'FILTER', 'FILTER VIRGINIA', 'BENSONd HEDGES', 'MENTHOL', 'alamy', 'WORLD FAMOUS SINCE 1e90', '- ANS', "PLAYER'S", 'Image ID: G1Y860', 'www.alamy.com', 'ITIR']
l2 = ['Pran', 'CAPoraL', 'Potato', 'Cigarette', 'Memphis', 'Dunhill', 'Woodbine', 'Noodles', 'Menthol', 'Benson Hedges']

text= []
match = []
for i in l1[0:15]:
    text.append(i)
    for j in l2:
        p = fuzz.partial_ratio(i,j)
        print(p)
        if p >=90:
            match.append(i)

print("the text list is: \n", text)
print("\n\nthe match list is: \n", match)


