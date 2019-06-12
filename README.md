
# Backup_app_teamwork

Simple multiplatform tool for back up. Created as school project.
How to use this program? It´s simple. Just follow these steps:

## Instalation

### Windows && Linux

<pre>

git clone https://github.com/Hojang2/Backup_app_teamwork/
</pre>

### RHEL, Fedora, Centos

<pre>
dnf copr enable hojang/Backup_team_application && sudo dnf install backup_app
dnf install backup_app
</pre>

## Backup

### CLI

<pre>
./main -c -e -p /path/to/directory/for/backup/ -o /path/where/to/store/backup/
</pre>

### GUI

<pre>
1. click on the backup button
2. choose what folder you want to backup and where
3. start it by pressing on backup!
</pre>

## Restore

### CLI

<pre>
./main -c -e -r -p /path/to/backup/[Backup_file.backup] -o /path/to/restore/backup/
</pre>

### GUI

<pre>
1. click on the restore button
2. select your backup file
3. select where you want to restore it
4. click on restore!
</pre>
