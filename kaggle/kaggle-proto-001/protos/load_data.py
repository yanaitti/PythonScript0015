import pandas as pd
import numpy as np

from logging import getLogger

TRAIN_DATA = '../input/train.csv'
TEST_DATA = '../input/test.csv'

logger = getLogger(__name__)

def read_csv(filename):
    logger.info(filename)
    df = pd.read_csv(filename)

    return df

def load_train_data():
    logger.info('enter')
    df = read_csv(TRAIN_DATA)
    logger.info('end')
    return df

def load_test_data():
    logger.info('enter')
    df = read_csv(TEST_DATA)
    logger.info('end')
    return df

if __name__ == '__main__':
    print(load_train_data().head())
    print(load_test_data().head())
