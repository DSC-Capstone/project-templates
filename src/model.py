
import pandas as pd

from sklearn.model_selection import train_test_split

import tensorflow
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense, BatchNormalization, Conv1D, Flatten, Lambda
import tensorflow.keras.backend as K


def model_build(
        features,
        tag,
        predictions_fp,
        mdl_fp,
        test_size,
        nodes_in_first_layer,
        nodes_in_second_layer,
        nodes_in_third_layer,
        activation_first_layer,
        activation_second_layer,
        activation_third_layer,
        activation_output_layer,
        optimizer,
        loss,
        batch_size,
        epochs,
        **params):

        X_train, X_test, y_train, y_test = train_test_split(
            features, tag, test_size=test_size)


        # define dense keras model
        inputs = Input(shape=(2,), name = 'input')  
        x = BatchNormalization(name='bn_1')(inputs)
        x = Flatten(name='flatten_1')(x)
        x = Dense(nodes_in_first_layer, name = 'dense_1', activation=activation_first_layer)(x)
        x = Dense(nodes_in_second_layer, name = 'dense_2', activation=activation_second_layer)(x)
        x = Dense(nodes_in_third_layer, name = 'dense_3', activation=activation_third_layer)(x)
        outputs = Dense(1, name = 'output', activation=activation_output_layer)(x)
        keras_model_dense = Model(inputs=inputs, outputs=outputs)
        keras_model_dense.compile(optimizer=optimizer, loss=loss, metrics=['accuracy'])

        # fit keras model
        keras_model_dense.fit(X_train, y_train, batch_size=batch_size, epochs=epochs)
        
        # save keras model        
        keras_model_dense.save(mdl_fp)

        predictions = keras_model_dense.predict(X_test)
        dataset = pd.DataFrame({'Predictions': predictions[:, 0]})
        
        # creates an output file containing predictions of the test data
        out = y_test
        out['Predictions'] = dataset.values
        out.to_csv(predictions_fp)
        
        return out



