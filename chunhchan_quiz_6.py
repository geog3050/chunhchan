import arcpy
calculatePercentAreaOfPolygonAInPolygonB(input_geodatabase, fcPolygonA, fcPolygonB, idFieldPolygonB):
    arcpy.env.workspace = input_geodatabase
    idfield = idFieldPolygonB
    arcpy.management.AddField('block_groups', "idfield", 'string')
    with arcpy.da.UpdateCursor('block_groups', 'idfield') as cursor: #I used this to create a distinct ID value for each blockgroup
    current = 1
    for row in cursor:
        row[0] = current
        current = current +1
        cursor.updateRow(row)
    arcpy.env.overwriteOutput = False
    parks = 'parks'
    blockg = 'block_groups'

    #This block below was exported through copy python command in the Intersect Tool. 
    arcpy.analysis.Intersect(
    in_features="parks #;block_groups #",
    out_feature_class = input_geodatabase + "\parks_Intersect",
    join_attributes="ALL",
    cluster_tolerance=None,
    output_type="INPUT")
    
    parks_intersect_layer = "parks_Intersect"
    block_groups_layer = "block_groups"
    area_sum_dict = {}
    #The block below calculate the total area of parks with the same idfield after intersection
    with arcpy.da.SearchCursor(parks_intersect_layer, ["idfield", "Shape_Area"]) as cursor:
    for row in cursor:
        idfield = row[0]
        shape_area = row[1]
        if idfield in area_sum_dict:
            area_sum_dict[idfield] += shape_area
        else:
            area_sum_dict[idfield] = shape_area
    #The block below inputs the value of the total parks area in to the areaA_sqmi field with the same idfield row 
    with arcpy.da.UpdateCursor(block_groups_layer, ["idfield", "areaA_sqmi"]) as cursor:
    for row in cursor:
        idfield = row[0]
        if idfield in area_sum_dict:
            row[1] = area_sum_dict[idfield]
            cursor.updateRow(row)
    #The block below calculates the areaA_pct in the block_groups atttribute table through simple division, also take cares of division by zero
    with arcpy.da.UpdateCursor(block_groups_layer, ["areaA_sqmi", "area_sqmi", "areaA_pct"]) as cursor:
    for row in cursor:
        areaA_sqmi = row[0]
        area_sqmi = row[1]
        if area_sqmi != 0:
            row[2] = (areaA_sqmi / area_sqmi) * 100
        else:
            row[2] = 0  
        cursor.updateRow(row)
