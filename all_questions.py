# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "no"
    answers["(b)"] = "no"
    answers["(c)"] = "yes"
    answers["(d)"] = "yes"

    # explain-string: explanation in english prose
    answers["(a) explain"] = "The rules cover different combinations of attributes, and some can overlap. For example, Rule 3 and Rule 4 both apply to people with low income and employment, predicting them as default borrowers."
    answers["(b) explain"] = "Not all combinations of attributes are covered by the rules. For instance, there's no rule for a divorced non-homeowner."
    answers["(c) explain"] = "Without ordering, it's unclear which rule should come first. For example, a person with low income and no homeownership triggers both Rule 1 and Rule 2."
    answers["(d) explain"] = "Because the rule set isn't complete, we need a default class for instances not covered by any rule. Sometimes no rule applies, and the default class predicts the outcome."

return answers


# -----------------------------------------------------------
"""
def question2():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = None
    answers["(b)"] = None
    answers["(c)"] = None
    answers["(d)"] = None

    # explain_string: explanation in english prose
    answers["(a) explain"] = None
    answers["(b) explain"] = None
    answers["(c) explain"] = None
    answers["(d) explain"] = None

    return answers
"""
# -----------------------------------------------------------
def question3():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "yes"
    answers["(b)"] = "no"
    answers["(c)"] = "yes"

    # explain-string: explanation in english prose
    answers["(a) example"] = "Each data instance seems to satisfy only one rule from the given set, indicating that the rules are mutually exclusive."
    answers["(b) example"] = "Instances of frogs and salamanders in the dataset belong to the amphibians class, yet there's no specific rule classifying them as amphibians, indicating that the rules are not exhaustive."
    answers["(c) example"] = "In the dataset, a penguin is classified as a bird. However, if rules are applied in the order {R1, R2, R3, R4}, the penguin would incorrectly be classified as a mammal based on rule R3. Thus, the order of rule application can influence classification outcomes, despite the rules being mutually exclusive."

return answers
# -----------------------------------------------------------
def question7():
    answers = {}

    # bool: True/False
    answers["(a)"] = True
    answers["(b)"] = True
    answers["(c)"] = False
    answers["(d)"] = True

    # explain_string: explanation in english prose
    answers["(a) explain"] = "The backpropagation algorithm functions by propagating the error from the output layer back through the hidden layers to the input layer. During this process, the gradients of the weights at each layer are computed and used to update the weights of the connections between layers. The weights at the (k+1)th layer can be computed using the gradient weights at the kth layer."
    answers["(b) explain"] = "This principle underlies the forward propagation step in neural networks. It involves utilizing the activations (outputs) of nodes in one layer to compute the activations (outputs) of nodes in the next layer."
    answers["(c) explain"] = "The vanishing gradient problem occurs when gradients used to update weights become exceedingly small as they propagate backward through the layers. This phenomenon does not necessarily cause the training error to diminish to zero but rather results in very slow network training."
    answers["(d) explain"] = "Gradients computed by backpropagation represent the rate of change of the loss function with respect to model weights. These gradients are employed by optimization algorithms to update weights and minimize loss. If the loss function reaches the global minimum for a set of weights, the ANN model perfectly classifies the training instances at that iteration. In this case, gradients of the loss with respect to weights at all layers will be zero."

return answers

# -----------------------------------------------------------
def question8():
    answers = {}

    # float
    answers["(a) P(X_1=1)"] = 0.65
    answers["(a) P(X_2=1)"] = 0.41
    answers["(a) P(X_1=1,X_2=1)"] = 0.28

    # string: "dependent" or "independent"
    answers["(a) Relationship between X_1 and X_2"] = "dependent"

    # string: "yes" or "no"
    answers["(b) X_1 and X_2 conditionally independent given the class?"] = "yes"

    # float
    answers["(c) P(X_1=1 | +)"] = 0.8
    answers["(c) P(X_1=1 | -)"] = 0.5
    answers["(c) P(X_2=1 | +)"] = 0.5
    answers["(c) P(X_2=1 | -)"] = 0.32
    answers["(c) P(X_3=1 | +)"] = 0.4
    answers["(c) P(X_3=1 | -)"] = 0.16

    # For each row give the class predicted by the model after training using Naive Bayes
    # String: either '+' or '-'
    answers["(d) Row 1"] = '+'
    answers["(d) Row 2"] = '-'
    answers["(d) Row 3"] = '-'
    answers["(d) Row 4"] = '-'

    # float between 0 and 1
    answers["(d) Training error rate"] = 0.25

    return answers

# --------------------------------------------------------
def question9():
    answers = {}

    # int
    answers["(a) K"] = 5
    answers["(b) K"] = 50

    # explain_string
    answers["(a) explain"] = "A smaller K value, such as 5, is preferred when data points from different classes are distinct yet close together. This choice enables the classifier to discern subtle differences between classes without being unduly swayed by distant points, achieving a balance between sensitivity and noise reduction."
    answers["(b) explain"] = "A higher K value is suitable when there is significant overlap between classes or when class boundaries are unclear. It contributes to smoothing the decision boundary and reducing the impact of noise, resulting in a more generalized model that performs better in situations with overlapped or mixed distributions."

return answers

# --------------------------------------------------------
def question10():
    answers = {}

    # float
    answers["(a) P(A=1|+)"] = 0.6
    answers["(a) P(B=1|+)"] = 0.5
    answers["(a) P(C=1|+)"] = 0.8
    answers["(a) P(A=1|-)"] = 0.4
    answers["(a) P(B=1|-)"] = 0.5
    answers["(a) P(C=1|-)"] = 0.2

    # type: explanatory string
    answers["(a) P(A=1|+) explain your answer"] = "In this scenario, there are 5 instances where A = 1. Among these instances, 3 belong to the positive class (A = 1 and Class = +). Therefore, to calculate the probability P(A=1|+), we divide the number of positive class instances by the total number of instances where A = 1."
  
    # type: float
    # note: R is the sample (A=1,B=1,C=1)
    answers["(b) P(+|R)"] = 0.12
    answers["(b) P(R|+)"] = 0.24
    answers["(b) P(R|-)"] = 0.04

    # string, '+' or '-'
    answers["(b) class label"] = '+'

    # explain_string
    answers["(b) Explain your reasoning"] = "Applying the Bayesian Formula involves computing posterior probabilities for each class, then multiplying the conditional probability for each feature given in the class by the prior class probability. By comparing the posterior probabilities, specifically P(+|R) and P(-|R),  the class with the highest value is selected. In this case, with P(+|R) = 0.12 and P(-|R) = 0.02, as P(+|R) surpasses P(-|R)the Naive Bayes classifier opts for predicting the positive class."
  
    # float
    answers["(c) P(A=1)"] = 0.5
    answers["(c) P(B=1)"] = 0.4
    answers["(c) P(A=1,B=1)"] = 0.2

    # type: string, 'yes' or 'no'
    answers["(c) A independent of B?"] = 'yes'
  
    # type: float
    answers["(d) P(A=1)"] = 0.5
    answers["(d) P(B=0)"] = 0.6
    answers["(d) P(A=1,B=0)"] = 0.3

    # type: string: 'yes' or 'no'
    answers["(d) A independent of B?"] = 'yes'
  
    # type: float
    answers["(e) P(A=1,B=1|+)"] = 0.3
    answers["(e) P(A=1|+)"] = 0.6
    answers["(e) P(B=1|+)"] = 0.5

    # type: string: 'yes' or 'no'
    answers["(e) A independent of B given class +?"] = 'yes'

    # type: explanatory string
    answers["(e) A and B conditionally independent given class +, explain"] =  "P(A=1,B=1|+) = P(A=1|+) * P(B=1|+). If this condition holds true, then A and B are considered conditionally independent given the positive class."
  
    return answers
# --------------------------------------------------------
if _name_ == '_main_':
    answers_dict = {}
    answers_dict['question1'] = question1()
    #answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    #answers_dict['question4'] = question4()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
