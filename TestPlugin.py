import sublime, sublime_plugin

class AddPipeToStartOfEachLineCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command('expand_selection_to_paragraph')
        self.view.run_command('split_selection_into_lines')
        self.view.run_command('move_to', {"extend": "false", "to": "bol"})
        self.view.run_command('move_to', {"extend": "false", "to": "bol"})
        self.view.run_command('insert', {"characters": "|"})

class SquirrelTableToPipeTableCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command('expand_selection_to_paragraph')
        e = self.view.begin_edit('squirreltable')
        regions = self.view.find_all('\t')
        for region in regions:
            if region.empty():
                continue
            self.view.replace(edit, region, "|")
        self.view.run_command('split_selection_into_lines')
        self.view.run_command('move_to', {"extend": "false", "to": "bol"})
        self.view.run_command('move_to', {"extend": "false", "to": "bol"})
        self.view.run_command('insert', {"characters": "|"})
        self.view.run_command('move_to', {"extend": "false", "to": "eol"})
        self.view.run_command('insert', {"characters": "|"})
        self.view.run_command('table_editor_enable_for_current_view')
        self.view.run_command('table_editor_align')
        self.view.end_edit(e)