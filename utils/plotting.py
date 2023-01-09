import seaborn as sns
import pandas as pd


def plot_question_distribution(question: str, data: pd.DataFrame, questions: pd.DataFrame):
    """plots histogram of polical orientation for a given question"""
    sns.catplot(
        data=data, y=question, hue='q212813', kind="count",
        palette="pastel", edgecolor=".6"
        ).set(title=questions.loc[question, 'text'])
