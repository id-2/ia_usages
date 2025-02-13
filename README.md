# ia_usages

*Using the french acronym "Intelligence Artificielle" (IA) instead of the english one "Artificial intelligence" (AI) for the directory name.*


**All the latest posts dedicated to artificial intelligence usages are brought together in this repository for convenience.**


**You can find all videos related to these posts dedicated to artificial intelligence at [https://www.youtube.com/playlist?list=PL999tA6UKRx_8ud6HfYg_Fn-ZFFyVvhr2](https://www.youtube.com/playlist?list=PL999tA6UKRx_8ud6HfYg_Fn-ZFFyVvhr2)**


1. POC with FastAPI for an NLP API with Spacy, SQLAlchemy, Sqlite and… Streamlit. [https://flaven.fr/2023/10/poc-with-fastapi-for-an-nlp-api-with-spacy-sqlalchemy-sqlite-and-streamlit/](https://flaven.fr/2023/10/poc-with-fastapi-for-an-nlp-api-with-spacy-sqlalchemy-sqlite-and-streamlit/)


2. How to expose NLP Machine Learning Models mostly for Spacy by quickly building an API with FastAPI and then play with them. [https://flaven.fr/2023/09/how-to-expose-nlp-machine-learning-models-mostly-for-spacy-by-quickly-building-an-api-with-fastapi-and-then-play-with-them/](https://flaven.fr/2023/09/how-to-expose-nlp-machine-learning-models-mostly-for-spacy-by-quickly-building-an-api-with-fastapi-and-then-play-with-them/)


3. The importance of the Labeling process or annotating inside an ML pipeline plus an example on how-to train a “custom” NER for Spacy. [https://flaven.fr/2023/08/the-importance-of-the-labeling-process-or-annotating-inside-an-ml-pipeline-plus-an-example-with-ner-made-for-spacy/](https://flaven.fr/2023/08/the-importance-of-the-labeling-process-or-annotating-inside-an-ml-pipeline-plus-an-example-with-ner-made-for-spacy/)

4. Some ideas on the probable future of journalism facing IA and how to create a prompt facilitation application for ChatGPT with Streamlit. [https://flaven.fr/2023/07/some-ideas-on-the-probable-future-of-journalism-facing-ia-and-how-to-create-a-prompt-facilitation-application-for-chatgpt-with-streamlit/](https://flaven.fr/2023/07/some-ideas-on-the-probable-future-of-journalism-facing-ia-and-how-to-create-a-prompt-facilitation-application-for-chatgpt-with-streamlit/)


5. Using ChatGPT on a daily work as a P.O, Developer or for Q/A or Support and checking plagiarism if needed with Python. [https://flaven.fr/2023/02/using-chatgpt-on-a-daily-work-as-a-p-o-developer-or-for-q-a-or-support-and-checking-plagiarism-if-needed-with-python/](https://flaven.fr/2023/02/using-chatgpt-on-a-daily-work-as-a-p-o-developer-or-for-q-a-or-support-and-checking-plagiarism-if-needed-with-python/)

6. Unlocking Speech-to-Text: Harnessing the Power of the OpenAI Whisper API with FastAPI Integration. [https://flaven.fr/2023/10/unlocking-speech-to-text-harnessing-the-power-of-the-openai-whisper-api-with-fastapi-integration/](https://flaven.fr/2023/10/unlocking-speech-to-text-harnessing-the-power-of-the-openai-whisper-api-with-fastapi-integration/)

7. Step by step Introducing to Azure Cloud Deployment: Deploying a FastAPI ML Feature API. [https://flaven.fr/2023/10/step-by-step-introducing-to-azure-cloud-deployment-deploying-a-fastapi-ml-feature-api/](https://flaven.fr/2023/10/step-by-step-introducing-to-azure-cloud-deployment-deploying-a-fastapi-ml-feature-api/)

8. Crafting Fluent Translation API: A quick Journey into Text Translation with NLLB, HuggingFace, and FastAPI, Plus a small Dive into Roberta Masked Language Modeling with Gradio. [https://flaven.fr/2023/11/crafting-fluent-translation-api-a-quick-journey-into-text-translation-with-nllb-huggingface-and-fastapi-plus-a-small-dive-into-roberta-masked-language-modeling-with-gradio/](https://flaven.fr/2023/11/crafting-fluent-translation-api-a-quick-journey-into-text-translation-with-nllb-huggingface-and-fastapi-plus-a-small-dive-into-roberta-masked-language-modeling-with-gradio/)

9. Empower Your Workflow: Harnessing the Power of LM Studio and Ollama for Seamless Local LLM Execution
[https://wp.me/p3Vuhl-3iX](https://wp.me/p3Vuhl-3iX)


10. A small Guide to Harnessing the Power of Open Interpreter and Unlocking Productivity with a ChatGPT-Like Terminal Interface
[https://wp.me/p3Vuhl-3jh](https://wp.me/p3Vuhl-3jh)

**And some other directories that does not have any attached to it but shows useful resources and code.**


**GIT COMMANDS REMINDER**

```bash
# GIT

# suppose you have set a personal access token
# https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token


# go to the directory
cd /Users/brunoflaven/Documents/03_git/BlogArticlesExamples/

# create the directory
git remote add origin streamlit-sweetviz-pandas-profiling-eda-made-easy

# know your branch
git branch


# check for status
git status


# for any change just type this command
git add .

# add a commit with a message
git commit -am "add usecase"
git commit -am "add files"
git commit -am "update files"
git commit -am "add files and update readme"
git commit -am "add to .svg the Musk\'s Favorite Letter X"
git commit -am "add .gitignore"
git commit -am "add docker files"


# push to github if your branch on github is master
# git push origin master
git push

# Repair Permissions
cd /Users/brunoflaven/Documents/03_git/ia_usages
# groupname is staff on a mac
sudo chgrp -R groupname .
sudo chmod -R g+rwX .
sudo find . -type d -exec chmod g+s '{}' +




```