from django.views.generic import TemplateView

class IndexView(TemplateView):
  template_name = "index.html"

  def get_context_data(self):
    ctxt = super().get_context_data()
    ctxt["username"] = "Sugu"
    return ctxt

class AboutView(TemplateView):
  template_name = "about.html"

  def get_context_data(self):
    ctxt = super().get_context_data()
    ctxt["skills"] = [
      "Python",
      "Javascript",
      "Ruby",
      "Go",
      "PHP",
    ]
    ctxt["num_services"] = 12345678
    return ctxt
