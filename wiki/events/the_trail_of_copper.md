#Information
 - Title: The Trail of Copper
 - ID: azka_evran.3
#Description
The Trail of Copper
#Options

___
##They will make good use of their new home in the mountains.

###Efects:<ul><li>526:</li><ul><li>add base tax = -3</li><li>add base production = -3</li><li>add base manpower = -3</li><li>change religion = bulwari_sun_cult</li><li>add unrest = 5</li><li>add devastation = 25</li></ul><li>525:</li><ul><li>add base tax = -3</li><li>add base production = -3</li><li>add base manpower = -3</li><li>change religion = bulwari_sun_cult</li><li>add unrest = 5</li><li>add devastation = 25</li></ul><li>2942:</li><ul><li>If is empty:</li><ul><li>If does not have exists is I11:</li><ul><li>change culture = copper_dwarf</li><li>change religion = variable:Root:ovdalTungrReligion</li><li>cede province = I11</li><li>add core = I11</li><li>ROOT:</li><ul><li>create subject:</li><ul><li>subject type = march</li><li>subject = I11</li></ul></ul><li>I11:</li><ul><li>change religion = variable:Root:ovdalTungrReligion</li><li>change primary culture = copper_dwarf</li><li>set ruler religion = variable:Root:ovdalTungrReligion</li><li>set ruler culture = copper_dwarf</li></ul></ul><li>add base tax = 3</li><li>add base production = 3</li><li>add base manpower = 3</li></ul><li>Else if has owned by is ROOT:</li><ul><li>If does not have exists is I11:</li><ul><li>change culture = copper_dwarf</li><li>change religion = variable:Root:ovdalTungrReligion</li><li>cede province = I11</li><li>remove core = ROOT</li><li>add core = I11</li><li>ROOT:</li><ul><li>create subject:</li><ul><li>subject type = march</li><li>subject = I11</li></ul></ul><li>I11:</li><ul><li>change religion = variable:Root:ovdalTungrReligion</li><li>change primary culture = copper_dwarf</li><li>set ruler religion = variable:Root:ovdalTungrReligion</li><li>set ruler culture = copper_dwarf</li></ul></ul><li>add base tax = 6</li><li>add base production = 6</li><li>add base manpower = 6</li></ul><li>else:</li><ul><li>add dwarven minority size effect = yes</li><li>add base tax = 6</li><li>add base production = 6</li><li>add base manpower = 6</li></ul></ul></ul>
