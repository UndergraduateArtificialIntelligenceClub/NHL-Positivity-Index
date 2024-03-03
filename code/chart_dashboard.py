import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from plottable import ColumnDefinition, Table
from plottable.cmap import normed_cmap
from plottable.plots import image, circled_image, bar
from plottable.formatters import decimal_to_percent
import os
import matplotlib.image as mpimg
import json
from constants import TEAMS

def create_positivity_score_df(pos_scores: list[dict]) -> pd.DataFrame:
    pos_scores = pd.Series(pos_scores)
    biweekly_NHL_positivity_index = pd.DataFrame(pos_scores, columns=['positivity_score'])
    biweekly_NHL_positivity_index.reset_index(inplace=True)
    biweekly_NHL_positivity_index.rename(columns={'index': 'team_abbr'}, inplace=True)
    biweekly_NHL_positivity_index['team_name'] = biweekly_NHL_positivity_index['team_abbr'].map(TEAMS)
    biweekly_NHL_positivity_index['logo'] = biweekly_NHL_positivity_index['team_abbr'].apply(
        lambda x:
        "data/nhl-logos/{x}_logo.png"
    )
    biweekly_NHL_positivity_index = biweekly_NHL_positivity_index.sort_values(by = 'positivity_score', ascending = False)

    biweekly_NHL_positivity_index = biweekly_NHL_positivity_index.reset_index(drop = True)

    biweekly_NHL_positivity_index.index += 1

    biweekly_NHL_positivity_index['rank'] = biweekly_NHL_positivity_index.index
    biweekly_NHL_positivity_index = biweekly_NHL_positivity_index[['rank', 'logo', 'team_name', 'positivity_score']]
    
    return biweekly_NHL_positivity_index

def plot_positivity_bar(ax, val, height, cmap, width = 0.4):
    """Plots TAA bar on the plottable table

    Args:
        ax : matplotlib axis
        val (float): value to be plotted
        height : height of bar
        cmap : matplotlib color map
        width (float, optional): width of bar Defaults to 0.5.
    """
    color = cmap(val)
    ax.barh(y=[0], width=[val], color=color, height=height)
    ax.set_xlim(-2, 3)
    ax.axis('off')
    ax.text(val + 0.05 if val >= 0 else val - 0.05, 0, f'{val:.2f}',
            va='center', ha='right' if val < 0 else 'left', fontweight='bold')
    
def create_biweekly_dashboard(biweekly_NHL_positivity_index: pd.DataFrame):
    bg_color = "#FFFFFF"
    text_color = "#000000"

    row_colors = {"#91C465", "D0F0C0", "F0FFF0", "F5FFFA"}

    plt.rcParams['text.color'] = text_color
    plt.rcParams['font.family'] = "monospace"
    cmap = normed_cmap(biweekly_NHL_positivity_index["positivity_score"], cmap = plt.cm.PiYG, num_stds = 2.5)

    col_defs = [
    ColumnDefinition(
        name = "rank",
        title = "Rank",
        textprops = {"ha": "center", "weight":"bold"},
        width = 0.1
    ),
    ColumnDefinition(
        name = "logo",
        title = "Team",
        textprops = {"ha": "center", "va":"center", "weight":"bold", "color": text_color},
        width = 0.1,
        plot_fn = image
    ),
    ColumnDefinition(
        name = "team_name",
        title = "",
        textprops = {"ha": "left", "va":"center", "weight":"bold", "color": text_color},
        width = 0.5,
    ),
    ColumnDefinition(
        name = "positivity_score",
        title = "Positivity Score",
        textprops = {"ha": "right", "va":"center", "weight":"bold", "color": text_color},
        width = 1.25,
        plot_fn = plot_positivity_bar,
        plot_kw = {
            "height": 0.4,
            "cmap": cmap
        }
    )
]

    fig, ax = plt.subplots(figsize=(20,17))
    fig.set_facecolor(bg_color)
    ax.set_facecolor(bg_color)
    table = Table(
        biweekly_NHL_positivity_index,
        column_definitions = col_defs,
        index_col = "rank",
        row_dividers = True,
        row_divider_kw = {"linewidth":1, "linestyle": (0, (1,5))},
        footer_divider = True,
        textprops = {"fontsize":10},
        ax = ax
    ).autoset_fontcolors(colnames=["positivity_score"])

    ax.set_title('NHL Positivity Index', fontsize=25)
    subtitle_x = 0.51
    subtitle_y = 0.865
    subtitle_text = 'Feb. 1 - Feb. 15, 2024'
    fig.text(subtitle_x, subtitle_y, subtitle_text, fontsize=16, va='center', ha='center', transform=fig.transFigure)
    uais_logo = mpimg.imread('/content/drive/Shareddrives/UAIS Executive Team/media/Logo/small_logo_color@0.5x.png')
    uais_logo_ax = fig.add_axes([0.25, 0.05, 0.15, 0.05])
    uais_logo_ax.axis('off')
    uais_logo_ax.imshow(uais_logo)
    text_x = 0.35
    text_y = 0.08
    fig.text(text_x, text_y, 'University of Alberta Undergraduate Artificial Intelligence Society', fontsize=12, va='center', ha='left')
    plt.show()
    fig.savefig('figures/dashboards/Feb1-Feb15.pdf', dpi=300, format='pdf', bbox_inches='tight')
