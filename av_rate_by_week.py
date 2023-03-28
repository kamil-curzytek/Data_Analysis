import pandas
from datetime import datetime

#preparing df to analyze average rating by week
df = pandas.read_csv("reviews.csv", parse_dates= ["Timestamp"])
df['Week'] = df['Timestamp'].dt.strftime('%Y-%U')  #%U - week number in the year
week_average = df.groupby(['Week']).mean()

week_average_chart = """
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Average rating by Week'
    },
    subtitle: {
        text: ' '
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Week'
        },
        labels: {
            format: '{value} '
        },
        accessibility: {
            rangeDescription: ''
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Average Rating'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: -90°C to 20°C.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.y}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Average Raiting',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}
"""