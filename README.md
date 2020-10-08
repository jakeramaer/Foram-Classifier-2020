# Foram-Classifier-2020

Dataset - http://endlessforams.org

## Abstract

This thesis applies current deep learning practices to the classification of small-scale, single-
celled organisms named planktonic foraminifera. We show that our suggested setup outperforms
the published state-of-the art in the domain [1] by 3.14% when training on a manually labelled
reference dataset consisting of 34,640 foram samples across 35 separate planktonic foraminiferal
species. This particular dataset is currently subject to major class imbalance, with the most
abundant species consisting of nearly 1500% more samples than the least abundant species.
Over the last few years, a variety of machine learning methods have provided several sig-
nificant accuracy improvements in regards to the class imbalance problem. In this paper, our
focus was on designing and evaluating new image classification strategies for this specific classi-
ifcation task, using current state-of-the-art deep-learning methods. This included rigorous data
augmentation, tests with various loss functions [2] and selective attention models [3]. We cross-
validate our results to reach a final validation accuracy of 90.55%. The baseline convolutional
neural networks we compare against are publicly available on endlessforams.org [1], where the
best baseline network reached a top validation accuracy of 87.41%.

[1] - https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2019PA003612

[2] - https://arxiv.org/abs/1708.02002

[3] - https://arxiv.org/abs/1807.06521

[4] - https://github.com/ahsiang/foram-classifier

## Key Features


## Setup


