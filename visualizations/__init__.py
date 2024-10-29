import itertools
import plotly.graph_objects as go
import pandas as pd

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
def plot_total_staked(df_raw, scenario_names):
    color_cycle = itertools.cycle(cadlabs_colorway_sequence)
    fig = go.Figure()

    df = df_raw.copy()
    df = df[df['substep'] == df['substep'].max()].reset_index(drop=True)
    df = df.drop(0).reset_index(drop=True)


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


def plot_cost_APY_for_agents(df_raw, agent_names):

    df = df_raw.copy()
    df = df[df['substep'] == df['substep'].max()].reset_index(drop=True)
    df = df.drop(0).reset_index(drop=True)
    
    cost_APY_data = pd.DataFrame({
        "timestep": df["timestep"]
    })

    for agent in agent_names:
        cost_APY_data[agent] = df[agent].apply(lambda x: x.cost_APY *100)

    color_cycle = itertools.cycle(cadlabs_colorway_sequence)
    fig = go.Figure()

    for agent in agent_names:
        color = next(color_cycle)
        fig.add_trace(
            go.Scatter(
                x=cost_APY_data["timestep"],
                y=cost_APY_data[agent],
                name=str(agent), 
                line=dict(color=color),
            )
        )

    fig.update_layout(
        title={
            'text': "Cost APY for Each Agent Category",
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        xaxis_title="Time",
        yaxis_title="Cost APY (%)",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.4,
            xanchor="center",
            x=0.5,
            font=dict(
                size=18,
                color="black",
            ),
        ),
        hovermode="x unified",
        template="plotly_white",
        font=dict(
            family="Arial",
            size=18,
            color="black"
        ),
        plot_bgcolor='rgba(255, 255, 255, 1)', 
        paper_bgcolor='rgba(255, 255, 255, 1)',
    )

    fig.for_each_xaxis(lambda x: x.update(dict(title=dict(text="Time"))))
    fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))

    return fig

def plot_balance_for_agents(df, agent_names):
    
    cost_APY_data = pd.DataFrame({
        "timestep": df["timestep"]
    })

    for agent in agent_names.keys():
        cost_APY_data[agent] = df[agent].apply(lambda x: x.cnt)

    color_cycle = itertools.cycle(cadlabs_colorway_sequence)
    fig = go.Figure()

    for agent in agent_names.keys():
        color = next(color_cycle)
        fig.add_trace(
            go.Scatter(
                x=cost_APY_data["timestep"],
                y=cost_APY_data[agent],
                name=str(agent), 
                line=dict(color=color),
            )
        )

    fig.update_layout(
        title={
            'text': "Total Deposits for Each Agent Category",
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        xaxis_title="Time",
        yaxis_title="Balance (ETH)",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.4,
            xanchor="center",
            x=0.5,
            font=dict(
                size=12,
                color="black",
            ),
        ),
        hovermode="x unified",
        template="plotly_white",
        font=dict(
            family="Arial",
            size=18,
            color="black"
        ),
        plot_bgcolor='rgba(255, 255, 255, 1)', 
        paper_bgcolor='rgba(255, 255, 255, 1)',
    )

    fig.for_each_xaxis(lambda x: x.update(dict(title=dict(text="Time"))))
    fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))

    return fig

def plot_revenue_APY_for_agents(df_raw, agent_names):
    """
    Visualize revenue_APY for each agent category over time.
    
    Parameters:
    - df: DataFrame containing simulation data with a 'revenue_APY_at_agent' column, where each entry is a dictionary.
    - agent_names: Dictionary mapping each agent key in 'revenue_APY_at_agent' to a display name.
    """

    

    df = df_raw.copy()
    df = df[df['substep'] == df['substep'].max()].reset_index(drop=True)
    df = df.drop(0).reset_index(drop=True)

    revenue_data = pd.DataFrame({
        "timestep": df["timestep"]
    })



    for agent in agent_names.keys():
        revenue_data[agent] = df["revenue_APY_at_agent"].apply(lambda x: x.get(agent, None)*100)
    print(revenue_data)

    color_cycle = itertools.cycle(cadlabs_colorway_sequence)
    fig = go.Figure()

    for agent in agent_names.keys():
        color = next(color_cycle)
        fig.add_trace(
            go.Scatter(
                x=revenue_data["timestep"],
                y=revenue_data[agent],
                name=agent,
                line=dict(color=color),
            )
        )

    fig.update_layout(
        title={
            'text': "Revenue APY for Each Agent Category",
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        xaxis_title="Time",
        yaxis_title="Revenue APY (%)",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.4,
            xanchor="center",
            x=0.5,
            font=dict(
                size=18,
                color="black",
            ),
        ),
        hovermode="x unified",
        template="plotly_white",
        font=dict(
            family="Arial",
            size=18,
            color="black"
        ),
        plot_bgcolor='rgba(255, 255, 255, 1)', 
        paper_bgcolor='rgba(255, 255, 255, 1)',
    )

    fig.for_each_xaxis(lambda x: x.update(dict(title=dict(text="Time"))))
    fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))

    return fig

def plot_avg_revenue_APY(df_raw, scenario_names):
    color_cycle = itertools.cycle(cadlabs_colorway_sequence)
    fig = go.Figure()

    df = df_raw.copy()
    df = df[df['substep'] == df['substep'].max()].reset_index(drop=True)
    df = df.drop(0).reset_index(drop=True)


    for subset in df.subset.unique():
        color = next(color_cycle)
        fig.add_trace(
            go.Scatter(
                x=df[df.subset == subset]["timestep"],
                y=df[df.subset == subset]["revenue_APY"]*100,
                name=scenario_names[subset],
                line=dict(color=color,dash='dot'),
            )
        )

    fig.update_layout(
        title={
            'text': "Revenue APY (%)",
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'},
        xaxis_title="Time",
        yaxis_title="APY (%)",
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

