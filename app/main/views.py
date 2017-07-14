from . import main
from .. import db
from ..models import Company, Contact


@main.route('/',methods=['GET','TOUCH'])
def index():
	return 'Hello world.'