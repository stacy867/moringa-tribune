from django.test import TestCase
from .models import Editor,Article,tags

class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.james= Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')
        self.aristote= Editor(first_name = 'Aristote', last_name ='Katy', email ='katy.aristote@moringaschool.com')
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.james,Editor))

    def test_save_method(self):
        self.james.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

    def test_delete(self):
        self.james.save_editor()
        self.aristote.save_editor()
        editor = Editor.objects.filter(first_name="Aristote").first()
        delete= Editor.objects.filter(id = editor.id).delete()
        editors = Editor.objects.all()
        print(editors)
        self.assertTrue(len(editors)== 1)

    def test_update(self):
        self.james.save_editor()
        editor = Editor.objects.filter(first_name="James").first()
        update=Editor.objects.filter(id=editor.id).update(first_name="Brenda")
        updated= Editor.objects.filter(first_name="Brenda").first()
        self.assertTrue(editor.first_name,updated.first_name)
    
    def test_display(self):
        self.james.save_editor()
        editors=Editor.objects.all()
        self.assertTrue(len(editors)==1)