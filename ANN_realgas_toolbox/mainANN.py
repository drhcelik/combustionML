# to play with the ANN toolbox

from ANN_realgas_toolbox import ANN_realgas_toolbox

ANN = ANN_realgas_toolbox()

ANN.genTrainData(nT=300, T_min=80, T_max=160, nP=100, P_min=1, P_max=2)
#P_min/P_max is factor of critical pressure p_c
# nr_Training_data = nT * nP -> randomly selected T-p pairs

ANN.setTestPoints(random=False)

# set up the Sequential ANN
ANN.setSequential(hiddenLayer=1,n_neurons=100,loss='mse', optimizer='adam',)  # 5 hidden layer, loss='mse' 'mean_squared_logarithmic_error'

#set up the Resnet ANN
#ANN.setResnet()

ANN.fitModel(batch_size=1000, epochs=400)
ANN.predict()
ANN.plotPredict()
ANN.plotLoss()
