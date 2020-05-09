//
//  DriverDetailsViewController.swift
//  CRMClient
//
//  Created by Nurzhan Ababakirov on 5/8/20.
//  Copyright © 2020 Nurzhan Ababakirov. All rights reserved.
//

import UIKit


class DriverDetailsViewController: UIViewController {
    
    @IBOutlet weak var idOrder: UILabel!
    @IBOutlet weak var nameOrder: UILabel!
    @IBOutlet weak var priceLabel: UILabel!
    @IBOutlet weak var cargoLabel: UILabel!
    @IBOutlet weak var loadLabel: UILabel!
    @IBOutlet weak var autoLabel: UILabel!
    @IBOutlet weak var releaseYearLabel: UILabel!
    @IBOutlet weak var reqLabel: UILabel!
    @IBOutlet weak var noHoles: UILabel!
    @IBOutlet weak var dry: UILabel!
    @IBOutlet weak var noGaps: UILabel!
    @IBOutlet weak var noPatches: UILabel!
    @IBOutlet weak var width: UILabel!
    @IBOutlet weak var height: UILabel!
    @IBOutlet weak var length: UILabel!
    @IBOutlet weak var weight: UILabel!
    @IBOutlet weak var username: UILabel!
    @IBOutlet weak var email: UILabel!
    @IBOutlet weak var address: UILabel!
    @IBOutlet weak var status: UILabel!
    
     var refresher: UIRefreshControl!
    
    var nameOrderT = ""
    var idOrderT = ""
    var priceT = ""
    var cargoT = ""
    var loadT = ""
    var autoT = ""
    var reqT = ""
    var relT = ""
    var holesT = ""
    var dryT = ""
    var noGapsT = ""
    var noPatchesT = ""
    var widthT = ""
    var heightT = ""
    var lengthT = ""
    var weightT = ""
    var usernameT = ""
    var emailT = ""
    var addressT = ""
    var statusT = ""

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
            noHoles.text = holesT
            dry.text = dryT
            noGaps.text = noGapsT
            noPatches.text = noPatchesT
            width.text = widthT
            height.text = heightT
            length.text = lengthT
            weight.text = weightT
            username.text = usernameT
            email.text = emailT
            address.text = addressT
            status.text = statusT
        
    }
    
    func configure(orders: [DriverOrderStruct]){
        nameOrderT = orders[0].name
        idOrderT = "Заказ № \(String(orders[0].id))"
             UserDefaults.standard.set(orders[0].id, forKey: "id")
        print(UserDefaults.standard.value(forKey: "id"))
        priceT = "Цена: \(orders[0].priceClient) сом"
        cargoT = "Тип груза: \(orders[0].typeCargo)"
        loadT = "Тип погрузки: \(orders[0].typeLoading)"
        var car = ""
        switch orders[0].typeAuto {
        case 1:
            car = "Тентованный полуприцеп (еврофура)"
        case 2:
            car = "Jumbo"
        default:
            car = "Рефрижераторный фургон"
        }

        autoT = "Тип авто: \(car)"
        relT = "Год выпуска авто: \(orders[0].autoReleaseYear)"
        reqT = "Требования погрузки: \(orders[0].requirementsLoading)"
        statusT = "Статус: \(orders[0].orderStatus)"
        var holes = ""
        switch orders[0].stateAwning.noHoles{
            case false:
            holes = "Да"
            default:
            holes = "Нет"
        }
        
        var dry = ""
        switch orders[0].stateAwning.dry {
        case false:
            dry = "Да"
        default:
            dry = "Нет"
        }
        
        var gaps = ""
        switch orders[0].stateAwning.noGaps {
        case false:
            gaps = "Да"
        default:
            gaps = "Нет"
        }
        
        var patches = ""
        switch orders[0].stateAwning.noPatches {
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
        switch orders[0].volume.unit{
            case 4:
            unit = " см"
            
        default:
            unit = " м"
        }
        
        var wmu = ""
        switch orders[0].weightMeasurementUnit {
        case 1:
            wmu = " кг"
        default:
            wmu = " т"
        }
        
        widthT = "Ширина:  \(String(orders[0].volume.width))\(unit)"
        lengthT = "Длина: \(String(orders[0].volume.length))\(unit)"
        heightT = "Высота: \(String(orders[0].volume.height))\(unit)"
        weightT = "Вес: \(String(orders[0].weight))\(wmu)"
        usernameT = "Владелец: \(orders[0].user.username)"
        emailT = "e-mail: \(orders[0].user.email)"
        addressT = "Адрес: \(orders[0].locationCargo.address)"
        
    }
    @IBAction func backButton(_ sender: Any) {
        UserDefaults.standard.set(nil, forKey: "id")
    }
        
}
