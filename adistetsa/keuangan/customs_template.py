# import pdfkit as pdf 

# def pdf(self):
#     persons = self.ID
#     template = pdf.get_template('plapp/person_list.html')
#     html = template.render({'persons': persons})
#     options = {
#         'page-size': 'Letter',
#         'encoding': "UTF-8",
#     }
#     pdf = pdf.from_string(html, False, options)
#     response = HttpResponse(pdf, content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment;
#     filename="pperson_list_pdf.pdf"'
#     return response    