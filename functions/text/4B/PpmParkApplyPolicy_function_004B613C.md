# PpmParkApplyPolicy

- RVA: `0x004B613C`–`0x004B6864` (길이 `1,832` bytes)
- VA: `0x00000001404B613C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BA5A4`
- 디코드: `465`개 명령, `1,832/1,832` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **17**; 고유 호출 대상: **14**
- 직접 호출자로 확인된 함수: **8**
- RIP 상대 이미지 참조: **16**

### Outgoing calls
- `0x004B6163` → [Feature_PpmParkEx__private_IsEnabledDeviceUsageNoInline](../4F/Feature_PpmParkEx__private_IsEnabledDeviceUsageNoInline_function_004F135C.md) (function, `0x004F135C`)
- `0x004B61AB` → [PpmParkEvalualteSmtUnparkPolicy](../4C/PpmParkEvalualteSmtUnparkPolicy_function_004C0868.md) (function, `0x004C0868`)
- `0x004B61BA` → [KeGetPrcb](../2D/KeGetPrcb_function_002D85D0.md) (function, `0x002D85D0`)
- `0x004B63FB` → [KeEnumerateNextProcessor](../41/KeEnumerateNextProcessor_function_00415480.md) (function, `0x00415480`)
- `0x004B640E` → [KeGetPrcb](../2D/KeGetPrcb_function_002D85D0.md) (function, `0x002D85D0`)
- `0x004B6430` → [KeEnumerateNextProcessor](../41/KeEnumerateNextProcessor_function_00415480.md) (function, `0x00415480`)
- `0x004B64BB` → [PpmEventParkNodeParkHintChanged](../4E/PpmEventParkNodeParkHintChanged_function_004E2D74.md) (function, `0x004E2D74`)
- `0x004B65D0` → [PpmConfigureRestrictionPolicy](../4A/PpmConfigureRestrictionPolicy_function_004A0398.md) (function, `0x004A0398`)
- `0x004B6744` → [PpmEventParkNodeCapChange](../5D/PpmEventParkNodeCapChange_function_005DAEDC.md) (function, `0x005DAEDC`)
- `0x004B67B3` → [PpmEventSoftParkLatencyUpdate](../4F/PpmEventSoftParkLatencyUpdate_function_004F3950.md) (function, `0x004F3950`)
- `0x004B67F3` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x004B6808` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x004B680D` → [KeUpdateSoftParkRankList](../2D/KeUpdateSoftParkRankList_function_002D5998.md) (function, `0x002D5998`)
- `0x004B6812` → [PpmEventSoftParkRankListChanged](../2D/PpmEventSoftParkRankListChanged_function_002D58D8.md) (function, `0x002D58D8`)
- `0x004B683B` → [PpmConvertTime](../44/PpmConvertTime_function_00447530.md) (function, `0x00447530`)
- `0x004B6846` → [PpmHeteroHgsCheckContainmentDecision](../3B/PpmHeteroHgsCheckContainmentDecision_function_003BEFF8.md) (function, `0x003BEFF8`)
- `0x004B684D` → [PpmParkApplyPolicyEx](../4F/PpmParkApplyPolicyEx_function_004F3090.md) (function, `0x004F3090`)

### Direct callers
- [PpmParkSetLpiCap](../4D/PpmParkSetLpiCap_function_004D9358.md) at `0x004D947D`
- [PpmParkRegisterParking](../5D/PpmParkRegisterParking_function_005DB508.md) at `0x005DBD98`
- [PpmParkRegisterParkingEx](../5E/PpmParkRegisterParkingEx_function_005E183C.md) at `0x005E1D80`
- [PpmRegisterPerfStates](../../page/75/PpmRegisterPerfStates_function_0075B084.md) at `0x0075BC0A`
- [PpmParkApplyForcedMask](../../page/76/PpmParkApplyForcedMask_function_0076A904.md) at `0x0076AB04`
- [PpmParkClearForcedMask](../../page/76/PpmParkClearForcedMask_function_0076AB20.md) at `0x0076ABF1`
- [PpmReapplyPerfPolicy](../../page/A5/PpmReapplyPerfPolicy_function_00A53148.md) at `0x00A531E5`
- [PopPowerRequestCallbackPerfBoostRequired](../../page/A9/PopPowerRequestCallbackPerfBoostRequired_function_00A96F70.md) at `0x00A96F9A`
- [PopPowerRequestCallbackPerfBoostRequired](../../page/A9/PopPowerRequestCallbackPerfBoostRequired_function_00A96F70.md) at `0x00A97007`

### Static image references
- `0x004B6170` → RVA `0x00F083D8` (`.data`; read)
- `0x004B6179` → RVA `0x00F23454` (`.data`; write)
- `0x004B6184` → RVA `0x00E08380` (`.data`; read)
- `0x004B618B` → RVA `0x00F0CE0C` (`.data`; read)
- `0x004B61D2` → RVA `0x00FC6D50` (`ALMOSTRO`; read)
- `0x004B61ED` → RVA `0x00F083E0` (`.data`; read)
- `0x004B61F6` → RVA `0x00F083A2` (`.data`; read)
- `0x004B61FD` → RVA `0x00E67A40` (`.data`; read)
- `0x004B6207` → RVA `0x00E67A44` (`.data`; read)
- `0x004B64EE` → RVA `0x00FC5038` (`ALMOSTRO`; read)
- `0x004B6780` → RVA `0x00F0E0F0` (`.data`; read)
- `0x004B6797` → RVA `0x00FC5094` (`ALMOSTRO`; read)
- `0x004B67BC` → RVA `0x00F083C8` (`.data`; read)
- `0x004B67C3` → RVA `0x00FC6AF1` (`ALMOSTRO`; write)
- `0x004B67D5` → RVA `0x00F083B8` (`.data`; read)
- `0x004B67E1` → RVA `0x00FC6AE8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004B613C  4C 8B DC                        mov r11, rsp
004B613F  53                              push rbx
004B6140  55                              push rbp
004B6141  56                              push rsi
004B6142  57                              push rdi
004B6143  41 54                           push r12
004B6145  41 55                           push r13
004B6147  41 56                           push r14
004B6149  41 57                           push r15
004B614B  48 83 EC 78                     sub rsp, 0x78
004B614F  33 C0                           xor eax, eax
004B6151  0F 57 C0                        xorps xmm0, xmm0
004B6154  33 FF                           xor edi, edi
004B6156  0F 11 44 24 50                  movups xmmword ptr [rsp + 0x50], xmm0
004B615B  41 89 7B 20                     mov dword ptr [r11 + 0x20], edi
004B615F  49 89 43 A8                     mov qword ptr [r11 - 0x58], rax
004B6163  E8 F4 B1 03 00                  call 0x1404f135c
004B6168  85 C0                           test eax, eax
004B616A  0F 85 DD 06 00 00               jne 0x1404b684d
004B6170  48 39 3D 61 22 A5 00            cmp qword ptr [rip + 0xa52261], rdi
004B6177  75 0B                           jne 0x1404b6184
004B6179  89 3D D5 D2 A6 00               mov dword ptr [rip + 0xa6d2d5], edi
004B617F  E9 CE 06 00 00                  jmp 0x1404b6852
004B6184  48 8B 35 F5 21 95 00            mov rsi, qword ptr [rip + 0x9521f5]
004B618B  48 63 05 7A 6C A5 00            movsxd rax, dword ptr [rip + 0xa56c7a]
004B6192  48 83 C6 28                     add rsi, 0x28
004B6196  48 69 C8 E8 01 00 00            imul rcx, rax, 0x1e8
004B619D  48 03 F1                        add rsi, rcx
004B61A0  48 89 74 24 48                  mov qword ptr [rsp + 0x48], rsi
004B61A5  8A 8E CA 01 00 00               mov cl, byte ptr [rsi + 0x1ca]
004B61AB  E8 B8 A6 00 00                  call 0x1404c0868
004B61B0  33 C9                           xor ecx, ecx
004B61B2  40 88 BC 24 C0 00 00 00         mov byte ptr [rsp + 0xc0], dil
004B61BA  E8 11 24 E2 FF                  call 0x1402d85d0
004B61BF  41 BB 01 00 00 00               mov r11d, 1
004B61C5  45 8D 63 3F                     lea r12d, [r11 + 0x3f]
004B61C9  48 39 B8 B0 89 00 00            cmp qword ptr [rax + 0x89b0], rdi
004B61D0  75 1B                           jne 0x1404b61ed
004B61D2  8B 05 78 0B B1 00               mov eax, dword ptr [rip + 0xb10b78]
004B61D8  41 3B C4                        cmp eax, r12d
004B61DB  0F B6 C8                        movzx ecx, al
004B61DE  41 0F 47 CC                     cmova ecx, r12d
004B61E2  44 88 9C 24 C0 00 00 00         mov byte ptr [rsp + 0xc0], r11b
004B61EA  44 8A E1                        mov r12b, cl
004B61ED  44 8B 05 EC 21 A5 00            mov r8d, dword ptr [rip + 0xa521ec]
004B61F4  33 D2                           xor edx, edx
004B61F6  0F B7 0D A5 21 A5 00            movzx ecx, word ptr [rip + 0xa521a5]
004B61FD  44 8B 35 3C 18 9B 00            mov r14d, dword ptr [rip + 0x9b183c]
004B6204  41 8B C6                        mov eax, r14d
004B6207  44 8B 3D 36 18 9B 00            mov r15d, dword ptr [rip + 0x9b1836]
004B620E  41 F7 F0                        div r8d
004B6211  33 D2                           xor edx, edx
004B6213  44 8B C8                        mov r9d, eax
004B6216  F7 F1                           div ecx
004B6218  41 8B C7                        mov eax, r15d
004B621B  44 2B CA                        sub r9d, edx
004B621E  33 D2                           xor edx, edx
004B6220  41 F7 F0                        div r8d
004B6223  33 D2                           xor edx, edx
004B6225  44 89 4C 24 30                  mov dword ptr [rsp + 0x30], r9d
004B622A  44 8B D0                        mov r10d, eax
004B622D  F7 F1                           div ecx
004B622F  0F B7 CF                        movzx ecx, di
004B6232  44 2B D2                        sub r10d, edx
004B6235  66 89 8C 24 D0 00 00 00         mov word ptr [rsp + 0xd0], cx
004B623D  44 89 54 24 2C                  mov dword ptr [rsp + 0x2c], r10d
004B6242  45 85 C0                        test r8d, r8d
004B6245  0F 84 28 04 00 00               je 0x1404b6673
004B624B  0F B7 C1                        movzx eax, cx
004B624E  48 69 D8 10 05 00 00            imul rbx, rax, 0x510
004B6255  41 0F B6 D1                     movzx edx, r9b
004B6259  48 03 1D 78 21 A5 00            add rbx, qword ptr [rip + 0xa52178]
004B6260  44 0F B7 0D 3A 21 A5 00         movzx r9d, word ptr [rip + 0xa5213a]
004B6268  44 0F B7 43 0A                  movzx r8d, word ptr [rbx + 0xa]
004B626D  41 8B C8                        mov ecx, r8d
004B6270  41 2B C9                        sub ecx, r9d
004B6273  3B D1                           cmp edx, ecx
004B6275  7E 06                           jle 0x1404b627d
004B6277  8A 53 0A                        mov dl, byte ptr [rbx + 0xa]
004B627A  41 2A D1                        sub dl, r9b
004B627D  0F B6 C2                        movzx eax, dl
004B6280  44 2B F0                        sub r14d, eax
004B6283  41 0F B6 CA                     movzx ecx, r10b
004B6287  0F B6 C2                        movzx eax, dl
004B628A  66 89 83 90 04 00 00            mov word ptr [rbx + 0x490], ax
004B6291  0F B7 15 0A 21 A5 00            movzx edx, word ptr [rip + 0xa5210a]
004B6298  44 2B C2                        sub r8d, edx
004B629B  44 89 74 24 24                  mov dword ptr [rsp + 0x24], r14d
004B62A0  41 3B C8                        cmp ecx, r8d
004B62A3  7E 05                           jle 0x1404b62aa
004B62A5  8A 4B 0A                        mov cl, byte ptr [rbx + 0xa]
004B62A8  2A CA                           sub cl, dl
004B62AA  0F B6 C1                        movzx eax, cl
004B62AD  48 8B D7                        mov rdx, rdi
004B62B0  44 2B F8                        sub r15d, eax
004B62B3  40 88 BC 24 C8 00 00 00         mov byte ptr [rsp + 0xc8], dil
004B62BB  44 8A EF                        mov r13b, dil
004B62BE  0F B6 C1                        movzx eax, cl
004B62C1  4C 8B C7                        mov r8, rdi
004B62C4  66 89 83 94 04 00 00            mov word ptr [rbx + 0x494], ax
004B62CB  8B EF                           mov ebp, edi
004B62CD  44 89 7C 24 28                  mov dword ptr [rsp + 0x28], r15d
004B62D2  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
004B62D7  48 89 54 24 40                  mov qword ptr [rsp + 0x40], rdx
004B62DC  40 38 7B 0C                     cmp byte ptr [rbx + 0xc], dil
004B62E0  0F 86 E7 01 00 00               jbe 0x1404b64cd
004B62E6  44 8A BC 24 C0 00 00 00         mov r15b, byte ptr [rsp + 0xc0]
004B62EE  45 33 F6                        xor r14d, r14d
004B62F1  8B C5                           mov eax, ebp
004B62F3  48 8D 3C 80                     lea rdi, [rax + rax*4]
004B62F7  8B C5                           mov eax, ebp
004B62F9  48 C1 E7 07                     shl rdi, 7
004B62FD  48 03 BB 08 05 00 00            add rdi, qword ptr [rbx + 0x508]
004B6304  F7 D8                           neg eax
004B6306  8B C5                           mov eax, ebp
004B6308  48 1B C9                        sbb rcx, rcx
004B630B  48 F7 D9                        neg rcx
004B630E  F7 D8                           neg eax
004B6310  44 0F B6 9C 31 9E 00 00 00      movzx r11d, byte ptr [rcx + rsi + 0x9e]
004B6319  48 1B C9                        sbb rcx, rcx
004B631C  48 F7 D9                        neg rcx
004B631F  44 0F B6 94 31 9C 00 00 00      movzx r10d, byte ptr [rcx + rsi + 0x9c]
004B6328  45 84 FF                        test r15b, r15b
004B632B  74 06                           je 0x1404b6333
004B632D  85 ED                           test ebp, ebp
004B632F  45 0F 45 D6                     cmovne r10d, r14d
004B6333  0F B6 07                        movzx eax, byte ptr [rdi]
004B6336  84 C0                           test al, al
004B6338  0F 84 4E 01 00 00               je 0x1404b648c
004B633E  44 0F B7 2D 5C 20 A5 00         movzx r13d, word ptr [rip + 0xa5205c]
004B6346  44 8B C8                        mov r9d, eax
004B6349  41 8B CB                        mov ecx, r11d
004B634C  BE 1F 85 EB 51                  mov esi, 0x51eb851f
004B6351  0F AF C8                        imul ecx, eax
004B6354  8B C6                           mov eax, esi
004B6356  83 C1 32                        add ecx, 0x32
004B6359  F7 E1                           mul ecx
004B635B  41 8B C1                        mov eax, r9d
004B635E  44 8B DA                        mov r11d, edx
004B6361  41 C1 EB 05                     shr r11d, 5
004B6365  41 0F B6 CB                     movzx ecx, r11b
004B6369  2B C1                           sub eax, ecx
004B636B  41 0F B6 CA                     movzx ecx, r10b
004B636F  99                              cdq
004B6370  41 0F AF C9                     imul ecx, r9d
004B6374  41 F7 FD                        idiv r13d
004B6377  8B C6                           mov eax, esi
004B6379  83 C1 32                        add ecx, 0x32
004B637C  44 02 DA                        add r11b, dl
004B637F  F7 E1                           mul ecx
004B6381  8B F2                           mov esi, edx
004B6383  C1 EE 05                        shr esi, 5
004B6386  40 0F B6 CE                     movzx ecx, sil
004B638A  44 2B C9                        sub r9d, ecx
004B638D  41 8B C1                        mov eax, r9d
004B6390  99                              cdq
004B6391  41 F7 FD                        idiv r13d
004B6394  40 02 F2                        add sil, dl
004B6397  85 ED                           test ebp, ebp
004B6399  74 11                           je 0x1404b63ac
004B639B  45 3A DC                        cmp r11b, r12b
004B639E  41 0F B6 CB                     movzx ecx, r11b
004B63A2  41 0F B6 C4                     movzx eax, r12b
004B63A6  0F 43 C8                        cmovae ecx, eax
004B63A9  44 8A D9                        mov r11b, cl
004B63AC  40 84 F6                        test sil, sil
004B63AF  74 11                           je 0x1404b63c2
004B63B1  41 0F B6 CD                     movzx ecx, r13b
004B63B5  40 3A CE                        cmp cl, sil
004B63B8  40 0F B6 C6                     movzx eax, sil
004B63BC  0F 47 C1                        cmova eax, ecx
004B63BF  40 8A F0                        mov sil, al
004B63C2  41 0F B6 CB                     movzx ecx, r11b
004B63C6  48 8D 54 24 50                  lea rdx, [rsp + 0x50]
004B63CB  40 0F B6 C6                     movzx eax, sil
004B63CF  44 3A DE                        cmp r11b, sil
004B63D2  4D 8B EE                        mov r13, r14
004B63D5  4C 89 74 24 50                  mov qword ptr [rsp + 0x50], r14
004B63DA  0F 42 C8                        cmovb ecx, eax
004B63DD  0F B7 43 04                     movzx eax, word ptr [rbx + 4]
004B63E1  89 4C 24 20                     mov dword ptr [rsp + 0x20], ecx
004B63E5  48 8B 4F 18                     mov rcx, qword ptr [rdi + 0x18]
004B63E9  48 89 4C 24 58                  mov qword ptr [rsp + 0x58], rcx
004B63EE  48 8D 8C 24 D8 00 00 00         lea rcx, [rsp + 0xd8]
004B63F6  66 89 44 24 60                  mov word ptr [rsp + 0x60], ax
004B63FB  E8 80 F0 F5 FF                  call 0x140415480
004B6400  85 C0                           test eax, eax
004B6402  75 40                           jne 0x1404b6444
004B6404  45 33 FF                        xor r15d, r15d
004B6407  8B 8C 24 D8 00 00 00            mov ecx, dword ptr [rsp + 0xd8]
004B640E  E8 BD 21 E2 FF                  call 0x1402d85d0
004B6413  44 38 B8 4C 8A 00 00            cmp byte ptr [rax + 0x8a4c], r15b
004B641A  74 07                           je 0x1404b6423
004B641C  4C 0B A8 C8 00 00 00            or r13, qword ptr [rax + 0xc8]
004B6423  48 8D 54 24 50                  lea rdx, [rsp + 0x50]
004B6428  48 8D 8C 24 D8 00 00 00         lea rcx, [rsp + 0xd8]
004B6430  E8 4B F0 F5 FF                  call 0x140415480
004B6435  85 C0                           test eax, eax
004B6437  74 CE                           je 0x1404b6407
004B6439  44 8A BC 24 C0 00 00 00         mov r15b, byte ptr [rsp + 0xc0]
004B6441  45 33 F6                        xor r14d, r14d
004B6444  4C 8B 44 24 38                  mov r8, qword ptr [rsp + 0x38]
004B6449  4C 0B 47 20                     or r8, qword ptr [rdi + 0x20]
004B644D  48 8B 54 24 40                  mov rdx, qword ptr [rsp + 0x40]
004B6452  0F B6 44 24 20                  movzx eax, byte ptr [rsp + 0x20]
004B6457  49 0B D5                        or rdx, r13
004B645A  4C 89 6F 20                     mov qword ptr [rdi + 0x20], r13
004B645E  44 8A AC 24 C8 00 00 00         mov r13b, byte ptr [rsp + 0xc8]
004B6466  44 02 EE                        add r13b, sil
004B6469  66 89 47 04                     mov word ptr [rdi + 4], ax
004B646D  40 0F B6 C6                     movzx eax, sil
004B6471  48 8B 74 24 48                  mov rsi, qword ptr [rsp + 0x48]
004B6476  44 88 AC 24 C8 00 00 00         mov byte ptr [rsp + 0xc8], r13b
004B647E  4C 89 44 24 38                  mov qword ptr [rsp + 0x38], r8
004B6483  48 89 54 24 40                  mov qword ptr [rsp + 0x40], rdx
004B6488  66 89 47 02                     mov word ptr [rdi + 2], ax
004B648C  0F B6 43 0C                     movzx eax, byte ptr [rbx + 0xc]
004B6490  41 BB 01 00 00 00               mov r11d, 1
004B6496  41 03 EB                        add ebp, r11d
004B6499  3B E8                           cmp ebp, eax
004B649B  0F 82 50 FE FF FF               jb 0x1404b62f1
004B64A1  44 8B 74 24 24                  mov r14d, dword ptr [rsp + 0x24]
004B64A6  44 8B 7C 24 28                  mov r15d, dword ptr [rsp + 0x28]
004B64AB  4C 3B C2                        cmp r8, rdx
004B64AE  74 16                           je 0x1404b64c6
004B64B0  0F B7 4B 04                     movzx ecx, word ptr [rbx + 4]
004B64B4  4C 8B C2                        mov r8, rdx
004B64B7  48 8B 53 10                     mov rdx, qword ptr [rbx + 0x10]
004B64BB  E8 B4 C8 02 00                  call 0x1404e2d74
004B64C0  41 BB 01 00 00 00               mov r11d, 1
004B64C6  33 FF                           xor edi, edi
004B64C8  45 84 ED                        test r13b, r13b
004B64CB  75 21                           jne 0x1404b64ee
004B64CD  0F B7 0D CE 1E A5 00            movzx ecx, word ptr [rip + 0xa51ece]
004B64D4  48 8B 93 08 05 00 00            mov rdx, qword ptr [rbx + 0x508]
004B64DB  0F B7 42 04                     movzx eax, word ptr [rdx + 4]
004B64DF  66 3B C8                        cmp cx, ax
004B64E2  66 89 4A 02                     mov word ptr [rdx + 2], cx
004B64E6  66 0F 46 C8                     cmovbe cx, ax
004B64EA  66 89 4A 04                     mov word ptr [rdx + 4], cx
004B64EE  8B 05 44 EB B0 00               mov eax, dword ptr [rip + 0xb0eb44]
004B64F4  83 F8 02                        cmp eax, 2
004B64F7  75 60                           jne 0x1404b6559
004B64F9  80 8B A0 04 00 00 04            or byte ptr [rbx + 0x4a0], 4
004B6500  48 8B 83 08 05 00 00            mov rax, qword ptr [rbx + 0x508]
004B6507  0F B7 48 02                     movzx ecx, word ptr [rax + 2]
004B650B  66 41 3B CB                     cmp cx, r11w
004B650F  77 03                           ja 0x1404b6514
004B6511  41 8B CB                        mov ecx, r11d
004B6514  66 89 48 02                     mov word ptr [rax + 2], cx
004B6518  0F B7 48 04                     movzx ecx, word ptr [rax + 4]
004B651C  66 41 3B CB                     cmp cx, r11w
004B6520  77 03                           ja 0x1404b6525
004B6522  41 8B CB                        mov ecx, r11d
004B6525  66 89 48 04                     mov word ptr [rax + 4], cx
004B6529  41 8B D3                        mov edx, r11d
004B652C  44 38 5B 0C                     cmp byte ptr [rbx + 0xc], r11b
004B6530  0F 86 97 00 00 00               jbe 0x1404b65cd
004B6536  8B C2                           mov eax, edx
004B6538  41 03 D3                        add edx, r11d
004B653B  48 8D 0C 80                     lea rcx, [rax + rax*4]
004B653F  48 C1 E1 07                     shl rcx, 7
004B6543  48 03 8B 08 05 00 00            add rcx, qword ptr [rbx + 0x508]
004B654A  48 83 61 02 00                  and qword ptr [rcx + 2], 0
004B654F  0F B6 43 0C                     movzx eax, byte ptr [rbx + 0xc]
004B6553  3B D0                           cmp edx, eax
004B6555  72 DF                           jb 0x1404b6536
004B6557  EB 74                           jmp 0x1404b65cd
004B6559  83 F8 03                        cmp eax, 3
004B655C  75 6F                           jne 0x1404b65cd
004B655E  40 38 BB A1 04 00 00            cmp byte ptr [rbx + 0x4a1], dil
004B6565  74 66                           je 0x1404b65cd
004B6567  80 8B A0 04 00 00 02            or byte ptr [rbx + 0x4a0], 2
004B656E  8B D7                           mov edx, edi
004B6570  44 38 5B 0C                     cmp byte ptr [rbx + 0xc], r11b
004B6574  76 24                           jbe 0x1404b659a
004B6576  8B C2                           mov eax, edx
004B6578  41 03 D3                        add edx, r11d
004B657B  48 8D 0C 80                     lea rcx, [rax + rax*4]
004B657F  48 C1 E1 07                     shl rcx, 7
004B6583  48 03 8B 08 05 00 00            add rcx, qword ptr [rbx + 0x508]
004B658A  48 83 61 02 00                  and qword ptr [rcx + 2], 0
004B658F  8D 4A 01                        lea ecx, [rdx + 1]
004B6592  0F B6 43 0C                     movzx eax, byte ptr [rbx + 0xc]
004B6596  3B C8                           cmp ecx, eax
004B6598  72 DC                           jb 0x1404b6576
004B659A  8B C2                           mov eax, edx
004B659C  48 8D 0C 80                     lea rcx, [rax + rax*4]
004B65A0  48 C1 E1 07                     shl rcx, 7
004B65A4  48 03 8B 08 05 00 00            add rcx, qword ptr [rbx + 0x508]
004B65AB  0F B7 41 02                     movzx eax, word ptr [rcx + 2]
004B65AF  66 41 3B C3                     cmp ax, r11w
004B65B3  77 03                           ja 0x1404b65b8
004B65B5  41 8B C3                        mov eax, r11d
004B65B8  66 89 41 02                     mov word ptr [rcx + 2], ax
004B65BC  0F B7 41 04                     movzx eax, word ptr [rcx + 4]
004B65C0  66 41 3B C3                     cmp ax, r11w
004B65C4  77 03                           ja 0x1404b65c9
004B65C6  41 8B C3                        mov eax, r11d
004B65C9  66 89 41 04                     mov word ptr [rcx + 4], ax
004B65CD  48 8B CB                        mov rcx, rbx
004B65D0  E8 C3 9D FE FF                  call 0x1404a0398
004B65D5  0F B7 8C 24 D0 00 00 00         movzx ecx, word ptr [rsp + 0xd0]
004B65DD  41 BB 01 00 00 00               mov r11d, 1
004B65E3  44 8B 05 F6 1D A5 00            mov r8d, dword ptr [rip + 0xa51df6]
004B65EA  66 41 03 CB                     add cx, r11w
004B65EE  44 8B 54 24 2C                  mov r10d, dword ptr [rsp + 0x2c]
004B65F3  44 8B 4C 24 30                  mov r9d, dword ptr [rsp + 0x30]
004B65F8  0F B7 C1                        movzx eax, cx
004B65FB  66 89 8C 24 D0 00 00 00         mov word ptr [rsp + 0xd0], cx
004B6603  41 3B C0                        cmp eax, r8d
004B6606  0F 82 3F FC FF FF               jb 0x1404b624b
004B660C  EB 65                           jmp 0x1404b6673
004B660E  0F B7 D7                        movzx edx, di
004B6611  45 85 C0                        test r8d, r8d
004B6614  74 5D                           je 0x1404b6673
004B6616  45 85 F6                        test r14d, r14d
004B6619  0F 84 BC 00 00 00               je 0x1404b66db
004B661F  0F B7 C2                        movzx eax, dx
004B6622  48 69 C8 10 05 00 00            imul rcx, rax, 0x510
004B6629  48 03 0D A8 1D A5 00            add rcx, qword ptr [rip + 0xa51da8]
004B6630  44 0F B7 49 0A                  movzx r9d, word ptr [rcx + 0xa]
004B6635  66 45 85 C9                     test r9w, r9w
004B6639  74 2C                           je 0x1404b6667
004B663B  8A 81 90 04 00 00               mov al, byte ptr [rcx + 0x490]
004B6641  44 0F B7 15 59 1D A5 00         movzx r10d, word ptr [rip + 0xa51d59]
004B6649  41 02 C2                        add al, r10b
004B664C  0F B6 C0                        movzx eax, al
004B664F  66 41 3B C1                     cmp ax, r9w
004B6653  73 12                           jae 0x1404b6667
004B6655  66 44 01 91 90 04 00 00         add word ptr [rcx + 0x490], r10w
004B665D  0F B7 05 3E 1D A5 00            movzx eax, word ptr [rip + 0xa51d3e]
004B6664  44 2B F0                        sub r14d, eax
004B6667  66 41 03 D3                     add dx, r11w
004B666B  0F B7 C2                        movzx eax, dx
004B666E  41 3B C0                        cmp eax, r8d
004B6671  72 A3                           jb 0x1404b6616
004B6673  45 85 F6                        test r14d, r14d
004B6676  75 96                           jne 0x1404b660e
004B6678  EB 61                           jmp 0x1404b66db
004B667A  0F B7 D7                        movzx edx, di
004B667D  45 85 C0                        test r8d, r8d
004B6680  74 59                           je 0x1404b66db
004B6682  45 85 FF                        test r15d, r15d
004B6685  74 59                           je 0x1404b66e0
004B6687  0F B7 C2                        movzx eax, dx
004B668A  48 69 C8 10 05 00 00            imul rcx, rax, 0x510
004B6691  48 03 0D 40 1D A5 00            add rcx, qword ptr [rip + 0xa51d40]
004B6698  44 0F B7 49 0A                  movzx r9d, word ptr [rcx + 0xa]
004B669D  66 45 85 C9                     test r9w, r9w
004B66A1  74 2C                           je 0x1404b66cf
004B66A3  8A 81 94 04 00 00               mov al, byte ptr [rcx + 0x494]
004B66A9  44 0F B7 15 F1 1C A5 00         movzx r10d, word ptr [rip + 0xa51cf1]
004B66B1  41 02 C2                        add al, r10b
004B66B4  0F B6 C0                        movzx eax, al
004B66B7  66 41 3B C1                     cmp ax, r9w
004B66BB  73 12                           jae 0x1404b66cf
004B66BD  66 44 01 91 94 04 00 00         add word ptr [rcx + 0x494], r10w
004B66C5  0F B7 05 D6 1C A5 00            movzx eax, word ptr [rip + 0xa51cd6]
004B66CC  44 2B F8                        sub r15d, eax
004B66CF  66 41 03 D3                     add dx, r11w
004B66D3  0F B7 C2                        movzx eax, dx
004B66D6  41 3B C0                        cmp eax, r8d
004B66D9  72 A7                           jb 0x1404b6682
004B66DB  45 85 FF                        test r15d, r15d
004B66DE  75 9A                           jne 0x1404b667a
004B66E0  0F B7 F7                        movzx esi, di
004B66E3  45 85 C0                        test r8d, r8d
004B66E6  0F 84 94 00 00 00               je 0x1404b6780
004B66EC  0F B7 C6                        movzx eax, si
004B66EF  48 69 D8 10 05 00 00            imul rbx, rax, 0x510
004B66F6  48 03 1D DB 1C A5 00            add rbx, qword ptr [rip + 0xa51cdb]
004B66FD  0F B7 83 90 04 00 00            movzx eax, word ptr [rbx + 0x490]
004B6704  48 8D BB 94 04 00 00            lea rdi, [rbx + 0x494]
004B670B  0F B7 53 0A                     movzx edx, word ptr [rbx + 0xa]
004B670F  4C 8D B3 96 04 00 00            lea r14, [rbx + 0x496]
004B6716  8B CA                           mov ecx, edx
004B6718  2B C8                           sub ecx, eax
004B671A  0F B7 83 92 04 00 00            movzx eax, word ptr [rbx + 0x492]
004B6721  3B C1                           cmp eax, ecx
004B6723  75 0D                           jne 0x1404b6732
004B6725  0F B7 07                        movzx eax, word ptr [rdi]
004B6728  2B D0                           sub edx, eax
004B672A  41 0F B7 06                     movzx eax, word ptr [r14]
004B672E  3B C2                           cmp eax, edx
004B6730  74 39                           je 0x1404b676b
004B6732  44 8A 0F                        mov r9b, byte ptr [rdi]
004B6735  44 8A 83 90 04 00 00            mov r8b, byte ptr [rbx + 0x490]
004B673C  48 8B 53 10                     mov rdx, qword ptr [rbx + 0x10]
004B6740  0F B7 4B 04                     movzx ecx, word ptr [rbx + 4]
004B6744  E8 93 47 12 00                  call 0x1405daedc
004B6749  0F B7 4B 0A                     movzx ecx, word ptr [rbx + 0xa]
004B674D  41 BB 01 00 00 00               mov r11d, 1
004B6753  0F B7 C1                        movzx eax, cx
004B6756  66 2B 83 90 04 00 00            sub ax, word ptr [rbx + 0x490]
004B675D  66 2B 0F                        sub cx, word ptr [rdi]
004B6760  66 41 89 0E                     mov word ptr [r14], cx
004B6764  66 89 83 92 04 00 00            mov word ptr [rbx + 0x492], ax
004B676B  66 41 03 F3                     add si, r11w
004B676F  0F B7 C6                        movzx eax, si
004B6772  3B 05 68 1C A5 00               cmp eax, dword ptr [rip + 0xa51c68]
004B6778  0F 82 6E FF FF FF               jb 0x1404b66ec
004B677E  33 FF                           xor edi, edi
004B6780  40 38 3D 69 79 A5 00            cmp byte ptr [rip + 0xa57969], dil
004B6787  40 8A D7                        mov dl, dil
004B678A  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
004B678F  8B 9B A0 00 00 00               mov ebx, dword ptr [rbx + 0xa0]
004B6795  74 17                           je 0x1404b67ae
004B6797  8B 05 F7 E8 B0 00               mov eax, dword ptr [rip + 0xb0e8f7]
004B679D  85 C0                           test eax, eax
004B679F  74 0D                           je 0x1404b67ae
004B67A1  85 DB                           test ebx, ebx
004B67A3  74 04                           je 0x1404b67a9
004B67A5  3B C3                           cmp eax, ebx
004B67A7  73 05                           jae 0x1404b67ae
004B67A9  41 8A D3                        mov dl, r11b
004B67AC  8B D8                           mov ebx, eax
004B67AE  44 8B C3                        mov r8d, ebx
004B67B1  33 C9                           xor ecx, ecx
004B67B3  E8 98 D1 03 00                  call 0x1404f3950
004B67B8  85 DB                           test ebx, ebx
004B67BA  75 5D                           jne 0x1404b6819
004B67BC  48 8B 0D 05 1C A5 00            mov rcx, qword ptr [rip + 0xa51c05]
004B67C3  40 88 3D 27 03 B1 00            mov byte ptr [rip + 0xb10327], dil
004B67CA  89 3D 84 CC A6 00               mov dword ptr [rip + 0xa6cc84], edi
004B67D0  48 85 C9                        test rcx, rcx
004B67D3  74 71                           je 0x1404b6846
004B67D5  48 8B 1D DC 1B A5 00            mov rbx, qword ptr [rip + 0xa51bdc]
004B67DC  48 85 DB                        test rbx, rbx
004B67DF  74 65                           je 0x1404b6846
004B67E1  44 8B 05 00 03 B1 00            mov r8d, dword ptr [rip + 0xb10300]
004B67E8  BF FF 00 00 00                  mov edi, 0xff
004B67ED  49 C1 E0 02                     shl r8, 2
004B67F1  8B D7                           mov edx, edi
004B67F3  E8 48 04 21 00                  call 0x1406c6c40
004B67F8  44 8B 05 E9 02 B1 00            mov r8d, dword ptr [rip + 0xb102e9]
004B67FF  8B D7                           mov edx, edi
004B6801  49 C1 E0 02                     shl r8, 2
004B6805  48 8B CB                        mov rcx, rbx
004B6808  E8 33 04 21 00                  call 0x1406c6c40
004B680D  E8 86 F1 E1 FF                  call 0x1402d5998
004B6812  E8 C1 F0 E1 FF                  call 0x1402d58d8
004B6817  EB 2D                           jmp 0x1404b6846
004B6819  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
004B6822  BA 40 42 0F 00                  mov edx, 0xf4240
004B6827  44 8B C3                        mov r8d, ebx
004B682A  C6 05 C0 02 B1 00 01            mov byte ptr [rip + 0xb102c0], 1
004B6831  8B 48 44                        mov ecx, dword ptr [rax + 0x44]
004B6834  48 69 C9 40 42 0F 00            imul rcx, rcx, 0xf4240
004B683B  E8 F0 0C F9 FF                  call 0x140447530
004B6840  89 05 0E CC A6 00               mov dword ptr [rip + 0xa6cc0e], eax
004B6846  E8 AD 87 F0 FF                  call 0x1403beff8
004B684B  EB 05                           jmp 0x1404b6852
004B684D  E8 3E C8 03 00                  call 0x1404f3090
004B6852  48 83 C4 78                     add rsp, 0x78
004B6856  41 5F                           pop r15
004B6858  41 5E                           pop r14
004B685A  41 5D                           pop r13
004B685C  41 5C                           pop r12
004B685E  5F                              pop rdi
004B685F  5E                              pop rsi
004B6860  5D                              pop rbp
004B6861  5B                              pop rbx
004B6862  C3                              ret
004B6863  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PpmParkApplyPolicy(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int16 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned int v_stack_m88;
    unsigned int v_stack_m8C;
    unsigned int v_stack_m90;
    unsigned int v_stack_m94;
    unsigned int v_stack_m98;
    unsigned __int8 v_stack_p10;
    unsigned __int16 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int8 v_stack_p8;

    v_rsp = (v_rsp) - (120);
    result = 0;
    v_rdi = 0;
    v_stack_m68 = v_xmm0;
    *(unsigned int *)(v_rsp + 32) = 0;
    *(unsigned __int64 *)(v_rsp - 88) = 0;
    result = Feature_PpmParkEx__private_IsEnabledDeviceUsageNoInline(a1, a2, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_004B684D;
    if ((*(unsigned __int64 *)(v_rip + 10822241)) != 0) goto loc_004B6184;
    *(unsigned int *)(v_rip + 10932949) = 0;
    goto loc_004B6852;
loc_004B6184:
    v_rsi = (*(unsigned __int64 *)(v_rip + 9773557)) + (40);
    a1 = (a1) * ((int)(*(unsigned int *)(v_rip + 10841210)));
    v_rsi = (v_rsi) + (a1);
    v_stack_m70 = v_rsi;
    result = PpmParkEvalualteSmtUnparkPolicy(*(unsigned __int8 *)(v_rsi + 458), a2, a3, a4);
    a1 = 0;
    v_stack_p8 = 0;
    result = KeGetPrcb(a1, a2, a3, a4);
    v_r12 = 1 + 63;
    if ((*(unsigned __int64 *)(result + 35248)) == 0) {
        result = *(unsigned int *)(v_rip + 11602808);
        a1 = (unsigned __int8)(result);
        if (((unsigned int)(result)) > ((unsigned int)(1 + 63))) { a1 = (unsigned int)(1 + 63); }
        v_stack_p8 = 1;
        v_r12 = (unsigned __int8)(a1);
    }
    a2 = 0;
    a2 = 0;
    a4 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10164284))))))) - (0));
    a2 = 0;
    a2 = 0;
    v_stack_m88 = (unsigned int)(a4);
    v_r10 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10164278))))))) - (0));
    v_stack_p18 = 0;
    v_stack_m8C = (unsigned int)(v_r10);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10822124))) == 0) goto loc_004B6673;
loc_004B624B:
    v_rbx = (v_rbx) * (0);
    v_rbx = (v_rbx) + (*(unsigned __int64 *)(v_rip + 10822008));
    a1 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rbx + 10)))) - ((unsigned int)(*(unsigned __int16 *)(v_rip + 10821946))));
    if (((unsigned int)((unsigned __int8)(a4))) >= = ((unsigned int)(a1))) {
        a2 = *(unsigned __int8 *)(v_rbx + 10);
        a2 = (unsigned __int8)((a2) - ((unsigned __int8)(*(unsigned __int16 *)(v_rip + 10821946))));
    }
    v_r14 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 10164284))) - ((unsigned int)((unsigned __int8)(a2))));
    *(unsigned __int16 *)(v_rbx + 1168) = (unsigned __int16)((unsigned __int8)(a2));
    a3 = (unsigned int)((*(unsigned __int16 *)(v_rbx + 10)) - ((unsigned int)(*(unsigned __int16 *)(v_rip + 10821898))));
    v_stack_m94 = (unsigned int)(v_r14);
    if (((unsigned int)((unsigned __int8)(v_r10))) >= = ((unsigned int)(a3))) {
        a1 = *(unsigned __int8 *)(v_rbx + 10);
        a1 = (unsigned __int8)((a1) - ((unsigned __int8)(*(unsigned __int16 *)(v_rip + 10821898))));
    }
    v_r15 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 10164278))) - ((unsigned int)((unsigned __int8)(a1))));
    v_stack_p10 = 0;
    *(unsigned __int16 *)(v_rbx + 1172) = (unsigned __int16)((unsigned __int8)(a1));
    v_stack_m90 = (unsigned int)(v_r15);
    v_stack_m80 = 0;
    v_stack_m78 = 0;
    if ((*(unsigned __int8 *)(v_rbx + 12)) <= 0) goto loc_004B64CD;
    v_r14 = 0;
loc_004B62F1:
    v_rdi = (0 + 0 * 4) << (7);
    v_rdi = (v_rdi) + (*(unsigned __int64 *)(v_rbx + 1288));
    result = (unsigned int)(-(0));
    a1 = -(a1);
    result = (unsigned int)(-(0));
    a1 = -(a1);
    v_r10 = *(unsigned __int8 *)(a1 + v_rsi * 1 + 156);
    if ((unsigned __int8)(v_stack_p8) != 0) {
        v_r10 = *(unsigned __int8 *)(a1 + v_rsi * 1 + 156);
        if (0 != 0) { v_r10 = 0; }
    }
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rdi)) == 0) goto loc_004B648C;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)(a1 + v_rsi * 1 + 158)))) * ((unsigned int)(*(unsigned __int8 *)(v_rdi))));
    a1 = (unsigned int)((a1) + (50));
    v_r11 = (unsigned int)((0) >> (5));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int8 *)(v_rdi)))))) - ((unsigned int)((unsigned __int8)(v_r11))));
    a1 = (unsigned int)(((unsigned __int8)(v_r10)) * ((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int8 *)(v_rdi))))));
    a1 = (unsigned int)((a1) + (50));
    v_r11 = (unsigned __int8)((v_r11) + (0));
    v_rsi = (unsigned int)((0) >> (5));
    a4 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)(v_rdi)))) - ((unsigned int)((unsigned __int8)(v_rsi))));
    v_rsi = (unsigned __int8)((v_rsi) + (0));
    result = (unsigned int)((unsigned int)(a4));
    if (0 != 0) {
        a1 = (unsigned __int8)(v_r11);
        result = (unsigned __int8)(v_r12);
        if (((unsigned __int8)(v_r11)) >= ((unsigned __int8)(v_r12))) { a1 = (unsigned int)(result); }
        v_r11 = (unsigned __int8)(a1);
    }
    if ((unsigned __int8)(v_rsi) != 0) {
        a1 = (unsigned __int8)(*(unsigned __int16 *)(v_rip + 10821724));
        result = (unsigned __int8)(v_rsi);
        if (((unsigned __int8)(a1)) > ((unsigned __int8)(v_rsi))) { result = (unsigned int)(a1); }
        v_rsi = (unsigned __int8)(result);
    }
    v_stack_m68 = 0;
    a1 = (unsigned __int8)(v_r11);
    if (((unsigned __int8)(v_r11)) < ((unsigned __int8)(v_rsi))) { a1 = (unsigned int)((unsigned __int8)(v_rsi)); }
    v_stack_m98 = (unsigned int)(a1);
    v_stack_m60 = *(unsigned __int64 *)(v_rdi + 24);
    v_stack_m58 = (unsigned __int16)(*(unsigned __int16 *)(v_rbx + 4));
    result = KeEnumerateNextProcessor(v_stack_p20, v_stack_m68, 0, a4);
    if ((unsigned int)(result) != 0) goto loc_004B6444;
    v_r15 = 0;
loc_004B6407:
    result = KeGetPrcb((unsigned int)(v_stack_p20), v_stack_m68, 0, a4);
    v_r13 = 0;
    if ((*(unsigned __int8 *)(result + 35404)) != 0) {
        v_r13 = (0) | (*(unsigned __int64 *)(result + 200));
    }
    result = KeEnumerateNextProcessor(v_stack_p20, v_stack_m68, 0, a4);
    if ((unsigned int)(result) == 0) goto loc_004B6407;
    v_r14 = 0;
loc_004B6444:
    a3 = (v_stack_m80) | (*(unsigned __int64 *)(v_rdi + 32));
    a2 = (v_stack_m78) | (v_r13);
    *(unsigned __int64 *)(v_rdi + 32) = v_r13;
    v_r13 = (unsigned __int8)((v_stack_p10) + ((unsigned __int8)(v_rsi)));
    *(unsigned __int16 *)(v_rdi + 4) = (unsigned __int16)(v_stack_m98);
    v_stack_p10 = (unsigned __int8)(v_r13);
    v_stack_m80 = a3;
    v_stack_m78 = a2;
    *(unsigned __int16 *)(v_rdi + 2) = (unsigned __int16)((unsigned __int8)(v_rsi));
loc_004B648C:
    v_rbp = (unsigned int)((0) + (1));
    if (((unsigned int)(v_rbp)) < ((unsigned int)(*(unsigned __int8 *)(v_rbx + 12)))) goto loc_004B62F1;
    result = *(unsigned __int8 *)(v_rbx + 12);
    v_r11 = 1;
    if (a3 != a2) {
        a1 = *(unsigned __int16 *)(v_rbx + 4);
        a3 = a2;
        a2 = *(unsigned __int64 *)(v_rbx + 16);
        result = PpmEventParkNodeParkHintChanged(a1, a2, a3, a4);
        v_r11 = 1;
    }
    v_rdi = 0;
    if ((unsigned __int8)(v_r13) == 0) {
        a1 = *(unsigned __int16 *)(v_rip + 10821326);
        a2 = *(unsigned __int64 *)(v_rbx + 1288);
        result = *(unsigned __int16 *)(a2 + 4);
        *(unsigned __int16 *)(a2 + 2) = (unsigned __int16)(a1);
        if (((unsigned __int16)(a1)) <= ((unsigned __int16)(result))) { a1 = (unsigned __int16)(result); }
        *(unsigned __int16 *)(a2 + 4) = (unsigned __int16)(a1);
    }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11594564)))) != 2) goto loc_004B6559;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rbx + 1288) + 2))) <= ((unsigned __int16)(v_r11))) {
        a1 = (unsigned int)(v_r11);
    }
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_rbx + 1288) + 2) = (unsigned __int16)(a1);
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rbx + 1288) + 4))) <= ((unsigned __int16)(v_r11))) {
        a1 = (unsigned int)(v_r11);
    }
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_rbx + 1288) + 4) = (unsigned __int16)(a1);
    if ((*(unsigned __int8 *)(v_rbx + 12)) <= ((unsigned __int8)(v_r11))) goto loc_004B65CD;
loc_004B6536:
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_r11))) + ((unsigned int)(v_r11)));
    a1 = ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r11)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r11)))) * 4) << (7);
    a1 = (a1) + (*(unsigned __int64 *)(v_rbx + 1288));
    if (a2 < ((unsigned int)(*(unsigned __int8 *)(v_rbx + 12)))) goto loc_004B6536;
    goto loc_004B65CD;
loc_004B6559:
    if (((unsigned int)(*(unsigned __int8 *)(v_rbx + 12))) != 3) goto loc_004B65CD;
    if ((*(unsigned __int8 *)(v_rbx + 1185)) == 0) goto loc_004B65CD;
    if ((*(unsigned __int8 *)(v_rbx + 12)) <= ((unsigned __int8)(v_r11))) goto loc_004B659A;
loc_004B6576:
    a2 = (unsigned int)((0) + ((unsigned int)(v_r11)));
    a1 = (0 + 0 * 4) << (7);
    a1 = (a1) + (*(unsigned __int64 *)(v_rbx + 1288));
    if (((unsigned int)(a2 + 1)) < ((unsigned int)(*(unsigned __int8 *)(v_rbx + 12)))) goto loc_004B6576;
loc_004B659A:
    a1 = ((unsigned int)(a2) + (unsigned int)(a2) * 4) << (7);
    a1 = (a1) + (*(unsigned __int64 *)(v_rbx + 1288));
    result = *(unsigned __int16 *)(a1 + 2);
    if (((unsigned __int16)(*(unsigned __int16 *)(a1 + 2))) <= ((unsigned __int16)(v_r11))) {
        result = (unsigned int)(v_r11);
    }
    *(unsigned __int16 *)(a1 + 2) = (unsigned __int16)(result);
    result = *(unsigned __int16 *)(a1 + 4);
    if (((unsigned __int16)(*(unsigned __int16 *)(a1 + 4))) <= ((unsigned __int16)(v_r11))) {
        result = (unsigned int)(v_r11);
    }
    *(unsigned __int16 *)(a1 + 4) = (unsigned __int16)(result);
loc_004B65CD:
    result = PpmConfigureRestrictionPolicy(v_rbx, a2, a3, a4);
    a1 = (unsigned __int16)((v_stack_p18) + (1));
    v_stack_p18 = (unsigned __int16)(a1);
    if (((unsigned int)((unsigned __int16)(a1))) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10821110))))) goto loc_004B624B;
    goto loc_004B6673;
loc_004B660E:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10821110))) == 0) goto loc_004B6673;
loc_004B6616:
    if ((unsigned int)((unsigned int)(v_stack_m94)) == 0) goto loc_004B66DB;
    a1 = (a1) * (0);
    a1 = (a1) + (*(unsigned __int64 *)(v_rip + 10821032));
    if ((unsigned __int16)(*(unsigned __int16 *)(a1 + 10)) == 0) goto loc_004B6667;
    result = (unsigned __int8)((*(unsigned __int8 *)(a1 + 1168)) + ((unsigned __int8)(*(unsigned __int16 *)(v_rip + 10820953))));
    result = (unsigned __int8)(result);
    v_r14 = (unsigned int)(v_stack_m94);
    if (((unsigned __int16)((unsigned __int8)(result))) < ((unsigned __int16)(*(unsigned __int16 *)(a1 + 10)))) {
        result = *(unsigned __int16 *)(v_rip + 10820926);
        v_r14 = (unsigned int)(((unsigned int)(v_stack_m94)) - ((unsigned int)(result)));
    }
    a2 = (unsigned __int16)((0) + (1));
    if (((unsigned int)((unsigned __int16)(a2))) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10821110))))) goto loc_004B6616;
loc_004B6673:
    if ((unsigned int)(v_r14) != 0) goto loc_004B660E;
    goto loc_004B66DB;
loc_004B667A:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10821110))) == 0) goto loc_004B66DB;
loc_004B6682:
    if ((unsigned int)((unsigned int)(v_stack_m90)) == 0) goto loc_004B66E0;
    a1 = (a1) * (0);
    a1 = (a1) + (*(unsigned __int64 *)(v_rip + 10820928));
    if ((unsigned __int16)(*(unsigned __int16 *)(a1 + 10)) == 0) goto loc_004B66CF;
    result = (unsigned __int8)((*(unsigned __int8 *)(a1 + 1172)) + ((unsigned __int8)(*(unsigned __int16 *)(v_rip + 10820849))));
    result = (unsigned __int8)(result);
    v_r15 = (unsigned int)(v_stack_m90);
    if (((unsigned __int16)((unsigned __int8)(result))) < ((unsigned __int16)(*(unsigned __int16 *)(a1 + 10)))) {
        result = *(unsigned __int16 *)(v_rip + 10820822);
        v_r15 = (unsigned int)(((unsigned int)(v_stack_m90)) - ((unsigned int)(result)));
    }
    a2 = (unsigned __int16)((0) + (1));
    if (((unsigned int)((unsigned __int16)(a2))) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10821110))))) goto loc_004B6682;
loc_004B66DB:
    if ((unsigned int)(v_r15) != 0) goto loc_004B667A;
loc_004B66E0:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10821110))) == 0) goto loc_004B6780;
loc_004B66EC:
    v_rbx = (v_rbx) * (0);
    v_rbx = (v_rbx) + (*(unsigned __int64 *)(v_rip + 10820827));
    a1 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rbx + 10)))) - ((unsigned int)(*(unsigned __int16 *)(v_rbx + 1168))));
    if (((unsigned int)(*(unsigned __int16 *)(v_rbx + 1170))) != ((unsigned int)(a1))) goto loc_004B6732;
    a2 = (unsigned int)((*(unsigned __int16 *)(v_rbx + 10)) - ((unsigned int)(*(unsigned __int16 *)(v_rbx + 1172))));
    result = *(unsigned __int16 *)(v_rbx + 1174);
    v_r11 = 1;
    if (((unsigned int)(*(unsigned __int16 *)(v_rbx + 1174))) != a2) {
        a4 = *(unsigned __int8 *)(v_rbx + 1172);
        a3 = *(unsigned __int8 *)(v_rbx + 1168);
        a2 = *(unsigned __int64 *)(v_rbx + 16);
        a1 = *(unsigned __int16 *)(v_rbx + 4);
        result = PpmEventParkNodeCapChange(a1, a2, a3, a4);
        a1 = *(unsigned __int16 *)(v_rbx + 10);
        v_r11 = 1;
        result = (unsigned __int16)(a1);
        result = (unsigned __int16)((result) - (*(unsigned __int16 *)(v_rbx + 1168)));
        a1 = (unsigned __int16)((a1) - (*(unsigned __int16 *)(v_rbx + 1172)));
        *(unsigned __int16 *)(v_rbx + 1174) = (unsigned __int16)(a1);
        *(unsigned __int16 *)(v_rbx + 1170) = (unsigned __int16)(result);
    }
    v_rsi = (unsigned __int16)((0) + ((unsigned __int16)(v_r11)));
    if (((unsigned int)((unsigned __int16)(v_rsi))) < (*(unsigned int *)(v_rip + 10820712))) goto loc_004B66EC;
    v_rdi = 0;
loc_004B6780:
    if ((*(unsigned __int8 *)(v_rip + 10844521)) == 0) goto loc_004B67AE;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11593975))) == 0) goto loc_004B67AE;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m70 + 160))) == 0) goto loc_004B67A9;
    v_rbx = (unsigned int)(*(unsigned int *)(v_stack_m70 + 160));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11593975)))) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m70 + 160))))) {
        a2 = (unsigned __int8)(v_r11);
        v_rbx = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11593975)));
    }
    a1 = 0;
    result = PpmEventSoftParkLatencyUpdate(a1, a2, (unsigned int)((unsigned int)(v_rbx)), a4);
    if ((unsigned int)(v_rbx) != 0) goto loc_004B6819;
    *(unsigned __int8 *)(v_rip + 11600679) = 0;
    *(unsigned int *)(v_rip + 10931332) = 0;
    if (*(unsigned __int64 *)(v_rip + 10820613) == 0) goto loc_004B6846;
    if (*(unsigned __int64 *)(v_rip + 10820572) == 0) goto loc_004B6846;
    a3 = ((unsigned int)(*(unsigned int *)(v_rip + 11600640))) << (2);
    result = memset(*(unsigned __int64 *)(v_rip + 10820613), 255, a3, a4);
    a3 = ((unsigned int)(*(unsigned int *)(v_rip + 11600617))) << (2);
    result = memset(*(unsigned __int64 *)(v_rip + 10820572), 255, a3, a4);
    result = KeUpdateSoftParkRankList(*(unsigned __int64 *)(v_rip + 10820572), 255, a3, a4);
    result = PpmEventSoftParkRankListChanged(*(unsigned __int64 *)(v_rip + 10820572), 255, a3, a4);
    goto loc_004B6846;
loc_004B6819:
    *(unsigned __int8 *)(v_rip + 11600576) = 1;
    a1 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 68))) * ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 68)));
    result = PpmConvertTime(a1, (unsigned int)(0xF4240ULL), (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rip + 10820572))), a4);
    *(unsigned int *)(v_rip + 10931214) = (unsigned int)(result);
loc_004B6846:
    result = PpmHeteroHgsCheckContainmentDecision(a1, (unsigned int)(0xF4240ULL), (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rip + 10820572))), a4);
    goto loc_004B6852;
loc_004B684D:
    result = PpmParkApplyPolicyEx(a1, (unsigned int)(0xF4240ULL), (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rip + 10820572))), a4);
loc_004B6852:
    v_rsp = (v_rsp) + (120);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PpmParkApplyPolicy(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint16_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint32_t v_stack_m88;
    uint32_t v_stack_m8C;
    uint32_t v_stack_m90;
    uint32_t v_stack_m94;
    uint32_t v_stack_m98;
    uint8_t v_stack_p10;
    uint16_t v_stack_p18;
    uint64_t v_stack_p20;
    uint8_t v_stack_p8;

    local_rsp = (local_rsp) - (120);
    result = 0;
    local_rdi = 0;
    v_stack_m68 = v_xmm0;
    *(uint32_t *)(local_rsp + 0x20) = 0;
    *(uint64_t *)(local_rsp - 0x58) = 0;
    result = Feature_PpmParkEx__private_IsEnabledDeviceUsageNoInline(Arg1, Arg2, a3, a4);
    if ((uint32_t)(result) != 0) goto loc_004B684D;
    if ((*(uint64_t *)(v_rip + 0xA52261)) != 0) goto loc_004B6184;
    *(uint32_t *)(v_rip + 0xA6D2D5) = 0;
    goto loc_004B6852;
loc_004B6184:
    local_rsi = (*(uint64_t *)(v_rip + 0x9521F5)) + (40);
    Arg1 = (Arg1) * ((int32_t)(*(uint32_t *)(v_rip + 0xA56C7A)));
    local_rsi = (local_rsi) + (Arg1);
    v_stack_m70 = local_rsi;
    result = PpmParkEvalualteSmtUnparkPolicy(*(uint8_t *)(local_rsi + 0x1CA), Arg2, a3, a4);
    Arg1 = 0;
    v_stack_p8 = 0;
    result = KeGetPrcb(Arg1, Arg2, a3, a4);
    local_r12 = 1 + 63;
    if ((*(uint64_t *)(result + 0x89B0)) == 0) {
        result = *(uint32_t *)(v_rip + 0xB10B78);
        Arg1 = (uint8_t)(result);
        if (((uint32_t)(result)) > ((uint32_t)(1 + 63))) { Arg1 = (uint32_t)(1 + 63); }
        v_stack_p8 = 1;
        local_r12 = (uint8_t)(Arg1);
    }
    Arg2 = 0;
    Arg2 = 0;
    a4 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x9B183C))))))) - (0));
    Arg2 = 0;
    Arg2 = 0;
    v_stack_m88 = (uint32_t)(a4);
    local_r10 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x9B1836))))))) - (0));
    v_stack_p18 = 0;
    v_stack_m8C = (uint32_t)(local_r10);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA521EC))) == 0) goto loc_004B6673;
loc_004B624B:
    local_rbx = (local_rbx) * (0);
    local_rbx = (local_rbx) + (*(uint64_t *)(v_rip + 0xA52178));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(local_rbx + 0xA)))) - ((uint32_t)(*(uint16_t *)(v_rip + 0xA5213A))));
    if (((uint32_t)((uint8_t)(a4))) >= = ((uint32_t)(Arg1))) {
        Arg2 = *(uint8_t *)(local_rbx + 0xA);
        Arg2 = (uint8_t)((Arg2) - ((uint8_t)(*(uint16_t *)(v_rip + 0xA5213A))));
    }
    local_r14 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x9B183C))) - ((uint32_t)((uint8_t)(Arg2))));
    *(uint16_t *)(local_rbx + 0x490) = (uint16_t)((uint8_t)(Arg2));
    a3 = (uint32_t)((*(uint16_t *)(local_rbx + 0xA)) - ((uint32_t)(*(uint16_t *)(v_rip + 0xA5210A))));
    v_stack_m94 = (uint32_t)(local_r14);
    if (((uint32_t)((uint8_t)(local_r10))) >= = ((uint32_t)(a3))) {
        Arg1 = *(uint8_t *)(local_rbx + 0xA);
        Arg1 = (uint8_t)((Arg1) - ((uint8_t)(*(uint16_t *)(v_rip + 0xA5210A))));
    }
    local_r15 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x9B1836))) - ((uint32_t)((uint8_t)(Arg1))));
    v_stack_p10 = 0;
    *(uint16_t *)(local_rbx + 0x494) = (uint16_t)((uint8_t)(Arg1));
    v_stack_m90 = (uint32_t)(local_r15);
    v_stack_m80 = 0;
    v_stack_m78 = 0;
    if ((*(uint8_t *)(local_rbx + 0xC)) <= 0) goto loc_004B64CD;
    local_r14 = 0;
loc_004B62F1:
    local_rdi = (0 + 0 * 4) << (7);
    local_rdi = (local_rdi) + (*(uint64_t *)(local_rbx + 0x508));
    result = (uint32_t)(-(0));
    Arg1 = -(Arg1);
    result = (uint32_t)(-(0));
    Arg1 = -(Arg1);
    local_r10 = *(uint8_t *)(Arg1 + local_rsi * 1 + 0x9C);
    if ((uint8_t)(v_stack_p8) != 0) {
        local_r10 = *(uint8_t *)(Arg1 + local_rsi * 1 + 0x9C);
        if (0 != 0) { local_r10 = 0; }
    }
    if ((uint8_t)(*(uint8_t *)(local_rdi)) == 0) goto loc_004B648C;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)(Arg1 + local_rsi * 1 + 0x9E)))) * ((uint32_t)(*(uint8_t *)(local_rdi))));
    Arg1 = (uint32_t)((Arg1) + (50));
    local_r11 = (uint32_t)((0) >> (5));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint8_t *)(local_rdi)))))) - ((uint32_t)((uint8_t)(local_r11))));
    Arg1 = (uint32_t)(((uint8_t)(local_r10)) * ((uint32_t)((uint32_t)((uint32_t)(*(uint8_t *)(local_rdi))))));
    Arg1 = (uint32_t)((Arg1) + (50));
    local_r11 = (uint8_t)((local_r11) + (0));
    local_rsi = (uint32_t)((0) >> (5));
    a4 = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)(local_rdi)))) - ((uint32_t)((uint8_t)(local_rsi))));
    local_rsi = (uint8_t)((local_rsi) + (0));
    result = (uint32_t)((uint32_t)(a4));
    if (0 != 0) {
        Arg1 = (uint8_t)(local_r11);
        result = (uint8_t)(local_r12);
        if (((uint8_t)(local_r11)) >= ((uint8_t)(local_r12))) { Arg1 = (uint32_t)(result); }
        local_r11 = (uint8_t)(Arg1);
    }
    if ((uint8_t)(local_rsi) != 0) {
        Arg1 = (uint8_t)(*(uint16_t *)(v_rip + 0xA5205C));
        result = (uint8_t)(local_rsi);
        if (((uint8_t)(Arg1)) > ((uint8_t)(local_rsi))) { result = (uint32_t)(Arg1); }
        local_rsi = (uint8_t)(result);
    }
    v_stack_m68 = 0;
    Arg1 = (uint8_t)(local_r11);
    if (((uint8_t)(local_r11)) < ((uint8_t)(local_rsi))) { Arg1 = (uint32_t)((uint8_t)(local_rsi)); }
    v_stack_m98 = (uint32_t)(Arg1);
    v_stack_m60 = *(uint64_t *)(local_rdi + 0x18);
    v_stack_m58 = (uint16_t)(*(uint16_t *)(local_rbx + 0x4));
    result = KeEnumerateNextProcessor(v_stack_p20, v_stack_m68, 0, a4);
    if ((uint32_t)(result) != 0) goto loc_004B6444;
    local_r15 = 0;
loc_004B6407:
    result = KeGetPrcb((uint32_t)(v_stack_p20), v_stack_m68, 0, a4);
    local_r13 = 0;
    if ((*(uint8_t *)(result + 0x8A4C)) != 0) {
        local_r13 = (0) | (*(uint64_t *)(result + 0xC8));
    }
    result = KeEnumerateNextProcessor(v_stack_p20, v_stack_m68, 0, a4);
    if ((uint32_t)(result) == 0) goto loc_004B6407;
    local_r14 = 0;
loc_004B6444:
    a3 = (v_stack_m80) | (*(uint64_t *)(local_rdi + 0x20));
    Arg2 = (v_stack_m78) | (local_r13);
    *(uint64_t *)(local_rdi + 0x20) = local_r13;
    local_r13 = (uint8_t)((v_stack_p10) + ((uint8_t)(local_rsi)));
    *(uint16_t *)(local_rdi + 0x4) = (uint16_t)(v_stack_m98);
    v_stack_p10 = (uint8_t)(local_r13);
    v_stack_m80 = a3;
    v_stack_m78 = Arg2;
    *(uint16_t *)(local_rdi + 0x2) = (uint16_t)((uint8_t)(local_rsi));
loc_004B648C:
    local_rbp = (uint32_t)((0) + (1));
    if (((uint32_t)(local_rbp)) < ((uint32_t)(*(uint8_t *)(local_rbx + 0xC)))) goto loc_004B62F1;
    result = *(uint8_t *)(local_rbx + 0xC);
    local_r11 = 1;
    if (a3 != Arg2) {
        Arg1 = *(uint16_t *)(local_rbx + 0x4);
        a3 = Arg2;
        Arg2 = *(uint64_t *)(local_rbx + 0x10);
        result = PpmEventParkNodeParkHintChanged(Arg1, Arg2, a3, a4);
        local_r11 = 1;
    }
    local_rdi = 0;
    if ((uint8_t)(local_r13) == 0) {
        Arg1 = *(uint16_t *)(v_rip + 0xA51ECE);
        Arg2 = *(uint64_t *)(local_rbx + 0x508);
        result = *(uint16_t *)(Arg2 + 0x4);
        *(uint16_t *)(Arg2 + 0x2) = (uint16_t)(Arg1);
        if (((uint16_t)(Arg1)) <= ((uint16_t)(result))) { Arg1 = (uint16_t)(result); }
        *(uint16_t *)(Arg2 + 0x4) = (uint16_t)(Arg1);
    }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB0EB44)))) != 2) goto loc_004B6559;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(local_rbx + 0x508) + 0x2))) <= ((uint16_t)(local_r11))) {
        Arg1 = (uint32_t)(local_r11);
    }
    *(uint16_t *)(*(uint64_t *)(local_rbx + 0x508) + 0x2) = (uint16_t)(Arg1);
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(local_rbx + 0x508) + 0x4))) <= ((uint16_t)(local_r11))) {
        Arg1 = (uint32_t)(local_r11);
    }
    *(uint16_t *)(*(uint64_t *)(local_rbx + 0x508) + 0x4) = (uint16_t)(Arg1);
    if ((*(uint8_t *)(local_rbx + 0xC)) <= ((uint8_t)(local_r11))) goto loc_004B65CD;
loc_004B6536:
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_r11))) + ((uint32_t)(local_r11)));
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r11)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r11)))) * 4) << (7);
    Arg1 = (Arg1) + (*(uint64_t *)(local_rbx + 0x508));
    if (Arg2 < ((uint32_t)(*(uint8_t *)(local_rbx + 0xC)))) goto loc_004B6536;
    goto loc_004B65CD;
loc_004B6559:
    if (((uint32_t)(*(uint8_t *)(local_rbx + 0xC))) != 3) goto loc_004B65CD;
    if ((*(uint8_t *)(local_rbx + 0x4A1)) == 0) goto loc_004B65CD;
    if ((*(uint8_t *)(local_rbx + 0xC)) <= ((uint8_t)(local_r11))) goto loc_004B659A;
loc_004B6576:
    Arg2 = (uint32_t)((0) + ((uint32_t)(local_r11)));
    Arg1 = (0 + 0 * 4) << (7);
    Arg1 = (Arg1) + (*(uint64_t *)(local_rbx + 0x508));
    if (((uint32_t)(Arg2 + 1)) < ((uint32_t)(*(uint8_t *)(local_rbx + 0xC)))) goto loc_004B6576;
loc_004B659A:
    Arg1 = ((uint32_t)(Arg2) + (uint32_t)(Arg2) * 4) << (7);
    Arg1 = (Arg1) + (*(uint64_t *)(local_rbx + 0x508));
    result = *(uint16_t *)(Arg1 + 0x2);
    if (((uint16_t)(*(uint16_t *)(Arg1 + 0x2))) <= ((uint16_t)(local_r11))) {
        result = (uint32_t)(local_r11);
    }
    *(uint16_t *)(Arg1 + 0x2) = (uint16_t)(result);
    result = *(uint16_t *)(Arg1 + 0x4);
    if (((uint16_t)(*(uint16_t *)(Arg1 + 0x4))) <= ((uint16_t)(local_r11))) {
        result = (uint32_t)(local_r11);
    }
    *(uint16_t *)(Arg1 + 0x4) = (uint16_t)(result);
loc_004B65CD:
    result = PpmConfigureRestrictionPolicy(local_rbx, Arg2, a3, a4);
    Arg1 = (uint16_t)((v_stack_p18) + (1));
    v_stack_p18 = (uint16_t)(Arg1);
    if (((uint32_t)((uint16_t)(Arg1))) < ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA51DF6))))) goto loc_004B624B;
    goto loc_004B6673;
loc_004B660E:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA51DF6))) == 0) goto loc_004B6673;
loc_004B6616:
    if ((uint32_t)((uint32_t)(v_stack_m94)) == 0) goto loc_004B66DB;
    Arg1 = (Arg1) * (0);
    Arg1 = (Arg1) + (*(uint64_t *)(v_rip + 0xA51DA8));
    if ((uint16_t)(*(uint16_t *)(Arg1 + 0xA)) == 0) goto loc_004B6667;
    result = (uint8_t)((*(uint8_t *)(Arg1 + 0x490)) + ((uint8_t)(*(uint16_t *)(v_rip + 0xA51D59))));
    result = (uint8_t)(result);
    local_r14 = (uint32_t)(v_stack_m94);
    if (((uint16_t)((uint8_t)(result))) < ((uint16_t)(*(uint16_t *)(Arg1 + 0xA)))) {
        result = *(uint16_t *)(v_rip + 0xA51D3E);
        local_r14 = (uint32_t)(((uint32_t)(v_stack_m94)) - ((uint32_t)(result)));
    }
    Arg2 = (uint16_t)((0) + (1));
    if (((uint32_t)((uint16_t)(Arg2))) < ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA51DF6))))) goto loc_004B6616;
loc_004B6673:
    if ((uint32_t)(local_r14) != 0) goto loc_004B660E;
    goto loc_004B66DB;
loc_004B667A:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA51DF6))) == 0) goto loc_004B66DB;
loc_004B6682:
    if ((uint32_t)((uint32_t)(v_stack_m90)) == 0) goto loc_004B66E0;
    Arg1 = (Arg1) * (0);
    Arg1 = (Arg1) + (*(uint64_t *)(v_rip + 0xA51D40));
    if ((uint16_t)(*(uint16_t *)(Arg1 + 0xA)) == 0) goto loc_004B66CF;
    result = (uint8_t)((*(uint8_t *)(Arg1 + 0x494)) + ((uint8_t)(*(uint16_t *)(v_rip + 0xA51CF1))));
    result = (uint8_t)(result);
    local_r15 = (uint32_t)(v_stack_m90);
    if (((uint16_t)((uint8_t)(result))) < ((uint16_t)(*(uint16_t *)(Arg1 + 0xA)))) {
        result = *(uint16_t *)(v_rip + 0xA51CD6);
        local_r15 = (uint32_t)(((uint32_t)(v_stack_m90)) - ((uint32_t)(result)));
    }
    Arg2 = (uint16_t)((0) + (1));
    if (((uint32_t)((uint16_t)(Arg2))) < ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA51DF6))))) goto loc_004B6682;
loc_004B66DB:
    if ((uint32_t)(local_r15) != 0) goto loc_004B667A;
loc_004B66E0:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA51DF6))) == 0) goto loc_004B6780;
loc_004B66EC:
    local_rbx = (local_rbx) * (0);
    local_rbx = (local_rbx) + (*(uint64_t *)(v_rip + 0xA51CDB));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(local_rbx + 0xA)))) - ((uint32_t)(*(uint16_t *)(local_rbx + 0x490))));
    if (((uint32_t)(*(uint16_t *)(local_rbx + 0x492))) != ((uint32_t)(Arg1))) goto loc_004B6732;
    Arg2 = (uint32_t)((*(uint16_t *)(local_rbx + 0xA)) - ((uint32_t)(*(uint16_t *)(local_rbx + 0x494))));
    result = *(uint16_t *)(local_rbx + 0x496);
    local_r11 = 1;
    if (((uint32_t)(*(uint16_t *)(local_rbx + 0x496))) != Arg2) {
        a4 = *(uint8_t *)(local_rbx + 0x494);
        a3 = *(uint8_t *)(local_rbx + 0x490);
        Arg2 = *(uint64_t *)(local_rbx + 0x10);
        Arg1 = *(uint16_t *)(local_rbx + 0x4);
        result = PpmEventParkNodeCapChange(Arg1, Arg2, a3, a4);
        Arg1 = *(uint16_t *)(local_rbx + 0xA);
        local_r11 = 1;
        result = (uint16_t)(Arg1);
        result = (uint16_t)((result) - (*(uint16_t *)(local_rbx + 0x490)));
        Arg1 = (uint16_t)((Arg1) - (*(uint16_t *)(local_rbx + 0x494)));
        *(uint16_t *)(local_rbx + 0x496) = (uint16_t)(Arg1);
        *(uint16_t *)(local_rbx + 0x492) = (uint16_t)(result);
    }
    local_rsi = (uint16_t)((0) + ((uint16_t)(local_r11)));
    if (((uint32_t)((uint16_t)(local_rsi))) < (*(uint32_t *)(v_rip + 0xA51C68))) goto loc_004B66EC;
    local_rdi = 0;
loc_004B6780:
    if ((*(uint8_t *)(v_rip + 0xA57969)) == 0) goto loc_004B67AE;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB0E8F7))) == 0) goto loc_004B67AE;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m70 + 0xA0))) == 0) goto loc_004B67A9;
    local_rbx = (uint32_t)(*(uint32_t *)(v_stack_m70 + 0xA0));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB0E8F7)))) < ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m70 + 0xA0))))) {
        Arg2 = (uint8_t)(local_r11);
        local_rbx = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB0E8F7)));
    }
    Arg1 = 0;
    result = PpmEventSoftParkLatencyUpdate(Arg1, Arg2, (uint32_t)((uint32_t)(local_rbx)), a4);
    if ((uint32_t)(local_rbx) != 0) goto loc_004B6819;
    *(uint8_t *)(v_rip + 0xB10327) = 0;
    *(uint32_t *)(v_rip + 0xA6CC84) = 0;
    if (*(uint64_t *)(v_rip + 0xA51C05) == 0) goto loc_004B6846;
    if (*(uint64_t *)(v_rip + 0xA51BDC) == 0) goto loc_004B6846;
    a3 = ((uint32_t)(*(uint32_t *)(v_rip + 0xB10300))) << (2);
    result = memset(*(uint64_t *)(v_rip + 0xA51C05), 255, a3, a4);
    a3 = ((uint32_t)(*(uint32_t *)(v_rip + 0xB102E9))) << (2);
    result = memset(*(uint64_t *)(v_rip + 0xA51BDC), 255, a3, a4);
    result = KeUpdateSoftParkRankList(*(uint64_t *)(v_rip + 0xA51BDC), 255, a3, a4);
    result = PpmEventSoftParkRankListChanged(*(uint64_t *)(v_rip + 0xA51BDC), 255, a3, a4);
    goto loc_004B6846;
loc_004B6819:
    *(uint8_t *)(v_rip + 0xB102C0) = 1;
    Arg1 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x44))) * ((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x44)));
    result = PpmConvertTime(Arg1, (uint32_t)(0xF4240ULL), (uint32_t)((uint32_t)(*(uint64_t *)(v_rip + 0xA51BDC))), a4);
    *(uint32_t *)(v_rip + 0xA6CC0E) = (uint32_t)(result);
loc_004B6846:
    result = PpmHeteroHgsCheckContainmentDecision(Arg1, (uint32_t)(0xF4240ULL), (uint32_t)((uint32_t)(*(uint64_t *)(v_rip + 0xA51BDC))), a4);
    goto loc_004B6852;
loc_004B684D:
    result = PpmParkApplyPolicyEx(Arg1, (uint32_t)(0xF4240ULL), (uint32_t)((uint32_t)(*(uint64_t *)(v_rip + 0xA51BDC))), a4);
loc_004B6852:
    local_rsp = (local_rsp) + (120);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004B613C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
