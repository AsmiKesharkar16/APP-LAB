# decorator for bold formatting
def bold_text(func):
    def wrapper(report):
        return "**" + func(report) +"**"
    return wrapper

# Report Class
class Report:
    # class variable to store templates
    templates={}

    # Constructor
    def __init__(self,title,content):
        self.title=title
        self.content=content

    # class method to add a template
    @classmethod
    def add_template(cls,name,template_func):
        cls.templates[name]=template_func
    
    # class method to get a template
    @classmethod
    def get_template(cls,name):
        return cls.templates.get(name)

    # Magic method to call report object with a template name
    def __call__(self,template_name):
        template=self.get_template(template_name)
        if template:
            return template(self)
        return "Template not found!"

    # string representation
    def __str__(self):
        return f"Report Title:{self.title}\nContent:{self.content}"

# Simple template
def simple_template(report):
    return f"Title:{report.title}\nContent:{report.content}"

# Fancy template with bold formatting
@bold_text
def fancy_template(report):
    return f"Title:{report.title}\nContent:{report.content}"

# Main function
def main():
    # Add templates
    Report.add_template("Simple",simple_template)
    Report.add_template("Fancy",fancy_template)

    # Create report object
    report=Report("Monthly sakes","Sales increased by 20% this month.")

    # Display original report
    print("-------------------------------------------")
    print("Original Report:")
    print("-------------------------------------------")
    print(report)

    # Generate reports using templates
    print("\n-------------------------------------------")
    print("Simple Template:")
    print("-------------------------------------------")
    print(report("Simple"))

    print("\n-------------------------------------------")
    print("Fancy Template:")
    print("-------------------------------------------")
    print(report("Fancy"))

# Run the program 
if __name__=="__main__":
    main()