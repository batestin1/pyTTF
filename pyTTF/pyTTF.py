import json
from pathlib import Path


def pyTTF():
    path = Path("./infra")
    path.mkdir(parents=True, exist_ok=True)

    ###create a file destroy ###
    file_destroy = 'destroy=false'
    destroy = open("infra/destroy.yml", "w")
    destroy.write(file_destroy)


    #### create a resource_to_delete.json ###
    file_resource = {
        "resource_to_remove": [

        ]
    }
    resource = open("infra/resource_to_delete.json", "w")
    json.dump(file_resource, resource, allow_nan=True, indent=True, separators=(',',':'))

    ##########create a main.tf####################################

    txt = """

    #######################################################################################
    # In this file you will put your infrastructure code.
    # The is no need to add a "provider" block - the pipeline does it for you
    # you can ccreate more .tf files in this folder or subfolders to organize your templates
    # but the main.tf files is MANDATORY for the pipeline in this BANK!
    ########################################################################################

    resource "<name-of-your-resource>" "<alias-for-your-resource>" {
        name = ""

    }
    """
    main_tf = open("infra/main.tf", "w")
    main_tf.write(txt)

    ###### create the variable.tf ############
    vartxt = """
    ###########################################################################################
    #In this file, you can add variables to use in your code.
    #e.g. creating a string parameter to define the environment:
    #
    #variable "image_id" {
    #    type = string
    #}
    #
    #You can change the name of this file  or use multiple files for variable
    #
    #variables example here down:
    ######################################################################################################

    variable "name"{
        type = string
        description = "the name of parameter. Cannot Be a Password ou Sensitive information"
        default = "value to put"
    }
    """
    variable = open("infra/variables.tf", "w")
    variable.write(vartxt)


    #################################
    #### the invetories ############

    ### making path ######
    path = Path("./infra/inventories/homolog")
    path.mkdir(parents=True, exist_ok=True)
    path = Path("./infra/inventories/dev")
    path.mkdir(parents=True, exist_ok=True)
    path = Path("./infra/inventories/prod")
    path.mkdir(parents=True, exist_ok=True)
    txtnull=''
    homo = open("infra/inventories/homolog/terraform.tfvars", "w")
    homo.write(txtnull)
    dev = open("infra/inventories/dev/terraform.tfvars", "w")
    dev.write(txtnull)
    homo.write(txtnull)
    prod = open("infra/inventories/prod/terraform.tfvars", "w")
    prod.write(txtnull)



