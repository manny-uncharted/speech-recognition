# Abuse Speech Detection

This project continuously listens to the microphone and converts the speech to text. And it detects for abuse words and if it detects any abuse words it will send a warning message to the user.

I was driven by the need to address the pervasive problem of sexual abuse and discrimination that affects millions of people worldwide. I recognized that traditional reporting mechanisms are often inadequate, as victims are often hesitant to report abuse due to fear of retaliation or lack of support, and perpetrators often use their power and influence to silence or intimidate victims.

To tackle this issue, I set out to develop an innovative and proactive solution that could detect and report abusive language in real-time, providing victims with the support they need to stay safe. SafeSpeak was born out of this need and aims to fill the gap in the market by providing a confidential and secure reporting mechanism to help break the cycle of abuse.

I team relied on a combination of speech-to-text algorithms, natural language processing (NLP), and machine learning techniques to detect and report abusive language in real-time. I started by scraping data off social media sites like Twitter to build a diverse dataset that included a range of languages, dialects, and cultural contexts. This was crucial to ensure that the system could accurately detect abusive language across various contexts.

I then used supervised and unsupervised learning techniques to train the machine learning algorithms, constantly updating and refining them to improve their accuracy and reduce false positives. The system listens to conversations and records the audio input, which is then transcribed into text using the speech-to-text algorithm. The text is further processed using NLP techniques to identify the language's tone and intent.

The machine learning algorithms analyze the transcribed text and use various metrics to determine whether the language is abusive or not. If the system detects abusive language, it sends an alert to a designated authority figure or support person. The alert includes the transcribed text, as well as information on the location and time of the incident. At the moment the reporting system is still in works. The system also provides resources and support to the victim, such as information on how to report the abuse and access to counseling services.
I am incredibly proud of the work that I did on SafeSpeak. By leveraging cutting-edge technology, I hope to have developed a powerful tool for detecting and preventing abusive language in real-time and promoting safety and equality for all.


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required packages.

```bash
pip install -r requirements.txt
```

## Usage

```python
python main.py
```

To Run the program on the web browser

```python
streamlit run web.py
```
- After it opens upload the recording file and click on the button to detect the abuse words.
