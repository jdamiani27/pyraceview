class CarStats(object):
    CAR_STATUS_RUNNING = 0
    CAR_STATUS_OUT_OF_RACE_ACCIDENT = 1
    CAR_STATUS_OUT_OF_RACE_ENGINE = 2
    CAR_STATUS_IN_GARAGE = 3
    CAR_STATUS_PRERACE = 4
    CAR_STATUS_WAITING = 5
    CAR_STATUS_WARMUP_LAP = 6
    CAR_STATUS_UNKNOWN = 7
    CAR_STATUS_ONDECK = 8
    CAR_STATUS_FINISHED = 9
    CAR_STATUS_DID_NOT_START = 10
    CAR_STATUS_LOST_GPS = 65280

    # public var rank:int
    # public var startPosition:int
    # public const tol:TimeOffLeader = new TimeOffLeader()
    # public var lastLapTimeOffLeader:Number
    # public var lastLapTime:Number
    # public var lastLapSpeed:Number
    # public var fastestLapTime:Number
    # public var fastestLapSpeed:Number
    # public var lapsLed:int
    # public var lapsInTopTen:int
    # public var topSpeed:Number
    # public var avgSpeed:Number
    # public var avgLapTime:Number
    # public var pointGain:int
    # public var points:int
    # public var lapNumber:int
    # public var status:int
    # private var _tolData:Object
    #
    # public const lastLapSectionAvgSpeeds:Vector.<Number> = new Vector.<Number>()
    #
    # public function CarStats()
    # {
    #     this._tolData = new Object()
    #     super()
    # }
    #
    # public function get tolData() : Object
    # {
    #     this._tolData.islaps = this.tol.isLaps
    #     this._tolData.value = this.tol.value
    #     this._tolData.lapsOffLeader = this.tol.lapsOffLeader
    #     return this._tolData
    # }
    #
    # public function reset() : void
    # {
    #     this.lastLapSectionAvgSpeeds.length = 0
    # }
