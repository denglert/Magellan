#!/bin/bash

DIR=$1

BACKUP_DIR='./backup'
PREPATH='./results/spectrum'

# Protection for unset DIR, in order not to wipe out ${PREPATH} directory.
if [ -z ${DIR+x} ]; then
   echo "Variable DIR is unset. Please specify DIR variable.;"
else
   if [ -d ${PREPATH}/${DIR} ]; then
   echo
   echo "Warning!";
   echo
   echo "There is already a ${PREPATH}/${DIR}. Making copy to ./backup";
      cp -rf ${PREPATH}/${DIR}/ ./backup/${DIR}/;
      rm -rf ${PREPATH}/${DIR};
   fi
   
   echo "Creating new working directory ${PREPATH}/${DIR}."
   echo
   mkdir -p ${PREPATH}/${DIR}/
fi
