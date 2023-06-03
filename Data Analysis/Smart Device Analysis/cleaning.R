install.packages('tidyverse')
library('tidyverse')

# Fetching data ------------------------------------------------------------------------
data <- read_csv("dataset/dailyActivity_merged.csv")
steps_data <- read_csv("dataset/hourlySteps_merged.csv")
cal_data <- read_csv("dataset/hourlyCalories_merged.csv")

# Cleaning data -------------------------------------------------------------------------
sum(duplicated(data))
sum(duplicated(steps_data))
sum(duplicated(cal_data))

data <- data %>%
  mutate(ActivityDate = as.Date(ActivityDate, "%m/%d/%y"))
data <- subset(data, select = -c(TrackerDistance, SedentaryActiveDistance,
                                 LoggedActivitiesDistance))
data <- data %>% rename(CaloriesBurnt = Calories)

steps_data <- steps_data %>%
  mutate(ActivityDate = as.Date(ActivityHour, "%m/%d/%y"))
steps_data <- steps_data %>%
  mutate(ActivityHour = format(as.POSIXct(ActivityHour, format="%m/%d/%Y %I:%M:%S %p"),
                               format="%H:%M"))
steps_data <- steps_data[,c(1,4,2,3)]


cal_data <- cal_data %>%
  mutate(ActivityDate = as.Date(ActivityHour, "%m/%d/%y"))
cal_data <- cal_data %>%
  mutate(ActivityHour = format(as.POSIXct(ActivityHour, format="%m/%d/%Y %I:%M:%S %p"),
                               format="%H:%M"))
cal_data <- cal_data[,c(1,4,2,3)]


# Analysis ---------------------------------------------------------------------------
steps_cal_data <- as_tibble(merge(steps_data, cal_data))

mean_steps_cal <- steps_cal_data %>% group_by(ActivityHour) %>%
  summarise(mean_steps = mean(StepTotal),
            mean_calories = mean(Calories))

data <- data %>%
  mutate(TotalActiveMinutes = LightlyActiveMinutes 
         + FairlyActiveMinutes + VeryActiveMinutes,
         Weekday = weekdays(ActivityDate))

mean_distance = mean(data$TotalDistance)

data <- data %>% select(Id, ActivityDate, Weekday, TotalSteps, 
                        TotalDistance, TotalActiveMinutes, CaloriesBurnt, everything())


# Export data -------------------------------------------------------------------------
write.csv(data, "dataset/processed/activity.csv", row.names = FALSE)
write.csv(mean_steps_cal, "dataset/processed/mean_hourly_steps.csv", row.names = FALSE)
