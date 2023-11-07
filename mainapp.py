import panel as pn
from panel.template import FastListTemplate
from CyberIndexDashboard import CyberIndexDashboard

main_area = pn.Column("")
ext="External"
def main():
    global main_area
    pn.extension('echarts','tabulator')
    pn.config.sizing_mode="stretch_width"
    # Instantiate pages and add them to the pages dictionarqy
    pages = {
        "CEIDashboard": CyberIndexDashboard("Region","CEI","CEI Avg."),
        "GCIDashboard": CyberIndexDashboard("Region","GCI","GCI Avg."),
        "NCSIDashboard": CyberIndexDashboard("Region","NCSI","NCSI Avg."),
        "DDLDashboard": CyberIndexDashboard("Region","DDL","DDL Avg."),
    }
    sidebar = None 
    data_source_info = pn.pane.Markdown("""
                                            ***The data describes cyber attacks split by continent***
                                            ***Data is taken from [Kaggle](https://www.kaggle.com/datasets/katerynameleshenko/cyber-security-indexes)!***
                                        """)
    
    radio_button_group = pn.widgets.ToggleGroup(name='Index', options=['NCSI', 'CEI','GCI', 'DDL'], behavior="radio",button_type='primary',orientation='vertical')
    
    def update(event):
        global main_area
        main_area.clear()
        main_area.append(pages[radio_button_group.value+"Dashboard"].view())

    radio_button_group.param.watch(update,'value',onlychanged=True)
    radio_button_group.param.trigger('value')
    sidebar = pn.Column(pn.Row(radio_button_group),pn.Row(data_source_info))
        
    template = FastListTemplate(
        title="Cyber Operations Instances",
        sidebar=[sidebar],
        main=[main_area],
    )

    pn.state.cache["template"] = template
    pn.state.cache["modal"] = template.modal
    
    # Serve the Panel app
    template.servable()

main()  