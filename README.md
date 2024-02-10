# CostaPy Template - Instaform
CostaPy template for register/login form

## Usage

- Put the folder in your templates directory
- Add to handler

        import templates.instaform.main as instaform

        kwargs["mako"] = {
          "website" : instaform.main(directory.page["portal"], "register") # page_directory, file_name
        }

- Define a necessary variable on your modules function

        title       = "CostaPy"
        baseurl     = "http://localhost"

- Set a template on your modules function

        from mako.template import Template

        interface = Template(params["mako"]["website"]['template']).render(
          title       = title,
          baseurl     = baseurl,
          container   = Template(params["mako"]["website"]['container']).render(
            # your container content here
          )
        )
