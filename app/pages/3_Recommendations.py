import streamlit as st
import pandas as pd
import html

from pathlib import Path

from recommendation.recommender import recommend_resources


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Recommendations",
    page_icon="⭐",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# RESET FUNCTION
# ============================================================

def reset_application():
    st.session_state.clear()


# ============================================================
# PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parents[2]

RESOURCE_PATH = (
    BASE_DIR
    / "data"
    / "recommendation"
    / "learning_resources.csv"
)


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
   MAIN PAGE
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
        0 0 8px
        rgba(67,146,255,0.55);
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

.recommendation-header {
    margin-bottom: 0.55rem;
}

.recommendation-title {
    margin: 0;

    color: #102347;

    font-size: 1.55rem;

    line-height: 1.05;

    font-weight: 820;
}

.recommendation-subtitle {
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

    align-items: center;

    justify-content: center;

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

    align-items: center;

    justify-content: center;

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

    color: #755ce8;

    font-size: 2rem;
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
    max-width: 520px;

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
   EMPTY CTA BUTTON
========================================================== */

.empty-button-spacer {
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

    white-space: nowrap !important;
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
   HOW RECOMMENDATIONS ARE GENERATED
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
   GENERAL CARDS
========================================================== */

.recommendation-card {
    width: 100%;

    background: #ffffff;

    border:
        1px solid
        #dce6f2;

    border-radius: 10px;

    box-shadow:
        0 2px 10px
        rgba(21,52,91,0.025);
}

.section-heading {
    margin: 0;

    color: #1b3151;

    font-size: 0.74rem;

    line-height: 1.25;

    font-weight: 780;
}

.section-description {
    margin-top: 0.15rem;

    color: #77869b;

    font-size: 0.51rem;

    line-height: 1.4;
}


/* ==========================================================
   LEARNING PATH
========================================================== */

.path-card {
    padding:
        0.78rem
        0.9rem
        0.85rem
        0.9rem;

    margin-bottom: 0.65rem;
}

.path-stage-row {
    width: 100%;

    display: flex;

    align-items: stretch;

    gap: 0.35rem;

    margin-top: 0.65rem;
}

.path-stage {
    flex: 1;

    min-width: 0;

    display: flex;

    align-items: flex-start;

    gap: 0.48rem;

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
        #e0e8f2;

    border-radius: 8px;
}

.path-number {
    width: 25px;
    height: 25px;

    min-width: 25px;

    display: flex;

    align-items: center;

    justify-content: center;

    border-radius: 50%;

    color: #ffffff;

    font-size: 0.54rem;

    font-weight: 800;
}

.path-number.green {
    background: #2eb873;
}

.path-number.blue {
    background: #3177ed;
}

.path-number.orange {
    background: #f0a120;
}

.path-stage-name {
    color: #253d60;

    font-size: 0.58rem;

    font-weight: 750;
}

.path-stage-text {
    margin-top: 0.12rem;

    color: #75849a;

    font-size: 0.46rem;

    line-height: 1.4;
}

.path-arrow {
    width: 25px;

    min-width: 25px;

    display: flex;

    align-items: center;

    justify-content: center;

    color: #5d8be4;

    font-size: 0.95rem;
}

.path-footer {
    margin-top: 0.55rem;

    padding:
        0.42rem
        0.55rem;

    display: flex;

    align-items: center;

    gap: 0.42rem;

    background: #f2f6ff;

    border-radius: 6px;

    color: #536d94;

    font-size: 0.48rem;

    line-height: 1.4;
}

.path-info-icon {
    width: 17px;
    height: 17px;

    min-width: 17px;

    display: flex;

    align-items: center;

    justify-content: center;

    border:
        1px solid
        #4382e4;

    border-radius: 50%;

    color: #2770dc;

    font-size: 0.43rem;

    font-weight: 800;
}


/* ==========================================================
   MAIN GRID
========================================================== */

.recommendation-grid {
    display: grid;

    grid-template-columns:
        1.45fr
        0.72fr;

    gap: 0.65rem;

    align-items: stretch;
}


/* ==========================================================
   RESOURCES PANEL
========================================================== */

.resources-panel {
    padding:
        0.78rem
        0.85rem;

    min-height: 355px;
}

.resources-header {
    margin-bottom: 0.48rem;
}

.resource-list {
    width: 100%;

    overflow: hidden;

    border:
        1px solid
        #e6ebf2;

    border-radius: 7px;
}

.resource-table-head {
    display: grid;

    grid-template-columns:
        1.25fr
        0.74fr
        2.1fr
        0.18fr;

    gap: 0.5rem;

    padding:
        0.38rem
        0.55rem;

    background: #f4f7fb;

    color: #6e7c91;

    font-size: 0.46rem;

    font-weight: 700;

    border-bottom:
        1px solid
        #e5eaf1;
}

.resource-row {
    display: grid;

    grid-template-columns:
        1.25fr
        0.74fr
        2.1fr
        0.18fr;

    gap: 0.5rem;

    align-items: center;

    min-height: 49px;

    padding:
        0.42rem
        0.55rem;

    background: #ffffff;

    border-bottom:
        1px solid
        #edf1f5;
}

.resource-row:last-child {
    border-bottom: none;
}

.resource-name-wrap {
    display: flex;

    align-items: center;

    gap: 0.38rem;

    min-width: 0;
}

.resource-icon {
    width: 24px;
    height: 24px;

    min-width: 24px;

    display: flex;

    align-items: center;

    justify-content: center;

    border-radius: 6px;

    background: #edf8f1;

    color: #29a665;

    font-size: 0.56rem;

    font-weight: 800;
}

.resource-name {
    color: #273b59;

    font-size: 0.51rem;

    line-height: 1.3;

    font-weight: 680;
}

.resource-provider {
    margin-top: 0.08rem;

    color: #8a95a6;

    font-size: 0.40rem;

    line-height: 1.25;
}

.match-badge {
    width: fit-content;

    padding:
        0.2rem
        0.35rem;

    border-radius: 999px;

    background: #eaf8ef;

    color: #29905b;

    font-size: 0.42rem;

    line-height: 1;

    font-weight: 700;
}

.resource-reason {
    color: #61728b;

    font-size: 0.46rem;

    line-height: 1.4;
}

.resource-meta {
    margin-top: 0.12rem;

    color: #8a96a8;

    font-size: 0.40rem;

    line-height: 1.3;
}

.resource-link {
    color: #3478e5;

    font-size: 0.72rem;

    text-decoration: none;

    text-align: right;
}

.resource-link:hover {
    color: #155fd2;
}

.resource-footer {
    margin-top: 0.48rem;

    padding:
        0.4rem
        0.5rem;

    display: flex;

    align-items: flex-start;

    gap: 0.4rem;

    background: #f3f7ff;

    border-radius: 6px;
}

.resource-footer-icon {
    width: 17px;
    height: 17px;

    min-width: 17px;

    display: flex;

    align-items: center;

    justify-content: center;

    border:
        1px solid
        #3c7fe5;

    border-radius: 50%;

    color: #2872db;

    font-size: 0.42rem;

    font-weight: 800;
}

.resource-footer-text {
    color: #5c7191;

    font-size: 0.46rem;

    line-height: 1.4;
}


/* ==========================================================
   RIGHT SIDE
========================================================== */

.side-stack {
    display: flex;

    flex-direction: column;

    gap: 0.65rem;
}

.focus-panel {
    padding:
        0.78rem
        0.82rem;
}

.focus-item {
    display: flex;

    align-items: center;

    gap: 0.48rem;

    min-height: 51px;

    padding: 0.4rem 0;

    border-bottom:
        1px solid
        #edf1f5;
}

.focus-item:last-child {
    border-bottom: none;
}

.focus-icon {
    width: 30px;
    height: 30px;

    min-width: 30px;

    display: flex;

    align-items: center;

    justify-content: center;

    border-radius: 50%;

    font-size: 0.64rem;

    font-weight: 800;
}

.focus-icon.green {
    background: #eaf8f0;
    color: #27a661;
}

.focus-icon.orange {
    background: #fff4e6;
    color: #f09221;
}

.focus-icon.purple {
    background: #f1edff;
    color: #7556e1;
}

.focus-content {
    flex: 1;
    min-width: 0;
}

.focus-name {
    color: #253a59;

    font-size: 0.52rem;

    font-weight: 720;
}

.focus-description {
    margin-top: 0.08rem;

    color: #76859a;

    font-size: 0.43rem;

    line-height: 1.35;
}

.focus-priority {
    font-size: 0.40rem;

    font-weight: 720;

    white-space: nowrap;
}

.priority-high {
    color: #2aa466;
}

.priority-medium {
    color: #dc921e;
}

.priority-low {
    color: #7655df;
}


/* ==========================================================
   GOAL
========================================================== */

.goal-panel {
    padding:
        0.78rem
        0.82rem;

    flex: 1;
}

.goal-content {
    display: flex;

    align-items: center;

    gap: 0.6rem;

    margin-top: 0.55rem;

    padding: 0.6rem;

    background:
        linear-gradient(
            135deg,
            #f2f6ff,
            #f8faff
        );

    border:
        1px solid
        #e2e9f4;

    border-radius: 8px;
}

.goal-icon {
    width: 38px;
    height: 38px;

    min-width: 38px;

    display: flex;

    align-items: center;

    justify-content: center;

    border-radius: 50%;

    background: #e9f0ff;

    color: #1767e8;

    font-size: 0.8rem;

    font-weight: 800;
}

.goal-name {
    color: #2362c4;

    font-size: 0.56rem;

    font-weight: 760;
}

.goal-description {
    margin-top: 0.1rem;

    color: #6d7d94;

    font-size: 0.44rem;

    line-height: 1.4;
}


/* ==========================================================
   METHOD NOTE
========================================================== */

.method-note {
    display: flex;

    align-items: flex-start;

    gap: 0.55rem;

    margin-top: 0.65rem;

    padding:
        0.62rem
        0.75rem;

    background:
        linear-gradient(
            135deg,
            #f3f7ff,
            #eef4ff
        );

    border:
        1px solid
        #dce8f8;

    border-radius: 8px;
}

.method-icon {
    width: 21px;
    height: 21px;

    min-width: 21px;

    display: flex;

    align-items: center;

    justify-content: center;

    border:
        1.4px solid
        #347be5;

    border-radius: 50%;

    color: #2470dc;

    font-size: 0.48rem;

    font-weight: 800;
}

.method-title {
    color: #294264;

    font-size: 0.51rem;

    font-weight: 750;
}

.method-text {
    margin-top: 0.08rem;

    color: #627792;

    font-size: 0.46rem;

    line-height: 1.4;
}


/* ==========================================================
   PAGE BUTTONS
========================================================== */

main div.stButton > button {
    min-height: 2.35rem !important;
    height: 2.35rem !important;

    border-radius: 6px !important;

    font-size: 0.61rem !important;
    font-weight: 700 !important;

    padding:
        0.4rem
        0.8rem !important;

    white-space: nowrap !important;
}


/* ==========================================================
   UPDATE ACADEMIC INFORMATION
========================================================== */

.st-key-update_academic button {
    background: #ffffff !important;

    border:
        1px solid
        #8eb5ec !important;

    color: #1767e8 !important;

    white-space: nowrap !important;

    overflow: hidden !important;

    box-shadow: none !important;
}

.st-key-update_academic button * {
    color: #1767e8 !important;

    -webkit-text-fill-color:
        #1767e8 !important;

    white-space: nowrap !important;

    font-size: 0.61rem !important;

    line-height: 1 !important;
}


/* ==========================================================
   VIEW ACADEMIC INSIGHTS
========================================================== */

.st-key-view_insights button {
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

    overflow: hidden !important;

    box-shadow:
        0 4px 12px
        rgba(23,103,232,0.16) !important;
}

.st-key-view_insights button * {
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
   TABLET
========================================================== */

@media (max-width: 1050px) {

    .recommendation-grid {
        grid-template-columns: 1fr;
    }

    .path-stage-row {
        flex-wrap: wrap;
    }

    .path-stage {
        flex:
            1 1
            220px;
    }

    .path-arrow {
        display: none;
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

    .recommendation-title {
        font-size: 1.25rem;
    }

    .empty-card {
        min-height: 320px;

        padding:
            1.5rem
            1rem;
    }

    .resource-table-head {
        display: none;
    }

    .resource-row {
        grid-template-columns: 1fr;

        gap: 0.25rem;
    }

    .resource-link {
        text-align: left;
    }

    .how-card {
        flex-direction: column;

        align-items: flex-start;
    }

    .how-inputs {
        width: 100%;

        min-width: 0;

        justify-content: flex-start;

        flex-wrap: wrap;
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
<div class="recommendation-header">

    <h1 class="recommendation-title">
        Personalised Recommendations
    </h1>

    <p class="recommendation-subtitle">

        Explore learning resources and a suggested learning path
        based on your academic profile and predicted performance.

    </p>

</div>
""")


# ============================================================
# REQUIRED SESSION DATA
# ============================================================

required_keys = [
    "academic_area",
    "confidence_scores",
    "interests",
    "academic_goal",
    "pass_probability"
]


missing_keys = [
    key
    for key in required_keys
    if key not in st.session_state
]


# ============================================================
# EMPTY STATE
# ============================================================

if missing_keys:

    st.html("""
    <div class="empty-card">

        <div class="empty-icon-wrap">
            ☆
        </div>

        <h2 class="empty-heading">
            No Recommendations Available Yet
        </h2>

        <div class="empty-description">

            Complete your Academic Information and generate
            a prediction first. Your personalised learning
            resources and suggested learning path will then
            appear here.

        </div>

    </div>
    """)


    st.html("""
    <div class="empty-button-spacer"></div>
    """)


    button_left, button_col, button_right = st.columns(
        [2.2, 1.25, 2.2],
        gap="small"
    )


    with button_col:

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
                How your recommendations are created
            </div>

            <div class="how-text">

                Your academic profile, confidence ratings,
                interests, academic goal and predicted performance
                help identify learning resources that are suitable
                for you and organise them into a suggested
                learning path.

            </div>

        </div>


        <div class="how-inputs">

            <div class="how-pill">
                Confidence
            </div>

            <div class="how-pill">
                Interests
            </div>

            <div class="how-pill">
                Academic Goal
            </div>

        </div>

    </div>
    """)

    st.stop()


# ============================================================
# LOAD RESOURCE DATASET
# ============================================================

if not RESOURCE_PATH.exists():

    st.error(
        "The learning resource dataset could not be found."
    )

    st.stop()


resources_df = pd.read_csv(
    RESOURCE_PATH
)


# ============================================================
# RETRIEVE CURRENT STUDENT PROFILE
# ============================================================

academic_area = st.session_state[
    "academic_area"
]

confidence_scores = st.session_state[
    "confidence_scores"
]

interests = st.session_state[
    "interests"
]

academic_goal = st.session_state[
    "academic_goal"
]

pass_probability = float(
    st.session_state[
        "pass_probability"
    ]
)


# ============================================================
# GENERATE RECOMMENDATIONS
# ============================================================

recommendation_results = recommend_resources(
    resources_df=resources_df,
    academic_area=academic_area,
    confidence_scores=confidence_scores,
    interests=interests,
    academic_goal=academic_goal,
    pass_probability=pass_probability,
    top_n=5
)


priority_skill = recommendation_results[
    "priority_skill"
]

priority_skills = recommendation_results[
    "priority_skills"
]

preferred_difficulties = recommendation_results[
    "preferred_difficulties"
]

top_recommendations = recommendation_results[
    "top_recommendations"
]

learning_path = recommendation_results[
    "learning_path"
]


# ============================================================
# SAVE RECOMMENDATION STATE
# ============================================================

st.session_state[
    "priority_skill"
] = priority_skill

st.session_state[
    "priority_skills"
] = priority_skills

st.session_state[
    "preferred_difficulties"
] = preferred_difficulties

st.session_state[
    "recommendations"
] = top_recommendations

st.session_state[
    "learning_path"
] = learning_path


# ============================================================
# EMPTY RESULT SAFETY
# ============================================================

if top_recommendations.empty:

    st.html("""
    <div class="empty-card">

        <div class="empty-icon-wrap">
            ☆
        </div>

        <h2 class="empty-heading">
            No Suitable Resources Found
        </h2>

        <div class="empty-description">

            No suitable learning resources were found for your
            current academic profile. You can update your
            Academic Information and generate a new prediction.

        </div>

    </div>
    """)


    st.html("""
    <div class="empty-button-spacer"></div>
    """)


    button_left, button_col, button_right = st.columns(
        [2.2, 1.25, 2.2],
        gap="small"
    )


    with button_col:

        if st.button(
            "Update Academic Information →",
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
                About your recommendations
            </div>

            <div class="how-text">

                Recommendations depend on the learning resources
                available for your selected academic area and
                the information in your current academic profile.

            </div>

        </div>


        <div class="how-inputs">

            <div class="how-pill">
                Academic Area
            </div>

            <div class="how-pill">
                Profile
            </div>

            <div class="how-pill">
                Resources
            </div>

        </div>

    </div>
    """)

    st.stop()


# ============================================================
# LEARNING PATH CONFIGURATION
# ============================================================

stage_order = [
    "Foundations",
    "Core Skills",
    "Advanced Topics"
]


available_stages = [
    stage
    for stage in stage_order
    if stage in learning_path[
        "Learning_Path_Stage"
    ].dropna().unique()
]


stage_descriptions = {

    "Foundations":
        "Build the core knowledge needed before moving "
        "towards more specialised material.",

    "Core Skills":
        "Develop the main practical and academic skills "
        "relevant to your selected area.",

    "Advanced Topics":
        "Progress towards more advanced concepts and "
        "higher-level learning resources."
}


stage_classes = {

    "Foundations":
        "green",

    "Core Skills":
        "blue",

    "Advanced Topics":
        "orange"
}


# ============================================================
# BUILD LEARNING PATH HTML
# ============================================================

path_html = ""


for index, stage in enumerate(
    available_stages
):

    stage_number = index + 1

    stage_class = stage_classes.get(
        stage,
        "blue"
    )

    description = stage_descriptions.get(
        stage,
        "Continue developing your academic knowledge."
    )


    path_html += f"""
    <div class="path-stage">

        <div class="path-number {stage_class}">
            {stage_number}
        </div>

        <div>

            <div class="path-stage-name">
                {html.escape(stage)}
            </div>

            <div class="path-stage-text">
                {html.escape(description)}
            </div>

        </div>

    </div>
    """


    if index < len(
        available_stages
    ) - 1:

        path_html += """
        <div class="path-arrow">
            →
        </div>
        """


# ============================================================
# LEARNING PATH PANEL
# ============================================================

st.html(
    f"""
    <div class="recommendation-card path-card">

        <h2 class="section-heading">
            Recommended Learning Path
        </h2>

        <div class="section-description">

            A suggested route through learning stages that
            match your predicted performance and the resources
            available for your academic area.

        </div>


        <div class="path-stage-row">

            {path_html}

        </div>


        <div class="path-footer">

            <div class="path-info-icon">
                i
            </div>

            <div>

                Work through the suggested stages in order where
                appropriate. The stages shown are based on the
                resource difficulty considered suitable for your
                current predicted performance.

            </div>

        </div>

    </div>
    """
)


# ============================================================
# BUILD RESOURCE ROWS
# ============================================================

resource_rows_html = ""


for rank, (_, row) in enumerate(
    top_recommendations.iterrows(),
    start=1
):

    resource_name = html.escape(
        str(
            row[
                "Resource_Name"
            ]
        )
    )

    provider = html.escape(
        str(
            row[
                "Provider"
            ]
        )
    )

    description = html.escape(
        str(
            row[
                "Description"
            ]
        )
    )

    skill = html.escape(
        str(
            row[
                "Supports_Skill"
            ]
        )
    )

    difficulty = html.escape(
        str(
            row[
                "Difficulty_Level"
            ]
        )
    )

    resource_type = html.escape(
        str(
            row[
                "Resource_Type"
            ]
        )
    )

    match_score = float(
        row[
            "Match_Score"
        ]
    )

    resource_url = html.escape(
        str(
            row[
                "URL"
            ]
        ),
        quote=True
    )


    resource_rows_html += f"""
    <div class="resource-row">

        <div class="resource-name-wrap">

            <div class="resource-icon">
                {rank}
            </div>

            <div>

                <div class="resource-name">
                    {resource_name}
                </div>

                <div class="resource-provider">
                    {provider}
                </div>

            </div>

        </div>


        <div>

            <div class="match-badge">
                {match_score:.1f}% Match
            </div>

        </div>


        <div>

            <div class="resource-reason">
                {description}
            </div>

            <div class="resource-meta">

                {skill}
                ·
                {difficulty}
                ·
                {resource_type}

            </div>

        </div>


        <div>

            <a
                class="resource-link"
                href="{resource_url}"
                target="_blank"
                rel="noopener noreferrer"
            >
                ›
            </a>

        </div>

    </div>
    """


# ============================================================
# PRIORITY INFORMATION
# ============================================================

if priority_skills:

    if len(
        priority_skills
    ) == 1:

        priority_name = (
            priority_skills[0]
        )

        priority_description = (
            "This is currently your lowest-confidence "
            "skill area."
        )

    else:

        priority_name = (
            ", ".join(
                priority_skills
            )
        )

        priority_description = (
            "These areas currently have your lowest "
            "confidence ratings."
        )

else:

    priority_name = (
        "No major low-confidence area"
    )

    priority_description = (
        "Your confidence ratings do not currently show "
        "a major low-confidence area."
    )


# ============================================================
# DIFFICULTY INFORMATION
# ============================================================

if preferred_difficulties:

    difficulty_focus = ", ".join(
        preferred_difficulties
    )

else:

    difficulty_focus = (
        "Balanced"
    )


# ============================================================
# INTEREST INFORMATION
# ============================================================

if interests:

    interest_focus = ", ".join(
        interests[:2]
    )

else:

    interest_focus = (
        "No topics selected"
    )


# ============================================================
# MAIN RECOMMENDATION GRID
# ============================================================

st.html(
    f"""
    <div class="recommendation-grid">


        <div class="recommendation-card resources-panel">

            <div class="resources-header">

                <h2 class="section-heading">
                    Recommended Resources
                </h2>

                <div class="section-description">
                    Your five highest-ranked learning resources.
                </div>

            </div>


            <div class="resource-list">

                <div class="resource-table-head">

                    <div>
                        Resource
                    </div>

                    <div>
                        Profile Match
                    </div>

                    <div>
                        Why it is relevant
                    </div>

                    <div></div>

                </div>

                {resource_rows_html}

            </div>


            <div class="resource-footer">

                <div class="resource-footer-icon">
                    i
                </div>

                <div class="resource-footer-text">

                    Resources are selected from your academic area
                    and ranked based on the skills you may need
                    support with, your interests, how well each
                    resource matches your profile, and a suitable
                    difficulty level.

                </div>

            </div>

        </div>


        <div class="side-stack">


            <div class="recommendation-card focus-panel">

                <h2 class="section-heading">
                    Focus Areas
                </h2>

                <div class="section-description">
                    What your recommendations are currently based on.
                </div>


                <div class="focus-item">

                    <div class="focus-icon green">
                        ↗
                    </div>

                    <div class="focus-content">

                        <div class="focus-name">
                            {html.escape(priority_name)}
                        </div>

                        <div class="focus-description">
                            {html.escape(priority_description)}
                        </div>

                    </div>

                    <div class="focus-priority priority-high">
                        Support Area
                    </div>

                </div>


                <div class="focus-item">

                    <div class="focus-icon orange">
                        ◷
                    </div>

                    <div class="focus-content">

                        <div class="focus-name">
                            {html.escape(difficulty_focus)}
                        </div>

                        <div class="focus-description">

                            Resource difficulty considered suitable
                            for your predicted performance.

                        </div>

                    </div>

                    <div class="focus-priority priority-medium">
                        Difficulty
                    </div>

                </div>


                <div class="focus-item">

                    <div class="focus-icon purple">
                        ♡
                    </div>

                    <div class="focus-content">

                        <div class="focus-name">
                            {html.escape(interest_focus)}
                        </div>

                        <div class="focus-description">

                            Your selected interests help personalise
                            the resources shown to you.

                        </div>

                    </div>

                    <div class="focus-priority priority-low">
                        Interests
                    </div>

                </div>

            </div>


            <div class="recommendation-card goal-panel">

                <h2 class="section-heading">
                    Your Academic Goal
                </h2>

                <div class="section-description">

                    Your main academic goal is also considered
                    when personalising your recommendations.

                </div>


                <div class="goal-content">

                    <div class="goal-icon">
                        ◎
                    </div>

                    <div>

                        <div class="goal-name">
                            {html.escape(str(academic_goal))}
                        </div>

                        <div class="goal-description">

                            Your academic goal helps the system
                            identify resources that are more relevant
                            to what you want to achieve.

                        </div>

                    </div>

                </div>

            </div>

        </div>

    </div>
    """
)


# ============================================================
# RECOMMENDATION EXPLANATION
# ============================================================

if priority_skills:

    priority_message = (
        "Your current priority area(s) are "
        f"{', '.join(priority_skills)}."
    )

else:

    priority_message = (
        "No major low-confidence area was identified."
    )


difficulty_message = (
    ", ".join(
        preferred_difficulties
    )
    if preferred_difficulties
    else "balanced"
)


# ============================================================
# RECOMMENDATION NOTE
# ============================================================

st.html(
    f"""
    <div class="method-note">

        <div class="method-icon">
            i
        </div>

        <div>

            <div class="method-title">
                About these recommendations
            </div>

            <div class="method-text">

                {html.escape(priority_message)}
                Based on your predicted performance, the system
                currently gives more preference to
                <b>{html.escape(difficulty_message)}</b>
                resources where appropriate.

                Profile Match shows how closely each resource fits
                your current profile. It considers your confidence
                ratings, interests, academic goal, predicted
                performance and suitable difficulty level.

                Profile Match is a matching and ranking score.
                It does not mean there is a
                particular probability that a resource will improve
                your academic performance.

            </div>

        </div>

    </div>
    """
)


# ============================================================
# NAVIGATION
# ============================================================

nav_space, update_col, insights_col = st.columns(
    [4.8, 1.9, 1.75],
    gap="small"
)


with update_col:

    if st.button(
        "← Update Academic Information",
        use_container_width=True,
        key="update_academic"
    ):

        st.switch_page(
            "pages/1_Academic_Information.py"
        )


with insights_col:

    if st.button(
        "View Academic Insights →",
        type="primary",
        use_container_width=True,
        key="view_insights"
    ):

        st.switch_page(
            "pages/4_Academic_Insights.py"
        )


# ============================================================
# FOOTER
# ============================================================

st.html("""
<div class="page-footer">
    © 2026 All rights reserved.
</div>
""")