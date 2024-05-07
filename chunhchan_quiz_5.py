def hawkid():
    return(["Chun Hang Chan", "chunhchan"])

def createBufferAirpot(fcPoint, featureFieldName, enpFieldName, workspace):
    
    import arcpy
    import arcpy
    import sys

    try: 
        arcpy.env.workspace = workspace
        arcpy.management.AddField(fcpoint, "Buffer", "TEXT")
        with arcpy.da.UpdateCursor(fcpoint, [featureFieldName, enpFieldName, "Buffer"]) as cursor:
        for row in cursor: 
            feature = row[0]
            enp = row[1]
        
            if feature == "airport":
                if enp > 10000:
                    row[2] = 15000
                elif 1000 < enp <= 10000:  
                    row[2] = 10000
                else:
                    row[2] = 0
        
            elif feature == "seaplane base":  
                if enp > 1000:
                    row[2] = 7500
                else:
                    row[2] = 0
        
            cursor.updateRow(row)
        fcbuffer = "buffer_" + fcPoint
        arcpy.Buffer_analysis(fcPoint, fcbuffer, "Buffer")
        arcpy.CopyFeatures_management("buffer_airports", workspace)
        arcpy.FeatureClassToShapefile_conversion(fcbuffer, workspace)
    except acrpy.ExecuteError:
        print(arcpy.GetMEssages())
