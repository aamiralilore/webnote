import flask
app = flask.Flask("notesapp")

# === functions ====

def create_note(note):
    # open note
    notes = open("notesapp.txt", "a")
    # write note + newline
    notes.write(note + "\n")
    # write seperator
    notes.write("---\n")
    # close note
    notes.close()


def search_note():
    #open file
    document = open("notesapp.txt")
    # get content
    content = document.read()
    # close file
    document.close()
    # split content using separator
    notes = content.split("\n---")
    # erase the last element that is always empty
    notes.pop(len(notes)-1)
    return notes


# === Get HTML Page ===

def get_html(page_name):
    # get the .html file with the corresponding page name
    html_file = open(page_name + ".html")
    # get the content
    content = html_file.read()
    # close de file
    html_file.close()
    # return the content
    return content

# === ROUTE FUNCTIONS ===
# Homepage

@app.route("/")
def homepage():
    return get_html("index").replace("{$$ SUBMITTED $$}", "")

# Add note page
@app.route("/addnote", methods=['GET', 'POST'])
def addnote():
    # get the note's text
    note_text = flask.request.form['new_note']
    # get the page
    html_page = get_html("index")
    # variable to store the page's text to return
    page_text = ""

    # This Loop replaces the {$$ SUBMITED $$} in the layout depending 
    # on the content of the textbox. If the textbox is empty go to "else"

    if note_text != "":
        # Gets note without trailing white-spaces
        create_note(note_text.strip())
        # get the page text, replacing the {$$ SUBMITED $$} with message
        page_text = html_page.replace("{$$ SUBMITTED $$}", '<p class="form_saved"> Your note has been saved</p>')
    else:
        # replaces the {$$ SUBMITED $$} with empty string
        page_text= html_page.replace("{$$ SUBMITTED $$}", "")
    # returns the page text    
    return page_text

# All notes
@app.route("/all_notes")
def all_notes():
    # Get same html as search
    html_page = get_html("search")
    notes = search_note()

    actual_notes = ""
    for note in notes:
        actual_notes += "<p>" + note + "</p>"
    # return the page's content with the {$$ NOTES $$} replaced by the full list
    return html_page.replace("{$$ NOTES $$}", actual_notes)

# Search for notes
@app.route("/search")
def search():
    html_page = get_html("search")
    query = flask.request.args.get("q")
    notes = search_note()
    actual_notes = ""
    for note in notes:
        if note.lower().find(query.lower()) != -1:
            actual_notes += "<p>" + note + "</p>"

    if actual_notes == "":
        actual_notes = "<p>No result found</p>"
    return html_page.replace("{$$ NOTES $$}", actual_notes)





