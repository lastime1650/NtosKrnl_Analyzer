# sub_00B33FE8

- RVA: `0x00B33FE8`–`0x00B34453` (길이 `1,131` bytes)
- VA: `0x0000000140B33FE8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A83E8`
- 디코드: `286`개 명령, `1,131/1,131` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **46**; 고유 호출 대상: **27**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00B34030` → [PnpFinalizeVetoedRemove](../A0/PnpFinalizeVetoedRemove_function_00A04968.md) (function, `0x00A04968`)
- `0x00B34065` → [PpProfileIncludeInHardwareProfileTransition](../73/PpProfileIncludeInHardwareProfileTransition_function_00737B9C.md) (function, `0x00737B9C`)
- `0x00B34080` → [IoGetLegacyVetoList](../91/IoGetLegacyVetoList_function_00911300.md) (function, `0x00911300`)
- `0x00B34099` → [PpProfileCancelHardwareProfileTransition](../73/PpProfileCancelHardwareProfileTransition_function_00737918.md) (function, `0x00737918`)
- `0x00B340A1` → [IopFreeRelationList](../A0/IopFreeRelationList_function_00A08310.md) (function, `0x00A08310`)
- `0x00B340C2` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00B340CF` → [RtlCopyUnicodeString](../../text/3F/RtlCopyUnicodeString_function_003FEF30.md) (function, `0x003FEF30`)
- `0x00B340DA` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00B340F9` → [PnpFinalizeVetoedRemove](../A0/PnpFinalizeVetoedRemove_function_00A04968.md) (function, `0x00A04968`)
- `0x00B34110` → [PnpProcessCompletedEject](../72/PnpProcessCompletedEject_function_0072D090.md) (function, `0x0072D090`)
- `0x00B3412B` → [PpProfileQueryHardwareProfileChange](../73/PpProfileQueryHardwareProfileChange_function_00737C5C.md) (function, `0x00737C5C`)
- `0x00B34138` → [PpProfileCancelHardwareProfileTransition](../73/PpProfileCancelHardwareProfileTransition_function_00737918.md) (function, `0x00737918`)
- `0x00B34140` → [IopFreeRelationList](../A0/IopFreeRelationList_function_00A08310.md) (function, `0x00A08310`)
- `0x00B3414E` → [PpProfileCancelHardwareProfileTransition](../73/PpProfileCancelHardwareProfileTransition_function_00737918.md) (function, `0x00737918`)
- `0x00B34160` → [PnpInvalidateRelationsInList](../A0/PnpInvalidateRelationsInList_function_00A05DF8.md) (function, `0x00A05DF8`)
- `0x00B3416A` → [PnpTrackQueryRemoveDevices](../AC/PnpTrackQueryRemoveDevices_function_00ACCF54.md) (function, `0x00ACCF54`)
- `0x00B34172` → [IopFreeRelationList](../A0/IopFreeRelationList_function_00A08310.md) (function, `0x00A08310`)
- `0x00B3417F` → [PnpFinalizeVetoedRemove](../A0/PnpFinalizeVetoedRemove_function_00A04968.md) (function, `0x00A04968`)
- `0x00B34195` → [PipSetDevNodeUserFlags](../8F/PipSetDevNodeUserFlags_function_008FB8FC.md) (function, `0x008FB8FC`)
- `0x00B341A8` → [PnpTrackQueryRemoveDevices](../AC/PnpTrackQueryRemoveDevices_function_00ACCF54.md) (function, `0x00ACCF54`)
- `0x00B341B0` → [IopFreeRelationList](../A0/IopFreeRelationList_function_00A08310.md) (function, `0x00A08310`)
- `0x00B341CF` → [PipSetDevNodeFlags](../8F/PipSetDevNodeFlags_function_008FC048.md) (function, `0x008FC048`)
- `0x00B341FD` → [PnpDeleteLockedDeviceNodes](../A0/PnpDeleteLockedDeviceNodes_function_00A09B30.md) (function, `0x00A09B30`)
- `0x00B3422F` → [PiRestartRemovalRelations](../AB/PiRestartRemovalRelations_function_00AB06B8.md) (function, `0x00AB06B8`)
- `0x00B34237` → [PnpUnlinkDeviceRemovalRelations](../A0/PnpUnlinkDeviceRemovalRelations_function_00A063D8.md) (function, `0x00A063D8`)
- `0x00B34245` → [PnpTrackQueryRemoveDevices](../AC/PnpTrackQueryRemoveDevices_function_00ACCF54.md) (function, `0x00ACCF54`)
- `0x00B3424D` → [IopFreeRelationList](../A0/IopFreeRelationList_function_00A08310.md) (function, `0x00A08310`)
- `0x00B34274` → [PnpNotifyUserModeDeviceRemoval](../95/PnpNotifyUserModeDeviceRemoval_function_00954258.md) (function, `0x00954258`)
- `0x00B342B9` → [PipClearDevNodeProblem](../A2/PipClearDevNodeProblem_function_00A27C8C.md) (function, `0x00A27C8C`)
- `0x00B342C1` → [PnpRestartDeviceNode](../72/PnpRestartDeviceNode_function_0072CD60.md) (function, `0x0072CD60`)
- `0x00B342E6` → [PnpRequestDeviceAction](../../text/47/PnpRequestDeviceAction_function_00477FF8.md) (function, `0x00477FF8`)
- `0x00B342F8` → [PnpUnlinkDeviceRemovalRelations](../A0/PnpUnlinkDeviceRemovalRelations_function_00A063D8.md) (function, `0x00A063D8`)
- `0x00B34302` → [PnpTrackQueryRemoveDevices](../AC/PnpTrackQueryRemoveDevices_function_00ACCF54.md) (function, `0x00ACCF54`)
- `0x00B3430A` → [IopFreeRelationList](../A0/IopFreeRelationList_function_00A08310.md) (function, `0x00A08310`)
- `0x00B34321` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00B3432E` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00B3436C` → [PipSetDevNodeFlags](../8F/PipSetDevNodeFlags_function_008FC048.md) (function, `0x008FC048`)
- `0x00B34385` → [IopFreeRelationList](../A0/IopFreeRelationList_function_00A08310.md) (function, `0x00A08310`)
- `0x00B343AF` → [IopEnumerateRelations](../A6/IopEnumerateRelations_function_00A6E3B4.md) (function, `0x00A6E3B4`)
- `0x00B343BB` → [PnpUnlinkDeviceRemovalRelations](../A0/PnpUnlinkDeviceRemovalRelations_function_00A063D8.md) (function, `0x00A063D8`)
- `0x00B343CD` → [PiEventAllocatePendingEjectRelations](../74/PiEventAllocatePendingEjectRelations_function_00744220.md) (function, `0x00744220`)
- `0x00B343EA` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00B343F7` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00B34424` → [PoGetLightestSystemStateForEject](../75/PoGetLightestSystemStateForEject_function_00753E30.md) (function, `0x00753E30`)
- `0x00B34438` → [PpDevNodeUnlockTree](../A2/PpDevNodeUnlockTree_function_00A21290.md) (function, `0x00A21290`)
- `0x00B34444` → [IopEjectDevice](../73/IopEjectDevice_function_0073DC84.md) (function, `0x0073DC84`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00B3425D` → RVA `0x0001A220` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **8**
  - `0x00B340C2` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00B340CF` → [RtlCopyUnicodeString](../../text/3F/RtlCopyUnicodeString_function_003FEF30.md) (`PAGE` → `.text`)
  - `0x00B340DA` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00B342E6` → [PnpRequestDeviceAction](../../text/47/PnpRequestDeviceAction_function_00477FF8.md) (`PAGE` → `.text`)
  - `0x00B34321` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00B3432E` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00B343EA` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00B343F7` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **9**
  - `0x00B34018` → [PnpProcessQueryRemoveAndEject + 0x2D7](../A0/PnpProcessQueryRemoveAndEject_function_00A05170.md) (`tail-transfer`)
  - `0x00B34036` → [PnpProcessQueryRemoveAndEject + 0xBE](../A0/PnpProcessQueryRemoveAndEject_function_00A05170.md) (`tail-transfer`)
  - `0x00B3411A` → [PnpProcessQueryRemoveAndEject + 0xC1](../A0/PnpProcessQueryRemoveAndEject_function_00A05170.md) (`tail-transfer`)
  - `0x00B34132` → [PnpProcessQueryRemoveAndEject + 0x362](../A0/PnpProcessQueryRemoveAndEject_function_00A05170.md) (`tail-transfer`)
  - `0x00B34188` → [PnpProcessQueryRemoveAndEject + 0x353](../A0/PnpProcessQueryRemoveAndEject_function_00A05170.md) (`tail-transfer`)
  - `0x00B3419E` → [PnpProcessQueryRemoveAndEject + 0x365](../A0/PnpProcessQueryRemoveAndEject_function_00A05170.md) (`tail-transfer`)
  - `0x00B341B6` → [PnpProcessQueryRemoveAndEject + 0xC1](../A0/PnpProcessQueryRemoveAndEject_function_00A05170.md) (`tail-transfer`)
  - `0x00B34339` → [PnpProcessQueryRemoveAndEject + 0xC1](../A0/PnpProcessQueryRemoveAndEject_function_00A05170.md) (`tail-transfer`)
  - `0x00B3444E` → [PnpProcessQueryRemoveAndEject + 0x254](../A0/PnpProcessQueryRemoveAndEject_function_00A05170.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B33FE8  41 F7 84 24 8C 01 00 00 00 00 08 00  test dword ptr [r12 + 0x18c], 0x80000
00B33FF4  0F 85 39 03 00 00               jne 0x140b34333
00B33FFA  41 8B 84 24 38 02 00 00         mov eax, dword ptr [r12 + 0x238]
00B34002  83 E8 03                        sub eax, 3
00B34005  83 F8 01                        cmp eax, 1
00B34008  0F 86 25 03 00 00               jbe 0x140b34333
00B3400E  41 8B 84 24 30 02 00 00         mov eax, dword ptr [r12 + 0x230]
00B34016  A8 10                           test al, 0x10
00B34018  0F 85 29 14 ED FF               jne 0x140a05447
00B3401E  4D 8D 44 24 28                  lea r8, [r12 + 0x28]
00B34023  BA 08 00 00 00                  mov edx, 8
00B34028  48 8B CE                        mov rcx, rsi
00B3402B  BB 28 00 00 80                  mov ebx, 0x80000028
00B34030  E8 33 09 ED FF                  call 0x140a04968
00B34035  90                              nop
00B34036  E9 F3 11 ED FF                  jmp 0x140a0522e
00B3403B  48 8B 45 C7                     mov rax, qword ptr [rbp - 0x39]
00B3403F  48 8B 04 D8                     mov rax, qword ptr [rax + rbx*8]
00B34043  48 85 C0                        test rax, rax
00B34046  74 0D                           je 0x140b34055
00B34048  48 8B 80 38 01 00 00            mov rax, qword ptr [rax + 0x138]
00B3404F  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
00B34053  EB 02                           jmp 0x140b34057
00B34055  33 C9                           xor ecx, ecx
00B34057  83 B9 38 02 00 00 01            cmp dword ptr [rcx + 0x238], 1
00B3405E  75 0A                           jne 0x140b3406a
00B34060  BA 03 00 00 00                  mov edx, 3
00B34065  E8 32 3B C0 FF                  call 0x140737b9c
00B3406A  48 83 EB 01                     sub rbx, 1
00B3406E  79 CB                           jns 0x140b3403b
00B34070  83 FF 04                        cmp edi, 4
00B34073  0F 85 0D 01 00 00               jne 0x140b34186
00B34079  49 8B D7                        mov rdx, r15
00B3407C  48 8D 4D CF                     lea rcx, [rbp - 0x31]
00B34080  E8 7B D2 DD FF                  call 0x140911300
00B34085  45 33 ED                        xor r13d, r13d
00B34088  85 C0                           test eax, eax
00B3408A  0F 88 8F 00 00 00               js 0x140b3411f
00B34090  45 39 2F                        cmp dword ptr [r15], r13d
00B34093  0F 84 86 00 00 00               je 0x140b3411f
00B34099  E8 7A 38 C0 FF                  call 0x140737918
00B3409E  49 8B CE                        mov rcx, r14
00B340A1  E8 6A 42 ED FF                  call 0x140a08310
00B340A6  48 8B 4E 30                     mov rcx, qword ptr [rsi + 0x30]
00B340AA  48 85 C9                        test rcx, rcx
00B340AD  74 05                           je 0x140b340b4
00B340AF  41 8B 07                        mov eax, dword ptr [r15]
00B340B2  89 01                           mov dword ptr [rcx], eax
00B340B4  4C 39 6E 38                     cmp qword ptr [rsi + 0x38], r13
00B340B8  74 1A                           je 0x140b340d4
00B340BA  48 8B 55 CF                     mov rdx, qword ptr [rbp - 0x31]
00B340BE  48 8D 4D 07                     lea rcx, [rbp + 7]
00B340C2  E8 B9 66 8F FF                  call 0x14042a780
00B340C7  48 8B 4E 38                     mov rcx, qword ptr [rsi + 0x38]
00B340CB  48 8D 55 07                     lea rdx, [rbp + 7]
00B340CF  E8 5C AE 8C FF                  call 0x1403fef30
00B340D4  48 8B 4D CF                     mov rcx, qword ptr [rbp - 0x31]
00B340D8  33 D2                           xor edx, edx
00B340DA  E8 91 E7 04 00                  call 0x140b82870
00B340DF  4C 89 6D CF                     mov qword ptr [rbp - 0x31], r13
00B340E3  EB 30                           jmp 0x140b34115
00B340E5  3D DE 02 00 C0                  cmp eax, 0xc00002de
00B340EA  BA 09 00 00 00                  mov edx, 9
00B340EF  48 8B CE                        mov rcx, rsi
00B340F2  41 0F 45 D5                     cmovne edx, r13d
00B340F6  45 33 C0                        xor r8d, r8d
00B340F9  E8 6A 08 ED FF                  call 0x140a04968
00B340FE  4C 89 6B 30                     mov qword ptr [rbx + 0x30], r13
00B34102  48 8B CB                        mov rcx, rbx
00B34105  44 88 6B 59                     mov byte ptr [rbx + 0x59], r13b
00B34109  48 89 5B 08                     mov qword ptr [rbx + 8], rbx
00B3410D  48 89 1B                        mov qword ptr [rbx], rbx
00B34110  E8 7B 8F BF FF                  call 0x14072d090
00B34115  BB 28 00 00 80                  mov ebx, 0x80000028
00B3411A  E9 12 11 ED FF                  jmp 0x140a05231
00B3411F  8A 4D 6F                        mov cl, byte ptr [rbp + 0x6f]
00B34122  4D 8D 4F 08                     lea r9, [r15 + 8]
00B34126  4D 8B C7                        mov r8, r15
00B34129  33 D2                           xor edx, edx
00B3412B  E8 2C 3B C0 FF                  call 0x140737c5c
00B34130  85 C0                           test eax, eax
00B34132  0F 89 9A 13 ED FF               jns 0x140a054d2
00B34138  E8 DB 37 C0 FF                  call 0x140737918
00B3413D  49 8B CE                        mov rcx, r14
00B34140  E8 CB 41 ED FF                  call 0x140a08310
00B34145  41 8B 17                        mov edx, dword ptr [r15]
00B34148  4D 8D 47 08                     lea r8, [r15 + 8]
00B3414C  EB 2E                           jmp 0x140b3417c
00B3414E  E8 C5 37 C0 FF                  call 0x140737918
00B34153  45 33 C0                        xor r8d, r8d
00B34156  41 B1 01                        mov r9b, 1
00B34159  49 8B CE                        mov rcx, r14
00B3415C  41 8D 50 04                     lea edx, [r8 + 4]
00B34160  E8 93 1C ED FF                  call 0x140a05df8
00B34165  33 D2                           xor edx, edx
00B34167  49 8B CE                        mov rcx, r14
00B3416A  E8 E5 8D F9 FF                  call 0x140accf54
00B3416F  49 8B CE                        mov rcx, r14
00B34172  E8 99 41 ED FF                  call 0x140a08310
00B34177  45 33 C0                        xor r8d, r8d
00B3417A  33 D2                           xor edx, edx
00B3417C  48 8B CE                        mov rcx, rsi
00B3417F  E8 E4 07 ED FF                  call 0x140a04968
00B34184  EB 8F                           jmp 0x140b34115
00B34186  33 DB                           xor ebx, ebx
00B34188  E9 36 13 ED FF                  jmp 0x140a054c3
00B3418D  49 8B CD                        mov rcx, r13
00B34190  BA 00 01 00 00                  mov edx, 0x100
00B34195  E8 62 77 DC FF                  call 0x1408fb8fc
00B3419A  4C 8B 75 D7                     mov r14, qword ptr [rbp - 0x29]
00B3419E  E9 32 13 ED FF                  jmp 0x140a054d5
00B341A3  33 D2                           xor edx, edx
00B341A5  49 8B CE                        mov rcx, r14
00B341A8  E8 A7 8D F9 FF                  call 0x140accf54
00B341AD  49 8B CE                        mov rcx, r14
00B341B0  E8 5B 41 ED FF                  call 0x140a08310
00B341B5  90                              nop
00B341B6  E9 76 10 ED FF                  jmp 0x140a05231
00B341BB  4C 8B 6D F7                     mov r13, qword ptr [rbp - 9]
00B341BF  85 FF                           test edi, edi
00B341C1  0F 85 B7 00 00 00               jne 0x140b3427e
00B341C7  BA 00 00 00 02                  mov edx, 0x2000000
00B341CC  49 8B CC                        mov rcx, r12
00B341CF  E8 74 7E DC FF                  call 0x1408fc048
00B341D4  41 B1 01                        mov r9b, 1
00B341D7  48 83 64 24 38 00               and qword ptr [rsp + 0x38], 0
00B341DD  41 B8 02 00 00 00               mov r8d, 2
00B341E3  8B 46 14                        mov eax, dword ptr [rsi + 0x14]
00B341E6  49 8B D6                        mov rdx, r14
00B341E9  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
00B341EF  48 8B CB                        mov rcx, rbx
00B341F2  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00B341F6  8B 46 10                        mov eax, dword ptr [rsi + 0x10]
00B341F9  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00B341FD  E8 2E 59 ED FF                  call 0x140a09b30
00B34202  41 8B 84 24 30 02 00 00         mov eax, dword ptr [r12 + 0x230]
00B3420A  8B C8                           mov ecx, eax
00B3420C  C1 E9 03                        shr ecx, 3
00B3420F  C1 E8 10                        shr eax, 0x10
00B34212  80 E1 01                        and cl, 1
00B34215  24 01                           and al, 1
00B34217  89 4D 77                        mov dword ptr [rbp + 0x77], ecx
00B3421A  89 45 6F                        mov dword ptr [rbp + 0x6f], eax
00B3421D  83 FF 04                        cmp edi, 4
00B34220  0F 84 C7 00 00 00               je 0x140b342ed
00B34226  4C 8B C3                        mov r8, rbx
00B34229  49 8B D6                        mov rdx, r14
00B3422C  48 8B CE                        mov rcx, rsi
00B3422F  E8 84 C4 F7 FF                  call 0x140ab06b8
00B34234  49 8B D6                        mov rdx, r14
00B34237  E8 9C 21 ED FF                  call 0x140a063d8
00B3423C  85 FF                           test edi, edi
00B3423E  75 0A                           jne 0x140b3424a
00B34240  33 D2                           xor edx, edx
00B34242  49 8B CE                        mov rcx, r14
00B34245  E8 0A 8D F9 FF                  call 0x140accf54
00B3424A  49 8B CE                        mov rcx, r14
00B3424D  E8 BE 40 ED FF                  call 0x140a08310
00B34252  83 FF 02                        cmp edi, 2
00B34255  75 38                           jne 0x140b3428f
00B34257  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
00B3425D  4C 8D 05 BC 5F 4E FF            lea r8, [rip - 0xb1a044]
00B34264  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
00B3426A  45 33 C9                        xor r9d, r9d
00B3426D  48 8B 55 7F                     mov rdx, qword ptr [rbp + 0x7f]
00B34271  48 8B CE                        mov rcx, rsi
00B34274  E8 DF FF E1 FF                  call 0x140954258
00B34279  E9 91 00 00 00                  jmp 0x140b3430f
00B3427E  83 FF 04                        cmp edi, 4
00B34281  0F 84 4D FF FF FF               je 0x140b341d4
00B34287  45 32 C9                        xor r9b, r9b
00B3428A  E9 48 FF FF FF                  jmp 0x140b341d7
00B3428F  85 FF                           test edi, edi
00B34291  75 7C                           jne 0x140b3430f
00B34293  8B 86 98 00 00 00               mov eax, dword ptr [rsi + 0x98]
00B34299  A8 02                           test al, 2
00B3429B  75 72                           jne 0x140b3430f
00B3429D  41 F7 84 24 8C 01 00 00 00 20 00 00  test dword ptr [r12 + 0x18c], 0x2000
00B342A9  74 64                           je 0x140b3430f
00B342AB  41 83 BC 24 94 01 00 00 12      cmp dword ptr [r12 + 0x194], 0x12
00B342B4  75 59                           jne 0x140b3430f
00B342B6  49 8B CC                        mov rcx, r12
00B342B9  E8 CE 39 EF FF                  call 0x140a27c8c
00B342BE  49 8B CC                        mov rcx, r12
00B342C1  E8 9A 8A BF FF                  call 0x14072cd60
00B342C6  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
00B342CC  8D 57 10                        lea edx, [rdi + 0x10]
00B342CF  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
00B342D5  45 33 C9                        xor r9d, r9d
00B342D8  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
00B342DE  41 B0 01                        mov r8b, 1
00B342E1  49 8B 4C 24 20                  mov rcx, qword ptr [r12 + 0x20]
00B342E6  E8 0D 3D 94 FF                  call 0x140477ff8
00B342EB  EB 22                           jmp 0x140b3430f
00B342ED  84 C9                           test cl, cl
00B342EF  75 4D                           jne 0x140b3433e
00B342F1  84 C0                           test al, al
00B342F3  75 49                           jne 0x140b3433e
00B342F5  49 8B D6                        mov rdx, r14
00B342F8  E8 DB 20 ED FF                  call 0x140a063d8
00B342FD  33 D2                           xor edx, edx
00B342FF  49 8B CE                        mov rcx, r14
00B34302  E8 4D 8C F9 FF                  call 0x140accf54
00B34307  49 8B CE                        mov rcx, r14
00B3430A  E8 01 40 ED FF                  call 0x140a08310
00B3430F  4D 85 ED                        test r13, r13
00B34312  74 1F                           je 0x140b34333
00B34314  49 8B 45 20                     mov rax, qword ptr [r13 + 0x20]
00B34318  BA 01 00 00 00                  mov edx, 1
00B3431D  49 8B 4D 08                     mov rcx, qword ptr [r13 + 8]
00B34321  E8 AA 67 B8 FF                  call 0x1406baad0
00B34326  49 8B 45 18                     mov rax, qword ptr [r13 + 0x18]
00B3432A  49 8B 4D 08                     mov rcx, qword ptr [r13 + 8]
00B3432E  E8 9D 67 B8 FF                  call 0x1406baad0
00B34333  45 33 ED                        xor r13d, r13d
00B34336  41 8B DD                        mov ebx, r13d
00B34339  E9 F3 0E ED FF                  jmp 0x140a05231
00B3433E  83 65 E3 00                     and dword ptr [rbp - 0x1d], 0
00B34342  C7 45 DF 01 00 00 00            mov dword ptr [rbp - 0x21], 1
00B34349  EB 50                           jmp 0x140b3439b
00B3434B  48 8B 45 FF                     mov rax, qword ptr [rbp - 1]
00B3434F  48 85 C0                        test rax, rax
00B34352  74 47                           je 0x140b3439b
00B34354  48 8B 80 38 01 00 00            mov rax, qword ptr [rax + 0x138]
00B3435B  48 8B 58 28                     mov rbx, qword ptr [rax + 0x28]
00B3435F  48 85 DB                        test rbx, rbx
00B34362  74 37                           je 0x140b3439b
00B34364  BA 00 00 08 00                  mov edx, 0x80000
00B34369  48 8B CB                        mov rcx, rbx
00B3436C  E8 D7 7C DC FF                  call 0x1408fc048
00B34371  48 8B 83 B8 02 00 00            mov rax, qword ptr [rbx + 0x2b8]
00B34378  48 89 45 EF                     mov qword ptr [rbp - 0x11], rax
00B3437C  48 85 C0                        test rax, rax
00B3437F  74 1A                           je 0x140b3439b
00B34381  48 8B 48 40                     mov rcx, qword ptr [rax + 0x40]
00B34385  E8 86 3F ED FF                  call 0x140a08310
00B3438A  48 8B 45 EF                     mov rax, qword ptr [rbp - 0x11]
00B3438E  48 83 60 40 00                  and qword ptr [rax + 0x40], 0
00B34393  48 83 A3 B8 02 00 00 00         and qword ptr [rbx + 0x2b8], 0
00B3439B  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
00B343A1  4C 8D 45 FF                     lea r8, [rbp - 1]
00B343A5  45 33 C9                        xor r9d, r9d
00B343A8  48 8D 55 DF                     lea rdx, [rbp - 0x21]
00B343AC  49 8B CE                        mov rcx, r14
00B343AF  E8 00 A0 F3 FF                  call 0x140a6e3b4
00B343B4  84 C0                           test al, al
00B343B6  75 93                           jne 0x140b3434b
00B343B8  49 8B D6                        mov rdx, r14
00B343BB  E8 18 20 ED FF                  call 0x140a063d8
00B343C0  44 8A 45 67                     mov r8b, byte ptr [rbp + 0x67]
00B343C4  4D 8B CD                        mov r9, r13
00B343C7  49 8B D6                        mov rdx, r14
00B343CA  48 8B CE                        mov rcx, rsi
00B343CD  E8 4E FE C0 FF                  call 0x140744220
00B343D2  48 8B D8                        mov rbx, rax
00B343D5  48 85 C0                        test rax, rax
00B343D8  75 34                           jne 0x140b3440e
00B343DA  4D 85 ED                        test r13, r13
00B343DD  74 1D                           je 0x140b343fc
00B343DF  49 8B 45 20                     mov rax, qword ptr [r13 + 0x20]
00B343E3  8D 53 01                        lea edx, [rbx + 1]
00B343E6  49 8B 4D 08                     mov rcx, qword ptr [r13 + 8]
00B343EA  E8 E1 66 B8 FF                  call 0x1406baad0
00B343EF  49 8B 45 18                     mov rax, qword ptr [r13 + 0x18]
00B343F3  49 8B 4D 08                     mov rcx, qword ptr [r13 + 8]
00B343F7  E8 D4 66 B8 FF                  call 0x1406baad0
00B343FC  45 33 ED                        xor r13d, r13d
00B343FF  44 38 6D 67                     cmp byte ptr [rbp + 0x67], r13b
00B34403  0F 84 4A FD FF FF               je 0x140b34153
00B34409  E9 40 FD FF FF                  jmp 0x140b3414e
00B3440E  44 8A 45 6F                     mov r8b, byte ptr [rbp + 0x6f]
00B34412  4C 8D 48 5C                     lea r9, [rax + 0x5c]
00B34416  8A 55 77                        mov dl, byte ptr [rbp + 0x77]
00B34419  8A 4D 67                        mov cl, byte ptr [rbp + 0x67]
00B3441C  49 89 9C 24 B8 02 00 00         mov qword ptr [r12 + 0x2b8], rbx
00B34424  E8 07 FA C1 FF                  call 0x140753e30
00B34429  45 33 ED                        xor r13d, r13d
00B3442C  85 C0                           test eax, eax
00B3442E  0F 88 B1 FC FF FF               js 0x140b340e5
00B34434  41 8D 4D 01                     lea ecx, [r13 + 1]
00B34438  E8 53 CE EE FF                  call 0x140a21290
00B3443D  48 8B 4D E7                     mov rcx, qword ptr [rbp - 0x19]
00B34441  48 8B D3                        mov rdx, rbx
00B34444  E8 3B 98 C0 FF                  call 0x14073dc84
00B34449  BB 03 01 00 00                  mov ebx, 0x103
00B3444E  E9 71 0F ED FF                  jmp 0x140a053c4
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00B33FE8(void)
{
    __int64 result;
    __int64 v_r13;
    unsigned int v_stack_p20;
    unsigned int v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;

    if (((*(unsigned int *)(v_r12 + 396)) & (0x80000ULL)) != 0) goto loc_00B34333;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r12 + 568))) - (3));
    if (((unsigned int)(result)) <= 1) goto loc_00B34333;
    result = PnpFinalizeVetoedRemove(v_rsi, 8, v_r12 + 40, a4);
loc_00B34333:
    v_r13 = 0;
}
```

## 5. (Beta) C Style

```c
void sub_00B33FE8(void)
{
    int64_t result;
    int64_t local_r13;
    uint32_t v_stack_p20;
    uint32_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;

    if (((*(uint32_t *)(local_r12 + 0x18C)) & (0x80000ULL)) != 0) goto loc_00B34333;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r12 + 0x238))) - (3));
    if (((uint32_t)(result)) <= 1) goto loc_00B34333;
    result = PnpFinalizeVetoedRemove(local_rsi, 8, local_r12 + 40, a4);
loc_00B34333:
    local_r13 = 0;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B33FE8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
