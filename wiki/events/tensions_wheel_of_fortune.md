#Information
 - Title: Tensions Wheel of Fortune
 - ID: new_sun_cult.160
#Description
Tensions Wheel of Fortune
#Options

___
##.

###One of the following randomly happens:
Outcome 1:

Available if <li>None of the following:</li><ul><li>has country flag [nsc_assassination_attempt](../flags/nsc_assassination_attempt.md)</li></ul><li>does not have regency</li>

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>the event [Assassination Attempt](../events/assassination_attempt.md) happens</li></ul>
Outcome 2:

Available if <li>None of the following:</li><ul><li>has country flag [nsc_kidnapping](../flags/nsc_kidnapping.md)</li></ul><li>has heir</li>

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>the event [[Root.Heir.GetTitle] [Root.Heir.GetName] was Kidnapped](../events/root_heir_gettitle_root_heir_getname_was_kidnapped.md) happens</li></ul>
Outcome 3:

The weight of this outcome is 10  
 - Multiplied by 0.02 if has country flag is [nsc_arson](../flags/nsc_arson.md)

This outcome causes the following effects:<ul><li>random owned province:</li><ul><li>fire province event [new_sun_cult.166](new_sun_cult.166_slug) immediately </li></ul></ul>
Outcome 4:

The weight of this outcome is 10   
 - Multiplied by 0.02 if has country flag is [nsc_caravan_raided](../flags/nsc_caravan_raided.md)

This outcome causes the following effects:<ul><li>the event [Caravan Raided](../events/caravan_raided.md) happens</li></ul>
Outcome 5:

The weight of this outcome is 10    
 - Multiplied by 0.01 if has country flag is [nsc_instigated_revolts](../flags/nsc_instigated_revolts.md)

This outcome causes the following effects:<ul><li>random owned province:</li><ul><li>fire province event [new_sun_cult.168](new_sun_cult.168_slug) immediately </li></ul></ul>
Outcome 6:

Available if <li>None of the following:</li><ul><li>check variable:</li><ul><li>which is nscNoTensionEvent</li><li>value is at least 10</li></ul></ul>

The weight of this outcome is 100
 - Multiplied by 0.5 if has check variable has which is nscNoTensionEvent, and check variable has value is 9

The weight of this outcome is 100
 - Multiplied by 0.66 if has check variable has which is nscNoTensionEvent, and check variable has value is 8

The weight of this outcome is 100
 - Multiplied by 0.75 if has check variable has which is nscNoTensionEvent, and check variable has value is 7

The weight of this outcome is 100
 - Multiplied by 0.8 if has check variable has which is nscNoTensionEvent, and check variable has value is 6

The weight of this outcome is 100
 - Multiplied by 0.85 if has check variable has which is nscNoTensionEvent, and check variable has value is 5

The weight of this outcome is 100
 - Multiplied by 0.85 if has check variable has which is nscNoTensionEvent, and check variable has value is 4

The weight of this outcome is 100
 - Multiplied by 0.85 if has check variable has which is nscNoTensionEvent, and check variable has value is 3

The weight of this outcome is 100
 - Multiplied by 0.9 if has check variable has which is nscNoTensionEvent, and check variable has value is 2

The weight of this outcome is 100
 - Multiplied by 0.9 if has check variable has which is nscNoTensionEvent, and check variable has value is 1

The weight of this outcome is 100
 - Multiplied by 0.5 if does not have calc true if has all known country is incident potential is incident summit of samartal; and calc true if has amount is 20

The weight of this outcome is 100
 - Multiplied by 0 if does not have calc true if has all known country is incident potential is incident summit of samartal; and calc true if has amount is 11

The weight of this outcome is 100
 - Multiplied by 0 if is year is 1480

This outcome causes the following effects:<ul><li>change variable:</li><ul><li>which = nscNoTensionEvent</li><li>value = 1</li></ul></ul>
