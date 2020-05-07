//
//  DriverOrdersCell.swift
//  CRMClient
//
//  Created by Nurzhan Ababakirov on 5/7/20.
//  Copyright © 2020 Nurzhan Ababakirov. All rights reserved.
//

import UIKit

class DriverOrdersCell: UITableViewCell {


    @IBOutlet weak var idLabel: UILabel!
    @IBOutlet weak var nameLabel: UILabel!
    @IBOutlet weak var dateLabel: UILabel!
    
    func configure(orders: DriverOrderStruct) {
        
        nameLabel.text = ("Название: \(orders.name)")
        idLabel.text = ("№\(String(orders.id))")
        //dateLabel.text = orders.fromOrder

        
    }
}
