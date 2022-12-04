#### Ohjelmistotekniikka syys 2022

# Kanji Flash Card App

## Documentation

* [Software specification](https://github.com/johannalehto/ot-harjoitustyo/blob/master/kanji-app/documentation/software_specification.md)

* [Software architecture](https://github.com/johannalehto/ot-harjoitustyo/blob/master/kanji-app/documentation/software_architecture.md)

* [Changelog](https://github.com/johannalehto/ot-harjoitustyo/blob/master/kanji-app/documentation/changelog.md)

* [Työaikakirjanpito](https://github.com/johannalehto/ot-harjoitustyo/blob/master/kanji-app/documentation/tyoaikakirjanpito.md)


## Installation

Install application dependencies with command:

```bash
poetry install
```

<!-- 2. Run initialization with command:

```bash
poetry run invoke build
```

3. Start application with command:

```bash
poetry run invoke start
``` -->

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




