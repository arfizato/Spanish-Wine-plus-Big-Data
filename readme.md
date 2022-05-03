# Project For Big Data
This project is simply MapReduce homework for university 
## About Dataset
[Spanish Wine Quality Dataset](https://www.kaggle.com/datasets/fedesoriano/spanish-wine-quality-dataset)

### Context
This dataset is related to red variants of Spanish wines. The dataset describes several popularity and description metrics their effect on it's quality. The datasets can be used for classification or regression tasks. The classes are ordered and not balanced (i.e. the quality goes from almost 5 to 4 points). The task is to predict either the quality of wine or the prices using the given data.

### Content
The dataset contains 7500 different types of red wines from Spain with 11 features that describe their price, rating, and even some flavor description. The was collected by me using web scraping from different sources (from wine specialized pages to supermarkets). Please acknowledge the hard work to obtain and create this dataset, you can upvote it if you find it useful to use on your projects :)

If the dataset becomes popular I will probably try to create a bigger version with wines from other countries and a wider spectrum of ratings.

### Attribute Information
<dl>
<dt>winery: </dt><dd> Winery name</dd>
<dt>wine: </dt><dd> Name of the wine</dd>
<dt>year: </dt><dd> Year in which the grapes were harvested</dd>
<dt>rating: </dt><dd> Average rating given to the wine by the users [from 1-5]</dd>
<dt>num_reviews: </dt><dd> Number of users that reviewed the wine</dd>
<dt>country: </dt><dd> Country of origin [Spain]</dd>
<dt>region: </dt><dd> Region of the wine</dd>
<dt>price: </dt><dd> Price in euros [€]</dd>
<dt>type: </dt><dd> Wine variety</dd>
<dt>body: </dt><dd> Body score, defined as the richness and weight of the wine in your mouth [from 1-5]</dd>
<dt>acidity: </dt><dd> Acidity score, defined as wine's “pucker” or tartness; it's what makes a wine refreshing and your tongue salivate and want another sip [from 1-5]</dd>
</dl>

## Usage
*for all I know* **You Will Need to have Hadoop installed and set up correctly to run this**

1. First start all Hadoop services using `start-all.sh` and then switch to the directory containing the mapper and reducer function `cd <path>`


1. And then simply copy and paste these commands *(remember to delete or rename the file* `part-00000`*)* 
```
hdfs dfs -rmr /wineoutput
hadoop jar /$HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.3.2.jar  \
-file ./mapper.py -mapper 'python3 mapper.py' \
-file ./reducer.py -reducer 'python3 reducer.py' \
-input  /myinput/wine.txt \
-output /wineoutput
hadoop fs -ls /wineoutput
hdfs dfs -get /wineoutput/part-00000
```
<br>
<br>
    Any Feedback is  appreciated