from Util import *
from TemplateClasses import Crate

cratesInfo = convert_csv_to_dict("IMLCrateInfo - Crates.csv")

for crate in cratesInfo:
    curCrate = Crate.Crate(crate)
    curCrateYML = convert_dict_to_yaml(curCrate.dict)
    curFileName = f"Crates/{curCrate.CrateName[2:].replace(' ','')}.yml"
    with open(curFileName, "w") as outfile:
        yaml.dump(curCrate.dict, outfile, sort_keys=False)



