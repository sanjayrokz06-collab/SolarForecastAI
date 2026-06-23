import plotly.graph_objects as go


def create_weather_chart(result):

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=["Temperature", "Humidity", "Wind", "Cloud"],
        y=[
            result["temperature"],
            result["humidity"],
            result["wind"],
            result["cloud"]
        ],
        text=[
            result["temperature"],
            result["humidity"],
            result["wind"],
            result["cloud"]
        ],
        textposition="outside",
        name="Weather"
    ))

    fig.update_layout(
        title="Live Weather Parameters",
        template="plotly_dark",
        height=400
    )

    return fig.to_html(full_html=False)


def create_temperature_chart(result):

    x = ["6AM","9AM","12PM","3PM","6PM","9PM"]

    y = [
        result["temperature"]-3,
        result["temperature"]-1,
        result["temperature"],
        result["temperature"]+1,
        result["temperature"]-1,
        result["temperature"]-2
    ]

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=x,
        y=y,
        mode="lines+markers",
        name="Temperature"
    ))

    fig.update_layout(
        title="Temperature Trend",
        template="plotly_dark",
        height=400
    )

    return fig.to_html(full_html=False)


def create_dni_chart(result):

    x=["6AM","9AM","12PM","3PM","6PM","9PM"]

    y=[
        0,
        result["dni"]*0.4,
        result["dni"],
        result["dni"]*0.8,
        result["dni"]*0.2,
        0
    ]

    fig=go.Figure()

    fig.add_trace(go.Scatter(
        x=x,
        y=y,
        mode="lines+markers",
        name="DNI"
    ))

    fig.update_layout(
        title="Predicted Solar Irradiance",
        template="plotly_dark",
        height=400
    )

    return fig.to_html(full_html=False)


def create_power_chart(result):

    x=["6AM","9AM","12PM","3PM","6PM","9PM"]

    y=[
        0,
        result["power"]*0.4,
        result["power"],
        result["power"]*0.8,
        result["power"]*0.3,
        0
    ]

    fig=go.Figure()

    fig.add_trace(go.Scatter(
        x=x,
        y=y,
        mode="lines+markers",
        name="Power"
    ))

    fig.update_layout(
        title="Estimated Solar Power",
        template="plotly_dark",
        height=400
    )

    return fig.to_html(full_html=False)