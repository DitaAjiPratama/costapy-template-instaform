from core   import html

static = [
    {
        'name':'/instaform/jquery',
        'value':{
            'tools.staticdir.on'    : True ,
            'tools.staticdir.dir'   : './templates/instaform/static/jquery' ,
        }
    },
    {
        'name':'/instaform/bootstrap',
        'value':{
            'tools.staticdir.on'    : True ,
            'tools.staticdir.dir'   : './templates/instaform/static/bootstrap' ,
        }
    },
]

def main(dir, page):

    html_template   = html.main.get_html("templates/instaform/html")
    html_page       = html.main.get_html(dir)
    params_list = {
        "template"  : html_template ["template.html"    ]   ,
        "container" : html_page     [ page+".html"      ]
    }
    return params_list
