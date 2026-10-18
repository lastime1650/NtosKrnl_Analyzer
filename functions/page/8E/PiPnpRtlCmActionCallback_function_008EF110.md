# PiPnpRtlCmActionCallback

- RVA: `0x008EF110`–`0x008EF7B1` (길이 `1,697` bytes)
- VA: `0x00000001408EF110`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00086FFC`
- 디코드: `421`개 명령, `1,697/1,697` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **36**; 고유 호출 대상: **29**
- 직접 호출자로 확인된 함수: **7**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x008EF1C3` → [PiDmObjectGetCachedCmProperty](../8F/PiDmObjectGetCachedCmProperty_function_008FEE70.md) (function, `0x008FEE70`)
- `0x008EF205` → [_CmMapCmObjectTypeToPnpObjectType](../8F/_CmMapCmObjectTypeToPnpObjectType_function_008FF060.md) (function, `0x008FF060`)
- `0x008EF213` → [PiPnpRtlCacheObjectBaseKey](PiPnpRtlCacheObjectBaseKey_function_008E0690.md) (function, `0x008E0690`)
- `0x008EF248` → [PiDmObjectUpdateCachedCmProperty](../8F/PiDmObjectUpdateCachedCmProperty_function_008FFCF0.md) (function, `0x008FFCF0`)
- `0x008EF25C` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x008EF2B6` → [PiPnpRtlGetFilteredDeviceInterfaceList](../8D/PiPnpRtlGetFilteredDeviceInterfaceList_function_008DE9D0.md) (function, `0x008DE9D0`)
- `0x008EF31E` → [PiDmListRemoveObject](../70/PiDmListRemoveObject_function_007045E8.md) (function, `0x007045E8`)
- `0x008EF333` → [PiPnpRtlFreeInstallerClassChangeInfo](../70/PiPnpRtlFreeInstallerClassChangeInfo_function_00704564.md) (function, `0x00704564`)
- `0x008EF37A` → [PiPnpRtlGetFilteredDeviceList](../8F/PiPnpRtlGetFilteredDeviceList_function_008FE9F8.md) (function, `0x008FE9F8`)
- `0x008EF3EC` → [PnpIsValidGuidString](../8F/PnpIsValidGuidString_function_008F37F8.md) (function, `0x008F37F8`)
- `0x008EF415` → [_CmMapCmObjectTypeToPnpObjectType](../8F/_CmMapCmObjectTypeToPnpObjectType_function_008FF060.md) (function, `0x008FF060`)
- `0x008EF41F` → [PiDmAddCacheReferenceForObject](../95/PiDmAddCacheReferenceForObject_function_00950FB4.md) (function, `0x00950FB4`)
- `0x008EF444` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008EF482` → [_CmIsDeviceRegPropWritable](../A6/_CmIsDeviceRegPropWritable_function_00A6B360.md) (function, `0x00A6B360`)
- `0x008EF4C1` → [CmGetDeviceRegProp](CmGetDeviceRegProp_function_008ED870.md) (function, `0x008ED870`)
- `0x008EF4EE` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x008EF567` → [PiDmObjectManagerAcquireSharedLock](../95/PiDmObjectManagerAcquireSharedLock_function_009511A0.md) (function, `0x009511A0`)
- `0x008EF576` → [PiDmLookupObject](../95/PiDmLookupObject_function_00951360.md) (function, `0x00951360`)
- `0x008EF597` → [PiDmObjectManagerReleaseLock](../95/PiDmObjectManagerReleaseLock_function_0095111C.md) (function, `0x0095111C`)
- `0x008EF5AD` → [PiDmObjectRelease](PiDmObjectRelease_function_008E4F70.md) (function, `0x008E4F70`)
- `0x008EF5BE` → [PiDmObjectRelease](PiDmObjectRelease_function_008E4F70.md) (function, `0x008E4F70`)
- `0x008EF5DB` → [_CmMapCmObjectTypeToPnpObjectType](../8F/_CmMapCmObjectTypeToPnpObjectType_function_008FF060.md) (function, `0x008FF060`)
- `0x008EF5E2` → [PiDmRemoveCacheReferenceForObject](../95/PiDmRemoveCacheReferenceForObject_function_00950F24.md) (function, `0x00950F24`)
- `0x008EF5F4` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008EF61C` → [PiDmObjectUpdateCachedCmProperty](../8F/PiDmObjectUpdateCachedCmProperty_function_008FFCF0.md) (function, `0x008FFCF0`)
- `0x008EF656` → [_CmClassPropertyRead](../../text/46/_CmClassPropertyRead_function_0046286C.md) (function, `0x0046286C`)
- `0x008EF666` → [CmClassPropertyWrite](../../text/6A/CmClassPropertyWrite_function_006A2D58.md) (function, `0x006A2D58`)
- `0x008EF691` → [_CmMapCmObjectTypeToPnpObjectType](../8F/_CmMapCmObjectTypeToPnpObjectType_function_008FF060.md) (function, `0x008FF060`)
- `0x008EF69F` → [PiPnpRtlCacheObjectBaseKey](PiPnpRtlCacheObjectBaseKey_function_008E0690.md) (function, `0x008E0690`)
- `0x008EF6B3` → [PiDmListAddObject](../95/PiDmListAddObject_function_00950128.md) (function, `0x00950128`)
- `0x008EF6F9` → [PiDmGetCmObjectListFromCache](../8F/PiDmGetCmObjectListFromCache_function_008FEE14.md) (function, `0x008FEE14`)
- `0x008EF729` → [PiPnpRtlGatherDeviceDeleteInfo](../72/PiPnpRtlGatherDeviceDeleteInfo_function_0072FC04.md) (function, `0x0072FC04`)
- `0x008EF73F` → [PiDmGetObject](../8D/PiDmGetObject_function_008DFAE0.md) (function, `0x008DFAE0`)
- `0x008EF75F` → [PiDmListAddObject](../95/PiDmListAddObject_function_00950128.md) (function, `0x00950128`)
- `0x008EF774` → [PiDmListAddList](../94/PiDmListAddList_function_0094F4F8.md) (function, `0x0094F4F8`)
- `0x008EF7A6` → [PiPnpRtlGatherContainerRemoveInfo](../72/PiPnpRtlGatherContainerRemoveInfo_function_0072FB58.md) (function, `0x0072FB58`)

### Direct callers
- [CmGetDeviceRegProp](CmGetDeviceRegProp_function_008ED870.md) at `0x008ED929`
- [CmGetDeviceRegProp](CmGetDeviceRegProp_function_008ED870.md) at `0x008ED9B9`
- [_CmOpenDeviceRegKey](_CmOpenDeviceRegKey_function_008EE540.md) at `0x008EE5E3`
- [CmOpenCommonClassRegKey](CmOpenCommonClassRegKey_function_008EFF5C.md) at `0x008F001D`
- [IopGetDeviceInterfaces](../8F/IopGetDeviceInterfaces_function_008F0120.md) at `0x008F028A`
- [IopGetDeviceInterfaces](../8F/IopGetDeviceInterfaces_function_008F0120.md) at `0x008F04D5`
- [_CmOpenDeviceInterfaceRegKey](../8F/_CmOpenDeviceInterfaceRegKey_function_008F31F4.md) at `0x008F3294`
- [CmGetInstallerClassRegProp](../99/CmGetInstallerClassRegProp_function_00994940.md) at `0x009949F2`
- [CmGetInstallerClassRegProp](../99/CmGetInstallerClassRegProp_function_00994940.md) at `0x00994A7C`
- [_CmGetMatchingFilteredDeviceInterfaceList](../A0/_CmGetMatchingFilteredDeviceInterfaceList_function_00A09610.md) at `0x00A096E8`

### Static image references
- `0x008EF12C` → RVA `0x00E0A740` (`.data`; read)
- `0x008EF49D` → RVA `0x00E66398` (`.data`; read)
- `0x008EF553` → RVA `0x00F8B5E0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **6**
  - `0x008EF25C` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x008EF444` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008EF4EE` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (`PAGE` → `.text`)
  - `0x008EF5F4` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008EF656` → [_CmClassPropertyRead](../../text/46/_CmClassPropertyRead_function_0046286C.md) (`PAGE` → `.text`)
  - `0x008EF666` → [CmClassPropertyWrite](../../text/6A/CmClassPropertyWrite_function_006A2D58.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **16**
  - `0x008EF28B` → [sub_00B1DC0E + 0x323](../B1/Unknown_function_00B1DC0E.md) (`tail-transfer`)
  - `0x008EF3D8` → [sub_00B1DC0E + 0x30](../B1/Unknown_function_00B1DC0E.md) (`tail-transfer`)
  - `0x008EF3E2` → [sub_00B1DC0E + 0x30](../B1/Unknown_function_00B1DC0E.md) (`tail-transfer`)
  - `0x008EF3F3` → [sub_00B1DC0E + 0x30](../B1/Unknown_function_00B1DC0E.md) (`tail-transfer`)
  - `0x008EF3FD` → [sub_00B1DC0E + 0x30](../B1/Unknown_function_00B1DC0E.md) (`tail-transfer`)
  - `0x008EF5D2` → [sub_00B1DC0E + 0x265](../B1/Unknown_function_00B1DC0E.md) (`tail-transfer`)
  - `0x008EF632` → [sub_00B1DC0E + 0x2C0](../B1/Unknown_function_00B1DC0E.md) (`tail-transfer`)
  - `0x008EF64D` → [sub_00B1DC0E](../B1/Unknown_function_00B1DC0E.md) (`tail-transfer`)
  - `0x008EF65D` → [sub_00B1DC0E](../B1/Unknown_function_00B1DC0E.md) (`tail-transfer`)
  - `0x008EF66D` → [sub_00B1DC0E](../B1/Unknown_function_00B1DC0E.md) (`tail-transfer`)
  - `0x008EF70D` → [sub_00B1DC0E + 0x9E](../B1/Unknown_function_00B1DC0E.md) (`tail-transfer`)
  - `0x008EF716` → [sub_00B1DC0E + 0x56](../B1/Unknown_function_00B1DC0E.md) (`tail-transfer`)
  - `0x008EF72F` → [sub_00B1DC0E + 0x87](../B1/Unknown_function_00B1DC0E.md) (`tail-transfer`)
  - `0x008EF788` → [sub_00B1DC0E + 0x46D](../B1/Unknown_function_00B1DC0E.md) (`tail-transfer`)
  - `0x008EF792` → [sub_00B1DC0E + 0x45E](../B1/Unknown_function_00B1DC0E.md) (`tail-transfer`)
  - `0x008EF7AC` → [sub_00B1DC0E + 0x87](../B1/Unknown_function_00B1DC0E.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
008EF110  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
008EF115  55                              push rbp
008EF116  56                              push rsi
008EF117  57                              push rdi
008EF118  41 54                           push r12
008EF11A  41 55                           push r13
008EF11C  41 56                           push r14
008EF11E  41 57                           push r15
008EF120  48 8D 6C 24 E9                  lea rbp, [rsp - 0x17]
008EF125  48 81 EC A0 00 00 00            sub rsp, 0xa0
008EF12C  48 8B 05 0D B6 51 00            mov rax, qword ptr [rip + 0x51b60d]
008EF133  48 33 C4                        xor rax, rsp
008EF136  48 89 45 0F                     mov qword ptr [rbp + 0xf], rax
008EF13A  48 8B 5D 7F                     mov rbx, qword ptr [rbp + 0x7f]
008EF13E  45 8B F8                        mov r15d, r8d
008EF141  48 89 4D CF                     mov qword ptr [rbp - 0x31], rcx
008EF145  4C 8B E2                        mov r12, rdx
008EF148  4C 8B E9                        mov r13, rcx
008EF14B  BE 02 00 00 C0                  mov esi, 0xc0000002
008EF150  41 83 F9 0D                     cmp r9d, 0xd
008EF154  0F 8F 23 01 00 00               jg 0x1408ef27d
008EF15A  0F 84 CF 03 00 00               je 0x1408ef52f
008EF160  41 83 E9 02                     sub r9d, 2
008EF164  0F 84 98 02 00 00               je 0x1408ef402
008EF16A  41 83 E9 01                     sub r9d, 1
008EF16E  0F 84 8F 05 00 00               je 0x1408ef703
008EF174  41 83 E9 01                     sub r9d, 1
008EF178  0F 84 3F 05 00 00               je 0x1408ef6bd
008EF17E  41 83 E9 05                     sub r9d, 5
008EF182  0F 85 43 01 00 00               jne 0x1408ef2cb
008EF188  45 8D 71 01                     lea r14d, [r9 + 1]
008EF18C  33 FF                           xor edi, edi
008EF18E  44 39 75 77                     cmp dword ptr [rbp + 0x77], r14d
008EF192  0F 85 82 00 00 00               jne 0x1408ef21a
008EF198  F7 43 38 00 00 01 00            test dword ptr [rbx + 0x38], 0x10000
008EF19F  75 58                           jne 0x1408ef1f9
008EF1A1  48 8B 43 30                     mov rax, qword ptr [rbx + 0x30]
008EF1A5  41 8B C8                        mov ecx, r8d
008EF1A8  44 8B 4B 18                     mov r9d, dword ptr [rbx + 0x18]
008EF1AC  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008EF1B1  48 8B 43 28                     mov rax, qword ptr [rbx + 0x28]
008EF1B5  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008EF1BA  48 8B 43 20                     mov rax, qword ptr [rbx + 0x20]
008EF1BE  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008EF1C3  E8 A8 FC 00 00                  call 0x1408fee70
008EF1C8  85 C0                           test eax, eax
008EF1CA  0F 89 F2 00 00 00               jns 0x1408ef2c2
008EF1D0  3D 25 02 00 C0                  cmp eax, 0xc0000225
008EF1D5  0F 84 E7 00 00 00               je 0x1408ef2c2
008EF1DB  3D 23 00 00 C0                  cmp eax, 0xc0000023
008EF1E0  0F 84 DC 00 00 00               je 0x1408ef2c2
008EF1E6  44 8D 6E 32                     lea r13d, [rsi + 0x32]
008EF1EA  41 3B C5                        cmp eax, r13d
008EF1ED  0F 84 CF 00 00 00               je 0x1408ef2c2
008EF1F3  4C 8B 6D CF                     mov r13, qword ptr [rbp - 0x31]
008EF1F7  8B F7                           mov esi, edi
008EF1F9  4C 8D 4B 10                     lea r9, [rbx + 0x10]
008EF1FD  49 39 39                        cmp qword ptr [r9], rdi
008EF200  75 51                           jne 0x1408ef253
008EF202  41 8B CF                        mov ecx, r15d
008EF205  E8 56 FE 00 00                  call 0x1408ff060
008EF20A  44 8B C0                        mov r8d, eax
008EF20D  49 8B CD                        mov rcx, r13
008EF210  49 8B D4                        mov rdx, r12
008EF213  E8 78 14 FF FF                  call 0x1408e0690
008EF218  EB 39                           jmp 0x1408ef253
008EF21A  8B 03                           mov eax, dword ptr [rbx]
008EF21C  85 C0                           test eax, eax
008EF21E  0F 88 19 01 00 00               js 0x1408ef33d
008EF224  48 8B 43 30                     mov rax, qword ptr [rbx + 0x30]
008EF228  48 8B 4B 20                     mov rcx, qword ptr [rbx + 0x20]
008EF22C  8B 00                           mov eax, dword ptr [rax]
008EF22E  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
008EF232  48 8B 43 28                     mov rax, qword ptr [rbx + 0x28]
008EF236  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008EF23B  8B 01                           mov eax, dword ptr [rcx]
008EF23D  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
008EF241  44 8B 4B 18                     mov r9d, dword ptr [rbx + 0x18]
008EF245  41 8B CF                        mov ecx, r15d
008EF248  E8 A3 0A 01 00                  call 0x1408ffcf0
008EF24D  EB 02                           jmp 0x1408ef251
008EF24F  33 FF                           xor edi, edi
008EF251  8B F7                           mov esi, edi
008EF253  8B C6                           mov eax, esi
008EF255  48 8B 4D 0F                     mov rcx, qword ptr [rbp + 0xf]
008EF259  48 33 CC                        xor rcx, rsp
008EF25C  E8 DF D3 DB FF                  call 0x1406ac640
008EF261  48 8B 9C 24 F8 00 00 00         mov rbx, qword ptr [rsp + 0xf8]
008EF269  48 81 C4 A0 00 00 00            add rsp, 0xa0
008EF270  41 5F                           pop r15
008EF272  41 5E                           pop r14
008EF274  41 5D                           pop r13
008EF276  41 5C                           pop r12
008EF278  5F                              pop rdi
008EF279  5E                              pop rsi
008EF27A  5D                              pop rbp
008EF27B  C3                              ret
008EF27C  CC                              int3
008EF27D  41 83 E9 0E                     sub r9d, 0xe
008EF281  0F 84 F7 04 00 00               je 0x1408ef77e
008EF287  41 83 E9 01                     sub r9d, 1
008EF28B  0F 84 A0 EC 22 00               je 0x140b1df31
008EF291  41 83 E9 01                     sub r9d, 1
008EF295  0F 84 BF 00 00 00               je 0x1408ef35a
008EF29B  41 83 F9 01                     cmp r9d, 1
008EF29F  75 B2                           jne 0x1408ef253
008EF2A1  45 8B F1                        mov r14d, r9d
008EF2A4  44 39 4D 77                     cmp dword ptr [rbp + 0x77], r9d
008EF2A8  75 A9                           jne 0x1408ef253
008EF2AA  F7 43 50 00 00 01 00            test dword ptr [rbx + 0x50], 0x10000
008EF2B1  75 A0                           jne 0x1408ef253
008EF2B3  48 8B CB                        mov rcx, rbx
008EF2B6  E8 15 F7 FE FF                  call 0x1408de9d0
008EF2BB  3D 16 00 00 C0                  cmp eax, 0xc0000016
008EF2C0  74 8D                           je 0x1408ef24f
008EF2C2  89 03                           mov dword ptr [rbx], eax
008EF2C4  BE 20 01 00 C0                  mov esi, 0xc0000120
008EF2C9  EB 88                           jmp 0x1408ef253
008EF2CB  41 83 F9 01                     cmp r9d, 1
008EF2CF  75 82                           jne 0x1408ef253
008EF2D1  33 FF                           xor edi, edi
008EF2D3  45 8B F1                        mov r14d, r9d
008EF2D6  44 39 4D 77                     cmp dword ptr [rbp + 0x77], r9d
008EF2DA  0F 84 A4 00 00 00               je 0x1408ef384
008EF2E0  39 3B                           cmp dword ptr [rbx], edi
008EF2E2  0F 8D 16 03 00 00               jge 0x1408ef5fe
008EF2E8  45 3B FE                        cmp r15d, r14d
008EF2EB  0F 85 62 FF FF FF               jne 0x1408ef253
008EF2F1  83 7B 18 09                     cmp dword ptr [rbx + 0x18], 9
008EF2F5  0F 85 58 FF FF FF               jne 0x1408ef253
008EF2FB  4C 8B 73 08                     mov r14, qword ptr [rbx + 8]
008EF2FF  39 3B                           cmp dword ptr [rbx], edi
008EF301  7C 2D                           jl 0x1408ef330
008EF303  4D 8B 06                        mov r8, qword ptr [r14]
008EF306  4D 85 C0                        test r8, r8
008EF309  74 25                           je 0x1408ef330
008EF30B  49 8B 56 08                     mov rdx, qword ptr [r14 + 8]
008EF30F  BB 04 00 00 00                  mov ebx, 4
008EF314  48 85 D2                        test rdx, rdx
008EF317  74 0A                           je 0x1408ef323
008EF319  45 33 C9                        xor r9d, r9d
008EF31C  8B CB                           mov ecx, ebx
008EF31E  E8 C5 52 E1 FF                  call 0x1407045e8
008EF323  49 8B 56 10                     mov rdx, qword ptr [r14 + 0x10]
008EF327  48 85 D2                        test rdx, rdx
008EF32A  0F 85 7B 03 00 00               jne 0x1408ef6ab
008EF330  49 8B CE                        mov rcx, r14
008EF333  E8 2C 52 E1 FF                  call 0x140704564
008EF338  E9 16 FF FF FF                  jmp 0x1408ef253
008EF33D  3D 25 02 00 C0                  cmp eax, 0xc0000225
008EF342  0F 85 09 FF FF FF               jne 0x1408ef251
008EF348  89 7C 24 30                     mov dword ptr [rsp + 0x30], edi
008EF34C  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
008EF351  89 7C 24 20                     mov dword ptr [rsp + 0x20], edi
008EF355  E9 E7 FE FF FF                  jmp 0x1408ef241
008EF35A  41 BE 01 00 00 00               mov r14d, 1
008EF360  44 39 75 77                     cmp dword ptr [rbp + 0x77], r14d
008EF364  0F 85 E9 FE FF FF               jne 0x1408ef253
008EF36A  F7 43 48 00 00 01 00            test dword ptr [rbx + 0x48], 0x10000
008EF371  0F 85 DC FE FF FF               jne 0x1408ef253
008EF377  48 8B CB                        mov rcx, rbx
008EF37A  E8 79 F6 00 00                  call 0x1408fe9f8
008EF37F  E9 37 FF FF FF                  jmp 0x1408ef2bb
008EF384  F7 43 2C 00 00 02 00            test dword ptr [rbx + 0x2c], 0x20000
008EF38B  8B F7                           mov esi, edi
008EF38D  75 1E                           jne 0x1408ef3ad
008EF38F  8B 43 28                        mov eax, dword ptr [rbx + 0x28]
008EF392  4C 8B EF                        mov r13, rdi
008EF395  89 7D D7                        mov dword ptr [rbp - 0x29], edi
008EF398  85 C0                           test eax, eax
008EF39A  0F 85 96 00 00 00               jne 0x1408ef436
008EF3A0  39 7B 28                        cmp dword ptr [rbx + 0x28], edi
008EF3A3  0F 84 AC 00 00 00               je 0x1408ef455
008EF3A9  4C 8B 6D CF                     mov r13, qword ptr [rbp - 0x31]
008EF3AD  4C 8D 4B 10                     lea r9, [rbx + 0x10]
008EF3B1  49 39 39                        cmp qword ptr [r9], rdi
008EF3B4  0F 84 D4 02 00 00               je 0x1408ef68e
008EF3BA  45 3B FE                        cmp r15d, r14d
008EF3BD  0F 85 90 FE FF FF               jne 0x1408ef253
008EF3C3  83 7B 18 09                     cmp dword ptr [rbx + 0x18], 9
008EF3C7  0F 85 86 FE FF FF               jne 0x1408ef253
008EF3CD  48 8B F7                        mov rsi, rdi
008EF3D0  48 89 7D CF                     mov qword ptr [rbp - 0x31], rdi
008EF3D4  44 39 73 1C                     cmp dword ptr [rbx + 0x1c], r14d
008EF3D8  0F 85 60 E8 22 00               jne 0x140b1dc3e
008EF3DE  83 7B 28 4E                     cmp dword ptr [rbx + 0x28], 0x4e
008EF3E2  0F 85 56 E8 22 00               jne 0x140b1dc3e
008EF3E8  48 8B 4B 20                     mov rcx, qword ptr [rbx + 0x20]
008EF3EC  E8 07 44 00 00                  call 0x1408f37f8
008EF3F1  84 C0                           test al, al
008EF3F3  0F 84 45 E8 22 00               je 0x140b1dc3e
008EF3F9  48 8B 73 20                     mov rsi, qword ptr [rbx + 0x20]
008EF3FD  E9 3C E8 22 00                  jmp 0x140b1dc3e
008EF402  41 BE 01 00 00 00               mov r14d, 1
008EF408  44 39 75 77                     cmp dword ptr [rbp + 0x77], r14d
008EF40C  0F 85 B6 01 00 00               jne 0x1408ef5c8
008EF412  41 8B CF                        mov ecx, r15d
008EF415  E8 46 FC 00 00                  call 0x1408ff060
008EF41A  8B C8                           mov ecx, eax
008EF41C  45 33 C0                        xor r8d, r8d
008EF41F  E8 90 1B 06 00                  call 0x140950fb4
008EF424  8B F0                           mov esi, eax
008EF426  89 03                           mov dword ptr [rbx], eax
008EF428  C1 FE 1F                        sar esi, 0x1f
008EF42B  81 E6 20 01 00 C0               and esi, 0xc0000120
008EF431  E9 1D FE FF FF                  jmp 0x1408ef253
008EF436  48 8B D0                        mov rdx, rax
008EF439  B9 00 01 00 00                  mov ecx, 0x100
008EF43E  41 B8 50 6E 70 47               mov r8d, 0x47706e50
008EF444  E8 A7 2C 29 00                  call 0x140b820f0
008EF449  4C 8B E8                        mov r13, rax
008EF44C  48 85 C0                        test rax, rax
008EF44F  0F 84 4B FF FF FF               je 0x1408ef3a0
008EF455  8B 43 28                        mov eax, dword ptr [rbx + 0x28]
008EF458  41 8B CF                        mov ecx, r15d
008EF45B  44 88 75 C7                     mov byte ptr [rbp - 0x39], r14b
008EF45F  89 45 FF                        mov dword ptr [rbp - 1], eax
008EF462  41 2B CE                        sub ecx, r14d
008EF465  74 10                           je 0x1408ef477
008EF467  41 3B CE                        cmp ecx, r14d
008EF46A  0F 84 D2 01 00 00               je 0x1408ef642
008EF470  8B F7                           mov esi, edi
008EF472  E9 9C 00 00 00                  jmp 0x1408ef513
008EF477  44 8B 53 18                     mov r10d, dword ptr [rbx + 0x18]
008EF47B  4C 8D 45 C7                     lea r8, [rbp - 0x39]
008EF47F  41 8B D2                        mov edx, r10d
008EF482  E8 D9 BE 17 00                  call 0x140a6b360
008EF487  85 C0                           test eax, eax
008EF489  78 0A                           js 0x1408ef495
008EF48B  40 38 7D C7                     cmp byte ptr [rbp - 0x39], dil
008EF48F  0F 84 DE 01 00 00               je 0x1408ef673
008EF495  4C 8B 43 10                     mov r8, qword ptr [rbx + 0x10]
008EF499  48 8D 45 FF                     lea rax, [rbp - 1]
008EF49D  48 8B 0D F4 6E 57 00            mov rcx, qword ptr [rip + 0x576ef4]
008EF4A4  45 8B CA                        mov r9d, r10d
008EF4A7  89 7C 24 38                     mov dword ptr [rsp + 0x38], edi
008EF4AB  49 8B D4                        mov rdx, r12
008EF4AE  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008EF4B3  48 8D 45 D7                     lea rax, [rbp - 0x29]
008EF4B7  4C 89 6C 24 28                  mov qword ptr [rsp + 0x28], r13
008EF4BC  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008EF4C1  E8 AA E3 FF FF                  call 0x1408ed870
008EF4C6  8B F0                           mov esi, eax
008EF4C8  85 C0                           test eax, eax
008EF4CA  78 2B                           js 0x1408ef4f7
008EF4CC  8B 43 1C                        mov eax, dword ptr [rbx + 0x1c]
008EF4CF  39 45 D7                        cmp dword ptr [rbp - 0x29], eax
008EF4D2  0F 85 A5 01 00 00               jne 0x1408ef67d
008EF4D8  8B 45 FF                        mov eax, dword ptr [rbp - 1]
008EF4DB  3B 43 28                        cmp eax, dword ptr [rbx + 0x28]
008EF4DE  0F 85 99 01 00 00               jne 0x1408ef67d
008EF4E4  48 8B 53 20                     mov rdx, qword ptr [rbx + 0x20]
008EF4E8  44 8B C0                        mov r8d, eax
008EF4EB  49 8B CD                        mov rcx, r13
008EF4EE  E8 1D 76 DD FF                  call 0x1406c6b10
008EF4F3  85 C0                           test eax, eax
008EF4F5  74 15                           je 0x1408ef50c
008EF4F7  81 FE 25 02 00 C0               cmp esi, 0xc0000225
008EF4FD  0F 85 7A 01 00 00               jne 0x1408ef67d
008EF503  39 7B 28                        cmp dword ptr [rbx + 0x28], edi
008EF506  0F 85 64 FF FF FF               jne 0x1408ef470
008EF50C  89 33                           mov dword ptr [rbx], esi
008EF50E  BE 20 01 00 C0                  mov esi, 0xc0000120
008EF513  4D 85 ED                        test r13, r13
008EF516  0F 85 D0 00 00 00               jne 0x1408ef5ec
008EF51C  85 F6                           test esi, esi
008EF51E  0F 84 85 FE FF FF               je 0x1408ef3a9
008EF524  0F 88 29 FD FF FF               js 0x1408ef253
008EF52A  E9 8B FE FF FF                  jmp 0x1408ef3ba
008EF52F  41 BE 01 00 00 00               mov r14d, 1
008EF535  33 FF                           xor edi, edi
008EF537  44 39 75 77                     cmp dword ptr [rbp + 0x77], r14d
008EF53B  0F 84 10 FD FF FF               je 0x1408ef251
008EF541  41 83 FF 05                     cmp r15d, 5
008EF545  0F 85 DD 00 00 00               jne 0x1408ef628
008EF54B  39 3B                           cmp dword ptr [rbx], edi
008EF54D  0F 8C FE FC FF FF               jl 0x1408ef251
008EF553  48 8D 0D 86 C0 69 00            lea rcx, [rip + 0x69c086]
008EF55A  48 89 7D FF                     mov qword ptr [rbp - 1], rdi
008EF55E  8B F7                           mov esi, edi
008EF560  40 88 7D C7                     mov byte ptr [rbp - 0x39], dil
008EF564  44 8B EF                        mov r13d, edi
008EF567  E8 34 1C 06 00                  call 0x1409511a0
008EF56C  49 8B D4                        mov rdx, r12
008EF56F  48 8D 0D 6A C0 69 00            lea rcx, [rip + 0x69c06a]
008EF576  E8 E5 1D 06 00                  call 0x140951360
008EF57B  4C 8B F8                        mov r15, rax
008EF57E  48 85 C0                        test rax, rax
008EF581  0F 84 B0 00 00 00               je 0x1408ef637
008EF587  F0 44 01 70 08                  lock add dword ptr [rax + 8], r14d
008EF58C  48 8B 75 FF                     mov rsi, qword ptr [rbp - 1]
008EF590  48 8D 0D 49 C0 69 00            lea rcx, [rip + 0x69c049]
008EF597  E8 80 1B 06 00                  call 0x14095111c
008EF59C  45 85 ED                        test r13d, r13d
008EF59F  0F 89 8F 01 00 00               jns 0x1408ef734
008EF5A5  4D 85 FF                        test r15, r15
008EF5A8  74 08                           je 0x1408ef5b2
008EF5AA  49 8B CF                        mov rcx, r15
008EF5AD  E8 BE 59 FF FF                  call 0x1408e4f70
008EF5B2  48 85 F6                        test rsi, rsi
008EF5B5  0F 84 96 FC FF FF               je 0x1408ef251
008EF5BB  48 8B CE                        mov rcx, rsi
008EF5BE  E8 AD 59 FF FF                  call 0x1408e4f70
008EF5C3  E9 89 FC FF FF                  jmp 0x1408ef251
008EF5C8  33 FF                           xor edi, edi
008EF5CA  39 3B                           cmp dword ptr [rbx], edi
008EF5CC  7C 0A                           jl 0x1408ef5d8
008EF5CE  40 38 7B 20                     cmp byte ptr [rbx + 0x20], dil
008EF5D2  0F 85 9B E8 22 00               jne 0x140b1de73
008EF5D8  41 8B CF                        mov ecx, r15d
008EF5DB  E8 80 FA 00 00                  call 0x1408ff060
008EF5E0  8B C8                           mov ecx, eax
008EF5E2  E8 3D 19 06 00                  call 0x140950f24
008EF5E7  E9 65 FC FF FF                  jmp 0x1408ef251
008EF5EC  BA 50 6E 70 47                  mov edx, 0x47706e50
008EF5F1  49 8B CD                        mov rcx, r13
008EF5F4  E8 77 32 29 00                  call 0x140b82870
008EF5F9  E9 1E FF FF FF                  jmp 0x1408ef51c
008EF5FE  8B 43 28                        mov eax, dword ptr [rbx + 0x28]
008EF601  41 8B CF                        mov ecx, r15d
008EF604  44 8B 4B 18                     mov r9d, dword ptr [rbx + 0x18]
008EF608  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
008EF60C  48 8B 43 20                     mov rax, qword ptr [rbx + 0x20]
008EF610  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008EF615  8B 43 1C                        mov eax, dword ptr [rbx + 0x1c]
008EF618  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
008EF61C  E8 CF 06 01 00                  call 0x1408ffcf0
008EF621  8B F7                           mov esi, edi
008EF623  E9 C0 FC FF FF                  jmp 0x1408ef2e8
008EF628  41 83 FF 06                     cmp r15d, 6
008EF62C  0F 85 1F FC FF FF               jne 0x1408ef251
008EF632  E9 97 E8 22 00                  jmp 0x140b1dece
008EF637  41 BD 34 00 00 C0               mov r13d, 0xc0000034
008EF63D  E9 4E FF FF FF                  jmp 0x1408ef590
008EF642  44 8B 4B 18                     mov r9d, dword ptr [rbx + 0x18]
008EF646  41 8D 41 FF                     lea eax, [r9 - 1]
008EF64A  83 F8 24                        cmp eax, 0x24
008EF64D  0F 87 BB E5 22 00               ja 0x140b1dc0e
008EF653  41 8B C9                        mov ecx, r9d
008EF656  E8 11 32 B7 FF                  call 0x14046286c
008EF65B  84 C0                           test al, al
008EF65D  0F 84 AB E5 22 00               je 0x140b1dc0e
008EF663  41 8B C9                        mov ecx, r9d
008EF666  E8 ED 36 DB FF                  call 0x1406a2d58
008EF66B  84 C0                           test al, al
008EF66D  0F 85 9B E5 22 00               jne 0x140b1dc0e
008EF673  BE 22 00 00 C0                  mov esi, 0xc0000022
008EF678  E9 8F FE FF FF                  jmp 0x1408ef50c
008EF67D  81 FE 22 00 00 C0               cmp esi, 0xc0000022
008EF683  0F 85 E7 FD FF FF               jne 0x1408ef470
008EF689  E9 7E FE FF FF                  jmp 0x1408ef50c
008EF68E  41 8B CF                        mov ecx, r15d
008EF691  E8 CA F9 00 00                  call 0x1408ff060
008EF696  44 8B C0                        mov r8d, eax
008EF699  49 8B CD                        mov rcx, r13
008EF69C  49 8B D4                        mov rdx, r12
008EF69F  E8 EC 0F FF FF                  call 0x1408e0690
008EF6A4  85 F6                           test esi, esi
008EF6A6  E9 79 FE FF FF                  jmp 0x1408ef524
008EF6AB  4D 8B 06                        mov r8, qword ptr [r14]
008EF6AE  45 33 C9                        xor r9d, r9d
008EF6B1  8B CB                           mov ecx, ebx
008EF6B3  E8 70 0A 06 00                  call 0x140950128
008EF6B8  E9 73 FC FF FF                  jmp 0x1408ef330
008EF6BD  41 BE 01 00 00 00               mov r14d, 1
008EF6C3  44 39 75 77                     cmp dword ptr [rbp + 0x77], r14d
008EF6C7  0F 85 86 FB FF FF               jne 0x1408ef253
008EF6CD  F7 43 38 00 00 01 00            test dword ptr [rbx + 0x38], 0x10000
008EF6D4  0F 85 79 FB FF FF               jne 0x1408ef253
008EF6DA  48 8B 43 30                     mov rax, qword ptr [rbx + 0x30]
008EF6DE  41 8B CF                        mov ecx, r15d
008EF6E1  4C 8B 4B 20                     mov r9, qword ptr [rbx + 0x20]
008EF6E5  4C 8B 43 18                     mov r8, qword ptr [rbx + 0x18]
008EF6E9  48 8B 53 10                     mov rdx, qword ptr [rbx + 0x10]
008EF6ED  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008EF6F2  8B 43 28                        mov eax, dword ptr [rbx + 0x28]
008EF6F5  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
008EF6F9  E8 16 F7 00 00                  call 0x1408fee14
008EF6FE  E9 B8 FB FF FF                  jmp 0x1408ef2bb
008EF703  41 BE 01 00 00 00               mov r14d, 1
008EF709  44 39 75 77                     cmp dword ptr [rbp + 0x77], r14d
008EF70D  0F 85 99 E5 22 00               jne 0x140b1dcac
008EF713  45 3B FE                        cmp r15d, r14d
008EF716  0F 85 48 E5 22 00               jne 0x140b1dc64
008EF71C  33 FF                           xor edi, edi
008EF71E  48 8D 55 CF                     lea rdx, [rbp - 0x31]
008EF722  49 8B CC                        mov rcx, r12
008EF725  48 89 7D CF                     mov qword ptr [rbp - 0x31], rdi
008EF729  E8 D6 04 E4 FF                  call 0x14072fc04
008EF72E  90                              nop
008EF72F  E9 61 E5 22 00                  jmp 0x140b1dc95
008EF734  48 8B 53 18                     mov rdx, qword ptr [rbx + 0x18]
008EF738  4C 8D 45 FF                     lea r8, [rbp - 1]
008EF73C  41 8B CE                        mov ecx, r14d
008EF73F  E8 9C 03 FF FF                  call 0x1408dfae0
008EF744  48 8B 75 FF                     mov rsi, qword ptr [rbp - 1]
008EF748  85 C0                           test eax, eax
008EF74A  0F 88 55 FE FF FF               js 0x1408ef5a5
008EF750  4C 8D 4D C7                     lea r9, [rbp - 0x39]
008EF754  4C 8B C6                        mov r8, rsi
008EF757  49 8B D7                        mov rdx, r15
008EF75A  B9 03 00 00 00                  mov ecx, 3
008EF75F  E8 C4 09 06 00                  call 0x140950128
008EF764  40 38 7D C7                     cmp byte ptr [rbp - 0x39], dil
008EF768  0F 85 37 FE FF FF               jne 0x1408ef5a5
008EF76E  4C 8B CE                        mov r9, rsi
008EF771  49 8B D7                        mov rdx, r15
008EF774  E8 7F FD 05 00                  call 0x14094f4f8
008EF779  E9 27 FE FF FF                  jmp 0x1408ef5a5
008EF77E  41 BE 01 00 00 00               mov r14d, 1
008EF784  44 39 75 77                     cmp dword ptr [rbp + 0x77], r14d
008EF788  0F 85 ED E8 22 00               jne 0x140b1e07b
008EF78E  41 83 FF 05                     cmp r15d, 5
008EF792  0F 85 D4 E8 22 00               jne 0x140b1e06c
008EF798  48 8B 4B 18                     mov rcx, qword ptr [rbx + 0x18]
008EF79C  4C 8D 45 CF                     lea r8, [rbp - 0x31]
008EF7A0  33 FF                           xor edi, edi
008EF7A2  48 89 7D CF                     mov qword ptr [rbp - 0x31], rdi
008EF7A6  E8 AD 03 E4 FF                  call 0x14072fb58
008EF7AB  90                              nop
008EF7AC  E9 E4 E4 22 00                  jmp 0x140b1dc95
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiPnpRtlCmActionCallback(__int64 a1, __int64 a2, int a3, int a4, unsigned int a5, __int64 a6)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m4F;
    unsigned int v_stack_m50;
    unsigned int v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int8 v_stack_m88;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned int v_stack_p30;
    unsigned int v_stack_p38;

    v_stack_p20 = v_rbx;
    v_rsp = (v_rsp) - (160);
    result = (*(unsigned __int64 *)(v_rip + 5355021)) ^ (v_rsp);
    v_stack_m40 = result;
    v_stack_m80 = a1;
    if (a4 > 13) goto loc_008EF27D;
    if (a4 == 13) goto loc_008EF52F;
    a4 = (unsigned int)((a4) - (2));
    if (condition_is_equal) goto loc_008EF402;
    a4 = (unsigned int)((a4) - (1));
    if (condition_is_equal) goto loc_008EF703;
    a4 = (unsigned int)((a4) - (1));
    if (condition_is_equal) goto loc_008EF6BD;
    a4 = (unsigned int)((a4) - (5));
    if (condition_is_not_equal) goto loc_008EF2CB;
    v_rdi = 0;
    if (a5 != ((unsigned int)(a4 + 1))) goto loc_008EF21A;
    if (((*(unsigned int *)(a6 + 56)) & (0x10000ULL)) != 0) goto loc_008EF1F9;
    v_stack_mA8 = *(unsigned __int64 *)(a6 + 48);
    v_stack_mB0 = *(unsigned __int64 *)(a6 + 40);
    v_stack_mB8 = *(unsigned __int64 *)(a6 + 32);
    result = PiDmObjectGetCachedCmProperty((unsigned int)(a3), a2, a3, (unsigned int)(*(unsigned int *)(a6 + 24)));
    if (!sign_flag) goto loc_008EF2C2;
    if (((unsigned int)(result)) == 0xC0000225ULL) goto loc_008EF2C2;
    if (((unsigned int)(result)) == 0xC0000023ULL) goto loc_008EF2C2;
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0xC0000002ULL) + 50))) goto loc_008EF2C2;
loc_008EF1F9:
    if ((*(unsigned __int64 *)(a6 + 16)) != 0) goto loc_008EF253;
    result = _CmMapCmObjectTypeToPnpObjectType((unsigned int)((unsigned int)((unsigned int)(a3))), a2, a3, a6 + 16);
    result = PiPnpRtlCacheObjectBaseKey(v_stack_m80, a2, (unsigned int)((unsigned int)(result)), a6 + 16);
    goto loc_008EF253;
loc_008EF21A:
    if (sign_flag) goto loc_008EF33D;
    v_stack_mA8 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a6 + 48))));
    v_stack_mB0 = *(unsigned __int64 *)(a6 + 40);
    v_stack_mB8 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a6 + 32))));
loc_008EF241:
    result = PiDmObjectUpdateCachedCmProperty((unsigned int)((unsigned int)((unsigned int)(a3))), a2, (unsigned int)((unsigned int)(result)), (unsigned int)(*(unsigned int *)(a6 + 24)));
    goto loc_008EF251;
loc_008EF24F:
    v_rdi = 0;
loc_008EF251:
loc_008EF253:
    a1 = (v_stack_m40) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, (unsigned int)((unsigned int)(result)), (unsigned int)(*(unsigned int *)(a6 + 24)));
    v_rsp = (v_rsp) + (160);
    return result;
loc_008EF27D:
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(a6 + 24))) - (14));
    if (condition_is_equal) goto loc_008EF77E;
    a4 = (unsigned int)((a4) - (1));
    a4 = (unsigned int)((a4) - (1));
    if (condition_is_equal) goto loc_008EF35A;
    if (a4 != 1) goto loc_008EF253;
    if (a5 != a4) goto loc_008EF253;
    if (((*(unsigned int *)(v_stack_p20 + 80)) & (0x10000ULL)) != 0) goto loc_008EF253;
    result = PiPnpRtlGetFilteredDeviceInterfaceList(v_stack_p20, a2, (unsigned int)((unsigned int)(result)), a4);
loc_008EF2BB:
    if (((unsigned int)(result)) == 0xC0000016ULL) goto loc_008EF24F;
loc_008EF2C2:
    *(unsigned int *)(v_stack_p20) = (unsigned int)(result);
    goto loc_008EF253;
loc_008EF2CB:
    if (a4 != 1) goto loc_008EF253;
    v_rdi = 0;
    if (a5 == a4) goto loc_008EF384;
    if ((*(unsigned int *)(v_stack_p20)) >= 0) goto loc_008EF5FE;
loc_008EF2E8:
    if (((unsigned int)((unsigned int)(a3))) != ((unsigned int)((unsigned int)(a4)))) goto loc_008EF253;
    if ((*(unsigned int *)(v_stack_p20 + 24)) != 9) goto loc_008EF253;
    if ((*(unsigned int *)(v_stack_p20)) < 0) goto loc_008EF330;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p20 + 8)) == 0) goto loc_008EF330;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p20 + 8) + 8) != 0) {
        a4 = 0;
        a1 = 4;
        result = PiDmListRemoveObject(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p20 + 8) + 8), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p20 + 8)), a4);
    }
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p20 + 8) + 16) != 0) goto loc_008EF6AB;
loc_008EF330:
    result = PiPnpRtlFreeInstallerClassChangeInfo(*(unsigned __int64 *)(v_stack_p20 + 8), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p20 + 8) + 16), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p20 + 8)), a4);
    goto loc_008EF253;
loc_008EF33D:
    if (((unsigned int)(result)) != 0xC0000225ULL) goto loc_008EF251;
    v_stack_p30 = 0;
    v_stack_p28 = 0;
    v_stack_p20 = 0;
    goto loc_008EF241;
loc_008EF35A:
    if (a5 != 1) goto loc_008EF253;
    if (((*(unsigned int *)(4 + 72)) & (0x10000ULL)) != 0) goto loc_008EF253;
    result = PiPnpRtlGetFilteredDeviceList(4, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p20 + 8) + 16), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p20 + 8)), a4);
    goto loc_008EF2BB;
loc_008EF384:
    if (((*(unsigned int *)(4 + 44)) & (0x20000ULL)) != 0) goto loc_008EF3AD;
    v_stack_m78 = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(4 + 40))) != 0) goto loc_008EF436;
loc_008EF3A0:
    if ((*(unsigned int *)(4 + 40)) == 0) goto loc_008EF455;
loc_008EF3A9:
loc_008EF3AD:
    if ((*(unsigned __int64 *)(4 + 16)) == 0) goto loc_008EF68E;
loc_008EF3BA:
    if (((unsigned int)((unsigned int)(a3))) != 1) goto loc_008EF253;
    if ((*(unsigned int *)(4 + 24)) != 9) goto loc_008EF253;
    v_stack_m80 = 0;
    result = PnpIsValidGuidString(*(unsigned __int64 *)(4 + 32), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p20 + 8) + 16), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p20 + 8)), 4 + 16);
loc_008EF402:
    if (a5 != 1) goto loc_008EF5C8;
    result = _CmMapCmObjectTypeToPnpObjectType((unsigned int)((unsigned int)((unsigned int)(a3))), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p20 + 8) + 16), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p20 + 8)), 4 + 16);
    a3 = 0;
    result = PiDmAddCacheReferenceForObject((unsigned int)((unsigned int)(result)), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p20 + 8) + 16), a3, 4 + 16);
    *(unsigned int *)(4) = (unsigned int)(result);
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(result))) >> (31));
    v_rsi = (unsigned int)((v_rsi) & (0xC0000120ULL));
    goto loc_008EF253;
loc_008EF436:
    result = ExAllocatePool2(256, result, (unsigned int)(0x47706E50ULL), 4 + 16);
    if (result == 0) goto loc_008EF3A0;
loc_008EF455:
    v_stack_m88 = 1;
    v_stack_m50 = (unsigned int)((unsigned int)(*(unsigned int *)(4 + 40)));
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a3)))) - (1));
    if (condition_is_equal) goto loc_008EF477;
    if (((unsigned int)(a1)) == 1) goto loc_008EF642;
loc_008EF470:
    goto loc_008EF513;
loc_008EF477:
    result = _CmIsDeviceRegPropWritable(a1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(4 + 24)))), v_stack_m88, 4 + 16);
    if (sign_flag) goto loc_008EF495;
    if (v_stack_m88 == 0) goto loc_008EF673;
loc_008EF495:
    v_stack_p38 = 0;
    v_stack_p30 = v_stack_m50;
    v_stack_p28 = result;
    v_stack_p20 = v_stack_m78;
    result = CmGetDeviceRegProp(*(unsigned __int64 *)(v_rip + 5730036), a2, *(unsigned __int64 *)(4 + 16), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(4 + 24)))));
    if (sign_flag) goto loc_008EF4F7;
    if (v_stack_m78 != ((unsigned int)((unsigned int)(*(unsigned int *)(4 + 28))))) goto loc_008EF67D;
    if (((unsigned int)((unsigned int)(v_stack_m50))) != (*(unsigned int *)(4 + 40))) goto loc_008EF67D;
    result = memcmp(result, *(unsigned __int64 *)(4 + 32), (unsigned int)((unsigned int)((unsigned int)(v_stack_m50))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(4 + 24)))));
    if ((unsigned int)(result) == 0) goto loc_008EF50C;
loc_008EF4F7:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != 0xC0000225ULL) goto loc_008EF67D;
    if ((*(unsigned int *)(4 + 40)) != 0) goto loc_008EF470;
loc_008EF50C:
    *(unsigned int *)(4) = (unsigned int)((unsigned int)((unsigned int)(result)));
loc_008EF513:
    if (result != 0) goto loc_008EF5EC;
loc_008EF51C:
    if ((unsigned int)((unsigned int)(0xC0000120ULL)) == 0) goto loc_008EF3A9;
loc_008EF524:
    if (sign_flag) goto loc_008EF253;
    goto loc_008EF3BA;
loc_008EF52F:
    v_rdi = 0;
    if (a5 == 1) goto loc_008EF251;
    if (((unsigned int)((unsigned int)(a3))) != 5) goto loc_008EF628;
    if ((*(unsigned int *)(4)) < 0) goto loc_008EF251;
    v_stack_m50 = 0;
    v_stack_m88 = 0;
    result = PiDmObjectManagerAcquireSharedLock(v_rip + 6930566, *(unsigned __int64 *)(4 + 32), (unsigned int)((unsigned int)((unsigned int)(v_stack_m50))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(4 + 24)))));
    result = PiDmLookupObject(v_rip + 6930538, a2, (unsigned int)((unsigned int)((unsigned int)(v_stack_m50))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(4 + 24)))));
    if (result == 0) goto loc_008EF637;
loc_008EF590:
    result = PiDmObjectManagerReleaseLock(v_rip + 6930505, a2, (unsigned int)((unsigned int)((unsigned int)(v_stack_m50))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(4 + 24)))));
    if (!sign_flag) goto loc_008EF734;
loc_008EF5A5:
    if (result != 0) {
        a1 = result;
        result = PiDmObjectRelease(a1, a2, (unsigned int)((unsigned int)((unsigned int)(v_stack_m50))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(4 + 24)))));
    }
    if (v_stack_m50 == 0) goto loc_008EF251;
    result = PiDmObjectRelease(v_stack_m50, a2, (unsigned int)((unsigned int)((unsigned int)(v_stack_m50))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(4 + 24)))));
    goto loc_008EF251;
loc_008EF5C8:
    v_rdi = 0;
    if ((*(unsigned int *)(4)) < 0) goto loc_008EF5D8;
loc_008EF5D8:
    result = _CmMapCmObjectTypeToPnpObjectType((unsigned int)((unsigned int)(result)), a2, (unsigned int)((unsigned int)((unsigned int)(v_stack_m50))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(4 + 24)))));
    result = PiDmRemoveCacheReferenceForObject((unsigned int)((unsigned int)(result)), a2, (unsigned int)((unsigned int)((unsigned int)(v_stack_m50))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(4 + 24)))));
    goto loc_008EF251;
loc_008EF5EC:
    result = ExFreePoolWithTag(0, (unsigned int)(0x47706E50ULL), (unsigned int)((unsigned int)((unsigned int)(v_stack_m50))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(4 + 24)))));
    goto loc_008EF51C;
loc_008EF5FE:
    v_stack_p30 = (unsigned int)((unsigned int)(*(unsigned int *)(4 + 40)));
    v_stack_p28 = *(unsigned __int64 *)(4 + 32);
    v_stack_p20 = (unsigned int)((unsigned int)(*(unsigned int *)(4 + 28)));
    result = PiDmObjectUpdateCachedCmProperty((unsigned int)((unsigned int)(result)), (unsigned int)(0x47706E50ULL), (unsigned int)((unsigned int)((unsigned int)(v_stack_m50))), (unsigned int)(*(unsigned int *)(4 + 24)));
    goto loc_008EF2E8;
loc_008EF628:
    if (((unsigned int)(result)) != 6) goto loc_008EF251;
loc_008EF637:
    goto loc_008EF590;
loc_008EF642:
    result = _CmClassPropertyRead((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(4 + 24)))), (unsigned int)(0x47706E50ULL), (unsigned int)((unsigned int)((unsigned int)(v_stack_m50))), (unsigned int)(*(unsigned int *)(4 + 24)));
    result = CmClassPropertyWrite((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(4 + 24)))), (unsigned int)(0x47706E50ULL), (unsigned int)((unsigned int)((unsigned int)(v_stack_m50))), (unsigned int)(*(unsigned int *)(4 + 24)));
loc_008EF673:
    goto loc_008EF50C;
loc_008EF67D:
    if (((unsigned int)((unsigned int)(0xC0000022ULL))) != 0xC0000022ULL) goto loc_008EF470;
    goto loc_008EF50C;
loc_008EF68E:
    result = _CmMapCmObjectTypeToPnpObjectType((unsigned int)((unsigned int)(result)), (unsigned int)(0x47706E50ULL), (unsigned int)((unsigned int)((unsigned int)(v_stack_m50))), (unsigned int)(*(unsigned int *)(4 + 24)));
    result = PiPnpRtlCacheObjectBaseKey((unsigned int)(0xC0000034ULL), a2, (unsigned int)((unsigned int)(result)), (unsigned int)(*(unsigned int *)(4 + 24)));
    goto loc_008EF524;
loc_008EF6AB:
    a4 = 0;
    result = PiDmListAddObject(4, a2, *(unsigned __int64 *)(1), a4);
    goto loc_008EF330;
loc_008EF6BD:
    if (a5 != 1) goto loc_008EF253;
    if (((*(unsigned int *)(4 + 56)) & (0x10000ULL)) != 0) goto loc_008EF253;
    v_stack_p28 = *(unsigned __int64 *)(4 + 48);
    v_stack_p20 = (unsigned int)((unsigned int)(*(unsigned int *)(4 + 40)));
    result = PiDmGetCmObjectListFromCache((unsigned int)((unsigned int)(result)), *(unsigned __int64 *)(4 + 16), *(unsigned __int64 *)(4 + 24), *(unsigned __int64 *)(4 + 32));
    goto loc_008EF2BB;
loc_008EF703:
    v_rdi = 0;
    v_stack_m80 = 0;
    result = PiPnpRtlGatherDeviceDeleteInfo(a2, v_stack_m80, *(unsigned __int64 *)(4 + 24), *(unsigned __int64 *)(4 + 32));
loc_008EF734:
    result = PiDmGetObject(1, *(unsigned __int64 *)(4 + 24), v_stack_m50, *(unsigned __int64 *)(4 + 32));
    if (sign_flag) goto loc_008EF5A5;
    result = PiDmListAddObject(3, result, v_stack_m50, v_stack_m88);
    if (v_stack_m88 != 0) goto loc_008EF5A5;
    result = PiDmListAddList(3, result, v_stack_m50, v_stack_m50);
    goto loc_008EF5A5;
loc_008EF77E:
    v_rdi = 0;
    v_stack_m80 = 0;
    result = PiPnpRtlGatherContainerRemoveInfo(*(unsigned __int64 *)(4 + 24), result, v_stack_m80, v_stack_m50);
}
```

## 5. (Beta) C Style

```c
int64_t PiPnpRtlCmActionCallback(int64_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4, uint32_t Arg5, void *Arg6)
{
    uint8_t *arg6 = (uint8_t *)Arg6;

    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m4F;
    uint32_t v_stack_m50;
    uint32_t v_stack_m78;
    uint64_t v_stack_m80;
    uint8_t v_stack_m88;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint32_t v_stack_p30;
    uint32_t v_stack_p38;

    v_stack_p20 = local_rbx;
    local_rsp = (local_rsp) - (160);
    result = (*(uint64_t *)(v_rip + 0x51B60D)) ^ (local_rsp);
    v_stack_m40 = result;
    v_stack_m80 = Arg1;
    if (Arg4 > 13) goto loc_008EF27D;
    if (Arg4 == 13) goto loc_008EF52F;
    Arg4 = (uint32_t)((Arg4) - (2));
    if (condition_is_equal) goto loc_008EF402;
    Arg4 = (uint32_t)((Arg4) - (1));
    if (condition_is_equal) goto loc_008EF703;
    Arg4 = (uint32_t)((Arg4) - (1));
    if (condition_is_equal) goto loc_008EF6BD;
    Arg4 = (uint32_t)((Arg4) - (5));
    if (condition_is_not_equal) goto loc_008EF2CB;
    local_rdi = 0;
    if (Arg5 != ((uint32_t)(Arg4 + 1))) goto loc_008EF21A;
    if (((*(uint32_t *)(arg6 + 0x38)) & (0x10000ULL)) != 0) goto loc_008EF1F9;
    v_stack_mA8 = *(uint64_t *)(arg6 + 0x30);
    v_stack_mB0 = *(uint64_t *)(arg6 + 0x28);
    v_stack_mB8 = *(uint64_t *)(arg6 + 0x20);
    result = PiDmObjectGetCachedCmProperty((uint32_t)(Arg3), Arg2, Arg3, (uint32_t)(*(uint32_t *)(arg6 + 0x18)));
    if (!sign_flag) goto loc_008EF2C2;
    if (((uint32_t)(result)) == 0xC0000225ULL) goto loc_008EF2C2;
    if (((uint32_t)(result)) == 0xC0000023ULL) goto loc_008EF2C2;
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0xC0000002ULL) + 50))) goto loc_008EF2C2;
loc_008EF1F9:
    if ((*(uint64_t *)(arg6 + 0x10)) != 0) goto loc_008EF253;
    result = _CmMapCmObjectTypeToPnpObjectType((uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg2, Arg3, Arg6 + 16);
    result = PiPnpRtlCacheObjectBaseKey(v_stack_m80, Arg2, (uint32_t)((uint32_t)(result)), Arg6 + 16);
    goto loc_008EF253;
loc_008EF21A:
    if (sign_flag) goto loc_008EF33D;
    v_stack_mA8 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg6 + 0x30))));
    v_stack_mB0 = *(uint64_t *)(arg6 + 0x28);
    v_stack_mB8 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg6 + 0x20))));
loc_008EF241:
    result = PiDmObjectUpdateCachedCmProperty((uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg2, (uint32_t)((uint32_t)(result)), (uint32_t)(*(uint32_t *)(arg6 + 0x18)));
    goto loc_008EF251;
loc_008EF24F:
    local_rdi = 0;
loc_008EF251:
loc_008EF253:
    Arg1 = (v_stack_m40) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, (uint32_t)((uint32_t)(result)), (uint32_t)(*(uint32_t *)(arg6 + 0x18)));
    local_rsp = (local_rsp) + (160);
    return result;
loc_008EF27D:
    Arg4 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg6 + 0x18))) - (14));
    if (condition_is_equal) goto loc_008EF77E;
    Arg4 = (uint32_t)((Arg4) - (1));
    Arg4 = (uint32_t)((Arg4) - (1));
    if (condition_is_equal) goto loc_008EF35A;
    if (Arg4 != 1) goto loc_008EF253;
    if (Arg5 != Arg4) goto loc_008EF253;
    if (((*(uint32_t *)(v_stack_p20 + 0x50)) & (0x10000ULL)) != 0) goto loc_008EF253;
    result = PiPnpRtlGetFilteredDeviceInterfaceList(v_stack_p20, Arg2, (uint32_t)((uint32_t)(result)), Arg4);
loc_008EF2BB:
    if (((uint32_t)(result)) == 0xC0000016ULL) goto loc_008EF24F;
loc_008EF2C2:
    *(uint32_t *)(v_stack_p20) = (uint32_t)(result);
    goto loc_008EF253;
loc_008EF2CB:
    if (Arg4 != 1) goto loc_008EF253;
    local_rdi = 0;
    if (Arg5 == Arg4) goto loc_008EF384;
    if ((*(uint32_t *)(v_stack_p20)) >= 0) goto loc_008EF5FE;
loc_008EF2E8:
    if (((uint32_t)((uint32_t)(Arg3))) != ((uint32_t)((uint32_t)(Arg4)))) goto loc_008EF253;
    if ((*(uint32_t *)(v_stack_p20 + 0x18)) != 9) goto loc_008EF253;
    if ((*(uint32_t *)(v_stack_p20)) < 0) goto loc_008EF330;
    if (*(uint64_t *)(*(uint64_t *)(v_stack_p20 + 0x8)) == 0) goto loc_008EF330;
    if (*(uint64_t *)(*(uint64_t *)(v_stack_p20 + 0x8) + 0x8) != 0) {
        Arg4 = 0;
        Arg1 = 4;
        result = PiDmListRemoveObject(Arg1, *(uint64_t *)(*(uint64_t *)(v_stack_p20 + 0x8) + 0x8), *(uint64_t *)(*(uint64_t *)(v_stack_p20 + 0x8)), Arg4);
    }
    if (*(uint64_t *)(*(uint64_t *)(v_stack_p20 + 0x8) + 0x10) != 0) goto loc_008EF6AB;
loc_008EF330:
    result = PiPnpRtlFreeInstallerClassChangeInfo(*(uint64_t *)(v_stack_p20 + 0x8), *(uint64_t *)(*(uint64_t *)(v_stack_p20 + 0x8) + 0x10), *(uint64_t *)(*(uint64_t *)(v_stack_p20 + 0x8)), Arg4);
    goto loc_008EF253;
loc_008EF33D:
    if (((uint32_t)(result)) != 0xC0000225ULL) goto loc_008EF251;
    v_stack_p30 = 0;
    v_stack_p28 = 0;
    v_stack_p20 = 0;
    goto loc_008EF241;
loc_008EF35A:
    if (Arg5 != 1) goto loc_008EF253;
    if (((*(uint32_t *)(4 + 0x48)) & (0x10000ULL)) != 0) goto loc_008EF253;
    result = PiPnpRtlGetFilteredDeviceList(4, *(uint64_t *)(*(uint64_t *)(v_stack_p20 + 0x8) + 0x10), *(uint64_t *)(*(uint64_t *)(v_stack_p20 + 0x8)), Arg4);
    goto loc_008EF2BB;
loc_008EF384:
    if (((*(uint32_t *)(4 + 0x2C)) & (0x20000ULL)) != 0) goto loc_008EF3AD;
    v_stack_m78 = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(4 + 0x28))) != 0) goto loc_008EF436;
loc_008EF3A0:
    if ((*(uint32_t *)(4 + 0x28)) == 0) goto loc_008EF455;
loc_008EF3A9:
loc_008EF3AD:
    if ((*(uint64_t *)(4 + 0x10)) == 0) goto loc_008EF68E;
loc_008EF3BA:
    if (((uint32_t)((uint32_t)(Arg3))) != 1) goto loc_008EF253;
    if ((*(uint32_t *)(4 + 0x18)) != 9) goto loc_008EF253;
    v_stack_m80 = 0;
    result = PnpIsValidGuidString(*(uint64_t *)(4 + 0x20), *(uint64_t *)(*(uint64_t *)(v_stack_p20 + 0x8) + 0x10), *(uint64_t *)(*(uint64_t *)(v_stack_p20 + 0x8)), 4 + 16);
loc_008EF402:
    if (Arg5 != 1) goto loc_008EF5C8;
    result = _CmMapCmObjectTypeToPnpObjectType((uint32_t)((uint32_t)((uint32_t)(Arg3))), *(uint64_t *)(*(uint64_t *)(v_stack_p20 + 0x8) + 0x10), *(uint64_t *)(*(uint64_t *)(v_stack_p20 + 0x8)), 4 + 16);
    Arg3 = 0;
    result = PiDmAddCacheReferenceForObject((uint32_t)((uint32_t)(result)), *(uint64_t *)(*(uint64_t *)(v_stack_p20 + 0x8) + 0x10), Arg3, 4 + 16);
    *(uint32_t *)(4) = (uint32_t)(result);
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(result))) >> (31));
    local_rsi = (uint32_t)((local_rsi) & (0xC0000120ULL));
    goto loc_008EF253;
loc_008EF436:
    result = ExAllocatePool2(256, result, (uint32_t)(0x47706E50ULL), 4 + 16);
    if (result == 0) goto loc_008EF3A0;
loc_008EF455:
    v_stack_m88 = 1;
    v_stack_m50 = (uint32_t)((uint32_t)(*(uint32_t *)(4 + 0x28)));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg3)))) - (1));
    if (condition_is_equal) goto loc_008EF477;
    if (((uint32_t)(Arg1)) == 1) goto loc_008EF642;
loc_008EF470:
    goto loc_008EF513;
loc_008EF477:
    result = _CmIsDeviceRegPropWritable(Arg1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(4 + 0x18)))), v_stack_m88, 4 + 16);
    if (sign_flag) goto loc_008EF495;
    if (v_stack_m88 == 0) goto loc_008EF673;
loc_008EF495:
    v_stack_p38 = 0;
    v_stack_p30 = v_stack_m50;
    v_stack_p28 = result;
    v_stack_p20 = v_stack_m78;
    result = CmGetDeviceRegProp(*(uint64_t *)(v_rip + 0x576EF4), Arg2, *(uint64_t *)(4 + 0x10), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(4 + 0x18)))));
    if (sign_flag) goto loc_008EF4F7;
    if (v_stack_m78 != ((uint32_t)((uint32_t)(*(uint32_t *)(4 + 0x1C))))) goto loc_008EF67D;
    if (((uint32_t)((uint32_t)(v_stack_m50))) != (*(uint32_t *)(4 + 0x28))) goto loc_008EF67D;
    result = memcmp(result, *(uint64_t *)(4 + 0x20), (uint32_t)((uint32_t)((uint32_t)(v_stack_m50))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(4 + 0x18)))));
    if ((uint32_t)(result) == 0) goto loc_008EF50C;
loc_008EF4F7:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != 0xC0000225ULL) goto loc_008EF67D;
    if ((*(uint32_t *)(4 + 0x28)) != 0) goto loc_008EF470;
loc_008EF50C:
    *(uint32_t *)(4) = (uint32_t)((uint32_t)((uint32_t)(result)));
loc_008EF513:
    if (result != 0) goto loc_008EF5EC;
loc_008EF51C:
    if ((uint32_t)((uint32_t)(0xC0000120ULL)) == 0) goto loc_008EF3A9;
loc_008EF524:
    if (sign_flag) goto loc_008EF253;
    goto loc_008EF3BA;
loc_008EF52F:
    local_rdi = 0;
    if (Arg5 == 1) goto loc_008EF251;
    if (((uint32_t)((uint32_t)(Arg3))) != 5) goto loc_008EF628;
    if ((*(uint32_t *)(4)) < 0) goto loc_008EF251;
    v_stack_m50 = 0;
    v_stack_m88 = 0;
    result = PiDmObjectManagerAcquireSharedLock(v_rip + 6930566, *(uint64_t *)(4 + 0x20), (uint32_t)((uint32_t)((uint32_t)(v_stack_m50))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(4 + 0x18)))));
    result = PiDmLookupObject(v_rip + 6930538, Arg2, (uint32_t)((uint32_t)((uint32_t)(v_stack_m50))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(4 + 0x18)))));
    if (result == 0) goto loc_008EF637;
loc_008EF590:
    result = PiDmObjectManagerReleaseLock(v_rip + 6930505, Arg2, (uint32_t)((uint32_t)((uint32_t)(v_stack_m50))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(4 + 0x18)))));
    if (!sign_flag) goto loc_008EF734;
loc_008EF5A5:
    if (result != 0) {
        Arg1 = result;
        result = PiDmObjectRelease(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(v_stack_m50))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(4 + 0x18)))));
    }
    if (v_stack_m50 == 0) goto loc_008EF251;
    result = PiDmObjectRelease(v_stack_m50, Arg2, (uint32_t)((uint32_t)((uint32_t)(v_stack_m50))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(4 + 0x18)))));
    goto loc_008EF251;
loc_008EF5C8:
    local_rdi = 0;
    if ((*(uint32_t *)(4)) < 0) goto loc_008EF5D8;
loc_008EF5D8:
    result = _CmMapCmObjectTypeToPnpObjectType((uint32_t)((uint32_t)(result)), Arg2, (uint32_t)((uint32_t)((uint32_t)(v_stack_m50))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(4 + 0x18)))));
    result = PiDmRemoveCacheReferenceForObject((uint32_t)((uint32_t)(result)), Arg2, (uint32_t)((uint32_t)((uint32_t)(v_stack_m50))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(4 + 0x18)))));
    goto loc_008EF251;
loc_008EF5EC:
    result = ExFreePoolWithTag(0, (uint32_t)(0x47706E50ULL), (uint32_t)((uint32_t)((uint32_t)(v_stack_m50))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(4 + 0x18)))));
    goto loc_008EF51C;
loc_008EF5FE:
    v_stack_p30 = (uint32_t)((uint32_t)(*(uint32_t *)(4 + 0x28)));
    v_stack_p28 = *(uint64_t *)(4 + 0x20);
    v_stack_p20 = (uint32_t)((uint32_t)(*(uint32_t *)(4 + 0x1C)));
    result = PiDmObjectUpdateCachedCmProperty((uint32_t)((uint32_t)(result)), (uint32_t)(0x47706E50ULL), (uint32_t)((uint32_t)((uint32_t)(v_stack_m50))), (uint32_t)(*(uint32_t *)(4 + 0x18)));
    goto loc_008EF2E8;
loc_008EF628:
    if (((uint32_t)(result)) != 6) goto loc_008EF251;
loc_008EF637:
    goto loc_008EF590;
loc_008EF642:
    result = _CmClassPropertyRead((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(4 + 0x18)))), (uint32_t)(0x47706E50ULL), (uint32_t)((uint32_t)((uint32_t)(v_stack_m50))), (uint32_t)(*(uint32_t *)(4 + 0x18)));
    result = CmClassPropertyWrite((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(4 + 0x18)))), (uint32_t)(0x47706E50ULL), (uint32_t)((uint32_t)((uint32_t)(v_stack_m50))), (uint32_t)(*(uint32_t *)(4 + 0x18)));
loc_008EF673:
    goto loc_008EF50C;
loc_008EF67D:
    if (((uint32_t)((uint32_t)(0xC0000022ULL))) != 0xC0000022ULL) goto loc_008EF470;
    goto loc_008EF50C;
loc_008EF68E:
    result = _CmMapCmObjectTypeToPnpObjectType((uint32_t)((uint32_t)(result)), (uint32_t)(0x47706E50ULL), (uint32_t)((uint32_t)((uint32_t)(v_stack_m50))), (uint32_t)(*(uint32_t *)(4 + 0x18)));
    result = PiPnpRtlCacheObjectBaseKey((uint32_t)(0xC0000034ULL), Arg2, (uint32_t)((uint32_t)(result)), (uint32_t)(*(uint32_t *)(4 + 0x18)));
    goto loc_008EF524;
loc_008EF6AB:
    Arg4 = 0;
    result = PiDmListAddObject(4, Arg2, *(uint64_t *)(1), Arg4);
    goto loc_008EF330;
loc_008EF6BD:
    if (Arg5 != 1) goto loc_008EF253;
    if (((*(uint32_t *)(4 + 0x38)) & (0x10000ULL)) != 0) goto loc_008EF253;
    v_stack_p28 = *(uint64_t *)(4 + 0x30);
    v_stack_p20 = (uint32_t)((uint32_t)(*(uint32_t *)(4 + 0x28)));
    result = PiDmGetCmObjectListFromCache((uint32_t)((uint32_t)(result)), *(uint64_t *)(4 + 0x10), *(uint64_t *)(4 + 0x18), *(uint64_t *)(4 + 0x20));
    goto loc_008EF2BB;
loc_008EF703:
    local_rdi = 0;
    v_stack_m80 = 0;
    result = PiPnpRtlGatherDeviceDeleteInfo(Arg2, v_stack_m80, *(uint64_t *)(4 + 0x18), *(uint64_t *)(4 + 0x20));
loc_008EF734:
    result = PiDmGetObject(1, *(uint64_t *)(4 + 0x18), v_stack_m50, *(uint64_t *)(4 + 0x20));
    if (sign_flag) goto loc_008EF5A5;
    result = PiDmListAddObject(3, result, v_stack_m50, v_stack_m88);
    if (v_stack_m88 != 0) goto loc_008EF5A5;
    result = PiDmListAddList(3, result, v_stack_m50, v_stack_m50);
    goto loc_008EF5A5;
loc_008EF77E:
    local_rdi = 0;
    v_stack_m80 = 0;
    result = PiPnpRtlGatherContainerRemoveInfo(*(uint64_t *)(4 + 0x18), result, v_stack_m80, v_stack_m50);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg6` | `+ 0x0` | `32` | `R` |
| `Arg6` | `+ 0x0` | `32` | `W` |
| `Arg6` | `+ 0x0` | `64` | `R` |
| `Arg6` | `+ 0x8` | `64` | `R` |
| `Arg6` | `+ 0x10` | `64` | `R` |
| `Arg6` | `+ 0x18` | `32` | `R` |
| `Arg6` | `+ 0x18` | `64` | `R` |
| `Arg6` | `+ 0x1C` | `32` | `R` |
| `Arg6` | `+ 0x20` | `8` | `R` |
| `Arg6` | `+ 0x20` | `64` | `R` |
| `Arg6` | `+ 0x28` | `32` | `R` |
| `Arg6` | `+ 0x28` | `64` | `R` |
| `Arg6` | `+ 0x2C` | `32` | `R` |
| `Arg6` | `+ 0x30` | `64` | `R` |
| `Arg6` | `+ 0x38` | `32` | `R` |
| `Arg6` | `+ 0x48` | `32` | `R` |
| `Arg6` | `+ 0x50` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008EF110&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
