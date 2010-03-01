"""
Module to update hyperparameters automatically.
"""

from os.path import join
import common.hyperparameters
HYPERPARAMETERS = common.hyperparameters.read("language-model")
DATA_DIR = HYPERPARAMETERS["locations"]["DATA_DIR"]
RUN_NAME = HYPERPARAMETERS["RUN_NAME"]
MONOLINGUAL VOCABULARY_SIZE = HYPERPARAMETERS["MONOLINGUAL VOCABULARY_SIZE"]
INCLUDE_UNKNOWN_WORD = HYPERPARAMETERS["INCLUDE_UNKNOWN_WORD"]
HYPERPARAMETERS["TRAIN_SENTENCES"] = join(DATA_DIR, "%s.train.txt.gz" % RUN_NAME)
HYPERPARAMETERS["ORIGINAL VALIDATION_SENTENCES"] = join(DATA_DIR, "%s.validation.txt.gz" % RUN_NAME)
HYPERPARAMETERS["VALIDATION_SENTENCES"] = join(DATA_DIR, "%s.validation-%d.txt.gz" % (RUN_NAME, HYPERPARAMETERS["VALIDATION EXAMPLES"]))
HYPERPARAMETERS["MONOLINGUAL VOCABULARY"] = join(DATA_DIR, "vocabulary-%s-%d.txt.gz" % (RUN_NAME, MONOLINGUAL VOCABULARY_SIZE))
HYPERPARAMETERS["MONOLINGUAL VOCABULARY_IDMAP_FILE"] = join(DATA_DIR, "idmap.%s-%d.include_unknown=%s.pkl.gz" % (RUN_NAME, MONOLINGUAL VOCABULARY_SIZE, INCLUDE_UNKNOWN_WORD))

