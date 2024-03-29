*Course work for the Software Development Methods -course,  
Helsinki University Department of Computer Science, Fall 2022*



# Kanji Flash Card App


## Documentation

* [Release for the course deadline](https://github.com/johannalehto/ot-harjoitustyo/releases/tag/course-release)

* [User manual](https://github.com/johannalehto/ot-harjoitustyo/blob/main/kanji-app/documentation/user_manual.md)

* [Software specification](https://github.com/johannalehto/ot-harjoitustyo/blob/master/kanji-app/documentation/software_specification.md)

* [Software architecture](https://github.com/johannalehto/ot-harjoitustyo/blob/master/kanji-app/documentation/software_architecture.md)

* [Test documentation](https://github.com/johannalehto/ot-harjoitustyo/blob/main/kanji-app/documentation/test_documentation.md)

* [Changelog](https://github.com/johannalehto/ot-harjoitustyo/blob/master/kanji-app/documentation/changelog.md)

* [Work hours tracking](https://github.com/johannalehto/ot-harjoitustyo/blob/master/kanji-app/documentation/tyoaikakirjanpito.md)


## Installation


Install application dependencies with command:

```bash
poetry install
```


## Command line

### Starting the application: 

```bash
poetry run invoke start
```

### Testing

```bash
poetry run invoke test
```

### Test coverage report

```bash
poetry run invoke coverage-report
```

Report will be generated in _htmlcov_-directory.

### Pylint

Static code analysis can be run with:

```bash
poetry run invoke lint
```




