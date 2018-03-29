

from pyspark.mllib.classification import LogisticRegressionWithLBFGS, LogisticRegressionModel
from pyspark.mllib.regression import LabeledPoint

def parsePoint(line):
    """
        Load and parse the data

        Source :
            https://spark.apache.org/docs/latest/mllib-linear-methods.html#classification
    """
    values = [float(x) for x in line.split(' ')]
    return LabeledPoint(values[0], values[1:])


def logisticRegression(datafile):
    """
        Logistic Regression implementation on an
        apprentissage dataset using Apache Spark Framework.

        Apache Spark API for Logistic Regression Implementation :
            https://spark.apache.org/docs/latest/mllib-linear-methods.html#classification
    """
    data = sc.textFile(datafile)
    parsedData = data.map(parsePoint)

    # Build the model
    model = LogisticRegressionWithLBFGS.train(parsedData)

    # Evaluating the model on training data
    labelsAndPreds = parsedData.map(lambda p: (p.label, model.predict(p.features)))
    trainErr = labelsAndPreds.filter(lambda lp: lp[0] != lp[1]).count() / float(parsedData.count())
    print("Training Error = " + str(trainErr))

    # Save and load model
    model.save(sc, "target/tmp/pythonLogisticRegressionWithLBFGSModel")
    sameModel = LogisticRegressionModel.load(sc,"target/tmp/pythonLogisticRegressionWithLBFGSModel")
