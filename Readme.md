
## How to run LDTR on your own system?

1. Clone this repo onto your local machine.
2. You have first install Build Tools for Visual Studio 2019 from https://visualstudio.microsoft.com/downloads/
3. Next you have to build the package. Run the following command:
    ```sh
    python run_file.py
    ```
4. It might take few minutes to build. Once it is built, just try importing the following library and see if it works:
    ```sh
    from sklearn.tree import LinearDecisionTreeRegressor as LDTR
    ```
5. If this works, you have successfully built the package and now you are ready to try out LDTR. 
6. For more details and any errors follow this link: https://scikit-learn.org/stable/developers/advanced_installation.html. 
   This is the official guide on how to build the package.
7. To test the code try one of the following file: test_0.2.ipynb, test_0.3.ipynb