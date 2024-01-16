import os
import json
from pathlib import Path
import time
import openai
import timeout_decorator # conda install -c conda-forge timeout-decorator
from icecream import ic

openai.api_key = os.environ["OPENAI_API_KEY"]

dataset = 'asap-6'
prompt_version = '9999'

path = Path(f"./chatgpt_api_{prompt_version}/{dataset}/train.jsonl")
first_time = not path.is_file()

first_time = True

num = int(dataset.split('-')[1])
# load asap dataset


if first_time:
    import pandas as pd

    df_train = pd.read_csv("./asap-sas-splitted/original/train_data.tsv", sep='\t')
    #test_set_label = pd.read_csv("./asap-sas-splitted/original/public_leaderboard_solution.csv")
    df_test = pd.read_csv("./asap-sas-splitted/original/test_data.tsv", sep='\t')

    df_test['statement_score'] = None


    train_jsonl = json.loads(df_train.to_json(orient='records')) #right now it's empty
    test_jsonl = json.loads(df_test.to_json(orient='records')) #converting dataset into JSON  # it's have data

else:
    train_jsonl = []
    test_jsonl = []
    with open(f"./chatgpt_api_{prompt_version}/{dataset}/train.jsonl", 'r') as f:
        train_jsonl = [json.loads(each) for each in f.readlines()]
    with open(f"./chatgpt_api_{prompt_version}/{dataset}/test.jsonl", 'r') as f:
        test_jsonl = [json.loads(each) for each in f.readlines()]




# fix
prompt_path = f"chatgpt_api_{prompt_version}/prompts/{dataset}/prompt.txt" #Path for prompt



from tenacity import retry,stop_after_attempt,wait_random_exponential

def load_input(file_name):
    with open(file_name, 'r', encoding="utf8") as file:
        content = file.read()
    return content

prompt_message = load_input(prompt_path) #Loading the prompt with the message



def template(statement):
    return f"{prompt_message}\n\n[Statement]: {statement}\n[Score and Basis of scoring]:"

# Set the timeout
# @retry(wait=wait_random_exponential(min=30, max=80), stop=stop_after_attempt(2)) #Chatgpt retries
# @timeout_decorator.timeout(40)
def chat_completion(prompt):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
    )
    return completion.choices

def chat_completion(prompt_message, statement):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": prompt_message},{"role": "user", "content": statement}],
        temperature=0,
    )
    return completion.choices

from tqdm import tqdm



countTime = 0
for line in tqdm(train_jsonl, total=len(train_jsonl), desc="Processing lines"): #it will pas if it's not have any data

    # print(line)
    statement = line['statement']
    statement = statement.replace('^p',' ').replace('^P',' ')
    prompt = template(statement)
    if 'gpt-3.5-turbo' in line.keys() and len(line['gpt-3.5-turbo']) > 0:
        pass
    else:
        try:

            countTime += 1
            if countTime == 2:
                time.sleep(35)
                countTime = 0
            # choices = chat_completion
            choices = chat_completion(prompt_message, statement)
        except Exception as e:
            print(e)
            choices = []
        outputs = []
        if len(choices) == 0:
            line['gpt-3.5-turbo'] = outputs
        else:
            for choice in choices:
                score_and_ratioanle = choice.message["content"]
                outputs.append({"index":choice.index ,"content": score_and_ratioanle})
            line['gpt-3.5-turbo'] = outputs
#
import jsonlines
with jsonlines.open(f"./chatgpt_api_{prompt_version}/{dataset}/train.jsonl", 'w') as writer: #it will write that data in traning part
    writer.write_all(train_jsonl)



# this the test code which execute for test purposes

countTime = 0
for line in tqdm(test_jsonl, total=len(test_jsonl), desc="Processing lines"):


    statement = line['statement']
    statement = statement.replace('^p',' ').replace('^P',' ')

    prompt = template(statement) # generate prompt with statment and samples
    if 'gpt-3.5-turbo' in line.keys() and len(line['gpt-3.5-turbo']) > 0:
        pass
    else:
        try:
            countTime += 1
            if countTime == 2:
                time.sleep(35)
                countTime = 0
            # choices = chat_completion
            choices = chat_completion(prompt_message, statement)
        except Exception as e:
            print(e)
            choices = []
        outputs = []
        if len(choices) == 0:
            line['gpt-3.5-turbo'] = outputs
        else:
            for choice in choices:
                score_and_ratioanle = choice.message["content"]
                outputs.append({"index":choice.index ,"content": score_and_ratioanle})
            line['gpt-3.5-turbo'] = outputs

with jsonlines.open(f"./chatgpt_api_{prompt_version}/{dataset}/test.jsonl", 'w') as writer: # outputting the test data
    writer.write_all(test_jsonl)
