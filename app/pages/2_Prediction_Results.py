import streamlit as st


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Prediction Results",
    page_icon="📊",
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

.results-header {
    margin-bottom: 0.55rem;
}

.results-title {
    margin: 0;

    color: #102347;

    font-size: 1.55rem;

    line-height: 1.05;

    font-weight: 820;
}

.results-subtitle {
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
   EMPTY STATE
========================================================== */

.empty-card {
    width: 100%;

    min-height: 360px;

    display: flex;

    flex-direction: column;

    justify-content: center;

    align-items: center;

    text-align: center;

    padding:
        2.2rem
        2rem;

    background:
        linear-gradient(
            180deg,
            #ffffff 0%,
            #fbfdff 100%
        );

    border:
        1px solid
        #dbe6f3;

    border-radius: 12px;

    box-shadow:
        0 3px 14px
        rgba(
            25,
            56,
            95,
            0.035
        );
}


/* ==========================================================
   EMPTY ICON
========================================================== */

.empty-icon-wrap {
    width: 86px;
    height: 86px;

    display: flex;

    justify-content: center;

    align-items: center;

    margin-bottom: 0.9rem;

    border-radius: 50%;

    background:
        linear-gradient(
            145deg,
            #eff4ff,
            #f4f7ff
        );

    border:
        1px solid
        #e6edfb;

    box-shadow:
        0 8px 24px
        rgba(
            65,
            111,
            185,
            0.07
        );
}

.empty-chart {
    position: relative;

    width: 42px;
    height: 40px;
}

.empty-bar {
    position: absolute;

    bottom: 4px;

    width: 9px;

    border-radius:
        3px
        3px
        1px
        1px;

    background:
        linear-gradient(
            180deg,
            #3177ef,
            #0e5ddd
        );
}

.empty-bar-one {
    left: 2px;
    height: 17px;
}

.empty-bar-two {
    left: 16px;
    height: 27px;
}

.empty-bar-three {
    left: 30px;
    height: 35px;
}

.empty-line {
    position: absolute;

    top: 2px;
    left: 2px;

    width: 35px;
    height: 17px;

    border-top:
        2px dashed
        #755ce8;

    transform:
        rotate(-17deg);
}


/* ==========================================================
   EMPTY TEXT
========================================================== */

.empty-heading {
    margin: 0;

    color: #132646;

    font-size: 1.02rem;

    line-height: 1.2;

    font-weight: 800;
}

.empty-description {
    max-width: 500px;

    margin:
        0.55rem
        auto
        0
        auto;

    color: #667892;

    font-size: 0.63rem;

    line-height: 1.6;
}


/* ==========================================================
   EMPTY BUTTON
========================================================== */

.empty-button-space {
    height: 0.55rem;
}

.st-key-go_academic_info button {
    width: 100% !important;

    min-height:
        2.55rem !important;

    padding:
        0.5rem
        0.8rem !important;

    background:
        linear-gradient(
            135deg,
            #1767e8 0%,
            #075bd7 100%
        ) !important;

    border:
        1px solid
        #1767e8 !important;

    border-radius:
        7px !important;

    color:
        #ffffff !important;

    box-shadow:
        0 5px 14px
        rgba(
            23,
            103,
            232,
            0.17
        ) !important;
}

.st-key-go_academic_info button * {
    color:
        #ffffff !important;

    -webkit-text-fill-color:
        #ffffff !important;

    font-size:
        0.65rem !important;

    font-weight:
        700 !important;
}

.st-key-go_academic_info button:hover {
    background:
        linear-gradient(
            135deg,
            #0f60df,
            #064fc0
        ) !important;
}


/* ==========================================================
   HOW IT WORKS CARD
========================================================== */

.how-card {
    position: relative;

    width: 100%;

    display: flex;

    align-items: center;

    gap: 0.8rem;

    margin-top: 0.65rem;

    padding:
        0.8rem
        1rem;

    background:
        #ffffff;

    border:
        1px solid
        #dce6f3;

    border-radius:
        10px;

    box-shadow:
        0 2px 10px
        rgba(23,55,95,0.035);

    overflow: hidden;
}

.how-card::before {
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

.how-icon-wrap {
    width: 38px;
    height: 38px;

    flex:
        0 0
        38px;

    display: flex;

    align-items: center;

    justify-content: center;

    margin-left: 0.15rem;

    border-radius: 9px;

    background:
        linear-gradient(
            145deg,
            #edf4ff,
            #f4f6ff
        );

    color: #1767e8;

    font-size: 0.82rem;

    font-weight: 800;
}

.how-main {
    flex: 1;

    min-width: 0;
}

.how-title {
    margin-bottom: 0.12rem;

    color: #19304f;

    font-size: 0.66rem;

    line-height: 1.25;

    font-weight: 760;
}

.how-text {
    color: #62748e;

    font-size: 0.56rem;

    line-height: 1.45;
}

.how-inputs {
    min-width: 305px;

    display: flex;

    justify-content: flex-end;

    gap: 0.35rem;
}

.how-pill {
    padding:
        0.3rem
        0.48rem;

    background:
        #f3f7fd;

    border:
        1px solid
        #e0e8f3;

    border-radius: 6px;

    color: #49617e;

    font-size: 0.48rem;

    line-height: 1;

    font-weight: 650;

    white-space: nowrap;
}


/* ==========================================================
   RESULT CARDS
========================================================== */

.top-result-grid {
    display: grid;

    grid-template-columns:
        1.05fr
        1fr
        0.72fr;

    gap: 0.65rem;
}

.result-card {
    min-height: 190px;

    padding: 0.8rem;

    background: #ffffff;

    border:
        1px solid
        #dfe7f2;

    border-radius: 9px;

    box-shadow:
        0 2px 8px
        rgba(20,50,90,0.03);
}

.card-heading {
    margin-bottom: 0.65rem;

    color: #20324e;

    font-size: 0.68rem;

    font-weight: 780;
}


/* ==========================================================
   OVERALL PREDICTION
========================================================== */

.prediction-flex {
    display: flex;

    align-items: center;

    gap: 1rem;
}

.probability-ring {
    --percentage: 50;

    width: 102px;
    height: 102px;

    flex:
        0 0
        102px;

    position: relative;

    display: flex;

    align-items: center;

    justify-content: center;

    border-radius: 50%;

    background:
        conic-gradient(
            #42bd7d
            calc(
                var(--percentage)
                * 1%
            ),
            #e7edf4
            0
        );
}

.probability-ring::before {
    content: "";

    position: absolute;

    width: 75px;
    height: 75px;

    border-radius: 50%;

    background: #ffffff;
}

.probability-content {
    position: relative;

    z-index: 1;

    text-align: center;
}

.probability-number {
    color: #168e51;

    font-size: 1.2rem;

    font-weight: 820;
}

.probability-caption {
    margin-top: 0.12rem;

    max-width: 60px;

    color: #74839a;

    font-size: 0.46rem;

    line-height: 1.2;
}

.outcome-name {
    margin-bottom: 0.28rem;

    font-size: 0.73rem;

    font-weight: 770;
}

.outcome-description {
    color: #60728d;

    font-size: 0.54rem;

    line-height: 1.45;
}


/* ==========================================================
   RESULT SUPPORT MESSAGE
========================================================== */

.success-message {
    margin-top: 0.58rem;

    padding:
        0.42rem
        0.5rem;

    border-radius: 6px;

    font-size: 0.5rem;

    line-height: 1.4;

    font-weight: 620;
}

.success-message.positive {
    background: #ecf9f1;
    color: #238a52;
}

.success-message.moderate {
    background: #fff7e8;
    color: #b87912;
}

.success-message.support {
    background: #fff0f0;
    color: #bd4545;
}


/* ==========================================================
   RISK
========================================================== */

.risk-icon-line {
    display: flex;

    align-items: center;

    gap: 0.55rem;

    margin-bottom: 0.6rem;
}

.risk-icon {
    width: 34px;
    height: 34px;

    display: flex;

    justify-content: center;

    align-items: center;

    border-radius: 50%;

    font-size: 0.9rem;

    font-weight: 750;
}

.risk-icon.low {
    background: #eaf9f0;
    color: #24a862;
}

.risk-icon.moderate {
    background: #fff4e5;
    color: #dc8d17;
}

.risk-icon.high {
    background: #fff0f0;
    color: #d94b4b;
}

.risk-value {
    font-size: 0.76rem;

    font-weight: 790;
}

.risk-subtitle {
    margin-top: 0.1rem;

    color: #738097;

    font-size: 0.48rem;
}

.risk-scale {
    position: relative;

    width: 100%;
    height: 7px;

    margin:
        0.95rem
        0
        0.4rem
        0;

    border-radius: 20px;

    background:
        linear-gradient(
            90deg,
            #ef4444 0%,
            #f97316 28%,
            #f7b31c 55%,
            #64ba67 76%,
            #2eaa64 100%
        );
}

.risk-marker {
    position: absolute;

    top: -5px;

    width: 3px;
    height: 17px;

    background: #17345a;

    border-radius: 4px;

    transform:
        translateX(-50%);
}

.risk-labels {
    display: flex;

    justify-content: space-between;

    color: #77859a;

    font-size: 0.44rem;
}


/* ==========================================================
   SUMMARY
========================================================== */

.summary-box {
    display: flex;

    align-items: center;

    gap: 0.5rem;

    min-height: 46px;

    padding: 0.42rem;

    margin-bottom: 0.32rem;

    border:
        1px solid
        #e4eaf2;

    border-radius: 7px;

    background: #fcfdff;
}

.summary-icon {
    width: 27px;
    height: 27px;

    flex:
        0 0
        27px;

    display: flex;

    align-items: center;

    justify-content: center;

    border-radius: 50%;

    background: #edf8f1;

    color: #29a865;

    font-size: 0.66rem;
}

.summary-label {
    color: #718097;

    font-size: 0.47rem;
}

.summary-value {
    color: #203754;

    font-size: 0.61rem;

    font-weight: 760;
}


/* ==========================================================
   LOWER GRID
========================================================== */

.details-grid {
    display: grid;

    grid-template-columns:
        1fr
        1fr
        1.08fr;

    gap: 0.65rem;

    margin-top: 0.65rem;
}

.detail-card {
    min-height: 225px;

    padding: 0.78rem;

    display: flex;

    flex-direction: column;

    background: #ffffff;

    border:
        1px solid
        #dfe7f2;

    border-radius: 9px;

    overflow: hidden;
}

.detail-title {
    margin:
        0
        0
        0.12rem
        0;

    color: #20324e;

    font-size: 0.7rem;

    font-weight: 780;
}

.detail-subtitle {
    margin:
        0
        0
        0.52rem
        0;

    color: #77859a;

    font-size: 0.5rem;

    line-height: 1.35;
}


/* ==========================================================
   PROFILE TABLE
========================================================== */

.profile-table {
    width: 100%;

    border-collapse: collapse;

    font-size: 0.51rem;
}

.profile-table th {
    padding:
        0.3rem
        0.25rem;

    background: #f3f7fd;

    color: #65758d;

    text-align: left;

    font-size: 0.47rem;

    font-weight: 700;

    border-bottom:
        1px solid
        #e2e8f1;
}

.profile-table td {
    padding:
        0.32rem
        0.25rem;

    color: #314560;

    border-bottom:
        1px solid
        #edf1f6;
}

.profile-factor {
    font-weight: 620;
}


/* ==========================================================
   CONFIDENCE
========================================================== */

.confidence-strip {
    margin-top: 0.4rem;

    padding-top: 0.4rem;

    border-top:
        1px solid
        #edf1f5;
}

.confidence-strip-title {
    margin-bottom: 0.28rem;

    color: #314560;

    font-size: 0.5rem;

    font-weight: 700;
}

.confidence-chip {
    display: inline-block;

    margin:
        0
        0.18rem
        0.18rem
        0;

    padding:
        0.2rem
        0.34rem;

    background: #f2f5fa;

    border:
        1px solid
        #e2e8f0;

    border-radius: 5px;

    color: #4f6078;

    font-size: 0.45rem;
}


/* ==========================================================
   PREDICTION INPUTS
========================================================== */

.inputs-wrapper {
    flex: 1;

    display: flex;

    flex-direction: column;
}

.input-factor {
    margin-bottom: 0.62rem;
}

.input-factor-row {
    display: flex;

    justify-content: space-between;

    align-items: center;

    margin-bottom: 0.22rem;

    color: #41546e;

    font-size: 0.51rem;
}

.input-value {
    color: #233a59;

    font-size: 0.52rem;

    font-weight: 700;
}

.input-bar-bg {
    width: 100%;
    height: 7px;

    overflow: hidden;

    border-radius: 20px;

    background: #e9edf4;
}

.input-bar-fill {
    height: 100%;

    border-radius: inherit;

    background:
        linear-gradient(
            90deg,
            #55c47c,
            #3dae68
        );
}


/* ==========================================================
   DETAIL INFO BOX
========================================================== */

.detail-info-box {
    width: 100%;

    margin-top: auto;

    display: flex;

    align-items: flex-start;

    gap: 0.42rem;

    padding:
        0.48rem
        0.52rem;

    background: #f1f6ff;

    border:
        1px solid
        #dce8f8;

    border-radius: 6px;
}

.detail-info-icon {
    width: 18px;
    height: 18px;

    min-width: 18px;

    display: flex;

    align-items: center;

    justify-content: center;

    border:
        1.3px solid
        #3d82eb;

    border-radius: 50%;

    color: #2873e5;

    font-size: 0.46rem;

    font-weight: 800;
}

.detail-info-title {
    color: #314b70;

    font-size: 0.5rem;

    font-weight: 720;
}

.detail-info-text {
    color: #637792;

    font-size: 0.47rem;

    line-height: 1.38;
}


/* ==========================================================
   WHAT THIS MEANS
========================================================== */

.meanings-wrapper {
    flex: 1;

    display: flex;

    flex-direction: column;
}

.meaning-item {
    display: flex;

    align-items: flex-start;

    gap: 0.52rem;

    margin-bottom: 0.52rem;
}

.meaning-icon {
    width: 29px;
    height: 29px;

    flex:
        0 0
        29px;

    display: flex;

    justify-content: center;

    align-items: center;

    border-radius: 50%;

    background: #ebf8f0;

    color: #29a865;

    font-size: 0.68rem;
}

.meaning-icon.orange {
    background: #fff4e7;

    color: #ef8d24;
}

.meaning-icon.blue {
    background: #eef4ff;

    color: #3478df;
}

.meaning-title {
    margin-bottom: 0.1rem;

    color: #263a58;

    font-size: 0.54rem;

    font-weight: 760;
}

.meaning-text {
    color: #718098;

    font-size: 0.48rem;

    line-height: 1.4;
}


/* ==========================================================
   INTERESTS
========================================================== */

.interests-note {
    width: 100%;

    margin-top: auto;

    display: flex;

    align-items: flex-start;

    gap: 0.42rem;

    padding:
        0.46rem
        0.52rem;

    background: #f5f8fd;

    border:
        1px solid
        #e3eaf3;

    border-radius: 6px;
}

.interests-icon {
    width: 18px;
    height: 18px;

    min-width: 18px;

    display: flex;

    align-items: center;

    justify-content: center;

    border-radius: 50%;

    background: #eaf2ff;

    color: #3175dc;

    font-size: 0.46rem;

    font-weight: 800;
}

.interests-label {
    color: #314b70;

    font-size: 0.5rem;

    font-weight: 720;
}

.interests-text {
    margin-top: 0.08rem;

    color: #657893;

    font-size: 0.47rem;

    line-height: 1.38;
}


/* ==========================================================
   PREDICTION NOTE
========================================================== */

.model-note {
    display: flex;

    gap: 0.55rem;

    align-items: flex-start;

    margin-top: 0.62rem;

    padding:
        0.58rem
        0.7rem;

    background: #eef5ff;

    border:
        1px solid
        #dce9fa;

    border-radius: 8px;
}

.model-note-icon {
    width: 18px;
    height: 18px;

    min-width: 18px;

    display: flex;

    align-items: center;

    justify-content: center;

    border:
        1.3px solid
        #347be5;

    border-radius: 50%;

    color: #2470dc;

    font-size: 0.46rem;

    font-weight: 800;
}

.model-note-title {
    color: #263a58;

    font-size: 0.52rem;

    font-weight: 750;
}

.model-note-text {
    color: #61738d;

    font-size: 0.48rem;

    line-height: 1.4;
}


/* ==========================================================
   PAGE ACTION BUTTONS
========================================================== */

main div.stButton > button {
    min-height:
        2.35rem !important;

    height:
        2.35rem !important;

    border-radius:
        6px !important;

    font-size:
        0.61rem !important;

    font-weight:
        700 !important;

    padding:
        0.4rem
        0.8rem !important;

    white-space:
        nowrap !important;
}


/* ==========================================================
   UPDATE INFORMATION BUTTON
========================================================== */

.st-key-update_information button {
    background:
        #ffffff !important;

    border:
        1px solid
        #8eb5ec !important;

    color:
        #1767e8 !important;

    white-space:
        nowrap !important;

    overflow:
        hidden !important;
}

.st-key-update_information button * {
    color:
        #1767e8 !important;

    -webkit-text-fill-color:
        #1767e8 !important;

    white-space:
        nowrap !important;

    font-size:
        0.61rem !important;

    line-height:
        1 !important;
}


/* ==========================================================
   VIEW RECOMMENDATIONS BUTTON
========================================================== */

.st-key-view_recommendations button {
    background:
        linear-gradient(
            135deg,
            #1767e8,
            #0759d6
        ) !important;

    border:
        1px solid
        #1767e8 !important;

    color:
        #ffffff !important;

    white-space:
        nowrap !important;

    overflow:
        hidden !important;
}

.st-key-view_recommendations button * {
    color:
        #ffffff !important;

    -webkit-text-fill-color:
        #ffffff !important;

    white-space:
        nowrap !important;

    font-size:
        0.61rem !important;

    line-height:
        1 !important;
}


/* ==========================================================
   FOOTER
========================================================== */

.results-footer {
    min-height: 1.25rem;

    display: flex;

    align-items: center;

    color: #8b97aa;

    font-size: 0.52rem;
}


/* ==========================================================
   TABLET
========================================================== */

@media (max-width: 1050px) {

    .top-result-grid,
    .details-grid {
        grid-template-columns: 1fr;
    }

    .how-card {
        align-items: flex-start;
    }

    .how-inputs {
        min-width: 0;

        flex-wrap: wrap;

        justify-content: flex-start;
    }
}


/* ==========================================================
   MOBILE
========================================================== */

@media (max-width: 768px) {

    .block-container {
        padding:
            0.65rem
            0.7rem !important;
    }

    .prediction-flex {
        flex-direction: column;

        align-items: flex-start;
    }

    .results-title {
        font-size: 1.25rem;
    }

    .empty-card {
        min-height: 320px;

        padding:
            1.5rem
            1rem;
    }

    .how-card {
        flex-direction: column;
    }

    .how-inputs {
        width: 100%;

        justify-content: flex-start;
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
# PAGE HEADER
# ============================================================

st.html("""
<div class="results-header">

    <h1 class="results-title">
        Prediction Results
    </h1>

    <p class="results-subtitle">

        View your predicted academic performance based on
        the information you provided.

    </p>

</div>
""")


# ============================================================
# NO PREDICTION
# ============================================================

if "prediction" not in st.session_state:

    st.html("""
    <div class="empty-card">

        <div class="empty-icon-wrap">

            <div class="empty-chart">

                <div class="empty-line"></div>

                <div class="empty-bar empty-bar-one"></div>

                <div class="empty-bar empty-bar-two"></div>

                <div class="empty-bar empty-bar-three"></div>

            </div>

        </div>


        <h2 class="empty-heading">
            No Prediction Available Yet
        </h2>


        <div class="empty-description">

            You have not generated a prediction yet.
            Complete your Academic Information first,
            then return here to view your predicted
            academic outcome and risk level.

        </div>

    </div>
    """)


    st.html("""
    <div class="empty-button-space"></div>
    """)


    empty_left, empty_button, empty_right = st.columns(
        [2.2, 1.25, 2.2],
        gap="small"
    )


    with empty_button:

        if st.button(
            "Go to Academic Information →",
            type="primary",
            use_container_width=True,
            key="go_academic_info"
        ):

            st.switch_page(
                "pages/1_Academic_Information.py"
            )


    st.html("""
    <div class="how-card">

        <div class="how-icon-wrap">
            i
        </div>


        <div class="how-main">

            <div class="how-title">
                How your prediction is generated
            </div>

            <div class="how-text">

                Complete your academic information first.
                Your prediction is based on three academic
                performance values and your results will then
                become available on this page.

            </div>

        </div>


        <div class="how-inputs">

            <div class="how-pill">
                Study Hours
            </div>

            <div class="how-pill">
                Attendance Rate
            </div>

            <div class="how-pill">
                Past Exam Score
            </div>

        </div>

    </div>
    """)

    st.stop()


# ============================================================
# RETRIEVE DATA
# ============================================================

prediction = st.session_state["prediction"]

pass_probability = float(
    st.session_state["pass_probability"]
)

fail_probability = float(
    st.session_state["fail_probability"]
)

study_hours = st.session_state["study_hours"]

attendance = float(
    st.session_state["attendance"]
)

past_exam_score = st.session_state["past_exam_score"]

academic_area = st.session_state["academic_area"]

confidence_scores = st.session_state.get(
    "confidence_scores",
    {}
)

interests = st.session_state.get(
    "interests",
    []
)

academic_goal = st.session_state.get(
    "academic_goal",
    "Not specified"
)


# ============================================================
# RISK CLASSIFICATION
# ============================================================

if pass_probability >= 75:

    risk_level = "Low Risk"
    outlook = "Strong"

    risk_colour = "#1d9b58"
    risk_icon = "✓"
    risk_icon_class = "low"
    message_class = "positive"

    probability_message = (
        "High Predicted Pass Probability"
    )

    overall_message = (
        "Your current academic information indicates a strong "
        "predicted academic outcome."
    )

    support_message = (
        "Your current prediction is positive. "
        "Keep maintaining your academic habits."
    )


elif pass_probability >= 50:

    risk_level = "Moderate Risk"
    outlook = "Moderate"

    risk_colour = "#d99417"
    risk_icon = "!"
    risk_icon_class = "moderate"
    message_class = "moderate"

    probability_message = (
        "Moderate Predicted Pass Probability"
    )

    overall_message = (
        "Your current academic information indicates a moderate "
        "predicted academic outcome."
    )

    support_message = (
        "Your current result suggests that additional academic "
        "support may be useful in some areas."
    )


else:

    risk_level = "High Risk"
    outlook = "Needs Support"

    risk_colour = "#d94b4b"
    risk_icon = "!"
    risk_icon_class = "high"
    message_class = "support"

    probability_message = (
        "Low Predicted Pass Probability"
    )

    overall_message = (
        "Your current academic information indicates a higher "
        "level of predicted academic risk."
    )

    support_message = (
        "Consider focusing on consistent study habits, "
        "attendance and the areas where you need the most support."
    )


# ============================================================
# RISK SCALE POSITION
# ============================================================

risk_marker_position = max(
    0,
    min(
        100,
        pass_probability
    )
)


# ============================================================
# BAR DISPLAY VALUES
# ============================================================

study_display = max(
    0,
    min(
        100,
        ((study_hours - 10) / (39 - 10)) * 100
    )
)

attendance_display = max(
    0,
    min(
        100,
        ((attendance - 50) / 50) * 100
    )
)

exam_display = max(
    0,
    min(
        100,
        ((past_exam_score - 50) / 50) * 100
    )
)


# ============================================================
# CONFIDENCE HTML
# ============================================================

confidence_html = ""

for skill, score in confidence_scores.items():

    confidence_html += f"""
    <span class="confidence-chip">
        {skill}: {score}/5
    </span>
    """


if not confidence_html:

    confidence_html = """
    <span class="confidence-chip">
        No confidence ratings available
    </span>
    """


# ============================================================
# INTERESTS
# ============================================================

if interests:

    interest_text = ", ".join(interests)

else:

    interest_text = "No topics selected"


# ============================================================
# TOP RESULT CARDS
# ============================================================

st.html(
    f"""
    <div class="top-result-grid">

        <div class="result-card">

            <div class="card-heading">
                Overall Prediction
            </div>

            <div class="prediction-flex">

                <div
                    class="probability-ring"
                    style="--percentage:{pass_probability:.1f};"
                >

                    <div class="probability-content">

                        <div class="probability-number">
                            {pass_probability:.0f}%
                        </div>

                        <div class="probability-caption">
                            Predicted Pass Probability
                        </div>

                    </div>

                </div>

                <div>

                    <div
                        class="outcome-name"
                        style="color:{risk_colour};"
                    >
                        {probability_message}
                    </div>

                    <div class="outcome-description">

                        Based on the academic information you provided,
                        your predicted outcome is <b>{prediction}</b>.

                    </div>

                    <div class="success-message {message_class}">
                        {support_message}
                    </div>

                </div>

            </div>

        </div>


        <div class="result-card">

            <div class="card-heading">
                Risk Level
            </div>

            <div class="risk-icon-line">

                <div class="risk-icon {risk_icon_class}">
                    {risk_icon}
                </div>

                <div>

                    <div
                        class="risk-value"
                        style="color:{risk_colour};"
                    >
                        {risk_level}
                    </div>

                    <div class="risk-subtitle">
                        Your predicted risk level is
                        {risk_level.lower()}.
                    </div>

                </div>

            </div>

            <div class="risk-scale">

                <div
                    class="risk-marker"
                    style="left:{risk_marker_position}%;"
                ></div>

            </div>

            <div class="risk-labels">

                <span>High Risk</span>

                <span>Moderate Risk</span>

                <span>Low Risk</span>

            </div>

        </div>


        <div class="result-card">

            <div class="card-heading">
                Quick Summary
            </div>

            <div class="summary-box">

                <div class="summary-icon">
                    ▥
                </div>

                <div>

                    <div class="summary-label">
                        Pass Probability
                    </div>

                    <div class="summary-value">
                        {pass_probability:.1f}%
                    </div>

                </div>

            </div>

            <div class="summary-box">

                <div class="summary-icon">
                    ◇
                </div>

                <div>

                    <div class="summary-label">
                        Risk Level
                    </div>

                    <div class="summary-value">
                        {risk_level}
                    </div>

                </div>

            </div>

            <div class="summary-box">

                <div class="summary-icon">
                    ☆
                </div>

                <div>

                    <div class="summary-label">
                        Overall Outlook
                    </div>

                    <div class="summary-value">
                        {outlook}
                    </div>

                </div>

            </div>

        </div>

    </div>
    """
)


# ============================================================
# LOWER RESULT CARDS
# ============================================================

st.html(
    f"""
    <div class="details-grid">

        <div class="detail-card">

            <div class="detail-title">
                Your Academic Profile Summary
            </div>

            <div class="detail-subtitle">
                Information associated with this prediction.
            </div>

            <table class="profile-table">

                <tr>
                    <th>Factor</th>
                    <th>Your Value</th>
                </tr>

                <tr>
                    <td class="profile-factor">
                        Attendance Rate
                    </td>

                    <td>
                        {attendance:.1f}%
                    </td>
                </tr>

                <tr>
                    <td class="profile-factor">
                        Study Hours per Week
                    </td>

                    <td>
                        {study_hours}
                    </td>
                </tr>

                <tr>
                    <td class="profile-factor">
                        Past Exam Score
                    </td>

                    <td>
                        {past_exam_score}
                    </td>
                </tr>

                <tr>
                    <td class="profile-factor">
                        Academic Area
                    </td>

                    <td>
                        {academic_area}
                    </td>
                </tr>

                <tr>
                    <td class="profile-factor">
                        Academic Goal
                    </td>

                    <td>
                        {academic_goal}
                    </td>
                </tr>

            </table>

            <div class="confidence-strip">

                <div class="confidence-strip-title">
                    Confidence Profile
                </div>

                {confidence_html}

            </div>

        </div>


        <div class="detail-card">

            <div class="detail-title">
                Information Used for Your Prediction
            </div>

            <div class="detail-subtitle">

                These are the three academic values used
                to calculate your prediction.

            </div>

            <div class="inputs-wrapper">

                <div class="input-factor">

                    <div class="input-factor-row">

                        <span>
                            Attendance Rate
                        </span>

                        <span class="input-value">
                            {attendance:.1f}%
                        </span>

                    </div>

                    <div class="input-bar-bg">

                        <div
                            class="input-bar-fill"
                            style="width:{attendance_display:.1f}%;"
                        ></div>

                    </div>

                </div>


                <div class="input-factor">

                    <div class="input-factor-row">

                        <span>
                            Study Hours per Week
                        </span>

                        <span class="input-value">
                            {study_hours}
                        </span>

                    </div>

                    <div class="input-bar-bg">

                        <div
                            class="input-bar-fill"
                            style="width:{study_display:.1f}%;"
                        ></div>

                    </div>

                </div>


                <div class="input-factor">

                    <div class="input-factor-row">

                        <span>
                            Past Exam Score
                        </span>

                        <span class="input-value">
                            {past_exam_score}
                        </span>

                    </div>

                    <div class="input-bar-bg">

                        <div
                            class="input-bar-fill"
                            style="width:{exam_display:.1f}%;"
                        ></div>

                    </div>

                </div>


                <div class="detail-info-box">

                    <div class="detail-info-icon">
                        i
                    </div>

                    <div>

                        <div class="detail-info-title">
                            Information used for your prediction
                        </div>

                        <div class="detail-info-text">

                            Only Study Hours, Attendance Rate and
                            Past Exam Score are used to calculate
                            your predicted academic outcome.
                            Other profile information is used
                            separately to personalise your
                            learning recommendations.

                        </div>

                    </div>

                </div>

            </div>

        </div>


        <div class="detail-card">

            <div class="detail-title">
                What This Means
            </div>

            <div class="detail-subtitle">
                A simple explanation of your current results.
            </div>

            <div class="meanings-wrapper">

                <div class="meaning-item">

                    <div class="meaning-icon">
                        ✓
                    </div>

                    <div>

                        <div class="meaning-title">
                            Your predicted outcome
                        </div>

                        <div class="meaning-text">
                            {overall_message}
                        </div>

                    </div>

                </div>


                <div class="meaning-item">

                    <div class="meaning-icon orange">
                        !
                    </div>

                    <div>

                        <div class="meaning-title">
                            Use the result as guidance
                        </div>

                        <div class="meaning-text">

                            This prediction is an estimate based
                            on the information you provided and
                            does not guarantee your future result.

                        </div>

                    </div>

                </div>


                <div class="meaning-item">

                    <div class="meaning-icon blue">
                        ▣
                    </div>

                    <div>

                        <div class="meaning-title">
                            Continue to your recommendations
                        </div>

                        <div class="meaning-text">

                            Your academic profile and predicted
                            performance are used to personalise
                            relevant learning resources for you.

                        </div>

                    </div>

                </div>


                <div class="interests-note">

                    <div class="interests-icon">
                        i
                    </div>

                    <div>

                        <div class="interests-label">
                            Topics considered
                        </div>

                        <div class="interests-text">
                            {interest_text}
                        </div>

                    </div>

                </div>

            </div>

        </div>

    </div>
    """
)


# ============================================================
# PREDICTION NOTE
# ============================================================

st.html("""
<div class="model-note">

    <div class="model-note-icon">
        i
    </div>

    <div>

        <div class="model-note-title">
            About this prediction
        </div>

        <div class="model-note-text">

            Your prediction is based only on Study Hours per Week,
            Attendance Rate and Past Exam Score. The Predicted Pass
            Probability is an estimate based on the information you
            provided and does not guarantee your future result.
            Your confidence ratings, interests and academic goal are
            used separately to personalise your learning recommendations.

        </div>

    </div>

</div>
""")


# ============================================================
# PAGE NAVIGATION
# ============================================================

nav_space, update_col, recommendation_col = st.columns(
    [4.8, 1.9, 1.75],
    gap="small"
)


with update_col:

    if st.button(
        "← Update Academic Information",
        use_container_width=True,
        key="update_information"
    ):

        st.switch_page(
            "pages/1_Academic_Information.py"
        )


with recommendation_col:

    if st.button(
        "View Recommendations →",
        type="primary",
        use_container_width=True,
        key="view_recommendations"
    ):

        st.switch_page(
            "pages/3_Recommendations.py"
        )


# ============================================================
# FOOTER
# ============================================================

st.html("""
<div class="results-footer">
    © 2026 All rights reserved.
</div>
""")