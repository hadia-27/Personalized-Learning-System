import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ============================================================
# RECOMMENDATION WEIGHTS
# ============================================================

SKILL_WEIGHT = 0.35
INTEREST_WEIGHT = 0.25
SIMILARITY_WEIGHT = 0.25
DIFFICULTY_WEIGHT = 0.15


# ============================================================
# MAIN RECOMMENDATION FUNCTION
# ============================================================

def recommend_resources(
    resources_df,
    academic_area,
    confidence_scores,
    interests,
    academic_goal,
    pass_probability,
    top_n=5
):

    # ========================================================
    # 0. NORMALISE INPUT VALUES
    # ========================================================

    confidence_scores = {
        skill: int(score)
        for skill, score in confidence_scores.items()
    }

    pass_probability = float(pass_probability)

    interests = list(interests) if interests else []


    # ========================================================
    # 1. FILTER BY ACADEMIC AREA
    # ========================================================

    candidates = resources_df[
        resources_df["Academic_Area"] == academic_area
    ].copy()

    if candidates.empty:

        return {
            "priority_skill": None,
            "priority_skills": [],
            "preferred_difficulties": [],
            "top_recommendations": pd.DataFrame(),
            "learning_path": pd.DataFrame()
        }


    # ========================================================
    # 2. IDENTIFY LOWEST-CONFIDENCE AREA(S)
    # ========================================================

    minimum_confidence = min(
        confidence_scores.values()
    )

    lowest_confidence_skills = [
        skill
        for skill, score in confidence_scores.items()
        if score == minimum_confidence
    ]


    # --------------------------------------------------------
    # Priority-area interpretation
    #
    # 1–3/5:
    # Lowest-confidence skill(s) are development priorities.
    #
    # 4–5/5:
    # No major low-confidence area is identified.
    # --------------------------------------------------------

    if minimum_confidence <= 3:

        priority_skills = lowest_confidence_skills

        if len(priority_skills) == 1:

            priority_skill = priority_skills[0]

        else:

            priority_skill = ", ".join(
                priority_skills
            )

    else:

        priority_skills = []

        priority_skill = (
            "No major low-confidence area identified"
        )


    # ========================================================
    # 3. CONFIDENCE-BASED SKILL NEED SCORE
    # ========================================================

    def calculate_skill_need(supported_skill):

        confidence = confidence_scores.get(
            supported_skill,
            3
        )

        # Convert confidence 1–5 into development need 1–0:
        #
        # 1/5 -> 1.00
        # 2/5 -> 0.75
        # 3/5 -> 0.50
        # 4/5 -> 0.25
        # 5/5 -> 0.00

        skill_need = (
            5 - confidence
        ) / 4

        return float(skill_need)


    candidates["Skill_Need_Score"] = (
        candidates["Supports_Skill"]
        .apply(calculate_skill_need)
    )


    # ========================================================
    # 4. INTEREST MATCHING
    # ========================================================

    interests_lower = [
        str(interest).lower()
        for interest in interests
    ]


    def calculate_interest_matches(row):

        resource_text = (
            str(row["Primary_Topic"])
            + " "
            + str(row["Related_Topics"])
        ).lower()

        matches = sum(
            interest in resource_text
            for interest in interests_lower
        )

        return matches


    candidates["Interest_Matches"] = (
        candidates.apply(
            calculate_interest_matches,
            axis=1
        )
    )


    if len(interests) > 0:

        candidates["Interest_Score"] = (
            candidates["Interest_Matches"]
            / len(interests)
        )

    else:

        candidates["Interest_Score"] = 0.0


    # ========================================================
    # 5. PREDICTION-INFORMED DIFFICULTY
    # ========================================================

    if pass_probability < 50:

        preferred_difficulties = [
            "Beginner"
        ]

    elif pass_probability <= 75:

        preferred_difficulties = [
            "Beginner",
            "Intermediate"
        ]

    else:

        preferred_difficulties = [
            "Intermediate",
            "Advanced"
        ]


    candidates["Difficulty_Score"] = (
        candidates["Difficulty_Level"]
        .apply(
            lambda difficulty:
            1.0
            if difficulty in preferred_difficulties
            else 0.0
        )
    )


    # ========================================================
    # 6. BUILD RESOURCE TEXT
    # ========================================================

    candidates["Combined_Text"] = (

        candidates["Academic_Area"].astype(str)
        + " "
        + candidates["Primary_Topic"].astype(str)
        + " "
        + candidates["Related_Topics"].astype(str)
        + " "
        + candidates["Supports_Skill"].astype(str)
        + " "
        + candidates["Difficulty_Level"].astype(str)
        + " "
        + candidates["Description"].astype(str)

    )


    # ========================================================
    # 7. BUILD STUDENT SIMILARITY PROFILE
    # ========================================================

    student_profile_components = [
        str(academic_area)
    ]


    # Only genuine development-priority skills are added.
    #
    # Example:
    # 2,2,4 -> add the two weak skills
    # 4,4,4 -> do not add the skills as weaknesses

    if priority_skills:

        student_profile_components.append(
            " ".join(priority_skills)
        )


    if interests:

        student_profile_components.append(
            " ".join(
                str(interest)
                for interest in interests
            )
        )


    if academic_goal:

        student_profile_components.append(
            str(academic_goal)
        )


    student_text = " ".join(
        student_profile_components
    )


    # ========================================================
    # 8. TF-IDF + COSINE SIMILARITY
    # ========================================================

    documents = (
        [student_text]
        + candidates["Combined_Text"].tolist()
    )


    tfidf = TfidfVectorizer(
        stop_words="english"
    )


    tfidf_matrix = tfidf.fit_transform(
        documents
    )


    student_vector = tfidf_matrix[0]

    resource_vectors = tfidf_matrix[1:]


    similarity_scores = cosine_similarity(
        student_vector,
        resource_vectors
    )[0]


    candidates["Similarity_Score"] = (
        similarity_scores
    )


    # ========================================================
    # 9. FINAL WEIGHTED RECOMMENDATION SCORE
    # ========================================================

    candidates["Recommendation_Score"] = (

        candidates["Skill_Need_Score"]
        * SKILL_WEIGHT

        +

        candidates["Interest_Score"]
        * INTEREST_WEIGHT

        +

        candidates["Similarity_Score"]
        * SIMILARITY_WEIGHT

        +

        candidates["Difficulty_Score"]
        * DIFFICULTY_WEIGHT
    )


    # --------------------------------------------------------
    # Convert recommendation score to percentage
    # --------------------------------------------------------

    candidates["Match_Score"] = (
        candidates["Recommendation_Score"]
        * 100
    ).round(1)


    # ========================================================
    # 10. RANK RESOURCES
    # ========================================================

    ranked = (
        candidates
        .sort_values(
            by="Recommendation_Score",
            ascending=False
        )
        .copy()
    )

    # ========================================================
    # 11. LEARNING PATH
    # ========================================================

    difficulty_to_stage = {
        "Beginner": "Foundations",
        "Intermediate": "Core Skills",
        "Advanced": "Advanced Topics"
    }

    ranked["Learning_Path_Stage"] = (
        ranked["Difficulty_Level"]
        .map(difficulty_to_stage)
    )

    stage_order = {
        "Foundations": 1,
        "Core Skills": 2,
        "Advanced Topics": 3
    }

    ranked["Stage_Order"] = (
        ranked["Learning_Path_Stage"]
        .map(stage_order)
    )

    # --------------------------------------------------------
    # Only include resources from prediction-appropriate
    # difficulty levels in the suggested learning path.
    #
    # < 50%    -> Beginner only
    # 50–75%   -> Beginner + Intermediate
    # > 75%    -> Intermediate + Advanced
    # --------------------------------------------------------

    pathway = (
        ranked[
            ranked["Difficulty_Level"].isin(
                preferred_difficulties
            )
        ]
        .sort_values(
            by=[
                "Stage_Order",
                "Recommendation_Score"
            ],
            ascending=[
                True,
                False
            ]
        )
        .copy()
    )


    # Keep up to two resources from each available stage

    pathway = (
        pathway
        .groupby(
            "Learning_Path_Stage",
            sort=False,
            group_keys=False
        )
        .head(2)
        .copy()
    )

    # ========================================================
    # 12. RETURN RESULTS
    # ========================================================

    return {

        "priority_skill":
            priority_skill,

        "priority_skills":
            priority_skills,

        "preferred_difficulties":
            preferred_difficulties,

        "top_recommendations":
            ranked.head(top_n),

        "learning_path":
            pathway
    }