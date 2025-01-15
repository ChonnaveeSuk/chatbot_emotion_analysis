from transformers import pipeline

def summarize_text(text, max_length=130, min_length=30):
    """
    สรุปข้อความด้วยโมเดล Hugging Face
    :param text: ข้อความที่ต้องการสรุป
    :param max_length: ความยาวสูงสุดของข้อความที่สรุป
    :param min_length: ความยาวต่ำสุดของข้อความที่สรุป
    :return: ข้อความที่สรุปแล้ว
    """
    summarizer = pipeline('summarization', model='facebook/bart-large-cnn')
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']
