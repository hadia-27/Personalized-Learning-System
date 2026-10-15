import pandas as pd

from recommendation.recommender import recommend_resources


resources_df = pd.read_csv(
    "data/recommendation/learning_resources.csv"
)

result = recommend_resources(
    resources_df=resources_df,

    academic_area="Data Science & AI",

    confidence_scores={
        "Programming": 2,
        "Mathematics & Statistics": 4,
        "Data Analysis": 3
    },

    interests=[
        "Machine Learning",
        "Data Analysis"
    ],

    academic_goal="Improve academic performance",

    pass_probability=55.72
)


print("Priority skill:")
print(result["priority_skill"])

print("\nPreferred difficulties:")
print(result["preferred_difficulties"])

print("\nTop recommendations:")
print(
    result["top_recommendations"][
        [
            "Resource_Name",
            "Difficulty_Level",
            "Match_Score"
        ]
    ]
)