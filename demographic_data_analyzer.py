import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")
    df.info()

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race=df['race'].value_counts()
    race_count =pd.Series(race,index=['White','Black','Asian-Pac-Islander','Amer-Indian-Eskimo','Other'])
    # What is the average age of men?
    
    age_men =  df[df['sex'] == 'Male']['age']
    average_age_men =age_men.mean().round(1)

    # What is the percentage of people who have a Bachelor's degree?
    total_count=32561
    bachelors=(df['education']=='Bachelors').sum()

    percentage_bachelors = round((bachelors/total_count)*100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
       # What percentage of people without advanced education make more than 50K?
    # with and without `Bachelors`, `Masters`, or `Doctorate`

   # Filter rows for advanced education
    advanced = df.loc[
        (df['education'] == 'Bachelors') |
        (df['education'] == 'Masters') |
        (df['education'] == 'Doctorate')
    ]

    # Total count of advanced education
    advanced_total = advanced.shape[0]

    # Count of people with advanced education earning >50K
    advanced_higher = advanced.loc[advanced['salary'] == '>50K'].shape[0]

    # Filter rows for lower education
    lower = df.loc[
        ~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    ]

    # Count of people with lower education earning >50K
    lower_higher = lower.loc[lower['salary'] == '>50K'].shape[0]
    

    
    
                                                 

    # percentage with salary >50K
    higher_education_rich = round ((advanced_higher / advanced_total) * 100,1)
    lower_education_rich =  round((lower_higher / lower.shape[0]) * 100,1)

   # Minimum number of hours worked per week
    min_work_hours = df['hours-per-week'].min()

    # Filter workers who work the minimum number of hours
    num_min_workers = df.loc[df['hours-per-week'] == min_work_hours]

    # Count of minimum-hour workers earning >50K
    rich_min_workers = num_min_workers.loc[num_min_workers['salary'] == '>50K'].shape[0]

    # Total count of minimum-hour workers
    total_min_workers = num_min_workers.shape[0]

    # Percentage of rich among minimum-hour workers
    rich_percentage = (rich_min_workers / total_min_workers) * 100


    # What country has the highest percentage of people that earn >50K?
    
    rich=df[df['salary']=='>50K']
    country=df['native-country'].value_counts()
    rich_per_country=rich['native-country'].value_counts()
    percentage_per_country=((rich_per_country/country)*100).round(1)
    
    
    
    
    
    highest_earning_country = percentage_per_country.idxmax()
    highest_earning_country_percentage = percentage_per_country.max()

    # Identify the most popular occupation for those who earn >50K in India.
    india=df[df['native-country']=='India']
    india_rich=india[india['salary']=='>50K']
    india_occupation=india_rich['occupation'].value_counts()  
    
   
   
    top_IN_occupation = india_occupation.idxmax()
    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
