# Streamlit UI for "Schedule I", a game where players manage a drug empire.
# This tool helps users explore substances, effects, and strategies.

# #Each substance brings a unique effect to the mix. However, there are set rules that determine how different substances and their effects interact with existing substances and effects.
# When a substance is introduced to a mix: It applies rules based off the substance itself telling which effects to mix into what. After a mix is performed, the default substance adds its own "Default" effect to the mix (if there is space).
# Each "Strain" is only allowed to have up to 8 effects at a time. When a mix is done; and we try to add the default effect, if we are at that limit the default effect is not added.

# Products
# Weed
# Base Price: $35
# Meth
# Base Price: $70
# Cocaine
# Base Price: $150

# Substances that interact with each other:
# Cuke(Energizing) — Weed: ~$43, Meth: ~$85, Cocaine: ~$183
# If Toxic present, then replace Toxic with Euphoric.
# If Slippery present, then replace Slippery with Munchies.
# If Sneaky present, then replace Sneaky with Paranoia.
# If Foggy present, then replace Foggy with Cyclopean.
# If Gingeritis present, then replace Gingeritis with Thought-Provoking.
# If Munchies present, then replace Munchies with Athletic.
# If Euphoric present, then replace Euphoric with Laxative.

# Flu Medicine(Sedating) — Weed: ~$44, Meth: ~$88, Cocaine: ~$189
# If Calming present, then replace Calming with Bright-Eyed.
# If Athletic present, then replace Athletic with Munchies.
# If Thought-Provoking present, then replace Thought-Provoking with Gingeritis.
# If Cyclopean present, then replace Cyclopean with Foggy.
# If Munchies present, then replace Munchies with Slippery.
# If Laxative present, then replace Laxative with Euphoric.
# If Euphoric present, then replace Euphoric with Toxic.
# If Focused present, then replace Focused with Calming.
# If Electrifying present, then replace Electrifying with Refreshing.
# If Shrinking present, then replace Shrinking with Paranoia.

# Gasoline(Toxic) — Weed: ~$35, Meth: ~$70, Cocaine: ~$150
# If Gingeritis present, then replace Gingeritis with Smelly.
# If Jennerising present, then replace Jennerising with Sneaky.
# If Sneaky present, then replace Sneaky with Tropic Thunder.
# If Munchies present, then replace Munchies with Sedating.
# If Energizing present, then replace Energizing with Euphoric.
# If Euphoric present, then replace Euphoric with Energizing.
# If Laxative present, then replace Laxative with Foggy.
# If Disorienting present, then replace Disorienting with Glowing.
# If Paranoia present, then replace Paranoia with Calming.
# If Electrifying present, then replace Electrifying with Disorienting.
# If Shrinking present, then replace Shrinking with Focused.

# Donut(Calorie-Dense) — Weed: ~$45, Meth: ~$90, Cocaine: ~$192
# If Calorie-Dense present, then replace Calorie-Dense with Explosive.
# If Balding present, then replace Balding with Sneaky.
# If Anti-Gravity present, then replace Anti-Gravity with Slippery.
# If Jennerising present, then replace Jennerising with Gingeritis.
# If Focused present, then replace Focused with Euphoric.
# If Shrinking present, then replace Shrinking with Energizing.

# Energy Drink(Athletic) — Weed: ~$46, Meth: ~$92, Cocaine: ~$198
# If Sedating present, then replace Sedating with Munchies.
# If Euphoric present, then replace Euphoric with Energizing.
# If Spicy present, then replace Spicy with Euphoric.
# If Tropic Thunder present, then replace Tropic Thunder with Sneaky.
# If Glowing present, then replace Glowing with Disorienting.
# If Foggy present, then replace Foggy with Laxative.
# If Disorienting present, then replace Disorienting with Electrifying.
# If Schizophrenia present, then replace Schizophrenia with Balding.
# If Focused present, then replace Focused with Shrinking.

# Mouth Wash(Balding) — Weed: ~$46, Meth: ~$91, Cocaine: ~$195
# If Calming present, then replace Calming with Anti-Gravity.
# If Calorie-Dense present, then replace Calorie-Dense with Sneaky.
# If Explosive present, then replace Explosive with Sedating.
# If Focused present, then replace Focused with Jennerising.

# Motor Oil(Slippery) — Weed: ~$47, Meth: ~$94, Cocaine: ~$201
# If Energizing present, then replace Energizing with Munchies.
# If Foggy present, then replace Foggy with Toxic.
# If Euphoric present, then replace Euphoric with Sedating.
# If Paranoia present, then replace Paranoia with Anti-Gravity.
# If Munchies present, then replace Munchies with Schizophrenia.

# Banana(Gingeritis) — Weed: ~$42, Meth: ~$84, Cocaine: ~$180
# If Energizing present, then replace Energizing with Thought-Provoking.
# If Calming present, then replace Calming with Sneaky.
# If Toxic present, then replace Toxic with Smelly.
# If Long Faced present, then replace Long Faced with Refreshing.
# If Cyclopean present, then replace Cyclopean with Thought-Provoking.
# If Disorienting present, then replace Disorienting with Focused.
# If Focused present, then replace Focused with Seizure-Inducing.
# If Paranoia present, then replace Paranoia with Jennerising.
# If Smelly present, then replace Smelly with Anti-Gravity.

# Chili(Spicy) — Weed: ~$48, Meth: ~$97, Cocaine: ~$207
# If Athletic present, then replace Athletic with Euphoric.
# If Anti-Gravity present, then replace Anti-Gravity with Tropic Thunder.
# If Sneaky present, then replace Sneaky with Bright-Eyed.
# If Munchies present, then replace Munchies with Toxic.
# If Laxative present, then replace Laxative with Long Faced.
# If Shrinking present, then replace Shrinking with Refreshing.

# Iodine(Jennerising) — Weed: ~$50, Meth: ~$99, Cocaine: ~$213
# If Calming present, then replace Calming with Balding.
# If Toxic present, then replace Toxic with Sneaky.
# If Foggy present, then replace Foggy with Paranoia.
# If Calorie-Dense present, then replace Calorie-Dense with Gingeritis.
# If Euphoric present, then replace Euphoric with Seizure-Inducing.
# If Refreshing present, then replace Refreshing with Thought-Provoking.

# Paracetamol(Sneaky) — Weed: ~$43, Meth: ~$87, Cocaine: ~$186
# If Energizing present, then replace Energizing with Paranoia.
# If Calming present, then replace Calming with Slippery.
# If Toxic present, then replace Toxic with Tropic Thunder.
# If Spicy present, then replace Spicy with Bright-Eyed.
# If Glowing present, then replace Glowing with Toxic.
# If Foggy present, then replace Foggy with Calming.
# If Munchies present, then replace Munchies with Anti-Gravity.
# If Electrifying present, then replace Electrifying with Athletic.
# If Paranoia present, then replace Paranoia with Balding.
# If Focused present, then replace Focused with Gingeritis.

# Viagra(Tropic Thunder) — Weed: ~$51, Meth: ~$102, Cocaine: ~$219
# If Athletic present, then replace Athletic with Sneaky.
# If Euphoric present, then replace Euphoric with Bright-Eyed.
# If Laxative present, then replace Laxative with Calming.
# If Disorienting present, then replace Disorienting with Toxic.

# Horse Semen(Long Faced) — Weed: ~$53, Meth: ~$106, Cocaine: ~$228
# If Anti-Gravity present, then replace Anti-Gravity with Calming.
# If Gingeritis present, then replace Gingeritis with Refreshing.
# If Thought-Provoking present, then replace Thought-Provoking with Electrifying.

# Mega Bean(Foggy) — Weed: ~$48, Meth: ~$95, Cocaine: ~$204
# If Energizing present, then replace Energizing with Cyclopean.
# If Calming present, then replace Calming with Glowing.
# If Sneaky present, then replace Sneaky with Calming.
# If Jennerising present, then replace Jennerising with Paranoia.
# If Athletic present, then replace Athletic with Laxative.
# If Slippery present, then replace Slippery with Toxic.
# If Thought-Provoking present, then replace Thought-Provoking with Energizing.
# If Seizure-Inducing present, then replace Seizure-Inducing with Focused.
# If Focused present, then replace Focused with Disorienting.
# If Sneaky present, then replace Sneaky with Glowing.
# If Thought-Provoking present, then replace Thought-Provoking with Cyclopean.
# If Shrinking present, then replace Shrinking with Electrifying.

# Addy(Thought-Provoking) — Weed: ~$50, Meth: ~$101, Cocaine: ~$216
# If Sedating present, then replace Sedating with Gingeritis.
# If Long Faced present, then replace Long Faced with Electrifying.
# If Glowing present, then replace Glowing with Refreshing.
# If Foggy present, then replace Foggy with Energizing.
# If Explosive present, then replace Explosive with Euphoric.

# Battery(Bright-Eyed) — Weed: ~$49, Meth: ~$98, Cocaine: ~$210
# If Munchies present, then replace Munchies with Tropic Thunder.
# If Euphoric present, then replace Euphoric with Zombifying.
# If Electrifying present, then replace Electrifying with Euphoric.
# If Laxative present, then replace Laxative with Calorie-Dense.
# If Cyclopean present, then replace Cyclopean with Glowing.
# If Shrinking present, then replace Shrinking with Munchies.
