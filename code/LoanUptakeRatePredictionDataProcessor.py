# Import the required libraries
import warnings
import pandas as pd
import numpy as np
import config as cfg
from functools import reduce
from pandas.api.types import CategoricalDtype

warnings.filterwarnings("ignore", category=DeprecationWarning)


class LoanUptakeRatePredictionDataProcessor:

    def __init__(self):
        self.encoding_format = cfg.ENCODING_FORMAT
        self.ext_county_town_file = cfg.EXT_COUNTY_TOWN_DATA_FILE
        self.ext_merchant_category_file = cfg.EXT_MERCHANT_CATEGORY_DATA_FILE
        self.raw_tra_data_dir = cfg.RAW_TRAIN_DATA_DIR
        self.raw_training_data_file_list = cfg.RAW_TRAINING_DATA_FILE_LIST
        self.raw_test_data_dir = cfg.RAW_TEST_DATA_DIR
        self.raw_test_data_file_list = cfg.RAW_TEST_DATA_FILE_LIST
        self.integer_var_col_list = cfg.INTEGER_VAR_COL_LIST
        self.float_var_col_list = cfg.FLOAT_VAR_COL_LIST
        self.category_var_col_list = cfg.CATEGORY_VAR_COL_LIST
        self.pro_training_data_file = cfg.PRO_TRA_DATA_FILE_NAME
        self.pro_test_data_file = cfg.PRO_TEST_DATA_FILE_NAME

    def load_data_to_df(self, data_file_name):
        """
        Public: Method to read the CSV file and load the data into a pandas dataframe.
        :param data_file_name: Name of the CSV file which contains the data.
        :return: A pandas dataframe object
        """
        input_data = pd.read_csv(data_file_name, encoding=self.encoding_format)
        return input_data

    def load_external_data_dict(self, external_data_file_name):
        """
        Public: Method to read the CSV file containing the external data to support data cleaning, into a python
        dictionary object.
        :param external_data_file_name: Name of the CSV file containing the data
        :return: A dictionary object
        """
        df_external_data = self.load_data_to_df(external_data_file_name)
        external_data_dict = dict(zip(df_external_data[df_external_data.columns[0]],
                                      df_external_data[df_external_data.columns[1]]))
        return external_data_dict

    def prepare_demographic_data(self, demographic_data_file):
        """
        Private: Method to load the demographic data and perform the first level of pre-processing (renaming of columns
        and drop duplicate rows) on the demographic data.
        :param demographic_data_file: Name of the CSV file containing the demographic data.
        :return df_demographics_data: A pandas dataframe object containing the pre-processed version of the demographic
        data.
        """
        df_demographics_data = self.load_data_to_df(demographic_data_file)
        dict_demographic_data_cols = {"Client ID": "ClientID",
                                      "Age": "Age",
                                      "Gender \n1: Female, 2: Male": "Gender",
                                      "County": "County",
                                      "Income Group": "IncomeGroup"}
        df_demographics_data = df_demographics_data.rename(columns=dict_demographic_data_cols)
        # Drop any row in the data frame that contains a duplicate value of Client ID.
        df_demographics_data.drop_duplicates("ClientID", inplace=True)
        return df_demographics_data

    def prepare_previous_loan_data(self, prev_loan_data_file):
        """
        Public: Method to load the previously loan held data into a pandas dataframe object and then perform the first
        level of pre-processing on the data (renaming of columns and drop duplicate rows).
        :param prev_loan_data_file: Name of the CSV file which contains the previous loan held data.
        :return A pandas dataframe containing the pre-processed previous loan held data.
        """
        df_prev_loan_data = self.load_data_to_df(prev_loan_data_file)
        dict_prev_loan_data_cols = {"Client ID": "ClientID",
                                    "Held Loan previously": "LoanHeldBefore"}
        df_prev_loan_data = df_prev_loan_data.rename(columns=dict_prev_loan_data_cols)
        # Drop any row in the data frame that contains a duplicate value of Client ID.
        df_prev_loan_data.drop_duplicates("ClientID", inplace=True)
        return df_prev_loan_data

    def prepare_prods_held_data(self, prods_held_data_file):
        """
        Public: Method to load the number of products held data into a pandas dataframe object and then perform the
        first level of pre-processing on the data (renaming of columns and drop duplicate rows).
        :param prods_held_data_file: Name of the CSV file which contains the number of products held data.
        :return A pandas dataframe containing the pre-processed number of products held data.
        """
        df_prods_held_data = self.load_data_to_df(prods_held_data_file)
        dict_prods_held_data_cols = {"Client ID": "ClientID",
                                     "# Products in bank": "NoOfProductsHeld"}
        df_prods_held_data = df_prods_held_data.rename(columns=dict_prods_held_data_cols)
        # Drop any row in the data frame that contains a duplicate value of Client ID.
        df_prods_held_data.drop_duplicates("ClientID", inplace=True)
        return df_prods_held_data

    def prepare_avg_txn_amt_data(self, avg_txn_amt_data_file):
        """
        Public: Method to load the average transaction amount data into a pandas dataframe object and then perform the
        first level of pre-processing on the data (renaming of columns and drop duplicate rows).
        :param avg_txn_amt_data_file: Name of the CSV file which contains average transaction amount data.
        :return A pandas dataframe containing the pre-processed average transaction amounts data.
        """
        df_avg_txn_amt_data = self.load_data_to_df(avg_txn_amt_data_file)
        dict_avg_txn_amt_data_cols = {"Client ID": "ClientID",
                                      "Average amount of CA transaction": "AvgTxnAmt"}
        df_avg_txn_amt_data = df_avg_txn_amt_data.rename(columns=dict_avg_txn_amt_data_cols)
        # Drop any row in the data frame that contains a duplicate value of Client ID.
        df_avg_txn_amt_data.drop_duplicates("ClientID", inplace=True)
        return df_avg_txn_amt_data

    def prepare_txn_details_data(self, txn_details_data_file):
        """
        Public: Method to load the transaction details data into a pandas dataframe object and then perform the first
        level of pre-processing on the data (renaming of columns and drop duplicate rows).
        :param txn_details_data_file: Name of the CSV file which contains transaction details data.
        :return A pandas dataframe containing the pre-processed transaction details data.
        """
        df_txn_details_data = self.load_data_to_df(txn_details_data_file)
        dict_txn_details_data_cols = {"Client": "ClientID",
                                      "Num Transactions": "NoOfTxns",
                                      "Last TXN Amount": "LastTxnAmt",
                                      "Merchant Code": "MerCode",
                                      "Last Transaction Narrative": "LastTxnNrtv"}
        df_txn_details_data = df_txn_details_data.rename(columns=dict_txn_details_data_cols)
        # Drop any row in the data frame that contains a duplicate value of Client ID.
        df_txn_details_data.drop_duplicates('ClientID', inplace=True)
        return df_txn_details_data

    def prepare_loan_flag_data(self, loan_flag_data_file):
        """
        Public: Method to load the loan flag data into a pandas dataframe object and then perform the first level of
        pre-processing on the data (renaming of columns and drop duplicate rows).
        :param loan_flag_data_file: Name of the CSV file which contains the loan flag data.
        :return A pandas dataframe containing the pre-processed loan flag data.
        """
        df_loan_flag_data = self.load_data_to_df(loan_flag_data_file)
        dict_loan_flag_data_cols = {"Client ID": "ClientID",
                                    "Loan Flag": "LoanFlag"}
        df_loan_flag_data = df_loan_flag_data.rename(columns=dict_loan_flag_data_cols)
        # Drop any row in the data frame that contains a duplicate value of Client ID.
        df_loan_flag_data.drop_duplicates("ClientID", inplace=True)
        return df_loan_flag_data

    def prepare_combined_data_frame_list(self, list_of_input_files):
        """
        Public: Method to generate a list of pandas dataframe objects by loading the data from each individual CSV file
        and applying the first level of pre-processing on them.
        :param list_of_input_files: A list containing the names of all CSV files containing the required data.
        :return A list containing all the pandas dataframe objects loaded with the data from CSV files.
        """
        data_frame_list = []

        # Load & Pre-Process Demographic Data
        demographic_data_file = list_of_input_files[0]
        df_demographics_data = self.prepare_demographic_data(demographic_data_file)
        data_frame_list.append(df_demographics_data)

        # Load & Pre-Process Previous Loan Held Data
        prev_loan_data_file = list_of_input_files[1]
        df_prev_loan_data = self.prepare_previous_loan_data(prev_loan_data_file)
        data_frame_list.append(df_prev_loan_data)

        # Load & Pre-Process Products Held Data
        prods_held_data_file = list_of_input_files[2]
        df_prods_held_data = self.prepare_prods_held_data(prods_held_data_file)
        data_frame_list.append(df_prods_held_data)

        # Load & Pre-Process Average Transaction Amount Data
        avg_txn_amt_data_file = list_of_input_files[3]
        df_avg_txn_amt_data = self.prepare_avg_txn_amt_data(avg_txn_amt_data_file)
        data_frame_list.append(df_avg_txn_amt_data)

        # Load & Pre-Process Transaction Details Data
        txn_details_data_file = list_of_input_files[4]
        df_txn_details_data = self.prepare_txn_details_data(txn_details_data_file)
        data_frame_list.append(df_txn_details_data)

        # Load & Pre-Process Loan Flag Data
        if len(list_of_input_files) == 6:
            if list_of_input_files[5] != "" and list_of_input_files[5] is not None:
                loan_flag_data_file = list_of_input_files[5]
                df_loan_flag_data = self.prepare_loan_flag_data(loan_flag_data_file)
                data_frame_list.append(df_loan_flag_data)

        return data_frame_list

    def combine_all_dataframes(self, data_frame_list):
        """
        Public: Method to merge all the pandas dataframe objects in the input list into a single one, based on
        the common column 'ClientID'.
        :param data_frame_list: A list containing all the pandas dataframe objects loaded with the data from CSV files.
        :return A merged pandas dataframe object containing the data from each individual dataframe object in the list.
        """
        df_unified_loan_data = reduce(lambda left, right: pd.merge(left, right, on='ClientID'), data_frame_list)
        return df_unified_loan_data

    def load_training_data(self):
        """
        Public: Method to generate a merged pandas dataframe object containing the data to train the model.
        :return A pandas dataframe object containing the training data.
        """
        training_data_frames_list = self.prepare_combined_data_frame_list(self.raw_training_data_file_list)
        df_training_data = self.combine_all_dataframes(training_data_frames_list)
        return df_training_data

    def load_testing_data(self):
        """
        Public: Method to generate a merged pandas dataframe object containing the data to test the model.
        :return A pandas dataframe object containing the testing data.
        """
        testing_data_frames_list = self.prepare_combined_data_frame_list(self.raw_test_data_file_list)
        df_testing_data = self.combine_all_dataframes(testing_data_frames_list)
        return df_testing_data

    def clean_age_values(self, df_loan_data):
        """
        Public: Method to clean the data within the 'Age' column in the pandas dataframe.
        :param df_loan_data: A pandas dataframe object containing the data.
        :return A pandas dataframe object containing the cleaned 'Age' data.
        """
        df_loan_data['Age'] = df_loan_data['Age'].astype(str)
        for index, row in df_loan_data.iterrows():
            if not row['Age'].isdigit():
                df_loan_data.loc[index, 'Age'] = ""
        return df_loan_data

    def clean_gender_values(self, df_loan_data):
        """
        Public: Method to clean the data within the 'Gender' column in the pandas dataframe.
        :param df_loan_data: A pandas dataframe object containing the data.
        :return A pandas dataframe object containing the cleaned 'Gender' data.
        """
        df_loan_data['Gender'] = df_loan_data['Gender'].astype(str)
        for index, row in df_loan_data.iterrows():
            if row['Gender'].strip().lower().startswith('f'):
                df_loan_data.loc[index, 'Gender'] = 0
            elif row['Gender'].strip().lower().startswith('m'):
                df_loan_data.loc[index, 'Gender'] = 1
            elif row['Gender'].strip() == '0':
                df_loan_data.loc[index, 'Gender'] = 0
            elif row['Gender'].strip() == '1':
                df_loan_data.loc[index, 'Gender'] = 1
            else:
                df_loan_data.loc[index, 'Gender'] = -1
        return df_loan_data

    def clean_income_category_values(self, df_loan_data):
        """
        Public: Method to clean the data within the 'Income Category' column in the pandas dataframe.
        :param df_loan_data: A pandas dataframe object containing the data.
        :return A pandas dataframe object containing the cleaned 'Income Category' data.
        """
        df_loan_data['IncomeGroup'] = df_loan_data['IncomeGroup'].astype(str)
        df_loan_data['IncomeGroup'] = df_loan_data['IncomeGroup'].str.replace('\\W+', '-')
        df_loan_data[['LowerLimit', 'UpperLimit']] = df_loan_data['IncomeGroup'].str.split('-', expand=True)
        df_loan_data['LowerLimit'] = pd.to_numeric(df_loan_data['LowerLimit'])
        df_loan_data['UpperLimit'] = pd.to_numeric(df_loan_data['UpperLimit'])

        income_category_conditions = [(df_loan_data['LowerLimit'] >= 0) & (df_loan_data['UpperLimit'] <= 10000),
                                (df_loan_data['LowerLimit'] >= 10001) & (df_loan_data['UpperLimit'] <= 40000),
                                (df_loan_data['LowerLimit'] >= 40001) & (df_loan_data['UpperLimit'] <= 60000),
                                (df_loan_data['LowerLimit'] >= 60001) & (df_loan_data['UpperLimit'] <= 100000),
                                (df_loan_data['LowerLimit'] > 100000)]
        income_category_values = ['Low', 'Lower Middle', 'Upper', 'Upper Middle', 'High']
        df_loan_data['IncomeCategory'] = np.select(income_category_conditions, income_category_values,
                                                   default='Lower Middle')
        df_loan_data['IncomeCategory'] = df_loan_data['IncomeCategory'].astype(
            CategoricalDtype(categories=income_category_values))
        df_loan_data = df_loan_data.drop(['IncomeGroup', 'LowerLimit', 'UpperLimit'], axis=1)
        return df_loan_data

    def clean_county_values(self, df_loan_data):
        """
        Public: Method to clean the data within the 'County' column in the pandas dataframe.
        :param df_loan_data: A pandas dataframe object containing the data.
        :return A pandas dataframe object containing the cleaned 'County' data.
        """
        county_town_data_dict = self.load_external_data_dict(self.ext_county_town_file)
        df_loan_data['County'] = df_loan_data['County'].astype(str)
        for index, row in df_loan_data.iterrows():
            if row['County'].isdigit():
                df_loan_data.loc[index, 'County'] = "Unknown"
            if row['County'].strip().lower() == "sandyford":
                df_loan_data.loc[index, 'County'] = "Dublin"
            elif 'dublin' in row['County'].strip().lower() or 'blin' in row['County'].strip().lower():
                df_loan_data.loc[index, 'County'] = "Dublin"
            elif 'cork' in row['County'].strip().lower():
                df_loan_data.loc[index, 'County'] = "Cork"
            elif 'kildare' in row['County'].strip().lower():
                df_loan_data.loc[index, 'County'] = "Kildare"
            elif 'galway' in row['County'].strip().lower():
                df_loan_data.loc[index, 'County'] = "Galway"
            elif row['County'].strip() in county_town_data_dict:
                df_loan_data.loc[index, 'County'] = county_town_data_dict[row['County'].strip()].split("/")[0].strip()
            elif row['County'].strip() not in set(list(county_town_data_dict.values())):
                df_loan_data.loc[index, 'County'] = "Outside ROI"
            elif row['County'].strip() is None or row['County'].strip() == "":
                df_loan_data.loc[index, 'County'] = "Unknown"
        df_loan_data['County'] = df_loan_data['County'].str.replace(".", "")
        df_loan_data['County'] = df_loan_data['County'].str.replace("Co ", "")
        df_loan_data['County'] = df_loan_data['County'].str.replace("co ", "")
        df_loan_data['County'] = df_loan_data['County'].str.replace("County ", "")
        return df_loan_data

    def clean_loan_held_before_values(self, df_loan_data):
        """
        Public: Method to clean the data within the 'LoanHeldBefore' column in the pandas dataframe.
        :param df_loan_data: A pandas dataframe object containing the data.
        :return A pandas dataframe object containing the cleaned 'LoanHeldBefore' data.
        """
        df_loan_data['LoanHeldBefore'] = df_loan_data['LoanHeldBefore'].astype(str)
        for index, row in df_loan_data.iterrows():
            if row['LoanHeldBefore'] != '0' and row['LoanHeldBefore'] != '1':
                df_loan_data.loc[index, 'LoanHeldBefore'] = -1
        return df_loan_data

    def clean_prods_held_values(self, df_loan_data):
        """
        Public: Method to clean the data within the 'NoOfProductsHeld' column in the pandas dataframe.
        :param df_loan_data: A pandas dataframe object containing the data.
        :return A pandas dataframe object containing the cleaned 'NoOfProductsHeld' data.
        """
        df_loan_data['NoOfProductsHeld'] = df_loan_data['NoOfProductsHeld'].astype(str)
        for index, row in df_loan_data.iterrows():
            if not row['NoOfProductsHeld'].isdigit():
                df_loan_data.loc[index, 'NoOfProductsHeld'] = 0
            else:
                if int(row['NoOfProductsHeld']) < 0:
                    df_loan_data.loc[index, 'NoOfProductsHeld'] = 0
        return df_loan_data

    def clean_avg_txt_amt_values(self, df_loan_data):
        """
        Public: Method to clean the data within the 'AvgTxnAmt' column in the pandas dataframe.
        :param df_loan_data: A pandas dataframe object containing the data.
        :return A pandas dataframe object containing the cleaned 'AvgTxnAmt' data.
        """
        df_loan_data['AvgTxnAmt'] = df_loan_data['AvgTxnAmt'].astype(str)
        for index, row in df_loan_data.iterrows():
            temp_str = ""
            for ch in row['AvgTxnAmt']:
                if 48 <= ord(ch) <= 57:     # Handling Control Characters appearing in values
                    temp_str += ch
            df_loan_data.loc[index, 'AvgTxnAmt'] = temp_str
        return df_loan_data

    def clean_txn_details_values(self, df_loan_data):
        """
        Public: Method to clean the data within the 'MerCode' and 'LastTxnNrtv' columns in the pandas dataframe.
        :param df_loan_data: A pandas dataframe object containing the data.
        :return A pandas dataframe object containing the cleaned 'MerCode' and 'LastTxnNrtv' data.
        """
        merchant_category_data_dict = self.load_external_data_dict(self.ext_merchant_category_file)
        merchant_category_data_dict[0] = "Unknown"      # Appending the value for missing merchant categories
        df_loan_data['MerCode'] = df_loan_data['MerCode'].fillna(0).astype(np.int64)
        df_loan_data['MerCategory'] = df_loan_data['MerCode'].map(merchant_category_data_dict)
        df_loan_data.drop(columns=['MerCode', 'LastTxnNrtv'], inplace=True)

        return df_loan_data

    def restore_valid_col_dtypes(self, df_loan_data):
        """
        Public: Method to restore the column dtypes in the pandas dataframe (as they were converted to 'str' earlier).
        :param df_loan_data: A pandas dataframe object containing the data merged from the CSV files.
        :return A pandas dataframe object containing all the required columns in cleaned format.
        """
        df_col_list = df_loan_data.columns
        for col in self.integer_var_col_list:
            df_loan_data[col] = df_loan_data[col].astype(int)

        for col in self.float_var_col_list:
            df_loan_data[col] = df_loan_data[col].astype(float)

        for col in self.category_var_col_list:
            if col in df_col_list:
                df_loan_data[col] = df_loan_data[col].astype(object)

        # if 'LoanFlag' in df_loan_data.columns:
        #     df_loan_data['LoanFlag'] = df_loan_data['LoanFlag'].astype(object)
        #     # Pushing the LoanFlag (target variable) column to the end of the dataframe
        #     cols = list(df_loan_data.columns)
        #     a, b = cols.index('LoanFlag'), cols.index('MerCategory')
        #     cols[b], cols[a] = cols[a], cols[b]
        #     df_loan_data = df_loan_data[cols]
        return df_loan_data

    def process_input_data(self, df_loan_data):
        """
        Public: Method to clean the input data within the columns in the pandas dataframe.
        :param df_loan_data: A pandas dataframe object containing the data merged from the CSV files.
        :return A pandas dataframe object containing all the required columns in cleaned format.
        """
        df_loan_data = self.clean_age_values(df_loan_data)
        df_loan_data = self.clean_gender_values(df_loan_data)
        df_loan_data = self.clean_income_category_values(df_loan_data)
        df_loan_data = self.clean_county_values(df_loan_data)
        df_loan_data = self.clean_loan_held_before_values(df_loan_data)
        df_loan_data = self.clean_prods_held_values(df_loan_data)
        df_loan_data = self.clean_avg_txt_amt_values(df_loan_data)
        df_loan_data = self.clean_txn_details_values(df_loan_data)
        df_loan_data = self.restore_valid_col_dtypes(df_loan_data)
        return df_loan_data

    def execution_package(self):
        """
        Public: Method to clean the input data within the columns in the pandas dataframe.
        :return A boolean flag indicating whether the cleaned data files were generated or not.
        """
        exec_flag = False
        df_training_data = self.load_training_data()
        processed_training_data = self.process_input_data(df_training_data)
        df_testing_data = self.load_testing_data()
        processed_testing_data = self.process_input_data(df_testing_data)

        tra_data_write_result = processed_training_data.to_csv(self.pro_training_data_file, index=False)
        test_data_write_result = processed_testing_data.to_csv(self.pro_test_data_file, index=False)
        if tra_data_write_result is None and test_data_write_result is None:
            exec_flag = True
        return exec_flag


obj_data_cleaner = LoanUptakeRatePredictionDataProcessor()
success_flag = obj_data_cleaner.execution_package()
if success_flag:
    print("Successfully generated cleaned data files for Training & Testing sets.")
else:
    print("Files couldn't be generated.")
