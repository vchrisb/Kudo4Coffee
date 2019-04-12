
# migrate database
cf run-task kudo4coffee "python manage.py migrate" --name migrate
# create initial superuser
cf run-task kudo4coffee "echo \"from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@myproject.com', 'password')\" | python manage.py shell" --name create_initial_superuser
