## ==================== STREAMLIT COMPLETE GUIDE ====================
# pip install streamlit
# streamlit run app.py

import streamlit as st
import numpy as np
import pandas as pd
import time
import random
# ───────────────────────────── PAGE CONFIG ─────────────────────────────
st.set_page_config(page_title="Streamlit Guide", page_icon="🚀", layout="wide")

# ───────────────────────────── CUSTOM CSS ──────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;600&family=Inter:wght@400;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .section-title {
        background: linear-gradient(90deg, #1e3a5f, #0f62fe);
        color: white;
        padding: 10px 20px;
        border-radius: 8px;
        font-size: 1.4rem;
        font-weight: 700;
        margin-top: 2rem;
        margin-bottom: 0.5rem;
        letter-spacing: 0.5px;
    }

    .concept-box {
        background-color: #f0f4ff;
        border-left: 4px solid #0f62fe;
        padding: 10px 16px;
        border-radius: 0 8px 8px 0;
        margin: 10px 0;
        font-size: 0.92rem;
        color: #1e3a5f;
    }

    .arg-box {
        background-color: #fff8e1;
        border-left: 4px solid #f59e0b;
        padding: 10px 16px;
        border-radius: 0 8px 8px 0;
        margin: 8px 0;
        font-size: 0.88rem;
        color: #78350f;
    }

    .sub-title {
        font-size: 1.05rem;
        font-weight: 600;
        color: #1e3a5f;
        margin-top: 1.2rem;
        margin-bottom: 0.3rem;
        border-bottom: 2px dotted #0f62fe;
        padding-bottom: 3px;
    }

    .divider {
        border: none;
        border-top: 2px solid #e5e7eb;
        margin: 2rem 0;
    }
</style>
""", unsafe_allow_html=True)


# ─────────────────────────── HEADER ────────────────────────────────────
st.markdown("""
<h1 style='text-align:center; color:#0f62fe; font-family:Inter; font-size:2.5rem;'>
    🚀 Streamlit Complete Guide
</h1>
<p style='text-align:center; color:#64748b; font-size:1rem;'>
    A structured reference with descriptions, arguments & working examples
</p>
<hr style='border-top: 3px solid #0f62fe; margin-bottom: 2rem;'/>
""", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════
# 1. INSTALLATION
# ════════════════════════════════════════════════════════════════════════
st.markdown("<div class='section-title'>📦 1. Installation</div>", unsafe_allow_html=True)

st.markdown("<div class='concept-box'>Install Streamlit via pip. Requires Python 3.8+</div>", unsafe_allow_html=True)

st.code("pip install streamlit", language="bash")

st.markdown("<hr class='divider'/>", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════
# 2. RUN APP
# ════════════════════════════════════════════════════════════════════════
st.markdown("<div class='section-title'>▶️ 2. Run App</div>", unsafe_allow_html=True)

st.markdown("<div class='concept-box'>Start the Streamlit dev server. Opens at <b>localhost:8501</b> by default. You can also run directly from a URL.</div>", unsafe_allow_html=True)

st.code("""
streamlit run app.py                    # Run local file
streamlit run https://example.com/app.py   # Run from URL
""", language="bash")

st.markdown("<hr class='divider'/>", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════
# 3. IMPORTS
# ════════════════════════════════════════════════════════════════════════
st.markdown("<div class='section-title'>📥 3. Imports</div>", unsafe_allow_html=True)

st.markdown("<div class='concept-box'>Standard imports used throughout most Streamlit apps.</div>", unsafe_allow_html=True)

st.code("""
import streamlit as st   # Core library
import numpy as np       # Numerical operations
import pandas as pd      # DataFrames
import time              # Used for delays, spinners, progress
import random
""", language="python")

st.markdown("<hr class='divider'/>", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════
# 4. BASIC OUTPUT
# ════════════════════════════════════════════════════════════════════════
st.markdown("<div class='section-title'>🖊️ 4. Basic Output</div>", unsafe_allow_html=True)

st.markdown("""
<div class='concept-box'>
    Streamlit provides multiple text display functions, each with different styling.<br>
    <b>st.write()</b> is the most versatile — it accepts text, DataFrames, dicts, charts, and more.
</div>
""", unsafe_allow_html=True)

st.markdown("<div class='arg-box'><b>st.title(body)</b> — Large top-level heading<br><b>st.header(body)</b> — Section heading<br><b>st.subheader(body)</b> — Smaller section heading<br><b>st.text(body)</b> — Fixed-width plain text<br><b>st.write(*args)</b> — Smart display for almost any object</div>", unsafe_allow_html=True)

st.code("""
st.title("My App Title")
st.header("Section Header")
st.subheader("Sub Section")
st.text("Plain fixed-width text")
st.write("Hello, World!")
st.write("Supports **markdown** too!")
""", language="python")

st.markdown("<div class='sub-title'>▸ Live Output</div>", unsafe_allow_html=True)
st.title("My App Title")
st.header("Section Header")
st.subheader("Sub Section")
st.text("Plain fixed-width text")
st.write("Hello, World!")
st.write("Supports **markdown** too!")

st.markdown("<hr class='divider'/>", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════
# 5. DATA DISPLAY
# ════════════════════════════════════════════════════════════════════════
st.markdown("<div class='section-title'>📊 5. Data Display</div>", unsafe_allow_html=True)

st.markdown("""
<div class='concept-box'>
    Display tabular data using <b>st.dataframe()</b> (interactive, scrollable) or <b>st.table()</b> (static).
    <b>st.write(df)</b> also renders DataFrames interactively.
</div>
""", unsafe_allow_html=True)

st.markdown("<div class='arg-box'><b>st.dataframe(data, width, height, use_container_width)</b><br><b>st.table(data)</b> — Static non-scrollable table<br><b>st.write(df)</b> — Auto-detects DataFrame and renders interactively</div>", unsafe_allow_html=True)

st.code("""
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

st.write("Here's our first attempt at using data to create a table:")
st.write(df)                             # Interactive table via st.write
st.dataframe(df, use_container_width=True)   # Explicit interactive dataframe
st.table(df)                             # Static table
""", language="python")

st.markdown("<div class='sub-title'>▸ Live Output</div>", unsafe_allow_html=True)
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
st.write("Here's our first attempt at using data to create a table:")
st.write(df)
st.dataframe(df, use_container_width=True)
st.table(df)

st.markdown("<hr class='divider'/>", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════
# 6. WIDGETS
# ════════════════════════════════════════════════════════════════════════
st.markdown("<div class='section-title'>🎛️ 6. Widgets</div>", unsafe_allow_html=True)
st.markdown("<div class='concept-box'>Widgets let users interact with your app. Every widget returns a value that you can use in your Python code. Streamlit reruns the script from top to bottom on every interaction.</div>", unsafe_allow_html=True)


# 6.1 SLIDER
st.markdown("<div class='sub-title'>6.1 — st.slider()</div>", unsafe_allow_html=True)
st.markdown("<div class='arg-box'><b>st.slider(label, min_value, max_value, value, step, key)</b><br>• label — text shown above slider<br>• min_value / max_value — range bounds<br>• value — default value (or tuple for range)<br>• step — increment size</div>", unsafe_allow_html=True)
st.code("""
age = st.slider("Select your age", min_value=0, max_value=100, value=25, step=1)
st.write(f"Your age: {age}")
""", language="python")
st.markdown("<div class='sub-title'>▸ Live Output</div>", unsafe_allow_html=True)
age = st.slider("Select your age", min_value=0, max_value=100, value=25, step=1)
st.write(f"Your age: {age}")


# 6.2 TEXT INPUT
st.markdown("<div class='sub-title'>6.2 — st.text_input()</div>", unsafe_allow_html=True)
st.markdown("<div class='arg-box'><b>st.text_input(label, value, placeholder, type, key)</b><br>• type='password' — hides input<br>• placeholder — ghost text when empty</div>", unsafe_allow_html=True)
st.code("""
name = st.text_input("Enter your name", placeholder="e.g. Alice")
st.write(f"Hello, {name}!")
""", language="python")
st.markdown("<div class='sub-title'>▸ Live Output</div>", unsafe_allow_html=True)
name = st.text_input("Enter your name", placeholder="e.g. Alice", key="name_widget")
st.write(f"Hello, {name}!" if name else "Waiting for input...")


# 6.3 NUMBER INPUT
st.markdown("<div class='sub-title'>6.3 — st.number_input()</div>", unsafe_allow_html=True)
st.markdown("<div class='arg-box'><b>st.number_input(label, min_value, max_value, value, step, format, key)</b><br>• format — e.g. '%0.2f' for 2 decimals</div>", unsafe_allow_html=True)
st.code("""
num = st.number_input("Enter a number", min_value=0, max_value=1000, value=50, step=5)
st.write(f"You entered: {num}")
""", language="python")
st.markdown("<div class='sub-title'>▸ Live Output</div>", unsafe_allow_html=True)
num = st.number_input("Enter a number", min_value=0, max_value=1000, value=50, step=5)
st.write(f"You entered: {num}")


# 6.4 SELECTBOX
st.markdown("<div class='sub-title'>6.4 — st.selectbox()</div>", unsafe_allow_html=True)
st.markdown("<div class='arg-box'><b>st.selectbox(label, options, index, format_func, key)</b><br>• options — list or tuple of choices<br>• index — default selected index<br>• format_func — function to format each option label</div>", unsafe_allow_html=True)
st.code("""
color = st.selectbox("Pick a color", ["Red", "Green", "Blue"], index=0)
st.write(f"You chose: {color}")
""", language="python")
st.markdown("<div class='sub-title'>▸ Live Output</div>", unsafe_allow_html=True)
color = st.selectbox("Pick a color", ["Red", "Green", "Blue"], index=0)
st.write(f"You chose: {color}")


# 6.5 MULTISELECT
st.markdown("<div class='sub-title'>6.5 — st.multiselect()</div>", unsafe_allow_html=True)
st.markdown("<div class='arg-box'><b>st.multiselect(label, options, default, key)</b><br>• default — list of pre-selected values<br>• Returns a list of selected items</div>", unsafe_allow_html=True)
st.code("""
skills = st.multiselect("Select your skills", ["Python", "SQL", "ML", "Streamlit"], default=["Python"])
st.write(f"Skills: {skills}")
""", language="python")
st.markdown("<div class='sub-title'>▸ Live Output</div>", unsafe_allow_html=True)
skills = st.multiselect("Select your skills", ["Python", "SQL", "ML", "Streamlit"], default=["Python"])
st.write(f"Skills: {skills}")


# 6.6 CHECKBOX
st.markdown("<div class='sub-title'>6.6 — st.checkbox()</div>", unsafe_allow_html=True)
st.markdown("<div class='arg-box'><b>st.checkbox(label, value, key)</b><br>• value — default checked state (True/False)<br>• Returns True if checked, False otherwise</div>", unsafe_allow_html=True)
st.code("""
agree = st.checkbox("I agree to the terms", value=False)
if agree:
    st.success("Thank you for agreeing!")
""", language="python")
st.markdown("<div class='sub-title'>▸ Live Output</div>", unsafe_allow_html=True)
agree = st.checkbox("I agree to the terms", value=False)
if agree:
    st.success("Thank you for agreeing!")


# 6.7 RADIO
st.markdown("<div class='sub-title'>6.7 — st.radio()</div>", unsafe_allow_html=True)
st.markdown("<div class='arg-box'><b>st.radio(label, options, index, horizontal, key)</b><br>• horizontal=True — displays options side by side<br>• Returns the selected option value</div>", unsafe_allow_html=True)
st.code("""
plan = st.radio("Choose a plan", ["Free", "Pro", "Enterprise"], horizontal=True)
st.write(f"Selected plan: {plan}")
""", language="python")
st.markdown("<div class='sub-title'>▸ Live Output</div>", unsafe_allow_html=True)
plan = st.radio("Choose a plan", ["Free", "Pro", "Enterprise"], horizontal=True)
st.write(f"Selected plan: {plan}")


# 6.8 BUTTON
st.markdown("<div class='sub-title'>6.8 — st.button()</div>", unsafe_allow_html=True)
st.markdown("<div class='arg-box'><b>st.button(label, type, use_container_width, key)</b><br>• type='primary' — blue filled button; 'secondary' — outline<br>• Returns True only on the run triggered by the click</div>", unsafe_allow_html=True)
st.code("""
if st.button("Submit", type="primary"):
    st.write("Button clicked! ✅")
""", language="python")
st.markdown("<div class='sub-title'>▸ Live Output</div>", unsafe_allow_html=True)
if st.button("Submit", type="primary"):
    st.write("Button clicked! ✅")

st.markdown("<hr class='divider'/>", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════
# 7. SIDEBAR
# ════════════════════════════════════════════════════════════════════════
st.markdown("<div class='section-title'>📌 7. Sidebar</div>", unsafe_allow_html=True)
st.markdown("<div class='concept-box'>Add any widget to the sidebar by prefixing with <b>st.sidebar.</b> — great for navigation, filters, and settings that persist across the app.</div>", unsafe_allow_html=True)
st.markdown("<div class='arg-box'><b>st.sidebar.widget(...)</b> — mirrors every widget available in the main area<br><b>with st.sidebar:</b> — context manager style</div>", unsafe_allow_html=True)

st.code("""
# Method 1: Direct prefix
option = st.sidebar.selectbox("Choose dataset", ["Iris", "Titanic", "MNIST"])

# Method 2: Context manager
with st.sidebar:
    st.header("Settings")
    threshold = st.slider("Threshold", 0.0, 1.0, 0.5)
""", language="python")

# Live sidebar example
with st.sidebar:
    st.markdown("---")
    st.markdown("**🔧 Guide Controls**")
    theme = st.selectbox("Dataset", ["Iris", "Titanic", "MNIST"])
    threshold = st.slider("Threshold", 0.0, 1.0, 0.5)

st.write(f"Sidebar selected: `{theme}` | Threshold: `{threshold}`")
st.markdown("<hr class='divider'/>", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════
# 8. LAYOUT
# ════════════════════════════════════════════════════════════════════════
st.markdown("<div class='section-title'>📐 8. Layout</div>", unsafe_allow_html=True)
st.markdown("<div class='concept-box'>Organize content using <b>columns</b>, <b>tabs</b>, <b>expanders</b>, and <b>containers</b> for clean multi-panel interfaces.</div>", unsafe_allow_html=True)
st.markdown("<div class='arg-box'><b>st.columns(spec)</b> — spec is int (equal cols) or list of weights e.g. [2,1]<br><b>st.tabs(list)</b> — returns list of tab contexts<br><b>st.expander(label, expanded)</b> — collapsible section<br><b>st.container()</b> — logical grouping block</div>", unsafe_allow_html=True)

st.code("""
# Columns
col1, col2, col3 = st.columns([2, 1, 1])
with col1:
    st.metric("Revenue", "$12,500", "+8%")
with col2:
    st.metric("Users", "1,240", "+12%")
with col3:
    st.metric("Churn", "3.2%", "-1%")

# Tabs
tab1, tab2 = st.tabs(["📈 Chart", "📋 Data"])
with tab1:
    st.line_chart(data)
with tab2:
    st.dataframe(data)

# Expander
with st.expander("🔍 See details", expanded=False):
    st.write("Hidden content revealed on click!")
""", language="python")

st.markdown("<div class='sub-title'>▸ Live Output</div>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([2, 1, 1])
with col1:
    st.metric("Revenue", "$12,500", "+8%")
with col2:
    st.metric("Users", "1,240", "+12%")
with col3:
    st.metric("Churn", "3.2%", "-1%")

tab1, tab2 = st.tabs(["📈 Chart", "📋 Data"])
demo_data = pd.DataFrame(np.random.randn(15, 3), columns=["A", "B", "C"])
with tab1:
    st.line_chart(demo_data)
with tab2:
    st.dataframe(demo_data)

with st.expander("🔍 See details", expanded=False):
    st.write("Hidden content revealed on click!")

st.markdown("<hr class='divider'/>", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════
# 9. FILE UPLOAD
# ════════════════════════════════════════════════════════════════════════
st.markdown("<div class='section-title'>📂 9. File Upload</div>", unsafe_allow_html=True)
st.markdown("<div class='concept-box'>Allow users to upload files. The returned object behaves like a file-like object — read with <b>.read()</b>, load with pandas, etc.</div>", unsafe_allow_html=True)
st.markdown("<div class='arg-box'><b>st.file_uploader(label, type, accept_multiple_files, key)</b><br>• type — list of allowed extensions e.g. ['csv', 'xlsx']<br>• accept_multiple_files=True — returns a list of files</div>", unsafe_allow_html=True)

st.code("""
file = st.file_uploader("Upload a CSV file", type=["csv"])
if file is not None:
    df = pd.read_csv(file)
    st.write(f"Filename: {file.name} | Size: {file.size} bytes")
    st.dataframe(df)
""", language="python")

st.markdown("<div class='sub-title'>▸ Live Output</div>", unsafe_allow_html=True)
file = st.file_uploader("Upload a CSV file", type=["csv"])
if file is not None:
    df_uploaded = pd.read_csv(file)
    st.write(f"Filename: `{file.name}` | Size: `{file.size}` bytes")
    st.dataframe(df_uploaded)

st.markdown("<hr class='divider'/>", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════
# 10. CHARTS
# ════════════════════════════════════════════════════════════════════════
st.markdown("<div class='section-title'>📉 10. Charts</div>", unsafe_allow_html=True)
st.markdown("<div class='concept-box'>Streamlit includes built-in chart functions. For advanced charts, use <b>Plotly</b>, <b>Altair</b>, or <b>Matplotlib</b> with <b>st.plotly_chart()</b>, <b>st.altair_chart()</b>, <b>st.pyplot()</b>.</div>", unsafe_allow_html=True)
st.markdown("<div class='arg-box'><b>st.line_chart(data, x, y, color, use_container_width)</b><br><b>st.bar_chart(data)</b><br><b>st.area_chart(data)</b><br><b>st.scatter_chart(data)</b></div>", unsafe_allow_html=True)

st.code("""
data = pd.DataFrame(np.random.randn(20, 3), columns=['A', 'B', 'C'])

st.line_chart(data)
st.bar_chart(data)
st.area_chart(data)
""", language="python")

st.markdown("<div class='sub-title'>▸ Live Output</div>", unsafe_allow_html=True)
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['A', 'B', 'C'])
col_a, col_b = st.columns(2)
with col_a:
    st.write("Line Chart")
    st.line_chart(chart_data)
with col_b:
    st.write("Bar Chart")
    st.bar_chart(chart_data)
st.write("Area Chart")
st.area_chart(chart_data)

st.markdown("<hr class='divider'/>", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════
# 11. PROGRESS BAR
# ════════════════════════════════════════════════════════════════════════
st.markdown("<div class='section-title'>⏳ 11. Progress Bar</div>", unsafe_allow_html=True)
st.markdown("<div class='concept-box'>Show task completion progress. Create with <b>st.progress()</b> and update dynamically in a loop using <b>.progress(value)</b>. Value ranges from 0 to 100 (or 0.0 to 1.0).</div>", unsafe_allow_html=True)
st.markdown("<div class='arg-box'><b>st.progress(value, text)</b><br>• value — int (0–100) or float (0.0–1.0)<br>• text — optional label shown beside the bar</div>", unsafe_allow_html=True)

st.code("""
bar = st.progress(0, text="Processing...")

for i in range(100):
    bar.progress(i + 1, text=f"Step {i+1}/100")
    time.sleep(0.01)

st.success("Done!")
""", language="python")

st.markdown("<div class='sub-title'>▸ Live Output</div>", unsafe_allow_html=True)
if st.button("▶ Run Progress Demo"):
    bar = st.progress(0, text="Processing...")
    for i in range(100):
        bar.progress(i + 1, text=f"Step {i+1}/100")
        time.sleep(0.01)
    st.success("Done!")

st.markdown("<hr class='divider'/>", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════
# 12. STATUS MESSAGES
# ════════════════════════════════════════════════════════════════════════
st.markdown("<div class='section-title'>🔔 12. Status Messages</div>", unsafe_allow_html=True)
st.markdown("<div class='concept-box'>Display color-coded alert boxes to communicate state, errors, warnings, or general info to users.</div>", unsafe_allow_html=True)
st.markdown("<div class='arg-box'><b>st.success(body, icon)</b> — green box<br><b>st.error(body, icon)</b> — red box<br><b>st.warning(body, icon)</b> — yellow box<br><b>st.info(body, icon)</b> — blue box<br><b>st.exception(e)</b> — shows traceback</div>", unsafe_allow_html=True)

st.code("""
st.success("✅ Data loaded successfully!")
st.error("❌ Failed to connect to database.")
st.warning("⚠️ API rate limit approaching.")
st.info("ℹ️ Results are cached for 10 minutes.")
""", language="python")

st.markdown("<div class='sub-title'>▸ Live Output</div>", unsafe_allow_html=True)
st.success("✅ Data loaded successfully!")
st.error("❌ Failed to connect to database.")
st.warning("⚠️ API rate limit approaching.")
st.info("ℹ️ Results are cached for 10 minutes.")

st.markdown("<hr class='divider'/>", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════
# 13. SPINNER
# ════════════════════════════════════════════════════════════════════════
st.markdown("<div class='section-title'>🌀 13. Spinner</div>", unsafe_allow_html=True)
st.markdown("<div class='concept-box'>Show a loading animation while a long operation runs. Use as a context manager — the spinner disappears when the <b>with</b> block exits.</div>", unsafe_allow_html=True)
st.markdown("<div class='arg-box'><b>with st.spinner(text)</b><br>• text — message displayed beside the spinner animation</div>", unsafe_allow_html=True)

st.code("""
with st.spinner("Fetching data from API..."):
    time.sleep(2)       # simulate delay
    data = fetch_data()

st.success("Data loaded!")
""", language="python")

st.markdown("<div class='sub-title'>▸ Live Output</div>", unsafe_allow_html=True)
if st.button("▶ Run Spinner Demo"):
    with st.spinner("Fetching data from API..."):
        time.sleep(2)
    st.success("Data loaded!")

st.markdown("<hr class='divider'/>", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════
# 14. SESSION STATE
# ════════════════════════════════════════════════════════════════════════
st.markdown("<div class='section-title'>💾 14. Session State</div>", unsafe_allow_html=True)
st.markdown("""
<div class='concept-box'>
    Streamlit reruns the entire script on every interaction, resetting all variables.
    <b>st.session_state</b> persists values across reruns — essential for counters, multi-step forms, login state, etc.
    Access like a dict: <code>st.session_state['key']</code> or like an attribute: <code>st.session_state.key</code>
</div>
""", unsafe_allow_html=True)
st.markdown("<div class='arg-box'><b>st.session_state[key]</b> — dict-style access<br><b>st.session_state.key</b> — attribute-style access<br>• Initialize with: <code>if 'key' not in st.session_state: st.session_state.key = default</code></div>", unsafe_allow_html=True)

st.code("""
# Initialize counter if not yet set
if "count" not in st.session_state:
    st.session_state.count = 0

col1, col2, col3 = st.columns(3)
if col1.button("➕ Increment"):
    st.session_state.count += 1
if col2.button("➖ Decrement"):
    st.session_state.count -= 1
if col3.button("🔄 Reset"):
    st.session_state.count = 0

st.metric("Counter", st.session_state.count)
""", language="python")

st.markdown("<div class='sub-title'>▸ Live Output</div>", unsafe_allow_html=True)
if "count" not in st.session_state:
    st.session_state.count = 0

c1, c2, c3 = st.columns(3)
if c1.button("➕ Increment"):
    st.session_state.count += 1
if c2.button("➖ Decrement"):
    st.session_state.count -= 1
if c3.button("🔄 Reset"):
    st.session_state.count = 0

st.metric("Counter Value", st.session_state.count)

st.markdown("<hr class='divider'/>", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════
# 15. CACHING
# ════════════════════════════════════════════════════════════════════════
st.markdown("<div class='section-title'>⚡ 15. Caching</div>", unsafe_allow_html=True)
st.markdown("""
<div class='concept-box'>
    Avoid re-running expensive computations on every rerun.<br>
    • <b>@st.cache_data</b> — for data (DataFrames, API responses, computed values). Each call returns a copy.<br>
    • <b>@st.cache_resource</b> — for shared resources (ML models, DB connections). Returns the same object.
</div>
""", unsafe_allow_html=True)
st.markdown("<div class='arg-box'><b>@st.cache_data(ttl, max_entries, show_spinner)</b><br>• ttl — time-to-live in seconds (e.g. ttl=3600)<br>• max_entries — max cached results to keep<br><b>@st.cache_resource(ttl, show_spinner)</b></div>", unsafe_allow_html=True)

st.code("""
@st.cache_data(ttl=600)            # Cache for 10 minutes
def load_data(url: str):
    return pd.read_csv(url)

@st.cache_resource                 # Load model once, share across sessions
def load_model():
    return MyMLModel.load("model.pkl")

df = load_data("https://data.example.com/data.csv")
model = load_model()
""", language="python")

@st.cache_data
def get_sample_data():
    return pd.DataFrame({"x": range(5), "y": np.random.randn(5)})

st.markdown("<div class='sub-title'>▸ Live Output (cached function)</div>", unsafe_allow_html=True)
st.dataframe(get_sample_data())

st.markdown("<hr class='divider'/>", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════
# 16. FORMS
# ════════════════════════════════════════════════════════════════════════
st.markdown("<div class='section-title'>📝 16. Forms</div>", unsafe_allow_html=True)
st.markdown("<div class='concept-box'>Wrap widgets in a form so the app only reruns when the user explicitly submits — preventing premature reruns on each widget interaction.</div>", unsafe_allow_html=True)
st.markdown("<div class='arg-box'><b>with st.form(key, clear_on_submit)</b><br>• key — unique form identifier (required)<br>• clear_on_submit — reset widgets after submit<br><b>st.form_submit_button(label, type)</b> — must be inside the form</div>", unsafe_allow_html=True)

st.code("""
with st.form("signup_form", clear_on_submit=False):
    st.subheader("Sign Up")
    username = st.text_input("Username")
    email    = st.text_input("Email")
    role     = st.selectbox("Role", ["Developer", "Analyst", "Manager"])
    submit   = st.form_submit_button("Register", type="primary")

if submit:
    st.success(f"Registered: {username} | {email} | {role}")
""", language="python")

st.markdown("<div class='sub-title'>▸ Live Output</div>", unsafe_allow_html=True)
with st.form("signup_form", clear_on_submit=False):
    st.subheader("Sign Up")
    username = st.text_input("Username")
    email    = st.text_input("Email")
    role     = st.selectbox("Role", ["Developer", "Analyst", "Manager"])
    submit   = st.form_submit_button("Register", type="primary")

if submit:
    st.success(f"Registered: **{username}** | {email} | {role}")

st.markdown("<hr class='divider'/>", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════
# 17. CHAT
# ════════════════════════════════════════════════════════════════════════
st.markdown("<div class='section-title'>💬 17. Chat Interface</div>", unsafe_allow_html=True)
st.markdown("<div class='concept-box'>Build conversational UIs with <b>st.chat_input()</b> and <b>st.chat_message()</b>. Combine with session state to maintain conversation history.</div>", unsafe_allow_html=True)
st.markdown("<div class='arg-box'><b>st.chat_input(placeholder, key)</b> — returns typed message or None<br><b>st.chat_message(name)</b> — name is 'user' or 'assistant' (or any string)<br>• Use inside a <b>with</b> block to write the message content</div>", unsafe_allow_html=True)

st.code("""
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Accept new input
if prompt := st.chat_input("Type a message..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    reply = f"Echo: {prompt}"
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.write(reply)
""", language="python")

st.markdown("<div class='sub-title'>▸ Live Output</div>", unsafe_allow_html=True)
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if prompt := st.chat_input("Type a message..."):
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    reply = f"Echo: {prompt}"
    st.session_state.chat_history.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.write(reply)

st.markdown("<hr class='divider'/>", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════
# 18. HTML STYLING
# ════════════════════════════════════════════════════════════════════════
st.markdown("<div class='section-title'>🎨 18. HTML & Styling</div>", unsafe_allow_html=True)
st.markdown("<div class='concept-box'>Use <b>st.markdown()</b> with <b>unsafe_allow_html=True</b> to inject custom HTML and CSS for advanced styling beyond Streamlit's defaults.</div>", unsafe_allow_html=True)
st.markdown("<div class='arg-box'><b>st.markdown(body, unsafe_allow_html)</b><br>• body — markdown string or HTML string<br>• unsafe_allow_html=True — required to render raw HTML tags<br><b>st.html(body)</b> — (Streamlit 1.31+) dedicated HTML renderer</div>", unsafe_allow_html=True)

st.code("""
st.markdown("<h3 style='color:#0f62fe;'>Blue Heading</h3>", unsafe_allow_html=True)

st.markdown(\"\"\"
<div style='background:#1e3a5f; color:white; padding:12px; border-radius:8px;'>
    Custom styled card content
</div>
\"\"\", unsafe_allow_html=True)

# Inject global CSS
st.markdown(\"\"\"
<style>
    .stButton > button { background: #0f62fe; color: white; border-radius: 8px; }
</style>
\"\"\", unsafe_allow_html=True)
""", language="python")

st.markdown("<div class='sub-title'>▸ Live Output</div>", unsafe_allow_html=True)
st.markdown("<h3 style='color:#0f62fe;'>Blue Heading</h3>", unsafe_allow_html=True)
st.markdown("""
<div style='background:#1e3a5f; color:white; padding:12px 18px; border-radius:8px; margin:8px 0;'>
    ✨ Custom styled card — use HTML for anything Streamlit can't do natively.
</div>
""", unsafe_allow_html=True)

st.markdown("<hr class='divider'/>", unsafe_allow_html=True)



# ════════════════════════════════════════════════════════════════════════
# 19. STREAMING — st.write_stream()
# ════════════════════════════════════════════════════════════════════════
st.markdown("<div class='section-title'>🌊 19. Streaming — st.write_stream()</div>", unsafe_allow_html=True)
 
st.markdown("""
<div class='concept-box'>
    <b>st.write_stream()</b> consumes a Python generator (or any iterable) and prints each yielded
    chunk to the screen as it arrives — producing a live typing / streaming effect.<br><br>
    This is the standard way to stream LLM responses (OpenAI, Anthropic, etc.) in Streamlit.
    The function returns the full assembled string once streaming completes.
</div>
""", unsafe_allow_html=True)
 
st.markdown("<div class='arg-box'><b>st.write_stream(stream)</b><br>• stream — a generator, iterator, or any iterable that yields string chunks<br>• Also accepts: OpenAI stream objects, Anthropic stream objects directly<br>• Returns: the full concatenated string after streaming finishes</div>", unsafe_allow_html=True)
 
st.code("""
import time
 
# 1. Basic generator-based stream
def stream_text(text, delay=0.03):
    for word in text.split(" "):
        yield word + " "
        time.sleep(delay)
 
if st.button("▶ Stream Text"):
    response = st.write_stream(stream_text("Hello! This text streams word by word."))
    # response now holds the full string
 
 
# 2. Character-by-character (slower, typewriter feel)
def typewriter(text, delay=0.02):
    for char in text:
        yield char
        time.sleep(delay)
 
if st.button("▶ Typewriter Effect"):
    st.write_stream(typewriter("Typing... one... character... at... a... time."))
 
 
# 3. Simulated LLM chunk streaming
def fake_llm_stream(prompt):
    reply = f"You asked: '{prompt}'. Here is a streamed answer with variable chunk sizes."
    words = reply.split()
    for i, word in enumerate(words):
        chunk_size = random.randint(1, 3)        # simulate variable chunk sizes
        yield " ".join(words[i:i+chunk_size]) + " "
        time.sleep(random.uniform(0.03, 0.08))   # simulate network jitter
        if i + chunk_size >= len(words):
            break
 
if st.button("▶ Fake LLM Stream"):
    st.write_stream(fake_llm_stream("What is Streamlit?"))
 
 
# 4. Real OpenAI streaming (requires: pip install openai)
import openai
client = openai.OpenAI(api_key="YOUR_API_KEY")
 
def openai_stream(prompt):
    stream = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        stream=True,
    )
    for chunk in stream:
        delta = chunk.choices[0].delta.content
        if delta:
            yield delta
 
if st.button("▶ OpenAI Stream"):
    st.write_stream(openai_stream("Explain Streamlit in 2 sentences."))
""", language="python")
 
st.markdown("<div class='sub-title'>▸ Live Output</div><div class='live-box'>", unsafe_allow_html=True)
 
sample_text = "Streamlit makes it incredibly easy to build and share beautiful data apps in pure Python — no front-end experience needed."
 
def stream_words(text, delay=0.05):
    for word in text.split(" "):
        yield word + " "
        time.sleep(delay)
 
def stream_chars(text, delay=0.025):
    for char in text:
        yield char
        time.sleep(delay)
 
def fake_llm_stream(prompt, delay_min=0.03, delay_max=0.09):
    reply = f"You asked: \"{prompt}\". Streamlit is a fast, open-source Python framework that turns scripts into shareable web apps instantly."
    words = reply.split()
    i = 0
    while i < len(words):
        chunk_size = random.randint(1, 3)
        yield " ".join(words[i:i+chunk_size]) + " "
        time.sleep(random.uniform(delay_min, delay_max))
        i += chunk_size
 
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🌊 Word Stream"):
        st.write_stream(stream_words(sample_text))
with col2:
    if st.button("⌨️ Typewriter"):
        st.write_stream(stream_chars("Typing one char at a time..."))
with col3:
    if st.button("🤖 Fake LLM"):
        st.write_stream(fake_llm_stream("What is Streamlit?"))
 
st.markdown("</div>", unsafe_allow_html=True)
st.markdown("<hr class='divider'/>", unsafe_allow_html=True)
 
 
# ════════════════════════════════════════════════════════════════════════
# 20. STREAMING WITH CHAT (Full Chat Pattern)
# ════════════════════════════════════════════════════════════════════════
st.markdown("<div class='section-title'>💬 20. Streaming Inside Chat Messages</div>", unsafe_allow_html=True)
 
st.markdown("""
<div class='concept-box'>
    The most common real-world pattern: stream the assistant reply <i>inside</i> a
    <b>st.chat_message()</b> block. Use <b>st.session_state</b> to store the full response
    after streaming so it can be re-rendered on reruns without re-streaming.
</div>
""", unsafe_allow_html=True)
 
st.code("""
import time, random
 
def fake_llm_stream(prompt):
    reply = f"Sure! Here's my answer to '{prompt}': Streamlit streams responses word by word."
    for word in reply.split():
        yield word + " "
        time.sleep(random.uniform(0.04, 0.1))
 
if "stream_chat" not in st.session_state:
    st.session_state.stream_chat = []
 
# Render existing messages
for msg in st.session_state.stream_chat:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
 
# New input
if prompt := st.chat_input("Ask something..."):
    # Show & store user message
    st.session_state.stream_chat.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
 
    # Stream assistant reply
    with st.chat_message("assistant"):
        full_reply = st.write_stream(fake_llm_stream(prompt))   # streams live
 
    # Store the completed reply for future reruns
    st.session_state.stream_chat.append({"role": "assistant", "content": full_reply})
""", language="python")
 
st.markdown("<div class='sub-title'>▸ Live Output</div><div class='live-box'>", unsafe_allow_html=True)
 
def fake_llm_chat_stream(prompt):
    replies = [
        f"Great question! '{prompt}' is something I can answer with streaming text, word by word.",
        f"Sure thing! Here's a streamed response to '{prompt}': Streamlit is powerful and easy.",
        f"Interesting! Let me think about '{prompt}'... Streamlit handles streaming beautifully.",
    ]
    reply = random.choice(replies)
    for word in reply.split():
        yield word + " "
        time.sleep(random.uniform(0.04, 0.09))
 
if "stream_chat" not in st.session_state:
    st.session_state.stream_chat = []
 
if st.button("🗑️ Clear Chat"):
    st.session_state.stream_chat = []
    st.rerun()
 
for msg in st.session_state.stream_chat:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
 
if prompt := st.chat_input("Ask something and watch it stream..."):
    st.session_state.stream_chat.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    with st.chat_message("assistant"):
        full_reply = st.write_stream(fake_llm_chat_stream(prompt))
    st.session_state.stream_chat.append({"role": "assistant", "content": full_reply})
 
st.markdown("</div>", unsafe_allow_html=True)
st.markdown("<hr class='divider'/>", unsafe_allow_html=True)
 
 
# ════════════════════════════════════════════════════════════════════════
# 21. STREAMING WITH st.empty() — Manual Typing Effect
# ════════════════════════════════════════════════════════════════════════
st.markdown("<div class='section-title'>📦 21. Manual Typing with st.empty()</div>", unsafe_allow_html=True)
 
st.markdown("""
<div class='concept-box'>
    <b>st.empty()</b> creates a single placeholder slot that can be <i>overwritten</i> repeatedly.
    This gives you full control over the typing effect — useful when you want custom styling,
    a blinking cursor, markdown rendering mid-stream, or any non-standard display.
</div>
""", unsafe_allow_html=True)
 
st.markdown("<div class='arg-box'><b>placeholder = st.empty()</b><br>• placeholder.write(x) — overwrite with text / markdown<br>• placeholder.markdown(x) — overwrite with styled markdown<br>• placeholder.empty() — clear the slot completely<br>• Works with: write, markdown, code, dataframe, image, and more</div>", unsafe_allow_html=True)
 
st.code("""
import time
 
placeholder = st.empty()
full_text = "This text appears character by character using st.empty()!"
 
# Method A — character by character with blinking cursor
typed = ""
for char in full_text:
    typed += char
    placeholder.markdown(typed + "▌")   # ▌ acts as blinking cursor
    time.sleep(0.03)
placeholder.markdown(typed)             # remove cursor at end
 
 
# Method B — word by word with custom styled container
words = "Streaming words with bold **markdown** and `code` rendered live!".split()
built = ""
for word in words:
    built += word + " "
    placeholder.markdown(f"> {built}▌")
    time.sleep(0.07)
placeholder.markdown(f"> {built}")
 
 
# Method C — overwrite with completely different content when done
placeholder.success("✅ Streaming complete!")
""", language="python")
 
st.markdown("<div class='sub-title'>▸ Live Output</div><div class='live-box'>", unsafe_allow_html=True)
 
demo_text = "This text appears character by character using st.empty() — giving you full control over the cursor and styling!"
demo_words = "You can also stream **bold text**, `inline code`, and > blockquotes word by word with live markdown rendering!"
 
col_a, col_b, col_c = st.columns(3)
with col_a:
    if st.button("⌨️ Char + Cursor"):
        ph = st.empty()
        typed = ""
        for char in demo_text:
            typed += char
            ph.markdown(typed + " ▌")
            time.sleep(0.018)
        ph.markdown(typed)
 
with col_b:
    if st.button("📝 Word + Markdown"):
        ph = st.empty()
        built = ""
        for word in demo_words.split():
            built += word + " "
            ph.markdown(f"> {built}▌")
            time.sleep(0.06)
        ph.markdown(f"> {built}")
 
with col_c:
    if st.button("✅ Then Replace"):
        ph = st.empty()
        typed = ""
        short = "Streaming... almost done..."
        for char in short:
            typed += char
            ph.markdown(typed + " ▌")
            time.sleep(0.03)
        time.sleep(0.3)
        ph.success("✅ Done! Placeholder replaced entirely.")
 
st.markdown("</div>", unsafe_allow_html=True)
st.markdown("<hr class='divider'/>", unsafe_allow_html=True)
 
 
# ════════════════════════════════════════════════════════════════════════
# 22. STREAMING WITH st.status() — Live Step Updates
# ════════════════════════════════════════════════════════════════════════
st.markdown("<div class='section-title'>🔄 22. Live Step Updates with st.status()</div>", unsafe_allow_html=True)
 
st.markdown("""
<div class='concept-box'>
    <b>st.status()</b> shows an expandable container that displays live step-by-step progress
    while a long task runs. It starts in a <i>running</i> state and transitions to
    <i>complete</i> or <i>error</i> when you call <b>.update()</b>.
    Perfect for multi-step pipelines, data loading, or agentic workflows.
</div>
""", unsafe_allow_html=True)
 
st.markdown("<div class='arg-box'><b>with st.status(label, expanded, state) as status:</b><br>• label — text shown in the header bar<br>• expanded=True — shows steps as they run<br>• state — 'running' | 'complete' | 'error'<br>• status.update(label, state, expanded) — call at the end to finalise</div>", unsafe_allow_html=True)
 
st.code("""
import time
 
with st.status("⚙️ Processing pipeline...", expanded=True) as status:
    st.write("🔍 Step 1: Validating inputs...")
    time.sleep(1)
 
    st.write("📥 Step 2: Loading data...")
    time.sleep(1.5)
 
    st.write("🧠 Step 3: Running model inference...")
    time.sleep(2)
 
    st.write("💾 Step 4: Saving results...")
    time.sleep(1)
 
    status.update(label="✅ Pipeline complete!", state="complete", expanded=False)
 
st.success("All steps finished successfully.")
""", language="python")
 
st.markdown("<div class='sub-title'>▸ Live Output</div><div class='live-box'>", unsafe_allow_html=True)
 
steps_ok = [
    ("🔍 Validating inputs...",        0.6),
    ("📥 Loading dataset...",          0.9),
    ("🧹 Cleaning & transforming...",  0.7),
    ("🧠 Running model inference...",  1.1),
    ("💾 Saving results to disk...",   0.6),
]
steps_err = [
    ("🔍 Validating inputs...",  0.5),
    ("📥 Loading dataset...",    0.8),
    ("💥 Connection refused — database unreachable.", 0.3),
]
 
col1, col2 = st.columns(2)
with col1:
    if st.button("▶ Run Pipeline (success)"):
        with st.status("⚙️ Running pipeline...", expanded=True) as status:
            for label, delay in steps_ok:
                st.write(label)
                time.sleep(delay)
            status.update(label="✅ Pipeline complete!", state="complete", expanded=False)
        st.success("All steps finished successfully.")
 
with col2:
    if st.button("▶ Run Pipeline (error)"):
        with st.status("⚙️ Running pipeline...", expanded=True) as status:
            for label, delay in steps_err:
                st.write(label)
                time.sleep(delay)
            status.update(label="❌ Pipeline failed.", state="error", expanded=True)
        st.error("Pipeline stopped due to a connection error.")
 
st.markdown("</div>", unsafe_allow_html=True)
st.markdown("<hr class='divider'/>", unsafe_allow_html=True)
 
 
# ════════════════════════════════════════════════════════════════════════
# 23. FRAGMENT — Partial Re-runs (st.fragment)
# ════════════════════════════════════════════════════════════════════════
st.markdown("<div class='section-title'>⚡ 23. st.fragment — Partial Re-runs</div>", unsafe_allow_html=True)
 
st.markdown("""
<div class='concept-box'>
    By default, Streamlit reruns the <i>entire</i> script on every interaction.
    <b>@st.fragment</b> lets you isolate a function so only that section reruns —
    leaving the rest of the page untouched. This is essential for smooth streaming
    and live-updating components inside larger apps.
</div>
""", unsafe_allow_html=True)
 
st.markdown("<div class='arg-box'><b>@st.fragment(run_every=None)</b><br>• Decorate a function — only that function reruns on interaction inside it<br>• run_every — auto-rerun interval e.g. <code>'5s'</code>, <code>'1m'</code>, or seconds as float<br>• Requires Streamlit ≥ 1.33</div>", unsafe_allow_html=True)
 
st.code("""
import streamlit as st
import time, random
 
# This fragment reruns independently — the rest of the page stays frozen
@st.fragment
def live_ticker():
    cols = st.columns(3)
    cols[0].metric("BTC", f"${random.randint(60000,70000):,}", f"{random.uniform(-2,2):.2f}%")
    cols[1].metric("ETH", f"${random.randint(3000,4000):,}",  f"{random.uniform(-2,2):.2f}%")
    cols[2].metric("SOL", f"${random.randint(130,180):,}",    f"{random.uniform(-2,2):.2f}%")
    if st.button("🔄 Refresh Prices"):
        pass   # clicking this only reruns live_ticker(), not the whole page
 
live_ticker()
 
 
# Auto-refreshing fragment — updates every 3 seconds automatically
@st.fragment(run_every="3s")
def auto_clock():
    st.write(f"🕐 Current time: {time.strftime('%H:%M:%S')}")
 
auto_clock()
""", language="python")
 
st.markdown("<div class='sub-title'>▸ Live Output</div><div class='live-box'>", unsafe_allow_html=True)
 
@st.fragment
def live_ticker():
    st.caption("👇 Clicking Refresh only reruns this fragment — not the whole page")
    cols = st.columns(3)
    cols[0].metric("BTC", f"${random.randint(60000, 70000):,}", f"{random.uniform(-2, 2):.2f}%")
    cols[1].metric("ETH", f"${random.randint(3000, 4000):,}",  f"{random.uniform(-2, 2):.2f}%")
    cols[2].metric("SOL", f"${random.randint(130, 180):,}",    f"{random.uniform(-2, 2):.2f}%")
    if st.button("🔄 Refresh Prices"):
        pass
 
live_ticker()
 
@st.fragment(run_every="2s")
def auto_clock():
    st.caption(f"🕐 Auto-refreshes every 2s: **{time.strftime('%H:%M:%S')}**")
 
auto_clock()
 
st.markdown("</div>", unsafe_allow_html=True)
st.markdown("<hr class='divider'/>", unsafe_allow_html=True)
 
 
# ════════════════════════════════════════════════════════════════════════
# QUICK REFERENCE CARD
# ════════════════════════════════════════════════════════════════════════
st.markdown("<div class='section-title'>📋 Quick Reference — Streaming Cheatsheet</div>", unsafe_allow_html=True)
 
st.markdown("""
<div class='concept-box'>
<b>Choose the right tool:</b><br><br>
 
| Use Case                              | Tool                         |
|---------------------------------------|------------------------------|
| Stream LLM / generator output         | <code>st.write_stream(gen)</code>       |
| Custom typewriter with cursor/styling | <code>st.empty()</code> + overwrite     |
| Multi-step pipeline progress          | <code>st.status()</code>                |
| Isolate a section from full reruns    | <code>@st.fragment</code>               |
| Auto-refresh a section periodically   | <code>@st.fragment(run_every="Xs")</code> |
| Stream inside chat bubbles            | <code>st.chat_message</code> + <code>st.write_stream</code> |
 
</div>
""", unsafe_allow_html=True)
 
st.code("""
# Minimal streaming pattern — copy & paste ready
import streamlit as st
import time
 
def my_stream(text):
    for word in text.split():
        yield word + " "
        time.sleep(0.05)
 
if st.button("Stream"):
    result = st.write_stream(my_stream("Hello streaming world!"))
    st.write("Full text:", result)   # result holds the assembled string
""", language="python")
 
st.markdown("""
<div style='text-align:center; padding:20px; color:#64748b; font-size:0.85rem;'>
    ⚡ Streamlit Streaming Extension &nbsp;|&nbsp; Append to your existing guide
</div>
""", unsafe_allow_html=True)
 
 

# ─────────────────────────── FOOTER ────────────────────────────────────
st.markdown("""
<div style='text-align:center; padding: 20px; color:#94a3b8; font-size:0.85rem;'>
    🚀 Streamlit Complete Guide &nbsp;|&nbsp; Happy Building!
</div>
""", unsafe_allow_html=True)