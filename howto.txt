1. Generate Ising configuration by running MC_2DIsing_model_v1.ipynb.

2. Two categories of output are produced: (i) MC_2DIsing.txt and (ii) numbered directories in data/, e.g., data/0.1/, data/0.2/, data/0.3/, ..., where the number signifies 'temperature' at which the *.dat files were generated.


Step 3, 4, 5 below are optional
===============================

3. Use visualise_MC_2DIsing_record.ipynb for visualising MC_2DIsing.txt.

4. Use visualise_config.ipynb for visualising the Ising configurations in all folders in data/*

5. Use gen_spinconfig_png to convert all *.dat files in data/ into *.png. You can then view the configurations in the form of individual *.png file. However, tThis procedure is optional and not necessaary because (i) machine learning will only require data in numerical form (*.npy) instead of *.png, and (ii) you can use step 7 for visualising the configuration instead. 

6. With the condition that *.dat files in the directory data/ are already generated, run convert_dat_to_npy.ipynb to convert all *.dat files in data/ into a single file named data.npy plus another file data_y.npy. 

7. Use visualise_npy.ipynb for visualing the Ising configurations data.npy generated in step 6. If you this step for visualing the Ising configuration, you would not need to use step 4.

8. The file data.npy contains the input data of configurations while data_y.npy the corresponding phase for the configuration in data.npy. In other words, data_y.npy contains the labels of the 'classes' for each of the configurations in data.npy. 

9. With the existance of data.npy, data_y.npy in current directory, run training.ipynb to train the CNN model using data.npy, data_y.npy, and to verify the trained model using data_to_verify/aaibb.dat. The trained model is saved in the folder 'saved_model/2DIsing'.


10. Run gen_data_only.ipynb to generate many data file in the form of data_to_verify/aaibb.dat, where aa is float indicating temperature, while bb is integer that index the data file. These files, data_to_verify/aaibb.dat, will be used as data for verifying the trainned CNN. 

11. Run load_model.ipynb to verify the model with data_to_verify/aaibb.dat and check the accuracy of the model's prediction.

