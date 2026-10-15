import streamlit as st
import pandas as pd
import html

from pathlib import Path
from io import BytesIO

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import (
    getSampleStyleSheet,
    ParagraphStyle
)
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak
)


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Academic Insights",
    page_icon="💡",
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

FACTOR_PATH = (
    BASE_DIR
    / "models"
    / "model_factor_importance.csv"
)


# ============================================================
# REQUIRED SESSION DATA
# ============================================================

required_keys = [
    "prediction",
    "pass_probability",
    "fail_probability",
    "academic_area",
    "study_hours",
    "attendance",
    "past_exam_score",
    "confidence_scores",
    "interests",
    "academic_goal",
    "priority_skill",
    "recommendations",
    "learning_path"
]


missing_keys = [
    key
    for key in required_keys
    if key not in st.session_state
]


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

.insights-header-row {
    width: 100%;

    display: flex;

    align-items: flex-start;

    justify-content: space-between;

    gap: 1rem;

    margin-bottom: 0.55rem;
}

.insights-title {
    margin: 0;

    color: #102347;

    font-size: 1.55rem;

    line-height: 1.05;

    font-weight: 820;
}

.insights-subtitle {
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
   DISABLED DOWNLOAD
========================================================== */

.download-disabled {
    min-width: 145px;

    min-height: 2.1rem;

    display: flex;

    align-items: center;

    justify-content: center;

    padding:
        0.42rem
        0.7rem;

    background: #edf0f5;

    border:
        1px solid
        #e4e8ef;

    border-radius: 6px;

    color: #a7b0bd;

    font-size: 0.56rem;

    font-weight: 650;
}


/* ==========================================================
   DOWNLOAD BUTTON
========================================================== */

.st-key-download_report button {
    min-height: 2.25rem !important;
    height: 2.25rem !important;

    padding:
        0.4rem
        0.85rem !important;

    background:
        linear-gradient(
            135deg,
            #1767e8,
            #0759d6
        ) !important;

    border:
        1px solid
        #1767e8 !important;

    border-radius: 6px !important;

    color: #ffffff !important;

    font-size: 0.6rem !important;

    font-weight: 700 !important;

    white-space: nowrap !important;

    box-shadow:
        0 4px 12px
        rgba(23,103,232,0.15) !important;
}

.st-key-download_report button * {
    color: #ffffff !important;

    -webkit-text-fill-color:
        #ffffff !important;

    white-space: nowrap !important;

    font-size: 0.6rem !important;
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

    color: #1767e8;

    box-shadow:
        0 8px 24px
        rgba(
            65,
            111,
            185,
            0.07
        );
}

.insight-icon {
    position: relative;

    width: 43px;
    height: 43px;
}

.insight-circle {
    position: absolute;

    left: 2px;
    top: 2px;

    width: 27px;
    height: 27px;

    border:
        2px solid
        #1767e8;

    border-radius: 50%;
}

.insight-line-v {
    position: absolute;

    left: 15px;
    top: 2px;

    width: 2px;
    height: 14px;

    background: #1767e8;
}

.insight-line-h {
    position: absolute;

    left: 15px;
    top: 15px;

    width: 13px;
    height: 2px;

    background: #1767e8;

    transform:
        rotate(25deg);

    transform-origin: left;
}

.insight-bar {
    position: absolute;

    bottom: 4px;

    width: 5px;

    border:
        2px solid
        #1767e8;

    border-radius:
        2px
        2px
        0
        0;
}

.insight-bar-1 {
    right: 15px;
    height: 9px;
}

.insight-bar-2 {
    right: 8px;
    height: 14px;
}

.insight-bar-3 {
    right: 1px;
    height: 20px;
}

.empty-heading {
    margin: 0;

    color: #132646;

    font-size: 1.02rem;

    line-height: 1.2;

    font-weight: 800;
}

.empty-description {
    width: 100%;

    max-width: 510px;

    margin:
        0.55rem
        auto
        0
        auto;

    color: #667892;

    font-size: 0.63rem;

    line-height: 1.6;
}

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
   HOW ACADEMIC INSIGHTS WORKS
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
    min-width: 360px;

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
   GENERAL CARD
========================================================== */

.dashboard-card {
    width: 100%;

    background: #ffffff;

    border:
        1px solid
        #dde6f2;

    border-radius: 10px;

    box-shadow:
        0 2px 9px
        rgba(21,52,91,0.025);
}

.card-heading {
    margin: 0;

    color: #1e3555;

    font-size: 0.72rem;

    line-height: 1.25;

    font-weight: 780;
}

.card-description {
    margin-top: 0.12rem;

    color: #78869a;

    font-size: 0.49rem;

    line-height: 1.4;
}


/* ==========================================================
   OVERVIEW GRID
========================================================== */

.overview-grid {
    display: grid;

    grid-template-columns:
        1fr
        1fr
        1fr
        1.25fr;

    gap: 0.62rem;

    margin-bottom: 0.62rem;
}

.overview-card {
    min-height: 128px;

    padding:
        0.72rem
        0.75rem;

    display: flex;

    flex-direction: column;

    justify-content: space-between;
}

.overview-label {
    color: #718198;

    font-size: 0.5rem;

    font-weight: 620;
}

.overview-value {
    margin-top: 0.35rem;

    color: #183354;

    font-size: 1rem;

    line-height: 1.15;

    font-weight: 820;
}

.overview-value.green {
    color: #24975a;
}

.overview-value.orange {
    color: #d89117;
}

.overview-value.red {
    color: #d74949;
}

.overview-meta {
    margin-top: 0.12rem;

    color: #8995a5;

    font-size: 0.44rem;
}

.probability-mini {
    width: 100%;

    height: 6px;

    margin-top: 0.55rem;

    overflow: hidden;

    border-radius: 50px;

    background: #e8edf4;
}

.probability-mini-fill {
    height: 100%;

    border-radius: inherit;

    background:
        linear-gradient(
            90deg,
            #4dc47c,
            #34ad67
        );
}

.priority-list {
    margin-top: 0.45rem;
}

.priority-chip {
    display: inline-block;

    margin:
        0
        0.2rem
        0.2rem
        0;

    padding:
        0.22rem
        0.38rem;

    border-radius: 5px;

    background: #f2efff;

    border:
        1px solid
        #e5defe;

    color: #6753c7;

    font-size: 0.44rem;

    font-weight: 650;
}


/* ==========================================================
   MAIN TWO-COLUMN GRID
========================================================== */

.insights-grid {
    display: grid;

    grid-template-columns:
        1.15fr
        0.85fr;

    gap: 0.62rem;

    margin-bottom: 0.62rem;
}


/* ==========================================================
   CONFIDENCE PROFILE
========================================================== */

.confidence-card {
    padding:
        0.75rem
        0.8rem;
}

.confidence-list {
    margin-top: 0.65rem;
}

.confidence-row {
    margin-bottom: 0.65rem;
}

.confidence-row:last-child {
    margin-bottom: 0;
}

.confidence-label-row {
    display: flex;

    justify-content: space-between;

    align-items: center;

    margin-bottom: 0.22rem;
}

.confidence-label {
    color: #344b69;

    font-size: 0.53rem;

    font-weight: 650;
}

.confidence-value {
    color: #25456f;

    font-size: 0.51rem;

    font-weight: 720;
}

.confidence-track {
    width: 100%;

    height: 7px;

    overflow: hidden;

    border-radius: 30px;

    background: #ebeff5;
}

.confidence-fill {
    height: 100%;

    border-radius: inherit;

    background:
        linear-gradient(
            90deg,
            #7263e5,
            #8c72ed
        );
}


/* ==========================================================
   PREDICTION FACTORS
========================================================== */

.factor-card {
    padding:
        0.75rem
        0.8rem;
}

.factor-list {
    margin-top: 0.65rem;
}

.factor-row {
    margin-bottom: 0.65rem;
}

.factor-row:last-child {
    margin-bottom: 0;
}

.factor-top {
    display: flex;

    justify-content: space-between;

    gap: 0.5rem;

    margin-bottom: 0.22rem;
}

.factor-name {
    color: #344b69;

    font-size: 0.52rem;

    font-weight: 650;
}

.factor-number {
    color: #218e57;

    font-size: 0.5rem;

    font-weight: 730;
}

.factor-track {
    height: 7px;

    overflow: hidden;

    border-radius: 40px;

    background: #ebeff5;
}

.factor-fill {
    height: 100%;

    border-radius: inherit;

    background:
        linear-gradient(
            90deg,
            #53c17a,
            #36a967
        );
}


/* ==========================================================
   SECONDARY GRID
========================================================== */

.secondary-grid {
    display: grid;

    grid-template-columns:
        0.9fr
        1.15fr
        1fr;

    gap: 0.62rem;
}


/* ==========================================================
   PROFILE CARD
========================================================== */

.profile-card {
    padding:
        0.75rem
        0.8rem;
}

.profile-table {
    width: 100%;

    margin-top: 0.52rem;

    border-collapse: collapse;

    font-size: 0.48rem;
}

.profile-table tr {
    border-bottom:
        1px solid
        #edf1f5;
}

.profile-table tr:last-child {
    border-bottom: none;
}

.profile-table td {
    padding:
        0.32rem
        0.15rem;
}

.profile-name {
    color: #6c7b91;

    font-weight: 620;
}

.profile-value {
    color: #2c425f;

    text-align: right;

    font-weight: 660;
}


/* ==========================================================
   RECOMMENDATIONS
========================================================== */

.recommendations-card {
    padding:
        0.75rem
        0.8rem;
}

.recommendation-item {
    display: flex;

    align-items: center;

    gap: 0.48rem;

    min-height: 49px;

    padding:
        0.35rem
        0;

    border-bottom:
        1px solid
        #edf1f5;
}

.recommendation-item:last-child {
    border-bottom: none;
}

.rec-number {
    width: 25px;
    height: 25px;

    min-width: 25px;

    display: flex;

    align-items: center;

    justify-content: center;

    border-radius: 6px;

    background: #eaf7ef;

    color: #249d5d;

    font-size: 0.5rem;

    font-weight: 800;
}

.rec-main {
    flex: 1;

    min-width: 0;
}

.rec-name {
    color: #2b405c;

    font-size: 0.5rem;

    line-height: 1.3;

    font-weight: 680;
}

.rec-meta {
    margin-top: 0.07rem;

    color: #8995a5;

    font-size: 0.42rem;
}

.rec-score {
    padding:
        0.2rem
        0.32rem;

    border-radius: 999px;

    background: #eaf8ef;

    color: #288f59;

    font-size: 0.4rem;

    font-weight: 720;

    white-space: nowrap;
}


/* ==========================================================
   LEARNING PATH
========================================================== */

.path-card {
    padding:
        0.75rem
        0.8rem;
}

.path-list {
    margin-top: 0.58rem;
}

.path-item {
    display: flex;

    align-items: center;

    gap: 0.45rem;

    margin-bottom: 0.5rem;
}

.path-item:last-child {
    margin-bottom: 0;
}

.path-number {
    width: 27px;
    height: 27px;

    min-width: 27px;

    display: flex;

    align-items: center;

    justify-content: center;

    border-radius: 50%;

    color: #ffffff;

    font-size: 0.48rem;

    font-weight: 800;
}

.path-green {
    background: #2db776;
}

.path-blue {
    background: #3177ed;
}

.path-orange {
    background: #f0a020;
}

.path-name {
    color: #304661;

    font-size: 0.51rem;

    font-weight: 690;
}

.path-meta {
    margin-top: 0.05rem;

    color: #8592a4;

    font-size: 0.42rem;
}


/* ==========================================================
   INTERPRETATION
========================================================== */

.interpretation-card {
    width: 100%;

    display: flex;

    align-items: flex-start;

    gap: 0.65rem;

    margin-top: 0.62rem;

    padding:
        0.68rem
        0.8rem;

    background:
        linear-gradient(
            135deg,
            #f1f6ff,
            #eef4ff
        );

    border:
        1px solid
        #dce8f8;

    border-radius: 8px;
}

.interpretation-icon {
    width: 25px;
    height: 25px;

    min-width: 25px;

    display: flex;

    align-items: center;

    justify-content: center;

    border:
        1.4px solid
        #377fe8;

    border-radius: 50%;

    color: #2671de;

    font-size: 0.52rem;

    font-weight: 800;
}

.interpretation-title {
    color: #294263;

    font-size: 0.54rem;

    font-weight: 760;
}

.interpretation-text {
    margin-top: 0.1rem;

    color: #637690;

    font-size: 0.47rem;

    line-height: 1.45;
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

.st-key-back_recommendations button {
    background: #ffffff !important;

    border:
        1px solid
        #8eb5ec !important;

    color: #1767e8 !important;

    box-shadow: none !important;

    white-space: nowrap !important;
}

.st-key-back_recommendations button * {
    color: #1767e8 !important;

    -webkit-text-fill-color:
        #1767e8 !important;

    white-space: nowrap !important;

    font-size: 0.61rem !important;
}

.st-key-update_information button {
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

.st-key-update_information button * {
    color: #ffffff !important;

    -webkit-text-fill-color:
        #ffffff !important;

    white-space: nowrap !important;

    font-size: 0.61rem !important;
}


/* ==========================================================
   FOOTER
========================================================== */

.page-footer {
    min-height: 1.2rem;

    display: flex;

    align-items: center;

    color: #8b97aa;

    font-size: 0.51rem;
}


/* ==========================================================
   RESPONSIVE
========================================================== */

@media (max-width: 1050px) {

    .overview-grid {
        grid-template-columns:
            1fr
            1fr;
    }

    .insights-grid,
    .secondary-grid {
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


@media (max-width: 768px) {

    .block-container {
        padding:
            0.65rem
            0.7rem !important;
    }

    .overview-grid {
        grid-template-columns: 1fr;
    }

    .insights-title {
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
# EMPTY STATE
# ============================================================

if missing_keys:

    st.html("""
    <div class="insights-header-row">

        <div>

            <h1 class="insights-title">
                Academic Insights
            </h1>

            <p class="insights-subtitle">

                Explore a summary of your academic profile,
                prediction and recommendations.

            </p>

        </div>

        <div class="download-disabled">
            ↓&nbsp;&nbsp;Download Report
        </div>

    </div>
    """)


    st.html("""
    <div class="empty-card">

        <div class="empty-icon-wrap">

            <div class="insight-icon">

                <div class="insight-circle"></div>

                <div class="insight-line-v"></div>

                <div class="insight-line-h"></div>

                <div class="insight-bar insight-bar-1"></div>

                <div class="insight-bar insight-bar-2"></div>

                <div class="insight-bar insight-bar-3"></div>

            </div>

        </div>


        <h2 class="empty-heading">
            No Insights Available Yet
        </h2>


        <div class="empty-description">

            Complete your Academic Information and generate a
            performance prediction first. Once your prediction
            and recommendations are available, your combined
            academic insights will appear here.

        </div>

    </div>
    """)


    st.html("""
    <div class="empty-button-spacer"></div>
    """)


    left_space, button_col, right_space = st.columns(
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
                How your academic insights are generated
            </div>

            <div class="how-text">

                Complete your academic information first.
                Once your prediction and recommendations are
                available, this page combines your academic
                profile, predicted performance, confidence
                ratings and personalised recommendations into
                one academic summary.

            </div>

        </div>


        <div class="how-inputs">

            <div class="how-pill">
                Prediction
            </div>

            <div class="how-pill">
                Confidence
            </div>

            <div class="how-pill">
                Focus Areas
            </div>

            <div class="how-pill">
                Recommendations
            </div>

        </div>

    </div>
    """)

    st.stop()


# ============================================================
# RETRIEVE SESSION DATA
# ============================================================

prediction = st.session_state[
    "prediction"
]

pass_probability = float(
    st.session_state[
        "pass_probability"
    ]
)

fail_probability = float(
    st.session_state[
        "fail_probability"
    ]
)

academic_area = st.session_state[
    "academic_area"
]

study_hours = st.session_state[
    "study_hours"
]

attendance = float(
    st.session_state[
        "attendance"
    ]
)

past_exam_score = st.session_state[
    "past_exam_score"
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

priority_skill = st.session_state[
    "priority_skill"
]

priority_skills = st.session_state.get(
    "priority_skills",
    []
)

recommendations = st.session_state[
    "recommendations"
]

learning_path = st.session_state[
    "learning_path"
]


# ============================================================
# CONFIDENCE INTERPRETATION
# ============================================================

minimum_confidence = min(
    confidence_scores.values()
)

lowest_confidence_skills = [
    skill
    for skill, score in confidence_scores.items()
    if score == minimum_confidence
]

has_priority_area = (
    minimum_confidence <= 3
)


# ============================================================
# RISK INTERPRETATION
# ============================================================

if pass_probability >= 75:

    risk_level = "Low Risk"

    risk_class = "green"

    support_message = (
        "Your current profile indicates a relatively strong "
        "predicted academic outcome. Continue maintaining your "
        "academic habits while using your recommendations to "
        "strengthen relevant skills."
    )


elif pass_probability >= 50:

    risk_level = "Moderate Risk"

    risk_class = "orange"

    support_message = (
        "Your current profile indicates a moderate level of "
        "predicted academic risk. Maintaining consistent study "
        "habits and strengthening lower-confidence areas may "
        "provide useful additional support."
    )


else:

    risk_level = "High Risk"

    risk_class = "red"

    support_message = (
        "Your current profile indicates a higher level of "
        "predicted academic risk. Starting with learning resources "
        "that match your current level and focusing on weaker areas "
        "may provide useful additional support."
    )


# ============================================================
# LOAD PREDICTION FACTORS
# ============================================================

factor_df = None

if FACTOR_PATH.exists():

    factor_df = pd.read_csv(
        FACTOR_PATH
    )


# ============================================================
# PDF REPORT
# ============================================================

def generate_pdf_report():

    buffer = BytesIO()

    document = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "ReportTitle",
        parent=styles["Title"],
        fontSize=20,
        alignment=TA_CENTER,
        spaceAfter=20
    )

    heading_style = ParagraphStyle(
        "SectionHeading",
        parent=styles["Heading2"],
        fontSize=14,
        spaceBefore=14,
        spaceAfter=8
    )

    subheading_style = ParagraphStyle(
        "SubHeading",
        parent=styles["Heading3"],
        fontSize=11,
        spaceBefore=8,
        spaceAfter=5
    )

    normal_style = ParagraphStyle(
        "NormalText",
        parent=styles["BodyText"],
        fontSize=9,
        leading=13
    )

    story = []


    # --------------------------------------------------------
    # TITLE
    # --------------------------------------------------------

    story.append(
        Paragraph(
            "Personalised Academic Support Report",
            title_style
        )
    )

    story.append(
        Paragraph(
            "This report summarises the student's academic "
            "profile, predicted academic outcome, personalised "
            "recommendations and suggested learning pathway.",
            normal_style
        )
    )

    story.append(
        Spacer(
            1,
            18
        )
    )


    # --------------------------------------------------------
    # ACADEMIC PROFILE
    # --------------------------------------------------------

    story.append(
        Paragraph(
            "1. Academic Profile",
            heading_style
        )
    )

    profile_data = [
        [
            "Academic Area",
            Paragraph(
                str(academic_area),
                normal_style
            )
        ],
        [
            "Study Hours per Week",
            str(study_hours)
        ],
        [
            "Attendance Rate",
            f"{attendance:.1f}%"
        ],
        [
            "Past Exam Score",
            str(past_exam_score)
        ],
        [
            "Academic Goal",
            Paragraph(
                str(academic_goal),
                normal_style
            )
        ],
        [
            "Topics of Interest",
            Paragraph(
                ", ".join(interests),
                normal_style
            )
        ]
    ]

    profile_table = Table(
        profile_data,
        colWidths=[
            160,
            340
        ]
    )

    profile_table.setStyle(
        TableStyle([
            (
                "BACKGROUND",
                (0, 0),
                (0, -1),
                colors.HexColor("#E9EEF8")
            ),
            (
                "FONTNAME",
                (0, 0),
                (0, -1),
                "Helvetica-Bold"
            ),
            (
                "GRID",
                (0, 0),
                (-1, -1),
                0.5,
                colors.grey
            ),
            (
                "VALIGN",
                (0, 0),
                (-1, -1),
                "TOP"
            ),
            (
                "PADDING",
                (0, 0),
                (-1, -1),
                7
            )
        ])
    )

    story.append(
        profile_table
    )

    story.append(
        Spacer(
            1,
            16
        )
    )


    # --------------------------------------------------------
    # CONFIDENCE PROFILE
    # --------------------------------------------------------

    story.append(
        Paragraph(
            "2. Confidence in Key Areas",
            heading_style
        )
    )

    confidence_data = [
        [
            "Skill",
            "Confidence"
        ]
    ]

    for skill, score in confidence_scores.items():

        confidence_data.append([
            Paragraph(
                str(skill),
                normal_style
            ),
            f"{score}/5"
        ])

    confidence_table = Table(
        confidence_data,
        colWidths=[
            350,
            150
        ]
    )

    confidence_table.setStyle(
        TableStyle([
            (
                "BACKGROUND",
                (0, 0),
                (-1, 0),
                colors.HexColor("#DDE6F8")
            ),
            (
                "FONTNAME",
                (0, 0),
                (-1, 0),
                "Helvetica-Bold"
            ),
            (
                "GRID",
                (0, 0),
                (-1, -1),
                0.5,
                colors.grey
            ),
            (
                "VALIGN",
                (0, 0),
                (-1, -1),
                "TOP"
            ),
            (
                "PADDING",
                (0, 0),
                (-1, -1),
                7
            )
        ])
    )

    story.append(
        confidence_table
    )

    story.append(
        Spacer(
            1,
            16
        )
    )


    # --------------------------------------------------------
    # PREDICTION
    # --------------------------------------------------------

    story.append(
        Paragraph(
            "3. Prediction Results",
            heading_style
        )
    )

    prediction_data = [
        [
            "Predicted Outcome",
            prediction
        ],
        [
            "Pass Probability",
            f"{pass_probability:.2f}%"
        ],
        [
            "Fail Probability",
            f"{fail_probability:.2f}%"
        ],
        [
            "Risk Level",
            risk_level
        ]
    ]

    prediction_table = Table(
        prediction_data,
        colWidths=[
            200,
            300
        ]
    )

    prediction_table.setStyle(
        TableStyle([
            (
                "BACKGROUND",
                (0, 0),
                (0, -1),
                colors.HexColor("#E9EEF8")
            ),
            (
                "FONTNAME",
                (0, 0),
                (0, -1),
                "Helvetica-Bold"
            ),
            (
                "GRID",
                (0, 0),
                (-1, -1),
                0.5,
                colors.grey
            ),
            (
                "PADDING",
                (0, 0),
                (-1, -1),
                7
            )
        ])
    )

    story.append(
        prediction_table
    )

    story.append(
        Spacer(
            1,
            8
        )
    )

    story.append(
        Paragraph(
            "The prediction is based on Study Hours per Week, "
            "Attendance Rate and Past Exam Score. The displayed "
            "Pass Probability is a model-based estimate and is "
            "not a guaranteed future result.",
            normal_style
        )
    )

    story.append(
        Spacer(
            1,
            16
        )
    )


    # --------------------------------------------------------
    # PREDICTION FACTORS
    # --------------------------------------------------------

    story.append(
        Paragraph(
            "4. Factors Influencing the Prediction",
            heading_style
        )
    )

    if factor_df is not None:

        if (
            "Feature" in factor_df.columns
            and "Relative_Importance" in factor_df.columns
        ):

            factor_data = [
                [
                    "Academic Factor",
                    "Relative Influence"
                ]
            ]

            friendly_names = {
                "Past_Exam_Scores":
                    "Past Exam Score",

                "Attendance_Rate":
                    "Attendance Rate",

                "Study_Hours_per_Week":
                    "Study Hours per Week"
            }

            for _, row in factor_df.iterrows():

                feature_name = friendly_names.get(
                    row["Feature"],
                    row["Feature"]
                )

                factor_data.append([
                    Paragraph(
                        str(feature_name),
                        normal_style
                    ),
                    f"{float(row['Relative_Importance']):.2f}%"
                ])

            factor_table = Table(
                factor_data,
                colWidths=[
                    350,
                    150
                ]
            )

            factor_table.setStyle(
                TableStyle([
                    (
                        "BACKGROUND",
                        (0, 0),
                        (-1, 0),
                        colors.HexColor("#DDE6F8")
                    ),
                    (
                        "FONTNAME",
                        (0, 0),
                        (-1, 0),
                        "Helvetica-Bold"
                    ),
                    (
                        "GRID",
                        (0, 0),
                        (-1, -1),
                        0.5,
                        colors.grey
                    ),
                    (
                        "PADDING",
                        (0, 0),
                        (-1, -1),
                        7
                    )
                ])
            )

            story.append(
                factor_table
            )

            story.append(
                Spacer(
                    1,
                    8
                )
            )

            story.append(
                Paragraph(
                    "These percentages show the relative influence "
                    "of each academic factor within the prediction "
                    "model. They are intended as an overall guide "
                    "and do not represent exact individual effects "
                    "or prove that one factor directly causes the "
                    "predicted outcome.",
                    normal_style
                )
            )

    story.append(
        Spacer(
            1,
            16
        )
    )


    # --------------------------------------------------------
    # RECOMMENDATIONS
    # --------------------------------------------------------

    story.append(
        Paragraph(
            "5. Personalised Recommendations",
            heading_style
        )
    )

    if has_priority_area:

        story.append(
            Paragraph(
                f"Current priority area(s): "
                f"<b>{priority_skill}</b>",
                normal_style
            )
        )

    else:

        story.append(
            Paragraph(
                "<b>No major low-confidence area was identified.</b>",
                normal_style
            )
        )

    story.append(
        Spacer(
            1,
            8
        )
    )

    recommendation_data = [
        [
            "Resource",
            "Skill",
            "Difficulty",
            "Profile Match"
        ]
    ]

    for _, row in recommendations.iterrows():

        recommendation_data.append([
            Paragraph(
                str(
                    row[
                        "Resource_Name"
                    ]
                ),
                normal_style
            ),
            Paragraph(
                str(
                    row[
                        "Supports_Skill"
                    ]
                ),
                normal_style
            ),
            row[
                "Difficulty_Level"
            ],
            f"{row['Match_Score']:.1f}%"
        ])

    recommendation_table = Table(
        recommendation_data,
        colWidths=[
            230,
            120,
            90,
            80
        ],
        repeatRows=1
    )

    recommendation_table.setStyle(
        TableStyle([
            (
                "BACKGROUND",
                (0, 0),
                (-1, 0),
                colors.HexColor("#DDE6F8")
            ),
            (
                "FONTNAME",
                (0, 0),
                (-1, 0),
                "Helvetica-Bold"
            ),
            (
                "GRID",
                (0, 0),
                (-1, -1),
                0.5,
                colors.grey
            ),
            (
                "VALIGN",
                (0, 0),
                (-1, -1),
                "TOP"
            ),
            (
                "PADDING",
                (0, 0),
                (-1, -1),
                6
            )
        ])
    )

    story.append(
        recommendation_table
    )

    story.append(
        PageBreak()
    )


    # --------------------------------------------------------
    # LEARNING PATH
    # --------------------------------------------------------

    story.append(
        Paragraph(
            "6. Suggested Learning Path",
            heading_style
        )
    )

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

    for stage_number, stage in enumerate(
        available_stages,
        start=1
    ):

        story.append(
            Paragraph(
                f"{stage_number}. {stage}",
                subheading_style
            )
        )

        stage_df = learning_path[
            learning_path[
                "Learning_Path_Stage"
            ] == stage
        ]

        for _, row in stage_df.iterrows():

            story.append(
                Paragraph(
                    f"<b>{row['Resource_Name']}</b> "
                    f"- {row['Difficulty_Level']} "
                    f"- Profile Match: "
                    f"{row['Match_Score']:.1f}%",
                    normal_style
                )
            )

            story.append(
                Spacer(
                    1,
                    4
                )
            )

        story.append(
            Spacer(
                1,
                8
            )
        )


    # --------------------------------------------------------
    # INTERPRETATION
    # --------------------------------------------------------

    story.append(
        Paragraph(
            "7. Academic Interpretation",
            heading_style
        )
    )

    story.append(
        Paragraph(
            support_message,
            normal_style
        )
    )

    story.append(
        Spacer(
            1,
            10
        )
    )

    if has_priority_area:

        story.append(
            Paragraph(
                f"The recommendation system identified "
                f"<b>{priority_skill}</b> as the current "
                f"priority area(s) based on the student's "
                f"confidence ratings.",
                normal_style
            )
        )

    else:

        story.append(
            Paragraph(
                "No major low-confidence area was identified "
                "from the student's self-reported confidence "
                "ratings. The recommendations therefore rely "
                "more on the student's interests, how closely "
                "each resource matches the overall profile and "
                "the difficulty level considered appropriate for "
                "the predicted performance.",
                normal_style
            )
        )

    story.append(
        Spacer(
            1,
            14
        )
    )

    story.append(
        Paragraph(
            "<b>Important:</b> This report is intended to "
            "support academic planning. The prediction is a "
            "model-based estimate and Profile Match is a "
            "ranking score showing how well a resource matches "
            "the student's profile. It is not a probability "
            "that the resource will improve academic performance. "
            "The system does not replace professional academic advice.",
            normal_style
        )
    )

    document.build(
        story
    )

    buffer.seek(0)

    return buffer.getvalue()


# ============================================================
# GENERATE PDF BEFORE HEADER
# ============================================================

pdf_report = generate_pdf_report()


# ============================================================
# PAGE HEADER + DOWNLOAD
# ============================================================

header_col, download_col = st.columns(
    [6.2, 1.25],
    gap="small"
)


with header_col:

    st.html("""
    <div>

        <h1 class="insights-title">
            Academic Insights
        </h1>

        <p class="insights-subtitle">

            Explore a combined summary of your academic profile,
            prediction and personalised learning recommendations.

        </p>

    </div>
    """)


with download_col:

    st.download_button(
        label="↓ Download Report",
        data=pdf_report,
        file_name="academic_support_report.pdf",
        mime="application/pdf",
        type="primary",
        use_container_width=True,
        key="download_report"
    )


# ============================================================
# BUILD PRIORITY DISPLAY
# ============================================================

if has_priority_area:

    priority_display = ", ".join(
        lowest_confidence_skills
    )

else:

    priority_display = (
        "No major low-confidence area"
    )


priority_chips = ""

if has_priority_area:

    for skill in lowest_confidence_skills:

        priority_chips += f"""
        <span class="priority-chip">
            {html.escape(str(skill))}
        </span>
        """

else:

    priority_chips = """
    <span class="priority-chip">
        Balanced confidence profile
    </span>
    """


# ============================================================
# OVERVIEW
# ============================================================

st.html(
    f"""
    <div class="overview-grid">


        <div class="dashboard-card overview-card">

            <div>

                <div class="overview-label">
                    Predicted Outcome
                </div>

                <div class="overview-value">
                    {html.escape(str(prediction))}
                </div>

            </div>

            <div class="overview-meta">
                Your current predicted result
            </div>

        </div>


        <div class="dashboard-card overview-card">

            <div>

                <div class="overview-label">
                    Pass Probability
                </div>

                <div class="overview-value green">
                    {pass_probability:.1f}%
                </div>

                <div class="probability-mini">

                    <div
                        class="probability-mini-fill"
                        style="width:{pass_probability:.1f}%;"
                    ></div>

                </div>

            </div>

            <div class="overview-meta">
                Model-based predicted pass probability
            </div>

        </div>


        <div class="dashboard-card overview-card">

            <div>

                <div class="overview-label">
                    Risk Level
                </div>

                <div class="overview-value {risk_class}">
                    {risk_level}
                </div>

            </div>

            <div class="overview-meta">
                Based on your predicted pass probability
            </div>

        </div>


        <div class="dashboard-card overview-card">

            <div>

                <div class="overview-label">
                    Priority Area
                </div>

                <div class="priority-list">
                    {priority_chips}
                </div>

            </div>

            <div class="overview-meta">
                Based on your confidence ratings
            </div>

        </div>


    </div>
    """
)


# ============================================================
# CONFIDENCE HTML
# ============================================================

confidence_html = ""

for skill, score in confidence_scores.items():

    width = max(
        0,
        min(
            100,
            (float(score) / 5) * 100
        )
    )

    confidence_html += f"""
    <div class="confidence-row">

        <div class="confidence-label-row">

            <span class="confidence-label">
                {html.escape(str(skill))}
            </span>

            <span class="confidence-value">
                {score}/5
            </span>

        </div>

        <div class="confidence-track">

            <div
                class="confidence-fill"
                style="width:{width:.1f}%;"
            ></div>

        </div>

    </div>
    """


# ============================================================
# PREDICTION FACTOR HTML
# ============================================================

factor_html = ""

friendly_names = {
    "Past_Exam_Scores":
        "Past Exam Score",

    "Attendance_Rate":
        "Attendance Rate",

    "Study_Hours_per_Week":
        "Study Hours per Week"
}


if (
    factor_df is not None
    and "Feature" in factor_df.columns
    and "Relative_Importance" in factor_df.columns
):

    max_factor = float(
        factor_df[
            "Relative_Importance"
        ].max()
    )

    for _, row in factor_df.iterrows():

        feature = friendly_names.get(
            row["Feature"],
            row["Feature"]
        )

        importance = float(
            row[
                "Relative_Importance"
            ]
        )

        if max_factor > 0:

            factor_width = (
                importance
                / max_factor
                * 100
            )

        else:

            factor_width = 0


        factor_html += f"""
        <div class="factor-row">

            <div class="factor-top">

                <span class="factor-name">
                    {html.escape(str(feature))}
                </span>

                <span class="factor-number">
                    {importance:.2f}%
                </span>

            </div>

            <div class="factor-track">

                <div
                    class="factor-fill"
                    style="width:{factor_width:.1f}%;"
                ></div>

            </div>

        </div>
        """

else:

    factor_html = """
    <div class="card-description">
        Prediction factor information is currently unavailable.
    </div>
    """


# ============================================================
# CONFIDENCE + PREDICTION FACTORS
# ============================================================

st.html(
    f"""
    <div class="insights-grid">


        <div class="dashboard-card confidence-card">

            <h2 class="card-heading">
                Confidence Profile
            </h2>

            <div class="card-description">

                Your confidence ratings across the key skills
                associated with your selected academic area.

            </div>


            <div class="confidence-list">

                {confidence_html}

            </div>

        </div>


        <div class="dashboard-card factor-card">

            <h2 class="card-heading">
                Factors Influencing the Prediction
            </h2>

            <div class="card-description">

                This shows the relative influence of each
                academic factor within the prediction model.

            </div>


            <div class="factor-list">

                {factor_html}

            </div>

        </div>


    </div>
    """
)


# ============================================================
# PROFILE TABLE HTML
# ============================================================

interests_text = (
    ", ".join(interests)
    if interests
    else "None selected"
)


profile_html = f"""
<table class="profile-table">

    <tr>

        <td class="profile-name">
            Academic Area
        </td>

        <td class="profile-value">
            {html.escape(str(academic_area))}
        </td>

    </tr>

    <tr>

        <td class="profile-name">
            Study Hours
        </td>

        <td class="profile-value">
            {study_hours} / week
        </td>

    </tr>

    <tr>

        <td class="profile-name">
            Attendance
        </td>

        <td class="profile-value">
            {attendance:.1f}%
        </td>

    </tr>

    <tr>

        <td class="profile-name">
            Past Exam Score
        </td>

        <td class="profile-value">
            {past_exam_score}
        </td>

    </tr>

    <tr>

        <td class="profile-name">
            Academic Goal
        </td>

        <td class="profile-value">
            {html.escape(str(academic_goal))}
        </td>

    </tr>

    <tr>

        <td class="profile-name">
            Interests
        </td>

        <td class="profile-value">
            {html.escape(interests_text)}
        </td>

    </tr>

</table>
"""


# ============================================================
# TOP RECOMMENDATIONS HTML
# ============================================================

recommendation_html = ""

top_three = recommendations.head(
    3
)


for rank, (_, row) in enumerate(
    top_three.iterrows(),
    start=1
):

    recommendation_html += f"""
    <div class="recommendation-item">

        <div class="rec-number">
            {rank}
        </div>

        <div class="rec-main">

            <div class="rec-name">
                {html.escape(str(row['Resource_Name']))}
            </div>

            <div class="rec-meta">

                {html.escape(str(row['Supports_Skill']))}
                ·
                {html.escape(str(row['Difficulty_Level']))}

            </div>

        </div>

        <div class="rec-score">
            {float(row['Match_Score']):.1f}% Match
        </div>

    </div>
    """


# ============================================================
# LEARNING PATH HTML
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


path_classes = {
    "Foundations": "path-green",
    "Core Skills": "path-blue",
    "Advanced Topics": "path-orange"
}


path_html = ""


for stage_number, stage in enumerate(
    available_stages,
    start=1
):

    stage_df = learning_path[
        learning_path[
            "Learning_Path_Stage"
        ] == stage
    ]

    resource_count = len(
        stage_df
    )

    path_html += f"""
    <div class="path-item">

        <div class="path-number {path_classes.get(stage, 'path-blue')}">
            {stage_number}
        </div>

        <div>

            <div class="path-name">
                {html.escape(str(stage))}
            </div>

            <div class="path-meta">
                {resource_count}
                recommended
                {"resource" if resource_count == 1 else "resources"}
            </div>

        </div>

    </div>
    """


# ============================================================
# SECONDARY GRID
# ============================================================

st.html(
    f"""
    <div class="secondary-grid">


        <div class="dashboard-card profile-card">

            <h2 class="card-heading">
                Student Profile
            </h2>

            <div class="card-description">
                Information used across the application.
            </div>

            {profile_html}

        </div>


        <div class="dashboard-card recommendations-card">

            <h2 class="card-heading">
                Top Learning Recommendations
            </h2>

            <div class="card-description">

                Your three highest-ranked personalised
                learning resources.

            </div>

            <div>
                {recommendation_html}
            </div>

        </div>


        <div class="dashboard-card path-card">

            <h2 class="card-heading">
                Learning Path Overview
            </h2>

            <div class="card-description">

                Your recommended resources organised into
                learning stages appropriate to your predicted
                performance.

            </div>

            <div class="path-list">
                {path_html}
            </div>

        </div>


    </div>
    """
)


# ============================================================
# OVERALL INTERPRETATION
# ============================================================

if has_priority_area:

    confidence_interpretation = (
        f"Your current priority area(s) are "
        f"{', '.join(lowest_confidence_skills)}. "
        f"These areas are considered when selecting and "
        f"ranking relevant learning resources."
    )

else:

    confidence_interpretation = (
        "Your confidence ratings do not indicate a major "
        "low-confidence area. Recommendations therefore rely "
        "more on your interests, how closely each resource "
        "matches your overall profile and the difficulty level "
        "considered appropriate for your predicted performance."
    )


st.html(
    f"""
    <div class="interpretation-card">

        <div class="interpretation-icon">
            i
        </div>

        <div>

            <div class="interpretation-title">
                What this means
            </div>

            <div class="interpretation-text">

                {html.escape(support_message)}

                {html.escape(confidence_interpretation)}

                Your performance prediction is based only on
                <b>Study Hours per Week, Attendance Rate and
                Past Exam Score</b>. Your confidence ratings,
                interests and academic goal are used separately
                to personalise your learning recommendations.

            </div>

        </div>

    </div>
    """
)


# ============================================================
# NAVIGATION
# ============================================================

nav_space, recommendations_col, update_col = st.columns(
    [4.4, 1.75, 1.95],
    gap="small"
)


with recommendations_col:

    if st.button(
        "← View Recommendations",
        use_container_width=True,
        key="back_recommendations"
    ):

        st.switch_page(
            "pages/3_Recommendations.py"
        )


with update_col:

    if st.button(
        "Update Academic Information →",
        type="primary",
        use_container_width=True,
        key="update_information"
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