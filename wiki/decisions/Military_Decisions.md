This is a list of all [decisions](decisions.md) in the category "Military_Decisions"

| Decision | Completion requirements | Effects | Requirements to appear |
| ----- | ------ | ----- | ------ |
| <a name="enlist_privateers">Enlist Privateers</a><br />*Commission privateers to disrupt foreign trade by allowing them to pass beyond our country borders in search of enemy vessels or ships belonging to other nations considered untrustworthy.* | <li>navy size percentage is at least 0.5</li><li>full idea group is maritime_ideas</li><li>mil is at least 3</li> | <li>country gets the modifier "hire_privateers" until otherwise removed</li> | <li>None of the following:</li><ul><li>has country modifier hire_privateers</li></ul><li>navy size is at least 1</li><li>has idea group maritime_ideas</li><li>num of ports is at least 1</li><li>dip tech is at least 8</li> |
| <a name="state_firearm_regiments">State Firearm Regiments</a><br />*While the technology is still in its infancy, firearms can be a deadly force on any battlefield. In order to be efficient, however, firearms require regular training and a steady supply of ammunition. For a regular levy army this level of proficiency can be hard to maintain. A soldier that has to go home to tend his fields is not one that will regularly exercise with his weapon.\nWhile we cannot change our entire army structure in one stroke we can ensure that a core of highly trained salaried troops specialize in these weapons.* | <li>mil tech is at least 6</li><li>army professionalism is at least 0.20</li> | <li>custom tooltip = Gives the following modifier until revoked:</li><li>country gets the modifier "gunpowder_core" until otherwise removed</li><li>set country flag [gunpowder_core_activated](../flags/gunpowder_core_activated.md)</li> | <li>has dlc "Cradle of Civilization"</li><li>None of the following:</li><ul><li>has country modifier gunpowder_core</li></ul><li>NOT:</li><ul><li>mil tech is at least 19</li></ul> |
| <a name="abolish_state_firearm_regiments">Abolish our Armed Elite Regiments</a><br />*We are paying far too much for new technology and new methods. We should strive to lift the entire army and not just a few pioneers.* | <li>has country modifier gunpowder_core</li> | <li>add army professionalism = -0.05</li><li>remove country modifier = gunpowder_core</li><li>clr country flag [gunpowder_core_activated](../flags/gunpowder_core_activated.md)</li> | <li>has dlc "Cradle of Civilization"</li><li>has country modifier gunpowder_core</li> |
| <a name="standardized_uniforms">Standardized Uniforms</a><br />*To the extent that uniforms are in use in our armies regiment commanders are often expected to provide and pay for them. This leads to a great variety in colors and styles on the battlefield and makes identifying friend from foe confusing. Let us create a standard uniform for all troops on our payrolls that we then attempt to provide for our troops.* | <li>army professionalism is at least 0.40</li> | <li>custom tooltip = Gives the following modifier until revoked:</li><li>country gets the modifier "standardized_uniforms_modifier" until otherwise removed</li> | <li>has dlc "Cradle of Civilization"</li><li>None of the following:</li><ul><li>has country modifier gunpowder_core</li></ul><li>NOT:</li><ul><li>has country modifier standardized_uniforms_modifier</li></ul><li>mil tech is at least 19</li> |
| <a name="abolish_standardized_uniforms">Abolish Standardized Uniforms</a><br />*There are many upsides to the state supplying standardized uniforms but it is perhaps cheaper and more efficient to have regimental commanders pay and commission them instead. We could go back to the way things were even if our army professionalism would suffer somewhat.* | <li>has country modifier standardized_uniforms_modifier</li> | <li>add army professionalism = -0.05</li><li>remove country modifier = standardized_uniforms_modifier</li> | <li>has dlc "Cradle of Civilization"</li><li>has country modifier standardized_uniforms_modifier</li> |