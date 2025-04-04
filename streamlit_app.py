# Streamlit UI for "Schedule I", a game where players manage a drug empire.
# This tool helps users explore substances, effects, and strategies.

# #Each substance brings a unique effect to the mix. However, there are set rules that determine how different substances and their effects interact with existing substances and effects.
# When a substance is introduced to a mix: It applies rules based off the substance itself telling which effects to mix into what. After a mix is performed, the default substance adds its own "Default" effect to the mix (if there is space).
# Each "Strain" is only allowed to have up to 8 effects at a time. When a mix is done; and we try to add the default effect, if we are at that limit the default effect is not added.

import streamlit as st

# Base prices for products
BASE_PRICES = {
    "OG Kush": 39,
    "Sour Diesel": 40,
    "Green Crack": 43,
    "Granddaddy Purple": 44,
    "Meth": 70,
    "Cocaine": 150
}

# Effects and their multipliers
EFFECTS = {
    "Anti-Gravity": 0.54,
    "Athletic": 0.32,
    "Balding": 0.30,
    "Bright-Eyed": 0.40,
    "Calming": 0.10,
    "Calorie-Dense": 0.28,
    "Cyclopean": 0.56,
    "Disorienting": 0.00,
    "Electrifying": 0.50,
    "Energizing": 0.22,
    "Euphoric": 0.18,
    "Explosive": 0.00,
    "Focused": 0.16,
    "Foggy": 0.36,
    "Gingeritis": 0.20,
    "Glowing": 0.48,
    "Jennerising": 0.42,
    "Laxative": 0.00,
    "Long Faced": 0.52,
    "Munchies": 0.12,
    "Paranoia": 0.00,
    "Refreshing": 0.14,
    "Schizophrenia": 0.00,
    "Sedating": 0.26,
    "Seizure-Inducing": 0.00,
    "Shrinking": 0.60,
    "Slippery": 0.34,
    "Smelly": 0.00,
    "Sneaky": 0.24,
    "Spicy": 0.38,
    "Thought-Provoking": 0.44,
    "Toxic": 0.00,
    "Tropic Thunder": 0.46,
    "Zombifying": 0.58
}

# Default effects for substances
DEFAULT_EFFECTS = {
    "OG Kush": ["Calming"],
    "Sour Diesel": ["Refreshing"],
    "Green Crack": ["Energizing"],
    "Granddaddy Purple": ["Sedating"],
    "Addy": ["Thought-Provoking"],
    "Banana": ["Gingeritis"],
    "Battery": ["Bright-Eyed"],
    "Chili": ["Spicy"],
    "Cuke": ["Energizing"],
    "Donut": ["Calorie-Dense"],
    "Energy Drink": ["Athletic"],
    "Flu Medicine": ["Sedating"],
    "Gasoline": ["Toxic"],
    "Horse Semen": ["Long Faced"],
    "Iodine": ["Jennerising"],
    "Mega Bean": ["Foggy"],
    "Motor Oil": ["Slippery"],
    "Mouth Wash": ["Balding"],
    "Paracetamol": ["Sneaky"],
    "Viagra": ["Tropic Thunder"]
}

# Rules for each substance
SUBSTANCE_RULES = {
    "Addy": [
        ("Sedating", "Gingeritis"),
        ("Long Faced", "Electrifying"),
        ("Glowing", "Refreshing"),
        ("Foggy", "Energizing"),
        ("Explosive", "Euphoric")
    ],
    "Battery": [
        ("Munchies", "Tropic Thunder"),
        ("Euphoric", "Zombifying"),
        ("Electrifying", "Euphoric"),
        ("Laxative", "Calorie-Dense"),
        ("Cyclopean", "Glowing"),
        ("Shrinking", "Munchies")
    ],
    "Banana": [
        ("Energizing", "Thought-Provoking"),
        ("Calming", "Sneaky"),
        ("Toxic", "Smelly"),
        ("Long Faced", "Refreshing"),
        ("Cyclopean", "Thought-Provoking"),
        ("Disorienting", "Focused"),
        ("Focused", "Seizure-Inducing"),
        ("Paranoia", "Jennerising"),
        ("Smelly", "Anti-Gravity")
    ],
    "Chili": [
        ("Athletic", "Euphoric"),
        ("Anti-Gravity", "Tropic Thunder"),
        ("Sneaky", "Bright-Eyed"),
        ("Munchies", "Toxic"),
        ("Laxative", "Long Faced"),
        ("Shrinking", "Refreshing")
    ],
    "Cuke": [
        ("Toxic", "Euphoric"),
        ("Slippery", "Munchies"),
        ("Sneaky", "Paranoia"),
        ("Foggy", "Cyclopean"),
        ("Gingeritis", "Thought-Provoking"),
        ("Munchies", "Athletic"),
        ("Euphoric", "Laxative")
    ],
    "Donut": [
        ("Calorie-Dense", "Explosive"),
        ("Balding", "Sneaky"),
        ("Anti-Gravity", "Slippery"),
        ("Jennerising", "Gingeritis"),
        ("Focused", "Euphoric"),
        ("Shrinking", "Energizing")
    ],
    "Energy Drink": [
        ("Sedating", "Munchies"),
        ("Euphoric", "Energizing"),
        ("Spicy", "Euphoric"),
        ("Tropic Thunder", "Sneaky"),
        ("Glowing", "Disorienting"),
        ("Foggy", "Laxative"),
        ("Disorienting", "Electrifying"),
        ("Schizophrenia", "Balding"),
        ("Focused", "Shrinking")
    ],
    "Flu Medicine": [
        ("Calming", "Bright-Eyed"),
        ("Athletic", "Munchies"),
        ("Thought-Provoking", "Gingeritis"),
        ("Cyclopean", "Foggy"),
        ("Munchies", "Slippery"),
        ("Laxative", "Euphoric"),
        ("Euphoric", "Toxic"),
        ("Focused", "Calming"),
        ("Electrifying", "Refreshing"),
        ("Shrinking", "Paranoia")
    ],
    "Gasoline": [
        ("Gingeritis", "Smelly"),
        ("Jennerising", "Sneaky"),
        ("Sneaky", "Tropic Thunder"),
        ("Munchies", "Sedating"),
        ("Energizing", "Euphoric"),
        ("Euphoric", "Energizing"),
        ("Laxative", "Foggy"),
        ("Disorienting", "Glowing"),
        ("Paranoia", "Calming"),
        ("Electrifying", "Disorienting"),
        ("Shrinking", "Focused")
    ],
    "Horse Semen": [
        ("Anti-Gravity", "Calming"),
        ("Gingeritis", "Refreshing"),
        ("Thought-Provoking", "Electrifying")
    ],
    "Iodine": [
        ("Calming", "Balding"),
        ("Toxic", "Sneaky"),
        ("Foggy", "Paranoia"),
        ("Calorie-Dense", "Gingeritis"),
        ("Euphoric", "Seizure-Inducing"),
        ("Refreshing", "Thought-Provoking")
    ],
    "Mega Bean": [
        ("Energizing", "Cyclopean"),
        ("Calming", "Glowing"),
        ("Sneaky", "Calming"),
        ("Jennerising", "Paranoia"),
        ("Athletic", "Laxative"),
        ("Slippery", "Toxic"),
        ("Thought-Provoking", "Energizing"),
        ("Seizure-Inducing", "Focused"),
        ("Focused", "Disorienting"),
        ("Shrinking", "Electrifying")
    ],
    "Motor Oil": [
        ("Energizing", "Munchies"),
        ("Foggy", "Toxic"),
        ("Euphoric", "Sedating"),
        ("Paranoia", "Anti-Gravity"),
        ("Munchies", "Schizophrenia")
    ],
    "Mouth Wash": [
        ("Calming", "Anti-Gravity"),
        ("Calorie-Dense", "Sneaky"),
        ("Explosive", "Sedating"),
        ("Focused", "Jennerising")
    ],
    "Paracetamol": [
        ("Energizing", "Paranoia"),
        ("Calming", "Slippery"),
        ("Toxic", "Tropic Thunder"),
        ("Spicy", "Bright-Eyed"),
        ("Glowing", "Toxic"),
        ("Foggy", "Calming"),
        ("Munchies", "Anti-Gravity"),
        ("Electrifying", "Athletic"),
        ("Paranoia", "Balding"),
        ("Focused", "Gingeritis")
    ],
    "Viagra": [
        ("Athletic", "Sneaky"),
        ("Euphoric", "Bright-Eyed"),
        ("Laxative", "Calming"),
        ("Disorienting", "Toxic")
    ]
}

# Function to add default effects


def add_substance_default_effects(substance, selected_effects):
    default_effects = DEFAULT_EFFECTS.get(substance, [])
    updated_effects = set(selected_effects)
    for effect in default_effects:
        # Max 8 effects
        if effect not in updated_effects and len(updated_effects) < 8:
            updated_effects.add(effect)
    return list(updated_effects)

# Function to apply rules to effects


def apply_substance_rules(substance, selected_effects):
    rules = SUBSTANCE_RULES.get(substance, [])
    updated_effects = set(selected_effects)
    for old_effect, new_effect in rules:
        if old_effect in updated_effects:
            updated_effects.remove(old_effect)
            updated_effects.add(new_effect)
    return list(updated_effects)

# Function to process effects for a single substance


def process_effects(substance, selected_effects):
    effects_with_defaults = add_substance_default_effects(
        substance, selected_effects)
    final_effects = apply_substance_rules(substance, effects_with_defaults)
    return final_effects

# Function to generate dropdown options with base effects


def get_substance_options():
    """
    Returns a list of substances with their default effects included in the label.
    """
    options = ["None"]  # Start with "None" as the default option
    for substance, effects in DEFAULT_EFFECTS.items():
        # Combine multiple effects if present
        effect_label = ", ".join(effects)
        options.append(f"{substance} ({effect_label})")
    return options

# Function to find substances that can produce the desired effects


def find_substances_with_effects(desired_effects):
    """
    Finds substances that can produce the desired effects, either as default effects
    or through rule-based transformations.
    """
    matching_substances = []

    for substance, default_effects in DEFAULT_EFFECTS.items():
        # Start with the default effects of the substance
        effects = set(default_effects)

        # Apply the substance's rules to simulate possible effects
        if substance in SUBSTANCE_RULES:
            for old_effect, new_effect in SUBSTANCE_RULES[substance]:
                if old_effect in effects:
                    effects.remove(old_effect)
                    effects.add(new_effect)

        # Check if the substance can produce all desired effects
        if all(effect in effects for effect in desired_effects):
            matching_substances.append(substance)

    return matching_substances

# Function to find substances and show how they produce the desired effects


def find_substances_with_effects_and_steps(desired_effects):
    """
    Finds substances that can produce the desired effects and tracks the steps
    (default effects and rule-based transformations) used to achieve them.
    """
    matching_substances = []
    transformation_steps = []

    for substance, default_effects in DEFAULT_EFFECTS.items():
        # Start with the default effects of the substance
        effects = set(default_effects)
        steps = [
            f"{substance} (Default Effects: {', '.join(default_effects)})"]

        # Apply the substance's rules to simulate possible effects
        if substance in SUBSTANCE_RULES:
            for old_effect, new_effect in SUBSTANCE_RULES[substance]:
                if old_effect in effects:
                    effects.remove(old_effect)
                    effects.add(new_effect)
                    steps.append(
                        f"{substance} transformed {old_effect} → {new_effect}")

        # Check if the substance can produce all desired effects
        if all(effect in effects for effect in desired_effects):
            matching_substances.append(substance)
            transformation_steps.append(steps)

    return matching_substances, transformation_steps

# Function to perform BFS to explore all possible transformations


def bfs_all_transformations(selected_effects):
    """
    Perform BFS to find all reachable effects starting from the selected effects.
    :param selected_effects: Set of currently selected effects.
    :return: Set of all reachable effects.
    """
    if not selected_effects:
        # If no effects are selected, all effects are valid
        return set(EFFECTS.keys())

    # Initialize the queue with selected effects
    queue = list(selected_effects)
    visited = set(selected_effects)  # Track visited effects

    while queue:
        current_effect = queue.pop(0)  # Dequeue the next effect

        # Check all transformations for the current effect
        for substance, rules in SUBSTANCE_RULES.items():
            for old_effect, new_effect in rules:
                if old_effect == current_effect and new_effect not in visited:
                    # Add the new effect to the queue and mark it as visited
                    queue.append(new_effect)
                    visited.add(new_effect)

    return visited

# Function to perform BFS to find the shortest path between two effects


def bfs_shortest_path(start_effect, target_effect):
    """
    Perform BFS to find the shortest path from start_effect to target_effect.
    :param start_effect: The starting effect.
    :param target_effect: The target effect.
    :return: List representing the shortest path, or None if no path exists.
    """
    queue = [(start_effect, [start_effect])
             ]  # Initialize the queue with the starting effect and path
    visited = set([start_effect])  # Track visited effects

    while queue:
        # Dequeue the next effect and its path
        current_effect, path = queue.pop(0)

        # If the target effect is found, return the path
        if current_effect == target_effect:
            return path

        # Check all transformations for the current effect
        for substance, rules in SUBSTANCE_RULES.items():
            for old_effect, new_effect in rules:
                if old_effect == current_effect and new_effect not in visited:
                    # Add the new effect to the queue with the updated path
                    queue.append((new_effect, path + [new_effect]))
                    visited.add(new_effect)

    return None  # Return None if no path exists

# Function to perform BFS to find all paths between two effects


def bfs_all_paths(start_effect, target_effect):
    """
    Perform BFS to find all paths from start_effect to target_effect.
    :param start_effect: The starting effect.
    :param target_effect: The target effect.
    :return: List of all paths, where each path is a list of effects.
    """
    queue = [(start_effect, [start_effect])
             ]  # Initialize the queue with the starting effect and path
    all_paths = []  # Store all paths

    while queue:
        # Dequeue the next effect and its path
        current_effect, path = queue.pop(0)

        # If the target effect is found, add the path to the list of all paths
        if current_effect == target_effect:
            all_paths.append(path)
            continue

        # Check all transformations for the current effect
        for substance, rules in SUBSTANCE_RULES.items():
            for old_effect, new_effect in rules:
                if old_effect == current_effect and new_effect not in path:  # Avoid cycles
                    # Add the new effect to the queue with the updated path
                    queue.append((new_effect, path + [new_effect]))

    return all_paths


# Streamlit app
st.title("Schedule I: Substance Mix Calculator")

# Tabs for better organization
tab1, tab2 = st.tabs(["Substance Mix Calculator", "Reverse Search"])

# Tab 1: Substance Mix Calculator
with tab1:
    st.header("Substance Mix Calculator")

    # Step 1: Select a product
    product = st.selectbox("Select a Product:", list(BASE_PRICES.keys()))

    # Step 2: Add substances dynamically
    st.markdown("### Add Substances")
    substances = []
    # Get dropdown options with base effects, excluding the 4 strains of weed
    substance_options = [
        f"{substance} ({', '.join(effects)})"
        for substance, effects in DEFAULT_EFFECTS.items()
        if substance not in ["OG Kush", "Sour Diesel", "Green Crack", "Granddaddy Purple"]
    ]
    substance_options.insert(0, "None")  # Add "None" as the first option

    # Create 2 columns for 8 dropdowns (4 in each column)
    col1, col2 = st.columns(2)

    # Add 4 dropdowns in each column
    for i in range(4):
        with col1:
            selected_option = st.selectbox(
                f"Substance {i + 1}:", substance_options, key=f"substance_{i}"
            )
            if selected_option != "None":
                # Extract the substance name (remove the effect label in parentheses)
                substance_name = selected_option.split(" (")[0]
                substances.append(substance_name)

    for i in range(4, 8):
        with col2:
            selected_option = st.selectbox(
                f"Substance {i + 1}:", substance_options, key=f"substance_{i}"
            )
            if selected_option != "None":
                # Extract the substance name (remove the effect label in parentheses)
                substance_name = selected_option.split(" (")[0]
                substances.append(substance_name)

    # Step 3: Mix button
    if st.button("Mix"):
        # Process effects for all selected substances
        final_effects = []
        for substance in substances:
            final_effects = process_effects(substance, final_effects)

        # Calculate total multiplier
        total_multiplier = sum(EFFECTS.get(effect, 0)
                               for effect in final_effects)

        # Calculate final price
        base_price = BASE_PRICES[product]
        final_price = base_price * (1 + total_multiplier)

        # Display results
        st.subheader("Mix Results")
        st.write(f"**Product:** {product}")
        st.write(f"**Base Price:** ${base_price}")
        st.write(f"**Selected Substances:** {', '.join(substances)}")
        st.write(f"**Final Effects:**")
        for effect in final_effects:
            st.write(f"- {effect} (x{EFFECTS[effect]:.2f})")
        st.write(f"**Total Multiplier:** {total_multiplier:.2f}")
        st.write(f"**Final Price:** ~${round(final_price)}")

# Tab 2: Reverse Search
with tab2:
    st.header("Reverse Search: Find Substances by Effects")

    # Reverse Search Section
    st.markdown("### Select Desired Effects")

    # Initialize selected effects
    selected_effects = set()

    # Divide effects into 4 groups for columns
    effects_list = list(EFFECTS.keys())
    column_groups = [
        effects_list[:8],   # First 8 effects
        effects_list[8:16],  # Next 8 effects
        effects_list[16:24],  # Next 8 effects
        effects_list[24:]   # Remaining effects
    ]

    # Create 4 columns
    col1, col2, col3, col4 = st.columns(4)

    # Add checkboxes to each column
    for col, group in zip([col1, col2, col3, col4], column_groups):
        with col:
            for effect in group:
                # Allow selection up to 8 effects
                if len(selected_effects) < 8 or effect in selected_effects:
                    if st.checkbox(effect, key=f"effect_{effect}"):
                        selected_effects.add(effect)
                    else:
                        selected_effects.discard(effect)

    # Display the selected effects
    st.write(
        f"Selected Effects ({len(selected_effects)}/8): {', '.join(selected_effects)}")

    # Search button
    if st.button("Search Substances"):
        # Automatically find the shortest path of ingredients to achieve the desired effects
        matching_substances, transformation_steps = find_substances_with_effects_and_steps(
            selected_effects)

        st.subheader("Reverse Search Results")
        if matching_substances:
            st.write("The following substances can produce the desired effects:")
            for i, substance in enumerate(matching_substances):
                st.write(f"- **{substance}**")
                st.write("  Steps to achieve effects:")
                for step in transformation_steps[i]:
                    st.write(f"    - {step}")
        else:
            st.write("No substances found that can produce the desired effects.")

# Streamlit section: How Pricing Works
st.sidebar.markdown("## How Pricing Works")
st.sidebar.markdown("""
Our mix pricing is calculated by taking the base price of each product and applying the effect multipliers. The formula used is:

**Final Price** = Base Price * (1 + total effect multiplier)

### Base Prices:
- **Weed**: $35
- **Meth**: $70
- **Cocaine**: $150

### Effect Multiplier:
Each effect adds a multiplier that increases the base price.

### Example:
Suppose you have a mix that includes the effects: **Bright-Eyed** and **Tropic Thunder** with multipliers of 0.40 and 0.46. The total multiplier is 0.40 + 0.46 = 0.86. For a base product like Meth (base price $70), the final price is:

$70 * (1 + 0.86) = $130
""")

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
