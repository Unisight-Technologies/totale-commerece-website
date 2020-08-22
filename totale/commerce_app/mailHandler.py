from django.core.mail import send_mail


def sendMailToUser(name, send_to):
    subject = "Regarding query sent on Totale's Website"
    message = "Hello "+name+"! \n\nWe have successfully received your query.\nWe are glad that you tried to connect with us.\n\nWe will get back to you as soon as possible.\n\nRegards\n-Totale Commerce Academy"
    send_mail(
        subject,
        message,
        'teamurbaninsight@gmail.com',
        [send_to],
        fail_silently = False,
    )
def sendMailQuery(name, email, query):
    message = "The following query has been received on our website:\n\nName: "+name+"\nEmail Id: "+email+"\nMessage: "+query+"\n\nRegards"
    subject = "A query has been received on Totale's Website"
    send_mail(
        subject,
        message,
        'teamurbaninsight@gmail.com',
        ['parmarnaitik0909@gmail.com'],
        fail_silently = False,

    )

def sendMailAdmission(name, email, phone, query, course):
    message = "The following query has been received on our website:\n\nName: "+name+"\nEmail Id: "+email+"\nWhatsapp Number: "+phone+"\nCourse: "+course+"\nMessage: "+query+"\n\nRegards"
    subject = "A query has been received on Totale's website"
    send_mail(
        subject,
        message,
        'teamurbaninsight@gmail.com',
        ['tca.commerce.academy@gmail.com'],
        fail_silently = False,

    )
