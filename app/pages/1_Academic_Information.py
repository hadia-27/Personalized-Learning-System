import streamlit as st
import pandas as pd
import joblib

from pathlib import Path


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Academic Information",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CONSTANTS
# ============================================================

ACADEMIC_AREA_PLACEHOLDER = "Select an academic area"

DEFAULT_STUDY_HOURS = 20
DEFAULT_ATTENDANCE = 75.0
DEFAULT_PAST_EXAM = 70

DEFAULT_ACADEMIC_GOAL = "Improve academic performance"


# ============================================================
# ACADEMIC PROFILE TAXONOMY
# ============================================================

academic_profiles = {

    "Business & Management": {
        "confidence": [
            "Business Analysis",
            "Quantitative Skills",
            "Strategic Thinking"
        ],
        "interests": [
            "Marketing",
            "Finance",
            "Accounting",
            "Entrepreneurship",
            "Human Resource Management",
            "Operations Management",
            "Business Strategy"
        ]
    },

    "Computing & IT": {
        "confidence": [
            "Programming",
            "Databases",
            "Computer Systems"
        ],
        "interests": [
            "Software Development",
            "Web Development",
            "Databases",
            "Cybersecurity",
            "Cloud Computing",
            "Computer Networks",
            "Mobile App Development"
        ]
    },

    "Data Science & AI": {
        "confidence": [
            "Programming",
            "Mathematics & Statistics",
            "Data Analysis"
        ],
        "interests": [
            "Machine Learning",
            "Artificial Intelligence",
            "Data Analysis",
            "Deep Learning",
            "Data Visualization",
            "Big Data",
            "Natural Language Processing"
        ]
    },

    "Engineering & Technology": {
        "confidence": [
            "Mathematics",
            "Technical Problem Solving",
            "Engineering Analysis"
        ],
        "interests": [
            "Mechanical Engineering",
            "Electrical Engineering",
            "Electronics",
            "Robotics",
            "Automation",
            "CAD & Engineering Design",
            "Renewable Energy"
        ]
    },

    "Psychology & Health Sciences": {
        "confidence": [
            "Research Methods",
            "Statistical Analysis",
            "Critical Evaluation"
        ],
        "interests": [
            "Cognitive Psychology",
            "Social Psychology",
            "Mental Health",
            "Health Psychology",
            "Human Development",
            "Neuroscience",
            "Psychological Research"
        ]
    },

    "Law & Criminology": {
        "confidence": [
            "Academic Writing",
            "Critical Analysis",
            "Legal Research"
        ],
        "interests": [
            "Criminal Law",
            "International Law",
            "Human Rights",
            "Criminology",
            "Cybercrime",
            "Business Law",
            "Legal Research"
        ]
    },

    "Media & Communications": {
        "confidence": [
            "Communication Skills",
            "Media Analysis",
            "Research Skills"
        ],
        "interests": [
            "Digital Media",
            "Journalism",
            "Public Relations",
            "Advertising",
            "Social Media",
            "Film & Television",
            "Media Production"
        ]
    },

    "Design & Creative Arts": {
        "confidence": [
            "Creative Thinking",
            "Design Skills",
            "Visual Communication"
        ],
        "interests": [
            "Graphic Design",
            "UX/UI Design",
            "Illustration",
            "Animation",
            "Photography",
            "3D Design",
            "Digital Art"
        ]
    },

    "Mathematics & Statistics": {
        "confidence": [
            "Mathematical Reasoning",
            "Statistical Analysis",
            "Problem Solving"
        ],
        "interests": [
            "Calculus",
            "Algebra",
            "Probability",
            "Statistics",
            "Mathematical Modelling",
            "Data Analysis",
            "Discrete Mathematics"
        ]
    },

    "Social Sciences & Humanities": {
        "confidence": [
            "Academic Writing",
            "Critical Analysis",
            "Research Skills"
        ],
        "interests": [
            "Sociology",
            "Politics",
            "History",
            "Philosophy",
            "International Relations",
            "Cultural Studies",
            "Social Research"
        ]
    }
}


ACADEMIC_GOALS = [
    DEFAULT_ACADEMIC_GOAL,
    "Strengthen weak academic areas",
    "Build skills for future study",
    "Build skills for a future career",
    "Develop advanced subject knowledge"
]


# ============================================================
# SESSION STATE
# ============================================================

def initialise_form_state():

    defaults = {
        "academic_area_input": ACADEMIC_AREA_PLACEHOLDER,
        "study_hours_input": DEFAULT_STUDY_HOURS,
        "attendance_input": DEFAULT_ATTENDANCE,
        "past_exam_input": DEFAULT_PAST_EXAM,
        "academic_goal_input": DEFAULT_ACADEMIC_GOAL,
        "interests_input": [],
        "form_errors": {}
    }

    for key, value in defaults.items():

        if key not in st.session_state:
            st.session_state[key] = value


initialise_form_state()


# ============================================================
# ERROR HELPERS
# ============================================================

def clear_field_error(field_name):

    errors = st.session_state.get(
        "form_errors",
        {}
    ).copy()

    errors.pop(
        field_name,
        None
    )

    st.session_state[
        "form_errors"
    ] = errors


def show_inline_error(field_name):

    errors = st.session_state.get(
        "form_errors",
        {}
    )

    if field_name in errors:

        st.html(
            f"""
            <div class="inline-field-error">

                <span class="inline-error-icon">
                    !
                </span>

                <span>
                    {errors[field_name]}
                </span>

            </div>
            """
        )


# ============================================================
# RESET FUNCTIONS
# ============================================================

def remove_confidence_widget_state():

    confidence_keys = [
        key
        for key in list(
            st.session_state.keys()
        )
        if str(key).startswith(
            "confidence_"
        )
    ]

    for key in confidence_keys:
        del st.session_state[key]


def clear_downstream_results():

    downstream_keys = [
        "academic_area",
        "study_hours",
        "attendance",
        "past_exam_score",
        "confidence_scores",
        "interests",
        "academic_goal",

        "prediction",
        "pass_probability",
        "fail_probability",

        "priority_skill",
        "priority_skills",
        "preferred_difficulties",
        "recommendations",
        "top_recommendations",
        "learning_path",
        "pathway_resources"
    ]

    for key in downstream_keys:

        st.session_state.pop(
            key,
            None
        )


def clear_academic_form():

    remove_confidence_widget_state()
    clear_downstream_results()

    st.session_state[
        "academic_area_input"
    ] = ACADEMIC_AREA_PLACEHOLDER

    st.session_state[
        "study_hours_input"
    ] = DEFAULT_STUDY_HOURS

    st.session_state[
        "attendance_input"
    ] = DEFAULT_ATTENDANCE

    st.session_state[
        "past_exam_input"
    ] = DEFAULT_PAST_EXAM

    st.session_state[
        "academic_goal_input"
    ] = DEFAULT_ACADEMIC_GOAL

    st.session_state[
        "interests_input"
    ] = []

    st.session_state[
        "form_errors"
    ] = {}


def reset_application():

    st.session_state.clear()


def academic_area_changed():

    remove_confidence_widget_state()

    st.session_state[
        "interests_input"
    ] = []

    clear_downstream_results()

    clear_field_error(
        "academic_area"
    )


# ============================================================
# MODEL
# ============================================================

BASE_DIR = Path(
    __file__
).resolve().parents[2]

MODEL_PATH = (
    BASE_DIR
    / "models"
    / "logistic_regression_model.pkl"
)

SCALER_PATH = (
    BASE_DIR
    / "models"
    / "standard_scaler.pkl"
)

model = joblib.load(
    MODEL_PATH
)

scaler = joblib.load(
    SCALER_PATH
)


# ============================================================
# CSS
# ============================================================

st.html("""
<style>

* {
    box-sizing: border-box;
}

html,
body {
    margin: 0;
    padding: 0;
    overflow-x: hidden;
}

.stApp {
    min-height: 100vh;
    background: #f6f8fc;
    color: #14213d;
}

html,
body,
button,
input,
textarea,
select {
    font-family:
        Inter,
        "Segoe UI",
        Arial,
        sans-serif;
}


/* ==========================================================
   STREAMLIT DEFAULTS
========================================================== */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header[data-testid="stHeader"] {
    height: 0 !important;
    min-height: 0 !important;
    background: transparent !important;
}

[data-testid="stSidebarNav"] {
    display: none !important;
}


/* ==========================================================
   MAIN
========================================================== */

.block-container {
    width: 100%;
    max-width: 1450px;

    margin: 0 auto;

    padding:
        0.7rem
        1.15rem
        0.75rem
        1.15rem !important;
}

main div[data-testid="stVerticalBlock"] {
    gap: 0.5rem !important;
}


/* ==========================================================
   SIDEBAR
========================================================== */

section[data-testid="stSidebar"] {
    width: 235px !important;
    min-width: 235px !important;
    max-width: 235px !important;
    height: 100vh !important;

    background:
        linear-gradient(
            180deg,
            #061a42 0%,
            #08275f 100%
        );

    overflow: hidden !important;
}

section[data-testid="stSidebar"] > div {
    height: 100vh !important;

    padding:
        0.8rem
        1rem
        0.9rem
        1rem !important;

    overflow: hidden !important;
}

section[data-testid="stSidebar"]
div[data-testid="stVerticalBlock"] {

    height: 100% !important;

    display: flex !important;
    flex-direction: column !important;

    gap: 0.18rem !important;
}


/* Academic icon */

.sidebar-academic-mark {
    width: 100%;

    display: flex;

    justify-content: center;

    align-items: center;

    margin:
        0.1rem
        0
        0.65rem
        0;
}

.academic-icon-badge {
    width: 52px;
    height: 52px;

    display: flex;

    align-items: center;

    justify-content: center;

    border-radius: 50%;

    background:
        linear-gradient(
            145deg,
            rgba(42,114,226,0.42),
            rgba(14,72,164,0.18)
        );

    border:
        1px solid
        rgba(110,166,250,0.45);

    font-size: 1.55rem;

    box-shadow:
        0 0 0 5px
        rgba(33,103,214,0.06),
        0 8px 22px
        rgba(0,55,150,0.22);
}


/* Navigation */

section[data-testid="stSidebar"]
[data-testid="stPageLink"] {
    margin: 0 !important;
}

section[data-testid="stSidebar"]
[data-testid="stPageLink"] a {

    position: relative;

    width: 100%;

    min-height: 2.55rem;

    display: flex;

    align-items: center;

    padding:
        0.5rem
        0.8rem;

    border:
        1px solid
        transparent;

    border-radius: 7px;

    background:
        transparent !important;

    text-decoration:
        none !important;
}

section[data-testid="stSidebar"]
[data-testid="stPageLink"] a p {

    margin: 0 !important;

    color:
        #dce7f7 !important;

    font-size:
        0.76rem !important;

    font-weight:
        560 !important;
}

section[data-testid="stSidebar"]
[data-testid="stPageLink"] a::before {

    content: "";

    position: absolute;

    left: 0;

    top: 8px;

    bottom: 8px;

    width: 3px;

    border-radius:
        0
        4px
        4px
        0;

    background:
        rgba(
            100,
            157,
            239,
            0.20
        );
}

section[data-testid="stSidebar"]
[data-testid="stPageLink"] a[aria-current="page"] {

    background:
        linear-gradient(
            90deg,
            rgba(30,103,213,0.26),
            rgba(31,102,204,0.12)
        ) !important;

    border:
        1px solid
        rgba(103,160,244,0.20);
}

section[data-testid="stSidebar"]
[data-testid="stPageLink"] a[aria-current="page"] p {

    color:
        #ffffff !important;

    font-weight:
        680 !important;
}

section[data-testid="stSidebar"]
[data-testid="stPageLink"] a[aria-current="page"]::before {

    background:
        #4392ff;
}


/* Sidebar bottom */

.sidebar-bottom-anchor {
    height: 1px;
}

section[data-testid="stSidebar"]
div[data-testid="stElementContainer"]:has(.sidebar-bottom-anchor) {

    flex:
        1
        1
        auto !important;
}

.sidebar-divider {
    height: 1px;

    margin-bottom:
        0.55rem;

    background:
        linear-gradient(
            90deg,
            transparent,
            rgba(255,255,255,0.16),
            transparent
        );
}


/* Clear Session */

section[data-testid="stSidebar"]
.st-key-sidebar_clear_session {

    width: 100% !important;
}

section[data-testid="stSidebar"]
.st-key-sidebar_clear_session button {

    width: 100% !important;

    height:
        2.25rem !important;

    min-height:
        2.25rem !important;

    background:
        rgba(
            255,
            255,
            255,
            0.025
        ) !important;

    border:
        1px solid
        rgba(
            153,
            184,
            232,
            0.30
        ) !important;

    border-radius:
        7px !important;

    color:
        #ffffff !important;

    font-size:
        0.64rem !important;

    font-weight:
        600 !important;

    box-shadow:
        none !important;
}

section[data-testid="stSidebar"]
.st-key-sidebar_clear_session button * {

    color:
        #ffffff !important;

    -webkit-text-fill-color:
        #ffffff !important;
}


/* Privacy */

.privacy-card {

    margin-top:
        0.65rem;

    padding:
        0.75rem;

    border:
        1px solid
        rgba(
            147,
            176,
            220,
            0.19
        );

    border-radius:
        8px;

    background:
        rgba(
            255,
            255,
            255,
            0.025
        );
}

.privacy-title {

    margin-bottom:
        0.32rem;

    color:
        #ffffff;

    font-size:
        0.65rem;

    font-weight:
        700;
}

.privacy-text {

    color:
        #c3d0e3;

    font-size:
        0.55rem;

    line-height:
        1.45;
}


/* ==========================================================
   HEADER
========================================================== */

.page-top-grid {

    display: grid;

    grid-template-columns:
        1.05fr
        0.95fr;

    gap: 1rem;

    align-items:
        stretch;
}

.page-heading-panel {

    padding:
        0.65rem
        0.25rem;

    display: flex;

    flex-direction:
        column;

    justify-content:
        center;
}

.page-title {

    margin:
        0
        0
        0.3rem
        0;

    color:
        #102347;

    font-size:
        1.75rem;

    line-height:
        1.05;

    font-weight:
        820;
}

.page-subtitle {

    margin: 0;

    max-width:
        590px;

    color:
        #68768e;

    font-size:
        0.74rem;

    line-height:
        1.65;
}


/* Why card */

.why-card {

    display: flex;

    align-items:
        flex-start;

    gap: 0.75rem;

    padding:
        0.85rem
        1rem;

    border:
        1px solid
        #d8e5f7;

    border-radius:
        10px;

    background:
        linear-gradient(
            135deg,
            #f4f8ff,
            #edf4ff
        );
}

.why-icon {

    width:
        30px;

    height:
        30px;

    flex:
        0 0
        30px;

    display: flex;

    align-items:
        center;

    justify-content:
        center;

    border:
        2px solid
        #1767e8;

    border-radius:
        50%;

    color:
        #1767e8;

    font-size:
        0.75rem;

    font-weight:
        800;
}

.why-title {

    margin-bottom:
        0.25rem;

    color:
        #1767e8;

    font-size:
        0.72rem;

    font-weight:
        750;
}

.why-text {

    color:
        #56677f;

    font-size:
        0.62rem;

    line-height:
        1.6;
}


/* ==========================================================
   SECTION HEADINGS
========================================================== */

.section-heading {

    display: flex;

    align-items:
        center;

    gap:
        0.55rem;

    margin-bottom:
        0.6rem;
}

.section-badge {

    width:
        28px;

    height:
        28px;

    flex:
        0 0
        28px;

    display: flex;

    align-items:
        center;

    justify-content:
        center;

    border-radius:
        50%;

    color:
        #ffffff;

    font-size:
        0.66rem;

    font-weight:
        750;
}

.badge-blue {
    background:
        #1767e8;
}

.badge-purple {
    background:
        #815ee8;
}

.badge-orange {
    background:
        #f2a126;
}

.badge-pink {
    background:
        #e85a9e;
}

.section-title {

    color:
        #172744;

    font-size:
        0.92rem;

    font-weight:
        780;
}

.section-help {

    margin-top:
        0.12rem;

    color:
        #7d899d;

    font-size:
        0.6rem;
}


/* ==========================================================
   CARDS
========================================================== */

div[data-testid="stVerticalBlockBorderWrapper"] {

    border:
        1px solid
        #dfe7f2 !important;

    border-radius:
        10px !important;

    background:
        #ffffff !important;

    box-shadow:
        0 2px 9px
        rgba(20,50,90,0.03);

    overflow:
        visible !important;
}

div[data-testid="stVerticalBlockBorderWrapper"] > div {

    padding:
        0.9rem
        1rem !important;

    background:
        #ffffff !important;
}


/* ==========================================================
   LABELS
========================================================== */

label[data-testid="stWidgetLabel"] p {

    color:
        #263955 !important;

    font-size:
        0.67rem !important;

    font-weight:
        650 !important;
}


/* ==========================================================
   SELECTBOX
========================================================== */

main [data-testid="stSelectbox"]
div[data-baseweb="select"] > div {

    min-height:
        2.65rem !important;

    background:
        #ffffff !important;

    color:
        #17345a !important;

    border:
        1px solid
        #b7cae2 !important;

    border-radius:
        8px !important;
}

main [data-testid="stSelectbox"]
div[data-baseweb="select"] * {

    color:
        #17345a !important;

    -webkit-text-fill-color:
        #17345a !important;
}

.st-key-academic_area_input
div[data-baseweb="select"] > div {

    background:
        #f5f9ff !important;

    border-color:
        #b9d1ef !important;
}

.st-key-academic_goal_input
div[data-baseweb="select"] > div {

    background:
        #fffaf2 !important;

    border-color:
        #ead3a6 !important;
}


/* ==========================================================
   NUMBER INPUTS
========================================================== */

main [data-testid="stNumberInput"]
div[data-baseweb="input"] {

    background:
        #ffffff !important;

    border:
        1px solid
        #b7cae2 !important;

    border-radius:
        8px !important;

    overflow:
        hidden !important;
}

main [data-testid="stNumberInput"] input {

    min-height:
        2.65rem !important;

    background:
        #ffffff !important;

    color:
        #17345a !important;

    -webkit-text-fill-color:
        #17345a !important;
}

main [data-testid="stNumberInput"] button {

    background:
        #eef5fd !important;

    color:
        #245582 !important;

    border:
        0 !important;

    border-left:
        1px solid
        #d2dfed !important;
}


/* ==========================================================
   MULTISELECT
========================================================== */

main [data-testid="stMultiSelect"]
div[data-baseweb="select"] > div {

    min-height:
        2.65rem !important;

    background:
        #fff8fb !important;

    border:
        1px solid
        #e9bfd4 !important;

    border-radius:
        8px !important;
}

main [data-testid="stMultiSelect"]
span[data-baseweb="tag"] {

    background:
        #fbe6f1 !important;

    border:
        1px solid
        #efb4d1 !important;

    border-radius:
        6px !important;

    color:
        #9b3368 !important;
}


/* ==========================================================
   INLINE ERRORS
========================================================== */

.inline-field-error {

    display: flex;

    align-items:
        center;

    gap:
        0.32rem;

    margin-top:
        0.32rem;

    padding:
        0.32rem
        0.45rem;

    width:
        fit-content;

    max-width:
        100%;

    background:
        #fff1f2;

    border:
        1px solid
        #f3c4ca;

    border-radius:
        6px;

    color:
        #a93b47;

    font-size:
        0.55rem;

    line-height:
        1.3;

    font-weight:
        620;
}

.inline-error-icon {

    width:
        16px;

    height:
        16px;

    min-width:
        16px;

    display: flex;

    align-items:
        center;

    justify-content:
        center;

    border-radius:
        50%;

    background:
        #dc5a66;

    color:
        #ffffff;

    font-size:
        0.47rem;

    font-weight:
        800;
}


/* ==========================================================
   INFORMATION BAR
========================================================== */

.form-information {

    display: flex;

    align-items:
        center;

    gap:
        0.5rem;

    margin-top:
        0.55rem;

    padding:
        0.55rem
        0.65rem;

    border:
        1px solid
        #d9e8fb;

    border-radius:
        7px;

    background:
        #eef5ff;

    color:
        #557094;

    font-size:
        0.58rem;
}

.info-circle {

    width:
        20px;

    height:
        20px;

    min-width:
        20px;

    display: flex;

    align-items:
        center;

    justify-content:
        center;

    border:
        1.5px solid
        #4184ec;

    border-radius:
        50%;

    color:
        #2873e5;

    font-size:
        0.55rem;

    font-weight:
        800;
}


/* ==========================================================
   CONFIDENCE
========================================================== */

.confidence-scale {

    margin:
        -0.15rem
        0
        0.5rem
        0;

    color:
        #7b879a;

    font-size:
        0.59rem;
}


/* ==========================================================
   EMPTY STATE
========================================================== */

.empty-state {

    min-height:
        100px;

    display: flex;

    justify-content:
        center;

    align-items:
        center;

    gap:
        0.8rem;

    padding:
        1rem;

    border:
        1px dashed
        #cfc6f7;

    border-radius:
        8px;

    background:
        #fcfbff;
}

.empty-state-pink {

    border-color:
        #efc5da;

    background:
        #fffafd;
}

.empty-icon {

    width:
        42px;

    height:
        42px;

    flex:
        0 0
        42px;

    display: flex;

    align-items:
        center;

    justify-content:
        center;

    border-radius:
        50%;

    background:
        #f0edff;

    color:
        #8058e5;

    font-size:
        1.05rem;
}

.empty-icon-pink {

    background:
        #fff0f7;

    color:
        #e65a9c;
}

.empty-title {

    margin-bottom:
        0.2rem;

    color:
        #243552;

    font-size:
        0.72rem;

    font-weight:
        750;
}

.empty-text {

    color:
        #778399;

    font-size:
        0.58rem;

    line-height:
        1.45;
}


/* ==========================================================
   BUTTONS
========================================================== */

main div.stButton > button {

    min-height:
        2.7rem !important;

    border-radius:
        7px !important;

    font-size:
        0.72rem !important;

    font-weight:
        700 !important;
}

.st-key-clear_form_button button {

    background:
        #edf4ff !important;

    border:
        1px solid
        #8eb5ec !important;

    color:
        #155fcf !important;
}

.st-key-clear_form_button button * {

    color:
        #155fcf !important;

    -webkit-text-fill-color:
        #155fcf !important;
}

.st-key-generate_prediction_button button {

    background:
        linear-gradient(
            135deg,
            #1767e8,
            #0d5acd
        ) !important;

    border:
        1px solid
        #1767e8 !important;

    color:
        #ffffff !important;

    box-shadow:
        0 5px 14px
        rgba(23,103,232,0.18) !important;
}

.st-key-generate_prediction_button button * {

    color:
        #ffffff !important;

    -webkit-text-fill-color:
        #ffffff !important;
}


/* ==========================================================
   FOOTER
========================================================== */

.action-footer {

    min-height:
        2.7rem;

    display: flex;

    align-items:
        center;

    color:
        #8b97aa;

    font-size:
        0.58rem;
}

</style>
""")


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.html("""
    <div class="sidebar-academic-mark">

        <div class="academic-icon-badge">
            🎓
        </div>

    </div>
    """)

    st.page_link(
        "Home.py",
        label="Home"
    )

    st.page_link(
        "pages/1_Academic_Information.py",
        label="Academic Information"
    )

    st.page_link(
        "pages/2_Prediction_Results.py",
        label="Prediction Results"
    )

    st.page_link(
        "pages/3_Recommendations.py",
        label="Recommendations"
    )

    st.page_link(
        "pages/4_Academic_Insights.py",
        label="Academic Insights"
    )

    st.page_link(
        "pages/5_About.py",
        label="About / How It Works"
    )

    st.html("""
    <div class="sidebar-bottom-anchor"></div>
    """)

    st.html("""
    <div class="sidebar-divider"></div>
    """)

    if st.button(
        "Clear Session",
        use_container_width=True,
        key="sidebar_clear_session"
    ):

        reset_application()

        st.switch_page(
            "Home.py"
        )

    st.html("""
    <div class="privacy-card">

        <div class="privacy-title">
            Your privacy matters
        </div>

        <div class="privacy-text">

            Your information is used only during this
            session to generate predictions and
            personalised recommendations.

        </div>

    </div>
    """)


# ============================================================
# HEADER
# ============================================================

st.html("""
<div class="page-top-grid">

    <div class="page-heading-panel">

        <h1 class="page-title">
            Academic Information
        </h1>

        <p class="page-subtitle">

            Provide your academic details and learning preferences.
            This information will be used to estimate your academic
            outcome and personalise your learning recommendations.

        </p>

    </div>


    <div class="why-card">

        <div class="why-icon">
            i
        </div>

        <div>

            <div class="why-title">
                Why we need this information
            </div>

            <div class="why-text">

                Your profile helps the system understand your current
                academic performance, confidence levels, interests and
                goals so that your results and recommendations remain
                relevant to you.

            </div>

        </div>

    </div>

</div>
""")


# ============================================================
# FIRST ROW
# ============================================================

background_col, performance_col = st.columns(
    [0.82, 1.18],
    gap="medium"
)


# ============================================================
# 1. ACADEMIC BACKGROUND
# ============================================================

with background_col:

    with st.container(
        border=True
    ):

        st.html("""
        <div class="section-heading">

            <div class="section-badge badge-blue">
                1
            </div>

            <div>

                <div class="section-title">
                    Academic Background
                </div>

                <div class="section-help">
                    Select the academic area that best represents your studies.
                </div>

            </div>

        </div>
        """)

        st.selectbox(
            "Academic Area / Field of Study",

            options=[
                ACADEMIC_AREA_PLACEHOLDER
            ] + list(
                academic_profiles.keys()
            ),

            key="academic_area_input",

            on_change=academic_area_changed
        )

        show_inline_error(
            "academic_area"
        )

        st.html("""
        <div class="form-information">

            <div class="info-circle">
                i
            </div>

            <div>
                Your selection determines which confidence areas
                and topics are shown below.
            </div>

        </div>
        """)


# ============================================================
# 2. ACADEMIC PERFORMANCE
# ============================================================

with performance_col:

    with st.container(
        border=True
    ):

        st.html("""
        <div class="section-heading">

            <div class="section-badge badge-blue">
                2
            </div>

            <div>

                <div class="section-title">
                    Academic Performance
                </div>

                <div class="section-help">
                    These three values are used to estimate your academic outcome.
                </div>

            </div>

        </div>
        """)

        perf1, perf2, perf3 = st.columns(
            3,
            gap="small"
        )


        with perf1:

            st.number_input(
                "Study Hours per Week",

                step=1,

                key="study_hours_input",

                on_change=clear_field_error,

                args=(
                    "study_hours",
                )
            )

            show_inline_error(
                "study_hours"
            )


        with perf2:

            st.number_input(
                "Attendance Rate (%)",

                step=1.0,

                format="%.1f",

                key="attendance_input",

                on_change=clear_field_error,

                args=(
                    "attendance",
                )
            )

            show_inline_error(
                "attendance"
            )


        with perf3:

            st.number_input(
                "Past Exam Score",

                step=1,

                key="past_exam_input",

                on_change=clear_field_error,

                args=(
                    "past_exam_score",
                )
            )

            show_inline_error(
                "past_exam_score"
            )


        st.html("""
        <div class="form-information">

            <div class="info-circle">
                i
            </div>

            <div>

                Please enter values within the supported ranges:
                10–39 study hours per week,
                50–100% attendance,
                and a past exam score between 50 and 100.

            </div>

        </div>
        """)


# ============================================================
# 3. CONFIDENCE
# ============================================================

confidence_scores = {}


with st.container(
    border=True
):

    st.html("""
    <div class="section-heading">

        <div class="section-badge badge-purple">
            3
        </div>

        <div>

            <div class="section-title">
                Confidence in Key Areas
            </div>

            <div class="section-help">

                Rate how confident you currently feel in the main
                skills associated with your selected academic area.

            </div>

        </div>

    </div>
    """)

    current_area = st.session_state[
        "academic_area_input"
    ]

    if current_area == ACADEMIC_AREA_PLACEHOLDER:

        st.html("""
        <div class="empty-state">

            <div class="empty-icon">
                ▥
            </div>

            <div>

                <div class="empty-title">
                    No academic area selected yet
                </div>

                <div class="empty-text">

                    Select your field of study above to view and rate
                    your confidence in the relevant key areas.

                </div>

            </div>

        </div>
        """)

    else:

        confidence_areas = (
            academic_profiles[
                current_area
            ]["confidence"]
        )

        st.html("""
        <div class="confidence-scale">

            Confidence scale:
            1 = Very Low

            &nbsp;&nbsp; • &nbsp;&nbsp;

            3 = Moderate

            &nbsp;&nbsp; • &nbsp;&nbsp;

            5 = Very High

        </div>
        """)

        confidence_columns = st.columns(
            3,
            gap="medium"
        )

        for index, skill in enumerate(
            confidence_areas
        ):

            widget_key = (
                f"confidence_"
                f"{current_area}_"
                f"{skill}"
            )

            if widget_key not in st.session_state:

                st.session_state[
                    widget_key
                ] = 3

            with confidence_columns[
                index
            ]:

                st.slider(
                    skill,

                    min_value=1,

                    max_value=5,

                    key=widget_key
                )

                confidence_scores[
                    skill
                ] = st.session_state[
                    widget_key
                ]


# ============================================================
# FINAL ROW
# ============================================================

goal_col, interests_col = st.columns(
    [0.82, 1.18],
    gap="medium"
)


# ============================================================
# 4. ACADEMIC GOAL
# ============================================================

with goal_col:

    with st.container(
        border=True
    ):

        st.html("""
        <div class="section-heading">

            <div class="section-badge badge-orange">
                4
            </div>

            <div>

                <div class="section-title">
                    Academic Goal
                </div>

                <div class="section-help">
                    What would you most like to achieve?
                </div>

            </div>

        </div>
        """)

        st.selectbox(
            "Select your academic goal",

            options=ACADEMIC_GOALS,

            key="academic_goal_input"
        )


# ============================================================
# 5. INTERESTS
# ============================================================

with interests_col:

    with st.container(
        border=True
    ):

        st.html("""
        <div class="section-heading">

            <div class="section-badge badge-pink">
                5
            </div>

            <div>

                <div class="section-title">
                    Topics You Are Most Interested In
                </div>

                <div class="section-help">

                    Choose any topics you are interested in to help
                    personalise your recommendations.

                </div>

            </div>

        </div>
        """)

        current_area = st.session_state[
            "academic_area_input"
        ]

        if current_area == ACADEMIC_AREA_PLACEHOLDER:

            st.html("""
            <div class="empty-state empty-state-pink">

                <div class="empty-icon empty-icon-pink">
                    ♥
                </div>

                <div>

                    <div class="empty-title">
                        No academic area selected yet
                    </div>

                    <div class="empty-text">

                        Select your field of study above to choose
                        topics that interest you.

                    </div>

                </div>

            </div>
            """)

        else:

            interest_options = (
                academic_profiles[
                    current_area
                ]["interests"]
            )

            existing_interests = (
                st.session_state.get(
                    "interests_input",
                    []
                )
            )

            valid_existing_interests = [
                topic
                for topic
                in existing_interests
                if topic
                in interest_options
            ]

            if (
                valid_existing_interests
                != existing_interests
            ):

                st.session_state[
                    "interests_input"
                ] = (
                    valid_existing_interests
                )

            st.multiselect(
                "Select topics",

                options=interest_options,

                placeholder=
                    "Optional — choose topics that interest you",

                key="interests_input"
            )


# ============================================================
# ACTIONS
# ============================================================

footer_left, clear_col, generate_col = st.columns(
    [5.6, 1.15, 1.8],
    gap="small"
)


with footer_left:

    st.html("""
    <div class="action-footer">
        © 2026 All rights reserved.
    </div>
    """)


with clear_col:

    st.button(
        "Clear Form",

        type="secondary",

        use_container_width=True,

        key="clear_form_button",

        on_click=
            clear_academic_form
    )


with generate_col:

    generate_prediction = st.button(
        "Generate Prediction →",

        type="primary",

        use_container_width=True,

        key=
            "generate_prediction_button"
    )


# ============================================================
# GENERATE PREDICTION
# ============================================================

if generate_prediction:

    # --------------------------------------------------------
    # READ CURRENT VALUES
    # --------------------------------------------------------

    current_area = st.session_state.get(
        "academic_area_input",
        ACADEMIC_AREA_PLACEHOLDER
    )

    current_interests = st.session_state.get(
        "interests_input",
        []
    )

    study_hours = st.session_state.get(
        "study_hours_input"
    )

    attendance = st.session_state.get(
        "attendance_input"
    )

    past_exam_score = st.session_state.get(
        "past_exam_input"
    )

    academic_goal = st.session_state.get(
        "academic_goal_input",
        DEFAULT_ACADEMIC_GOAL
    )


    # --------------------------------------------------------
    # VALIDATION
    # --------------------------------------------------------

    errors = {}


    # Academic area

    if (
        current_area
        == ACADEMIC_AREA_PLACEHOLDER
    ):

        errors[
            "academic_area"
        ] = (
            "Please select an academic area."
        )


    # Study hours

    try:

        study_hours_number = int(
            study_hours
        )

        if not (
            10
            <= study_hours_number
            <= 39
        ):

            errors[
                "study_hours"
            ] = (
                "Enter between 10 and 39 study hours."
            )

    except (
        TypeError,
        ValueError
    ):

        errors[
            "study_hours"
        ] = (
            "Enter a valid number of study hours."
        )


    # Attendance

    try:

        attendance_number = float(
            attendance
        )

        if not (
            50.0
            <= attendance_number
            <= 100.0
        ):

            errors[
                "attendance"
            ] = (
                "Enter an attendance rate between 50% and 100%."
            )

    except (
        TypeError,
        ValueError
    ):

        errors[
            "attendance"
        ] = (
            "Enter a valid attendance rate."
        )


    # Exam score

    try:

        exam_number = int(
            past_exam_score
        )

        if not (
            50
            <= exam_number
            <= 100
        ):

            errors[
                "past_exam_score"
            ] = (
                "Enter a past exam score between 50 and 100."
            )

    except (
        TypeError,
        ValueError
    ):

        errors[
            "past_exam_score"
        ] = (
            "Enter a valid past exam score."
        )


    # --------------------------------------------------------
    # STOP IF FORM HAS ERRORS
    # --------------------------------------------------------

    if errors:

        st.session_state[
            "form_errors"
        ] = errors

        st.rerun()


    # ========================================================
    # VALID FORM
    # ========================================================

    st.session_state[
        "form_errors"
    ] = {}


    study_hours = (
        study_hours_number
    )

    attendance = (
        attendance_number
    )

    past_exam_score = (
        exam_number
    )


    # ========================================================
    # PREDICTION INPUT
    # ========================================================

    prediction_input = pd.DataFrame({

        "Study_Hours_per_Week": [
            study_hours
        ],

        "Attendance_Rate": [
            attendance
        ],

        "Past_Exam_Scores": [
            past_exam_score
        ]
    })


    # ========================================================
    # APPLY SAVED PREPROCESSING
    # ========================================================

    scaled_input = scaler.transform(
        prediction_input
    )


    # ========================================================
    # GENERATE PREDICTION
    # ========================================================

    prediction = model.predict(
        scaled_input
    )[0]

    probabilities = (
        model.predict_proba(
            scaled_input
        )[0]
    )


    # Map each probability to its corresponding class.
    # This avoids relying on the probability array order.

    class_probabilities = dict(
        zip(
            model.classes_,
            probabilities
        )
    )


    pass_probability = (
        float(
            class_probabilities[
                1
            ]
        )
        * 100
    )

    fail_probability = (
        float(
            class_probabilities[
                0
            ]
        )
        * 100
    )


    predicted_label = (
        "Pass"
        if prediction == 1
        else "Fail"
    )


    # ========================================================
    # CONFIDENCE PROFILE
    # ========================================================

    confidence_scores = {}

    for skill in academic_profiles[
        current_area
    ]["confidence"]:

        confidence_key = (
            f"confidence_"
            f"{current_area}_"
            f"{skill}"
        )

        confidence_scores[
            skill
        ] = st.session_state.get(
            confidence_key,
            3
        )


    # ========================================================
    # REMOVE OLD RECOMMENDATIONS
    # ========================================================

    downstream_keys = [
        "priority_skill",
        "priority_skills",
        "preferred_difficulties",
        "recommendations",
        "top_recommendations",
        "learning_path",
        "pathway_resources"
    ]

    for key in downstream_keys:

        st.session_state.pop(
            key,
            None
        )


    # ========================================================
    # SAVE PROFILE
    # ========================================================

    st.session_state[
        "academic_area"
    ] = current_area

    st.session_state[
        "study_hours"
    ] = study_hours

    st.session_state[
        "attendance"
    ] = attendance

    st.session_state[
        "past_exam_score"
    ] = past_exam_score

    st.session_state[
        "confidence_scores"
    ] = confidence_scores

    st.session_state[
        "interests"
    ] = current_interests

    st.session_state[
        "academic_goal"
    ] = academic_goal


    # ========================================================
    # SAVE PREDICTION
    # ========================================================

    st.session_state[
        "prediction"
    ] = predicted_label

    st.session_state[
        "pass_probability"
    ] = pass_probability

    st.session_state[
        "fail_probability"
    ] = fail_probability


    # ========================================================
    # RESULTS PAGE
    # ========================================================

    st.switch_page(
        "pages/2_Prediction_Results.py"
    )