
import streamlit.components.v1 as components
import time
import json
import requests
import smtplib
import datetime
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
from streamlit_ace import st_ace
from streamlit_drawable_canvas import st_canvas
import pandas as pd
from PIL import Image
import streamlit as st


wide="wide"
st.set_page_config(
    page_title=" SaeeAM",
    page_icon=":computer",  
    layout=wide,
    initial_sidebar_state="expanded",
    menu_items={
         'Get Help': 'https://www.extremelycoolapp.com/help',
         'Report a bug': "https://www.extremelycoolapp.com/bug",
         'About': "#SaeeAM. Startup Company!"
     }
)




def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()



with st.sidebar:
   pages = ["Home", "Coding", "Project", "ClassRoom"]
   page = st.selectbox("Menu", pages)
   

   with st.expander("How May I Help U"):

       with st.form("my_form", clear_on_submit=True):
           name= st.text_input(label="Name",value="", placeholder="Enter Name Here", type="default", key="name")
           email =st.text_input(label="Email",value="", placeholder="Enter Email Here", type="default", key="email")
           number= st.text_input(label="Number",value="", max_chars=10, placeholder="Enter Number Here", type="default", key="number")
           message= st.text_area(label="Message",value="", max_chars=1000, placeholder="Enter Number Here", key="message")

           submitted = st.form_submit_button("Submit")
          

            
           if submitted:
               if len(email) > 0 or len(number) >0 or len(message) >0:
                   if email.endswith("@gmail.com"):
                       st.success("Thats Good Write Email syntax")
                       with st.spinner(text='Email Sending'):
                           time.sleep(3)
                           sending = (name+" "+email+" "+number+" "+message)
                           st.write(sending)
                       
                       st.success('Done')
                       st.balloons()
                   else:
                       st.warning("Thats Bad Syntax You use")
               else:
                   st.warning("Fill Form Don't Leave Blanks Email Never Leave Blanks")







if page == "Home":
    cont1 = st.container()

    cont1col1, cont1col2= cont1.columns([3,2])


    with cont1col1:
        st.title("SaeeAM")

        st.subheader("""Indian Collage Studnet Startup Company""")
        st.write("Help Indian Startup TO Grow Help By Creating Projects And Provide SErvices")
        options = st.multiselect(
     'Select Services How May I Help You',
     ['Jobs','SaeeAM Team', 'Apply Online', 'Sarkari Result', 'Teaching','Payment', 'Document Services','More & More'],['Jobs', 'Apply Online', 'Sarkari Result', 'Teaching','Payment', 'Document Services' ,'More & More'])

        st.code(options)
    with cont1col2:
        youths =  "https://assets4.lottiefiles.com/packages/lf20_ljotbiif.json"
        lottie_json_youth = load_lottieurl(youths)

        st_lottie(lottie_json_youth)
        
    cont2 = st.container()

    cont2col1, cont2col2= cont2.columns([3,2])


    with cont2col1:
        st.title("Learn By Teach Someone")

        st.subheader("""Indian Collage Studnet Teaching U As U Want""")
        st.code("Python, Css, Html, Javascript, C++ ...👈👈👈")
    
    with cont2col2:
        collage = "https://assets10.lottiefiles.com/packages/lf20_khyisucd.json"

        lottie_json_coll = load_lottieurl(collage)
        st_lottie(lottie_json_coll)
        


    cont3 = st.container()

    cont3col1, cont3col2= cont3.columns([3,2])


    with cont3col1:
        st.title("Join US")

        st.subheader("JOin Us TO Creating Projects Related Computer Science field Earn With LEarn")
        st.code("Website, App, Software, Networking, Servers ...👈👈👈")
        
    with cont3col2:
        youth = "https://assets3.lottiefiles.com/packages/lf20_Xdbivx.json"
        lottie_json_youths = load_lottieurl(youth)
       
        st_lottie(lottie_json_youths)

    cont4 = st.container()

    cont4col1, cont4col2= cont4.columns([3,2])


elif page == "Coding":
    
    st.header(page)
    c1, c2 = st.columns([3, 1])

    c2.subheader("Parameters")

    with c1:
        THEMES = [
    "ambiance", "chaos", "chrome", "clouds", "clouds_midnight", "cobalt", "crimson_editor", "dawn",
    "dracula", "dreamweaver", "eclipse", "github", "gob", "gruvbox", "idle_fingers", "iplastic",
    "katzenmilch", "kr_theme", "kuroir", "merbivore", "merbivore_soft", "mono_industrial", "monokai",
    "nord_dark", "pastel_on_dark", "solarized_dark", "solarized_light", "sqlserver", "terminal",
    "textmate", "tomorrow", "tomorrow_night", "tomorrow_night_blue", "tomorrow_night_bright",
    "tomorrow_night_eighties", "twilight", "vibrant_ink", "xcode"
]

        KEYBINDINGS = [
    "emacs", "sublime", "vim", "vscode"
]
        LANGUAGES = [
    "abap", "abc", "actionscript", "ada", "alda", "apache_conf", "apex", "applescript", "aql", 
    "asciidoc", "asl", "assembly_x86", "autohotkey", "batchfile", "c9search", "c_cpp", "cirru", 
    "clojure", "cobol", "coffee", "coldfusion", "crystal", "csharp", "csound_document", "csound_orchestra", 
    "csound_score", "csp", "css", "curly", "d", "dart", "diff", "django", "dockerfile", "dot", "drools", 
    "edifact", "eiffel", "ejs", "elixir", "elm", "erlang", "forth", "fortran", "fsharp", "fsl", "ftl", 
    "gcode", "gherkin", "gitignore", "glsl", "gobstones", "golang", "graphqlschema", "groovy", "haml", 
    "handlebars", "haskell", "haskell_cabal", "haxe", "hjson", "html", "html_elixir", "html_ruby", "ini", 
    "io", "jack", "jade", "java", "javascript", "json", "json5", "jsoniq", "jsp", "jssm", "jsx", "julia", 
    "kotlin", "latex", "less", "liquid", "lisp", "livescript", "logiql", "logtalk", "lsl", "lua", "luapage", 
    "lucene", "makefile", "markdown", "mask", "matlab", "maze", "mediawiki", "mel", "mixal", "mushcode", 
    "mysql", "nginx", "nim", "nix", "nsis", "nunjucks", "objectivec", "ocaml", "pascal", "perl", "perl6", 
    "pgsql", "php", "php_laravel_blade", "pig", "plain_text", "powershell", "praat", "prisma", "prolog", 
    "properties", "protobuf", "puppet", "python", "qml", "r", "razor", "rdoc", "red", "redshift", "rhtml", 
    "rst", "ruby", "rust", "sass", "scad", "scala", "scheme", "scss", "sh", "sjs", "slim", "smarty", 
    "snippets", "soy_template", "space", "sparql", "sql", "sqlserver", "stylus", "svg", "swift", "tcl", 
    "terraform", "tex", "text", "textile", "toml", "tsx", "turtle", "twig", "typescript", "vala", "vbscript", 
    "velocity", "verilog", "vhdl", "visualforce", "wollok", "xml", "xquery", "yaml"
]
        content = st_ace(
                placeholder=c2.text_input("Editor placeholder", value="Write your code here"),
                language=c2.selectbox("Language mode", options=LANGUAGES, index=121),
                theme=c2.selectbox("Theme", options=THEMES, index=35),
                keybinding=c2.selectbox("Keybinding mode", options=KEYBINDINGS, index=3),
                font_size=c2.slider("Font size", 5, 24, 14),
                tab_size=c2.slider("Tab size", 1, 8, 4),
                show_gutter=c2.checkbox("Show gutter", value=True),
                show_print_margin=c2.checkbox("Show print margin", value=False),
                wrap=c2.checkbox("Wrap enabled", value=False),
                auto_update=c2.checkbox("Auto update", value=False),
                readonly=c2.checkbox("Read-only", value=False),
                min_lines=45,
                key="ace",
                height=400,
            )

        if content:
            st.subheader("Content")
            st.code(content)
            
elif page == "Project":
    st.header(page)
    src= st.text_input(label="Website LInk HEre",value="", placeholder="Enter website link Here", type="default", key="iframe")

    st.components.v1.iframe(src, height=600,  scrolling=True)

    
    
elif page == "ClassRoom":
    class1, class2 = st.columns([3, 1])
    class2.subheader("Parameters")

    with class2:

        # Specify canvas parameters in application
        stroke_width = class2.slider("Stroke width: ", 1, 25, 3)
        
        stroke_color = class2.color_picker("Stroke color hex: ")
        bg_color = class2.color_picker("Background color hex: ", "#eee")
        bg_image = class2.file_uploader("Background image:", type=["png", "jpg"])
        drawing_mode = class2.selectbox(
            "Drawing tool:", ("freedraw", "line", "rect", "circle", "transform", "point")
            )
        realtime_update = class2.checkbox("Update in realtime", True)
       
    with class1:

# Create a canvas component
        canvas_result = st_canvas(
            fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
            stroke_width=stroke_width,
            stroke_color=stroke_color,
            background_color=bg_color,
            background_image=Image.open(bg_image) if bg_image else None,
            update_streamlit=realtime_update,
            width=800,
            drawing_mode=drawing_mode,
            display_toolbar=class2.checkbox("Display toolbar", True),
            key="canvas",
            )

# Do something interesting with the image data and paths
        if canvas_result.image_data is not None:

            st.image(canvas_result.image_data)
        if canvas_result.json_data is not None:
            objects = pd.json_normalize(canvas_result.json_data["objects"]) # need to convert obj to str because PyArrow
            for col in objects.select_dtypes(include=['object']).columns:
                objects[col] = objects[col].astype("str")
            st.dataframe(objects)
       



