def getDefaultCrateString(crateName):
    return f"{crateName}Crate,QuickCrate,&e{crateName} Crate,&e{crateName} Crate,0,10,FALSE,14,TRUE,%prefix%&6&l%player%&r &7is opening a &e&l{crateName} Crate&7.,CHEST,FALSE,&e&l{crateName} Crate,&7This crate contains some awesome items!!!\\n&7You have &6%Keys% keys &7to open this crate with.\\n&7&l(&e&l!&7&l) Right click to view rewards.,TRUE,6,TRUE,,ORANGE_STAINED_GLASS,&e&lC++ Crate &c&lKey,&7A {crateName} Key\\n&7For a {crateName} Crate.,TRIPWIRE_HOOK,TRUE,TRUE,1.5,&e&l{crateName} Crate"

print(getDefaultCrateString("Lotto"))