from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


#########################################
#####       My Stuff Below          #####
#########################################


@app.route('/test')
def test():
    return render_template('test.html', title = 'Test')

@app.route('/processerror')
def processeserror():
    return render_template('processerror.html', title='Error')

@app.route('/speciesunknown')
def speciesunknown():
    return render_template('speciesunknown.html', title='Mysterious')

#@app.route('/newpage')
#def newpage():
#    return render_template('newpage.html', title='Playground')


@app.route('/results')
def results():
    backend_value = 'complete'  # incomplete until function 2 finishes.
    species = 'test'   # unknown vs. species vs. null to be filled by lookup from csv

    if backend_value == 'incomplete':
        return render_template('loading.html', title='loading') ##HOW TO SET REFRESH TIIMER
    elif backend_value == 'complete':
        if species =='unknown':
            return render_template('speciesunknown.html', title='Mysterious')
        else:
            return render_template('results.html', title='Mysterious')
    else:
        return render_template('processerror.html', title='Error') 
    
############################
        
@app.route('/newresults')
def new_results():
    import pandas
    from google.cloud import storage
    storage_client = storage.Client()

    def download_blob(bucket_name1, source_blob_name1, destination_file_name1):
        bucket = storage_client.get_bucket(bucket_name1)
        blob1 = bucket.blob(source_blob_name1)
        blob1.download_to_filename(destination_file_name1)
        print('Blob {} downloaded to {}.'.format(source_blob_name1, destination_file_name1))

    download_blob('tempml_bucket4', 'query_results.txt', '/tmp/query_results.csv')
    df = pandas.read_csv('/tmp/query_results.csv')
    return render_template('new_results.html', title='New Results', UniqueName = df['UniqueName'][0], GenusName = df['GenusName'][0], SpeciesName = df['SpeciesName'][0], Family = df['Family'][0], Order = df['Order'][0], CommonName = df['CommonName'][0], Leaf_Type = df['Leaf_Type'][0], GrowthRate = df['GrowthRate'][0], MatureHeight_ft = df['MatureHeight_ft'][0], URLLink = df['URLLink'][0], ImageLink = df['ImageLink'][0])

    
############################









    
    
#        if species == 'unknown':
#            return render_template('test.html', title='Mysterious')
#        else:
#            return render_template('index.html', title='wtf?') 
#    else:
#        return render_template('processerror.html', title='Error')
        

#@app.route('/results')
#def results():
#    backend_state = 1 ### We'll make a function that tests backend to see if ready, broken, etc.
#    species = 'spot'

#    if backend_state == 1 and species == 'unknown':
#        return render_template('speciesunknown.html', title='Mysterious')
    
#    elif backend_state == 1:
#        return render_template('results.html', title='Classification Results')
    
#    elif backend_state == 0:
#        return render_template('processerror.html', title='Error')
    
#    else:
#        return render_template('processerror.html', title='Error')

##    For above, we'll need function that keeps checking to see output form backend.

    

#@app.route('/prediction')
#def prediction():
#   if output file is a species name
#       render everything in the output file
#   elif output file is unknown_species
#       render "STUMPED" template (function ran but species not known)
#   elif error in returning file:
#       if counter < threshold
#           render loading page#
#           add to counter
#           refresh in 10 seconds
#       if counter >= threshold:
#           render error page (something went wrong, function did not produce output).
#

#try:
#    f = open(fname, 'rb')
#except OSError:
#    print "Could not open/read file:", fname
#    sys.exit()
#
#with f:
#    reader = csv.reader(f)
#    for row in reader:
#        pass #do stuff here
#








##########   OLD INDEX BELOW:

#def index():
#    user = {'username': 'Albus'}
#    posts = [
#        {
#            'author': {'username': 'Minerva'},
#            'body': 'Disloyalty!?'
#        },
#        {
#            'author': {'username': 'Severus'},
#            'body': 'I miss Lilly'
#        }
#    ]
#    return render_template('index.html', title='Home', user=user['username'], posts=posts)

