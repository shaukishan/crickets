
from odoo import api, fields, models
from datetime import datetime
from odoo.exceptions import UserError



class Team(models.Model):
    _name = 'cricket.team'

    @api.depends('players')
    def get_players_count(self):
        print self
        for team in self:
            count = 0
            for x in team.players:
                count += 1
            team.players_count = count

    name = fields.Char()
    players_count = fields.Integer(compute='get_players_count')
    # Old API - fields.function(function_name, type='' )

    experience = fields.Float()
    on_tour = fields.Boolean()
    players = fields.One2many('res.partner', 'team', 'Players')


# class Players(models.Model):
#     _name = 'cricket.player'

    
#     name = fields.Char()
#     team = fields.Many2one('cricket.team', 'Team')
#     dob = fields.Date('Date of Birth')
#     age = fields.Integer(compute='get_player_age')
#     contact_no = fields.Char(size=10)

# class PlayerPartner(models.Model):
#     _name = 'cricket.player.1'
#     _inherit = 'res.partner'

#     is_player = fields.Boolean()
#     


class PlayerParter(models.Model):
    _inherit = 'res.partner'

    @api.depends('dob')
    def get_player_age(self):
        for player in self:
            age = 0
            if player.dob:
                age = (datetime.now() - datetime.strptime(player.dob, '%Y-%m-%d')).days/365
            player.age = age

    is_player = fields.Boolean()
    team = fields.Many2one('cricket.team', 'Team')
    dob = fields.Date('Date of Birth')
    age = fields.Integer(compute='get_player_age')

    @api.model
    def create(self, vals):
        print vals
        if 'team' in vals and vals['team']:
            team = self.env['cricket.team'].browse(vals['team'])
            if team.on_tour:
                raise UserError('Team is on tour. You can not add players on it.')
        return super(PlayerParter, self).create(vals)
