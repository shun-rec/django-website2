from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"
    
    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["username"] = "ヌートバー"
        return ctxt
    

class AboutView(TemplateView):
    template_name = "about.html"
    
    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["skills"] = [
            "2012年にプロ入りし、2013年には最優秀新人賞を受賞",
            "2014年には、パシフィック・リーグで最多勝、最優秀防御率、最多奪三振、最多完投を達成し、日本シリーズでもMVPを獲得",
            "2016年には、リーグ戦で22本の本塁打を放ち、MVPを受賞",
            "2017年には、自身初の二刀流で、打者として22本の本塁打を打ち、投手としても10勝を挙げました",
            "",
            ""
        ]
        ctxt["num_services"] = 1234567
        return ctxt