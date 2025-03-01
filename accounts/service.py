# from django.core.mail import send_mail
#
# def send_email_letter():
#     send_mail(
#         message='Test message',
#         subject='Test subject',
#         from_email='khushvaqt.arab@gmail.com',
#         recipient_list=['xushvaqt.abdigafforov@gmail.com'],
#         html_message= """
#         <main>
#             <h1>👋 Xush kelibsiz!</h1>
#             <p>📖 Saytdagi </p>
#         </main>
#         """
#     )
from django.core.mail import EmailMultiAlternatives

from shop.models import Product, Order, Category  # O‘zingga mos modellarni tekshir

def send_email_alternative():
    file = 'khushvaqt.pdf'
    subject = 'Test'
    text_content = 'Test content'
    from_email = 'khushvaqt.arab@gmail.com'
    to = ['xushvaqt.abdigafforov@gmail.com']
    html_content = """
    <main>
        <h1>Welcome to TEST</h1>
        <p>It is your page</p>
    </main>
    """
    email = EmailMultiAlternatives(
        subject, text_content, from_email, to
    )

    email.attach_alternative(html_content, 'text/html')

    with open(file, 'rb') as f:
        email.attach(file, f.read(), "khushvaqt/pdf")

    email.send()

