# SBGBook

Playground for Standards Based Grading app, just toying with ideas.

Server Side: Pyramid product sbg_book 

    pyramid/            primary source directory
    pyramid/sbg_book/   python product directory
    pyramid/scratch     temporary/cache/production data (not held in repository)

Getting Started with Pyramid

    #
    # get into virtual environment
    #
    python3.5 -m venv ~/vsbg
    . ~/vsbg/bin/activate
    
    #
    # set up repository
    #
    
    git clone git@github.com:sspickle/SBGBook.git
    cd SBGBook/
    cd pyramid/
    pip install -U pip
    pip install -e .
    cd sbg_book
    
    #
    # install client side javascript libs
    #
    
    npm install
    bower install
    cd ..
    
    #
    # populate database
    #
    
    mkdir scratch
    initialize_sbg_book_db development.ini 
    import_csv_people development.ini sbg_book/test_data/students.csv 
    
    #
    # Go!
    #
    
    pserve development.ini --reload




