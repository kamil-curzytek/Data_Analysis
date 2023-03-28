import justpy as jp
import pandas
from datetime import datetime

from av_rate_by_day import day_average_chart
from av_rate_by_day import day_average

from av_rate_by_week import week_average_chart
from av_rate_by_week import week_average

from av_rate_by_month import month_average_chart
from av_rate_by_month import month_average

from av_rate_by_course_by_month import month_average_crs_chart
from av_rate_by_course_by_month import month_average_crs

from count_rate_by_course_by_month_stream import month_count_crs_str_chart
from count_rate_by_course_by_month_stream import month_count_crs_str

from av_rate_by_weekday import weekday_average_chart
from av_rate_by_weekday import weekday_average

from rate_percentage_by_course import rate_percentage
from rate_percentage_by_course import percentage_chart

def app():
    wp = jp.QuasarPage() 
    h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews", classes = "text-h1 text-center")
    p1 = jp.QDiv(a=wp, text = " -- ", classes = "text-h3 text-white")
    p2 = jp.QDiv(a=wp, text = "This website consists of few interactive graphs which shows data analysis example based on Udemy courses reviews csv file. Frameworks -> Pandas, JustPy, HighCharts", classes = "text-h8 text-center")
    p3 = jp.QDiv(a=wp, text = " -- ", classes = "text-h3 text-white")

    #average raiting by day chart
    hc1 = jp.HighCharts(a=wp, options = day_average_chart)
    hc1.options.xAxis.categories = list(day_average.index)
    hc1.options.series[0].data = list(day_average["Rating"])

    #average raiting by week chart
    hc2 = jp.HighCharts(a=wp, options = week_average_chart)
    hc2.options.xAxis.categories = list(week_average.index)
    hc2.options.series[0].data = list(week_average["Rating"]) 

    #average raiting by month chart
    hc3 = jp.HighCharts(a=wp, options = month_average_chart)
    hc3.options.xAxis.categories = list(month_average.index)
    hc3.options.series[0].data = list(month_average["Rating"])

    #average raiting by course by month chart
    hc4 = jp.HighCharts(a=wp, options = month_average_crs_chart)
    hc4.options.xAxis.categories = list(month_average_crs.index)
    hc4_list = [{"name": v1, "data": [v2 for v2 in month_average_crs[v1]]} for v1 in month_average_crs.columns]
    hc4.options.series = hc4_list

    #average raiting by course by month chart
    hc5 = jp.HighCharts(a=wp, options = month_count_crs_str_chart)
    hc5.options.xAxis.categories = list(month_count_crs_str.index)
    hc5_list = [{"name": v1, "data": [v2 for v2 in month_count_crs_str[v1]]} for v1 in month_count_crs_str.columns]
    hc5.options.series = hc5_list

    #average raiting by weekday
    hc6 = jp.HighCharts(a=wp, options = weekday_average_chart)
    hc6.options.xAxis.categories = list(weekday_average.index.get_level_values(0)) #getting only Weekday values, no index numbers
    hc6.options.series[0].data = list(weekday_average["Rating"])

    #percentage chart by course
    hc7 = jp.HighCharts(a=wp, options = percentage_chart)
    hc7_data = [{"name": v1, "y": v2} for v1,v2 in zip(rate_percentage.index, rate_percentage)]
    hc7.options.series[0].data = hc7_data

    return wp

jp.justpy(app) #calling app function