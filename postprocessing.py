import camelot
from datetime import date
import pandas as pd



if __name__ == "__main__":

    print("argv :", sys.argv)

  
    df = pd.DataFrame(np.random.randint(
    0, 100, size=(10, 4)), columns=list('ABCD'))

    df.to_csv("df_output.csv")

    df = camelot.read_pdf('https://www.cookcountysheriffil.gov/wp-content/uploads/2020/05/CCSO_BIU_CommunicationsCCDOC_v1_2020_05_29.pdf')
    if len(df) ==1:
        dfs = df[0].df

    dfs.to_csv('parsed_pdf_test.csv')
