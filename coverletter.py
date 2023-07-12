import openai as ai
import json
import streamlit as st 

print("** Loading API Key")
ai.api_key = "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"

st.title("Guide To Job Search")
st.markdown("# Indra Cover Letter Generator 🎈")
st.sidebar.markdown("# Cover Letter Generator  🎈")

with st.sidebar: 
    model_used = st.selectbox(
     'GPT-3 Model',
    #  ('DaVinci', 'Curie', 'Babbage', 'Ada'))
    ('text-davinci-002', 'text-curie-001', 'text-babbage-001', 'text-ada-001'))


    

    max_tokens = st.text_input("Maximum number of tokens:", "1949")

    
    temperature = st.text_input("Temperature: ", "0.99")
    top_p = st.text_input("Top P: ", "1")


with st.form(key='my_form_to_submit'):    
    company_name = st.text_input("Company Name: ", "Google")
    role = st.text_input("What role are you applying for? ", "Machine Learning Engineer")
    contact_person = st.text_input("Who are you emailing? ", "Technical Hiring Manager")
    your_name = st.text_input("What is your name? ", "Amber Teng")
    personal_exp = st.text_input("I have experience in...", "natural language processing, fraud detection, statistical modeling, and machine learning algorithms. ")
    job_desc = st.text_input("I am excited about the job because...", "this role will allow me to work on technically challenging problems and create impactful solutions while working with an innovative team. " )
    passion = st.text_input("I am passionate about...", "solving problems at the intersection of technology and social good.")
    # job_specific = st.text_input("What do you like about this job? (Please keep this brief, one sentence only.) ")
    # specific_fit = st.text_input("Why do you think your experience is a good fit for this role? (Please keep this brief, one sentence only.) ")
    submit_button = st.form_submit_button(label='Submit')

prompt = ("Write a cover letter to " + contact_person + " from " + your_name +" for a " + role + " job at " + company_name +"." + " I have experience in " +personal_exp + " I am excited about the job because " +job_desc + " I am passionate about "+ passion)

if submit_button:
    # The Model
    response = ai.Completion.create(
        engine = model_used,
        # engine="text-davinci-002", # OpenAI has made four text completion engines available, named davinci, ada, babbage and curie. We are using davinci, which is the most capable of the four.
        prompt=prompt, # The text file we use as input (step 3)
        max_tokens=int(max_tokens), # how many maximum characters the text will consists of.
        temperature=0.99,
        # temperature=int(temperature), # a number between 0 and 1 that determines how many creative risks the engine takes when generating text.,
        top_p=int(top_p), # an alternative way to control the originality and creativity of the generated text.
        n=1, # number of predictions to generate
        frequency_penalty=0.3, # a number between 0 and 1. The higher this value the model will make a bigger effort in not repeating itself.
        presence_penalty=0.9 # a number between 0 and 1. The higher this value the model will make a bigger effort in talking about new topics.
    )


    text = response['choices'][0]['text']
    print("Prompt:", prompt)
    print("Response:", text)

    st.subheader("Cover Letter Prompt")
    st.write(prompt)
    st.subheader("Auto-Generated Cover Letter")
    st.write(text)
    st.download_button(label='Download Cover Letter', file_name='cover_letter.txt', data=text)

    # print("Other results:", response)

    with open('cover_letters.txt', 'a') as f:
        f.write(text)
