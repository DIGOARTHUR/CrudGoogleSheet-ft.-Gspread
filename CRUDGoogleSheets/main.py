import gspread
import math
import logging
import logging.config

logging.config.fileConfig('simple_loggin.ini')
logger = logging.getLogger('root')


def connectGoogleSheets():

    gc = gspread.service_account(filename='credentials.json')  # API connection
    sh = gc.open_by_key('1gI7G6xh6H4_2lz1yujChxiZfdYda3PURjmDmLugD2CM')  # table id GoogleSheets
    worksheet = sh.sheet1  # Object that will give conditions and functions to access the table: Create, Read, Update and Delete, for example.
    logger.info('Connecting Google Sheets Engenharia de Software Desafio [Diego Arthur]')
    return worksheet


def updateSituation_checkingFrequency():
    logger.info('       Update Situation')
    worksheet.update_cell(row, 7, 'Reprovado por Falta')
    worksheet.update_cell(row, 8, 0)
    logger.info('           Score for final exam')


def sumScore(totalScore):
    for col in range(4, 7):
        totalScore += int(worksheet.cell(row, col).value)
    return totalScore


def scoreAverage(totalScore):
    m = totalScore / 3
    return m


def updateSituation_checkingScore(situation):
    logger.info('       Update Situation')
    if situation == 1:
        worksheet.update_cell(row, 7, 'Reprovado por Nota')
        worksheet.update_cell(row, 8, 0)

        colorCell = "G"+str(row)+":"+"G"+ str(row)
        worksheet.format(colorCell, {
            "backgroundColor": {
            "red": 0.0,
            "green": 0.0,
            "blue": 1.0
         }})
        logger.info('           Score for final exam')
    elif situation == 2:
        worksheet.update_cell(row, 7, 'Exame Final')

        naf = str(math.ceil((50 * 2) - m))  # Being 5 <= (m + naf)/2, have
        naf = '>=' + naf
        worksheet.update_cell(row, 8, naf)
        colorCell = "A"+str(row)+":"+"G"+ str(row)
    
        worksheet.format(colorCell, {
            "backgroundColor": {
            "red": 1.0,
            "green": 1.0,
            "blue": 0.6
         }})
        logger.info('           Score for final exam')
    elif situation == 3:
        worksheet.update_cell(row, 7, 'Aprovado')
        worksheet.update_cell(row, 8, 0)
        colorCell = "A"+str(row)+":"+"G"+ str(row)
    
        worksheet.format(colorCell, {
            "backgroundColor": {
            "red": 0.0,
            "green": 1.0,
            "blue": 0.0
         }})
        logger.info('           Score for final exam')


########  MAIN  ################

worksheet = connectGoogleSheets()  # call function for connect GoogleSheets

try:
    for row in range(4, 28):  # line by line from the first(4) name to the last name (27)
        logger.info('Read Student enrollment: %s', row - 3)
        totalScore = 0
        frequencyNumber = int(worksheet.cell(row, 3).value)  #

        # CHECKS IF IT'S DISAPPROVED BY FREQUENCY
        logger.info('   Checking Frequency')
        if frequencyNumber > (60 * (25 / 100)):
            updateSituation_checkingFrequency()

        # ELSE CHECK THE SCORES
        else:
            logger.info('   Checking Score')
            totalScore = sumScore(totalScore)
            m = scoreAverage(totalScore)

            if m < 50:  # check if it's disapproved
                updateSituation_checkingScore(1)


            elif m < 70 and m >= 50:  # check if it's in final exam
                updateSituation_checkingScore(2)


            elif m >= 70:  # check if it's approved
                updateSituation_checkingScore(3)


except:
    logger.error('Quota exceeded for quota metric (Read requests) and (limit Read requests per minute per user) of service.')
    logger.info('Please check your Google Cloud Platform service at https://cloud.google.com/compute/quotas')