from unicodedata import normalize

class generate_email:
    def __init__(self,parameters):
        parameters = parameters.lower()
        parameters = normalize('NFKD',parameters).encode('ASCII','ignore').decode('ASCII')
        params = parameters.split()
        i = len(params)
        for j in range(i):
            params.append(params[j][0])
        emails = []
        iduff = '@id.uff.br'
        emails.append(params[0] + '_' + params[1] + iduff)
        emails.append(params[0] + params[4] + params[5] + iduff)
        emails.append(params[0] + params[2] + iduff)
        emails.append(params[3] + params[2] + iduff)
        emails.append(params[3] + params[1] + params[2] + iduff)
        self.emails = emails


