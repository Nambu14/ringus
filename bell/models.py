from django.db import models


# Objects from the model schema of MVC

class Account(models.Model):
    # Account class represents the device owner's information
    # accountId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)

    def __str__(self):
        return self.name + ' ' + self.surname


class Visitor(models.Model):
    # Visitor class represents each visitor stored in the doorbell system
    # visitorId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)

    def __str__(self):
        return self.name + ' ' + self.surname


class Visit(models.Model):
    # shit happens
    visitor = models.ForeignKey(Visitor)
    date = models.DateTimeField('Fecha de Visita')

    def __str__(self):
        return self.visitor.__str__() + ' ' + self.date.__str__()


class Message(models.Model):
    # Message class represents each message delivered from a visitor to the owner
    # messageId = models.AutoField(primary_key=True)
    visitor = models.ForeignKey(Visitor)
    # audio files handling needs to be defined
    # message = ??
    date = models.DateTimeField('Message Date')
    # duration = ??
    # size = ??


class Notification(models.Model):
    # notificationId = models.AutoField(primary_key=True)
    visitor = models.ForeignKey(Visitor)
    # handling audio files seems not easy
    notification_text = models.CharField('Notification Message', max_length=200)
    date = models.DateTimeField('Notification Date')
    # duration = ??
    # size =  ??

    def __str__(self):
        return self.notification_text + ' ' + self.date.__str__()

