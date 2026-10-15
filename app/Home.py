import streamlit as st


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Personalized Learning Path",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# RESET
# ============================================================

def reset_application():
    st.session_state.clear()


# ============================================================
# GLOBAL CSS
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
    color: #14213d;
    overflow-x: hidden;
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
   STREAMLIT DEFAULT CHROME
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
    max-width: 1450px;
    margin: 0 auto;

    padding:
        0.75rem
        1.25rem
        0.5rem
        1.25rem !important;
}

main div[data-testid="stVerticalBlock"] {
    gap: 0 !important;
}


/* ==========================================================
   SIDEBAR SHELL
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

    border-right: none;
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
[data-testid="stSidebarContent"] {
    height: 100% !important;
    overflow: hidden !important;
}

section[data-testid="stSidebar"]
div[data-testid="stVerticalBlock"] {
    height: 100% !important;

    display: flex !important;
    flex-direction: column !important;

    gap: 0.18rem !important;

    overflow: hidden !important;
}


/* ==========================================================
   ACADEMIC ICON ABOVE NAV
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
    width: 52px;
    height: 52px;

    display: flex;
    align-items: center;
    justify-content: center;

    border-radius: 50%;

    background:
        linear-gradient(
            145deg,
            rgba(42, 114, 226, 0.42),
            rgba(14, 72, 164, 0.18)
        );

    border:
        1px solid
        rgba(
            110,
            166,
            250,
            0.45
        );

    box-shadow:
        0 0 0 5px
        rgba(
            33,
            103,
            214,
            0.06
        ),
        0 8px 22px
        rgba(
            0,
            55,
            150,
            0.22
        );

    color: #ffffff;

    font-size: 1.55rem;

    line-height: 1;

    user-select: none;
}


/* ==========================================================
   NAVIGATION
========================================================== */

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

    border: 1px solid transparent;

    border-radius: 7px;

    background: transparent !important;

    color: #dce7f7 !important;

    text-decoration: none !important;

    font-size: 0.76rem;
    font-weight: 560;

    box-shadow: none !important;

    transition:
        background 0.16s ease,
        border-color 0.16s ease,
        color 0.16s ease,
        transform 0.16s ease;
}

section[data-testid="stSidebar"]
[data-testid="stPageLink"] a p {
    margin: 0 !important;

    color: #dce7f7 !important;

    font-size: 0.76rem !important;
    font-weight: 560 !important;
}


/* ==========================================================
   SUBTLE LEFT ACCENT
========================================================== */

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

    transition:
        background 0.16s ease;
}


/* ==========================================================
   NAVIGATION HOVER
========================================================== */

section[data-testid="stSidebar"]
[data-testid="stPageLink"] a:hover {
    background:
        rgba(
            255,
            255,
            255,
            0.055
        ) !important;

    border-color:
        rgba(
            255,
            255,
            255,
            0.055
        );

    color: #ffffff !important;

    transform: translateX(2px);
}

section[data-testid="stSidebar"]
[data-testid="stPageLink"] a:hover p {
    color: #ffffff !important;
}

section[data-testid="stSidebar"]
[data-testid="stPageLink"] a:hover::before {
    background: #4a93ff;
}


/* ==========================================================
   ACTIVE PAGE
========================================================== */

section[data-testid="stSidebar"]
[data-testid="stPageLink"] a[aria-current="page"] {
    background:
        linear-gradient(
            90deg,
            rgba(30, 103, 213, 0.26) 0%,
            rgba(31, 102, 204, 0.12) 100%
        ) !important;

    border:
        1px solid
        rgba(
            103,
            160,
            244,
            0.20
        );

    color: #ffffff !important;

    box-shadow:
        inset 0 0 18px
        rgba(
            32,
            108,
            222,
            0.05
        ) !important;
}

section[data-testid="stSidebar"]
[data-testid="stPageLink"] a[aria-current="page"] p {
    color: #ffffff !important;
    font-weight: 680 !important;
}

section[data-testid="stSidebar"]
[data-testid="stPageLink"] a[aria-current="page"]::before {
    background: #4392ff;

    width: 3px;

    box-shadow:
        0 0 8px
        rgba(
            67,
            146,
            255,
            0.55
        );
}


/* ==========================================================
   PUSH BOTTOM CONTROLS DOWN
========================================================== */

.sidebar-bottom-anchor {
    height: 1px;
}

section[data-testid="stSidebar"]
div[data-testid="stElementContainer"]:has(.sidebar-bottom-anchor) {
    flex:
        1
        1
        auto !important;

    min-height: 1rem !important;
}


/* ==========================================================
   DIVIDER
========================================================== */

.sidebar-divider {
    width: 100%;
    height: 1px;

    margin:
        0
        0
        0.55rem
        0;

    background:
        linear-gradient(
            90deg,
            rgba(255,255,255,0.02),
            rgba(255,255,255,0.16),
            rgba(255,255,255,0.02)
        );
}


/* ==========================================================
   START OVER
========================================================== */

section[data-testid="stSidebar"]
div.stButton {
    margin: 0 !important;
}

section[data-testid="stSidebar"]
div.stButton > button {
    width: 100%;
    min-height: 2.55rem;

    padding:
        0.52rem
        0.7rem !important;

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

    border-radius: 8px;

    color: #ffffff !important;

    font-size: 0.7rem;
    font-weight: 600;

    box-shadow: none !important;
}

section[data-testid="stSidebar"]
div.stButton > button p {
    margin: 0 !important;

    color: #ffffff !important;

    font-size: 0.7rem !important;
}

section[data-testid="stSidebar"]
div.stButton > button:hover {
    background:
        rgba(
            255,
            255,
            255,
            0.065
        ) !important;

    border-color:
        rgba(
            176,
            202,
            243,
            0.48
        ) !important;
}


/* ==========================================================
   PRIVACY CARD
========================================================== */

.privacy-card {
    margin-top: 0.65rem;

    padding:
        0.75rem
        0.75rem;

    border:
        1px solid
        rgba(
            147,
            176,
            220,
            0.19
        );

    border-radius: 8px;

    background:
        linear-gradient(
            145deg,
            rgba(255,255,255,0.040),
            rgba(255,255,255,0.015)
        );
}

.privacy-title {
    margin-bottom: 0.32rem;

    color: #ffffff;

    font-size: 0.65rem;
    font-weight: 700;
}

.privacy-text {
    color: #c3d0e3;

    font-size: 0.55rem;

    line-height: 1.45;
}


/* ==========================================================
   HERO
========================================================== */

.hero {
    width: 100%;

    min-height: 335px;

    display: grid;

    grid-template-columns:
        minmax(0, 1.2fr)
        minmax(330px, 0.8fr);

    gap: 1.6rem;

    align-items: center;

    padding:
        1.65rem
        1.8rem;

    margin-bottom: 0.85rem;

    border:
        1px solid
        #dce5f1;

    border-radius: 12px;

    background:
        linear-gradient(
            110deg,
            #ffffff 0%,
            #ffffff 65%,
            #f2f6ff 100%
        );

    box-shadow:
        0 3px 12px
        rgba(
            20,
            50,
            100,
            0.045
        );
}

.hero-copy {
    min-width: 0;
}

.hero-title {
    max-width: 780px;

    margin:
        0
        0
        0.8rem
        0;

    color: #11213f;

    font-size:
        clamp(
            2.15rem,
            2.7vw,
            2.85rem
        );

    line-height: 1.04;

    letter-spacing: -0.035em;

    font-weight: 820;
}

.hero-subtitle {
    max-width: 740px;

    margin:
        0
        0
        1rem
        0;

    color: #65738b;

    font-size:
        clamp(
            0.94rem,
            1.02vw,
            1.05rem
        );

    line-height: 1.55;
}


/* ==========================================================
   HERO BUTTONS
========================================================== */

.hero-actions {
    display: flex;
    gap: 0.7rem;
    flex-wrap: wrap;
}

.hero-button-primary,
.hero-button-secondary {
    min-height: 2.65rem;

    display: inline-flex;

    align-items: center;
    justify-content: center;

    padding:
        0.62rem
        1.1rem;

    border-radius: 6px;

    font-size: 0.79rem;
    font-weight: 650;

    text-decoration: none !important;
}

.hero-button-primary {
    background: #0d63df;

    color: #ffffff !important;

    border:
        1px solid
        #0d63df;
}

.hero-button-primary:hover {
    background: #0a55c5;
}

.hero-button-secondary {
    background: #ffffff;

    color: #0d63df !important;

    border:
        1px solid
        #a9c5f7;
}

.hero-button-secondary:hover {
    background: #f3f7ff;
}


/* ==========================================================
   HERO VISUAL
========================================================== */

.hero-visual {
    width: 100%;
    min-height: 245px;

    position: relative;

    display: flex;

    align-items: center;
    justify-content: center;
}

.hero-laptop {
    width:
        min(
            100%,
            285px
        );

    padding: 0.72rem;

    background: #ffffff;

    border:
        5px solid
        #10244a;

    border-radius: 11px;

    box-shadow:
        0 12px 28px
        rgba(
            20,
            55,
            110,
            0.14
        );

    z-index: 3;
}

.hero-laptop-screen {
    min-height: 145px;

    padding: 0.85rem;

    border-radius: 6px;

    background:
        linear-gradient(
            145deg,
            #f8fbff,
            #edf4ff
        );
}

.hero-dashboard {
    display: flex;

    align-items: center;
    justify-content: space-between;

    gap: 0.7rem;
}

.score-circle {
    width: 65px;
    height: 65px;

    min-width: 65px;

    display: flex;

    align-items: center;
    justify-content: center;

    border-radius: 50%;

    border:
        7px solid
        #44c59a;

    background: white;

    color: #17486f;

    font-size: 0.9rem;
    font-weight: 800;
}

.mini-chart {
    height: 65px;

    display: flex;
    align-items: flex-end;

    gap: 5px;
}

.chart-bar {
    width: 11px;

    background: #1464e8;

    border-radius:
        3px
        3px
        0
        0;
}

.chart-bar-1 {
    height: 25px;
}

.chart-bar-2 {
    height: 38px;
}

.chart-bar-3 {
    height: 52px;
}

.chart-bar-4 {
    height: 44px;
}

.chart-bar-5 {
    height: 60px;
}

.dashboard-line {
    height: 4px;

    margin-top: 0.65rem;

    border-radius: 50px;

    background: #dbe5f3;
}

.dashboard-line-blue {
    width: 84%;

    background: #6d9eff;
}

.dashboard-line-short {
    width: 58%;
}


/* ==========================================================
   FLOATING CARDS
========================================================== */

.floating-card {
    position: absolute;

    z-index: 4;

    min-width: 120px;

    padding:
        0.6rem
        0.7rem;

    background: white;

    border:
        1px solid
        #dfe6f1;

    border-radius: 7px;

    box-shadow:
        0 7px 20px
        rgba(
            22,
            55,
            105,
            0.09
        );

    color: #65738a;

    font-size: 0.59rem;
}

.floating-title {
    display: block;

    margin-bottom: 0.28rem;

    color: #17294b;

    font-size: 0.61rem;
    font-weight: 700;
}

.float-performance {
    top: 0;
    left: 0;
}

.float-path {
    top: 2%;
    right: 0;
}

.float-focus {
    right: 0;
    bottom: 0;
}

.fake-line {
    height: 4px;

    margin-top: 4px;

    border-radius: 20px;

    background: #dfe7f3;
}

.fake-blue {
    width: 60px;

    background: #5388ff;
}

.fake-purple {
    width: 52px;

    background: #946ff0;
}


/* ==========================================================
   CONTENT CARDS
========================================================== */

.content-card {
    width: 100%;

    margin-bottom: 0.85rem;

    padding:
        1.15rem
        1.3rem;

    background: white;

    border:
        1px solid
        #dce5f1;

    border-radius: 11px;

    box-shadow:
        0 2px 9px
        rgba(
            20,
            50,
            100,
            0.025
        );
}

.content-card:has(.steps-grid) {
    min-height: 255px;
}

.content-card:has(.benefit-grid) {
    min-height: 190px;
}

.section-title {
    margin-bottom: 0.15rem;

    color: #142541;

    font-size: 1.2rem;
    font-weight: 800;
}

.section-subtitle {
    margin-bottom: 1rem;

    color: #78849a;

    font-size: 0.8rem;

    line-height: 1.45;
}


/* ==========================================================
   HOW IT WORKS
========================================================== */

.steps-grid {
    min-height: 170px;

    display: grid;

    grid-template-columns:
        repeat(
            4,
            minmax(0, 1fr)
        );

    align-items: center;

    gap: 0.8rem;
}

.step {
    min-width: 0;

    position: relative;

    padding:
        0.25rem
        0.9rem;
}

.step:not(:last-child)::after {
    content: "→";

    position: absolute;

    top: 35px;
    right: -4px;

    color: #84aaff;

    font-size: 1.15rem;
}

.step-top {
    display: flex;

    align-items: center;

    gap: 0.55rem;

    margin-bottom: 0.6rem;
}

.step-number {
    width: 25px;
    height: 25px;

    flex:
        0
        0
        25px;

    display: flex;

    align-items: center;
    justify-content: center;

    border-radius: 50%;

    background: #1464e8;

    color: white;

    font-size: 0.61rem;
    font-weight: 700;
}

.step-number-green {
    background: #35b96d;
}

.step-number-purple {
    background: #815ee6;
}

.step-number-orange {
    background: #f1a32a;
}

.step-icon {
    width: 44px;
    height: 44px;

    flex:
        0
        0
        44px;

    display: flex;

    align-items: center;
    justify-content: center;

    border-radius: 50%;

    background: #edf4ff;

    font-size: 1rem;
}

.step-icon-green {
    background: #ecf9f1;
}

.step-icon-purple {
    background: #f2efff;
}

.step-icon-orange {
    background: #fff5e5;
}

.step-title {
    margin-bottom: 0.28rem;

    color: #172a4b;

    font-size: 0.79rem;
    font-weight: 750;
}

.step-text {
    max-width: 235px;

    color: #748196;

    font-size: 0.66rem;

    line-height: 1.45;
}


/* ==========================================================
   BENEFITS
========================================================== */

.benefit-grid {
    min-height: 115px;

    display: grid;

    grid-template-columns:
        repeat(
            3,
            minmax(0, 1fr)
        );

    align-items: center;

    gap: 0.8rem;
}

.benefit-card {
    min-height: 90px;

    display: flex;

    align-items: center;

    gap: 0.75rem;

    padding:
        0.8rem
        0.85rem;

    background: #fbfcff;

    border:
        1px solid
        #e3e9f2;

    border-radius: 8px;
}

.benefit-icon {
    width: 46px;
    height: 46px;

    flex:
        0
        0
        46px;

    display: flex;

    align-items: center;
    justify-content: center;

    border-radius: 8px;

    background: #edf4ff;

    font-size: 1.05rem;
}

.benefit-icon-green {
    background: #ecf9f1;
}

.benefit-icon-purple {
    background: #f2efff;
}

.benefit-title {
    margin-bottom: 0.22rem;

    color: #192b4c;

    font-size: 0.74rem;
    font-weight: 750;
}

.benefit-text {
    color: #768298;

    font-size: 0.62rem;

    line-height: 1.45;
}


/* ==========================================================
   FOOTER
========================================================== */

.custom-footer {
    padding:
        0.05rem
        0
        0.2rem
        0;

    color: #909bad;

    font-size: 0.59rem;
}


/* ==========================================================
   SHORTER DESKTOP
========================================================== */

@media (max-height: 850px) and (min-width: 1100px) {

    section[data-testid="stSidebar"] > div {
        padding-top:
            0.55rem !important;
    }

    .sidebar-academic-mark {
        margin-bottom:
            0.45rem;
    }

    .academic-icon-badge {
        width: 46px;
        height: 46px;

        font-size: 1.35rem;
    }

    .block-container {
        padding-top:
            0.55rem !important;
    }

    .hero {
        min-height: 275px;

        padding:
            1rem
            1.25rem;

        margin-bottom: 0.6rem;
    }

    .hero-title {
        font-size:
            clamp(
                1.85rem,
                2.25vw,
                2.35rem
            );
    }

    .hero-subtitle {
        margin-bottom: 0.7rem;

        font-size: 0.85rem;
    }

    .hero-visual {
        min-height: 205px;
    }

    .hero-laptop {
        width: 240px;
    }

    .content-card {
        margin-bottom: 0.6rem;

        padding:
            0.8rem
            1rem;
    }

    .content-card:has(.steps-grid) {
        min-height: 205px;
    }

    .content-card:has(.benefit-grid) {
        min-height: 145px;
    }

    .steps-grid {
        min-height: 130px;
    }

    .benefit-grid {
        min-height: 80px;
    }

    .section-title {
        font-size: 1.02rem;
    }

    .section-subtitle {
        margin-bottom: 0.55rem;

        font-size: 0.7rem;
    }

    .step-icon {
        width: 36px;
        height: 36px;

        flex-basis: 36px;
    }

    .step-number {
        width: 21px;
        height: 21px;

        flex-basis: 21px;
    }

    .step-title {
        font-size: 0.69rem;
    }

    .step-text {
        font-size: 0.58rem;
    }

    .benefit-card {
        min-height: 64px;

        padding: 0.55rem;
    }

    .benefit-icon {
        width: 36px;
        height: 36px;

        flex-basis: 36px;
    }

    .benefit-title {
        font-size: 0.65rem;
    }

    .benefit-text {
        font-size: 0.54rem;
    }
}


/* ==========================================================
   TABLET
========================================================== */

@media (max-width: 1100px) {

    .hero {
        grid-template-columns: 1fr;

        min-height: auto;
    }

    .hero-visual {
        min-height: 240px;
    }

    .steps-grid {
        grid-template-columns:
            repeat(
                2,
                minmax(0, 1fr)
            );

        gap: 1.2rem;
    }

    .step:not(:last-child)::after {
        display: none;
    }

    .benefit-grid {
        grid-template-columns: 1fr;
    }

    .content-card:has(.steps-grid),
    .content-card:has(.benefit-grid) {
        min-height: auto;
    }
}


/* ==========================================================
   MOBILE
========================================================== */

@media (max-width: 768px) {

    section[data-testid="stSidebar"] {
        width: 215px !important;

        min-width: 215px !important;

        max-width: 215px !important;
    }

    section[data-testid="stSidebar"] > div {
        padding-top:
            0.55rem !important;
    }

    .academic-icon-badge {
        width: 42px;
        height: 42px;

        font-size: 1.2rem;
    }

    .block-container {
        padding:
            0.7rem
            0.8rem !important;
    }

    .hero {
        padding: 1rem;
    }

    .hero-title {
        font-size:
            clamp(
                1.55rem,
                6vw,
                2rem
            );
    }

    .hero-subtitle {
        font-size: 0.82rem;
    }

    .hero-visual {
        display: flex;

        flex-direction: column;

        gap: 0.5rem;

        min-height: auto;
    }

    .floating-card {
        position: static;

        width: 100%;

        max-width: 290px;
    }

    .steps-grid {
        grid-template-columns: 1fr;
    }

    .benefit-grid {
        grid-template-columns: 1fr;
    }
}

</style>
""")


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    # --------------------------------------------------------
    # ACADEMIC LOGO / ICON
    # --------------------------------------------------------

    st.html("""
    <div class="sidebar-academic-mark">

        <div class="academic-icon-badge">
            🎓
        </div>

    </div>
    """)


    # --------------------------------------------------------
    # NAVIGATION
    # --------------------------------------------------------

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


    # Flexible space

    st.html("""
    <div class="sidebar-bottom-anchor"></div>
    """)


    # Divider

    st.html("""
    <div class="sidebar-divider"></div>
    """)


    # Start over

    if st.button(
        "Clear Session",
        use_container_width=True
    ):
        reset_application()
        st.rerun()


    # Privacy

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
# HERO
# ============================================================

st.html("""
<div class="hero">

    <div class="hero-copy">

        <h1 class="hero-title">

            Personalised Academic
            Support System

        </h1>


        <p class="hero-subtitle">

            This system uses your academic information to
            estimate your performance and recommend personalised
            learning resources and learning paths based on your
            confidence, interests, goals and predicted performance.

        </p>


        <div class="hero-actions">

            <a
                class="hero-button-primary"
                href="/Academic_Information"
                target="_self">

                Start Your Assessment

            </a>


            <a
                class="hero-button-secondary"
                href="/About"
                target="_self">

                Learn More

            </a>

        </div>

    </div>


    <div class="hero-visual">


        <div class="floating-card float-performance">

            <span class="floating-title">
                Predicted Performance
            </span>

            <div class="fake-line fake-blue"></div>

            <div
                class="fake-line"
                style="width:42px;">
            </div>

        </div>


        <div class="floating-card float-path">

            <span class="floating-title">
                Recommended Path
            </span>

            <div class="fake-line fake-purple"></div>

            <div
                class="fake-line"
                style="width:38px;">
            </div>

        </div>


        <div class="hero-laptop">

            <div class="hero-laptop-screen">

                <div class="hero-dashboard">

                    <div class="score-circle">
                        78%
                    </div>


                    <div class="mini-chart">

                        <div class="chart-bar chart-bar-1"></div>
                        <div class="chart-bar chart-bar-2"></div>
                        <div class="chart-bar chart-bar-3"></div>
                        <div class="chart-bar chart-bar-4"></div>
                        <div class="chart-bar chart-bar-5"></div>

                    </div>

                </div>


                <div class="dashboard-line dashboard-line-blue"></div>

                <div class="dashboard-line dashboard-line-short"></div>

            </div>

        </div>


        <div class="floating-card float-focus">

            <span class="floating-title">
                Focus Areas
            </span>

            🔵 Programming<br>
            🟢 Data Analysis<br>
            🟠 Learning Path

        </div>


    </div>

</div>
""")


# ============================================================
# HOW IT WORKS
# ============================================================

st.html("""
<div class="content-card">

    <div class="section-title">
        How It Works
    </div>


    <div class="section-subtitle">

        Complete four simple steps to receive your
        personalised results.

    </div>


    <div class="steps-grid">


        <div class="step">

            <div class="step-top">

                <div class="step-number">
                    1
                </div>

                <div class="step-icon">
                    ♙
                </div>

            </div>


            <div class="step-title">
                Enter Your Profile
            </div>


            <div class="step-text">

                Provide your academic information,
                confidence ratings, interests and goal.

            </div>

        </div>


        <div class="step">

            <div class="step-top">

                <div class="step-number step-number-green">
                    2
                </div>

                <div class="step-icon step-icon-green">
                    ▥
                </div>

            </div>


            <div class="step-title">
                Predict Performance
            </div>


            <div class="step-text">

                Your academic information is used to
                estimate your predicted academic outcome.

            </div>

        </div>


        <div class="step">

            <div class="step-top">

                <div class="step-number step-number-purple">
                    3
                </div>

                <div class="step-icon step-icon-purple">
                    ◇
                </div>

            </div>


            <div class="step-title">
                Get Recommendations
            </div>


            <div class="step-text">

                Receive learning resources and a suggested
                learning path personalised to your profile.

            </div>

        </div>


        <div class="step">

            <div class="step-top">

                <div class="step-number step-number-orange">
                    4
                </div>

                <div class="step-icon step-icon-orange">
                    ◔
                </div>

            </div>


            <div class="step-title">
                View Insights
            </div>


            <div class="step-text">

                Explore your prediction, confidence profile
                and personalised recommendations.

            </div>

        </div>


    </div>

</div>
""")


# ============================================================
# WHY THIS SYSTEM HELPS
# ============================================================

st.html("""
<div class="content-card">

    <div class="section-title">
        Why This System Helps You
    </div>


    <div class="benefit-grid">


        <div class="benefit-card">

            <div class="benefit-icon">
                ↗
            </div>

            <div>

                <div class="benefit-title">
                    Academic Performance Insights
                </div>

                <div class="benefit-text">

                    Receive an estimate of your predicted
                    academic performance based on your information.

                </div>

            </div>

        </div>


        <div class="benefit-card">

            <div class="benefit-icon benefit-icon-green">
                ◎
            </div>

            <div>

                <div class="benefit-title">
                    Personalised Guidance
                </div>

                <div class="benefit-text">

                    Receive learning recommendations
                    matched to your academic profile.

                </div>

            </div>

        </div>


        <div class="benefit-card">

            <div class="benefit-icon benefit-icon-purple">
                ◇
            </div>

            <div>

                <div class="benefit-title">
                    Support Your Learning
                </div>

                <div class="benefit-text">

                    Identify areas where you may need support
                    and follow a suggested learning path.

                </div>

            </div>

        </div>


    </div>

</div>
""")


# ============================================================
# FOOTER
# ============================================================

st.html("""
<div class="custom-footer">

    © 2026 All rights reserved.

</div>
""")