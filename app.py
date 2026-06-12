import streamlit as st
import pandas as pd

st.set_page_config(page_title="Student Score Grader", page_icon="📚")

st.title("📚 Automated Student Test Score Grader")

# Sample Data
students = {
    "Name": [
        "Alice", "Bob", "Charlie", "David", "Emma",
        "Frank", "Grace", "Henry", "Ivy", "Jack"
    ],
    "Score": [85, 42, 78, 90, 56, 33, 67, 95, 48, 72]
}

df = pd.DataFrame(students)

# Grade Assignment Function
def assign_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"

# Add Grade Column
df["Grade"] = df["Score"].apply(assign_grade)

# Pass/Fail Status
df["Status"] = df["Score"].apply(
    lambda x: "Pass" if x >= 50 else "Fail"
)

# Sidebar Filters
st.sidebar.header("Filters")

grade_filter = st.sidebar.multiselect(
    "Select Grade",
    options=sorted(df["Grade"].unique()),
    default=sorted(df["Grade"].unique())
)

status_filter = st.sidebar.multiselect(
    "Select Status",
    options=["Pass", "Fail"],
    default=["Pass", "Fail"]
)

min_score = st.sidebar.slider(
    "Minimum Score",
    min_value=0,
    max_value=100,
    value=0
)

# Apply Filters
filtered_df = df[
    (df["Grade"].isin(grade_filter)) &
    (df["Status"].isin(status_filter)) &
    (df["Score"] >= min_score)
]

# Summary Statistics
average_score = df["Score"].mean()
highest_score = df["Score"].max()
lowest_score = df["Score"].min()
passed_count = len(df[df["Status"] == "Pass"])
failed_count = len(df[df["Status"] == "Fail"])

# Metrics
st.subheader("📊 Summary Report")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Average Score", f"{average_score:.2f}")

with col2:
    st.metric("Highest Score", highest_score)

with col3:
    st.metric("Lowest Score", lowest_score)

col4, col5 = st.columns(2)

with col4:
    st.metric("Passed Students", passed_count)

with col5:
    st.metric("Failed Students", failed_count)

# Filtered Student Records
st.subheader("📋 Student Records")

st.dataframe(
    filtered_df,
    use_container_width=True
)

# Grade Distribution
st.subheader("📈 Grade Distribution")

grade_counts = df["Grade"].value_counts().sort_index()

st.bar_chart(grade_counts)

# Show Above Average Students
st.subheader("⭐ Students Above Average")

above_avg = df[df["Score"] > average_score]

st.dataframe(
    above_avg,
    use_container_width=True
)

# Download Button
csv = filtered_df.to_csv(index=False)

st.download_button(
    label="📥 Download Filtered Data",
    data=csv,
    file_name="student_scores.csv",
    mime="text/csv"
)