# Config File for LoanUptakeRatePredictionDataProcessor

RAW_DATA_DIR = "../data/raw/"
RAW_TRAIN_DATA_DIR = RAW_DATA_DIR + "train/"
RAW_TEST_DATA_DIR = RAW_DATA_DIR + "test/"

PROCESSED_DATA_DIR = "../data/processed/"
PROCESSED_TRAIN_DATA_DIR = PROCESSED_DATA_DIR + "train/"
PROCESSED_TEST_DATA_DIR = PROCESSED_DATA_DIR + "test/"
PRO_TRA_DATA_FILE_NAME = PROCESSED_TRAIN_DATA_DIR + "Processed_Training_Data.csv"
PRO_TEST_DATA_FILE_NAME = PROCESSED_TEST_DATA_DIR + "Processed_Testing_Data.csv"

EXTERNAL_DATA_DIR = "../data/external/"
EXT_COUNTY_TOWN_DATA_FILE = EXTERNAL_DATA_DIR + "Towns And Counties.csv"
EXT_MERCHANT_CATEGORY_DATA_FILE = EXTERNAL_DATA_DIR + "MerchantCode_Category.csv"

PREDICTED_DATA_DIR = "../data/predicted/"
PRE_LOAN_LIKELIHOOD_FILE = PREDICTED_DATA_DIR + "Predicted_Loan_Likelihoods.csv"

ENCODING_FORMAT = "ISO-8859-1"

# Config Variables for Raw Data
RAW_TRA_DEMOGRAPHIC_DATA_FILE = RAW_TRAIN_DATA_DIR + "Model Build - Demographics.csv"
RAW_TRA_PREVIOUS_LOAN_DATA_FILE = RAW_TRAIN_DATA_DIR + "Model Build - Previous Loan Holdings.csv"
RAW_TRA_PRODUCTS_HELD_DATA_FILE = RAW_TRAIN_DATA_DIR + "Model Build - Product Held in Bank.csv"
RAW_TRA_TXN_DETAILS_DATA_FILE = RAW_TRAIN_DATA_DIR + "Model Build - Transactions out of Current Account.csv"
RAW_TRA_AVG_TXN_AMOUNT_DATA_FILE = RAW_TRAIN_DATA_DIR + "Model Build - TXN Amount.csv"
RAW_TRA_TARGET_VARIABLE_DATA_FILE = RAW_TRAIN_DATA_DIR + "Target Variable - Purchased Loan Flag.csv"
RAW_TEST_DEMOGRAPHIC_DATA_FILE = RAW_TEST_DATA_DIR + "TEST - Demographics.csv"
RAW_TEST_PREVIOUS_LOAN_DATA_FILE = RAW_TEST_DATA_DIR + "TEST- Previous Loan Holdings.csv"
RAW_TEST_PRODUCTS_HELD_DATA_FILE = RAW_TEST_DATA_DIR + "TEST - Product Held in Bank.csv"
RAW_TEST_TXN_DETAILS_DATA_FILE = RAW_TEST_DATA_DIR + "TEST - Transactions out of Current Account.csv"
RAW_TEST_AVG_TXN_AMOUNT_DATA_FILE = RAW_TEST_DATA_DIR + "TEST - TXN Amount.csv"

RAW_TRAINING_DATA_FILE_LIST = [RAW_TRA_DEMOGRAPHIC_DATA_FILE, RAW_TRA_PREVIOUS_LOAN_DATA_FILE,
                               RAW_TRA_PRODUCTS_HELD_DATA_FILE, RAW_TRA_AVG_TXN_AMOUNT_DATA_FILE,
                               RAW_TRA_TXN_DETAILS_DATA_FILE, RAW_TRA_TARGET_VARIABLE_DATA_FILE]
RAW_TEST_DATA_FILE_LIST = [RAW_TEST_DEMOGRAPHIC_DATA_FILE, RAW_TEST_PREVIOUS_LOAN_DATA_FILE,
                           RAW_TEST_PRODUCTS_HELD_DATA_FILE, RAW_TEST_AVG_TXN_AMOUNT_DATA_FILE,
                           RAW_TEST_TXN_DETAILS_DATA_FILE]

INTEGER_VAR_COL_LIST = ['Age', 'NoOfProductsHeld', 'NoOfTxns']
FLOAT_VAR_COL_LIST = ['LastTxnAmt', 'AvgTxnAmt']
CATEGORY_VAR_COL_LIST = ['Gender', 'County', 'LoanHeldBefore', 'MerCategory', 'IncomeCategory']
