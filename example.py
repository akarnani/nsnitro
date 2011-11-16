import nsnitro
from nsresources.nsservice import *
import json

nitro = nsnitro.NSNitro('localhost', 'api_user', 'api_user')
nitro.login()

# add service test

addservice = NSService()
addservice.set_name("aurora_testnitroadd")
addservice.set_servername("mp-be002")
addservice.set_servicetype("HTTP")
addservice.set_port(11111)
NSService.add(nitro, addservice)

# get service test

service = NSService()
service.set_name("aurora_testnitroadd")
service = service.get(nitro, service)
print service.get_name() + ": " + service.get_svrstate()

# disable service test

disservice = NSService()
disservice.set_name("aurora_testnitroadd")
NSService.disable(nitro, disservice)

service = NSService.get(nitro, "aurora_testnitroadd")
print service.get_name() + ": " +  service.get_svrstate()

# enable service test

enservice = NSService()
enservice.set_name("aurora_testnitroadd")
NSService.enable(nitro, enservice)

service = NSService.get(nitro, "aurora_testnitroadd")
print service.get_name() + ": " +  service.get_svrstate()


# rename service test

renservice = NSService()
renservice.set_name("aurora_testnitroadd")
renservice.set_newname("aurora_testnitroadd_rename")
NSService.rename(nitro, renservice)

# rename service back test

renservice = NSService()
renservice.set_name("aurora_testnitroadd_rename")
renservice.set_newname("aurora_testnitroadd")
NSService.rename(nitro, renservice)

# delete service test

NSService.delete(nitro, "aurora_testnitroadd")
try:
        service = NSService.get(nitro, "aurora_testnitroadd")
except NSNitroError, e:
        print e.message
