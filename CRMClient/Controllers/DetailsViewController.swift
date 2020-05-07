//
//  DetailsViewController.swift
//  CRMClient
//
//  Created by Nurzhan Ababakirov on 2/22/20.
//  Copyright © 2020 Nurzhan Ababakirov. All rights reserved.
//

import UIKit

class DetailsViewController: UIViewController {


    @IBOutlet weak var idOrder: UILabel!
    @IBOutlet weak var nameOrder: UILabel!
    @IBOutlet weak var priceLabel: UILabel!
    @IBOutlet weak var cargoLabel: UILabel!
    @IBOutlet weak var loadLabel: UILabel!
    @IBOutlet weak var autoLabel: UILabel!
    @IBOutlet weak var releaseYearLabel: UILabel!
    @IBOutlet weak var reqLabel: UILabel!
    @IBOutlet weak var statusLabel: UILabel!
    @IBOutlet weak var clientLabel: UILabel!
    
    var nameOrderT = ""
    var idOrderT = ""
    var priceT = ""
    var cargoT = ""
    var loadT = ""
    var autoT = ""
    var reqT = ""
    var relT = ""
    var statusT = ""
    var clientT = ""
    
    override func viewDidLoad() {
        super.viewDidLoad()
        nameOrder.text = nameOrderT
        idOrder.text = idOrderT
        priceLabel.text = priceT
        cargoLabel.text = cargoT
        loadLabel.text = loadT
        autoLabel.text = autoT
        releaseYearLabel.text = relT
        reqLabel.text = reqT
        statusLabel.text = statusT
        clientLabel.text = clientT
    }
    
    func configure(order: OrderStruct){
        nameOrderT = order.name
        idOrderT = "Заказ № \(String(order.id))"
        priceT = "Цена: \(order.priceClient) сом"
        cargoT = "Тип груза: \(order.typeCargo)"
        loadT = "Тип погрузки: \(order.typeLoading)"
        autoT = "Тип авто: \(order.typeAuto)"
        relT = "Год выпуска авто: \(order.autoReleaseYear)"
        reqT = "Требования погрузки: \(order.requirementsLoading)"
        statusT = "Статус заказа: \(order.orderStatus)"
        clientT = "Заказчик: \(order.user)"
        
    }

}


