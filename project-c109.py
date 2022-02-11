import pandas as pd
import statistics
import csv

df = pd.read_csv("project-c109.csv")
math_score = df["math score"].to_list()
reading_score = df["reading score"].to_list()
writing_score = df["writing score"].to_list()

math_mean = statistics.mean(math_score)
reading_mean = statistics.mean(reading_score)
writing_mean = statistics.mean(writing_score)

math_median = statistics.median(math_score)
reading_median = statistics.median(reading_score)
writing_median = statistics.median(writing_score)

math_mode = statistics.mode(math_score)
reading_mode = statistics.mode(reading_score)
writing_mode = statistics.mode(writing_score)

print("Mean, Median and Mode of math is {}, {} and {} respectively".format(math_mean, math_median, math_mode))
print("Mean, Median and Mode of reading is {}, {} and {} respectively".format(reading_mean, reading_median, reading_mode))
print("Mean, Median and Mode of reading is {}, {} and {} respectively".format(writing_mean, writing_median, writing_mode))

math_std_deviation = statistics.stdev(math_score)
reading_std_deviation = statistics.stdev(reading_score)
writing_std_deviation = statistics.stdev(writing_score)

math_first_std_deviation_start, math_first_std_deviation_end = math_mean - math_std_deviation, math_mean+math_std_deviation
math_second_std_deviation_start, math_second_std_deviation_end = math_mean - (2*math_std_deviation), math_mean+(2*math_std_deviation)
math_third_std_deviation_start, math_third_std_deviation_end = math_mean - (3*math_std_deviation), math_mean+(3*math_std_deviation)

reading_first_std_deviation_start, reading_first_std_deviation_end = reading_mean - reading_std_deviation, reading_mean+reading_std_deviation
reading_second_std_deviation_start, reading_second_std_deviation_end = reading_mean - (2*reading_std_deviation), reading_mean+(2*reading_std_deviation)
reading_third_std_deviation_start, reading_third_std_deviation_end = reading_mean - (3*reading_std_deviation), reading_mean+(3*reading_std_deviation)

writing_first_std_deviation_start, writing_first_std_deviation_end = writing_mean - writing_std_deviation, writing_mean+writing_std_deviation
writing_second_std_deviation_start, writing_second_std_deviation_end = writing_mean - (2*writing_std_deviation), writing_mean+(2*writing_std_deviation)
writing_third_std_deviation_start, writing_third_std_deviation_end = writing_mean - (3*writing_std_deviation), writing_mean+(3*writing_std_deviation)

math_score_of_data_within_1_std_deviation = [result for result in math_score if result > math_first_std_deviation_start and result < math_first_std_deviation_end]
math_score_of_data_within_2_std_deviation = [result for result in math_score if result >math_second_std_deviation_start and result < math_second_std_deviation_end]
math_score_of_data_within_3_std_deviation = [result for result in math_score if result > math_third_std_deviation_start and result < math_third_std_deviation_end]

reading_score_of_data_within_1_std_deviation = [result for result in reading_score if result > reading_first_std_deviation_start and result < reading_first_std_deviation_end]
reading_score_of_data_within_2_std_deviation = [result for result in reading_score if result >reading_second_std_deviation_start and result < reading_second_std_deviation_end]
reading_score_of_data_within_3_std_deviation = [result for result in reading_score if result > reading_third_std_deviation_start and result < reading_third_std_deviation_end]

writing_score_of_data_within_1_std_deviation = [result for result in writing_score if result > writing_first_std_deviation_start and result < writing_first_std_deviation_end]
writing_score_of_data_within_2_std_deviation = [result for result in writing_score if result > writing_second_std_deviation_start and result < writing_second_std_deviation_end]
writing_score_of_data_within_3_std_deviation = [result for result in writing_score if result > writing_third_std_deviation_start and result < writing_third_std_deviation_end]

print("{}% of data for math lies within 1 standard deviation".format(len(math_score_of_data_within_1_std_deviation)*100.0/len(math_score)))
print("{}% of data for math lies within 2 standard deviations".format(len(math_score_of_data_within_2_std_deviation)*100.0/len(math_score)))
print("{}% of data for math lies within 3 standard deviations".format(len(math_score_of_data_within_3_std_deviation)*100.0/len(math_score)))

print("{}% of data for reading lies within 1 standard deviation".format(len(reading_score_of_data_within_1_std_deviation)*100.0/len(reading_score)))
print("{}% of data for reading lies within 2 standard deviations".format(len(reading_score_of_data_within_2_std_deviation)*100.0/len(reading_score)))
print("{}% of data for reading lies within 3 standard deviations".format(len(reading_score_of_data_within_3_std_deviation)*100.0/len(reading_score)))

print("{}% of data for writing lies within 1 standard deviation".format(len(writing_score_of_data_within_1_std_deviation)*100.0/len(writing_score)))
print("{}% of data for writing lies within 2 standard deviations".format(len(writing_score_of_data_within_2_std_deviation)*100.0/len(writing_score)))
print("{}% of data for writing lies within 3 standard deviations".format(len(writing_score_of_data_within_3_std_deviation)*100.0/len(writing_score)))
