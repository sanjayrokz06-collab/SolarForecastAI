from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.platypus import Spacer
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime
import os


def generate_report(result):

    if not os.path.exists("reports"):
        os.mkdir("reports")

    filename = "reports/Solar_Report.pdf"

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph(
            "<b><font size=18>AI Based Smart Solar Forecasting System</font></b>",
            styles["Title"]
        )
    )

    story.append(Spacer(1,20))

    story.append(
        Paragraph(
            "<b>Solar Forecast Research Report</b>",
            styles["Heading2"]
        )
    )

    story.append(Spacer(1,12))

    story.append(
        Paragraph(
            f"<b>Date :</b> {datetime.now()}",
            styles["Normal"]
        )
    )

    story.append(Spacer(1,12))

    story.append(
        Paragraph(
            "<b>Current Weather</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            f"Temperature : {result['temperature']} °C",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"Humidity : {result['humidity']} %",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"Wind Speed : {result['wind']} m/s",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"Cloud Cover : {result['cloud']} %",
            styles["Normal"]
        )
    )

    story.append(Spacer(1,18))

    story.append(
        Paragraph(
            "<b>AI Prediction</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            f"Predicted DNI : {result['dni']} W/m²",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"Estimated Solar Power : {result['power']} kW",
            styles["Normal"]
        )
    )

    story.append(Spacer(1,18))

    story.append(
        Paragraph(
            "<b>AI Model Information</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            "Model : LSTM Neural Network",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            "Optimizer : Adam",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            "Loss Function : Mean Squared Error",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            "Epochs : 30",
            styles["Normal"]
        )
    )

    story.append(Spacer(1,18))

    story.append(
        Paragraph(
            "<b>Solar PV Specifications</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            "Panel Area : 26 m²",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            "Efficiency : 21.3%",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            "Performance Ratio : 0.80",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            "Inverter Efficiency : 97%",
            styles["Normal"]
        )
    )

    story.append(Spacer(1,20))

    story.append(
        Paragraph(
            "<b>Research Summary</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            "The AI model predicts solar irradiance using live weather information and estimates solar power generation using photovoltaic system parameters.",
            styles["Normal"]
        )
    )

    doc.build(story)

    return filename