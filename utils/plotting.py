import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


def plot_question_distribution(question: str, data: pd.DataFrame, questions: pd.DataFrame):
    """plots histogram of polical orientation for a given question"""
    sns.catplot(
        data=data, y='q212813', hue=question, kind="count",
        palette="pastel", edgecolor=".6"
        ).set(title=questions.loc[question, 'text'])

def plot_confusion_matrix(conf_matrix, labels):
    plt.figure(figsize=(8,6), dpi=100)
    # Scale up the size of all text
    sns.set(font_scale = 1.1)

    # Plot Confusion Matrix using Seaborn heatmap()
    # Parameters:
    # first param - confusion matrix in array format   
    # annot = True: show the numbers in each heatmap cell
    # fmt = 'd': show numbers as integers. 
    ax = sns.heatmap(conf_matrix, annot=True, fmt='d', )

    # set x-axis label and ticks. 
    ax.set_xlabel("Predicted Political Orientation", fontsize=14, labelpad=20)
    ax.xaxis.set_ticklabels(labels)

    # set y-axis label and ticks
    ax.set_ylabel("Actual Political Orientation", fontsize=14, labelpad=20)
    ax.yaxis.set_ticklabels(labels)

    # set plot title
    #ax.set_title("", fontsize=14, pad=20)

    plt.show()


def plot_contingency_table(tb):
    ax = sns.heatmap(tb, annot=True, fmt='g')

    # set x-axis label and ticks. 
    ax.set_xlabel("Scrambled Targets", fontsize=14, labelpad=20)
    ax.xaxis.set_ticklabels(['correct', 'wrong'])
    
    # set y-axis label and ticks
    ax.set_ylabel("Model Proediction", fontsize=14, labelpad=20)
    ax.yaxis.set_ticklabels(['correct', 'wrong'])

    # set plot title
    ax.set_title("Contingency Table", fontsize=14, pad=20)

    plt.show()