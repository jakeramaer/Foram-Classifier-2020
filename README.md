# Foram-Classifier-2020

Dataset - http://endlessforams.org

<a href="https://colab.research.google.com/github/jakeramaer/Foram-Classifier-2020/blob/main/Classifier.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>


## Abstract

<img src="https://github.com/jakeramaer/Foram-Classifier-2020/blob/main/9F0E3A56-A450-4AF4-8D4A-612E69FD6FFC.jpeg" width="600">


This thesis applies current deep learning practices to the classification of small-scale, single-celled organisms named planktonic foraminifera. We show that our suggested setup outperforms
the published state-of-the art in the domain <a href="https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2019PA003612">[1]</a> by 3.14% when training on a manually labelled
reference dataset consisting of 34,640 foram samples across 35 separate planktonic foraminiferal
species. This particular dataset is currently subject to major class imbalance, with the most
abundant species consisting of nearly 1500% more samples than the least abundant species.
Over the last few years, a variety of machine learning methods have provided several significant accuracy improvements in regards to the class imbalance problem. In this paper, our
focus was on designing and evaluating new image classification strategies for this specific classiifcation task, using current state-of-the-art deep-learning methods. This included rigorous data
augmentation, tests with various loss functions <a href="https://arxiv.org/abs/1708.02002">[2]</a> and selective attention models <a href="https://arxiv.org/abs/1807.06521">[3]</a>. We cross-validate our results to reach a final validation accuracy of 90.55%. The baseline convolutional
neural networks we compare against are publicly available <a href="https://github.com/ahsiang/foram-classifier">[4]</a>, where the
best baseline network reached a top validation accuracy of 87.41%.

Full thesis - <a href="https://github.com/jakeramaer/Foram-Classifier-2020/blob/main/On_the_Classification_of_Planktonic_Foraminifera_2020-signed.pdf">On the Classification of Planktonic Foraminifera_2020</a>

## Key Features
* Replication of the reference model to test and validate the results obtained in <a href="https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2019PA003612">[1]</a>.
* Conversion of state-of-the-art VGG16 architecture for usage as a pre-trained model within general geological taxonomy.
* Background on the foundations of machine learning and convolutional networks for the benefit of geologists interested in using and further developing the foram model.


## Setup
Model is run via google colab, which is accessible via the jupyter file or <a href="https://colab.research.google.com/drive/1gRKUHKsyG-pa5VKAaV2bSaYBI2cm0NSH?usp=sharing">here</a>. Dataset downloaded <a href="http://endlessforams.org">here</a>. 

Instructions for data-preprocessing listed on jupyter file.

