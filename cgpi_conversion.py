import streamlit as st

# Function to convert CGPI to percentage based on conditions
def cgpi_to_percentage(cgpi):
    if cgpi < 7:
        percentage = 7.1 * cgpi + 12
    else:
        percentage = 7.4 * cgpi + 12
    return round(percentage)

# Function to calculate overall percentage from all semester CGPIs
def calculate_overall_percentage(cgpis):
    total_cgpi = sum(cgpis)
    avg_cgpi = total_cgpi / len(cgpis)
    return cgpi_to_percentage(avg_cgpi)

# Streamlit UI
st.title("CGPI to Percentage Converter")
st.write("This application converts your CGPI to Percentage based on the University of Mumbai formula.")

# Initialize session state to store CGPI values
if 'cgpis' not in st.session_state:
    st.session_state.cgpis = []

# Input for the number of semesters
semesters = st.number_input("Enter the number of semesters:", min_value=1, step=1, value=len(st.session_state.cgpis) or 1)

# Adjust session state based on the number of semesters
if len(st.session_state.cgpis) < semesters:
    st.session_state.cgpis.extend([0.0] * (semesters - len(st.session_state.cgpis)))
elif len(st.session_state.cgpis) > semesters:
    st.session_state.cgpis = st.session_state.cgpis[:semesters]

# Input fields for CGPIs of each semester
for i in range(semesters):
    st.session_state.cgpis[i] = st.number_input(f"Enter CGPI for Semester {i+1}:", min_value=0.0, max_value=10.0, step=0.01, value=st.session_state.cgpis[i])

# Button to trigger the percentage calculation
if st.button("Calculate Overall Percentage"):
    if st.session_state.cgpis:
        overall_percentage = calculate_overall_percentage(st.session_state.cgpis)
        st.success(f"Overall Percentage: {overall_percentage}%")

# Footer
st.markdown("---")
st.markdown("**Made by Amey Mali** | Contact: [ameymali54@icloud.com](mailto:ameymali54@icloud.com)")
