import streamlit as st
from bs4 import BeautifulSoup
from graphviz import Digraph
import io
from collections import Counter

def parse_html_content(content):
    soup = BeautifulSoup(content, 'html.parser')
    return soup

def visualize_tree(soup):
    dot = Digraph(comment='HTML Tree Visualization')
    add_node(dot, soup)
    st.graphviz_chart(dot.source)

def add_node(dot, element, parent=None):
    if element.name:
        node_id = str(id(element))
        label = f'<{element.name}>'
        dot.node(node_id, label=label, shape='box', style='filled', color='lightblue')
        
        if parent:
            dot.edge(parent, node_id)
        
        for child in element.children:
            if child.name:
                child_id = str(id(child))
                add_node(dot, child, node_id)

def count_tags(soup):
    tags = [tag.name for tag in soup.find_all()]
    tag_freq = Counter(tags)
    return tag_freq

def count_lines(content):
    line_count = len(content.splitlines())
    return line_count

def show_html_content(content):
    st.header("Uploaded HTML Code")
    st.code(content, language='html', height=800, width=900)

def main():
    st.title('HTML Tree Visualization')

    # Demo HTML file
    demo_html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Demo HTML File</title>
    </head>
    <body>
        <h1>Hello, Streamlit!</h1>
        <p>This is a demo HTML file for visualization.</p>
    </body>
    </html>
    '''

    

    uploaded_file = st.file_uploader('Upload HTML file', type=['html'])
    load_demo = st.button('Load Demo HTML')

    show_tag_frequency = st.sidebar.checkbox("Show Tag Frequency")
    st.sidebar.success("Made By : Mainak")

    if load_demo:
        uploaded_file = io.StringIO(demo_html)

    if uploaded_file:
        st.success('File successfully uploaded!')
        content = uploaded_file.read()
        soup = parse_html_content(content)
        visualize_tree(soup)

        if show_tag_frequency:
            tag_freq = count_tags(soup)
            st.header('Tag Frequency')
            st.table(list(tag_freq.most_common()))

        if show_html_checkbox:
            show_html_content(content)

   

if __name__ == "__main__":
    main()
