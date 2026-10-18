# sub_00B1DC0E

- RVA: `0x00B1DC0E`–`0x00B1E10A` (길이 `1,276` bytes)
- VA: `0x0000000140B1DC0E`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00087024`
- 디코드: `336`개 명령, `1,276/1,276` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **37**; 고유 호출 대상: **25**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x00B1DC33` → [CmGetInstallerClassRegProp](../99/CmGetInstallerClassRegProp_function_00994940.md) (function, `0x00994940`)
- `0x00B1DC48` → [PiPnpRtlGatherInstallerClassChangeInfo](../AD/PiPnpRtlGatherInstallerClassChangeInfo_function_00AD26FC.md) (function, `0x00AD26FC`)
- `0x00B1DC7B` → [PiPnpRtlGatherInterfaceDeleteInfo](../72/PiPnpRtlGatherInterfaceDeleteInfo_function_0072FD48.md) (function, `0x0072FD48`)
- `0x00B1DC90` → [PiPnpRtlGatherPanelRemoveInfo](../72/PiPnpRtlGatherPanelRemoveInfo_function_0072FFF8.md) (function, `0x0072FFF8`)
- `0x00B1DCD1` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00B1DCDE` → [RtlGUIDFromString](../8F/RtlGUIDFromString_function_008F1EF0.md) (function, `0x008F1EF0`)
- `0x00B1DCFF` → [PnpIsNullGuid](../8D/PnpIsNullGuid_function_008DD9E0.md) (function, `0x008DD9E0`)
- `0x00B1DD1A` → [PnpIsNullGuid](../8D/PnpIsNullGuid_function_008DD9E0.md) (function, `0x008DD9E0`)
- `0x00B1DD44` → [McTemplateK0zjdd_EtwWriteTransfer](../../text/5A/McTemplateK0zjdd_EtwWriteTransfer_function_005A7BDC.md) (function, `0x005A7BDC`)
- `0x00B1DDA8` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00B1DDB0` → [CmIsRootEnumeratedDevice](../8F/CmIsRootEnumeratedDevice_function_008F6E08.md) (function, `0x008F6E08`)
- `0x00B1DDC0` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00B1DDDD` → [PnpDeviceObjectFromDeviceInstanceWithTag](../8E/PnpDeviceObjectFromDeviceInstanceWithTag_function_008E7490.md) (function, `0x008E7490`)
- `0x00B1DDF6` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00B1DDFE` → [PiPnpRtlFreeDeviceDeleteInfo](../72/PiPnpRtlFreeDeviceDeleteInfo_function_0072FAD8.md) (function, `0x0072FAD8`)
- `0x00B1DE31` → [PiDmListRemoveObject](../70/PiDmListRemoveObject_function_007045E8.md) (function, `0x007045E8`)
- `0x00B1DE48` → [PiDmListRemoveObject](../70/PiDmListRemoveObject_function_007045E8.md) (function, `0x007045E8`)
- `0x00B1DE60` → [PiDmListRemoveObject](../70/PiDmListRemoveObject_function_007045E8.md) (function, `0x007045E8`)
- `0x00B1DE68` → [PiPnpRtlFreeInterfaceDeleteInfo](../72/PiPnpRtlFreeInterfaceDeleteInfo_function_0072FAF8.md) (function, `0x0072FAF8`)
- `0x00B1DE7A` → [_CmMapCmObjectTypeToPnpObjectType](../8F/_CmMapCmObjectTypeToPnpObjectType_function_008FF060.md) (function, `0x008FF060`)
- `0x00B1DE88` → [PiDmGetObject](../8D/PiDmGetObject_function_008DFAE0.md) (function, `0x008DFAE0`)
- `0x00B1DE9C` → [CmpLockSiloKeyLockTrackerExclusive](../8F/CmpLockSiloKeyLockTrackerExclusive_function_008F9EF8.md) (function, `0x008F9EF8`)
- `0x00B1DEAF` → [PiDmObjectReleaseLock](../8E/PiDmObjectReleaseLock_function_008E5584.md) (function, `0x008E5584`)
- `0x00B1DEC3` → [PiDmRemoveCacheReferenceForObject](../95/PiDmRemoveCacheReferenceForObject_function_00950F24.md) (function, `0x00950F24`)
- `0x00B1DEEA` → [PiDmGetObject](../8D/PiDmGetObject_function_008DFAE0.md) (function, `0x008DFAE0`)
- `0x00B1DF06` → [PiDmGetObject](../8D/PiDmGetObject_function_008DFAE0.md) (function, `0x008DFAE0`)
- `0x00B1DF26` → [PiDmListAddObject](../95/PiDmListAddObject_function_00950128.md) (function, `0x00950128`)
- `0x00B1DF70` → [PiDmGetObject](../8D/PiDmGetObject_function_008DFAE0.md) (function, `0x008DFAE0`)
- `0x00B1DFBC` → [PiDmListEnumObjectsWithCallback](../8E/PiDmListEnumObjectsWithCallback_function_008E3B60.md) (function, `0x008E3B60`)
- `0x00B1E001` → [PiDmGetObject](../8D/PiDmGetObject_function_008DFAE0.md) (function, `0x008DFAE0`)
- `0x00B1E045` → [PiDmListEnumObjectsWithCallback](../8E/PiDmListEnumObjectsWithCallback_function_008E3B60.md) (function, `0x008E3B60`)
- `0x00B1E05F` → [PiDmObjectRelease](../8E/PiDmObjectRelease_function_008E4F70.md) (function, `0x008E4F70`)
- `0x00B1E0A7` → [PiDmListRemoveObject](../70/PiDmListRemoveObject_function_007045E8.md) (function, `0x007045E8`)
- `0x00B1E0B9` → [PiDmListRemoveList](../73/PiDmListRemoveList_function_00730474.md) (function, `0x00730474`)
- `0x00B1E0C1` → [PiPnpRtlFreeContainerRemoveInfo](../72/PiPnpRtlFreeContainerRemoveInfo_function_0072FA94.md) (function, `0x0072FA94`)
- `0x00B1E0F7` → [PiDmListRemoveObject](../70/PiDmListRemoveObject_function_007045E8.md) (function, `0x007045E8`)
- `0x00B1E0FF` → [PiPnpRtlFreeContainerRemoveInfo](../72/PiPnpRtlFreeContainerRemoveInfo_function_0072FA94.md) (function, `0x0072FA94`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00B1DC16` → RVA `0x00E66398` (`.data`; read)
- `0x00B1DCF2` → RVA `0x00EF012A` (`.data`; read)
- `0x00B1DD04` → RVA `0x00027310` (`.rdata`; read)
- `0x00B1DD1F` → RVA `0x00027020` (`.rdata`; read)
- `0x00B1DD8F` → RVA `0x00022AE0` (`.rdata`; read)
- `0x00B1DFAD` → RVA `0x0072FA20` (`PiPnpRtlEnumDevicesCallback`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x00B1DCD1` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00B1DD44` → [McTemplateK0zjdd_EtwWriteTransfer](../../text/5A/McTemplateK0zjdd_EtwWriteTransfer_function_005A7BDC.md) (`PAGE` → `.text`)
  - `0x00B1DDC0` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00B1DDF6` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **25**
  - `0x00B1DC39` → [PiPnpRtlCmActionCallback + 0x3B6](../8E/PiPnpRtlCmActionCallback_function_008EF110.md) (`tail-transfer`)
  - `0x00B1DC51` → [PiPnpRtlCmActionCallback + 0x1B2](../8E/PiPnpRtlCmActionCallback_function_008EF110.md) (`tail-transfer`)
  - `0x00B1DC5F` → [PiPnpRtlCmActionCallback + 0x143](../8E/PiPnpRtlCmActionCallback_function_008EF110.md) (`tail-transfer`)
  - `0x00B1DC68` → [PiPnpRtlCmActionCallback + 0x143](../8E/PiPnpRtlCmActionCallback_function_008EF110.md) (`tail-transfer`)
  - `0x00B1DC99` → [PiPnpRtlCmActionCallback + 0x1B2](../8E/PiPnpRtlCmActionCallback_function_008EF110.md) (`tail-transfer`)
  - `0x00B1DCA7` → [PiPnpRtlCmActionCallback + 0x143](../8E/PiPnpRtlCmActionCallback_function_008EF110.md) (`tail-transfer`)
  - `0x00B1DE04` → [PiPnpRtlCmActionCallback + 0x141](../8E/PiPnpRtlCmActionCallback_function_008EF110.md) (`tail-transfer`)
  - `0x00B1DE0D` → [PiPnpRtlCmActionCallback + 0x141](../8E/PiPnpRtlCmActionCallback_function_008EF110.md) (`tail-transfer`)
  - `0x00B1DE6E` → [PiPnpRtlCmActionCallback + 0x141](../8E/PiPnpRtlCmActionCallback_function_008EF110.md) (`tail-transfer`)
  - `0x00B1DE8F` → [PiPnpRtlCmActionCallback + 0x141](../8E/PiPnpRtlCmActionCallback_function_008EF110.md) (`tail-transfer`)
  - `0x00B1DEB7` → [PiPnpRtlCmActionCallback + 0x4AB](../8E/PiPnpRtlCmActionCallback_function_008EF110.md) (`tail-transfer`)
  - `0x00B1DEC9` → [PiPnpRtlCmActionCallback + 0x4AB](../8E/PiPnpRtlCmActionCallback_function_008EF110.md) (`tail-transfer`)
  - `0x00B1DED0` → [PiPnpRtlCmActionCallback + 0x141](../8E/PiPnpRtlCmActionCallback_function_008EF110.md) (`tail-transfer`)
  - `0x00B1DEF5` → [PiPnpRtlCmActionCallback + 0x495](../8E/PiPnpRtlCmActionCallback_function_008EF110.md) (`tail-transfer`)
  - `0x00B1DF11` → [PiPnpRtlCmActionCallback + 0x495](../8E/PiPnpRtlCmActionCallback_function_008EF110.md) (`tail-transfer`)
  - `0x00B1DF2C` → [PiPnpRtlCmActionCallback + 0x495](../8E/PiPnpRtlCmActionCallback_function_008EF110.md) (`tail-transfer`)
  - `0x00B1DF3B` → [PiPnpRtlCmActionCallback + 0x143](../8E/PiPnpRtlCmActionCallback_function_008EF110.md) (`tail-transfer`)
  - `0x00B1DF52` → [PiPnpRtlCmActionCallback + 0x143](../8E/PiPnpRtlCmActionCallback_function_008EF110.md) (`tail-transfer`)
  - `0x00B1DFD6` → [PiPnpRtlCmActionCallback + 0x143](../8E/PiPnpRtlCmActionCallback_function_008EF110.md) (`tail-transfer`)
  - `0x00B1DFE3` → [PiPnpRtlCmActionCallback + 0x143](../8E/PiPnpRtlCmActionCallback_function_008EF110.md) (`tail-transfer`)
  - `0x00B1E067` → [PiPnpRtlCmActionCallback + 0x1B4](../8E/PiPnpRtlCmActionCallback_function_008EF110.md) (`tail-transfer`)
  - `0x00B1E070` → [PiPnpRtlCmActionCallback + 0x143](../8E/PiPnpRtlCmActionCallback_function_008EF110.md) (`tail-transfer`)
  - `0x00B1E0C7` → [PiPnpRtlCmActionCallback + 0x141](../8E/PiPnpRtlCmActionCallback_function_008EF110.md) (`tail-transfer`)
  - `0x00B1E0D0` → [PiPnpRtlCmActionCallback + 0x141](../8E/PiPnpRtlCmActionCallback_function_008EF110.md) (`tail-transfer`)
  - `0x00B1E105` → [PiPnpRtlCmActionCallback + 0x141](../8E/PiPnpRtlCmActionCallback_function_008EF110.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B1DC0E  4C 8B 43 10                     mov r8, qword ptr [rbx + 0x10]
00B1DC12  48 8D 45 FF                     lea rax, [rbp - 1]
00B1DC16  48 8B 0D 7B 87 34 00            mov rcx, qword ptr [rip + 0x34877b]
00B1DC1D  49 8B D4                        mov rdx, r12
00B1DC20  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00B1DC25  48 8D 45 D7                     lea rax, [rbp - 0x29]
00B1DC29  4C 89 6C 24 28                  mov qword ptr [rsp + 0x28], r13
00B1DC2E  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00B1DC33  E8 08 6D E7 FF                  call 0x140994940
00B1DC38  90                              nop
00B1DC39  E9 88 18 DD FF                  jmp 0x1408ef4c6
00B1DC3E  4C 8D 45 CF                     lea r8, [rbp - 0x31]
00B1DC42  48 8B D6                        mov rdx, rsi
00B1DC45  49 8B CC                        mov rcx, r12
00B1DC48  E8 AF 4A FB FF                  call 0x140ad26fc
00B1DC4D  8B F0                           mov esi, eax
00B1DC4F  85 C0                           test eax, eax
00B1DC51  0F 88 6B 16 DD FF               js 0x1408ef2c2
00B1DC57  48 8B 4D CF                     mov rcx, qword ptr [rbp - 0x31]
00B1DC5B  48 89 4B 08                     mov qword ptr [rbx + 8], rcx
00B1DC5F  E9 EF 15 DD FF                  jmp 0x1408ef253
00B1DC64  41 83 FF 03                     cmp r15d, 3
00B1DC68  0F 85 E5 15 DD FF               jne 0x1408ef253
00B1DC6E  33 FF                           xor edi, edi
00B1DC70  48 8D 55 CF                     lea rdx, [rbp - 0x31]
00B1DC74  49 8B CC                        mov rcx, r12
00B1DC77  48 89 7D CF                     mov qword ptr [rbp - 0x31], rdi
00B1DC7B  E8 C8 20 C1 FF                  call 0x14072fd48
00B1DC80  EB 13                           jmp 0x140b1dc95
00B1DC82  48 8B 4B 18                     mov rcx, qword ptr [rbx + 0x18]
00B1DC86  4C 8D 45 CF                     lea r8, [rbp - 0x31]
00B1DC8A  33 FF                           xor edi, edi
00B1DC8C  48 89 7D CF                     mov qword ptr [rbp - 0x31], rdi
00B1DC90  E8 63 23 C1 FF                  call 0x14072fff8
00B1DC95  8B F0                           mov esi, eax
00B1DC97  85 C0                           test eax, eax
00B1DC99  0F 88 23 16 DD FF               js 0x1408ef2c2
00B1DC9F  48 8B 45 CF                     mov rax, qword ptr [rbp - 0x31]
00B1DCA3  48 89 43 08                     mov qword ptr [rbx + 8], rax
00B1DCA7  E9 A7 15 DD FF                  jmp 0x1408ef253
00B1DCAC  33 FF                           xor edi, edi
00B1DCAE  45 3B FE                        cmp r15d, r14d
00B1DCB1  0F 85 52 01 00 00               jne 0x140b1de09
00B1DCB7  48 8B 73 08                     mov rsi, qword ptr [rbx + 8]
00B1DCBB  48 8D 4D DF                     lea rcx, [rbp - 0x21]
00B1DCBF  0F 57 C0                        xorps xmm0, xmm0
00B1DCC2  0F 57 C9                        xorps xmm1, xmm1
00B1DCC5  0F 11 45 DF                     movups xmmword ptr [rbp - 0x21], xmm0
00B1DCC9  48 8D 56 04                     lea rdx, [rsi + 4]
00B1DCCD  0F 11 4D FF                     movups xmmword ptr [rbp - 1], xmm1
00B1DCD1  E8 AA CA 90 FF                  call 0x14042a780
00B1DCD6  48 8D 55 FF                     lea rdx, [rbp - 1]
00B1DCDA  48 8D 4D DF                     lea rcx, [rbp - 0x21]
00B1DCDE  E8 0D 42 DD FF                  call 0x1408f1ef0
00B1DCE3  85 C0                           test eax, eax
00B1DCE5  79 07                           jns 0x140b1dcee
00B1DCE7  0F 57 C0                        xorps xmm0, xmm0
00B1DCEA  0F 11 45 FF                     movups xmmword ptr [rbp - 1], xmm0
00B1DCEE  39 3B                           cmp dword ptr [rbx], edi
00B1DCF0  7C 1B                           jl 0x140b1dd0d
00B1DCF2  F6 05 31 24 3D 00 10            test byte ptr [rip + 0x3d2431], 0x10
00B1DCF9  74 4E                           je 0x140b1dd49
00B1DCFB  48 8D 4D FF                     lea rcx, [rbp - 1]
00B1DCFF  E8 DC FC DB FF                  call 0x1408dd9e0
00B1DD04  48 8D 15 05 96 50 FF            lea rdx, [rip - 0xaf69fb]
00B1DD0B  EB 19                           jmp 0x140b1dd26
00B1DD0D  F6 05 16 24 3D 00 20            test byte ptr [rip + 0x3d2416], 0x20
00B1DD14  74 33                           je 0x140b1dd49
00B1DD16  48 8D 4D FF                     lea rcx, [rbp - 1]
00B1DD1A  E8 C1 FC DB FF                  call 0x1408dd9e0
00B1DD1F  48 8D 15 FA 92 50 FF            lea rdx, [rip - 0xaf6d06]
00B1DD26  84 C0                           test al, al
00B1DD28  48 8D 4D FF                     lea rcx, [rbp - 1]
00B1DD2C  8B 03                           mov eax, dword ptr [rbx]
00B1DD2E  4D 8B CC                        mov r9, r12
00B1DD31  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00B1DD35  48 0F 45 CF                     cmovne rcx, rdi
00B1DD39  8B 06                           mov eax, dword ptr [rsi]
00B1DD3B  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00B1DD3F  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00B1DD44  E8 93 9E A8 FF                  call 0x1405a7bdc
00B1DD49  39 3B                           cmp dword ptr [rbx], edi
00B1DD4B  0F 8C AA 00 00 00               jl 0x140b1ddfb
00B1DD51  BB 02 00 00 00                  mov ebx, 2
00B1DD56  66 39 7E 04                     cmp word ptr [rsi + 4], di
00B1DD5A  74 51                           je 0x140b1ddad
00B1DD5C  89 7C 24 48                     mov dword ptr [rsp + 0x48], edi
00B1DD60  48 8D 56 04                     lea rdx, [rsi + 4]
00B1DD64  C7 44 24 40 08 00 00 00         mov dword ptr [rsp + 0x40], 8
00B1DD6C  48 B8 14 00 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000014
00B1DD76  45 33 C9                        xor r9d, r9d
00B1DD79  44 8B C3                        mov r8d, ebx
00B1DD7C  49 8B CD                        mov rcx, r13
00B1DD7F  48 8B 00                        mov rax, qword ptr [rax]
00B1DD82  48 89 45 CF                     mov qword ptr [rbp - 0x31], rax
00B1DD86  48 8D 45 CF                     lea rax, [rbp - 0x31]
00B1DD8A  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00B1DD8F  48 8D 05 4A 4D 50 FF            lea rax, [rip - 0xafb2b6]
00B1DD96  C7 44 24 30 10 00 00 00         mov dword ptr [rsp + 0x30], 0x10
00B1DD9E  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B1DDA3  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00B1DDA8  E8 3B 89 DD FF                  call 0x1408f66e8
00B1DDAD  49 8B CC                        mov rcx, r12
00B1DDB0  E8 53 90 DD FF                  call 0x1408f6e08
00B1DDB5  84 C0                           test al, al
00B1DDB7  74 42                           je 0x140b1ddfb
00B1DDB9  49 8B D4                        mov rdx, r12
00B1DDBC  48 8D 4D DF                     lea rcx, [rbp - 0x21]
00B1DDC0  E8 BB C9 90 FF                  call 0x14042a780
00B1DDC5  66 39 5D DF                     cmp word ptr [rbp - 0x21], bx
00B1DDC9  72 30                           jb 0x140b1ddfb
00B1DDCB  48 8B 45 E7                     mov rax, qword ptr [rbp - 0x19]
00B1DDCF  66 39 38                        cmp word ptr [rax], di
00B1DDD2  74 27                           je 0x140b1ddfb
00B1DDD4  BA 44 66 6C 74                  mov edx, 0x746c6644
00B1DDD9  48 8D 4D DF                     lea rcx, [rbp - 0x21]
00B1DDDD  E8 AE 96 DC FF                  call 0x1408e7490
00B1DDE2  48 85 C0                        test rax, rax
00B1DDE5  74 14                           je 0x140b1ddfb
00B1DDE7  48 8B 50 40                     mov rdx, qword ptr [rax + 0x40]
00B1DDEB  48 85 D2                        test rdx, rdx
00B1DDEE  74 03                           je 0x140b1ddf3
00B1DDF0  44 09 32                        or dword ptr [rdx], r14d
00B1DDF3  48 8B C8                        mov rcx, rax
00B1DDF6  E8 55 B5 7D FF                  call 0x1402f9350
00B1DDFB  48 8B CE                        mov rcx, rsi
00B1DDFE  E8 D5 1C C1 FF                  call 0x14072fad8
00B1DE03  90                              nop
00B1DE04  E9 48 14 DD FF                  jmp 0x1408ef251
00B1DE09  41 83 FF 03                     cmp r15d, 3
00B1DE0D  0F 85 3E 14 DD FF               jne 0x1408ef251
00B1DE13  48 8B 73 08                     mov rsi, qword ptr [rbx + 8]
00B1DE17  39 3B                           cmp dword ptr [rbx], edi
00B1DE19  7C 4A                           jl 0x140b1de65
00B1DE1B  4C 8B 06                        mov r8, qword ptr [rsi]
00B1DE1E  4D 85 C0                        test r8, r8
00B1DE21  74 42                           je 0x140b1de65
00B1DE23  48 8B 56 08                     mov rdx, qword ptr [rsi + 8]
00B1DE27  48 85 D2                        test rdx, rdx
00B1DE2A  74 0A                           je 0x140b1de36
00B1DE2C  45 33 C9                        xor r9d, r9d
00B1DE2F  33 C9                           xor ecx, ecx
00B1DE31  E8 B2 67 BE FF                  call 0x1407045e8
00B1DE36  48 8B 56 10                     mov rdx, qword ptr [rsi + 0x10]
00B1DE3A  48 85 D2                        test rdx, rdx
00B1DE3D  74 0E                           je 0x140b1de4d
00B1DE3F  4C 8B 06                        mov r8, qword ptr [rsi]
00B1DE42  45 33 C9                        xor r9d, r9d
00B1DE45  41 8B CE                        mov ecx, r14d
00B1DE48  E8 9B 67 BE FF                  call 0x1407045e8
00B1DE4D  48 8B 56 18                     mov rdx, qword ptr [rsi + 0x18]
00B1DE51  48 85 D2                        test rdx, rdx
00B1DE54  74 0F                           je 0x140b1de65
00B1DE56  4C 8B 06                        mov r8, qword ptr [rsi]
00B1DE59  45 33 C9                        xor r9d, r9d
00B1DE5C  41 8D 49 02                     lea ecx, [r9 + 2]
00B1DE60  E8 83 67 BE FF                  call 0x1407045e8
00B1DE65  48 8B CE                        mov rcx, rsi
00B1DE68  E8 8B 1C C1 FF                  call 0x14072faf8
00B1DE6D  90                              nop
00B1DE6E  E9 DE 13 DD FF                  jmp 0x1408ef251
00B1DE73  41 8B CF                        mov ecx, r15d
00B1DE76  48 89 7D CF                     mov qword ptr [rbp - 0x31], rdi
00B1DE7A  E8 E1 11 DE FF                  call 0x1408ff060
00B1DE7F  8B C8                           mov ecx, eax
00B1DE81  4C 8D 45 CF                     lea r8, [rbp - 0x31]
00B1DE85  44 8B F8                        mov r15d, eax
00B1DE88  E8 53 1C DC FF                  call 0x1408dfae0
00B1DE8D  85 C0                           test eax, eax
00B1DE8F  0F 88 BC 13 DD FF               js 0x1408ef251
00B1DE95  48 8B 75 CF                     mov rsi, qword ptr [rbp - 0x31]
00B1DE99  48 8B CE                        mov rcx, rsi
00B1DE9C  E8 57 C0 DD FF                  call 0x1408f9ef8
00B1DEA1  8B 5E 20                        mov ebx, dword ptr [rsi + 0x20]
00B1DEA4  48 8B CE                        mov rcx, rsi
00B1DEA7  8B D3                           mov edx, ebx
00B1DEA9  41 0B D6                        or edx, r14d
00B1DEAC  89 56 20                        mov dword ptr [rsi + 0x20], edx
00B1DEAF  E8 D0 76 DC FF                  call 0x1408e5584
00B1DEB4  41 84 DE                        test r14b, bl
00B1DEB7  0F 84 FE 16 DD FF               je 0x1408ef5bb
00B1DEBD  49 8B D4                        mov rdx, r12
00B1DEC0  41 8B CF                        mov ecx, r15d
00B1DEC3  E8 5C 30 E3 FF                  call 0x140950f24
00B1DEC8  90                              nop
00B1DEC9  E9 ED 16 DD FF                  jmp 0x1408ef5bb
00B1DECE  39 3B                           cmp dword ptr [rbx], edi
00B1DED0  0F 8C 7B 13 DD FF               jl 0x1408ef251
00B1DED6  4C 8D 45 FF                     lea r8, [rbp - 1]
00B1DEDA  48 89 7D FF                     mov qword ptr [rbp - 1], rdi
00B1DEDE  B9 06 00 00 00                  mov ecx, 6
00B1DEE3  48 89 7D CF                     mov qword ptr [rbp - 0x31], rdi
00B1DEE7  48 8B F7                        mov rsi, rdi
00B1DEEA  E8 F1 1B DC FF                  call 0x1408dfae0
00B1DEEF  4C 8B 7D FF                     mov r15, qword ptr [rbp - 1]
00B1DEF3  85 C0                           test eax, eax
00B1DEF5  0F 88 AA 16 DD FF               js 0x1408ef5a5
00B1DEFB  48 8B 53 18                     mov rdx, qword ptr [rbx + 0x18]
00B1DEFF  4C 8D 45 CF                     lea r8, [rbp - 0x31]
00B1DF03  41 8B CE                        mov ecx, r14d
00B1DF06  E8 D5 1B DC FF                  call 0x1408dfae0
00B1DF0B  48 8B 75 CF                     mov rsi, qword ptr [rbp - 0x31]
00B1DF0F  85 C0                           test eax, eax
00B1DF11  0F 88 8E 16 DD FF               js 0x1408ef5a5
00B1DF17  4C 8D 4D C7                     lea r9, [rbp - 0x39]
00B1DF1B  4C 8B C6                        mov r8, rsi
00B1DF1E  49 8B D7                        mov rdx, r15
00B1DF21  B9 05 00 00 00                  mov ecx, 5
00B1DF26  E8 FD 21 E3 FF                  call 0x140950128
00B1DF2B  90                              nop
00B1DF2C  E9 74 16 DD FF                  jmp 0x1408ef5a5
00B1DF31  41 BE 01 00 00 00               mov r14d, 1
00B1DF37  44 39 75 77                     cmp dword ptr [rbp + 0x77], r14d
00B1DF3B  0F 85 12 13 DD FF               jne 0x1408ef253
00B1DF41  41 83 FF 05                     cmp r15d, 5
00B1DF45  0F 85 87 00 00 00               jne 0x140b1dfd2
00B1DF4B  F7 43 28 00 00 01 00            test dword ptr [rbx + 0x28], 0x10000
00B1DF52  0F 85 FB 12 DD FF               jne 0x1408ef253
00B1DF58  33 FF                           xor edi, edi
00B1DF5A  4C 8D 45 CF                     lea r8, [rbp - 0x31]
00B1DF5E  41 8B CF                        mov ecx, r15d
00B1DF61  89 7D F8                        mov dword ptr [rbp - 8], edi
00B1DF64  66 89 7D FC                     mov word ptr [rbp - 4], di
00B1DF68  40 88 7D FE                     mov byte ptr [rbp - 2], dil
00B1DF6C  48 89 7D CF                     mov qword ptr [rbp - 0x31], rdi
00B1DF70  E8 6B 1B DC FF                  call 0x1408dfae0
00B1DF75  44 8B F8                        mov r15d, eax
00B1DF78  85 C0                           test eax, eax
00B1DF7A  0F 88 E4 00 00 00               js 0x140b1e064
00B1DF80  48 8B 4B 18                     mov rcx, qword ptr [rbx + 0x18]
00B1DF84  48 8B 75 CF                     mov rsi, qword ptr [rbp - 0x31]
00B1DF88  48 89 4D E7                     mov qword ptr [rbp - 0x19], rcx
00B1DF8C  48 8B 4B 20                     mov rcx, qword ptr [rbx + 0x20]
00B1DF90  48 89 4D EF                     mov qword ptr [rbp - 0x11], rcx
00B1DF94  4C 89 6D DF                     mov qword ptr [rbp - 0x21], r13
00B1DF98  44 88 75 F7                     mov byte ptr [rbp - 9], r14b
00B1DF9C  45 84 F6                        test r14b, r14b
00B1DF9F  0F 84 B2 00 00 00               je 0x140b1e057
00B1DFA5  4C 8D 4D DF                     lea r9, [rbp - 0x21]
00B1DFA9  40 88 7D F7                     mov byte ptr [rbp - 9], dil
00B1DFAD  4C 8D 05 6C 1A C1 FF            lea r8, [rip - 0x3ee594]
00B1DFB4  48 8B D6                        mov rdx, rsi
00B1DFB7  B9 03 00 00 00                  mov ecx, 3
00B1DFBC  E8 9F 5B DC FF                  call 0x1408e3b60
00B1DFC1  44 8B F8                        mov r15d, eax
00B1DFC4  85 C0                           test eax, eax
00B1DFC6  0F 88 8B 00 00 00               js 0x140b1e057
00B1DFCC  44 8A 75 F7                     mov r14b, byte ptr [rbp - 9]
00B1DFD0  EB CA                           jmp 0x140b1df9c
00B1DFD2  41 83 FF 06                     cmp r15d, 6
00B1DFD6  0F 85 77 12 DD FF               jne 0x1408ef253
00B1DFDC  F7 43 28 00 00 01 00            test dword ptr [rbx + 0x28], 0x10000
00B1DFE3  0F 85 6A 12 DD FF               jne 0x1408ef253
00B1DFE9  33 FF                           xor edi, edi
00B1DFEB  4C 8D 45 CF                     lea r8, [rbp - 0x31]
00B1DFEF  41 8B CF                        mov ecx, r15d
00B1DFF2  89 7D F8                        mov dword ptr [rbp - 8], edi
00B1DFF5  66 89 7D FC                     mov word ptr [rbp - 4], di
00B1DFF9  40 88 7D FE                     mov byte ptr [rbp - 2], dil
00B1DFFD  48 89 7D CF                     mov qword ptr [rbp - 0x31], rdi
00B1E001  E8 DA 1A DC FF                  call 0x1408dfae0
00B1E006  44 8B F8                        mov r15d, eax
00B1E009  85 C0                           test eax, eax
00B1E00B  78 57                           js 0x140b1e064
00B1E00D  48 8B 4B 18                     mov rcx, qword ptr [rbx + 0x18]
00B1E011  48 8B 75 CF                     mov rsi, qword ptr [rbp - 0x31]
00B1E015  48 89 4D E7                     mov qword ptr [rbp - 0x19], rcx
00B1E019  48 8B 4B 20                     mov rcx, qword ptr [rbx + 0x20]
00B1E01D  48 89 4D EF                     mov qword ptr [rbp - 0x11], rcx
00B1E021  4C 89 6D DF                     mov qword ptr [rbp - 0x21], r13
00B1E025  44 88 75 F7                     mov byte ptr [rbp - 9], r14b
00B1E029  45 84 F6                        test r14b, r14b
00B1E02C  74 29                           je 0x140b1e057
00B1E02E  4C 8D 4D DF                     lea r9, [rbp - 0x21]
00B1E032  40 88 7D F7                     mov byte ptr [rbp - 9], dil
00B1E036  4C 8D 05 E3 19 C1 FF            lea r8, [rip - 0x3ee61d]
00B1E03D  48 8B D6                        mov rdx, rsi
00B1E040  B9 05 00 00 00                  mov ecx, 5
00B1E045  E8 16 5B DC FF                  call 0x1408e3b60
00B1E04A  44 8B F8                        mov r15d, eax
00B1E04D  85 C0                           test eax, eax
00B1E04F  78 06                           js 0x140b1e057
00B1E051  44 8A 75 F7                     mov r14b, byte ptr [rbp - 9]
00B1E055  EB D2                           jmp 0x140b1e029
00B1E057  48 85 F6                        test rsi, rsi
00B1E05A  74 08                           je 0x140b1e064
00B1E05C  48 8B CE                        mov rcx, rsi
00B1E05F  E8 0C 6F DC FF                  call 0x1408e4f70
00B1E064  44 89 3B                        mov dword ptr [rbx], r15d
00B1E067  E9 58 12 DD FF                  jmp 0x1408ef2c4
00B1E06C  41 83 FF 06                     cmp r15d, 6
00B1E070  0F 85 DD 11 DD FF               jne 0x1408ef253
00B1E076  E9 07 FC FF FF                  jmp 0x140b1dc82
00B1E07B  33 FF                           xor edi, edi
00B1E07D  41 83 FF 05                     cmp r15d, 5
00B1E081  75 49                           jne 0x140b1e0cc
00B1E083  48 8B 73 08                     mov rsi, qword ptr [rbx + 8]
00B1E087  39 3B                           cmp dword ptr [rbx], edi
00B1E089  7C 33                           jl 0x140b1e0be
00B1E08B  48 8B 56 08                     mov rdx, qword ptr [rsi + 8]
00B1E08F  40 88 7D C7                     mov byte ptr [rbp - 0x39], dil
00B1E093  48 85 D2                        test rdx, rdx
00B1E096  74 26                           je 0x140b1e0be
00B1E098  4C 8B 06                        mov r8, qword ptr [rsi]
00B1E09B  4D 85 C0                        test r8, r8
00B1E09E  74 1E                           je 0x140b1e0be
00B1E0A0  4C 8D 4D C7                     lea r9, [rbp - 0x39]
00B1E0A4  8D 4F 03                        lea ecx, [rdi + 3]
00B1E0A7  E8 3C 65 BE FF                  call 0x1407045e8
00B1E0AC  40 38 7D C7                     cmp byte ptr [rbp - 0x39], dil
00B1E0B0  74 0C                           je 0x140b1e0be
00B1E0B2  4C 8B 0E                        mov r9, qword ptr [rsi]
00B1E0B5  48 8B 56 08                     mov rdx, qword ptr [rsi + 8]
00B1E0B9  E8 B6 23 C1 FF                  call 0x140730474
00B1E0BE  48 8B CE                        mov rcx, rsi
00B1E0C1  E8 CE 19 C1 FF                  call 0x14072fa94
00B1E0C6  90                              nop
00B1E0C7  E9 85 11 DD FF                  jmp 0x1408ef251
00B1E0CC  41 83 FF 06                     cmp r15d, 6
00B1E0D0  0F 85 7B 11 DD FF               jne 0x1408ef251
00B1E0D6  48 8B 73 08                     mov rsi, qword ptr [rbx + 8]
00B1E0DA  39 3B                           cmp dword ptr [rbx], edi
00B1E0DC  7C 1E                           jl 0x140b1e0fc
00B1E0DE  48 8B 56 08                     mov rdx, qword ptr [rsi + 8]
00B1E0E2  48 85 D2                        test rdx, rdx
00B1E0E5  74 15                           je 0x140b1e0fc
00B1E0E7  4C 8B 06                        mov r8, qword ptr [rsi]
00B1E0EA  4D 85 C0                        test r8, r8
00B1E0ED  74 0D                           je 0x140b1e0fc
00B1E0EF  4C 8D 4D C7                     lea r9, [rbp - 0x39]
00B1E0F3  41 8D 4F FF                     lea ecx, [r15 - 1]
00B1E0F7  E8 EC 64 BE FF                  call 0x1407045e8
00B1E0FC  48 8B CE                        mov rcx, rsi
00B1E0FF  E8 90 19 C1 FF                  call 0x14072fa94
00B1E104  90                              nop
00B1E105  E9 47 11 DD FF                  jmp 0x1408ef251
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00B1DC0E(void)
{
    __int64 result;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned int v_stack_p40;
    unsigned int v_stack_p48;

    v_stack_p30 = v_rbp - 1;
    v_stack_p28 = v_r13;
    v_stack_p20 = v_rbp - 41;
    result = CmGetInstallerClassRegProp(*(unsigned __int64 *)(v_rip + 3442555), v_r12, *(unsigned __int64 *)(v_rbx + 16), a4);
}
```

## 5. (Beta) C Style

```c
void sub_00B1DC0E(void)
{
    int64_t result;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint32_t v_stack_p40;
    uint32_t v_stack_p48;

    v_stack_p30 = local_rbp - 1;
    v_stack_p28 = local_r13;
    v_stack_p20 = local_rbp - 41;
    result = CmGetInstallerClassRegProp(*(uint64_t *)(v_rip + 0x34877B), local_r12, *(uint64_t *)(local_rbx + 0x10), a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B1DC0E&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
