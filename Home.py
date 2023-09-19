# Theme is set in config.toml
import streamlit as st
import utils as ut

# This should be the first line of the code
st.set_page_config(page_title='ACW - After Call Work Portal', layout='wide')
ut.add_logo()
ut.set_acw_header()

st.markdown("<h3 style='text-align: left;'>Overview</h3>", unsafe_allow_html=True)
st.markdown("ACW or After Call Work is an integral part of contact center for every interaction handled by the agent. Call center agent is responsible for ACW after completing the interaction with the customer and before they accept the next call. After the call is ended, call center agents enter call related important information in the agent desktop/CRM application so that it can be used for subsequent interactions with that caller or for reporting, dashboards, agent assist applications or for agent training (or for pure data analysis, easy search, tagging and annotating call interaction). Traditionally this data can be anything starting from reason of call, call disposition, call summary, caller sentiment, notes, etc.")
st.markdown("Agent is marked as not ready for the duration of ACW which means agents can not take the next call. Also, completing the ACW needs an agent to take notes during the call while assisting the caller at the same time. Agents need to be on their toes to be able to recall all important details discussed/captured during the call for ACW notes and they need to do this all quickly because they are on a clock for ACW. This eventually takes a toll on an agent's productivity. If you are from the contact center domain, you know how crucial is Average handling time is for the agent. AHT is the time taken by the call center agent to handle customer's query on a call including talk time, hold time and ACW time. AHT is a key metric for call center and agent efficiency. Now imagine if the agent could solely focus on resolving customer queries than having to memorize the conversation points, taking notes and hurriedly feeding all the data in the CRM application for customer call records. This is possible if ACW can be automated, what's even better is when it is backed by Generative AI.")
st.markdown("""Using this portal, you can test the ACW automation (<a href="Upload_File" target="_self">ACW Playground</a>), view ACW records (<a href="ACW_Table" target="_self">ACW Records</a>) and ACW based contact center metrics (<a href="ACW_Charts" target="_self">ACW Charts</a>).""", unsafe_allow_html=True)

ut.add_footer()