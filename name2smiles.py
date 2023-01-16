import pubchempy
import csv

def name_to_smiles(name):

    records = pubchempy.get_compounds(name, 'name')

    if len(records) == 0:
        return 'None'
    if len(records) >1:
        return 'Warning: multiple records found'
    else:
        return records[0].canonical_smiles

input_filename = 'input.csv'
output_filename = 'output.csv'
delimiter = ','
name_col = 'name'
smiles_col = 'SMILES'

input_f = open(input_filename)
output_f = open(output_filename, 'w')

reader = csv.DictReader(input_f, delimiter=delimiter)
writer = csv.DictWriter(output_f, fieldnames=[name_col, smiles_col], delimiter=delimiter)
for row in reader:
    smiles = name_to_smiles(row[name_col])
    name = row[name_col]
    writer.writerow({
        name_col: name,
        smiles_col: smiles
    })

input_f.close()
output_f.close()
    
        
