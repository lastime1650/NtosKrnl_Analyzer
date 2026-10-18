# sub_00B336B0

- RVA: `0x00B336B0`–`0x00B33DCD` (길이 `1,821` bytes)
- VA: `0x0000000140B336B0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A832C`
- 디코드: `470`개 명령, `1,821/1,821` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **55**; 고유 호출 대상: **12**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00B33729` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00B33738` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00B33744` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00B3375F` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00B33777` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00B3379B` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00B337B7` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00B337D3` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00B33816` → [PnpProcessRelation](../A0/PnpProcessRelation_function_00A04A4C.md) (function, `0x00A04A4C`)
- `0x00B33821` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00B33848` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00B3385A` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00B3386E` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00B3387F` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00B338A1` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00B338B0` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00B338BC` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00B338D7` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00B338EF` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00B33913` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00B3392F` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00B3394B` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00B33953` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00B33980` → [PipIsDeviceInDeviceObjectList](../A0/PipIsDeviceInDeviceObjectList_function_00A070D0.md) (function, `0x00A070D0`)
- `0x00B33996` → [IopRemoveRelationFromList](../73/IopRemoveRelationFromList_function_0073DBB8.md) (function, `0x0073DBB8`)
- `0x00B339A1` → [IopCancelPendingEject](../73/IopCancelPendingEject_function_0073DBF4.md) (function, `0x0073DBF4`)
- `0x00B339B0` → [IopMergeRelationLists](../73/IopMergeRelationLists_function_0073DA50.md) (function, `0x0073DA50`)
- `0x00B339D3` → [IopAddRelationToList](../A0/IopAddRelationToList_function_00A04D04.md) (function, `0x00A04D04`)
- `0x00B339F7` → [IopRemoveRelationFromList](../73/IopRemoveRelationFromList_function_0073DBB8.md) (function, `0x0073DBB8`)
- `0x00B33A07` → [PipClearDevNodeFlags](../8F/PipClearDevNodeFlags_function_008F9F54.md) (function, `0x008F9F54`)
- `0x00B33A23` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00B33A3E` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00B33A56` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00B33A6B` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00B33A9A` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00B33AAB` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00B33AB8` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00B33AF7` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00B33B23` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00B33B80` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00B33BB4` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00B33BCE` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00B33BF1` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00B33C12` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00B33C2D` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00B33C41` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00B33C73` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00B33C84` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00B33C91` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00B33CD0` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00B33CFC` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00B33D59` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00B33D85` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00B33DA0` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00B33DBE` → [RtlCopyUnicodeString](../../text/3F/RtlCopyUnicodeString_function_003FEF30.md) (function, `0x003FEF30`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00B3395E` → RVA `0x00F8C450` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **47**
  - `0x00B33729` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00B33738` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00B33744` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00B3375F` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00B33777` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00B3379B` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00B337B7` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00B337D3` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x00B33821` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00B33848` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00B3385A` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00B3386E` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00B3387F` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00B338A1` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00B338B0` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00B338BC` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00B338D7` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00B338EF` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00B33913` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00B3392F` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00B3394B` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x00B33953` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00B33A23` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00B33A3E` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00B33A56` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00B33A6B` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00B33A9A` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00B33AAB` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00B33AB8` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00B33AF7` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00B33B23` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00B33B80` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00B33BB4` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00B33BCE` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x00B33BF1` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00B33C12` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00B33C2D` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00B33C41` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00B33C73` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00B33C84` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00B33C91` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00B33CD0` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00B33CFC` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00B33D59` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00B33D85` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00B33DA0` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x00B33DBE` → [RtlCopyUnicodeString](../../text/3F/RtlCopyUnicodeString_function_003FEF30.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **9**
  - `0x00B336FC` → [PnpProcessRelation + 0x4E](../A0/PnpProcessRelation_function_00A04A4C.md) (`tail-transfer`)
  - `0x00B33707` → [PnpProcessRelation + 0x115](../A0/PnpProcessRelation_function_00A04A4C.md) (`tail-transfer`)
  - `0x00B3382E` → [PnpProcessRelation + 0x1FD](../A0/PnpProcessRelation_function_00A04A4C.md) (`tail-transfer`)
  - `0x00B33959` → [PnpProcessRelation + 0xF0](../A0/PnpProcessRelation_function_00A04A4C.md) (`tail-transfer`)
  - `0x00B339C0` → [PnpProcessRelation + 0x17F](../A0/PnpProcessRelation_function_00A04A4C.md) (`tail-transfer`)
  - `0x00B339D9` → [PnpProcessRelation + 0x17F](../A0/PnpProcessRelation_function_00A04A4C.md) (`tail-transfer`)
  - `0x00B33A0D` → [PnpProcessRelation + 0x17F](../A0/PnpProcessRelation_function_00A04A4C.md) (`tail-transfer`)
  - `0x00B33BDB` → [PnpProcessRelation + 0x17F](../A0/PnpProcessRelation_function_00A04A4C.md) (`tail-transfer`)
  - `0x00B33DC8` → [PnpProcessRelation + 0x115](../A0/PnpProcessRelation_function_00A04A4C.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B336B0  8B 89 2C 01 00 00               mov ecx, dword ptr [rcx + 0x12c]
00B336B6  8D 81 F0 FC FF FF               lea eax, [rcx - 0x310]
00B336BC  83 F8 01                        cmp eax, 1
00B336BF  0F 86 EA 06 00 00               jbe 0x140b33daf
00B336C5  81 F9 16 03 00 00               cmp ecx, 0x316
00B336CB  0F 84 DE 06 00 00               je 0x140b33daf
00B336D1  39 9F 90 02 00 00               cmp dword ptr [rdi + 0x290], ebx
00B336D7  0F 8F C9 06 00 00               jg 0x140b33da6
00B336DD  8D 81 ED FC FF FF               lea eax, [rcx - 0x313]
00B336E3  A9 FD FF FF FF                  test eax, 0xfffffffd
00B336E8  0F 84 B8 06 00 00               je 0x140b33da6
00B336EE  81 F9 0C 03 00 00               cmp ecx, 0x30c
00B336F4  74 0C                           je 0x140b33702
00B336F6  81 F9 0D 03 00 00               cmp ecx, 0x30d
00B336FC  0F 85 98 13 ED FF               jne 0x140a04a9a
00B33702  B8 10 00 00 C0                  mov eax, 0xc0000010
00B33707  E9 55 14 ED FF                  jmp 0x140a04b61
00B3370C  48 8B 86 38 01 00 00            mov rax, qword ptr [rsi + 0x138]
00B33713  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
00B33717  48 85 C9                        test rcx, rcx
00B3371A  0F 84 9C 00 00 00               je 0x140b337bc
00B33720  BA 88 03 00 00                  mov edx, 0x388
00B33725  48 8D 79 28                     lea rdi, [rcx + 0x28]
00B33729  E8 46 4C 8F FF                  call 0x140428374
00B3372E  66 39 1F                        cmp word ptr [rdi], bx
00B33731  74 16                           je 0x140b33749
00B33733  8B D5                           mov edx, ebp
00B33735  48 8B CF                        mov rcx, rdi
00B33738  E8 37 4C 8F FF                  call 0x140428374
00B3373D  0F B7 17                        movzx edx, word ptr [rdi]
00B33740  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
00B33744  E8 2B 4C 8F FF                  call 0x140428374
00B33749  48 8B 86 38 01 00 00            mov rax, qword ptr [rsi + 0x138]
00B33750  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
00B33754  48 83 C1 38                     add rcx, 0x38
00B33758  66 39 19                        cmp word ptr [rcx], bx
00B3375B  74 1F                           je 0x140b3377c
00B3375D  8B D5                           mov edx, ebp
00B3375F  E8 10 4C 8F FF                  call 0x140428374
00B33764  48 8B 86 38 01 00 00            mov rax, qword ptr [rsi + 0x138]
00B3376B  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
00B3376F  0F B7 51 38                     movzx edx, word ptr [rcx + 0x38]
00B33773  48 8B 49 40                     mov rcx, qword ptr [rcx + 0x40]
00B33777  E8 F8 4B 8F FF                  call 0x140428374
00B3377C  48 8B 86 38 01 00 00            mov rax, qword ptr [rsi + 0x138]
00B33783  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
00B33787  48 8B 41 10                     mov rax, qword ptr [rcx + 0x10]
00B3378B  48 85 C0                        test rax, rax
00B3378E  74 2C                           je 0x140b337bc
00B33790  48 8D 48 38                     lea rcx, [rax + 0x38]
00B33794  66 39 19                        cmp word ptr [rcx], bx
00B33797  74 23                           je 0x140b337bc
00B33799  8B D5                           mov edx, ebp
00B3379B  E8 D4 4B 8F FF                  call 0x140428374
00B337A0  48 8B 86 38 01 00 00            mov rax, qword ptr [rsi + 0x138]
00B337A7  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
00B337AB  48 8B 49 10                     mov rcx, qword ptr [rcx + 0x10]
00B337AF  0F B7 51 38                     movzx edx, word ptr [rcx + 0x38]
00B337B3  48 8B 49 40                     mov rcx, qword ptr [rcx + 0x40]
00B337B7  E8 B8 4B 8F FF                  call 0x140428374
00B337BC  41 B9 03 00 00 00               mov r9d, 3
00B337C2  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00B337C7  4C 8B C6                        mov r8, rsi
00B337CA  B9 CA 00 00 00                  mov ecx, 0xca
00B337CF  41 8D 51 08                     lea edx, [r9 + 8]
00B337D3  E8 88 9E 9C FF                  call 0x1404fd660
00B337D8  CC                              int3
00B337D9  44 3B 39                        cmp r15d, dword ptr [rcx]
00B337DC  0F 83 6F 01 00 00               jae 0x140b33951
00B337E2  41 8B C7                        mov eax, r15d
00B337E5  48 8B 74 C1 08                  mov rsi, qword ptr [rcx + rax*8 + 8]
00B337EA  48 8B 8E 38 01 00 00            mov rcx, qword ptr [rsi + 0x138]
00B337F1  8B 41 20                        mov eax, dword ptr [rcx + 0x20]
00B337F4  40 84 C5                        test bpl, al
00B337F7  75 48                           jne 0x140b33841
00B337F9  48 8B 49 28                     mov rcx, qword ptr [rcx + 0x28]
00B337FD  48 85 C9                        test rcx, rcx
00B33800  74 3F                           je 0x140b33841
00B33802  48 39 59 10                     cmp qword ptr [rcx + 0x10], rbx
00B33806  74 39                           je 0x140b33841
00B33808  4D 8B CE                        mov r9, r14
00B3380B  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00B33810  45 33 C0                        xor r8d, r8d
00B33813  41 8B D5                        mov edx, r13d
00B33816  E8 31 12 ED FF                  call 0x140a04a4c
00B3381B  48 8B CE                        mov rcx, rsi
00B3381E  44 8B E0                        mov r12d, eax
00B33821  E8 2A 5B 7C FF                  call 0x1402f9350
00B33826  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
00B3382B  45 85 E4                        test r12d, r12d
00B3382E  0F 88 15 14 ED FF               js 0x140a04c49
00B33834  4C 8B A4 24 90 00 00 00         mov r12, qword ptr [rsp + 0x90]
00B3383C  41 FF C7                        inc r15d
00B3383F  EB 98                           jmp 0x140b337d9
00B33841  0F B7 56 02                     movzx edx, word ptr [rsi + 2]
00B33845  48 8B CE                        mov rcx, rsi
00B33848  E8 27 4B 8F FF                  call 0x140428374
00B3384D  48 8B 4E 08                     mov rcx, qword ptr [rsi + 8]
00B33851  48 85 C9                        test rcx, rcx
00B33854  74 2E                           je 0x140b33884
00B33856  0F BF 51 02                     movsx edx, word ptr [rcx + 2]
00B3385A  E8 15 4B 8F FF                  call 0x140428374
00B3385F  48 8B 4E 08                     mov rcx, qword ptr [rsi + 8]
00B33863  48 83 C1 38                     add rcx, 0x38
00B33867  66 39 19                        cmp word ptr [rcx], bx
00B3386A  74 18                           je 0x140b33884
00B3386C  8B D5                           mov edx, ebp
00B3386E  E8 01 4B 8F FF                  call 0x140428374
00B33873  48 8B 4E 08                     mov rcx, qword ptr [rsi + 8]
00B33877  0F B7 51 38                     movzx edx, word ptr [rcx + 0x38]
00B3387B  48 8B 49 40                     mov rcx, qword ptr [rcx + 0x40]
00B3387F  E8 F0 4A 8F FF                  call 0x140428374
00B33884  48 8B 86 38 01 00 00            mov rax, qword ptr [rsi + 0x138]
00B3388B  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
00B3388F  48 85 C9                        test rcx, rcx
00B33892  0F 84 9C 00 00 00               je 0x140b33934
00B33898  BA 88 03 00 00                  mov edx, 0x388
00B3389D  48 8D 79 28                     lea rdi, [rcx + 0x28]
00B338A1  E8 CE 4A 8F FF                  call 0x140428374
00B338A6  66 39 1F                        cmp word ptr [rdi], bx
00B338A9  74 16                           je 0x140b338c1
00B338AB  8B D5                           mov edx, ebp
00B338AD  48 8B CF                        mov rcx, rdi
00B338B0  E8 BF 4A 8F FF                  call 0x140428374
00B338B5  0F B7 17                        movzx edx, word ptr [rdi]
00B338B8  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
00B338BC  E8 B3 4A 8F FF                  call 0x140428374
00B338C1  48 8B 86 38 01 00 00            mov rax, qword ptr [rsi + 0x138]
00B338C8  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
00B338CC  48 83 C1 38                     add rcx, 0x38
00B338D0  66 39 19                        cmp word ptr [rcx], bx
00B338D3  74 1F                           je 0x140b338f4
00B338D5  8B D5                           mov edx, ebp
00B338D7  E8 98 4A 8F FF                  call 0x140428374
00B338DC  48 8B 86 38 01 00 00            mov rax, qword ptr [rsi + 0x138]
00B338E3  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
00B338E7  0F B7 51 38                     movzx edx, word ptr [rcx + 0x38]
00B338EB  48 8B 49 40                     mov rcx, qword ptr [rcx + 0x40]
00B338EF  E8 80 4A 8F FF                  call 0x140428374
00B338F4  48 8B 86 38 01 00 00            mov rax, qword ptr [rsi + 0x138]
00B338FB  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
00B338FF  48 8B 41 10                     mov rax, qword ptr [rcx + 0x10]
00B33903  48 85 C0                        test rax, rax
00B33906  74 2C                           je 0x140b33934
00B33908  48 8D 48 38                     lea rcx, [rax + 0x38]
00B3390C  66 39 19                        cmp word ptr [rcx], bx
00B3390F  74 23                           je 0x140b33934
00B33911  8B D5                           mov edx, ebp
00B33913  E8 5C 4A 8F FF                  call 0x140428374
00B33918  48 8B 86 38 01 00 00            mov rax, qword ptr [rsi + 0x138]
00B3391F  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
00B33923  48 8B 49 10                     mov rcx, qword ptr [rcx + 0x10]
00B33927  0F B7 51 38                     movzx edx, word ptr [rcx + 0x38]
00B3392B  48 8B 49 40                     mov rcx, qword ptr [rcx + 0x40]
00B3392F  E8 40 4A 8F FF                  call 0x140428374
00B33934  41 B9 01 00 00 00               mov r9d, 1
00B3393A  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00B3393F  4C 8B C6                        mov r8, rsi
00B33942  B9 CA 00 00 00                  mov ecx, 0xca
00B33947  41 8D 51 0A                     lea edx, [r9 + 0xa]
00B3394B  E8 10 9D 9C FF                  call 0x1404fd660
00B33950  CC                              int3
00B33951  33 D2                           xor edx, edx
00B33953  E8 18 EF 04 00                  call 0x140b82870
00B33958  90                              nop
00B33959  E9 DE 11 ED FF                  jmp 0x140a04b3c
00B3395E  48 8D 05 EB 8A 45 00            lea rax, [rip + 0x458aeb]
00B33965  4C 3B F0                        cmp r14, rax
00B33968  0F 84 A4 00 00 00               je 0x140b33a12
00B3396E  49 8B 4E 40                     mov rcx, qword ptr [r14 + 0x40]
00B33972  48 85 C9                        test rcx, rcx
00B33975  74 67                           je 0x140b339de
00B33977  48 8B 16                        mov rdx, qword ptr [rsi]
00B3397A  45 33 C0                        xor r8d, r8d
00B3397D  48 8B 09                        mov rcx, qword ptr [rcx]
00B33980  E8 4B 37 ED FF                  call 0x140a070d0
00B33985  84 C0                           test al, al
00B33987  74 55                           je 0x140b339de
00B33989  41 83 FD 04                     cmp r13d, 4
00B3398D  75 57                           jne 0x140b339e6
00B3398F  48 8B 57 20                     mov rdx, qword ptr [rdi + 0x20]
00B33993  49 8B CC                        mov rcx, r12
00B33996  E8 1D A2 C0 FF                  call 0x14073dbb8
00B3399B  49 8B CE                        mov rcx, r14
00B3399E  44 8B F8                        mov r15d, eax
00B339A1  E8 4E A2 C0 FF                  call 0x14073dbf4
00B339A6  49 8B 56 40                     mov rdx, qword ptr [r14 + 0x40]
00B339AA  45 33 C0                        xor r8d, r8d
00B339AD  49 8B CC                        mov rcx, r12
00B339B0  E8 9B A0 C0 FF                  call 0x14073da50
00B339B5  41 8D 6D FE                     lea ebp, [r13 - 2]
00B339B9  39 AC 24 80 00 00 00            cmp dword ptr [rsp + 0x80], ebp
00B339C0  0F 85 05 12 ED FF               jne 0x140a04bcb
00B339C6  48 8B 57 20                     mov rdx, qword ptr [rdi + 0x20]
00B339CA  45 33 C9                        xor r9d, r9d
00B339CD  44 8B C5                        mov r8d, ebp
00B339D0  49 8B CC                        mov rcx, r12
00B339D3  E8 2C 13 ED FF                  call 0x140a04d04
00B339D8  90                              nop
00B339D9  E9 ED 11 ED FF                  jmp 0x140a04bcb
00B339DE  4D 8B 36                        mov r14, qword ptr [r14]
00B339E1  E9 78 FF FF FF                  jmp 0x140b3395e
00B339E6  45 85 ED                        test r13d, r13d
00B339E9  0F 84 D4 03 00 00               je 0x140b33dc3
00B339EF  48 8B 57 20                     mov rdx, qword ptr [rdi + 0x20]
00B339F3  49 8B 4E 40                     mov rcx, qword ptr [r14 + 0x40]
00B339F7  E8 BC A1 C0 FF                  call 0x14073dbb8
00B339FC  BA 00 00 08 00                  mov edx, 0x80000
00B33A01  48 8B CF                        mov rcx, rdi
00B33A04  44 8B F8                        mov r15d, eax
00B33A07  E8 48 65 DC FF                  call 0x1408f9f54
00B33A0C  90                              nop
00B33A0D  E9 B9 11 ED FF                  jmp 0x140a04bcb
00B33A12  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
00B33A16  48 85 C9                        test rcx, rcx
00B33A19  0F 84 9A 01 00 00               je 0x140b33bb9
00B33A1F  0F B7 51 02                     movzx edx, word ptr [rcx + 2]
00B33A23  E8 4C 49 8F FF                  call 0x140428374
00B33A28  48 8B 47 20                     mov rax, qword ptr [rdi + 0x20]
00B33A2C  BD 02 00 00 00                  mov ebp, 2
00B33A31  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
00B33A35  48 85 C9                        test rcx, rcx
00B33A38  74 36                           je 0x140b33a70
00B33A3A  0F BF 51 02                     movsx edx, word ptr [rcx + 2]
00B33A3E  E8 31 49 8F FF                  call 0x140428374
00B33A43  48 8B 47 20                     mov rax, qword ptr [rdi + 0x20]
00B33A47  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
00B33A4B  48 83 C1 38                     add rcx, 0x38
00B33A4F  66 39 19                        cmp word ptr [rcx], bx
00B33A52  74 1C                           je 0x140b33a70
00B33A54  8B D5                           mov edx, ebp
00B33A56  E8 19 49 8F FF                  call 0x140428374
00B33A5B  48 8B 47 20                     mov rax, qword ptr [rdi + 0x20]
00B33A5F  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
00B33A63  0F B7 51 38                     movzx edx, word ptr [rcx + 0x38]
00B33A67  48 8B 49 40                     mov rcx, qword ptr [rcx + 0x40]
00B33A6B  E8 04 49 8F FF                  call 0x140428374
00B33A70  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
00B33A74  48 85 C9                        test rcx, rcx
00B33A77  0F 84 3C 01 00 00               je 0x140b33bb9
00B33A7D  48 8B 81 38 01 00 00            mov rax, qword ptr [rcx + 0x138]
00B33A84  48 39 58 28                     cmp qword ptr [rax + 0x28], rbx
00B33A88  0F 84 2B 01 00 00               je 0x140b33bb9
00B33A8E  48 8B 70 28                     mov rsi, qword ptr [rax + 0x28]
00B33A92  BA 88 03 00 00                  mov edx, 0x388
00B33A97  48 8B CE                        mov rcx, rsi
00B33A9A  E8 D5 48 8F FF                  call 0x140428374
00B33A9F  66 39 5E 28                     cmp word ptr [rsi + 0x28], bx
00B33AA3  74 18                           je 0x140b33abd
00B33AA5  8B D5                           mov edx, ebp
00B33AA7  48 8D 4E 28                     lea rcx, [rsi + 0x28]
00B33AAB  E8 C4 48 8F FF                  call 0x140428374
00B33AB0  0F B7 56 28                     movzx edx, word ptr [rsi + 0x28]
00B33AB4  48 8B 4E 30                     mov rcx, qword ptr [rsi + 0x30]
00B33AB8  E8 B7 48 8F FF                  call 0x140428374
00B33ABD  48 8B 57 20                     mov rdx, qword ptr [rdi + 0x20]
00B33AC1  48 8D 8A 38 01 00 00            lea rcx, [rdx + 0x138]
00B33AC8  48 85 D2                        test rdx, rdx
00B33ACB  74 09                           je 0x140b33ad6
00B33ACD  48 8B 01                        mov rax, qword ptr [rcx]
00B33AD0  4C 8B 40 28                     mov r8, qword ptr [rax + 0x28]
00B33AD4  EB 03                           jmp 0x140b33ad9
00B33AD6  4C 8B C3                        mov r8, rbx
00B33AD9  66 41 39 58 38                  cmp word ptr [r8 + 0x38], bx
00B33ADE  74 48                           je 0x140b33b28
00B33AE0  48 85 D2                        test rdx, rdx
00B33AE3  74 09                           je 0x140b33aee
00B33AE5  48 8B 01                        mov rax, qword ptr [rcx]
00B33AE8  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
00B33AEC  EB 03                           jmp 0x140b33af1
00B33AEE  48 8B CB                        mov rcx, rbx
00B33AF1  48 83 C1 38                     add rcx, 0x38
00B33AF5  8B D5                           mov edx, ebp
00B33AF7  E8 78 48 8F FF                  call 0x140428374
00B33AFC  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
00B33B00  48 85 C9                        test rcx, rcx
00B33B03  74 10                           je 0x140b33b15
00B33B05  48 8B 81 38 01 00 00            mov rax, qword ptr [rcx + 0x138]
00B33B0C  4C 8B 40 28                     mov r8, qword ptr [rax + 0x28]
00B33B10  49 8B C8                        mov rcx, r8
00B33B13  EB 06                           jmp 0x140b33b1b
00B33B15  4C 8B C3                        mov r8, rbx
00B33B18  48 8B CB                        mov rcx, rbx
00B33B1B  0F B7 51 38                     movzx edx, word ptr [rcx + 0x38]
00B33B1F  49 8B 48 40                     mov rcx, qword ptr [r8 + 0x40]
00B33B23  E8 4C 48 8F FF                  call 0x140428374
00B33B28  48 8B 57 20                     mov rdx, qword ptr [rdi + 0x20]
00B33B2C  48 8D 8A 38 01 00 00            lea rcx, [rdx + 0x138]
00B33B33  48 85 D2                        test rdx, rdx
00B33B36  74 09                           je 0x140b33b41
00B33B38  48 8B 01                        mov rax, qword ptr [rcx]
00B33B3B  4C 8B 40 28                     mov r8, qword ptr [rax + 0x28]
00B33B3F  EB 03                           jmp 0x140b33b44
00B33B41  4C 8B C3                        mov r8, rbx
00B33B44  49 39 58 10                     cmp qword ptr [r8 + 0x10], rbx
00B33B48  74 6F                           je 0x140b33bb9
00B33B4A  48 85 D2                        test rdx, rdx
00B33B4D  74 09                           je 0x140b33b58
00B33B4F  48 8B 01                        mov rax, qword ptr [rcx]
00B33B52  48 8B 40 28                     mov rax, qword ptr [rax + 0x28]
00B33B56  EB 03                           jmp 0x140b33b5b
00B33B58  48 8B C3                        mov rax, rbx
00B33B5B  48 8B 40 10                     mov rax, qword ptr [rax + 0x10]
00B33B5F  66 39 58 38                     cmp word ptr [rax + 0x38], bx
00B33B63  74 54                           je 0x140b33bb9
00B33B65  48 85 D2                        test rdx, rdx
00B33B68  74 09                           je 0x140b33b73
00B33B6A  48 8B 01                        mov rax, qword ptr [rcx]
00B33B6D  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
00B33B71  EB 03                           jmp 0x140b33b76
00B33B73  48 8B CB                        mov rcx, rbx
00B33B76  48 8B 49 10                     mov rcx, qword ptr [rcx + 0x10]
00B33B7A  8B D5                           mov edx, ebp
00B33B7C  48 83 C1 38                     add rcx, 0x38
00B33B80  E8 EF 47 8F FF                  call 0x140428374
00B33B85  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
00B33B89  48 85 C9                        test rcx, rcx
00B33B8C  74 10                           je 0x140b33b9e
00B33B8E  48 8B 81 38 01 00 00            mov rax, qword ptr [rcx + 0x138]
00B33B95  4C 8B 40 28                     mov r8, qword ptr [rax + 0x28]
00B33B99  49 8B C0                        mov rax, r8
00B33B9C  EB 06                           jmp 0x140b33ba4
00B33B9E  4C 8B C3                        mov r8, rbx
00B33BA1  48 8B C3                        mov rax, rbx
00B33BA4  48 8B 40 10                     mov rax, qword ptr [rax + 0x10]
00B33BA8  49 8B 48 10                     mov rcx, qword ptr [r8 + 0x10]
00B33BAC  0F B7 50 38                     movzx edx, word ptr [rax + 0x38]
00B33BB0  48 8B 49 40                     mov rcx, qword ptr [rcx + 0x40]
00B33BB4  E8 BB 47 8F FF                  call 0x140428374
00B33BB9  4C 8B 47 20                     mov r8, qword ptr [rdi + 0x20]
00B33BBD  45 33 C9                        xor r9d, r9d
00B33BC0  B9 CA 00 00 00                  mov ecx, 0xca
00B33BC5  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00B33BCA  41 8D 51 06                     lea edx, [r9 + 6]
00B33BCE  E8 8D 9A 9C FF                  call 0x1404fd660
00B33BD3  CC                              int3
00B33BD4  41 81 FF 9A 00 00 C0            cmp r15d, 0xc000009a
00B33BDB  0F 84 EA 0F ED FF               je 0x140a04bcb
00B33BE1  48 8B 0E                        mov rcx, qword ptr [rsi]
00B33BE4  48 85 C9                        test rcx, rcx
00B33BE7  0F 84 9D 01 00 00               je 0x140b33d8a
00B33BED  0F B7 51 02                     movzx edx, word ptr [rcx + 2]
00B33BF1  E8 7E 47 8F FF                  call 0x140428374
00B33BF6  48 8B 06                        mov rax, qword ptr [rsi]
00B33BF9  48 8B CE                        mov rcx, rsi
00B33BFC  BD 02 00 00 00                  mov ebp, 2
00B33C01  4C 8B 40 08                     mov r8, qword ptr [rax + 8]
00B33C05  4D 85 C0                        test r8, r8
00B33C08  74 40                           je 0x140b33c4a
00B33C0A  41 0F BF 50 02                  movsx edx, word ptr [r8 + 2]
00B33C0F  49 8B C8                        mov rcx, r8
00B33C12  E8 5D 47 8F FF                  call 0x140428374
00B33C17  48 8B 06                        mov rax, qword ptr [rsi]
00B33C1A  48 8B CE                        mov rcx, rsi
00B33C1D  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00B33C21  66 39 58 38                     cmp word ptr [rax + 0x38], bx
00B33C25  74 23                           je 0x140b33c4a
00B33C27  8B D5                           mov edx, ebp
00B33C29  48 8D 48 38                     lea rcx, [rax + 0x38]
00B33C2D  E8 42 47 8F FF                  call 0x140428374
00B33C32  48 8B 06                        mov rax, qword ptr [rsi]
00B33C35  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
00B33C39  0F B7 51 38                     movzx edx, word ptr [rcx + 0x38]
00B33C3D  48 8B 49 40                     mov rcx, qword ptr [rcx + 0x40]
00B33C41  E8 2E 47 8F FF                  call 0x140428374
00B33C46  48 8D 4F 20                     lea rcx, [rdi + 0x20]
00B33C4A  48 8B 09                        mov rcx, qword ptr [rcx]
00B33C4D  48 85 C9                        test rcx, rcx
00B33C50  0F 84 34 01 00 00               je 0x140b33d8a
00B33C56  48 8B 81 38 01 00 00            mov rax, qword ptr [rcx + 0x138]
00B33C5D  48 39 58 28                     cmp qword ptr [rax + 0x28], rbx
00B33C61  0F 84 23 01 00 00               je 0x140b33d8a
00B33C67  48 8B 70 28                     mov rsi, qword ptr [rax + 0x28]
00B33C6B  BA 88 03 00 00                  mov edx, 0x388
00B33C70  48 8B CE                        mov rcx, rsi
00B33C73  E8 FC 46 8F FF                  call 0x140428374
00B33C78  66 39 5E 28                     cmp word ptr [rsi + 0x28], bx
00B33C7C  74 18                           je 0x140b33c96
00B33C7E  8B D5                           mov edx, ebp
00B33C80  48 8D 4E 28                     lea rcx, [rsi + 0x28]
00B33C84  E8 EB 46 8F FF                  call 0x140428374
00B33C89  0F B7 56 28                     movzx edx, word ptr [rsi + 0x28]
00B33C8D  48 8B 4E 30                     mov rcx, qword ptr [rsi + 0x30]
00B33C91  E8 DE 46 8F FF                  call 0x140428374
00B33C96  48 8B 57 20                     mov rdx, qword ptr [rdi + 0x20]
00B33C9A  48 8D 8A 38 01 00 00            lea rcx, [rdx + 0x138]
00B33CA1  48 85 D2                        test rdx, rdx
00B33CA4  74 09                           je 0x140b33caf
00B33CA6  48 8B 01                        mov rax, qword ptr [rcx]
00B33CA9  4C 8B 40 28                     mov r8, qword ptr [rax + 0x28]
00B33CAD  EB 03                           jmp 0x140b33cb2
00B33CAF  4C 8B C3                        mov r8, rbx
00B33CB2  66 41 39 58 38                  cmp word ptr [r8 + 0x38], bx
00B33CB7  74 48                           je 0x140b33d01
00B33CB9  48 85 D2                        test rdx, rdx
00B33CBC  74 09                           je 0x140b33cc7
00B33CBE  48 8B 01                        mov rax, qword ptr [rcx]
00B33CC1  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
00B33CC5  EB 03                           jmp 0x140b33cca
00B33CC7  48 8B CB                        mov rcx, rbx
00B33CCA  48 83 C1 38                     add rcx, 0x38
00B33CCE  8B D5                           mov edx, ebp
00B33CD0  E8 9F 46 8F FF                  call 0x140428374
00B33CD5  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
00B33CD9  48 85 C9                        test rcx, rcx
00B33CDC  74 10                           je 0x140b33cee
00B33CDE  48 8B 81 38 01 00 00            mov rax, qword ptr [rcx + 0x138]
00B33CE5  4C 8B 40 28                     mov r8, qword ptr [rax + 0x28]
00B33CE9  49 8B C8                        mov rcx, r8
00B33CEC  EB 06                           jmp 0x140b33cf4
00B33CEE  4C 8B C3                        mov r8, rbx
00B33CF1  48 8B CB                        mov rcx, rbx
00B33CF4  0F B7 51 38                     movzx edx, word ptr [rcx + 0x38]
00B33CF8  49 8B 48 40                     mov rcx, qword ptr [r8 + 0x40]
00B33CFC  E8 73 46 8F FF                  call 0x140428374
00B33D01  48 8B 57 20                     mov rdx, qword ptr [rdi + 0x20]
00B33D05  48 8D 8A 38 01 00 00            lea rcx, [rdx + 0x138]
00B33D0C  48 85 D2                        test rdx, rdx
00B33D0F  74 09                           je 0x140b33d1a
00B33D11  48 8B 01                        mov rax, qword ptr [rcx]
00B33D14  4C 8B 40 28                     mov r8, qword ptr [rax + 0x28]
00B33D18  EB 03                           jmp 0x140b33d1d
00B33D1A  4C 8B C3                        mov r8, rbx
00B33D1D  49 39 58 10                     cmp qword ptr [r8 + 0x10], rbx
00B33D21  74 67                           je 0x140b33d8a
00B33D23  48 85 D2                        test rdx, rdx
00B33D26  74 09                           je 0x140b33d31
00B33D28  48 8B 01                        mov rax, qword ptr [rcx]
00B33D2B  48 8B 40 28                     mov rax, qword ptr [rax + 0x28]
00B33D2F  EB 03                           jmp 0x140b33d34
00B33D31  48 8B C3                        mov rax, rbx
00B33D34  48 8B 40 10                     mov rax, qword ptr [rax + 0x10]
00B33D38  66 39 58 38                     cmp word ptr [rax + 0x38], bx
00B33D3C  74 4C                           je 0x140b33d8a
00B33D3E  48 85 D2                        test rdx, rdx
00B33D41  74 09                           je 0x140b33d4c
00B33D43  48 8B 01                        mov rax, qword ptr [rcx]
00B33D46  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
00B33D4A  EB 03                           jmp 0x140b33d4f
00B33D4C  48 8B CB                        mov rcx, rbx
00B33D4F  48 8B 49 10                     mov rcx, qword ptr [rcx + 0x10]
00B33D53  8B D5                           mov edx, ebp
00B33D55  48 83 C1 38                     add rcx, 0x38
00B33D59  E8 16 46 8F FF                  call 0x140428374
00B33D5E  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
00B33D62  48 85 C9                        test rcx, rcx
00B33D65  74 0B                           je 0x140b33d72
00B33D67  48 8B 81 38 01 00 00            mov rax, qword ptr [rcx + 0x138]
00B33D6E  48 8B 58 28                     mov rbx, qword ptr [rax + 0x28]
00B33D72  48 8B 4B 10                     mov rcx, qword ptr [rbx + 0x10]
00B33D76  48 8B C3                        mov rax, rbx
00B33D79  48 8B 43 10                     mov rax, qword ptr [rbx + 0x10]
00B33D7D  48 8B 49 40                     mov rcx, qword ptr [rcx + 0x40]
00B33D81  0F B7 50 38                     movzx edx, word ptr [rax + 0x38]
00B33D85  E8 EA 45 8F FF                  call 0x140428374
00B33D8A  4C 8B 47 20                     mov r8, qword ptr [rdi + 0x20]
00B33D8E  4D 8B CC                        mov r9, r12
00B33D91  BA 07 00 00 00                  mov edx, 7
00B33D96  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00B33D9B  B9 CA 00 00 00                  mov ecx, 0xca
00B33DA0  E8 BB 98 9C FF                  call 0x1404fd660
00B33DA5  CC                              int3
00B33DA6  41 C7 01 05 00 00 00            mov dword ptr [r9], 5
00B33DAD  EB 07                           jmp 0x140b33db6
00B33DAF  41 C7 01 0D 00 00 00            mov dword ptr [r9], 0xd
00B33DB6  48 8D 57 28                     lea rdx, [rdi + 0x28]
00B33DBA  49 8D 49 08                     lea rcx, [r9 + 8]
00B33DBE  E8 6D B1 8C FF                  call 0x1403fef30
00B33DC3  B8 01 00 00 C0                  mov eax, 0xc0000001
00B33DC8  E9 94 0D ED FF                  jmp 0x140a04b61
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00B336B0(__int64 a1)
{
    __int64 result;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p30;
    unsigned int v_stack_p80;
    unsigned __int64 v_stack_p90;

    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 300)) - 784)) <= 1) goto loc_00B33DAF;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 300)))) == 790) goto loc_00B33DAF;
    if ((*(unsigned int *)(v_rdi + 656)) > ((unsigned int)(v_rbx))) goto loc_00B33DA6;
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 300)) - 787)) & (0xFFFFFFFDULL)) == 0) goto loc_00B33DA6;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 300)))) == 780) goto loc_00B33702;
loc_00B33702:
loc_00B33DA6:
    *(unsigned int *)(a4) = 5;
    goto loc_00B33DB6;
loc_00B33DAF:
    *(unsigned int *)(a4) = 13;
loc_00B33DB6:
    result = RtlCopyUnicodeString(a4 + 8, v_rdi + 40, a3, a4);
loc_00B33DC3:
}
```

## 5. (Beta) C Style

```c
int64_t sub_00B336B0(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    uint64_t v_stack_p20;
    uint64_t v_stack_p30;
    uint32_t v_stack_p80;
    uint64_t v_stack_p90;

    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x12C)) - 784)) <= 1) goto loc_00B33DAF;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x12C)))) == 790) goto loc_00B33DAF;
    if ((*(uint32_t *)(local_rdi + 0x290)) > ((uint32_t)(local_rbx))) goto loc_00B33DA6;
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x12C)) - 787)) & (0xFFFFFFFDULL)) == 0) goto loc_00B33DA6;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x12C)))) == 780) goto loc_00B33702;
loc_00B33702:
loc_00B33DA6:
    *(uint32_t *)(a4) = 5;
    goto loc_00B33DB6;
loc_00B33DAF:
    *(uint32_t *)(a4) = 13;
loc_00B33DB6:
    result = RtlCopyUnicodeString(a4 + 8, local_rdi + 40, a3, a4);
loc_00B33DC3:
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x12C` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B336B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
