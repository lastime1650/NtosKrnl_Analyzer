# sub_00B34E9C

- RVA: `0x00B34E9C`–`0x00B365E0` (길이 `5,956` bytes)
- VA: `0x0000000140B34E9C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A8940`
- 디코드: `1,428`개 명령, `5,956/5,956` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **75**; 고유 호출 대상: **8**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **36**

### Outgoing calls
- `0x00B34EDC` → [PnpGetObjectProperty](../8E/PnpGetObjectProperty_function_008E2180.md) (function, `0x008E2180`)
- `0x00B34EFE` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00B34F18` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00B34F49` → [CmRemovePanelDevice](../82/CmRemovePanelDevice_function_0082F32C.md) (function, `0x0082F32C`)
- `0x00B34F96` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00B34FF0` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00B3504C` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00B350A1` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00B350D7` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00B3510D` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00B35168` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00B351C4` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00B3521E` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00B35269` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00B352C2` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00B3537F` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00B353FE` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00B35477` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00B354F7` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00B35545` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00B3557B` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00B355B8` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00B355EE` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00B35624` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00B35684` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00B3569D` → [_CmGetDevicePanelGroup](../A0/_CmGetDevicePanelGroup_function_00A0B618.md) (function, `0x00A0B618`)
- `0x00B356E1` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00B35702` → [CmBuildDevicePanelId](../A0/CmBuildDevicePanelId_function_00A0B008.md) (function, `0x00A0B008`)
- `0x00B35725` → [CmCreateDevicePanel](../82/CmCreateDevicePanel_function_0082E0E0.md) (function, `0x0082E0E0`)
- `0x00B35782` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00B357D9` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00B35856` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00B358A0` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00B3590C` → [PnpGetObjectProperty](../8E/PnpGetObjectProperty_function_008E2180.md) (function, `0x008E2180`)
- `0x00B3592D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00B35944` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00B35A03` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00B35A79` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00B35AA2` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00B35AED` → [CmBuildDevicePanelId](../A0/CmBuildDevicePanelId_function_00A0B008.md) (function, `0x00A0B008`)
- `0x00B35B4B` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00B35BC1` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00B35C39` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00B35C92` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00B35D0F` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00B35D45` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00B35D7B` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00B35DCE` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00B35E27` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00B35E82` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00B35EFB` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00B35F64` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00B35FE1` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00B3608A` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00B36105` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00B3615B` → [PnpGetObjectProperty](../8E/PnpGetObjectProperty_function_008E2180.md) (function, `0x008E2180`)
- `0x00B361BD` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00B36233` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00B36269` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00B3629F` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00B362D5` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00B3630B` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00B36341` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00B36377` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00B363AD` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00B363E3` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00B36419` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00B3644F` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00B36485` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00B364BB` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00B364F1` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00B36529` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00B3655F` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00B36595` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00B365CB` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00B34EC8` → RVA `0x00021B48` (`.rdata`; read)
- `0x00B34F73` → RVA `0x00014E40` (`.rdata`; read)
- `0x00B34FD4` → RVA `0x00014E58` (`.rdata`; read)
- `0x00B35029` → RVA `0x00014E70` (`.rdata`; read)
- `0x00B35074` → RVA `0x000115A0` (`.rdata`; read)
- `0x00B350A8` → RVA `0x00014E10` (`.rdata`; read)
- `0x00B350DE` → RVA `0x00014E28` (`.rdata`; read)
- `0x00B3514C` → RVA `0x00014E88` (`.rdata`; read)
- `0x00B351A1` → RVA `0x00014EA0` (`.rdata`; read)
- `0x00B35202` → RVA `0x00014EB8` (`.rdata`; read)
- `0x00B3535F` → RVA `0x00021FD0` (`.rdata`; read)
- `0x00B353D8` → RVA `0x00021410` (`.rdata`; read)
- `0x00B35451` → RVA `0x00022400` (`.rdata`; read)
- `0x00B35668` → RVA `0x00021C80` (`.rdata`; read)
- `0x00B356BA` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x00B3575F` → RVA `0x000227A0` (`.rdata`; read)
- `0x00B357BD` → RVA `0x000221A8` (`.rdata`; read)
- `0x00B35836` → RVA `0x00021490` (`.rdata`; read)
- `0x00B359E7` → RVA `0x00022460` (`.rdata`; read)
- `0x00B35A5D` → RVA `0x00021E78` (`.rdata`; read)
- `0x00B35B26` → RVA `0x00021218` (`.rdata`; read)
- `0x00B35BA5` → RVA `0x000230C0` (`.rdata`; read)
- `0x00B35C19` → RVA `0x00021AF0` (`.rdata`; read)
- `0x00B35C6F` → RVA `0x00020CB8` (`.rdata`; read)
- `0x00B35CB1` → RVA `0x000223D8` (`.rdata`; read)
- `0x00B35DAB` → RVA `0x00022148` (`.rdata`; read)
- `0x00B35E0B` → RVA `0x00022B60` (`.rdata`; read)
- `0x00B35E5F` → RVA `0x00020CE8` (`.rdata`; read)
- `0x00B35EDB` → RVA `0x000215C8` (`.rdata`; read)
- `0x00B35F48` → RVA `0x00020F90` (`.rdata`; read)
- `0x00B35FBE` → RVA `0x00022558` (`.rdata`; read)
- `0x00B36068` → RVA `0x00022180` (`.rdata`; read)
- `0x00B360E3` → RVA `0x000223B0` (`.rdata`; read)
- `0x00B36147` → RVA `0x00022510` (`.rdata`; read)
- `0x00B36420` → RVA `0x00020C68` (`.rdata`; read)
- `0x00B36456` → RVA `0x000220E0` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **6**
  - `0x00B34EFE` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00B34F18` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00B356E1` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00B3592D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00B35944` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00B35AA2` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **52**
  - `0x00B34EE8` → [_CmUpdateDevicePanel + 0x963](../A0/_CmUpdateDevicePanel_function_00A0A16C.md) (`tail-transfer`)
  - `0x00B34F07` → [_CmUpdateDevicePanel + 0x3DB](../A0/_CmUpdateDevicePanel_function_00A0A16C.md) (`tail-transfer`)
  - `0x00B34F11` → [_CmUpdateDevicePanel + 0x496](../A0/_CmUpdateDevicePanel_function_00A0A16C.md) (`tail-transfer`)
  - `0x00B34F24` → [_CmUpdateDevicePanel + 0x116](../A0/_CmUpdateDevicePanel_function_00A0A16C.md) (`tail-transfer`)
  - `0x00B34F2E` → [_CmUpdateDevicePanel + 0x6BA](../A0/_CmUpdateDevicePanel_function_00A0A16C.md) (`tail-transfer`)
  - `0x00B34F3A` → [_CmUpdateDevicePanel + 0x6BA](../A0/_CmUpdateDevicePanel_function_00A0A16C.md) (`tail-transfer`)
  - `0x00B34F54` → [_CmUpdateDevicePanel + 0x6AD](../A0/_CmUpdateDevicePanel_function_00A0A16C.md) (`tail-transfer`)
  - `0x00B34F5E` → [_CmUpdateDevicePanel + 0x2CB](../A0/_CmUpdateDevicePanel_function_00A0A16C.md) (`tail-transfer`)
  - `0x00B34FA1` → [_CmUpdateDevicePanel + 0x496](../A0/_CmUpdateDevicePanel_function_00A0A16C.md) (`tail-transfer`)
  - `0x00B34FFB` → [_CmUpdateDevicePanel + 0x496](../A0/_CmUpdateDevicePanel_function_00A0A16C.md) (`tail-transfer`)
  - `0x00B35057` → [_CmUpdateDevicePanel + 0x496](../A0/_CmUpdateDevicePanel_function_00A0A16C.md) (`tail-transfer`)
  - `0x00B3505D` → [_CmUpdateDevicePanel + 0x883](../A0/_CmUpdateDevicePanel_function_00A0A16C.md) (`tail-transfer`)
  - `0x00B3506A` → [_CmUpdateDevicePanel + 0x1B4](../A0/_CmUpdateDevicePanel_function_00A0A16C.md) (`tail-transfer`)
  - `0x00B35114` → [_CmUpdateDevicePanel + 0x8B1](../A0/_CmUpdateDevicePanel_function_00A0A16C.md) (`tail-transfer`)
  - `0x00B35234` → [_CmUpdateDevicePanel + 0x55E](../A0/_CmUpdateDevicePanel_function_00A0A16C.md) (`tail-transfer`)
  - `0x00B352DB` → [_CmUpdateDevicePanel + 0x55E](../A0/_CmUpdateDevicePanel_function_00A0A16C.md) (`tail-transfer`)
  - `0x00B35303` → [_CmUpdateDevicePanel + 0x548](../A0/_CmUpdateDevicePanel_function_00A0A16C.md) (`tail-transfer`)
  - `0x00B3530B` → [_CmUpdateDevicePanel + 0x1DA](../A0/_CmUpdateDevicePanel_function_00A0A16C.md) (`tail-transfer`)
  - `0x00B3538B` → [_CmUpdateDevicePanel + 0x496](../A0/_CmUpdateDevicePanel_function_00A0A16C.md) (`tail-transfer`)
  - `0x00B3540A` → [_CmUpdateDevicePanel + 0x496](../A0/_CmUpdateDevicePanel_function_00A0A16C.md) (`tail-transfer`)
  - `0x00B35482` → [_CmUpdateDevicePanel + 0x496](../A0/_CmUpdateDevicePanel_function_00A0A16C.md) (`tail-transfer`)
  - `0x00B3548D` → [_CmUpdateDevicePanel + 0x40A](../A0/_CmUpdateDevicePanel_function_00A0A16C.md) (`tail-transfer`)
  - `0x00B35502` → [_CmUpdateDevicePanel + 0x496](../A0/_CmUpdateDevicePanel_function_00A0A16C.md) (`tail-transfer`)
  - `0x00B35510` → [_CmUpdateDevicePanel + 0x40A](../A0/_CmUpdateDevicePanel_function_00A0A16C.md) (`tail-transfer`)
  - `0x00B35582` → [_CmUpdateDevicePanel + 0x40A](../A0/_CmUpdateDevicePanel_function_00A0A16C.md) (`tail-transfer`)
  - `0x00B3562B` → [_CmUpdateDevicePanel + 0x1E3](../A0/_CmUpdateDevicePanel_function_00A0A16C.md) (`tail-transfer`)
  - `0x00B35633` → [_CmUpdateDevicePanel + 0x210](../A0/_CmUpdateDevicePanel_function_00A0A16C.md) (`tail-transfer`)
  - `0x00B3568F` → [_CmUpdateDevicePanel + 0x496](../A0/_CmUpdateDevicePanel_function_00A0A16C.md) (`tail-transfer`)
  - `0x00B35695` → [_CmUpdateDevicePanel + 0xB6E](../A0/_CmUpdateDevicePanel_function_00A0A16C.md) (`tail-transfer`)
  - `0x00B356EC` → [_CmUpdateDevicePanel + 0xBC1](../A0/_CmUpdateDevicePanel_function_00A0A16C.md) (`tail-transfer`)
  - `0x00B3570B` → [_CmUpdateDevicePanel + 0x2C2](../A0/_CmUpdateDevicePanel_function_00A0A16C.md) (`tail-transfer`)
  - `0x00B35734` → [_CmUpdateDevicePanel + 0x2C2](../A0/_CmUpdateDevicePanel_function_00A0A16C.md) (`tail-transfer`)
  - `0x00B3578D` → [_CmUpdateDevicePanel + 0x2C2](../A0/_CmUpdateDevicePanel_function_00A0A16C.md) (`tail-transfer`)
  - `0x00B357E2` → [_CmUpdateDevicePanel + 0x2C2](../A0/_CmUpdateDevicePanel_function_00A0A16C.md) (`tail-transfer`)
  - `0x00B3585F` → [_CmUpdateDevicePanel + 0x2C2](../A0/_CmUpdateDevicePanel_function_00A0A16C.md) (`tail-transfer`)
  - `0x00B35921` → [_CmUpdateDevicePanel + 0xBB7](../A0/_CmUpdateDevicePanel_function_00A0A16C.md) (`tail-transfer`)
  - `0x00B35950` → [_CmUpdateDevicePanel + 0xBC1](../A0/_CmUpdateDevicePanel_function_00A0A16C.md) (`tail-transfer`)
  - `0x00B35971` → [_CmUpdateDevicePanel + 0x2C2](../A0/_CmUpdateDevicePanel_function_00A0A16C.md) (`tail-transfer`)
  - `0x00B35A0E` → [_CmUpdateDevicePanel + 0x2C2](../A0/_CmUpdateDevicePanel_function_00A0A16C.md) (`tail-transfer`)
  - `0x00B35A84` → [_CmUpdateDevicePanel + 0x2C2](../A0/_CmUpdateDevicePanel_function_00A0A16C.md) (`tail-transfer`)
  - `0x00B35AB3` → [_CmUpdateDevicePanel + 0xBC1](../A0/_CmUpdateDevicePanel_function_00A0A16C.md) (`tail-transfer`)
  - `0x00B35AF8` → [_CmUpdateDevicePanel + 0x2C2](../A0/_CmUpdateDevicePanel_function_00A0A16C.md) (`tail-transfer`)
  - `0x00B35B56` → [_CmUpdateDevicePanel + 0x2C2](../A0/_CmUpdateDevicePanel_function_00A0A16C.md) (`tail-transfer`)
  - `0x00B35BCA` → [_CmUpdateDevicePanel + 0x2C2](../A0/_CmUpdateDevicePanel_function_00A0A16C.md) (`tail-transfer`)
  - `0x00B35C44` → [_CmUpdateDevicePanel + 0x2C2](../A0/_CmUpdateDevicePanel_function_00A0A16C.md) (`tail-transfer`)
  - `0x00B35C9D` → [_CmUpdateDevicePanel + 0x2C2](../A0/_CmUpdateDevicePanel_function_00A0A16C.md) (`tail-transfer`)
  - `0x00B35DD9` → [_CmUpdateDevicePanel + 0x2C2](../A0/_CmUpdateDevicePanel_function_00A0A16C.md) (`tail-transfer`)
  - `0x00B35E32` → [_CmUpdateDevicePanel + 0x2C2](../A0/_CmUpdateDevicePanel_function_00A0A16C.md) (`tail-transfer`)
  - `0x00B35E8B` → [_CmUpdateDevicePanel + 0x2C2](../A0/_CmUpdateDevicePanel_function_00A0A16C.md) (`tail-transfer`)
  - `0x00B35F06` → [_CmUpdateDevicePanel + 0x2C2](../A0/_CmUpdateDevicePanel_function_00A0A16C.md) (`tail-transfer`)
  - `0x00B35F6F` → [_CmUpdateDevicePanel + 0x2C2](../A0/_CmUpdateDevicePanel_function_00A0A16C.md) (`tail-transfer`)
  - `0x00B365DB` → [_CmUpdateDevicePanel + 0x257](../A0/_CmUpdateDevicePanel_function_00A0A16C.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B34E9C  89 54 24 50                     mov dword ptr [rsp + 0x50], edx
00B34EA0  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
00B34EA5  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
00B34EAA  4D 8B CF                        mov r9, r15
00B34EAD  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
00B34EB1  41 B8 01 00 00 00               mov r8d, 1
00B34EB7  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00B34EBC  48 8B CF                        mov rcx, rdi
00B34EBF  48 8D 45 88                     lea rax, [rbp - 0x78]
00B34EC3  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00B34EC8  48 8D 05 79 CC 4E FF            lea rax, [rip - 0xb13387]
00B34ECF  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B34ED4  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00B34ED9  48 8B D6                        mov rdx, rsi
00B34EDC  E8 9F D2 DA FF                  call 0x1408e2180
00B34EE1  8B D8                           mov ebx, eax
00B34EE3  3D 23 00 00 C0                  cmp eax, 0xc0000023
00B34EE8  0F 85 E1 5B ED FF               jne 0x140a0aacf
00B34EEE  8B 45 90                        mov eax, dword ptr [rbp - 0x70]
00B34EF1  39 44 24 68                     cmp dword ptr [rsp + 0x68], eax
00B34EF5  76 15                           jbe 0x140b34f0c
00B34EF7  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
00B34EFC  33 D2                           xor edx, edx
00B34EFE  E8 6D D9 04 00                  call 0x140b82870
00B34F03  8B 5C 24 68                     mov ebx, dword ptr [rsp + 0x68]
00B34F07  E9 3B 56 ED FF                  jmp 0x140a0a547
00B34F0C  BB 01 00 00 C0                  mov ebx, 0xc0000001
00B34F11  E9 EC 56 ED FF                  jmp 0x140a0a602
00B34F16  33 D2                           xor edx, edx
00B34F18  E8 53 D9 04 00                  call 0x140b82870
00B34F1D  33 C0                           xor eax, eax
00B34F1F  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00B34F24  E9 59 53 ED FF                  jmp 0x140a0a282
00B34F29  B0 01                           mov al, 1
00B34F2B  48 85 DB                        test rbx, rbx
00B34F2E  0F 84 F2 58 ED FF               je 0x140a0a826
00B34F34  88 44 24 64                     mov byte ptr [rsp + 0x64], al
00B34F38  84 C0                           test al, al
00B34F3A  0F 84 E6 58 ED FF               je 0x140a0a826
00B34F40  4C 8B C6                        mov r8, rsi
00B34F43  48 8B D3                        mov rdx, rbx
00B34F46  48 8B CF                        mov rcx, rdi
00B34F49  E8 DE A3 CF FF                  call 0x14082f32c
00B34F4E  33 D2                           xor edx, edx
00B34F50  8B D8                           mov ebx, eax
00B34F52  85 C0                           test eax, eax
00B34F54  0F 89 BF 58 ED FF               jns 0x140a0a819
00B34F5A  4C 8B 65 A8                     mov r12, qword ptr [rbp - 0x58]
00B34F5E  E9 D4 54 ED FF                  jmp 0x140a0a437
00B34F63  8B 40 04                        mov eax, dword ptr [rax + 4]
00B34F66  0F B7 C8                        movzx ecx, ax
00B34F69  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00B34F6E  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00B34F73  48 8D 05 C6 FE 4D FF            lea rax, [rip - 0xb2013a]
00B34F7A  C7 44 24 30 07 00 00 00         mov dword ptr [rsp + 0x30], 7
00B34F82  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B34F87  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00B34F8C  48 8B D6                        mov rdx, rsi
00B34F8F  89 4C 24 60                     mov dword ptr [rsp + 0x60], ecx
00B34F93  48 8B CF                        mov rcx, rdi
00B34F96  E8 4D 17 DC FF                  call 0x1408f66e8
00B34F9B  33 D2                           xor edx, edx
00B34F9D  8B D8                           mov ebx, eax
00B34F9F  85 C0                           test eax, eax
00B34FA1  0F 88 5B 56 ED FF               js 0x140a0a602
00B34FA7  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
00B34FAC  44 8D 42 01                     lea r8d, [rdx + 1]
00B34FB0  89 54 24 48                     mov dword ptr [rsp + 0x48], edx
00B34FB4  4D 8B CF                        mov r9, r15
00B34FB7  C7 44 24 40 04 00 00 00         mov dword ptr [rsp + 0x40], 4
00B34FBF  0F B7 41 06                     movzx eax, word ptr [rcx + 6]
00B34FC3  48 8B CF                        mov rcx, rdi
00B34FC6  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
00B34FCA  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00B34FCF  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00B34FD4  48 8D 05 7D FE 4D FF            lea rax, [rip - 0xb20183]
00B34FDB  C7 44 24 30 07 00 00 00         mov dword ptr [rsp + 0x30], 7
00B34FE3  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B34FE8  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00B34FED  48 8B D6                        mov rdx, rsi
00B34FF0  E8 F3 16 DC FF                  call 0x1408f66e8
00B34FF5  33 D2                           xor edx, edx
00B34FF7  8B D8                           mov ebx, eax
00B34FF9  85 C0                           test eax, eax
00B34FFB  0F 88 01 56 ED FF               js 0x140a0a602
00B35001  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
00B35006  44 8D 42 01                     lea r8d, [rdx + 1]
00B3500A  89 54 24 48                     mov dword ptr [rsp + 0x48], edx
00B3500E  4D 8B CF                        mov r9, r15
00B35011  C7 44 24 40 04 00 00 00         mov dword ptr [rsp + 0x40], 4
00B35019  8B 40 08                        mov eax, dword ptr [rax + 8]
00B3501C  0F B7 C8                        movzx ecx, ax
00B3501F  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00B35024  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00B35029  48 8D 05 40 FE 4D FF            lea rax, [rip - 0xb201c0]
00B35030  C7 44 24 30 07 00 00 00         mov dword ptr [rsp + 0x30], 7
00B35038  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B3503D  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00B35042  48 8B D6                        mov rdx, rsi
00B35045  89 4C 24 60                     mov dword ptr [rsp + 0x60], ecx
00B35049  48 8B CF                        mov rcx, rdi
00B3504C  E8 97 16 DC FF                  call 0x1408f66e8
00B35051  33 D2                           xor edx, edx
00B35053  8B D8                           mov ebx, eax
00B35055  85 C0                           test eax, eax
00B35057  0F 88 A5 55 ED FF               js 0x140a0a602
00B3505D  E9 8D 59 ED FF                  jmp 0x140a0a9ef
00B35062  48 8B 5C 24 78                  mov rbx, qword ptr [rsp + 0x78]
00B35067  48 85 DB                        test rbx, rbx
00B3506A  0F 84 B0 52 ED FF               je 0x140a0a320
00B35070  89 54 24 48                     mov dword ptr [rsp + 0x48], edx
00B35074  48 8D 05 25 C5 4D FF            lea rax, [rip - 0xb23adb]
00B3507B  89 54 24 40                     mov dword ptr [rsp + 0x40], edx
00B3507F  4D 8B CF                        mov r9, r15
00B35082  48 89 54 24 38                  mov qword ptr [rsp + 0x38], rdx
00B35087  41 B8 01 00 00 00               mov r8d, 1
00B3508D  89 54 24 30                     mov dword ptr [rsp + 0x30], edx
00B35091  48 8B CF                        mov rcx, rdi
00B35094  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B35099  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00B3509E  48 8B D6                        mov rdx, rsi
00B350A1  E8 42 16 DC FF                  call 0x1408f66e8
00B350A6  33 C9                           xor ecx, ecx
00B350A8  48 8D 05 61 FD 4D FF            lea rax, [rip - 0xb2029f]
00B350AF  89 4C 24 48                     mov dword ptr [rsp + 0x48], ecx
00B350B3  4D 8B CF                        mov r9, r15
00B350B6  89 4C 24 40                     mov dword ptr [rsp + 0x40], ecx
00B350BA  48 8B D6                        mov rdx, rsi
00B350BD  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
00B350C2  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
00B350C6  44 8D 41 01                     lea r8d, [rcx + 1]
00B350CA  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B350CF  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00B350D4  48 8B CF                        mov rcx, rdi
00B350D7  E8 0C 16 DC FF                  call 0x1408f66e8
00B350DC  33 C9                           xor ecx, ecx
00B350DE  48 8D 05 43 FD 4D FF            lea rax, [rip - 0xb202bd]
00B350E5  89 4C 24 48                     mov dword ptr [rsp + 0x48], ecx
00B350E9  4D 8B CF                        mov r9, r15
00B350EC  89 4C 24 40                     mov dword ptr [rsp + 0x40], ecx
00B350F0  48 8B D6                        mov rdx, rsi
00B350F3  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
00B350F8  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
00B350FC  44 8D 41 01                     lea r8d, [rcx + 1]
00B35100  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B35105  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00B3510A  48 8B CF                        mov rcx, rdi
00B3510D  E8 D6 15 DC FF                  call 0x1408f66e8
00B35112  33 D2                           xor edx, edx
00B35114  E9 04 59 ED FF                  jmp 0x140a0aa1d
00B35119  89 54 24 48                     mov dword ptr [rsp + 0x48], edx
00B3511D  4D 8B CF                        mov r9, r15
00B35120  C7 44 24 40 04 00 00 00         mov dword ptr [rsp + 0x40], 4
00B35128  41 B8 01 00 00 00               mov r8d, 1
00B3512E  48 8B CF                        mov rcx, rdi
00B35131  48 85 C0                        test rax, rax
00B35134  0F 84 FF 00 00 00               je 0x140b35239
00B3513A  0F B7 40 0A                     movzx eax, word ptr [rax + 0xa]
00B3513E  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
00B35142  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00B35147  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00B3514C  48 8D 05 35 FD 4D FF            lea rax, [rip - 0xb202cb]
00B35153  C7 44 24 30 07 00 00 00         mov dword ptr [rsp + 0x30], 7
00B3515B  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B35160  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00B35165  48 8B D6                        mov rdx, rsi
00B35168  E8 7B 15 DC FF                  call 0x1408f66e8
00B3516D  33 D2                           xor edx, edx
00B3516F  8B D8                           mov ebx, eax
00B35171  85 C0                           test eax, eax
00B35173  0F 88 E1 FD FF FF               js 0x140b34f5a
00B35179  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
00B3517E  44 8D 42 01                     lea r8d, [rdx + 1]
00B35182  89 54 24 48                     mov dword ptr [rsp + 0x48], edx
00B35186  4D 8B CF                        mov r9, r15
00B35189  C7 44 24 40 04 00 00 00         mov dword ptr [rsp + 0x40], 4
00B35191  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00B35194  0F B7 C8                        movzx ecx, ax
00B35197  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00B3519C  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00B351A1  48 8D 05 F8 FC 4D FF            lea rax, [rip - 0xb20308]
00B351A8  C7 44 24 30 07 00 00 00         mov dword ptr [rsp + 0x30], 7
00B351B0  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B351B5  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00B351BA  48 8B D6                        mov rdx, rsi
00B351BD  89 4C 24 60                     mov dword ptr [rsp + 0x60], ecx
00B351C1  48 8B CF                        mov rcx, rdi
00B351C4  E8 1F 15 DC FF                  call 0x1408f66e8
00B351C9  33 D2                           xor edx, edx
00B351CB  8B D8                           mov ebx, eax
00B351CD  85 C0                           test eax, eax
00B351CF  0F 88 85 FD FF FF               js 0x140b34f5a
00B351D5  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
00B351DA  44 8D 42 01                     lea r8d, [rdx + 1]
00B351DE  89 54 24 48                     mov dword ptr [rsp + 0x48], edx
00B351E2  4D 8B CF                        mov r9, r15
00B351E5  C7 44 24 40 04 00 00 00         mov dword ptr [rsp + 0x40], 4
00B351ED  48 8B CF                        mov rcx, rdi
00B351F0  0F B7 40 0E                     movzx eax, word ptr [rax + 0xe]
00B351F4  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
00B351F8  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00B351FD  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00B35202  48 8D 05 AF FC 4D FF            lea rax, [rip - 0xb20351]
00B35209  C7 44 24 30 07 00 00 00         mov dword ptr [rsp + 0x30], 7
00B35211  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B35216  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00B3521B  48 8B D6                        mov rdx, rsi
00B3521E  E8 C5 14 DC FF                  call 0x1408f66e8
00B35223  33 D2                           xor edx, edx
00B35225  8B D8                           mov ebx, eax
00B35227  85 C0                           test eax, eax
00B35229  0F 88 2B FD FF FF               js 0x140b34f5a
00B3522F  48 8B 5C 24 78                  mov rbx, qword ptr [rsp + 0x78]
00B35234  E9 91 54 ED FF                  jmp 0x140a0a6ca
00B35239  41 0F B7 44 24 12               movzx eax, word ptr [r12 + 0x12]
00B3523F  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
00B35243  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00B35248  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00B3524D  48 8D 05 34 FC 4D FF            lea rax, [rip - 0xb203cc]
00B35254  C7 44 24 30 07 00 00 00         mov dword ptr [rsp + 0x30], 7
00B3525C  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B35261  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00B35266  48 8B D6                        mov rdx, rsi
00B35269  E8 7A 14 DC FF                  call 0x1408f66e8
00B3526E  33 D2                           xor edx, edx
00B35270  8B D8                           mov ebx, eax
00B35272  85 C0                           test eax, eax
00B35274  0F 88 E0 FC FF FF               js 0x140b34f5a
00B3527A  41 8B 44 24 10                  mov eax, dword ptr [r12 + 0x10]
00B3527F  44 8D 42 01                     lea r8d, [rdx + 1]
00B35283  89 54 24 48                     mov dword ptr [rsp + 0x48], edx
00B35287  4D 8B CF                        mov r9, r15
00B3528A  0F B7 C8                        movzx ecx, ax
00B3528D  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00B35292  C7 44 24 40 04 00 00 00         mov dword ptr [rsp + 0x40], 4
00B3529A  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00B3529F  48 8D 05 FA FB 4D FF            lea rax, [rip - 0xb20406]
00B352A6  C7 44 24 30 07 00 00 00         mov dword ptr [rsp + 0x30], 7
00B352AE  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B352B3  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00B352B8  48 8B D6                        mov rdx, rsi
00B352BB  89 4C 24 60                     mov dword ptr [rsp + 0x60], ecx
00B352BF  48 8B CF                        mov rcx, rdi
00B352C2  E8 21 14 DC FF                  call 0x1408f66e8
00B352C7  33 D2                           xor edx, edx
00B352C9  8B D8                           mov ebx, eax
00B352CB  85 C0                           test eax, eax
00B352CD  0F 88 87 FC FF FF               js 0x140b34f5a
00B352D3  48 8B 5C 24 78                  mov rbx, qword ptr [rsp + 0x78]
00B352D8  48 85 DB                        test rbx, rbx
00B352DB  0F 84 E9 53 ED FF               je 0x140a0a6ca
00B352E1  89 54 24 48                     mov dword ptr [rsp + 0x48], edx
00B352E5  48 8D 05 CC FB 4D FF            lea rax, [rip - 0xb20434]
00B352EC  89 54 24 40                     mov dword ptr [rsp + 0x40], edx
00B352F0  48 89 54 24 38                  mov qword ptr [rsp + 0x38], rdx
00B352F5  89 54 24 30                     mov dword ptr [rsp + 0x30], edx
00B352F9  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B352FE  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00B35303  E9 AC 53 ED FF                  jmp 0x140a0a6b4
00B35308  4D 85 E4                        test r12, r12
00B3530B  0F 84 35 50 ED FF               je 0x140a0a346
00B35311  4D 8B CF                        mov r9, r15
00B35314  48 85 C0                        test rax, rax
00B35317  0F 84 75 01 00 00               je 0x140b35492
00B3531D  8B 08                           mov ecx, dword ptr [rax]
00B3531F  41 8B C0                        mov eax, r8d
00B35322  C1 E9 05                        shr ecx, 5
00B35325  81 E1 FF 01 00 00               and ecx, 0x1ff
00B3532B  F7 E1                           mul ecx
00B3532D  8B C1                           mov eax, ecx
00B3532F  2B C2                           sub eax, edx
00B35331  D1 E8                           shr eax, 1
00B35333  03 C2                           add eax, edx
00B35335  48 8B D6                        mov rdx, rsi
00B35338  C1 E8 08                        shr eax, 8
00B3533B  69 C0 68 01 00 00               imul eax, eax, 0x168
00B35341  2B C8                           sub ecx, eax
00B35343  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00B35348  89 4C 24 60                     mov dword ptr [rsp + 0x60], ecx
00B3534C  33 C9                           xor ecx, ecx
00B3534E  89 4C 24 48                     mov dword ptr [rsp + 0x48], ecx
00B35352  C7 44 24 40 04 00 00 00         mov dword ptr [rsp + 0x40], 4
00B3535A  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00B3535F  48 8D 05 6A CC 4E FF            lea rax, [rip - 0xb13396]
00B35366  C7 44 24 30 07 00 00 00         mov dword ptr [rsp + 0x30], 7
00B3536E  44 8D 41 01                     lea r8d, [rcx + 1]
00B35372  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B35377  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00B3537C  48 8B CF                        mov rcx, rdi
00B3537F  E8 64 13 DC FF                  call 0x1408f66e8
00B35384  45 33 C0                        xor r8d, r8d
00B35387  8B D8                           mov ebx, eax
00B35389  85 C0                           test eax, eax
00B3538B  0F 88 71 52 ED FF               js 0x140a0a602
00B35391  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
00B35396  4D 8B CF                        mov r9, r15
00B35399  44 89 44 24 48                  mov dword ptr [rsp + 0x48], r8d
00B3539E  C7 44 24 40 04 00 00 00         mov dword ptr [rsp + 0x40], 4
00B353A6  8B 08                           mov ecx, dword ptr [rax]
00B353A8  B8 6D C1 16 6C                  mov eax, 0x6c16c16d
00B353AD  C1 E9 0E                        shr ecx, 0xe
00B353B0  81 E1 FF 01 00 00               and ecx, 0x1ff
00B353B6  F7 E1                           mul ecx
00B353B8  8B C1                           mov eax, ecx
00B353BA  2B C2                           sub eax, edx
00B353BC  D1 E8                           shr eax, 1
00B353BE  03 C2                           add eax, edx
00B353C0  48 8B D6                        mov rdx, rsi
00B353C3  C1 E8 08                        shr eax, 8
00B353C6  69 C0 68 01 00 00               imul eax, eax, 0x168
00B353CC  2B C8                           sub ecx, eax
00B353CE  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00B353D3  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00B353D8  48 8D 05 31 C0 4E FF            lea rax, [rip - 0xb13fcf]
00B353DF  C7 44 24 30 07 00 00 00         mov dword ptr [rsp + 0x30], 7
00B353E7  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B353EC  4C 89 44 24 20                  mov qword ptr [rsp + 0x20], r8
00B353F1  41 B8 01 00 00 00               mov r8d, 1
00B353F7  89 4C 24 60                     mov dword ptr [rsp + 0x60], ecx
00B353FB  48 8B CF                        mov rcx, rdi
00B353FE  E8 E5 12 DC FF                  call 0x1408f66e8
00B35403  45 33 C0                        xor r8d, r8d
00B35406  8B D8                           mov ebx, eax
00B35408  85 C0                           test eax, eax
00B3540A  0F 88 F2 51 ED FF               js 0x140a0a602
00B35410  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
00B35415  4D 8B CF                        mov r9, r15
00B35418  44 89 44 24 48                  mov dword ptr [rsp + 0x48], r8d
00B3541D  C7 44 24 40 04 00 00 00         mov dword ptr [rsp + 0x40], 4
00B35425  8B 08                           mov ecx, dword ptr [rax]
00B35427  B8 6D C1 16 6C                  mov eax, 0x6c16c16d
00B3542C  C1 E9 17                        shr ecx, 0x17
00B3542F  F7 E1                           mul ecx
00B35431  8B C1                           mov eax, ecx
00B35433  2B C2                           sub eax, edx
00B35435  D1 E8                           shr eax, 1
00B35437  03 C2                           add eax, edx
00B35439  48 8B D6                        mov rdx, rsi
00B3543C  C1 E8 08                        shr eax, 8
00B3543F  69 C0 68 01 00 00               imul eax, eax, 0x168
00B35445  2B C8                           sub ecx, eax
00B35447  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00B3544C  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00B35451  48 8D 05 A8 CF 4E FF            lea rax, [rip - 0xb13058]
00B35458  C7 44 24 30 07 00 00 00         mov dword ptr [rsp + 0x30], 7
00B35460  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B35465  4C 89 44 24 20                  mov qword ptr [rsp + 0x20], r8
00B3546A  41 B8 01 00 00 00               mov r8d, 1
00B35470  89 4C 24 60                     mov dword ptr [rsp + 0x60], ecx
00B35474  48 8B CF                        mov rcx, rdi
00B35477  E8 6C 12 DC FF                  call 0x1408f66e8
00B3547C  33 D2                           xor edx, edx
00B3547E  8B D8                           mov ebx, eax
00B35480  85 C0                           test eax, eax
00B35482  0F 88 7A 51 ED FF               js 0x140a0a602
00B35488  48 8B 5C 24 78                  mov rbx, qword ptr [rsp + 0x78]
00B3548D  E9 E4 50 ED FF                  jmp 0x140a0a576
00B35492  41 8B 44 24 0C                  mov eax, dword ptr [r12 + 0xc]
00B35497  C1 E8 13                        shr eax, 0x13
00B3549A  83 E0 0F                        and eax, 0xf
00B3549D  6B C8 2D                        imul ecx, eax, 0x2d
00B354A0  41 8B C0                        mov eax, r8d
00B354A3  F7 E1                           mul ecx
00B354A5  8B C1                           mov eax, ecx
00B354A7  2B C2                           sub eax, edx
00B354A9  D1 E8                           shr eax, 1
00B354AB  03 C2                           add eax, edx
00B354AD  48 8B D6                        mov rdx, rsi
00B354B0  C1 E8 08                        shr eax, 8
00B354B3  69 C0 68 01 00 00               imul eax, eax, 0x168
00B354B9  2B C8                           sub ecx, eax
00B354BB  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00B354C0  89 4C 24 60                     mov dword ptr [rsp + 0x60], ecx
00B354C4  33 C9                           xor ecx, ecx
00B354C6  89 4C 24 48                     mov dword ptr [rsp + 0x48], ecx
00B354CA  C7 44 24 40 04 00 00 00         mov dword ptr [rsp + 0x40], 4
00B354D2  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00B354D7  48 8D 05 22 CF 4E FF            lea rax, [rip - 0xb130de]
00B354DE  C7 44 24 30 07 00 00 00         mov dword ptr [rsp + 0x30], 7
00B354E6  44 8D 41 01                     lea r8d, [rcx + 1]
00B354EA  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B354EF  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00B354F4  48 8B CF                        mov rcx, rdi
00B354F7  E8 EC 11 DC FF                  call 0x1408f66e8
00B354FC  33 D2                           xor edx, edx
00B354FE  8B D8                           mov ebx, eax
00B35500  85 C0                           test eax, eax
00B35502  0F 88 FA 50 ED FF               js 0x140a0a602
00B35508  48 8B 5C 24 78                  mov rbx, qword ptr [rsp + 0x78]
00B3550D  48 85 DB                        test rbx, rbx
00B35510  0F 84 60 50 ED FF               je 0x140a0a576
00B35516  89 54 24 48                     mov dword ptr [rsp + 0x48], edx
00B3551A  48 8D 05 AF CA 4E FF            lea rax, [rip - 0xb13551]
00B35521  89 54 24 40                     mov dword ptr [rsp + 0x40], edx
00B35525  44 8D 42 01                     lea r8d, [rdx + 1]
00B35529  48 89 54 24 38                  mov qword ptr [rsp + 0x38], rdx
00B3552E  4D 8B CF                        mov r9, r15
00B35531  89 54 24 30                     mov dword ptr [rsp + 0x30], edx
00B35535  48 8B CF                        mov rcx, rdi
00B35538  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B3553D  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00B35542  48 8B D6                        mov rdx, rsi
00B35545  E8 9E 11 DC FF                  call 0x1408f66e8
00B3554A  33 C9                           xor ecx, ecx
00B3554C  48 8D 05 BD BE 4E FF            lea rax, [rip - 0xb14143]
00B35553  89 4C 24 48                     mov dword ptr [rsp + 0x48], ecx
00B35557  4D 8B CF                        mov r9, r15
00B3555A  89 4C 24 40                     mov dword ptr [rsp + 0x40], ecx
00B3555E  48 8B D6                        mov rdx, rsi
00B35561  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
00B35566  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
00B3556A  44 8D 41 01                     lea r8d, [rcx + 1]
00B3556E  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B35573  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00B35578  48 8B CF                        mov rcx, rdi
00B3557B  E8 68 11 DC FF                  call 0x1408f66e8
00B35580  33 D2                           xor edx, edx
00B35582  E9 EF 4F ED FF                  jmp 0x140a0a576
00B35587  89 54 24 48                     mov dword ptr [rsp + 0x48], edx
00B3558B  48 8D 05 3E CA 4E FF            lea rax, [rip - 0xb135c2]
00B35592  89 54 24 40                     mov dword ptr [rsp + 0x40], edx
00B35596  4D 8B CF                        mov r9, r15
00B35599  48 89 54 24 38                  mov qword ptr [rsp + 0x38], rdx
00B3559E  41 B8 01 00 00 00               mov r8d, 1
00B355A4  89 54 24 30                     mov dword ptr [rsp + 0x30], edx
00B355A8  48 8B CF                        mov rcx, rdi
00B355AB  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B355B0  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00B355B5  48 8B D6                        mov rdx, rsi
00B355B8  E8 2B 11 DC FF                  call 0x1408f66e8
00B355BD  33 C9                           xor ecx, ecx
00B355BF  48 8D 05 4A BE 4E FF            lea rax, [rip - 0xb141b6]
00B355C6  89 4C 24 48                     mov dword ptr [rsp + 0x48], ecx
00B355CA  4D 8B CF                        mov r9, r15
00B355CD  89 4C 24 40                     mov dword ptr [rsp + 0x40], ecx
00B355D1  48 8B D6                        mov rdx, rsi
00B355D4  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
00B355D9  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
00B355DD  44 8D 41 01                     lea r8d, [rcx + 1]
00B355E1  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B355E6  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00B355EB  48 8B CF                        mov rcx, rdi
00B355EE  E8 F5 10 DC FF                  call 0x1408f66e8
00B355F3  33 C9                           xor ecx, ecx
00B355F5  48 8D 05 04 CE 4E FF            lea rax, [rip - 0xb131fc]
00B355FC  89 4C 24 48                     mov dword ptr [rsp + 0x48], ecx
00B35600  4D 8B CF                        mov r9, r15
00B35603  89 4C 24 40                     mov dword ptr [rsp + 0x40], ecx
00B35607  48 8B D6                        mov rdx, rsi
00B3560A  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
00B3560F  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
00B35613  44 8D 41 01                     lea r8d, [rcx + 1]
00B35617  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B3561C  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00B35621  48 8B CF                        mov rcx, rdi
00B35624  E8 BF 10 DC FF                  call 0x1408f66e8
00B35629  33 D2                           xor edx, edx
00B3562B  E9 1F 4D ED FF                  jmp 0x140a0a34f
00B35630  4D 85 E4                        test r12, r12
00B35633  0F 84 43 4D ED FF               je 0x140a0a37c
00B35639  41 8A 44 24 08                  mov al, byte ptr [r12 + 8]
00B3563E  B9 01 00 00 00                  mov ecx, 1
00B35643  89 54 24 48                     mov dword ptr [rsp + 0x48], edx
00B35647  22 C1                           and al, cl
00B35649  89 4C 24 40                     mov dword ptr [rsp + 0x40], ecx
00B3564D  F6 D8                           neg al
00B3564F  44 8B C1                        mov r8d, ecx
00B35652  4D 8B CF                        mov r9, r15
00B35655  1A C0                           sbb al, al
00B35657  48 8B CF                        mov rcx, rdi
00B3565A  88 44 24 6C                     mov byte ptr [rsp + 0x6c], al
00B3565E  48 8D 44 24 6C                  lea rax, [rsp + 0x6c]
00B35663  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00B35668  48 8D 05 11 C6 4E FF            lea rax, [rip - 0xb139ef]
00B3566F  C7 44 24 30 11 00 00 00         mov dword ptr [rsp + 0x30], 0x11
00B35677  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B3567C  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00B35681  48 8B D6                        mov rdx, rsi
00B35684  E8 5F 10 DC FF                  call 0x1408f66e8
00B35689  33 D2                           xor edx, edx
00B3568B  8B D8                           mov ebx, eax
00B3568D  85 C0                           test eax, eax
00B3568F  0F 88 6D 4F ED FF               js 0x140a0a602
00B35695  E9 40 56 ED FF                  jmp 0x140a0acda
00B3569A  49 8B CC                        mov rcx, r12
00B3569D  E8 76 5F ED FF                  call 0x140a0b618
00B356A2  33 D2                           xor edx, edx
00B356A4  89 45 98                        mov dword ptr [rbp - 0x68], eax
00B356A7  41 8B 4C 24 08                  mov ecx, dword ptr [r12 + 8]
00B356AC  44 8B C2                        mov r8d, edx
00B356AF  C1 E9 03                        shr ecx, 3
00B356B2  83 E1 07                        and ecx, 7
00B356B5  83 F9 07                        cmp ecx, 7
00B356B8  73 0F                           jae 0x140b356c9
00B356BA  4C 8D 05 3F A9 4C FF            lea r8, [rip - 0xb356c1]
00B356C1  45 8B 84 88 D0 21 04 00         mov r8d, dword ptr [r8 + rcx*4 + 0x421d0]
00B356C9  44 89 45 9C                     mov dword ptr [rbp - 0x64], r8d
00B356CD  4D 85 F6                        test r14, r14
00B356D0  75 27                           jne 0x140b356f9
00B356D2  41 8D 56 72                     lea edx, [r14 + 0x72]
00B356D6  B9 00 01 00 00                  mov ecx, 0x100
00B356DB  41 B8 50 4E 50 52               mov r8d, 0x52504e50
00B356E1  E8 0A CA 04 00                  call 0x140b820f0
00B356E6  4C 8B F0                        mov r14, rax
00B356E9  48 85 C0                        test rax, rax
00B356EC  0F 84 3B 56 ED FF               je 0x140a0ad2d
00B356F2  8B 45 98                        mov eax, dword ptr [rbp - 0x68]
00B356F5  44 8B 45 9C                     mov r8d, dword ptr [rbp - 0x64]
00B356F9  4D 8B CE                        mov r9, r14
00B356FC  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00B35700  8B D0                           mov edx, eax
00B35702  E8 01 59 ED FF                  call 0x140a0b008
00B35707  8B D8                           mov ebx, eax
00B35709  85 C0                           test eax, eax
00B3570B  0F 88 1D 4D ED FF               js 0x140a0a42e
00B35711  48 8D 44 24 65                  lea rax, [rsp + 0x65]
00B35716  49 8B D6                        mov rdx, r14
00B35719  4C 8D 4D C8                     lea r9, [rbp - 0x38]
00B3571D  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00B35722  48 8B CF                        mov rcx, rdi
00B35725  E8 B6 89 CF FF                  call 0x14082e0e0
00B3572A  4C 8B 6D C8                     mov r13, qword ptr [rbp - 0x38]
00B3572E  33 D2                           xor edx, edx
00B35730  8B D8                           mov ebx, eax
00B35732  85 C0                           test eax, eax
00B35734  0F 88 F4 4C ED FF               js 0x140a0a42e
00B3573A  41 8B 44 24 04                  mov eax, dword ptr [r12 + 4]
00B3573F  44 8D 42 06                     lea r8d, [rdx + 6]
00B35743  89 54 24 48                     mov dword ptr [rsp + 0x48], edx
00B35747  4D 8B CD                        mov r9, r13
00B3574A  0F B7 C8                        movzx ecx, ax
00B3574D  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00B35752  C7 44 24 40 04 00 00 00         mov dword ptr [rsp + 0x40], 4
00B3575A  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00B3575F  48 8D 05 3A D0 4E FF            lea rax, [rip - 0xb12fc6]
00B35766  C7 44 24 30 07 00 00 00         mov dword ptr [rsp + 0x30], 7
00B3576E  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B35773  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00B35778  49 8B D6                        mov rdx, r14
00B3577B  89 4C 24 60                     mov dword ptr [rsp + 0x60], ecx
00B3577F  48 8B CF                        mov rcx, rdi
00B35782  E8 61 0F DC FF                  call 0x1408f66e8
00B35787  33 D2                           xor edx, edx
00B35789  8B D8                           mov ebx, eax
00B3578B  85 C0                           test eax, eax
00B3578D  0F 88 9B 4C ED FF               js 0x140a0a42e
00B35793  41 0F B7 44 24 06               movzx eax, word ptr [r12 + 6]
00B35799  44 8D 42 06                     lea r8d, [rdx + 6]
00B3579D  89 54 24 48                     mov dword ptr [rsp + 0x48], edx
00B357A1  4D 8B CD                        mov r9, r13
00B357A4  C7 44 24 40 04 00 00 00         mov dword ptr [rsp + 0x40], 4
00B357AC  48 8B CF                        mov rcx, rdi
00B357AF  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
00B357B3  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00B357B8  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00B357BD  48 8D 05 E4 C9 4E FF            lea rax, [rip - 0xb1361c]
00B357C4  C7 44 24 30 07 00 00 00         mov dword ptr [rsp + 0x30], 7
00B357CC  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B357D1  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00B357D6  49 8B D6                        mov rdx, r14
00B357D9  E8 0A 0F DC FF                  call 0x1408f66e8
00B357DE  8B D8                           mov ebx, eax
00B357E0  85 C0                           test eax, eax
00B357E2  0F 88 46 4C ED FF               js 0x140a0a42e
00B357E8  41 8B 14 24                     mov edx, dword ptr [r12]
00B357EC  84 D2                           test dl, dl
00B357EE  78 79                           js 0x140b35869
00B357F0  8B C2                           mov eax, edx
00B357F2  4D 8B CD                        mov r9, r13
00B357F5  C1 E8 10                        shr eax, 0x10
00B357F8  0F B6 C8                        movzx ecx, al
00B357FB  41 0F B6 44 24 03               movzx eax, byte ptr [r12 + 3]
00B35801  C1 E0 08                        shl eax, 8
00B35804  0B C8                           or ecx, eax
00B35806  C1 EA 08                        shr edx, 8
00B35809  C1 E1 08                        shl ecx, 8
00B3580C  0F B6 C2                        movzx eax, dl
00B3580F  49 8B D6                        mov rdx, r14
00B35812  0B C8                           or ecx, eax
00B35814  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00B35819  81 C9 00 00 00 FF               or ecx, 0xff000000
00B3581F  89 4C 24 60                     mov dword ptr [rsp + 0x60], ecx
00B35823  33 C9                           xor ecx, ecx
00B35825  89 4C 24 48                     mov dword ptr [rsp + 0x48], ecx
00B35829  C7 44 24 40 04 00 00 00         mov dword ptr [rsp + 0x40], 4
00B35831  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00B35836  48 8D 05 53 BC 4E FF            lea rax, [rip - 0xb143ad]
00B3583D  C7 44 24 30 07 00 00 00         mov dword ptr [rsp + 0x30], 7
00B35845  44 8D 41 06                     lea r8d, [rcx + 6]
00B35849  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B3584E  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00B35853  48 8B CF                        mov rcx, rdi
00B35856  E8 8D 0E DC FF                  call 0x1408f66e8
00B3585B  8B D8                           mov ebx, eax
00B3585D  85 C0                           test eax, eax
00B3585F  0F 88 C9 4B ED FF               js 0x140a0a42e
00B35865  33 DB                           xor ebx, ebx
00B35867  EB 3C                           jmp 0x140b358a5
00B35869  33 DB                           xor ebx, ebx
00B3586B  38 5C 24 65                     cmp byte ptr [rsp + 0x65], bl
00B3586F  75 34                           jne 0x140b358a5
00B35871  89 5C 24 48                     mov dword ptr [rsp + 0x48], ebx
00B35875  48 8D 05 14 BC 4E FF            lea rax, [rip - 0xb143ec]
00B3587C  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
00B35880  44 8D 43 06                     lea r8d, [rbx + 6]
00B35884  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
00B35889  4D 8B CD                        mov r9, r13
00B3588C  89 5C 24 30                     mov dword ptr [rsp + 0x30], ebx
00B35890  49 8B D6                        mov rdx, r14
00B35893  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B35898  48 8B CF                        mov rcx, rdi
00B3589B  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00B358A0  E8 43 0E DC FF                  call 0x1408f66e8
00B358A5  48 83 7D 80 00                  cmp qword ptr [rbp - 0x80], 0
00B358AA  B8 10 00 00 00                  mov eax, 0x10
00B358AF  48 8B 4D A8                     mov rcx, qword ptr [rbp - 0x58]
00B358B3  8B 55 A0                        mov edx, dword ptr [rbp - 0x60]
00B358B6  0F 44 D0                        cmove edx, eax
00B358B9  48 89 4D 80                     mov qword ptr [rbp - 0x80], rcx
00B358BD  89 55 A0                        mov dword ptr [rbp - 0x60], edx
00B358C0  48 8B C1                        mov rax, rcx
00B358C3  48 85 C9                        test rcx, rcx
00B358C6  75 07                           jne 0x140b358cf
00B358C8  EB 6F                           jmp 0x140b35939
00B358CA  8B 55 A0                        mov edx, dword ptr [rbp - 0x60]
00B358CD  33 DB                           xor ebx, ebx
00B358CF  89 5C 24 50                     mov dword ptr [rsp + 0x50], ebx
00B358D3  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
00B358D8  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
00B358DD  4D 8B CF                        mov r9, r15
00B358E0  89 54 24 40                     mov dword ptr [rsp + 0x40], edx
00B358E4  41 B8 01 00 00 00               mov r8d, 1
00B358EA  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00B358EF  48 8B D6                        mov rdx, rsi
00B358F2  48 8D 45 88                     lea rax, [rbp - 0x78]
00B358F6  48 8B CF                        mov rcx, rdi
00B358F9  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00B358FE  48 8D 45 F8                     lea rax, [rbp - 8]
00B35902  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B35907  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00B3590C  E8 6F C8 DA FF                  call 0x1408e2180
00B35911  8B D8                           mov ebx, eax
00B35913  3D 23 00 00 C0                  cmp eax, 0xc0000023
00B35918  75 41                           jne 0x140b3595b
00B3591A  8B 45 A0                        mov eax, dword ptr [rbp - 0x60]
00B3591D  39 44 24 68                     cmp dword ptr [rsp + 0x68], eax
00B35921  0F 86 FC 53 ED FF               jbe 0x140a0ad23
00B35927  48 8B 4D 80                     mov rcx, qword ptr [rbp - 0x80]
00B3592B  33 D2                           xor edx, edx
00B3592D  E8 3E CF 04 00                  call 0x140b82870
00B35932  8B 54 24 68                     mov edx, dword ptr [rsp + 0x68]
00B35936  89 55 A0                        mov dword ptr [rbp - 0x60], edx
00B35939  B9 00 01 00 00                  mov ecx, 0x100
00B3593E  41 B8 50 4E 50 52               mov r8d, 0x52504e50
00B35944  E8 A7 C7 04 00                  call 0x140b820f0
00B35949  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
00B3594D  48 85 C0                        test rax, rax
00B35950  0F 84 D7 53 ED FF               je 0x140a0ad2d
00B35956  E9 6F FF FF FF                  jmp 0x140b358ca
00B3595B  3D 25 02 00 C0                  cmp eax, 0xc0000225
00B35960  75 0B                           jne 0x140b3596d
00B35962  48 8B 5D 80                     mov rbx, qword ptr [rbp - 0x80]
00B35966  83 23 E0                        and dword ptr [rbx], 0xffffffe0
00B35969  33 D2                           xor edx, edx
00B3596B  EB 29                           jmp 0x140b35996
00B3596D  33 D2                           xor edx, edx
00B3596F  85 C0                           test eax, eax
00B35971  0F 88 B7 4A ED FF               js 0x140a0a42e
00B35977  81 7D 88 03 10 00 00            cmp dword ptr [rbp - 0x78], 0x1003
00B3597E  75 0F                           jne 0x140b3598f
00B35980  8D 42 10                        lea eax, [rdx + 0x10]
00B35983  39 44 24 68                     cmp dword ptr [rsp + 0x68], eax
00B35987  72 06                           jb 0x140b3598f
00B35989  48 8B 5D 80                     mov rbx, qword ptr [rbp - 0x80]
00B3598D  EB 07                           jmp 0x140b35996
00B3598F  48 8B 5D 80                     mov rbx, qword ptr [rbp - 0x80]
00B35993  83 23 E0                        and dword ptr [rbx], 0xffffffe0
00B35996  8B 0B                           mov ecx, dword ptr [rbx]
00B35998  8B C1                           mov eax, ecx
00B3599A  24 1F                           and al, 0x1f
00B3599C  3C 01                           cmp al, 1
00B3599E  0F 82 54 08 00 00               jb 0x140b361f8
00B359A4  C1 E9 05                        shr ecx, 5
00B359A7  8B C2                           mov eax, edx
00B359A9  83 E1 0F                        and ecx, 0xf
00B359AC  83 F9 05                        cmp ecx, 5
00B359AF  73 10                           jae 0x140b359c1
00B359B1  8B C1                           mov eax, ecx
00B359B3  48 8D 0D 46 A6 4C FF            lea rcx, [rip - 0xb359ba]
00B359BA  8B 84 81 78 21 04 00            mov eax, dword ptr [rcx + rax*4 + 0x42178]
00B359C1  89 54 24 48                     mov dword ptr [rsp + 0x48], edx
00B359C5  4D 8B CD                        mov r9, r13
00B359C8  C7 44 24 40 04 00 00 00         mov dword ptr [rsp + 0x40], 4
00B359D0  41 B8 06 00 00 00               mov r8d, 6
00B359D6  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
00B359DA  48 8B CF                        mov rcx, rdi
00B359DD  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00B359E2  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00B359E7  48 8D 05 72 CA 4E FF            lea rax, [rip - 0xb1358e]
00B359EE  C7 44 24 30 07 00 00 00         mov dword ptr [rsp + 0x30], 7
00B359F6  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B359FB  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00B35A00  49 8B D6                        mov rdx, r14
00B35A03  E8 E0 0C DC FF                  call 0x1408f66e8
00B35A08  33 D2                           xor edx, edx
00B35A0A  8B D8                           mov ebx, eax
00B35A0C  85 C0                           test eax, eax
00B35A0E  0F 88 1A 4A ED FF               js 0x140a0a42e
00B35A14  48 8B 45 80                     mov rax, qword ptr [rbp - 0x80]
00B35A18  8B 08                           mov ecx, dword ptr [rax]
00B35A1A  8B C2                           mov eax, edx
00B35A1C  C1 E9 09                        shr ecx, 9
00B35A1F  83 E1 07                        and ecx, 7
00B35A22  83 F9 05                        cmp ecx, 5
00B35A25  73 10                           jae 0x140b35a37
00B35A27  8B C1                           mov eax, ecx
00B35A29  48 8D 0D D0 A5 4C FF            lea rcx, [rip - 0xb35a30]
00B35A30  8B 84 81 90 21 04 00            mov eax, dword ptr [rcx + rax*4 + 0x42190]
00B35A37  89 54 24 48                     mov dword ptr [rsp + 0x48], edx
00B35A3B  4D 8B CD                        mov r9, r13
00B35A3E  C7 44 24 40 04 00 00 00         mov dword ptr [rsp + 0x40], 4
00B35A46  41 B8 06 00 00 00               mov r8d, 6
00B35A4C  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
00B35A50  48 8B CF                        mov rcx, rdi
00B35A53  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00B35A58  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00B35A5D  48 8D 05 14 C4 4E FF            lea rax, [rip - 0xb13bec]
00B35A64  C7 44 24 30 07 00 00 00         mov dword ptr [rsp + 0x30], 7
00B35A6C  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B35A71  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00B35A76  49 8B D6                        mov rdx, r14
00B35A79  E8 6A 0C DC FF                  call 0x1408f66e8
00B35A7E  33 D2                           xor edx, edx
00B35A80  8B D8                           mov ebx, eax
00B35A82  85 C0                           test eax, eax
00B35A84  0F 88 A4 49 ED FF               js 0x140a0a42e
00B35A8A  4C 8B 4D B8                     mov r9, qword ptr [rbp - 0x48]
00B35A8E  4D 85 C9                        test r9, r9
00B35A91  75 26                           jne 0x140b35ab9
00B35A93  41 8D 51 72                     lea edx, [r9 + 0x72]
00B35A97  B9 00 01 00 00                  mov ecx, 0x100
00B35A9C  41 B8 50 4E 50 52               mov r8d, 0x52504e50
00B35AA2  E8 49 C6 04 00                  call 0x140b820f0
00B35AA7  33 D2                           xor edx, edx
00B35AA9  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
00B35AAD  4C 8B C8                        mov r9, rax
00B35AB0  48 85 C0                        test rax, rax
00B35AB3  0F 84 74 52 ED FF               je 0x140a0ad2d
00B35AB9  48 8B 45 80                     mov rax, qword ptr [rbp - 0x80]
00B35ABD  44 8B C2                        mov r8d, edx
00B35AC0  8B 08                           mov ecx, dword ptr [rax]
00B35AC2  C1 E9 14                        shr ecx, 0x14
00B35AC5  83 E1 07                        and ecx, 7
00B35AC8  83 F9 07                        cmp ecx, 7
00B35ACB  73 0F                           jae 0x140b35adc
00B35ACD  48 8D 15 2C A5 4C FF            lea rdx, [rip - 0xb35ad4]
00B35AD4  44 8B 84 8A D0 21 04 00         mov r8d, dword ptr [rdx + rcx*4 + 0x421d0]
00B35ADC  44 89 44 24 60                  mov dword ptr [rsp + 0x60], r8d
00B35AE1  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00B35AE5  8B 00                           mov eax, dword ptr [rax]
00B35AE7  C1 E8 0C                        shr eax, 0xc
00B35AEA  0F B6 D0                        movzx edx, al
00B35AED  E8 16 55 ED FF                  call 0x140a0b008
00B35AF2  33 D2                           xor edx, edx
00B35AF4  8B D8                           mov ebx, eax
00B35AF6  85 C0                           test eax, eax
00B35AF8  0F 88 30 49 ED FF               js 0x140a0a42e
00B35AFE  48 8B 4D B8                     mov rcx, qword ptr [rbp - 0x48]
00B35B02  48 83 C8 FF                     or rax, 0xffffffffffffffff
00B35B06  48 FF C0                        inc rax
00B35B09  66 39 14 41                     cmp word ptr [rcx + rax*2], dx
00B35B0D  75 F7                           jne 0x140b35b06
00B35B0F  89 54 24 48                     mov dword ptr [rsp + 0x48], edx
00B35B13  8D 04 45 02 00 00 00            lea eax, [rax*2 + 2]
00B35B1A  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00B35B1E  4D 8B CD                        mov r9, r13
00B35B21  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
00B35B26  48 8D 05 EB B6 4E FF            lea rax, [rip - 0xb14915]
00B35B2D  C7 44 24 30 12 00 00 00         mov dword ptr [rsp + 0x30], 0x12
00B35B35  41 B8 06 00 00 00               mov r8d, 6
00B35B3B  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B35B40  48 8B CF                        mov rcx, rdi
00B35B43  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00B35B48  49 8B D6                        mov rdx, r14
00B35B4B  E8 98 0B DC FF                  call 0x1408f66e8
00B35B50  33 D2                           xor edx, edx
00B35B52  8B D8                           mov ebx, eax
00B35B54  85 C0                           test eax, eax
00B35B56  0F 88 D2 48 ED FF               js 0x140a0a42e
00B35B5C  48 8B 45 80                     mov rax, qword ptr [rbp - 0x80]
00B35B60  8B 08                           mov ecx, dword ptr [rax]
00B35B62  8B C2                           mov eax, edx
00B35B64  C1 E9 17                        shr ecx, 0x17
00B35B67  83 E1 07                        and ecx, 7
00B35B6A  83 F9 05                        cmp ecx, 5
00B35B6D  73 10                           jae 0x140b35b7f
00B35B6F  8B C1                           mov eax, ecx
00B35B71  48 8D 0D 88 A4 4C FF            lea rcx, [rip - 0xb35b78]
00B35B78  8B 84 81 90 21 04 00            mov eax, dword ptr [rcx + rax*4 + 0x42190]
00B35B7F  89 54 24 48                     mov dword ptr [rsp + 0x48], edx
00B35B83  4D 8B CD                        mov r9, r13
00B35B86  C7 44 24 40 04 00 00 00         mov dword ptr [rsp + 0x40], 4
00B35B8E  41 B8 06 00 00 00               mov r8d, 6
00B35B94  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
00B35B98  48 8B CF                        mov rcx, rdi
00B35B9B  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00B35BA0  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00B35BA5  48 8D 05 14 D5 4E FF            lea rax, [rip - 0xb12aec]
00B35BAC  C7 44 24 30 07 00 00 00         mov dword ptr [rsp + 0x30], 7
00B35BB4  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B35BB9  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00B35BBE  49 8B D6                        mov rdx, r14
00B35BC1  E8 22 0B DC FF                  call 0x1408f66e8
00B35BC6  8B D8                           mov ebx, eax
00B35BC8  85 C0                           test eax, eax
00B35BCA  0F 88 5E 48 ED FF               js 0x140a0a42e
00B35BD0  41 0F B7 54 24 12               movzx edx, word ptr [r12 + 0x12]
00B35BD6  41 B8 FF FF 00 00               mov r8d, 0xffff
00B35BDC  66 41 3B D0                     cmp dx, r8w
00B35BE0  0F 84 EE 00 00 00               je 0x140b35cd4
00B35BE6  41 8B 44 24 10                  mov eax, dword ptr [r12 + 0x10]
00B35BEB  0F B7 C8                        movzx ecx, ax
00B35BEE  41 3B C8                        cmp ecx, r8d
00B35BF1  0F 84 DD 00 00 00               je 0x140b35cd4
00B35BF7  33 C9                           xor ecx, ecx
00B35BF9  89 54 24 60                     mov dword ptr [rsp + 0x60], edx
00B35BFD  89 4C 24 48                     mov dword ptr [rsp + 0x48], ecx
00B35C01  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00B35C06  C7 44 24 40 04 00 00 00         mov dword ptr [rsp + 0x40], 4
00B35C0E  4D 8B CD                        mov r9, r13
00B35C11  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00B35C16  49 8B D6                        mov rdx, r14
00B35C19  48 8D 05 D0 BE 4E FF            lea rax, [rip - 0xb14130]
00B35C20  C7 44 24 30 07 00 00 00         mov dword ptr [rsp + 0x30], 7
00B35C28  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B35C2D  44 8D 41 06                     lea r8d, [rcx + 6]
00B35C31  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00B35C36  48 8B CF                        mov rcx, rdi
00B35C39  E8 AA 0A DC FF                  call 0x1408f66e8
00B35C3E  33 D2                           xor edx, edx
00B35C40  8B D8                           mov ebx, eax
00B35C42  85 C0                           test eax, eax
00B35C44  0F 88 E4 47 ED FF               js 0x140a0a42e
00B35C4A  41 8B 44 24 10                  mov eax, dword ptr [r12 + 0x10]
00B35C4F  44 8D 42 06                     lea r8d, [rdx + 6]
00B35C53  89 54 24 48                     mov dword ptr [rsp + 0x48], edx
00B35C57  4D 8B CD                        mov r9, r13
00B35C5A  0F B7 C8                        movzx ecx, ax
00B35C5D  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00B35C62  C7 44 24 40 04 00 00 00         mov dword ptr [rsp + 0x40], 4
00B35C6A  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00B35C6F  48 8D 05 42 B0 4E FF            lea rax, [rip - 0xb14fbe]
00B35C76  C7 44 24 30 07 00 00 00         mov dword ptr [rsp + 0x30], 7
00B35C7E  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B35C83  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00B35C88  49 8B D6                        mov rdx, r14
00B35C8B  89 4C 24 60                     mov dword ptr [rsp + 0x60], ecx
00B35C8F  48 8B CF                        mov rcx, rdi
00B35C92  E8 51 0A DC FF                  call 0x1408f66e8
00B35C97  33 D2                           xor edx, edx
00B35C99  8B D8                           mov ebx, eax
00B35C9B  85 C0                           test eax, eax
00B35C9D  0F 88 8B 47 ED FF               js 0x140a0a42e
00B35CA3  38 54 24 65                     cmp byte ptr [rsp + 0x65], dl
00B35CA7  0F 85 D5 00 00 00               jne 0x140b35d82
00B35CAD  89 54 24 48                     mov dword ptr [rsp + 0x48], edx
00B35CB1  48 8D 05 20 C7 4E FF            lea rax, [rip - 0xb138e0]
00B35CB8  89 54 24 40                     mov dword ptr [rsp + 0x40], edx
00B35CBC  48 89 54 24 38                  mov qword ptr [rsp + 0x38], rdx
00B35CC1  89 54 24 30                     mov dword ptr [rsp + 0x30], edx
00B35CC5  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B35CCA  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00B35CCF  E9 98 00 00 00                  jmp 0x140b35d6c
00B35CD4  33 D2                           xor edx, edx
00B35CD6  38 54 24 65                     cmp byte ptr [rsp + 0x65], dl
00B35CDA  0F 85 A2 00 00 00               jne 0x140b35d82
00B35CE0  89 54 24 48                     mov dword ptr [rsp + 0x48], edx
00B35CE4  48 8D 05 05 BE 4E FF            lea rax, [rip - 0xb141fb]
00B35CEB  89 54 24 40                     mov dword ptr [rsp + 0x40], edx
00B35CEF  44 8D 42 06                     lea r8d, [rdx + 6]
00B35CF3  48 89 54 24 38                  mov qword ptr [rsp + 0x38], rdx
00B35CF8  4D 8B CD                        mov r9, r13
00B35CFB  89 54 24 30                     mov dword ptr [rsp + 0x30], edx
00B35CFF  48 8B CF                        mov rcx, rdi
00B35D02  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B35D07  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00B35D0C  49 8B D6                        mov rdx, r14
00B35D0F  E8 D4 09 DC FF                  call 0x1408f66e8
00B35D14  33 DB                           xor ebx, ebx
00B35D16  48 8D 05 9B AF 4E FF            lea rax, [rip - 0xb15065]
00B35D1D  89 5C 24 48                     mov dword ptr [rsp + 0x48], ebx
00B35D21  4D 8B CD                        mov r9, r13
00B35D24  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
00B35D28  49 8B D6                        mov rdx, r14
00B35D2B  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
00B35D30  48 8B CF                        mov rcx, rdi
00B35D33  89 5C 24 30                     mov dword ptr [rsp + 0x30], ebx
00B35D37  44 8D 43 06                     lea r8d, [rbx + 6]
00B35D3B  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B35D40  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00B35D45  E8 9E 09 DC FF                  call 0x1408f66e8
00B35D4A  89 5C 24 48                     mov dword ptr [rsp + 0x48], ebx
00B35D4E  48 8D 05 83 C6 4E FF            lea rax, [rip - 0xb1397d]
00B35D55  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
00B35D59  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
00B35D5E  89 5C 24 30                     mov dword ptr [rsp + 0x30], ebx
00B35D62  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B35D67  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00B35D6C  4D 8B CD                        mov r9, r13
00B35D6F  41 B8 06 00 00 00               mov r8d, 6
00B35D75  49 8B D6                        mov rdx, r14
00B35D78  48 8B CF                        mov rcx, rdi
00B35D7B  E8 68 09 DC FF                  call 0x1408f66e8
00B35D80  33 D2                           xor edx, edx
00B35D82  48 8B 45 80                     mov rax, qword ptr [rbp - 0x80]
00B35D86  4D 8B CD                        mov r9, r13
00B35D89  89 54 24 48                     mov dword ptr [rsp + 0x48], edx
00B35D8D  41 B8 06 00 00 00               mov r8d, 6
00B35D93  C7 44 24 40 04 00 00 00         mov dword ptr [rsp + 0x40], 4
00B35D9B  8B 40 08                        mov eax, dword ptr [rax + 8]
00B35D9E  0F B7 C8                        movzx ecx, ax
00B35DA1  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00B35DA6  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00B35DAB  48 8D 05 96 C3 4E FF            lea rax, [rip - 0xb13c6a]
00B35DB2  C7 44 24 30 07 00 00 00         mov dword ptr [rsp + 0x30], 7
00B35DBA  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B35DBF  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00B35DC4  49 8B D6                        mov rdx, r14
00B35DC7  89 4C 24 60                     mov dword ptr [rsp + 0x60], ecx
00B35DCB  48 8B CF                        mov rcx, rdi
00B35DCE  E8 15 09 DC FF                  call 0x1408f66e8
00B35DD3  33 D2                           xor edx, edx
00B35DD5  8B D8                           mov ebx, eax
00B35DD7  85 C0                           test eax, eax
00B35DD9  0F 88 4F 46 ED FF               js 0x140a0a42e
00B35DDF  48 8B 45 80                     mov rax, qword ptr [rbp - 0x80]
00B35DE3  44 8D 42 06                     lea r8d, [rdx + 6]
00B35DE7  89 54 24 48                     mov dword ptr [rsp + 0x48], edx
00B35DEB  4D 8B CD                        mov r9, r13
00B35DEE  C7 44 24 40 04 00 00 00         mov dword ptr [rsp + 0x40], 4
00B35DF6  48 8B CF                        mov rcx, rdi
00B35DF9  0F B7 40 0A                     movzx eax, word ptr [rax + 0xa]
00B35DFD  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
00B35E01  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00B35E06  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00B35E0B  48 8D 05 4E CD 4E FF            lea rax, [rip - 0xb132b2]
00B35E12  C7 44 24 30 07 00 00 00         mov dword ptr [rsp + 0x30], 7
00B35E1A  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B35E1F  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00B35E24  49 8B D6                        mov rdx, r14
00B35E27  E8 BC 08 DC FF                  call 0x1408f66e8
00B35E2C  33 D2                           xor edx, edx
00B35E2E  8B D8                           mov ebx, eax
00B35E30  85 C0                           test eax, eax
00B35E32  0F 88 F6 45 ED FF               js 0x140a0a42e
00B35E38  48 8B 45 80                     mov rax, qword ptr [rbp - 0x80]
00B35E3C  44 8D 42 06                     lea r8d, [rdx + 6]
00B35E40  89 54 24 48                     mov dword ptr [rsp + 0x48], edx
00B35E44  4D 8B CD                        mov r9, r13
00B35E47  C7 44 24 40 04 00 00 00         mov dword ptr [rsp + 0x40], 4
00B35E4F  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00B35E52  0F B7 C8                        movzx ecx, ax
00B35E55  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00B35E5A  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00B35E5F  48 8D 05 82 AE 4E FF            lea rax, [rip - 0xb1517e]
00B35E66  C7 44 24 30 07 00 00 00         mov dword ptr [rsp + 0x30], 7
00B35E6E  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B35E73  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00B35E78  49 8B D6                        mov rdx, r14
00B35E7B  89 4C 24 60                     mov dword ptr [rsp + 0x60], ecx
00B35E7F  48 8B CF                        mov rcx, rdi
00B35E82  E8 61 08 DC FF                  call 0x1408f66e8
00B35E87  8B D8                           mov ebx, eax
00B35E89  85 C0                           test eax, eax
00B35E8B  0F 88 9D 45 ED FF               js 0x140a0a42e
00B35E91  48 8B 45 80                     mov rax, qword ptr [rbp - 0x80]
00B35E95  4D 8B CD                        mov r9, r13
00B35E98  0F B7 48 0E                     movzx ecx, word ptr [rax + 0xe]
00B35E9C  B8 6D C1 16 6C                  mov eax, 0x6c16c16d
00B35EA1  81 E1 FF 01 00 00               and ecx, 0x1ff
00B35EA7  F7 E1                           mul ecx
00B35EA9  8B C1                           mov eax, ecx
00B35EAB  2B C2                           sub eax, edx
00B35EAD  D1 E8                           shr eax, 1
00B35EAF  03 C2                           add eax, edx
00B35EB1  49 8B D6                        mov rdx, r14
00B35EB4  C1 E8 08                        shr eax, 8
00B35EB7  69 C0 68 01 00 00               imul eax, eax, 0x168
00B35EBD  2B C8                           sub ecx, eax
00B35EBF  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00B35EC4  89 4C 24 60                     mov dword ptr [rsp + 0x60], ecx
00B35EC8  33 C9                           xor ecx, ecx
00B35ECA  89 4C 24 48                     mov dword ptr [rsp + 0x48], ecx
00B35ECE  C7 44 24 40 04 00 00 00         mov dword ptr [rsp + 0x40], 4
00B35ED6  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00B35EDB  48 8D 05 E6 B6 4E FF            lea rax, [rip - 0xb1491a]
00B35EE2  C7 44 24 30 07 00 00 00         mov dword ptr [rsp + 0x30], 7
00B35EEA  44 8D 41 06                     lea r8d, [rcx + 6]
00B35EEE  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B35EF3  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00B35EF8  48 8B CF                        mov rcx, rdi
00B35EFB  E8 E8 07 DC FF                  call 0x1408f66e8
00B35F00  33 D2                           xor edx, edx
00B35F02  8B D8                           mov ebx, eax
00B35F04  85 C0                           test eax, eax
00B35F06  0F 88 22 45 ED FF               js 0x140a0a42e
00B35F0C  48 8B 45 80                     mov rax, qword ptr [rbp - 0x80]
00B35F10  48 8D 0D E9 A0 4C FF            lea rcx, [rip - 0xb35f17]
00B35F17  89 54 24 48                     mov dword ptr [rsp + 0x48], edx
00B35F1B  44 8D 42 06                     lea r8d, [rdx + 6]
00B35F1F  C7 44 24 40 04 00 00 00         mov dword ptr [rsp + 0x40], 4
00B35F27  4D 8B CD                        mov r9, r13
00B35F2A  8B 00                           mov eax, dword ptr [rax]
00B35F2C  48 C1 E8 1F                     shr rax, 0x1f
00B35F30  8B 84 81 70 21 04 00            mov eax, dword ptr [rcx + rax*4 + 0x42170]
00B35F37  48 8B CF                        mov rcx, rdi
00B35F3A  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
00B35F3E  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00B35F43  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00B35F48  48 8D 05 41 B0 4E FF            lea rax, [rip - 0xb14fbf]
00B35F4F  C7 44 24 30 07 00 00 00         mov dword ptr [rsp + 0x30], 7
00B35F57  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B35F5C  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00B35F61  49 8B D6                        mov rdx, r14
00B35F64  E8 7F 07 DC FF                  call 0x1408f66e8
00B35F69  33 D2                           xor edx, edx
00B35F6B  8B D8                           mov ebx, eax
00B35F6D  85 C0                           test eax, eax
00B35F6F  0F 88 B9 44 ED FF               js 0x140a0a42e
00B35F75  48 8B 5D 80                     mov rbx, qword ptr [rbp - 0x80]
00B35F79  8B 03                           mov eax, dword ptr [rbx]
00B35F7B  C1 E8 05                        shr eax, 5
00B35F7E  83 E0 0F                        and eax, 0xf
00B35F81  0F 84 40 02 00 00               je 0x140b361c7
00B35F87  83 E8 01                        sub eax, 1
00B35F8A  74 13                           je 0x140b35f9f
00B35F8C  83 E8 01                        sub eax, 1
00B35F8F  74 0E                           je 0x140b35f9f
00B35F91  83 E8 01                        sub eax, 1
00B35F94  74 09                           je 0x140b35f9f
00B35F96  83 F8 01                        cmp eax, 1
00B35F99  0F 85 28 02 00 00               jne 0x140b361c7
00B35F9F  89 54 24 48                     mov dword ptr [rsp + 0x48], edx
00B35FA3  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00B35FA8  C7 44 24 40 04 00 00 00         mov dword ptr [rsp + 0x40], 4
00B35FB0  4D 8B CD                        mov r9, r13
00B35FB3  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00B35FB8  41 B8 06 00 00 00               mov r8d, 6
00B35FBE  48 8D 05 93 C5 4E FF            lea rax, [rip - 0xb13a6d]
00B35FC5  C7 44 24 30 07 00 00 00         mov dword ptr [rsp + 0x30], 7
00B35FCD  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B35FD2  48 8B CF                        mov rcx, rdi
00B35FD5  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00B35FDA  89 54 24 60                     mov dword ptr [rsp + 0x60], edx
00B35FDE  49 8B D6                        mov rdx, r14
00B35FE1  E8 02 07 DC FF                  call 0x1408f66e8
00B35FE6  33 D2                           xor edx, edx
00B35FE8  85 C0                           test eax, eax
00B35FEA  0F 88 E2 05 00 00               js 0x140b365d2
00B35FF0  8B 43 04                        mov eax, dword ptr [rbx + 4]
00B35FF3  44 0F B7 43 06                  movzx r8d, word ptr [rbx + 6]
00B35FF8  0F B7 C8                        movzx ecx, ax
00B35FFB  8B 03                           mov eax, dword ptr [rbx]
00B35FFD  25 E0 01 00 00                  and eax, 0x1e0
00B36002  83 F8 20                        cmp eax, 0x20
00B36005  75 05                           jne 0x140b3600c
00B36007  41 03 C8                        add ecx, r8d
00B3600A  EB 3E                           jmp 0x140b3604a
00B3600C  41 B9 6D C1 16 6C               mov r9d, 0x6c16c16d
00B36012  41 8B C1                        mov eax, r9d
00B36015  F7 E1                           mul ecx
00B36017  8B C1                           mov eax, ecx
00B36019  2B C2                           sub eax, edx
00B3601B  D1 E8                           shr eax, 1
00B3601D  03 C2                           add eax, edx
00B3601F  C1 E8 08                        shr eax, 8
00B36022  69 C0 68 01 00 00               imul eax, eax, 0x168
00B36028  2B C8                           sub ecx, eax
00B3602A  41 8B C1                        mov eax, r9d
00B3602D  41 F7 E0                        mul r8d
00B36030  41 8B C0                        mov eax, r8d
00B36033  2B C2                           sub eax, edx
00B36035  D1 E8                           shr eax, 1
00B36037  03 C2                           add eax, edx
00B36039  C1 E8 08                        shr eax, 8
00B3603C  69 C0 68 01 00 00               imul eax, eax, 0x168
00B36042  44 2B C0                        sub r8d, eax
00B36045  41 03 C8                        add ecx, r8d
00B36048  33 D2                           xor edx, edx
00B3604A  89 54 24 48                     mov dword ptr [rsp + 0x48], edx
00B3604E  48 8D 45 B0                     lea rax, [rbp - 0x50]
00B36052  C7 44 24 40 04 00 00 00         mov dword ptr [rsp + 0x40], 4
00B3605A  4D 8B CD                        mov r9, r13
00B3605D  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00B36062  41 B8 06 00 00 00               mov r8d, 6
00B36068  48 8D 05 11 C1 4E FF            lea rax, [rip - 0xb13eef]
00B3606F  C7 44 24 30 07 00 00 00         mov dword ptr [rsp + 0x30], 7
00B36077  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B3607C  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00B36081  49 8B D6                        mov rdx, r14
00B36084  89 4D B0                        mov dword ptr [rbp - 0x50], ecx
00B36087  48 8B CF                        mov rcx, rdi
00B3608A  E8 59 06 DC FF                  call 0x1408f66e8
00B3608F  33 D2                           xor edx, edx
00B36091  85 C0                           test eax, eax
00B36093  0F 88 39 05 00 00               js 0x140b365d2
00B36099  8B 03                           mov eax, dword ptr [rbx]
00B3609B  0F B7 4B 06                     movzx ecx, word ptr [rbx + 6]
00B3609F  25 E0 01 00 00                  and eax, 0x1e0
00B360A4  83 F8 20                        cmp eax, 0x20
00B360A7  74 1C                           je 0x140b360c5
00B360A9  B8 6D C1 16 6C                  mov eax, 0x6c16c16d
00B360AE  F7 E1                           mul ecx
00B360B0  8B C1                           mov eax, ecx
00B360B2  2B C2                           sub eax, edx
00B360B4  D1 E8                           shr eax, 1
00B360B6  03 C2                           add eax, edx
00B360B8  C1 E8 08                        shr eax, 8
00B360BB  69 C0 68 01 00 00               imul eax, eax, 0x168
00B360C1  2B C8                           sub ecx, eax
00B360C3  33 D2                           xor edx, edx
00B360C5  89 54 24 48                     mov dword ptr [rsp + 0x48], edx
00B360C9  48 8D 45 B4                     lea rax, [rbp - 0x4c]
00B360CD  C7 44 24 40 04 00 00 00         mov dword ptr [rsp + 0x40], 4
00B360D5  4D 8B CD                        mov r9, r13
00B360D8  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00B360DD  41 B8 06 00 00 00               mov r8d, 6
00B360E3  48 8D 05 C6 C2 4E FF            lea rax, [rip - 0xb13d3a]
00B360EA  C7 44 24 30 07 00 00 00         mov dword ptr [rsp + 0x30], 7
00B360F2  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B360F7  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00B360FC  49 8B D6                        mov rdx, r14
00B360FF  89 4D B4                        mov dword ptr [rbp - 0x4c], ecx
00B36102  48 8B CF                        mov rcx, rdi
00B36105  E8 DE 05 DC FF                  call 0x1408f66e8
00B3610A  33 D2                           xor edx, edx
00B3610C  85 C0                           test eax, eax
00B3610E  0F 88 BE 04 00 00               js 0x140b365d2
00B36114  89 54 24 50                     mov dword ptr [rsp + 0x50], edx
00B36118  48 8D 44 24 68                  lea rax, [rsp + 0x68]
00B3611D  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00B36122  44 8D 42 06                     lea r8d, [rdx + 6]
00B36126  C7 44 24 40 04 00 00 00         mov dword ptr [rsp + 0x40], 4
00B3612E  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00B36133  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00B36138  4D 8B CD                        mov r9, r13
00B3613B  48 8D 45 88                     lea rax, [rbp - 0x78]
00B3613F  48 8B CF                        mov rcx, rdi
00B36142  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00B36147  48 8D 05 C2 C3 4E FF            lea rax, [rip - 0xb13c3e]
00B3614E  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B36153  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00B36158  49 8B D6                        mov rdx, r14
00B3615B  E8 20 C0 DA FF                  call 0x1408e2180
00B36160  33 D2                           xor edx, edx
00B36162  85 C0                           test eax, eax
00B36164  78 1A                           js 0x140b36180
00B36166  83 7D 88 07                     cmp dword ptr [rbp - 0x78], 7
00B3616A  75 14                           jne 0x140b36180
00B3616C  83 7C 24 68 04                  cmp dword ptr [rsp + 0x68], 4
00B36171  75 0D                           jne 0x140b36180
00B36173  8B 45 B0                        mov eax, dword ptr [rbp - 0x50]
00B36176  39 44 24 60                     cmp dword ptr [rsp + 0x60], eax
00B3617A  0F 86 52 04 00 00               jbe 0x140b365d2
00B36180  89 54 24 48                     mov dword ptr [rsp + 0x48], edx
00B36184  48 8D 45 B4                     lea rax, [rbp - 0x4c]
00B36188  C7 44 24 40 04 00 00 00         mov dword ptr [rsp + 0x40], 4
00B36190  4D 8B CD                        mov r9, r13
00B36193  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00B36198  41 B8 06 00 00 00               mov r8d, 6
00B3619E  48 8D 05 6B C3 4E FF            lea rax, [rip - 0xb13c95]
00B361A5  C7 44 24 30 07 00 00 00         mov dword ptr [rsp + 0x30], 7
00B361AD  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B361B2  48 8B CF                        mov rcx, rdi
00B361B5  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00B361BA  49 8B D6                        mov rdx, r14
00B361BD  E8 26 05 DC FF                  call 0x1408f66e8
00B361C2  E9 09 04 00 00                  jmp 0x140b365d0
00B361C7  38 54 24 65                     cmp byte ptr [rsp + 0x65], dl
00B361CB  0F 85 01 04 00 00               jne 0x140b365d2
00B361D1  89 54 24 48                     mov dword ptr [rsp + 0x48], edx
00B361D5  48 8D 05 7C C3 4E FF            lea rax, [rip - 0xb13c84]
00B361DC  89 54 24 40                     mov dword ptr [rsp + 0x40], edx
00B361E0  48 89 54 24 38                  mov qword ptr [rsp + 0x38], rdx
00B361E5  89 54 24 30                     mov dword ptr [rsp + 0x30], edx
00B361E9  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B361EE  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00B361F3  E9 22 03 00 00                  jmp 0x140b3651a
00B361F8  38 54 24 65                     cmp byte ptr [rsp + 0x65], dl
00B361FC  0F 85 D0 03 00 00               jne 0x140b365d2
00B36202  89 54 24 48                     mov dword ptr [rsp + 0x48], edx
00B36206  48 8D 05 53 C2 4E FF            lea rax, [rip - 0xb13dad]
00B3620D  89 54 24 40                     mov dword ptr [rsp + 0x40], edx
00B36211  4D 8B CD                        mov r9, r13
00B36214  48 89 54 24 38                  mov qword ptr [rsp + 0x38], rdx
00B36219  41 B8 06 00 00 00               mov r8d, 6
00B3621F  89 54 24 30                     mov dword ptr [rsp + 0x30], edx
00B36223  48 8B CF                        mov rcx, rdi
00B36226  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B3622B  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00B36230  49 8B D6                        mov rdx, r14
00B36233  E8 B0 04 DC FF                  call 0x1408f66e8
00B36238  33 C0                           xor eax, eax
00B3623A  48 8D 0D 37 BC 4E FF            lea rcx, [rip - 0xb143c9]
00B36241  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00B36245  4D 8B CD                        mov r9, r13
00B36248  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00B3624C  49 8B D6                        mov rdx, r14
00B3624F  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00B36254  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00B36258  44 8D 40 06                     lea r8d, [rax + 6]
00B3625C  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00B36261  48 8B CF                        mov rcx, rdi
00B36264  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00B36269  E8 7A 04 DC FF                  call 0x1408f66e8
00B3626E  33 C0                           xor eax, eax
00B36270  48 8D 0D A1 AF 4E FF            lea rcx, [rip - 0xb1505f]
00B36277  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00B3627B  4D 8B CD                        mov r9, r13
00B3627E  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00B36282  49 8B D6                        mov rdx, r14
00B36285  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00B3628A  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00B3628E  44 8D 40 06                     lea r8d, [rax + 6]
00B36292  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00B36297  48 8B CF                        mov rcx, rdi
00B3629A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00B3629F  E8 44 04 DC FF                  call 0x1408f66e8
00B362A4  33 C0                           xor eax, eax
00B362A6  48 8D 0D 13 CE 4E FF            lea rcx, [rip - 0xb131ed]
00B362AD  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00B362B1  4D 8B CD                        mov r9, r13
00B362B4  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00B362B8  49 8B D6                        mov rdx, r14
00B362BB  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00B362C0  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00B362C4  44 8D 40 06                     lea r8d, [rax + 6]
00B362C8  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00B362CD  48 8B CF                        mov rcx, rdi
00B362D0  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00B362D5  E8 0E 04 DC FF                  call 0x1408f66e8
00B362DA  33 C0                           xor eax, eax
00B362DC  48 8D 0D 0D B8 4E FF            lea rcx, [rip - 0xb147f3]
00B362E3  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00B362E7  4D 8B CD                        mov r9, r13
00B362EA  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00B362EE  49 8B D6                        mov rdx, r14
00B362F1  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00B362F6  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00B362FA  44 8D 40 06                     lea r8d, [rax + 6]
00B362FE  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00B36303  48 8B CF                        mov rcx, rdi
00B36306  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00B3630B  E8 D8 03 DC FF                  call 0x1408f66e8
00B36310  33 C0                           xor eax, eax
00B36312  48 8D 0D 9F A9 4E FF            lea rcx, [rip - 0xb15661]
00B36319  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00B3631D  4D 8B CD                        mov r9, r13
00B36320  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00B36324  49 8B D6                        mov rdx, r14
00B36327  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00B3632C  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00B36330  44 8D 40 06                     lea r8d, [rax + 6]
00B36334  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00B36339  48 8B CF                        mov rcx, rdi
00B3633C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00B36341  E8 A2 03 DC FF                  call 0x1408f66e8
00B36346  33 C0                           xor eax, eax
00B36348  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00B3634C  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00B36350  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00B36355  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00B36359  48 8D 0D 78 C0 4E FF            lea rcx, [rip - 0xb13f88]
00B36360  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00B36365  44 8D 40 06                     lea r8d, [rax + 6]
00B36369  48 8B CF                        mov rcx, rdi
00B3636C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00B36371  4D 8B CD                        mov r9, r13
00B36374  49 8B D6                        mov rdx, r14
00B36377  E8 6C 03 DC FF                  call 0x1408f66e8
00B3637C  33 C0                           xor eax, eax
00B3637E  48 8D 0D C3 BD 4E FF            lea rcx, [rip - 0xb1423d]
00B36385  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00B36389  4D 8B CD                        mov r9, r13
00B3638C  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00B36390  49 8B D6                        mov rdx, r14
00B36393  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00B36398  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00B3639C  44 8D 40 06                     lea r8d, [rax + 6]
00B363A0  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00B363A5  48 8B CF                        mov rcx, rdi
00B363A8  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00B363AD  E8 36 03 DC FF                  call 0x1408f66e8
00B363B2  33 C0                           xor eax, eax
00B363B4  48 8D 0D A5 C7 4E FF            lea rcx, [rip - 0xb1385b]
00B363BB  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00B363BF  4D 8B CD                        mov r9, r13
00B363C2  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00B363C6  49 8B D6                        mov rdx, r14
00B363C9  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00B363CE  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00B363D2  44 8D 40 06                     lea r8d, [rax + 6]
00B363D6  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00B363DB  48 8B CF                        mov rcx, rdi
00B363DE  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00B363E3  E8 00 03 DC FF                  call 0x1408f66e8
00B363E8  33 C0                           xor eax, eax
00B363EA  48 8D 0D F7 A8 4E FF            lea rcx, [rip - 0xb15709]
00B363F1  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00B363F5  4D 8B CD                        mov r9, r13
00B363F8  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00B363FC  49 8B D6                        mov rdx, r14
00B363FF  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00B36404  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00B36408  44 8D 40 06                     lea r8d, [rax + 6]
00B3640C  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00B36411  48 8B CF                        mov rcx, rdi
00B36414  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00B36419  E8 CA 02 DC FF                  call 0x1408f66e8
00B3641E  33 C9                           xor ecx, ecx
00B36420  48 8D 05 41 A8 4E FF            lea rax, [rip - 0xb157bf]
00B36427  89 4C 24 48                     mov dword ptr [rsp + 0x48], ecx
00B3642B  4D 8B CD                        mov r9, r13
00B3642E  89 4C 24 40                     mov dword ptr [rsp + 0x40], ecx
00B36432  49 8B D6                        mov rdx, r14
00B36435  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
00B3643A  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
00B3643E  44 8D 41 06                     lea r8d, [rcx + 6]
00B36442  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B36447  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00B3644C  48 8B CF                        mov rcx, rdi
00B3644F  E8 94 02 DC FF                  call 0x1408f66e8
00B36454  33 C9                           xor ecx, ecx
00B36456  48 8D 05 83 BC 4E FF            lea rax, [rip - 0xb1437d]
00B3645D  89 4C 24 48                     mov dword ptr [rsp + 0x48], ecx
00B36461  4D 8B CD                        mov r9, r13
00B36464  89 4C 24 40                     mov dword ptr [rsp + 0x40], ecx
00B36468  49 8B D6                        mov rdx, r14
00B3646B  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
00B36470  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
00B36474  44 8D 41 06                     lea r8d, [rcx + 6]
00B36478  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B3647D  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00B36482  48 8B CF                        mov rcx, rdi
00B36485  E8 5E 02 DC FF                  call 0x1408f66e8
00B3648A  33 C0                           xor eax, eax
00B3648C  48 8D 0D 35 B1 4E FF            lea rcx, [rip - 0xb14ecb]
00B36493  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00B36497  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00B3649B  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00B364A0  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00B364A4  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00B364A9  4D 8B CD                        mov r9, r13
00B364AC  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00B364B1  44 8D 40 06                     lea r8d, [rax + 6]
00B364B5  49 8B D6                        mov rdx, r14
00B364B8  48 8B CF                        mov rcx, rdi
00B364BB  E8 28 02 DC FF                  call 0x1408f66e8
00B364C0  33 C0                           xor eax, eax
00B364C2  48 8D 0D C7 AA 4E FF            lea rcx, [rip - 0xb15539]
00B364C9  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00B364CD  4D 8B CD                        mov r9, r13
00B364D0  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00B364D4  49 8B D6                        mov rdx, r14
00B364D7  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00B364DC  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00B364E0  44 8D 40 06                     lea r8d, [rax + 6]
00B364E4  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00B364E9  48 8B CF                        mov rcx, rdi
00B364EC  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00B364F1  E8 F2 01 DC FF                  call 0x1408f66e8
00B364F6  33 C0                           xor eax, eax
00B364F8  48 8D 0D 59 C0 4E FF            lea rcx, [rip - 0xb13fa7]
00B364FF  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00B36503  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00B36507  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00B3650C  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00B36510  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00B36515  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00B3651A  4D 8B CD                        mov r9, r13
00B3651D  41 B8 06 00 00 00               mov r8d, 6
00B36523  49 8B D6                        mov rdx, r14
00B36526  48 8B CF                        mov rcx, rdi
00B36529  E8 BA 01 DC FF                  call 0x1408f66e8
00B3652E  33 C0                           xor eax, eax
00B36530  48 8D 0D 49 BC 4E FF            lea rcx, [rip - 0xb143b7]
00B36537  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00B3653B  49 8B D6                        mov rdx, r14
00B3653E  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00B36542  4D 8B CD                        mov r9, r13
00B36545  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00B3654A  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00B3654E  44 8D 40 06                     lea r8d, [rax + 6]
00B36552  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00B36557  48 8B CF                        mov rcx, rdi
00B3655A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00B3655F  E8 84 01 DC FF                  call 0x1408f66e8
00B36564  33 C0                           xor eax, eax
00B36566  48 8D 0D 43 BE 4E FF            lea rcx, [rip - 0xb141bd]
00B3656D  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00B36571  4D 8B CD                        mov r9, r13
00B36574  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00B36578  49 8B D6                        mov rdx, r14
00B3657B  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00B36580  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00B36584  44 8D 40 06                     lea r8d, [rax + 6]
00B36588  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00B3658D  48 8B CF                        mov rcx, rdi
00B36590  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00B36595  E8 4E 01 DC FF                  call 0x1408f66e8
00B3659A  33 C0                           xor eax, eax
00B3659C  48 8D 0D 6D BF 4E FF            lea rcx, [rip - 0xb14093]
00B365A3  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00B365A7  4D 8B CD                        mov r9, r13
00B365AA  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00B365AE  49 8B D6                        mov rdx, r14
00B365B1  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00B365B6  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00B365BA  44 8D 40 06                     lea r8d, [rax + 6]
00B365BE  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00B365C3  48 8B CF                        mov rcx, rdi
00B365C6  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00B365CB  E8 18 01 DC FF                  call 0x1408f66e8
00B365D0  33 D2                           xor edx, edx
00B365D2  FF 45 F0                        inc dword ptr [rbp - 0x10]
00B365D5  FF 45 08                        inc dword ptr [rbp + 8]
00B365D8  8B 45 90                        mov eax, dword ptr [rbp - 0x70]
00B365DB  E9 E3 3D ED FF                  jmp 0x140a0a3c3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00B34E9C(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, unsigned int a13, __int64 a14)
{
    __int64 result;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned int v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned int v_stack_p50;
    unsigned __int64 v_stack_p60;
    unsigned __int8 v_stack_p64;
    unsigned __int64 v_stack_p65;
    unsigned __int64 v_stack_p68;
    unsigned __int8 v_stack_p6C;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;

    v_stack_p50 = (unsigned int)(a2);
    v_stack_p48 = a13;
    v_stack_p40 = (unsigned int)(v_rbx);
    v_stack_p38 = result;
    v_stack_p30 = v_rbp - 120;
    v_stack_p28 = v_rip - 11613063;
    v_stack_p20 = a2;
    result = PnpGetObjectProperty(v_rdi, v_rsi, 1, v_r15);
    if (a13 <= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rbp - 112))))) goto loc_00B34F0C;
    a2 = 0;
    result = ExFreePoolWithTag(a14, a2, 1, v_r15);
loc_00B34F0C:
}
```

## 5. (Beta) C Style

```c
int64_t sub_00B34E9C(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, uint64_t Arg10, uint64_t Arg11, uint64_t Arg12, uint32_t Arg13, int64_t Arg14)
{
    int64_t result;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint32_t v_stack_p40;
    uint64_t v_stack_p48;
    uint32_t v_stack_p50;
    uint64_t v_stack_p60;
    uint8_t v_stack_p64;
    uint64_t v_stack_p65;
    uint64_t v_stack_p68;
    uint8_t v_stack_p6C;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;

    v_stack_p50 = (uint32_t)(Arg2);
    v_stack_p48 = Arg13;
    v_stack_p40 = (uint32_t)(local_rbx);
    v_stack_p38 = result;
    v_stack_p30 = local_rbp - 120;
    v_stack_p28 = v_rip - 11613063;
    v_stack_p20 = Arg2;
    result = PnpGetObjectProperty(local_rdi, local_rsi, 1, local_r15);
    if (Arg13 <= ((uint32_t)((uint32_t)(*(uint32_t *)(local_rbp - 0x70))))) goto loc_00B34F0C;
    Arg2 = 0;
    result = ExFreePoolWithTag(Arg14, Arg2, 1, local_r15);
loc_00B34F0C:
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B34E9C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
