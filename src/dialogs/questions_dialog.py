from __future__ import annotations
from typing import Any

from ..forms.questions_wizard import *
from ..subsets import *

from ..models import ListModel, HomeworkModel
from ..controllers import ListController, HomeworkController
from ..views import ListView, HomeworkView

from .options_dialog import OptionsDialog
from .template_dialog import TemplateDialog

from ..stores import NotecardStore, OptionStore

from aqt.qt import (
    QDialog,
    QMessageBox
)
from aqt import mw

# Questions Dialog - setup the questions that are
# asked in Homework and Assessments
# 
# use getResults() to show the dialog 
# state is managed internally and does not rely on a model

 # Templates: 
        # self.sel_templates = list of templates (dicts)
        ### template schema:
        ###     type_ind: question type. 0= multiple choice, 1=matching, 2=write the answer
        ###     type: question type string. "Multiple Choice", "Matching", or "Write the Answer"
        ###     question: Anki field to populate Question(s) from.
        ###     answer: Anki field to populate Answer(s) from.
        ###     include_reverse: True/False should sometimes reverse the question and answer fields
        # extra fields
        ###### for Multiple choice:
        ######      number_choices: the number of Answers to choose from.
        ###### for Matching:
        ######      groupsize: How many many questions/answers should be on a single page to match from.
        ######      extrabank: (not implemented currently) will be how many extra answers than questions there are.

        # self.subsets[self.curr_subset] -> returns Subset object with information needed
        #           must also include self.sub_group_ind to know which group of the subset to look at. or pass -1 to pass nothing

class QuestionsDialog(QDialog, Ui_QuestionsWizard):
    def __init__(self, notecard_store: NotecardStore, options_store: OptionStore):
        """Load questions wizard.

        Args:
            notecard_store (NotecardStore): Notecard store to use.
            options_store (OptionStore): Options store to load config from.
        """
        super(QuestionsDialog, self).__init__()
        self.setupUi(self)

        self.setWindowTitle("Questions Wizard - "+notecard_store.deck_name)
        self.setWindowIcon(mw.windowIcon())
        self.newTemplate.clicked.connect(self.new_template_sig)
        self.editTemplate.clicked.connect(self.edit_template_sig)
        self.deleteTemplate.clicked.connect(self.delete_template_sig)

        self.addSel.clicked.connect(self.add_sel_template_sig)
        self.removeSel.clicked.connect(self.remove_sel_template_sig)

        self.options.clicked.connect(self.show_options_sig)

        self.notecard_store = notecard_store
        self.options_store = options_store

        self.templates = []
        self.sel_templates = []

        self.subsets = []
        self.all_groups = True
        self.curr_subset = 0
        self.sub_group_ind = 0 # group index for the current subset

        lesson_size = options_store.get_globals(self.notecard_store.deck_name)["lesson_size"]
        
        self.add_subset(LinearSubset(notecard_store, lesson_size=lesson_size))
        self.add_subset(LearnedSubset(notecard_store, lesson_size=lesson_size))
        self.add_subset(LapsedSubset(notecard_store, lesson_size=lesson_size))
        self.add_subset(NewSubset(notecard_store, lesson_size=lesson_size))

        # signals / controller
        self.subsetBox.currentIndexChanged.connect(self.subset_index_sig)
        self.allgroups_box.stateChanged.connect(self.allgroups_sig)
        self.group_index_box.valueChanged.connect(self.group_index_sig)
        self.previewSubsetButton.clicked.connect(self.preview_subset_sig)

        self.buttonBox.accepted.connect(self.do_accept)

        # load last templates
        if "templates" in self.options_store.get_homework_config(notecard_store.deck_name):
            for templ in self.options_store.get_homework_config(notecard_store.deck_name)["templates"]:
                self.templates.append(templ)
                self.templatesList.addItem(self.get_template_string(templ))
        if "selected_templates" in self.options_store.get_homework_config(notecard_store.deck_name):
            for sel_templ  in self.options_store.get_homework_config(notecard_store.deck_name)["selected_templates"]:
                self.sel_templates.append(sel_templ)
                self.selectedList.addItem(self.get_template_string(self.templates[sel_templ]))

        # load last subset
        if "last_subset" in self.options_store.get_homework_config(notecard_store.deck_name):
            self.curr_subset = self.options_store.get_homework_config(notecard_store.deck_name)["last_subset"]
            self.subsetBox.setCurrentIndex(self.curr_subset)
    
    def do_accept(self):
        """Connected to button box, either reject the user because no templates have been
        created yet, or create the Homework view instance and begin practice. 
        """        
       
        if len(self.sel_templates) == 0:
            self._cancelMsg = QMessageBox()
            self._cancelMsg.setText("Please set-up question templates in order to proceed.")
            self._cancelMsg.exec_()
            return
        templs = [self.templates[i] for i in self.sel_templates]
        if self.all_groups:
            model = HomeworkModel(self.notecard_store, templs, self.options_store, subset=self.subsets[self.curr_subset], subset_group = -1)
        else:
            model = HomeworkModel(self.notecard_store, templs, self.options_store, subset=self.subsets[self.curr_subset], subset_group = self.sub_group_ind)
        controller = HomeworkController(model)
        mw._hwView = HomeworkView(model, controller)
        mw._hwView.show()

    def add_template(self, templ: dict[str, Any]):
        """Called to add a template. The dict argument is the same schema as
        the dict that is returned from the Template Dialog.

        Args:
            templ (dict[str, Any]): Template to add
        """
        self.templates.append(templ)
        # update UI
        self.templatesList.addItem(self.get_template_string(templ))

        # auto-add to selected templates
        row = len(self.templates) - 1
        self.sel_templates.append(row)
        self.selectedList.addItem(self.get_template_string(self.templates[row]))

        # update options store
        self.update_options()

    def edit_template(self, index: int, templ: dict[str, Any]):
        """Modify the template at index with the template dict passed.

        Args:
            index (int): Index to modify
            templ (dict[str, Any]): New template to set at index.
        """
        self.templates[index] = templ
        self.templatesList.item(index).setText(self.get_template_string(templ))
        try:
            sel_pos = self.sel_templates.index(index)
            self.selectedList.item(sel_pos).setText(self.get_template_string(templ))
        except:
            pass # not in selected templates
        self.update_options()

    def update_options(self):
        """Save the template presets to the options store / config file.
        """
        self.options_store.get_homework_config(self.notecard_store.deck_name)["templates"] = self.templates  
        self.options_store.get_homework_config(self.notecard_store.deck_name)["selected_templates"] = self.sel_templates
        self.options_store.save()

    def get_template_string(self, templ: dict[str, Any]) -> str:
        """Helper method to get a pretty string from a template dict, to display
        in the list views.

        Args:
            templ (dict[str, Any]): Template dict to translate to string

        Returns:
            str: String representing template "templ"
        """
        return templ["type"] +" - " + templ["question"] +" / " + templ["answer"] + (" (+reverse) "if templ["include_reverse"] else "")

    # Signals
    def new_template_sig(self):
        """Connected to the New Template button.
        """
        d = TemplateDialog(self.notecard_store, self.options_store)
        res = d.getResults()
        if res:
            self.add_template(res)
        else:
            pass # nothing happened
    
    def edit_template_sig(self):
        """Connected to the Edit Template button.
        """
        if len(self.templates) < 1: return
        # QListWidget.currentRow() is given -1 if nothing is selected
        # todo : consider selected list as well
        #if self.templatesList.currentRow() < 0 and self.selectedList.currentRow() < 0: return
        if self.templatesList.currentRow() < 0: return
        row = self.templatesList.currentRow()
        d = TemplateDialog(self.notecard_store, self.options_store, self.templates[row])
        res = d.getResults()
        if res:
            self.edit_template(row, res)
        else:
            pass
    
    def delete_template_sig(self):
        """Connected to the Delete Template button.
        """
        if self.templatesList.currentRow() < 0: return # nothing is selected
        row = self.templatesList.currentRow()
        # delete from self.templates
        del self.templates[row]

        # delete from ui
        self.templatesList.takeItem(row)

        # delete any reference in self.sel_templates 
        # so far, there can only be one reference in sel_templates, but will write this as if there could be multiple anyway
        # and,
        # use _below to move all values above row self.sel_templates -1
        to_delete = []
        for i in range(len(self.sel_templates)):
            if self.sel_templates[i] == row: # list index out of range after two deletes
                to_delete.append(i) # roundabout way to avoid concurrent modification?
                
        for ele in to_delete:
            # delete from model
            del self.sel_templates[ele]
            # delete from ui
            self.selectedList.takeItem(ele)

        for i in range(len(self.sel_templates)):
            if self.sel_templates[i] > row:
                self.sel_templates[i] = self.sel_templates[i] - 1
        
        self.update_options()

    def add_sel_template_sig(self):
        """Connected to the (right arrow) button to select a template
        for practice.
        """
        if self.templatesList.currentRow() < 0: return
        row = self.templatesList.currentRow()
        if row in self.sel_templates:
            pass
        else:
            self.sel_templates.append(row)
             
            # add to ui
            self.selectedList.addItem(self.get_template_string(self.templates[row]))
        
        self.update_options()

    def remove_sel_template_sig(self):
        """Connected to the (left arrow) button to unselect a template for practice.
        """
        if self.selectedList.currentRow() < 0: return
        row = self.selectedList.currentRow()

        del self.sel_templates[row]
        self.selectedList.takeItem(row)

        self.update_options()

    def add_subset(self, subset: Subset):
        """Internal method. Add a subset for use within the add-on.

        Args:
            subset (Subset): Subset to add.
        """
        self.subsets.append(subset)
        self.subsetBox.addItem(subset.get_subset_name())

    def update_subset_ui(self):
        """Update the UI elements for when curr_subset is changed.
        """
        subset = self.subsets[self.curr_subset]
        if self.all_groups:
            self.group_index_box.setEnabled(False)
        else:
            self.group_index_box.setEnabled(True)

        # set group index combobox limits
        self.group_index_box.setMaximum(subset.get_max_index())
        self.group_index_box.setMinimum(0)
        
    def subset_index_sig(self, ind: int):
        """Connected to the changes in the subset combo box, will save config and update the rest of the UI.

        Args:
            ind (int): current index of the subset combo box.
        """
        self.curr_subset = ind
        self.sub_group_ind = 0
        self.group_index_box.setValue(0)
        self.update_subset_ui()

        # write this to config
        self.options_store.get_homework_config(self.notecard_store.deck_name)["last_subset"] = self.curr_subset
        self.options_store.save()

    def allgroups_sig(self, val: int):
        """Connected to the All Groups checkbox.

        Args:
            val (int): Checkbox value
        """
        self.all_groups = bool(val)
        self.update_subset_ui()

    def group_index_sig(self, ind: int):
        """Connected to changes in the group number (subset group index) spinbox.

        Args:
            ind (int): _description_
        """
        self.sub_group_ind = ind

    def preview_subset_sig(self):
        """Connected to the List Button, to create a List view using the current subset settings.
        """
        subset_text = self.subsets[self.curr_subset].get_subset_name() +" - " + ("All" if self.all_groups else "Group "+str(self.sub_group_ind))

        if self.all_groups:
            _subset = self.subsets[self.curr_subset].get_all_cards()
        else:
            _subset = self.subsets[self.curr_subset].get_cards(self.sub_group_ind)
        
        model = ListModel(self.notecard_store, self.options_store, subset=_subset, subset_text=subset_text)
        controller = ListController(model) 
        
        self.list = ListView(model, controller)
        self.list.exec_()

    def show_options_sig(self):
        """Connected to the Options button, to create the Options dialog.
        """
        self.options_dialog = OptionsDialog(self.notecard_store, self.options_store)
        self.options_dialog.buttonBox.accepted.connect(self.update_from_options)
        #self.update_from_options()
        self.options_dialog.show()

    def update_from_options(self):
        """Connected to the accepted button box of an options dialog (so when the options change),
        to update things here in this questions wizard as necessary.
        """
        lesson_size = self.options_store.get_globals(self.notecard_store.deck_name)["lesson_size"]
        for subset in self.subsets:
            subset.lesson_size = lesson_size

        self.update_subset_ui()