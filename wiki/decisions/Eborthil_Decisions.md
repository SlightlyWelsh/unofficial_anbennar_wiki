This is a list of all [decisions](decisions.md) in the category "Eborthil_Decisions"

| Decision | Completion requirements | Effects | Requirements to appear |
| ----- | ------ | ----- | ------ |
| <a name="show_defensive_improvements">Show Defensive Improvements</a><br />*Show Defensive Improvements* | <li>owns core province 35</li><li>owns core province  36</li><li>owns core province   369</li><li>owns core province    379</li><li>owns core province     380</li> | <li>set country flag [show_defensive_improvements](../flags/show_defensive_improvements.md)</li> | <li>Country is Eborthil</li><li>has country flag [eborthil_reinforce_the_home_isles](../flags/eborthil_reinforce_the_home_isles.md)</li><li>None of the following:</li><ul><li>has country flag [show_defensive_improvements](../flags/show_defensive_improvements.md)</li></ul><li>NOT:</li><ul><li>All of the following:</li><ul><li>has country flag [tefori_protection](../flags/tefori_protection.md)</li><li>has country flag  space_cleared_out</li><li>has country flag   delian_battery</li><li>has country flag    tower_of_tef</li><li>has country flag     tunnel_systems</li><li>has country flag      toref_citadel</li></ul></ul> |
| <a name="hide_defensive_improvements">Hide Defensive Improvements</a><br />*Hide Defensive Improvements* | <li>always</li> | <li>clr country flag [show_defensive_improvements](../flags/show_defensive_improvements.md)</li> | <li>is not controlled by the AI</li><li>Country is Eborthil</li><li>has country flag [show_defensive_improvements](../flags/show_defensive_improvements.md)</li><li>None of the following:</li><ul><li>All of the following:</li><ul><li>has country flag [tefori_protection](../flags/tefori_protection.md)</li><li>has country flag  space_cleared_out</li><li>has country flag   delian_battery</li><li>has country flag    tower_of_tef</li><li>has country flag     tunnel_systems</li><li>has country flag      toref_citadel</li></ul></ul> |
| <a name="the_first_line">The First Line</a><br />*The first, and arguably main, defense of our nation is none other than the navy itself. As long as a ship stands, our shores shall remain untouched. §YUnlocks Wooden Wall Naval Doctrine§!* | <li>dip power is at least 50</li> | <li>add dip power = -50</li><li>set country flag [tefori_protection](../flags/tefori_protection.md)</li> | <li>Country is Eborthil</li><li>has country flag [show_defensive_improvements](../flags/show_defensive_improvements.md)</li><li>None of the following:</li><ul><li>has country flag [tefori_protection](../flags/tefori_protection.md)</li></ul> |
| <a name="clear_out_space">Clear out Space</a><br />*Our island only has so much usable space, before we engage in any large scale projects we will need to manually open land for use, this could also bring about economic benefits.* | <li>treasury is at least 200</li><li>owns core province 35</li><li>owns core province  36</li><li>owns core province   369</li><li>owns core province    379</li><li>owns core province     380</li> | <li>add treasury = -200</li><li>isle of tef area:</li><ul><li>add province modifier:</li><ul><li>name = eborthil_space_cleared_out</li><li>duration = -1</li></ul></ul><li>set country flag [space_cleared_out](../flags/space_cleared_out.md)</li> | <li>Country is Eborthil</li><li>has country flag [show_defensive_improvements](../flags/show_defensive_improvements.md)</li><li>None of the following:</li><ul><li>has country flag [space_cleared_out](../flags/space_cleared_out.md)</li></ul> |
| <a name="the_delian_battery">The Delian Battery</a><br />*During the Lilac Wars Delian II made devastating use of cannons against the Busilari navy, shredding the once proud Lion Armada. We can replicate this and make a stationary set of artillery to protect our northern shores from future invasions.* | <li>mil tech is at least 5</li><li>treasury is at least 100</li><li>owns core province 35</li><li>owns core province  379</li><li>owns core province   380</li> | <li>add treasury = -100</li><li>35:</li><ul><li>add building = coastal_defence</li></ul><li>379:</li><ul><li>add building = coastal_defence</li></ul><li>380:</li><ul><li>add building = coastal_defence</li></ul><li>set country flag [delian_battery](../flags/delian_battery.md)</li> | <li>Country is Eborthil</li><li>has country flag [show_defensive_improvements](../flags/show_defensive_improvements.md)</li><li>has country flag  space_cleared_out</li><li>None of the following:</li><ul><li>has country flag [delian_battery](../flags/delian_battery.md)</li></ul> |
| <a name="tower_of_tef">Construct the Tower of Tef</a><br />*New Tefkora is our most notable island besides the Isle of Tef and, should our navy fall, it'll need to fend for itself. A great fortress where the population can go to during times of crisis will be erected, it will also count on an extremely tall tower, capable of overseeing the entire isle and acting as a guide for ships when necessary.* | <li>treasury is at least 200</li><li>owns core province 36</li> | <li>add treasury = -200</li><li>36:</li><ul><li>add province modifier:</li><ul><li>name = eborthil_tower_of_tef</li><li>duration = -1</li></ul></ul><li>set country flag [tower_of_tef](../flags/tower_of_tef.md)</li> | <li>Country is Eborthil</li><li>has country flag [show_defensive_improvements](../flags/show_defensive_improvements.md)</li><li>has country flag  space_cleared_out</li><li>None of the following:</li><ul><li>has country flag [tower_of_tef](../flags/tower_of_tef.md)</li></ul> |
| <a name="tunnel_systems">Dig Tunnel Systems</a><br />*Our people have mined the hills that span the Isle of Tef for uncountable generations. We could repurpose many of these ancient tunnels to use as strategic devices, concealing the movement of allied troops and allowing us to harass enemies.* | <li>treasury is at least 200</li><li>owns core province 35</li><li>owns core province  369</li><li>owns core province   379</li><li>owns core province    380</li> | <li>add treasury = -200</li><li>35:</li><ul><li>add province modifier:</li><ul><li>name = eborthil_defensive_tunnels</li><li>duration = -1</li></ul></ul><li>369:</li><ul><li>add province modifier:</li><ul><li>name = eborthil_defensive_tunnels</li><li>duration = -1</li></ul></ul><li>379:</li><ul><li>add province modifier:</li><ul><li>name = eborthil_defensive_tunnels</li><li>duration = -1</li></ul></ul><li>380:</li><ul><li>add province modifier:</li><ul><li>name = eborthil_defensive_tunnels</li><li>duration = -1</li></ul></ul><li>set country flag [tunnel_systems](../flags/tunnel_systems.md)</li> | <li>Country is Eborthil</li><li>has country flag [show_defensive_improvements](../flags/show_defensive_improvements.md)</li><li>has country flag  space_cleared_out</li><li>None of the following:</li><ul><li>has country flag [tunnel_systems](../flags/tunnel_systems.md)</li></ul> |
| <a name="toref_citadel">Renovate the Toref Citadel</a><br />*The Toref Citadel is said to be the single oldest construction in our island, built initially by the Kheteratans thousands of years ago and being expanded by the various successor states. With some modernization it'll serve as the central command of our armies, historically ignored in favour of the navy.* | <li>treasury is at least 200</li><li>owns core province 35</li> | <li>add treasury = -200</li><li>35:</li><ul><li>add province modifier:</li><ul><li>name = eborthil_modern_citadel</li><li>duration = -1</li></ul></ul><li>set country flag [toref_citadel](../flags/toref_citadel.md)</li> | <li>Country is Eborthil</li><li>has country flag [show_defensive_improvements](../flags/show_defensive_improvements.md)</li><li>has country flag  space_cleared_out</li><li>None of the following:</li><ul><li>has country flag [toref_citadel](../flags/toref_citadel.md)</li></ul> |
