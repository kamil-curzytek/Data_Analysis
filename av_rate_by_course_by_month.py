import pandas
from datetime import datetime

#preparing df to analyze average rating by course by month
df=pandas.read_csv("reviews.csv", parse_dates = ["Timestamp"])
df['Month']=df["Timestamp"].dt.strftime("%Y-%m")
month_average_crs = df.groupby(["Month","Course Name"])['Rating'].mean().unstack()

month_average_crs_chart = """
{
    chart: {
        type: 'spline'
    },
    title: {
        text: 'Average Rating by Course by Month'
    },
    subtitle: {
        align: 'center',
        //text: 'Source: <a href="https://www.ssb.no/jord-skog-jakt-og-fiskeri/jakt" target="_blank">SSB</a>'
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 120,
        y: 70,
        floating: false,
        borderWidth: 1,
        backgroundColor: '54C09C'
    },
    xAxis: {
        categories: [
            
        ]
        /* plotBands: [{ // Highlight the two last years
            from: 2019,
            to: 2020,
            color: 'rgba(68, 170, 213, .2)'
        }] */
    },
    yAxis: {
        title: {
            text: 'Average Rating'
        }
    },
    tooltip: {
        shared: true,
        headerFormat: '<b>Average Rating {point.x}</b><br>'
    },
    credits: {
        enabled: false
    },
    plotOptions: {
        areaspline: {
            fillOpacity: 0.5
        }
    },
    series: [{
        name: 'Moose',
        data:
            [
                38000,
                37300,
                37892,
                38564,
                36770,
                36026,
                34978,
                35657,
                35620,
                35971,
                36409,
                36435,
                34643,
                34956,
                33199,
                31136,
                30835,
                31611,
                30666,
                30319,
                31766
            ]
    }, {
        name: 'Deer',
        data:
            [
                22534,
                23599,
                24533,
                25195,
                25896,
                27635,
                29173,
                32646,
                35686,
                37709,
                39143,
                36829,
                35031,
                36202,
                35140,
                33718,
                37773,
                42556,
                43820,
                46445,
                50048
            ]
    }]
}
"""