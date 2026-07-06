from {{ cookiecutter.project_slug }}.main import main

def test_main_runs(capsys):
    main()
    captured = capsys.readouterr()
    assert "{{ cookiecutter.project_name }}" in captured.out