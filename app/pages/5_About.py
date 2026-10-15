import streamlit as st


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# RESET FUNCTION
# ============================================================

def reset_application():
    st.session_state.clear()


# ============================================================
# CSS
# ============================================================

st.html("""
<style>

/* ==========================================================
   GLOBAL
========================================================== */

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
    background: #f7f9fd;
    color: #112446;
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
   HIDE STREAMLIT DEFAULTS
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
   MAIN CONTAINER
========================================================== */

.block-container {
    width: 100%;
    max-width: 1480px;

    margin: 0 auto;

    padding:
        0.65rem
        1.1rem
        0.7rem
        1.1rem !important;
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
        0.75rem
        1rem
        0.85rem
        1rem !important;

    overflow: hidden !important;
}

section[data-testid="stSidebar"]
div[data-testid="stVerticalBlock"] {
    height: 100% !important;

    display: flex !important;
    flex-direction: column !important;

    gap: 0.16rem !important;
}


/* ==========================================================
   SIDEBAR ICON
========================================================== */

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
    width: 50px;
    height: 50px;

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

    font-size: 1.45rem;

    box-shadow:
        0 0 0 5px rgba(33,103,214,0.06),
        0 8px 22px rgba(0,55,150,0.22);
}


/* ==========================================================
   SIDEBAR NAVIGATION
========================================================== */

section[data-testid="stSidebar"]
[data-testid="stPageLink"] {
    margin: 0 !important;
}

section[data-testid="stSidebar"]
[data-testid="stPageLink"] a {
    position: relative;

    width: 100%;
    min-height: 2.45rem;

    display: flex;
    align-items: center;

    padding:
        0.46rem
        0.8rem;

    border:
        1px solid transparent;

    border-radius: 7px;

    background: transparent !important;

    color: #dce7f7 !important;

    text-decoration: none !important;

    transition: all 0.16s ease;
}

section[data-testid="stSidebar"]
[data-testid="stPageLink"] a p {
    margin: 0 !important;

    color: #dce7f7 !important;

    font-size: 0.74rem !important;

    font-weight: 560 !important;
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
        rgba(100,157,239,0.20);
}

section[data-testid="stSidebar"]
[data-testid="stPageLink"] a:hover {
    background:
        rgba(255,255,255,0.05) !important;
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
    color: #ffffff !important;

    font-weight: 680 !important;
}

section[data-testid="stSidebar"]
[data-testid="stPageLink"] a[aria-current="page"]::before {
    background: #4392ff;

    box-shadow:
        0 0 8px rgba(67,146,255,0.55);
}


/* ==========================================================
   SIDEBAR BOTTOM
========================================================== */

.sidebar-bottom-anchor {
    height: 1px;
}

section[data-testid="stSidebar"]
div[data-testid="stElementContainer"]:has(.sidebar-bottom-anchor) {
    flex: 1 1 auto !important;
}

.sidebar-divider {
    height: 1px;

    margin-bottom: 0.5rem;

    background:
        linear-gradient(
            90deg,
            transparent,
            rgba(255,255,255,0.16),
            transparent
        );
}


/* ==========================================================
   CLEAR SESSION
========================================================== */

section[data-testid="stSidebar"]
.st-key-sidebar_clear_session {
    width: 100% !important;

    margin: 0 !important;
    padding: 0 !important;
}

section[data-testid="stSidebar"]
.st-key-sidebar_clear_session button {
    width: 100% !important;

    height: 2.25rem !important;
    min-height: 2.25rem !important;

    background:
        rgba(255,255,255,0.025) !important;

    border:
        1px solid
        rgba(153,184,232,0.30) !important;

    border-radius: 7px !important;

    color: #ffffff !important;

    font-size: 0.64rem !important;
    font-weight: 600 !important;

    box-shadow: none !important;
}

section[data-testid="stSidebar"]
.st-key-sidebar_clear_session button * {
    color: #ffffff !important;

    -webkit-text-fill-color:
        #ffffff !important;

    font-size: 0.64rem !important;
    font-weight: 600 !important;
}


/* ==========================================================
   PRIVACY
========================================================== */

.privacy-card {
    margin-top: 0.65rem;

    padding: 0.72rem;

    border:
        1px solid
        rgba(147,176,220,0.19);

    border-radius: 8px;

    background:
        rgba(255,255,255,0.025);
}

.privacy-title {
    margin-bottom: 0.3rem;

    color: #ffffff;

    font-size: 0.64rem;

    font-weight: 700;
}

.privacy-text {
    color: #c3d0e3;

    font-size: 0.54rem;

    line-height: 1.45;
}


/* ==========================================================
   PAGE HEADER
========================================================== */

.about-header {
    margin-bottom: 0.55rem;
}

.about-title {
    margin: 0;

    color: #102347;

    font-size: 1.55rem;

    line-height: 1.05;

    font-weight: 820;
}

.about-subtitle {
    max-width: 850px;

    margin:
        0.28rem
        0
        0
        0;

    color: #68778e;

    font-size: 0.67rem;

    line-height: 1.5;
}


/* ==========================================================
   OVERVIEW CARD
========================================================== */

.overview-card {
    display: grid;

    grid-template-columns:
        1.35fr
        0.65fr;

    min-height: 145px;

    margin-bottom: 0.65rem;

    background:
        linear-gradient(
            135deg,
            #ffffff 0%,
            #fafcff 100%
        );

    border:
        1px solid
        #dce6f2;

    border-radius: 11px;

    overflow: hidden;

    box-shadow:
        0 2px 10px
        rgba(21,52,91,0.025);
}

.overview-content {
    padding:
        0.9rem
        1rem;
}

.overview-badge {
    display: inline-flex;

    padding:
        0.23rem
        0.45rem;

    background: #edf4ff;

    border:
        1px solid
        #dce8fa;

    border-radius: 999px;

    color: #286bca;

    font-size: 0.45rem;

    font-weight: 700;
}

.overview-heading {
    margin-top: 0.5rem;

    color: #193150;

    font-size: 0.84rem;

    line-height: 1.3;

    font-weight: 780;
}

.overview-text {
    max-width: 800px;

    margin-top: 0.35rem;

    color: #667891;

    font-size: 0.54rem;

    line-height: 1.55;
}

.overview-visual {
    display: flex;

    align-items: center;
    justify-content: center;

    position: relative;

    background:
        radial-gradient(
            circle at center,
            #edf4ff 0%,
            #f7faff 62%,
            transparent 100%
        );
}

.overview-icon {
    width: 78px;
    height: 78px;

    display: flex;

    align-items: center;
    justify-content: center;

    border-radius: 50%;

    background:
        linear-gradient(
            145deg,
            #eaf2ff,
            #f6f8ff
        );

    border:
        1px solid
        #dde8f8;

    font-size: 1.7rem;
}

.overview-mini {
    position: absolute;

    padding:
        0.27rem
        0.4rem;

    background: #ffffff;

    border:
        1px solid
        #dfe7f1;

    border-radius: 6px;

    color: #4a617e;

    font-size: 0.41rem;

    font-weight: 650;
}

.overview-mini.one {
    top: 18px;
    left: 18px;
}

.overview-mini.two {
    top: 18px;
    right: 18px;
}

.overview-mini.three {
    bottom: 18px;
    right: 24px;
}


/* ==========================================================
   SYSTEM FLOW
========================================================== */

.flow-card {
    padding:
        0.78rem
        0.85rem;

    margin-bottom: 0.65rem;

    background: #ffffff;

    border:
        1px solid
        #dce6f2;

    border-radius: 10px;

    box-shadow:
        0 2px 10px
        rgba(21,52,91,0.02);
}

.section-heading {
    margin: 0;

    color: #1e3555;

    font-size: 0.74rem;

    line-height: 1.25;

    font-weight: 780;
}

.section-description {
    margin-top: 0.12rem;

    color: #78869a;

    font-size: 0.49rem;

    line-height: 1.4;
}

.flow-row {
    display: flex;

    align-items: stretch;

    gap: 0.35rem;

    margin-top: 0.65rem;
}

.flow-item {
    flex: 1;

    min-width: 0;

    padding:
        0.62rem
        0.65rem;

    background:
        linear-gradient(
            180deg,
            #ffffff,
            #fbfdff
        );

    border:
        1px solid
        #e1e8f2;

    border-radius: 8px;
}

.flow-number {
    width: 24px;
    height: 24px;

    display: flex;

    align-items: center;
    justify-content: center;

    margin-bottom: 0.4rem;

    border-radius: 50%;

    color: #ffffff;

    font-size: 0.5rem;

    font-weight: 800;
}

.flow-number.blue {
    background: #1767e8;
}

.flow-number.green {
    background: #2eb873;
}

.flow-number.purple {
    background: #7758e8;
}

.flow-number.orange {
    background: #f0a020;
}

.flow-title {
    color: #29405e;

    font-size: 0.53rem;

    font-weight: 720;
}

.flow-text {
    margin-top: 0.12rem;

    color: #78869a;

    font-size: 0.44rem;

    line-height: 1.4;
}

.flow-arrow {
    min-width: 20px;

    display: flex;

    align-items: center;
    justify-content: center;

    color: #6c94dc;

    font-size: 0.8rem;
}


/* ==========================================================
   TWO MAIN CARDS
========================================================== */

.main-grid {
    display: grid;

    grid-template-columns:
        0.95fr
        1.05fr;

    gap: 0.65rem;

    margin-bottom: 0.65rem;
}

.info-card {
    padding:
        0.78rem
        0.85rem;

    background: #ffffff;

    border:
        1px solid
        #dce6f2;

    border-radius: 10px;

    box-shadow:
        0 2px 10px
        rgba(21,52,91,0.02);
}


/* ==========================================================
   PREDICTION CARD
========================================================== */

.info-title {
    color: #203856;

    font-size: 0.68rem;

    font-weight: 770;
}

.info-text {
    margin-top: 0.28rem;

    color: #687a93;

    font-size: 0.5rem;

    line-height: 1.5;
}

.input-pills {
    display: flex;

    flex-wrap: wrap;

    gap: 0.3rem;

    margin-top: 0.55rem;
}

.input-pill {
    padding:
        0.26rem
        0.42rem;

    background: #f2f6fd;

    border:
        1px solid
        #dfe7f2;

    border-radius: 5px;

    color: #4d6583;

    font-size: 0.43rem;

    font-weight: 650;
}

.small-note {
    margin-top: 0.55rem;

    padding:
        0.45rem
        0.5rem;

    background: #f4f8ff;

    border-radius: 6px;

    color: #5e7492;

    font-size: 0.45rem;

    line-height: 1.45;
}


/* ==========================================================
   RECOMMENDATION LOGIC
========================================================== */

.logic-list {
    margin-top: 0.45rem;
}

.logic-row {
    display: flex;

    align-items: center;

    gap: 0.48rem;

    padding:
        0.34rem
        0;

    border-bottom:
        1px solid
        #edf1f5;
}

.logic-row:last-child {
    border-bottom: none;
}

.logic-number {
    width: 23px;
    height: 23px;

    min-width: 23px;

    display: flex;

    align-items: center;
    justify-content: center;

    border-radius: 50%;

    background: #edf4ff;

    color: #1767e8;

    font-size: 0.44rem;

    font-weight: 800;
}

.logic-main {
    flex: 1;
}

.logic-title {
    color: #314762;

    font-size: 0.49rem;

    font-weight: 700;
}

.logic-text {
    margin-top: 0.05rem;

    color: #7b889a;

    font-size: 0.42rem;

    line-height: 1.35;
}

.logic-weight {
    padding:
        0.2rem
        0.34rem;

    border-radius: 999px;

    font-size: 0.4rem;

    font-weight: 700;

    white-space: nowrap;
}

.logic-weight.green {
    background: #eaf8f0;
    color: #27975d;
}

.logic-weight.blue {
    background: #edf4ff;
    color: #2870d5;
}

.logic-weight.purple {
    background: #f1edff;
    color: #7158d5;
}

.logic-weight.orange {
    background: #fff3e5;
    color: #d98718;
}


/* ==========================================================
   IMPORTANT INFORMATION
========================================================== */

.important-card {
    display: grid;

    grid-template-columns:
        1fr
        1fr
        1fr;

    gap: 0.5rem;

    padding:
        0.78rem
        0.85rem;

    margin-bottom: 0.65rem;

    background: #ffffff;

    border:
        1px solid
        #dce6f2;

    border-radius: 10px;
}

.important-item {
    display: flex;

    gap: 0.5rem;

    align-items: flex-start;

    padding:
        0.55rem;

    background: #fbfcff;

    border:
        1px solid
        #e3e9f2;

    border-radius: 7px;
}

.important-icon {
    width: 27px;
    height: 27px;

    min-width: 27px;

    display: flex;

    align-items: center;
    justify-content: center;

    border-radius: 7px;

    background: #eef4ff;

    color: #1767e8;

    font-size: 0.53rem;

    font-weight: 800;
}

.important-title {
    color: #2a415f;

    font-size: 0.5rem;

    font-weight: 730;
}

.important-text {
    margin-top: 0.08rem;

    color: #738298;

    font-size: 0.43rem;

    line-height: 1.4;
}


/* ==========================================================
   RESPONSIBLE USE
========================================================== */

.responsible-card {
    position: relative;

    display: flex;

    align-items: center;

    gap: 0.7rem;

    padding:
        0.7rem
        0.85rem;

    margin-bottom: 0.65rem;

    background: #ffffff;

    border:
        1px solid
        #dce6f3;

    border-radius: 10px;

    overflow: hidden;

    box-shadow:
        0 2px 10px
        rgba(23,55,95,0.035);
}

.responsible-card::before {
    content: "";

    position: absolute;

    top: 0;
    bottom: 0;
    left: 0;

    width: 4px;

    background:
        linear-gradient(
            180deg,
            #1767e8,
            #6b63e8
        );
}

.responsible-icon {
    width: 38px;
    height: 38px;

    min-width: 38px;

    display: flex;

    align-items: center;
    justify-content: center;

    margin-left: 0.12rem;

    border-radius: 9px;

    background:
        linear-gradient(
            145deg,
            #edf4ff,
            #f4f6ff
        );

    color: #1767e8;

    font-size: 0.75rem;

    font-weight: 800;
}

.responsible-main {
    flex: 1;
}

.responsible-title {
    color: #19304f;

    font-size: 0.61rem;

    font-weight: 760;
}

.responsible-text {
    margin-top: 0.1rem;

    color: #62748e;

    font-size: 0.49rem;

    line-height: 1.45;
}

.responsible-pill {
    padding:
        0.29rem
        0.48rem;

    background: #f3f7fd;

    border:
        1px solid
        #e0e8f3;

    border-radius: 6px;

    color: #49617e;

    font-size: 0.45rem;

    font-weight: 650;

    white-space: nowrap;
}


/* ==========================================================
   NAVIGATION BUTTONS
========================================================== */

main div.stButton > button {
    min-height: 2.35rem !important;
    height: 2.35rem !important;

    padding:
        0.4rem
        0.8rem !important;

    border-radius: 6px !important;

    font-size: 0.61rem !important;
    font-weight: 700 !important;

    white-space: nowrap !important;
}


/* HOME */

.st-key-go_home button {
    background: #ffffff !important;

    border:
        1px solid
        #8eb5ec !important;

    color: #1767e8 !important;

    box-shadow: none !important;

    white-space: nowrap !important;
}

.st-key-go_home button * {
    color: #1767e8 !important;

    -webkit-text-fill-color:
        #1767e8 !important;

    white-space: nowrap !important;

    font-size: 0.61rem !important;

    line-height: 1 !important;
}


/* ACADEMIC INFO */

.st-key-go_academic button {
    background:
        linear-gradient(
            135deg,
            #1767e8,
            #0759d6
        ) !important;

    border:
        1px solid
        #1767e8 !important;

    color: #ffffff !important;

    white-space: nowrap !important;

    box-shadow:
        0 4px 12px
        rgba(23,103,232,0.16) !important;
}

.st-key-go_academic button * {
    color: #ffffff !important;

    -webkit-text-fill-color:
        #ffffff !important;

    white-space: nowrap !important;

    font-size: 0.61rem !important;

    line-height: 1 !important;
}


/* ==========================================================
   FOOTER
========================================================== */

.page-footer {
    min-height: 1.2rem;

    display: flex;

    align-items: center;

    color: #8c98a9;

    font-size: 0.51rem;
}


/* ==========================================================
   RESPONSIVE
========================================================== */

@media (max-width: 1050px) {

    .overview-card {
        grid-template-columns: 1fr;
    }

    .overview-visual {
        min-height: 130px;
    }

    .flow-row {
        flex-wrap: wrap;
    }

    .flow-item {
        flex:
            1 1
            200px;
    }

    .flow-arrow {
        display: none;
    }

    .main-grid {
        grid-template-columns: 1fr;
    }

    .important-card {
        grid-template-columns: 1fr;
    }
}


@media (max-width: 768px) {

    .block-container {
        padding:
            0.65rem
            0.7rem !important;
    }

    .about-title {
        font-size: 1.25rem;
    }

    .overview-visual {
        display: none;
    }

    .responsible-card {
        align-items: flex-start;
    }

    .responsible-pill {
        display: none;
    }
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
<div class="about-header">

    <h1 class="about-title">
        About the System
    </h1>

    <p class="about-subtitle">

        Learn how the Student Academic Support System uses
        academic information to provide a performance prediction
        and personalised learning recommendations.

    </p>

</div>
""")


# ============================================================
# COMPACT OVERVIEW
# ============================================================

st.html("""
<div class="overview-card">


    <div class="overview-content">

        <div class="overview-badge">
            Proof-of-Concept Academic Support System
        </div>

        <div class="overview-heading">

            Understand your academic profile and receive
            learning support tailored to your needs.

        </div>

        <div class="overview-text">

            The application combines academic performance
            prediction with personalised learning recommendations.

            It uses selected academic information to estimate a
            predicted outcome, then considers your wider academic
            profile to identify relevant learning resources and
            organise them into a suggested learning path.

        </div>

    </div>


    <div class="overview-visual">

        <div class="overview-mini one">
            Prediction
        </div>

        <div class="overview-mini two">
            Recommendations
        </div>

        <div class="overview-mini three">
            Learning Path
        </div>

        <div class="overview-icon">
            🎓
        </div>

    </div>


</div>
""")


# ============================================================
# SYSTEM FLOW
# ============================================================

st.html("""
<div class="flow-card">

    <h2 class="section-heading">
        How the System Works
    </h2>

    <div class="section-description">

        The application follows four connected stages.

    </div>


    <div class="flow-row">


        <div class="flow-item">

            <div class="flow-number blue">
                1
            </div>

            <div class="flow-title">
                Academic Profile
            </div>

            <div class="flow-text">

                Enter your academic performance values,
                confidence ratings, interests and academic goal.

            </div>

        </div>


        <div class="flow-arrow">
            →
        </div>


        <div class="flow-item">

            <div class="flow-number green">
                2
            </div>

            <div class="flow-title">
                Performance Prediction
            </div>

            <div class="flow-text">

                Your academic performance information is used
                to estimate a predicted Pass/Fail outcome and
                Predicted Pass Probability.

            </div>

        </div>


        <div class="flow-arrow">
            →
        </div>


        <div class="flow-item">

            <div class="flow-number purple">
                3
            </div>

            <div class="flow-title">
                Personalised Recommendations
            </div>

            <div class="flow-text">

                Learning resources are ranked based on your
                academic profile, support needs and predicted
                performance.

            </div>

        </div>


        <div class="flow-arrow">
            →
        </div>


        <div class="flow-item">

            <div class="flow-number orange">
                4
            </div>

            <div class="flow-title">
                Academic Insights
            </div>

            <div class="flow-text">

                Your prediction, confidence profile and
                recommendations are combined into one summary.

            </div>

        </div>


    </div>

</div>
""")


# ============================================================
# PREDICTION + RECOMMENDATION EXPLANATION
# ============================================================

st.html("""
<div class="main-grid">


    <!-- ==================================================
         PREDICTION
    =================================================== -->

    <div class="info-card">

        <div class="info-title">
            How the Prediction Works
        </div>

        <div class="info-text">

            The prediction uses Study Hours per Week,
            Attendance Rate and Past Exam Score to estimate
            whether the current academic information is more
            closely associated with a Pass or Fail outcome.

        </div>


        <div class="input-pills">

            <div class="input-pill">
                Study Hours per Week
            </div>

            <div class="input-pill">
                Attendance Rate
            </div>

            <div class="input-pill">
                Past Exam Score
            </div>

        </div>


        <div class="small-note">

            <b>Important:</b>
            Predicted Pass Probability is an estimate based on
            the academic information you provide. It is not an
            actual grade and does not guarantee a future result.

        </div>

    </div>


    <!-- ==================================================
         RECOMMENDATIONS
    =================================================== -->

    <div class="info-card">

        <div class="info-title">
            How Recommendations Are Created
        </div>

        <div class="info-text">

            Suitable learning resources are ranked using
            several parts of your academic profile.

        </div>


        <div class="logic-list">


            <div class="logic-row">

                <div class="logic-number">
                    1
                </div>

                <div class="logic-main">

                    <div class="logic-title">
                        Support Need
                    </div>

                    <div class="logic-text">

                        Gives more importance to resources that
                        support your lowest-confidence skill areas.

                    </div>

                </div>

                <div class="logic-weight green">
                    35%
                </div>

            </div>


            <div class="logic-row">

                <div class="logic-number">
                    2
                </div>

                <div class="logic-main">

                    <div class="logic-title">
                        Interests
                    </div>

                    <div class="logic-text">

                        Gives more importance to resources related
                        to topics you are interested in.

                    </div>

                </div>

                <div class="logic-weight blue">
                    25%
                </div>

            </div>


            <div class="logic-row">

                <div class="logic-number">
                    3
                </div>

                <div class="logic-main">

                    <div class="logic-title">
                        Overall Profile Match
                    </div>

                    <div class="logic-text">

                        Considers how closely each resource matches
                        your wider academic profile and goal.

                    </div>

                </div>

                <div class="logic-weight purple">
                    25%
                </div>

            </div>


            <div class="logic-row">

                <div class="logic-number">
                    4
                </div>

                <div class="logic-main">

                    <div class="logic-title">
                        Difficulty Level
                    </div>

                    <div class="logic-text">

                        Gives more importance to resource difficulty
                        levels that suit your predicted performance.

                    </div>

                </div>

                <div class="logic-weight orange">
                    15%
                </div>

            </div>


        </div>

    </div>


</div>
""")


# ============================================================
# IMPORTANT INFORMATION
# ============================================================

st.html("""
<div class="important-card">


    <div class="important-item">

        <div class="important-icon">
            1
        </div>

        <div>

            <div class="important-title">
                Profile Match
            </div>

            <div class="important-text">

                Profile Match shows how closely a resource fits
                your current academic profile. It is used to rank
                resources and is not a probability that the
                resource will improve your academic performance.

            </div>

        </div>

    </div>


    <div class="important-item">

        <div class="important-icon">
            2
        </div>

        <div>

            <div class="important-title">
                Learning Path
            </div>

            <div class="important-text">

                Your learning path shows the stages considered
                appropriate for your predicted performance.
                Depending on your result, this may include
                Foundations, Core Skills and/or Advanced Topics.

            </div>

        </div>

    </div>


    <div class="important-item">

        <div class="important-icon">
            3
        </div>

        <div>

            <div class="important-title">
                Project Scope
            </div>

            <div class="important-text">

                This is a proof-of-concept application.
                Confidence ratings are self-reported and the
                learning-resource catalogue is intentionally
                limited.

            </div>

        </div>

    </div>


</div>
""")


# ============================================================
# RESPONSIBLE USE
# ============================================================

st.html("""
<div class="responsible-card">

    <div class="responsible-icon">
        i
    </div>


    <div class="responsible-main">

        <div class="responsible-title">
            Responsible Use
        </div>

        <div class="responsible-text">

            This system is designed to support academic
            planning and student reflection. Prediction results
            and recommendations should be treated as guidance
            rather than guaranteed outcomes, and the system
            should not replace advice from lecturers, tutors or
            academic advisors.

        </div>

    </div>


    <div class="responsible-pill">
        Academic Support Tool
    </div>

</div>
""")


# ============================================================
# NAVIGATION
# ============================================================

nav_space, home_col, academic_col = st.columns(
    [4.8, 1.35, 1.95],
    gap="small"
)


with home_col:

    if st.button(
        "← Home",
        use_container_width=True,
        key="go_home"
    ):

        st.switch_page(
            "Home.py"
        )


with academic_col:

    if st.button(
        "Go to Academic Information →",
        type="primary",
        use_container_width=True,
        key="go_academic"
    ):

        st.switch_page(
            "pages/1_Academic_Information.py"
        )


# ============================================================
# FOOTER
# ============================================================

st.html("""
<div class="page-footer">
    © 2026 All rights reserved.
</div>
""")