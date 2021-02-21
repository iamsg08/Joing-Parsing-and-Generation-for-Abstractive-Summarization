# Joint-Parsing-and-Generation-for-Abstractive-Summarization

We provide the method to replicate the results of for the paper **"[Joint Parsing and Generation for Abstractive Summarization](https://arxiv.org/pdf/1911.10389.pdf)"**,. If you find the code useful, please cite the following paper. 

    @inproceedings{joint-parsing-summarization:2020,
     Author = {Kaiqiang Song and Logan Lebanoff and Qipeng Guo and Xipeng Qiu and Xiangyang Xue and Chen Li and Dong Yu and Fei Liu},
     Title = {Joint Parsing and Generation for Abstractive Summarization},
     Booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},
     Year = {2020}}

## Dependencies

The code is written in Python (v3.7) and Pytorch (v1.3). We suggest the following environment:

To install replicate the environment, run the command:
```
$ # using pip
$ pip install -r requirements.txt
 
```
To download the [Stanford CoreNLP toolkit](https://stanfordnlp.github.io/CoreNLP) and use it as a server, follow the steps provided below. The CoreNLP toolkit helps tokenization (for both train and test) and collect dependency parse trees from target sentences (for train only).
* Download the file on on the following [link](http://nlp.stanford.edu/software/stanford-corenlp-latest.zip).
* Unzip and store the the file(s) in the same location as the code for summarization (). 
* From terminal change your directory to the above location. 
* Run the following command -> 
```
$ java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 15000
```
* Now the server has been made for tokenization. 

* Before moving to training, download the following [folder](https://drive.google.com/file/d/1pSiQzdLKt8Agx9Z7EjjIgR8gGVufaYBF/view?usp=sharing) named 'others', and keep it in the same directory as 'run.py'. 


## Train the Model..
1. Training the Model with train files and validation files.
    ```
    $ python run.py --do_train --train_prefix data/train --valid_prefix data/valid
    ```

2. Generating Summaries with our joint parsing and generating summarization model trained on selected dataset including: gigaword (default), newsroom, cnndm, websplit.
    ```
    $ python run.py --do_test --inputFile data/test.txt
    ```
    Or if you want runing models other than that trained on gigaword:
    ```
    $ python run.py --do_test --data newsroom --inputFile data/test.txt
    ```
   
