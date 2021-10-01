pusher() {
    #requirment needs git installed #
    ## to-do
    # add git installing facility[with permission] after checking if it is installed or not
    echo "Enter your commit message: "
    read x
    echo "Your commit message is- ${X}"
    git add .
    git commit -am "${x}"
    git push -v
}

pusher