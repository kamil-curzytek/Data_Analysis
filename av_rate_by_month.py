import pandas
from datetime import datetime

#preparing df to analyze average rating by month
df=pandas.read_csv("reviews.csv", parse_dates = ["Timestamp"])
df['Month'] = df['Timestamp'].dt.strftime("%Y-%m")
month_average = df.groupby(['Month']).mean()

month_average_chart = """
{
  chart: {
    type: 'spline',
    inverted: false
  },
  title: {
    text: 'Average rating by Month'
  },
  subtitle: {
    text: ''
  },
  xAxis: {
    reversed: false,
    title: {
      enabled: true,
      text: 'Month'
    },
    labels: {
      format: '{value}'
    },
    accessibility: {
      rangeDescription: ''
    },
    maxPadding: 0.05,
    showLastLabel: true
  },
  yAxis: {
    title: {
      text: 'Average Raiting'
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
    name: 'Average Rating',
    data: [
      [0, 15],
      [10, -50],
      [20, -56.5],
      [30, -46.5],
      [40, -22.1],
      [50, -2.5],
      [60, -27.7],
      [70, -55.7],
      [80, -76.5]
    ]
  }]
}
"""