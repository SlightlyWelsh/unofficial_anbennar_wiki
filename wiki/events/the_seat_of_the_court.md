#Information
 - Title: The Seat of the Court
 - ID: jadd_empire.1
#Description
The Seat of the Court
#Options

___
##The Court shall remain where it is.

###Available if:
<li>any owned province:</li><ul><li>has province modifier jaddempire_court_seat</li></ul>

###Efects:<ul><li>capital scope:</li><ul><li>trigger switch:</li><ul><li>on trigger = province_id</li><li>8:</li><ul><li>ROOT:</li><ul><li>add ruler modifier:</li><ul><li>name = jaddempire_anbenncost_capital</li><li>duration = -1</li></ul><li>jaddempire change leaning west massive = yes</li></ul></ul><li>565:</li><ul><li>ROOT:</li><ul><li>add ruler modifier:</li><ul><li>name = jaddempire_brasan_capital</li><li>duration = -1</li></ul><li>jaddempire change leaning west large = yes</li></ul></ul><li>601:</li><ul><li>ROOT:</li><ul><li>add ruler modifier:</li><ul><li>name = jaddempire_bulwar_capital</li><li>duration = -1</li></ul><li>jaddempire change leaning west medium = yes</li></ul></ul><li>625:</li><ul><li>ROOT:</li><ul><li>add ruler modifier:</li><ul><li>name = jaddempire_jaddanzar_capital</li><li>duration = -1</li></ul><li>jaddempire change leaning west medium = yes</li></ul></ul><li>643:</li><ul><li>ROOT:</li><ul><li>add ruler modifier:</li><ul><li>name = jaddempire_azka_sur_capital</li><li>duration = -1</li></ul><li>jaddempire change leaning west small = yes</li></ul></ul><li>2909:</li><ul><li>ROOT:</li><ul><li>add ruler modifier:</li><ul><li>name = jaddempire_religious_capital</li><li>duration = -1</li></ul></ul></ul><li>4411:</li><ul><li>ROOT:</li><ul><li>add ruler modifier:</li><ul><li>name = jaddempire_dhenijansar_capital</li><li>duration = -1</li></ul><li>jaddempire change leaning east medium = yes</li></ul></ul><li>4420:</li><ul><li>ROOT:</li><ul><li>add ruler modifier:</li><ul><li>name = jaddempire_sramaya_capital</li><li>duration = -1</li></ul><li>jaddempire change leaning east medium = yes</li></ul></ul><li>4500:</li><ul><li>ROOT:</li><ul><li>add ruler modifier:</li><ul><li>name = jaddempire_aizt_ralare_capital</li><li>duration = -1</li></ul><li>jaddempire change leaning east large = yes</li></ul></ul><li>4871:</li><ul><li>ROOT:</li><ul><li>add ruler modifier:</li><ul><li>name = jaddempire_tianlou_capital</li><li>duration = -1</li></ul><li>jaddempire change leaning east massive = yes</li></ul></ul></ul></ul><li>add stability = -1</li></ul>

___
##Azka-Sur seems a good choice.

###Available if:
<li>None of the following:</li><ul><li>643:</li><ul><li>has province modifier jaddempire_court_seat</li></ul></ul><li>owns core province 643</li><li>643:</li><ul><li>controlled by is this nation</li></ul>

###Efects:<ul><li>goto = 643</li><li>If does not have capital is 643:</li><ul><li>jaddempire move court minorities from to:</li><ul><li>from = capital_scope</li><li>province id = 643</li></ul></ul><li>jaddempire move court:</li><ul><li>province id = 643</li></ul><li>If azka sur area has owned by is ROOT, and does not have province modifier is jaddempire court seat:</li><ul><li>add province modifier:</li><ul><li>name = jaddempire_court_area</li><li>duration = -1</li></ul></ul></ul>

___
##Bulwar would be perfect.

###Available if:
<li>None of the following:</li><ul><li>601:</li><ul><li>has province modifier jaddempire_court_seat</li></ul></ul><li>owns core province 601</li><li>601:</li><ul><li>controlled by is this nation</li></ul>

###Efects:<ul><li>goto = 601</li><li>If does not have capital is 601:</li><ul><li>jaddempire move court minorities from to:</li><ul><li>from = capital_scope</li><li>province id = 601</li></ul></ul><li>jaddempire move court:</li><ul><li>province id = 601</li></ul><li>If bulwar area has owned by is ROOT, and does not have province modifier is jaddempire court seat:</li><ul><li>add province modifier:</li><ul><li>name = jaddempire_court_area</li><li>duration = -1</li></ul></ul></ul>

___
##The Mountain of Clear Sight should be our seat.

###Available if:
<li>None of the following:</li><ul><li>2909:</li><ul><li>has province modifier jaddempire_court_seat</li></ul></ul><li>owns core province 2909</li><li>2909:</li><ul><li>controlled by is this nation</li></ul>

###Efects:<ul><li>goto = 2909</li><li>If does not have capital is 2909:</li><ul><li>jaddempire move court minorities from to:</li><ul><li>from = capital_scope</li><li>province id = 2909</li></ul></ul><li>jaddempire move court:</li><ul><li>province id = 2909</li></ul><li>If far east salahad area has owned by is ROOT, and does not have province modifier is jaddempire court seat:</li><ul><li>add province modifier:</li><ul><li>name = jaddempire_court_area</li><li>duration = -1</li></ul></ul></ul>

___
##Brasan is perfectly situated.

###Available if:
<li>None of the following:</li><ul><li>565:</li><ul><li>has province modifier jaddempire_court_seat</li></ul></ul><li>owns core province 565</li><li>565:</li><ul><li>controlled by is this nation</li></ul>

###Efects:<ul><li>goto = 565</li><li>If does not have capital is 565:</li><ul><li>jaddempire move court minorities from to:</li><ul><li>from = capital_scope</li><li>province id = 565</li></ul></ul><li>jaddempire move court:</li><ul><li>province id = 565</li></ul><li>If lower brasan area has owned by is ROOT, and does not have province modifier is jaddempire court seat:</li><ul><li>add province modifier:</li><ul><li>name = jaddempire_court_area</li><li>duration = -1</li></ul></ul></ul>

___
##Anbenncóst, the world's desire is ours.

###Available if:
<li>None of the following:</li><ul><li>8:</li><ul><li>has province modifier jaddempire_court_seat</li></ul></ul><li>owns core province 8</li><li>8:</li><ul><li>controlled by is this nation</li></ul>

###Efects:<ul><li>goto = 8</li><li>If does not have capital is 8:</li><ul><li>jaddempire move court minorities from to:</li><ul><li>from = capital_scope</li><li>province id = 8</li></ul></ul><li>jaddempire move court:</li><ul><li>province id = 8</li></ul><li>If east damesear area has owned by is ROOT, and does not have province modifier is jaddempire court seat:</li><ul><li>add province modifier:</li><ul><li>name = jaddempire_court_area</li><li>duration = -1</li></ul></ul></ul>

___
##Dhenijansar holds the imperial expertise of many ages.

###Available if:
<li>None of the following:</li><ul><li>4411:</li><ul><li>has province modifier jaddempire_court_seat</li></ul></ul><li>owns core province 4411</li><li>4411:</li><ul><li>controlled by is this nation</li></ul>

###Efects:<ul><li>goto = 4411</li><li>If does not have capital is 4411:</li><ul><li>jaddempire move court minorities from to:</li><ul><li>from = capital_scope</li><li>province id = 4411</li></ul></ul><li>jaddempire move court:</li><ul><li>province id = 4411</li></ul><li>If inner rahen area has owned by is ROOT, and does not have province modifier is jaddempire court seat:</li><ul><li>add province modifier:</li><ul><li>name = jaddempire_court_area</li><li>duration = -1</li></ul></ul></ul>

___
##Sramaya's location will support our rule.

###Available if:
<li>None of the following:</li><ul><li>4420:</li><ul><li>has province modifier jaddempire_court_seat</li></ul></ul><li>owns core province 4420</li><li>4420:</li><ul><li>controlled by is this nation</li></ul><li>has country flag [deal_with_jyntas_struck](../flags/deal_with_jyntas_struck.md)</li>

###Efects:<ul><li>goto = 4420</li><li>If does not have capital is 4420:</li><ul><li>jaddempire move court minorities from to:</li><ul><li>from = capital_scope</li><li>province id = 4420</li></ul></ul><li>jaddempire move court:</li><ul><li>province id = 4420</li></ul><li>If kharunyana estuary area has owned by is ROOT, and does not have province modifier is jaddempire court seat:</li><ul><li>add province modifier:</li><ul><li>name = jaddempire_court_area</li><li>duration = -1</li></ul></ul></ul>

___
##Aizt Ralare is the heart of Haless and our empire.

###Available if:
<li>None of the following:</li><ul><li>4500:</li><ul><li>has province modifier jaddempire_court_seat</li></ul></ul><li>owns core province 4500</li><li>4500:</li><ul><li>controlled by is this nation</li></ul><li>has country flag [aizt_ralare_founded_flag](../flags/aizt_ralare_founded_flag.md)</li>

###Efects:<ul><li>goto = 4500</li><li>If does not have capital is 4500:</li><ul><li>jaddempire move court minorities from to:</li><ul><li>from = capital_scope</li><li>province id = 4500</li></ul></ul><li>jaddempire move court:</li><ul><li>province id = 4500</li></ul><li>If sarisung area has owned by is ROOT, and does not have province modifier is jaddempire court seat:</li><ul><li>add province modifier:</li><ul><li>name = jaddempire_court_area</li><li>duration = -1</li></ul></ul></ul>

___
##Tianlou holds the secrets that we need.

###Available if:
<li>None of the following:</li><ul><li>4871:</li><ul><li>has province modifier jaddempire_court_seat</li></ul></ul><li>owns core province 4871</li><li>4871:</li><ul><li>controlled by is this nation</li></ul>

###Efects:<ul><li>goto = 4871</li><li>If does not have capital is 4871:</li><ul><li>jaddempire move court minorities from to:</li><ul><li>from = capital_scope</li><li>province id = 4871</li></ul></ul><li>jaddempire move court:</li><ul><li>province id = 4871</li></ul><li>If tianlou area has owned by is ROOT, and does not have province modifier is jaddempire court seat:</li><ul><li>add province modifier:</li><ul><li>name = jaddempire_court_area</li><li>duration = -1</li></ul></ul></ul>

___
##Jaddanzar is our true capital.

###Available if:
<li>None of the following:</li><ul><li>625:</li><ul><li>has province modifier jaddempire_court_seat</li></ul></ul><li>owns core province 625</li><li>625:</li><ul><li>controlled by is this nation</li></ul><li>has country flag [jaddanzar_founded_flag](../flags/jaddanzar_founded_flag.md)</li>

###Efects:<ul><li>goto = 625</li><li>If does not have capital is 625:</li><ul><li>jaddempire move court minorities from to:</li><ul><li>from = capital_scope</li><li>province id = 625</li></ul></ul><li>jaddempire move court:</li><ul><li>province id = 625</li></ul><li>If sareyand area has owned by is ROOT, and does not have province modifier is jaddempire court seat:</li><ul><li>add province modifier:</li><ul><li>name = jaddempire_court_area</li><li>duration = -1</li></ul></ul></ul>
