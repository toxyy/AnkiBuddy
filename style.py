button_style = """
QPushButton{
    background-color: transparent;
    border-radius: 8px;
    border: 5px solid #555;
    min-height: 20px;
    padding: 15px;
}
QPushButton:flat{
    border: 0px;
    color: rgba(1.0,1.0,1.0,0.1);
}
QPushButton:hover{
    background: rgba(100.0,100.0,100.0,0.01);
    border: 5px solid #32a3fa;
}
QPushButton:checked{
    border: 5px solid #32a3fa;
}
"""
button_style_custom_border = """
QPushButton{
    background-color: transparent;
    border-radius: 8px;
    border: 5px solid %s;
    min-height: 20px;
    padding: 15px;
}
"""
confirm_button_style= """
QPushButton{
    background-color: #32a3fa;
    padding: 10px;
    min-height: 12px;
    border-radius: 8px;
    color: #111;
}
"""
incorrect_button_style="""
QPushButton{
    background-color: transparent;C
    border-radius: 8px;
    border: 5px solid #32a3fa;
    min-height: 13px;
    padding: 9px;
}
"""
play_anchor_style = """
.b_playButton{
    
}
"""