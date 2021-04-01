# loan_likelihood_prediction
A classification model to predict the Loan Uptake Percentage


##########################################
										 #
SK_Loan_Likelihood_Prediction - ReadMe   #
										 #
##########################################


Project Folder Structure:
--------------------------

SK_Loan_Likelihood_Prediction
├── ReadMe.txt
├── code
│   ├── LoanUptakeRatePredictionDataProcessor.py
│   ├── __pycache__
│   │   └── config.cpython-37.pyc
│   └── config.py
├── data
│   ├── external
│   │   ├── MerchantCode_Category.csv
│   │   └── Towns\ And\ Counties.csv
│   ├── predicted
│   │   └── Predicted_Loan_Likelihoods.csv
│   ├── processed
│   │   ├── test
│   │   │   └── Processed_Testing_Data.csv
│   │   └── train
│   │       └── Processed_Training_Data.csv
│   └── raw
│       ├── test
│       │   ├── TEST\ -\ Demographics.csv
│       │   ├── TEST\ -\ Product\ Held\ in\ Bank.csv
│       │   ├── TEST\ -\ TXN\ Amount.csv
│       │   ├── TEST\ -\ Transactions\ out\ of\ Current\ Account.csv
│       │   └── TEST-\ Previous\ Loan\ Holdings.csv
│       └── train
│           ├── Model\ Build\ -\ Demographics.csv
│           ├── Model\ Build\ -\ Previous\ Loan\ Holdings.csv
│           ├── Model\ Build\ -\ Product\ Held\ in\ Bank.csv
│           ├── Model\ Build\ -\ TXN\ Amount.csv
│           ├── Model\ Build\ -\ Transactions\ out\ of\ Current\ Account.csv
│           └── Target\ Variable\ -\ Purchased\ Loan\ Flag.csv
├── eda
│   ├── Customers_per_County.png
│   ├── Customers_per_IncomeCategory.png
│   ├── Customers_per_LoanLikelihoodCategory.png
│   ├── ProductsPerAgeGroup.png
│   └── TxnsBasedOnAgeAndIncome.png
├── notebooks
│   └── LoanUptakeRatePrediction.ipynb
└── resources
    ├── Case\ Study\ v3.0.docx
    ├── SK_Loan_Likelihood_Prediction_Presentation.pdf
    └── SK_Loan_Likelihood_Prediction_Presentation.pptx


Part 1: Data Wrangling
------------------------

	1) Navigate to the directory /code/.
	2) Open a terminal and execute the command 'python LoanUptakeRatePredictionDataProcessor.py'.
	3) Processed data files would be generated under the directories /data/processed/train/ and /data/processed/test/.


Part 2: Business Intelligence and Model Building
--------------------------------------------------

	1) Navigate to the directory /notebooks/.
	2) Open the jupyter notebook LoanUptakeRatePrediction.ipynb.
	3) The entire process followed during model building are explained step by step here.


Use Case Presentation:
------------------------
	- The powerpoint presentation 'SK_Loan_Likelihood_Prediction_Presentation.pptx', present inside the directory /resources/, details the steps and processes undertaken to achieve the results.
	- A PDF version of the same is placed in the directory /resources/.

