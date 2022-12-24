import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class specific:
    
    description = "plot some data from data frame"
    def __init__(self,clabel,rlabel):
        # self.data_frame = df
        self.row_label = rlabel
        self.colulmn_label = clabel  
        
        
    def read_data(self,file = "crime_rate_Spain.csv"):
        """
        Parameters
        ----------
        file : 
            DESCRIPTION. The default is "crime_rate_Spain.csv".

        Returns
        -------
        df :DataFrame

        """
        df = pd.read_csv(file)
        return df
    
    
    def data_reduce(self,data,label,value):
        """
        Selecting subset of data  raws

        Parameters
        ----------
        data : dataFrame
        label : string
            the label of data coulmn.
        value : string
            the raw name  .

        Returns
        -------
        specific_data : TYPE
            DESCRIPTION.

        """
        
        specific_data= data[data[label] == value] 
        return  specific_data
    
    
    def trend_of_specific_phenomenon(self,data,label):
        """
        this function return two value the total sum 
        and the data we want to find sum of it

        """
        first_data =specific.remove_the_dublicates(data[label]) 
        total = specific.total_case_sum(first_data,data,label)
        return  first_data,total 
    
    
    def remove_the_dublicates(dlist):
        """
        remove the data dublicates in list

        """
        new_list =[]  
        for i in range(len(dlist)):
            item = dlist.iloc[i]
            if item not in new_list:
                new_list.append(item)
        return new_list
    
    
    def total_case_sum(first_data,data,label,cases="Total cases"):
        """
        find the total sum for cases acording to spicefic data
        Returns
        -------
        cases_sum : list
           

        """
        cases_sum =[]
        for i in range(len(first_data)):
            new= data[data[label] == first_data[i]]
            new2 = new[cases]#sum the total cases for all location 
            cases_sum.append(new2.sum())
        return cases_sum


class crime_per_year(specific):
    def __init__(self,clabel,rlabel):
        specific.__init__(self, clabel, rlabel)
        
    def curves_plot(self,x,y,titel,x_val,y_val):
        
        
        """
        curve plot for the data

        """
        plt.xlabel(x)
        plt.ylabel(y)
        plt.title(titel)
        plt.xticks(np.arange(min(x_val), max(x_val)+1, 1.0)) 
        plt.plot(x_val,y_val)
        plt.show()
    
    
class distrbution_per_city(specific):
    def __init__(self,clabel,rlabel):
        specific.__init__(self, clabel, rlabel)
    def pie_plot(self,values,label):
        """
        pie plot for given data

        """
        fig, ax = plt.subplots()
        ax.pie(values, radius=1, labels= label  )
        ax.set_title('distribution of different crimes in the Barcelona')
        plt.show()
       
        
def bar_chart(specific_crime):
    '''
    A bar chart showing a comparison of number of crimes in a few cities (at least 
    five)

    '''
    labels = specific_crime["Location"].iloc[0:5]
    number_of_crime = specific_crime["Total cases"].iloc[0:5]
    x = np.arange(len(labels))
    width = 0.5
    fig, ax = plt.subplots()
    ax.bar(x-width/2, number_of_crime, 0.5,  color = "green")
    ax.set_ylabel("total cases")
    ax.set_title("Locations")
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation='vertical')
    ax.legend()
    fig.tight_layout()
    plt.show()
    
        
#1 The trend of a specific crime over time
curve =  crime_per_year("Crime","Vehicle theft")
data = curve.read_data()       
specific_crime = curve.data_reduce(data,"Crime","Vehicle theft")    
totals = curve.trend_of_specific_phenomenon( specific_crime,"Year")
x=totals[0] #the years
y =totals[1] #total casses
curve.curves_plot("year","total cases","Vehicle theft",x,y)

#2  A pie chart showing the distribution of different crimes in the country or in aspecific city 
pie = distrbution_per_city("Location","Barcelona")
specific_city = pie.data_reduce(data,"Location","Barcelona")    
city_total = pie.trend_of_specific_phenomenon( specific_city ,"Crime")
pie.pie_plot(city_total[1],city_total[0])

#     """
#     Parameters
#     ----------
#     file : 
#         DESCRIPTION. The default is "crime_rate_Spain.csv".

#     Returns
#     -------
#     df :DataFrame

#     """
#     df = pd.read_csv(file)
#     return df

    
#3 A bar chart showing a comparison of number of crimes in a few cities (at least 
bar_chart(specific_crime) 



