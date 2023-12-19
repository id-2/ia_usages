#!/usr/bin/python
# -*- coding: utf-8 -*-
#

"""
[env]
# Conda Environment
conda create --name langchain_ai python=3.9.13
conda info --envs
source activate langchain_ai
conda deactivate

# if needed to remove
conda env remove -n [NAME_OF_THE_CONDA_ENVIRONMENT]
conda env remove -n langchain_ai

# update conda 
conda update -n base -c defaults conda

# to export requirements
pip freeze > requirements.txt

# to install
pip install -r requirements.txt

conda install -c conda-forge langchain

# This example requires beautifulsoup
conda install -c anaconda beautifulsoup4

conda install -c anaconda beautifulsoup4


# This example requires gpt4all
pip install pygpt4all


# This example requires chromadb
conda install -c conda-forge chromadb


# [path]
cd /Users/brunoflaven/Documents/03_git/ia_usages/ia_using_other_llm/

# LAUNCH the file
python gpt4all_test_1.py


# EXPLICATIONS
https://github.com/samwit/langchain-tutorials/blob/382e8db4dc5e01fc400bee8d4146cb1a2e9c3150/ollama/basic.py




"""


from gpt4all import GPT4All

model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf")
output = model.generate("The capital of France is ", max_tokens=3)
print(output)




    