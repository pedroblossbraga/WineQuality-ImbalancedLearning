import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from PIL import Image

def addlabels(x,y, 
              fontsize = 14):
    for i in range(len(x)):
        plt.text(x[i]-0.2,y[i],y[i],
                 fontsize=fontsize)

def plot_dist(col,
              lb = None,
              ub = None):
  """ 
  plot distribution and boxplot 
  ------------------------------
  Parameters
    col: column
    lb: float, lower bound for interval
    up: float, upper bound for interval
  ------------------------------
  """ 

  mu = df[[col]].mean()[0]
  sigma = df[[col]].std()[0]

  fig = plt.figure(figsize=(15,4))
  plt.subplot(1,2,1)
  plt.title('Distribution of {}'.format(col), 
            fontsize = 18)
  sns.distplot(df[col].values)
  plt.axvline(x = mu, color = 'red',
              label = r'$\mu$')
  
  if lb is None:
    lb = mu - (3*sigma)
    lb_label = r'$\mu-3\sigma$'
  else: 
    lb_label = '{:.3f}'.format(lb)

  if ub is None:
    ub = mu + (3*sigma)
    ub_label = r'$\mu+ 3\sigma$'
  else: 
    ub_label = '{:.3f}'.format(ub)

  plt.axvline(x = ub, 
              color = 'green',
              label = ub_label)
  plt.axvline(x = lb, 
              color = 'green',
              label = lb_label)
  plt.legend(loc='best',
             fontsize = 18)
  
  plt.subplot(1,2,2)
  sns.boxplot(df[col].values)
  return fig


@st.cache #helps page performance
def load_data():
    df = pd.read_csv(os.path.join( 'data', 'VinhoVerde.csv'))
    return df

df = load_data()

def show_explore_page():
    st.title('Explore the VinhoVerde dataset')

    st.write("""### Wine Quality""")


    labels = list(set(df['quality'].unique()))
    sizes = list(map(lambda val : len(df[df['quality']==val].values),
                    labels))
    N = len(labels)
    explode_list = tuple([0.2]* N)

    fig1, _ = plt.subplots(figsize = (16,5))
    plt.suptitle('Frequencies for each quality labels',
                fontsize = 20,
                y = 1.05)
    plt.subplot(1,2,1)
    plt.pie(sizes, explode=explode_list, labels=labels, 
            autopct='%1.2f%%',
            shadow=True, 
            startangle=0)

    plt.subplot(1,2,2)
    plt.bar(labels, sizes)
    addlabels(labels, sizes)
    st.pyplot(fig1)

    st.write("""## Imbalanced Learning""")

    st.write("""Since the original data had imbalance particularly for the high and low quality classes (3, 4 and 8),
     some Imbalanced Learning technicques could be applied, such as oversampling, adding weights to the Random Forest parameters.
     In this case we did both.
     """)
    st.write("""### Original data""")
    image = Image.open(os.path.join('images', 'original_data.png'))
    st.image(image, caption="")

    st.write("""### SMOTESVM oversampling augmented data""")
    image = Image.open(os.path.join('images', 'smotesvm_oversampling.png'))
    st.image(image, caption="")

    st.write("""As you can see, the classes with low frequencies had augmented data, 
    using the SMOTESVM algorithm from imblearn.
    Mainly, the algorithm searchs for new values similar to the existent, in order to "fill the gaps". """)


def show_explore_features_page():
    st.write("""### Distribution of Features""")
    st.write("""
    
    Here we can see the distribution of each attribute of the dataset,
     with the barplot, the boxplot, and a confidence interval.
     
     """)
    for col in df.columns:
        col_fig = plot_dist(col)
        st.pyplot(col_fig)


def show_project_page():
  st.write("""### Wine Quality - Imbalanced Learning Project""")
  st.write('Author: Pedro Blöss Braga')
  st.write('Github repository: https://github.com/pedroblossbraga/WineQuality-ImbalancedLearning/tree/main')