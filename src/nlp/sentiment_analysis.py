from transformers import pipeline

def analyze_sentiment(texts):
    """
    วิเคราะห์อารมณ์จากข้อความ
    :param texts: รายการข้อความ (list)
    :return: ผลลัพธ์การวิเคราะห์อารมณ์
    """
    sentiment_pipeline = pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')
    results = []
    for text in texts:
        result = sentiment_pipeline(text)
        results.append({"text": text, "sentiment": result[0]['label'], "score": result[0]['score']})
    return results
