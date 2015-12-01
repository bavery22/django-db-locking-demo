from django.core.management.base import NoArgsCommand, CommandError




class Command(NoArgsCommand):
    args = ""
    help = "prints cows"






    def handle_noargs(self, **options):
        print "cows rule!"
