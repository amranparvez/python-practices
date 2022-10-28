def patient_info (*args,**kwargs):

  print(args)
  print(kwargs)



name=['alan ','border','steve','tendulkar']
diseases={'eye':"conganctivities",'age':'57','age':"105"}
patient_info(*name ,**diseases)

