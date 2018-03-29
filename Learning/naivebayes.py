from pyspark.mllib.classification import NaiveBayes, NaiveBayesModel
from pyspark.mllib.util import MLUtils

def NaiveBayes(datafile):
    """
        Naive Bayes implementation on an apprentissage test
        using Apache Spark Framework.

        Apache Spark API for Naive Bayes Implementation :
            https://spark.apache.org/docs/latest/mllib-naive-bayes.html
    """

    # Load and parse the data file.
    data = MLUtils.loadLibSVMFile(sc, datafile)

    # Split data approximately into training (60%) and test (40%)
    training, test = data.randomSplit([0.6, 0.4])

    # Train a naive Bayes model.
    model = NaiveBayes.train(training, 1.0)

    # Make prediction and test accuracy.
    predictionAndLabel = test.map(lambda p: (model.predict(p.features), p.label))
    accuracy = 1.0 * predictionAndLabel.filter(lambda pl: pl[0] == pl[1]).count() / test.count()
    print('model accuracy {}'.format(accuracy))

    # Save and load model
    output_dir = 'target/tmp/myNaiveBayesModel'
    shutil.rmtree(output_dir, ignore_errors=True)
    model.save(sc, output_dir)
    sameModel = NaiveBayesModel.load(sc, output_dir)
    predictionAndLabel = test.map(lambda p: (sameModel.predict(p.features), p.label))
    accuracy = 1.0 * predictionAndLabel.filter(lambda pl: pl[0] == pl[1]).count() / test.count()
    print('sameModel accuracy {}'.format(accuracy))
