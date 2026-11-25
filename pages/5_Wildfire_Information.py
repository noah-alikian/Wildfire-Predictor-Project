import streamlit as st

st.title('Wildfire Information')
st.image('wildfire_home.jpg')
st.text('This page is dedicated to providing information on what to do in case a wildfire occurs in your community.')

tab1, tab2, tab3, tab4 = st.tabs(['Before', 'During', 'After', 'Additional Information'])

with tab1:
    st.subheader('Wildfire Preparation')
    st.markdown('**Evacuation-Ready**')
    st.markdown('- Sign up for alerts.')
    st.markdown('- Know your evacuation routes and a meetup spot.')
    st.markdown('- Keep gas tank more than halfway full.')
    st.markdown('- Go-bag ready for each person: water, food, meds, chargers, copies of IDs/insurance, masks (N95/KN95), flashlight, cash, pet supplies. Store by the door.')
    st.markdown('**Home-Prep**')
    st.markdown('- Home hardening: ember-resistant vents/screens, clean roof/gutters, 1/8-inch metal mesh on openings, fine metal screens over attic/under-deck areas.')
    st.markdown('- Defensible space: clear dead vegetation, keep the first 5 ft around the home “zero-ignition” (gravel/hardscape), trim trees.')
    st.markdown('- Prep the property: clearly mark your address, make sure hoses reach all sides, keep tools (shovel, rake) accessible, store firewood/propane away from structures.')
    st.markdown('**Additional Prep**')
    st.markdown("- Plan for people & pets: list special needs, backups for medical devices, transport crates, and a buddy who can help evacuate if you’re away.")
    st.markdown("- Documents & insurance: take photos of rooms, back up critical docs to cloud/USB, review insurance for wildfire coverage.")

with tab2:
    st.subheader('Active Wildfire Procedures')
    st.markdown('- Leave early. Traffic gets bad fast.')
    st.markdown('- Before you go: close all windows/doors, move furniture away from windows, shut interior doors, leave lights on, remove flammables from decks, connect garden hoses.')
    st.markdown('- ***Shut off gas only if you smell gas/see line damage or local officials instruct it.***')
    st.markdown('- Dress to protect: long sleeves/pants, sturdy shoes, goggles, hat, N95/KN95 for smoke.')
    st.markdown('- Keep pets on leash/in carriers.')
    st.markdown('- ***If you cannot leave:*** call 911 with exact location, stay in a cleared area or inside a room farthest from fire with a closed door, keep cellphone on, cover vents/gaps with wet towels if needed.')
    st.markdown('- Driving out: headlights on, watch for downed lines and smoke, follow official routes, not backroads unless directed.')

with tab3:
    st.subheader('Post-Wildfire Procedures')
    st.markdown('- Wait for the all-clear.')
    st.markdown('- Watch for hot spots, ash pits, falling trees/power lines.')
    st.markdown('- Protect yourself: gloves, long sleeves/pants, boots, and a proper mask when cleaning ash.')
    st.markdown('- Wet down ash before sweeping.')
    st.markdown("- Check utilities & food: don’t turn gas/electric back on if damaged.")
    st.markdown("- Throw out food that got warm or has ash/smoke damage.")
    st.markdown("- Photograph damage for insurance.")

with tab4:
    st.subheader('Additional Information')
    st.markdown('**During Smoke Event (Distant Fire)**')
    st.markdown('- Stay indoors with clean air.')
    st.markdown('- Close all windows/doors.')
    st.markdown('- Run HVAC on recirculate.')
    st.markdown('- Use a HEPA purifier or create a “clean room.”')
    st.markdown('- Wear N95/KN95 outside.')
    st.markdown('**Why Homes Ignite**')
    st.markdown('- Embers are the main threat. They travel far ahead of flames and ignite roofs, vents, decks, mulch, and items within ~0–200 ft of the house.')
    st.markdown('- Focus hardening + defensible space here.')

    st.sidebar.subheader('Useful Sources')
    st.sidebar.markdown('- https://www.ready.gov/wildfires')
    st.sidebar.markdown('- https://www.fire.ca.gov/prepare/get-ready-to-go')
    st.sidebar.markdown('- https://www.redcross.org/get-help/how-to-prepare-for-emergencies/types-of-emergencies/wildfire.html')
    st.sidebar.markdown('- https://www.nfpa.org/education-and-research/wildfire/preparing-homes-for-wildfire')