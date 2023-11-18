from models.Sentence import Sentence

def add_sentence_to_db(sentence_id, url, title, full_text, summary):
  session = Session()
  new_sentence = Sentence(
    id=sentence_id,
    url=url,
    pdf_url='',
    sentence_title=title,
    full_text=full_text,
    summary_text=summary
  )
  session.add(new_sentence)
  session.commit()
  session.close()