###################################################################### 
# Edit the following function definition, replacing the words
# 'name' with your name and 'hawkid' with your hawkid.
# 
# Note: Your hawkid is the login name you use to access ICON, and not
# your firsname-lastname@uiowa.edu email address.
# 
# def hawkid():
#     return(["Caglar Koylu", "ckoylu"])
###################################################################### 
def hawkid():
    return(["Chun Hang Chan", "chunhchan"])

###################################################################### 
# Problem 1 (10 Points)
#
# This function reads all the feature classes in a workspace (folder or geodatabase) and
# prints the name of each feature class and the geometry type of that feature class in the following format:
# 'states is a point feature class'

###################################################################### 

import arcpy
import os
def printFeatureClassNames(workspace):
    try: 
        arcpy.env.workspace = workspace
        fcs = arcpy.ListFeatureClasses()
        for i in fcs:
            desc = arcpy.Describe(i)
            if desc.shapeType == "Polygon":
                print(fc + " is a polygon feature class")
            elif desc.shapeType == "Polyline":
                print(fc + " is a polyline feature class")
            elif desc.shapeType == "Point":
                print(fc + " is a point feature class")
            else:
                print("Type unknown")
    except arcpy.ExecuteError:  
        msgs = arcpy.GetMessages(2) 
        arcpy.AddError(msgs) 
        print("Tool Error:", msgs)



###################################################################### 
# Problem 2 (20 Points)
#
# This function reads all the attribute names in a feature class or shape file and
# prints the name of each attribute name and its type (e.g., integer, float, double)
# only if it is a numerical type

###################################################################### 
def printNumericalFieldNames(inputFc, workspace):
    try: 
        arcpy.env.workspace = workspace
        fields = arcpy.ListFields(inputFc)
        for field in fields:
            k = (field.type)
            name = (field.name)
            if k == 'Integer' or k == 'Double' or k == 'Float':
                print(name+ " has a type of " + k)
    except arcpy.ExecuteError:  
        msgs = arcpy.GetMessages(2) 
        arcpy.AddError(msgs) 
        print("Tool Error:", msgs
###################################################################### 
# Problem 3 (30 Points)
#
# Given a geodatabase with feature classes, and shape type (point, line or polygon) and an output geodatabase:
# this function creates a new geodatabase and copying only the feature classes with the given shape type into the new geodatabase

###################################################################### 
def exportFeatureClassesByShapeType(input_geodatabase, shapeType, output_geodatabase):
    arcpy.env.workspace = input_geodatabase
    import os
    try:
        out_folder_path = os.path.dirname(os.path.abspath(output_geodatabase))
        arcpy.CreateFileGDB_management(out_folder_path, output_geodatabase)
        featureclasses = arcpy.ListFeatureClasses()
        for fc in featureclasses:
            describe_fc = arcpy.Describe(fc)
            if describe_fc.shapeType == shapeType:  
                arcpy.Copy_management(fc, output_geodatabase + "/" + fc)
    except arcpy.ExecuteError: 
        msgs = arcpy.GetMessages(2) 
        arcpy.AddError(msgs) 
        print("Tool Error:", msgs)

###################################################################### 
# Problem 4 (40 Points)
#
# Given an input feature class or a shape file and a table in a geodatabase or a folder workspace,
# join the table to the feature class using one-to-one and export to a new feature class.
# Print the results of the joined output to show how many records matched and unmatched in the join operation. 

###################################################################### 
def exportAttributeJoin(inputFc, idFieldInputFc, inputTable, idFieldTable, workspace):
    try: 
        arcpy.env.workspace = workspace
        arcpy.management.JoinField(inputFc, idFieldInputFc, inputTable, idFieldTable)
        a_count = int(arcpy.GetCount_management(inputFc)[0])
        b_count = int(arcpy.GetCount_management(inputTable)[0])
        matched_count = min(a_count, b_count)
        unmatched_count = abs(a_count - b_count)
        if a_count <= b_count:
            print(f"Matched count is: {matched_count}. Unmatched count is: {unmatched_count}.")
        else:
            print(f"Matched count is: {matched_count}. Unmatched count is: {unmatched_count}.")
    
        return inputFc
    
    except:arcpy.ExecuteError: 
        msgs = arcpy.GetMessages(2)  
        arcpy.AddError(msgs) 
        print("Tool Error:", msgs)

######################################################################
# MAKE NO CHANGES BEYOND THIS POINT.
######################################################################
if __name__ == '__main__' and hawkid()[1] == "hawkid":
    print('### Error: YOU MUST provide your hawkid in the hawkid() function.')
