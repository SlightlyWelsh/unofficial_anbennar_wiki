#Information
 - Title: Domandrod over Deepwoods
 - ID: eordand.40
#Description
Domandrod over Deepwoods
#Options

___
##It is time to unify the Deepwoods under Cyranvar, for they cannot protect it themselves.

###Available if:
<li>None of the following:</li><ul><li>exists is Cyranvar</li></ul>

###Efects:<ul><li>I45:</li><ul><li>inherit = I26</li><li>inherit = I27</li><li>inherit = I28</li><li>inherit = I29</li><li>inherit = I30</li><li>inherit = I31</li><li>inherit = I32</li><li>inherit = I33</li><li>inherit = I34</li><li>add trust:</li><ul><li>who = ROOT</li><li>value = 25</li><li>mutual = yes</li></ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = eord_reformed_cyranvar</li></ul><li>reverse add opinion:</li><ul><li>who = ROOT</li><li>modifier = eord_reformed_cyranvar</li></ul><li>largest increase of ruinborn tolerance effect = yes</li></ul><li>vassalize = I45</li></ul>

___
##Despite their flaws, the clan hierarchy should be maintained to ensure loyalty and security.

###Available if:
<li>None of the following:</li><ul><li>exists is Cyranvar</li></ul>

###Efects:<ul><li>If every subject country has culture is wood elf:</li><ul><li>country gets the modifier eord_evergreen_march until otherwise removed</li></ul></ul>

___
##The Evergreen Pact has been fulfilled, but it need not end. Let this only be the beginning of the cooperation between the Deepwoods and Domandrod!

###Available if:
<li>exists is Cyranvar</li>

###Efects:<ul><li>I45:</li><ul><li>add trust:</li><ul><li>who = ROOT</li><li>value = 25</li><li>mutual = yes</li></ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = eord_preserved_evergreen_pact</li></ul><li>reverse add opinion:</li><ul><li>who = ROOT</li><li>modifier = eord_preserved_evergreen_pact</li></ul></ul><li>country gets the modifier eord_sylvan_unity until otherwise removed</li><li>largest increase of elven tolerance effect = yes</li></ul>

___
##It is clear to us - The Wood Elves depend on us, they cannot stand on their own. They must answer to us, not just listen.

###Available if:
<li>exists is Cyranvar</li>

###Efects:<ul><li>declare war with cb:</li><ul><li>who = I45</li><li>casus belli = cb_restore_personal_union</li></ul><li>reverse add opinion:</li><ul><li>who = I45</li><li>modifier = eord_evergreen_betrayal_opinion</li></ul><li>country gets the modifier eord_evergreen_betrayal until otherwise removed</li></ul>
