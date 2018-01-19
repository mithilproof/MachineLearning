import tensorflow as tf 
import pandas as pd 

TRAIN_URL = "http://download.tensorflow.org/data/iris_training.csv"
TEST_URL = "http://download.tensorflow.org/data/iris_test.csv"

CSV_COLUMN_NAMES = ['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Species']

SPECIES = ['Sentosa', 'Versicolor', 'Virginica']

def maybe_download():
	train_path = tf.keras.utils.get_file(TRAIN_URL.split('/')[-1], TRAIN_URL)
	test_path = tf.keras.utils.get_file(TEST_URL.split('/')[-1], TEST_URL)

	return test_path, train_path

def load_data(y_names='Species'):
	"""This will return the iris dataset (train_x, train_y), (test_x, test_y)"""
	train_path, test_path = maybe_download()

	train = pd.read_csv(train_path, names=CSV_COLUMN_NAMES, header=0)
	train_x, train_y = train, train.pop(y_name)

	test = pd.read_csv(test_path, names=CSV_COLUMN_NAMES, header=0)
	test_x, test_y = test, test.pop(y_name)

	return (train_x, train_y), (test_x, test_y)

def train_input_fun(features, lables, batch_size):
	""" This is an input function for training """
	""" This converts an input to the dataset """	
	dataset = tf.data.Dataset.from_tensor_slices((dict(features), lables))
	# shuffle, repeat and batch the examples.
	dataset = dataset.shuffle(1000).repeat().batch(batch_size)

	# return the read end of the pipeline 
	return dataset.make_one_shot_iterator().get_next()


def eval_input_fun(features, lables, batch_size):
	""" An input function for evalution or prediction """
	features = dict(features)
	if lables is None:
		inputs = features 

	else:
		inputs = (features, lables)	

	# convert input to dataset
	dataset = tf.data.Dataset.from_tensor_slices(inputs)

	# Batch the example
	assert batch_size is not None, 
	dataset = dataset.batch(batch_size)

	# return the read end of the pipeline
	return dataset.make_one_shot_iterator().get_next()


CSV_TYPES = [[0,0], [0,0], [0,0], [0,0], [0]]

def _parse_line(line):
    # Decode the line into its fields
    fields = tf.decode_csv(line, record_defaults=CSV_TYPES)

    # Pack the result into a dictionary
    features = dict(zip(CSV_COLUMN_NAMES, fields))

    # Separate the label from the features
    label = features.pop('Species')

    return features, label


def csv_input_fn(csv_path, batch_size):
    # Create a dataset containing the text lines.
    dataset = tf.data.TextLineDataset(csv_path).skip(1)

    # Parse each line.
    dataset = dataset.map(_parse_line)

    # Shuffle, repeat, and batch the examples.
    dataset = dataset.shuffle(1000).repeat().batch(batch_size)

    # Return the read end of the pipeline.
return dataset.make_one_shot_iterator().get_next()































