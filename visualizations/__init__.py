import itertools
import plotly.graph_objects as go

from visualizations.plotly_theme import (
    cadlabs_colors,
    cadlabs_colorway_sequence,
)

legend_state_variable_name_mapping = {
    "timestep": "Day",
    "price": "ETH price", 
}


def update_legend_names(fig, name_mapping=legend_state_variable_name_mapping):
    for i, dat in enumerate(fig.data):
        for elem in dat:
            if elem == "name":
                try:
                    fig.data[i].name = name_mapping[fig.data[i].name]
                except KeyError:
                    continue
    return fig


# Token Price
def plot_token_price_per_subset(df, scenario_names):
    color_cycle = itertools.cycle(cadlabs_colorway_sequence)
    fig = go.Figure()

    for subset in df.subset.unique():
        color = next(color_cycle)
        fig.add_trace(
            go.Scatter(
                x=df[df.subset == subset]["timestep"],
                y=df[df.subset == subset]["price"],
                name=scenario_names[subset],
                line=dict(color=color,dash='dot'),
            )
        )

    fig.update_layout(
        title={
            'text': "ETH Token Price",
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'},
        xaxis_title="Time",
        yaxis_title="USD",
        legend=dict(
            orientation="h",  # Horizontal orientation
            yanchor="bottom",
            y=-0.4,  # Position it a bit below the x-axis
            xanchor="center",
            x=0.5,  # Center it
            font=dict(
                size=18,  # Adjust the size as needed
                color="black",
            ),
        ),
        hovermode="x unified",
        template="plotly_white",
        font=dict(
            family="Arial",
            size=18,
            color="black"),
        plot_bgcolor='rgba(255, 255, 255, 1)', 
        paper_bgcolor='rgba(255, 255, 255, 1)',
    )

    fig.for_each_xaxis(lambda x: x.update(dict(title=dict(text="Date"))))

    # Removes the 'subset=' from the facet_col title
    fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))

    update_legend_names(fig)
    #fig.write_html('/Users/wenxuan/Desktop/polygon/cadCAD/Token-Redesign/experiments/notebooks/visualizations/plots/token_price/token_price.html')


    return fig

# Total Staked
def plot_total_staked(df, scenario_names):
    color_cycle = itertools.cycle(cadlabs_colorway_sequence)
    fig = go.Figure()

    df = df.iloc[1:].copy()

    for subset in df.subset.unique():
        color = next(color_cycle)
        fig.add_trace(
            go.Scatter(
                x=df[df.subset == subset]["timestep"],
                y=df[df.subset == subset]["total_staked"],
                name=scenario_names[subset],
                line=dict(color=color,dash='dot'),
            )
        )

    fig.update_layout(
        title={
            'text': "Token Staked (ETH)",
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'},
        xaxis_title="Time",
        yaxis_title="ETH",
        legend=dict(
            orientation="h",  # Horizontal orientation
            yanchor="bottom",
            y=-0.4,  # Position it a bit below the x-axis
            xanchor="center",
            x=0.5,  # Center it
            font=dict(
                size=18,  # Adjust the size as needed
                color="black",
            ),
        ),
        hovermode="x unified",
        template="plotly_white",
        font=dict(
            family="Arial",
            size=18,
            color="black"),
        plot_bgcolor='rgba(255, 255, 255, 1)', 
        paper_bgcolor='rgba(255, 255, 255, 1)',
    )

    fig.for_each_xaxis(lambda x: x.update(dict(title=dict(text="Date"))))

    # Removes the 'subset=' from the facet_col title
    fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))

    update_legend_names(fig)
    #fig.write_html('/Users/wenxuan/Desktop/polygon/cadCAD/Token-Redesign/experiments/notebooks/visualizations/plots/token_price/token_price.html')


    return fig


# Total Staked
def plot_hhi(df, scenario_names):
    color_cycle = itertools.cycle(cadlabs_colorway_sequence)
    fig = go.Figure()

    df = df.iloc[1:].copy()
    df['HHI'] = df['decentralization_metrics'].apply(lambda x: x.get('HHI') if isinstance(x, dict) else None)


    for subset in df.subset.unique():
        color = next(color_cycle)
        fig.add_trace(
            go.Scatter(
                x=df[df.subset == subset]["timestep"],
                y=df[df.subset == subset]['HHI'],
                name=scenario_names[subset],
                line=dict(color=color,dash='dot'),
            )
        )

    fig.update_layout(
        title={
            'text': "HHI Decentralization",
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'},
        xaxis_title="Time",
        yaxis_title="HHI",
        legend=dict(
            orientation="h",  # Horizontal orientation
            yanchor="bottom",
            y=-0.4,  # Position it a bit below the x-axis
            xanchor="center",
            x=0.5,  # Center it
            font=dict(
                size=18,  # Adjust the size as needed
                color="black",
            ),
        ),
        hovermode="x unified",
        template="plotly_white",
        font=dict(
            family="Arial",
            size=18,
            color="black"),
        plot_bgcolor='rgba(255, 255, 255, 1)', 
        paper_bgcolor='rgba(255, 255, 255, 1)',
    )

    fig.for_each_xaxis(lambda x: x.update(dict(title=dict(text="Date"))))

    # Removes the 'subset=' from the facet_col title
    fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))

    update_legend_names(fig)
    #fig.write_html('/Users/wenxuan/Desktop/polygon/cadCAD/Token-Redesign/experiments/notebooks/visualizations/plots/token_price/token_price.html')


    return fig
