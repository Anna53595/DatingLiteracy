import pandas as pd
from pandas.api.types import CategoricalDtype


def top_k_questions(keyword: str, k: int, questions_df: pd.DataFrame, data: pd.DataFrame, print_q=True) -> list[str]:
    """Extracts k most answered question labels of a given question keyword"""
    n_answers_per_question = data.notnull().sum(axis=0)[1:] # first column is question name (Unnamed: 0) => [1:] #TODO: check this
    questions_df = questions_df.join(n_answers_per_question.to_frame('n_answers'))
    
    key_questions = questions_df[questions_df.Keywords == keyword]
    sorted_key_questions = key_questions.sort_values(by=['n_answers'], ascending=False)
    if print_q:
        print('selected questions: ', sorted_key_questions['text'][:k].values)
    return sorted_key_questions[:k] #TODO change back .index.to_list()

def get_categories(selected_questions: list[str], questions_df: pd.DataFrame, nonordinal_questions: set) -> tuple[dict, dict]:
    """extract unordered and ordered categories"""# TODO: können wir auch automatisch die nonordinalquestions erkennen?
    options = [column for column in questions_df.columns if 'option' in column]
    questions_categories = {index: row[options].dropna().tolist()
        for index, row in questions_df.loc[selected_questions].iterrows()}
    unordered_categories = {k: questions_categories[k]
        for k in questions_categories.keys() - nonordinal_questions}
    ordered_categories = {k: questions_categories[k]
        for k in questions_categories.keys() - unordered_categories.keys()}

    return unordered_categories, ordered_categories

def preprocess(data: pd.DataFrame, unordered_categories={}, ordered_categories={}) -> pd.DataFrame:
    """
    drop nan values and use categorical dtype
    if we dont pass categories the categorization part is skipped
    """
    feature_target_data = data.dropna() 
    #feature_target_data = feature_target_data[feature_target_data['q212813'] != 'Other']

    if not (unordered_categories and ordered_categories):

        for question, categories in unordered_categories.items():
            cat_type = CategoricalDtype(categories=categories)
            feature_target_data[question] = feature_target_data[question].astype(cat_type)

        for question, categories in ordered_categories.items():
            cat_type = CategoricalDtype(categories=categories.reverse(), ordered=True)
            feature_target_data[question] = feature_target_data[question].astype(cat_type)

    return feature_target_data
