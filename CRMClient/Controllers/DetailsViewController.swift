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
    @IBOutlet weak var noHoles: UILabel!
    @IBOutlet weak var dry: UILabel!
    @IBOutlet weak var noGaps: UILabel!
    @IBOutlet weak var noPatches: UILabel!
    @IBOutlet weak var width: UILabel!
    @IBOutlet weak var height: UILabel!
    @IBOutlet weak var length: UILabel!
    @IBOutlet weak var weight: UILabel!
    @IBOutlet weak var driver: UILabel!
    @IBOutlet weak var phone: UILabel!
    
    var nameOrderT = ""
    var idOrderT = ""
    var priceT = ""
    var cargoT = ""
    var loadT = ""
    var autoT = ""
    var reqT = ""
    var relT = ""
    var statusT = ""
    var holesT = ""
    var dryT = ""
    var noGapsT = ""
    var noPatchesT = ""
    var widthT = ""
    var heightT = ""
    var lengthT = ""
    var weightT = ""
    var driverT = ""
    var phoneT = ""
    
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

        noHoles.text = holesT
        dry.text = dryT
        noGaps.text = noGapsT
        noPatches.text = noPatchesT
        width.text = widthT
        height.text = heightT
        length.text = lengthT
        weight.text = weightT
        driver.text = driverT
        phone.text = phoneT
        
        
    }
    
    func configure(order: OrderStruct){
        nameOrderT = order.name
        idOrderT = "Заказ № \(String(order.id))"

        priceT = "Цена: \(order.priceClient) сом"
        cargoT = "Тип груза: \(order.typeCargo)"
        loadT = "Тип погрузки: \(order.typeLoading)"
        autoT = "Тип авто: \(order.typeAuto)"
        var car = ""
        switch order.typeAuto {
        case "1":
            car = "Тентованный полуприцеп (еврофура)"
        case "2":
            car = "Jumbo"
        default:
            car = "Рефрижераторный фургон"
        }
        autoT = "Тип авто: \(car)"
        relT = "Год выпуска авто: \(order.autoReleaseYear)"
        reqT = "Требования погрузки: \(order.requirementsLoading)"
        
        statusT = "Статус заказа: \(order.orderStatus)"
        
        var holes = ""
        switch order.stateAwning.noHoles{
            case false:
            holes = "Да"
            default:
            holes = "Нет"
        }
        
        var dry = ""
        switch order.stateAwning.dry {
        case false:
            dry = "Да"
        default:
            dry = "Нет"
        }
        
        var gaps = ""
        switch order.stateAwning.noGaps {
        case false:
            gaps = "Да"
        default:
            gaps = "Нет"
        }
        
        var patches = ""
        switch order.stateAwning.noPatches {
        case false:
            patches = "Да"
        default:
            patches = "Нет"
        }
        
        
        holesT = holes
        dryT = dry
        noGapsT = gaps
        noPatchesT = patches
        
        var unit = ""
        switch order.volume.unit{
            case 4:
            unit = " см"
            
        default:
            unit = " м"
        }
        
        var wmu = ""
        switch order.weightMeasurementUnit {
        case 1:
            wmu = " кг"
        default:
            wmu = " т"
        }
        
        widthT = "Ширина:  \(String(order.volume.width))\(unit)"
        lengthT = "Длина: \(String(order.volume.length))\(unit)"
        heightT = "Высота: \(String(order.volume.height))\(unit)"
        weightT = "Вес: \(String(order.weight))\(wmu)"
        driverT = "Водитель: \(order.driver.last_name) \(order.driver.first_name)"
        phoneT = "Номер телефона: \(order.driver.phone)"
        
        
    }

}


