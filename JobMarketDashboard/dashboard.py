import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Job Market Intelligence Dashboard",
    layout="wide"
)

# Read dataset
df = pd.read_csv("jobs.csv")

st.title("📊 Job Market Intelligence & Skill Gap Analysis")

menu = st.sidebar.selectbox(
    "Select Analysis",
    [
        "Overview",
        "Top Skills",
        "Salary Analysis",
        "Industry Analysis",
        "Skill Gap Analysis"
    ]
)

# OVERVIEW
if menu == "Overview":

    st.header("Project Overview")

    st.write("""
    This project uses Hadoop, Spark and Streamlit
    to analyze job market trends and identify skill gaps.
    """)

    st.subheader("Objectives")

    st.write("""
    • Analyze job market trends

    • Identify top demanded skills

    • Compare salary ranges

    • Analyze hiring industries

    • Detect skill gaps
    """)

    st.dataframe(df)

# TOP SKILLS
elif menu == "Top Skills":

    st.header("Top Skills Analysis")

    skills = df["Skill"].value_counts()

    fig, ax = plt.subplots()

    ax.bar(
        skills.index,
        skills.values
    )

    plt.xticks(rotation=45)

    st.pyplot(fig)

# SALARY ANALYSIS
elif menu == "Salary Analysis":

    st.header("Salary Analysis")

    st.dataframe(
        df[["Role","Salary"]]
    )

    fig, ax = plt.subplots()

    ax.bar(
        df["Role"],
        df["Salary"]
    )

    plt.xticks(rotation=45)

    st.pyplot(fig)

# INDUSTRY ANALYSIS
elif menu == "Industry Analysis":

    st.header("Industry Analysis")

    industries = df["Industry"].value_counts()

    fig, ax = plt.subplots()

    ax.pie(
        industries,
        labels=industries.index,
        autopct="%1.1f%%"
    )

    st.pyplot(fig)

# SKILL GAP ANALYSIS
elif menu == "Skill Gap Analysis":

    st.header("Skill Gap Analysis")

    user_input = st.text_input(
        "Enter your skills separated by commas"
    )

    if user_input:

        required_skills = {
            "Python",
            "SQL",
            "Spark",
            "AWS"
        }

        user_skills = {
            skill.strip()
            for skill in user_input.split(",")
        }

        missing = (
            required_skills -
            user_skills
        )

        st.success(
            f"Skills Entered: {len(user_skills)}"
        )

        st.warning(
            f"Missing Skills: {list(missing)}"
        )

        if len(missing) > 0:

            st.subheader(
                "Recommended Learning Path"
            )

            for skill in missing:

                st.write(
                    f"Learn {skill}"
                )