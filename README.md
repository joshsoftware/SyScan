The model - SyScan - which is based on Neural Networks (Machine Learning) will be used to identify and correct syntax errors in Python Code.
SyScan will be a part of SparKode and will be used in placement drives for evaluating the source codes written by the candidates.
It aims at reducing the manual effort required for correcting the syntactical part of the code.

PURPOSE:
The main purpose is to correct the syntactic errors in Python code using Machine Learning.
The system is given code snippets and a CHECKER C (code analyzer or compiler) that returns whether an input is good or bad. 
Using the CHECKER C, examples in data can be classified into bad (0) and good ones (1). 
Our task is to learn a CORRECTOR that maps a bad example into a good example such that it is close to a syntactically correct Python code.



BRIEF DESCRIPTION:

There are 3 major parts of the model proposed - the CHECKER, CORRECTOR and CODE_CORRUPTER.

The CHECKER is either a code analyzer or an interpreter. In our case the interpreter is considered as the checker and it is used to check whether the code contains any errors or not and classify the code as good (1) or bad (0). 
This is required to check whether the right type of code is being provided to the corrector and code_corruptoer for further processing.

The CORRECTOR is trained using the good and bad pair of Python codes initially and is used to produce the syntactically correct code as an output when a certain erroneous code is given as an input.

The CODE_CORRUPTER is used for the generation of erroneous code similar to that of the real world errors in the Python code contrary to the synthetically generated bad code. 
The output of the corrector is provided as input to the code_corrupter. 
This is the main task which aims at enhancing the accuracy of the model to the highest extent possible.
