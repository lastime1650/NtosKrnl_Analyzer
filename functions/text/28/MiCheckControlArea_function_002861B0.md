# MiCheckControlArea

- RVA: `0x002861B0`–`0x002865DE` (길이 `1,070` bytes)
- VA: `0x00000001402861B0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00066BC0`
- 디코드: `267`개 명령, `1,070/1,070` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **28**; 고유 호출 대상: **22**
- 직접 호출자로 확인된 함수: **11**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x00286279` → [MiImageUnused](../47/MiImageUnused_function_0047AD6C.md) (function, `0x0047AD6C`)
- `0x002862B7` → [MiReleaseSpinLockExclusive](../24/MiReleaseSpinLockExclusive_function_002482C0.md) (function, `0x002482C0`)
- `0x002862E4` → [MiWalkEntireImage](../36/MiWalkEntireImage_function_00365D70.md) (function, `0x00365D70`)
- `0x002862EC` → [MiDeleteDebuggerPatches](../4B/MiDeleteDebuggerPatches_function_004B7EAC.md) (function, `0x004B7EAC`)
- `0x00286319` → [MiInsertUnusedSegment](../44/MiInsertUnusedSegment_function_004443DC.md) (function, `0x004443DC`)
- `0x00286370` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x00286380` → [MiReleaseControlAreaWaiters](MiReleaseControlAreaWaiters_function_002865F0.md) (function, `0x002865F0`)
- `0x002863B0` → [MiReturnResident](MiReturnResident_function_00286890.md) (function, `0x00286890`)
- `0x002863C0` → [MiReturnCrossPartitionCharges](MiReturnCrossPartitionCharges_function_002867D0.md) (function, `0x002867D0`)
- `0x002863CA` → [MiReturnImageBase](../../page/98/MiReturnImageBase_function_00988B00.md) (function, `0x00988B00`)
- `0x00286418` → [ExReleaseSpinLockExclusive](../2C/ExReleaseSpinLockExclusive_function_002C0EF0.md) (function, `0x002C0EF0`)
- `0x00286420` → [MiSegmentDelete](../../page/A1/MiSegmentDelete_function_00A1FBB4.md) (function, `0x00A1FBB4`)
- `0x0028643A` → [ExReleaseSpinLockExclusiveFromDpcLevel](../24/ExReleaseSpinLockExclusiveFromDpcLevel_function_002497E0.md) (function, `0x002497E0`)
- `0x00286442` → [MiSegmentDelete](../../page/A1/MiSegmentDelete_function_00A1FBB4.md) (function, `0x00A1FBB4`)
- `0x00286457` → [MiClearFilePointer](../46/MiClearFilePointer_function_00463044.md) (function, `0x00463044`)
- `0x00286478` → [ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented](../2C/ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented_function_002C0F44.md) (function, `0x002C0F44`)
- `0x00286499` → [ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented](../2C/ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented_function_002C0F44.md) (function, `0x002C0F44`)
- `0x002864B2` → [MiShouldTrimUnusedSegments](../49/MiShouldTrimUnusedSegments_function_0049D7AC.md) (function, `0x0049D7AC`)
- `0x002864C1` → [PsGetNextPartition](../3B/PsGetNextPartition_function_003B9D5C.md) (function, `0x003B9D5C`)
- `0x002864EB` → [KeSetEvent](../33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x002864F3` → [PsGetNextPartition](../3B/PsGetNextPartition_function_003B9D5C.md) (function, `0x003B9D5C`)
- `0x00286517` → [MiCleanSection](../46/MiCleanSection_function_00462E1C.md) (function, `0x00462E1C`)
- `0x00286530` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x0028656E` → [MiImageUnused](../47/MiImageUnused_function_0047AD6C.md) (function, `0x0047AD6C`)
- `0x00286576` → [MiClearFilePointer](../46/MiClearFilePointer_function_00463044.md) (function, `0x00463044`)
- `0x00286585` → [MiReturnImageBase](../../page/98/MiReturnImageBase_function_00988B00.md) (function, `0x00988B00`)
- `0x002865A2` → [MiPurgeImageSection](../../page/AD/MiPurgeImageSection_function_00ADBFF4.md) (function, `0x00ADBFF4`)
- `0x002865D4` → [MiReturnCommit](../24/MiReturnCommit_function_00248410.md) (function, `0x00248410`)

### Direct callers
- [sub_00285E76](Unknown_function_00285E76.md) at `0x00285F40`
- [sub_002860AF](Unknown_function_002860AF.md) at `0x0028615D`
- [sub_00293C9B](../29/Unknown_function_00293C9B.md) at `0x00293F30`
- [MiRemoveMappedPtes](../29/MiRemoveMappedPtes_function_00296A50.md) at `0x00296B9E`
- [MiFlushRelease](../29/MiFlushRelease_function_002982C0.md) at `0x00298384`
- [MiAddViewsForSection](../32/MiAddViewsForSection_function_00324990.md) at `0x00324E62`
- [MmPurgeSection](../38/MmPurgeSection_function_0038B450.md) at `0x0038B664`
- [MiDereferenceControlAreaBySection](../45/MiDereferenceControlAreaBySection_function_00458348.md) at `0x0045836D`
- [MiReleaseFaultCharges](../47/MiReleaseFaultCharges_function_004798C8.md) at `0x00479934`
- [MiDereferenceControlArea](../47/MiDereferenceControlArea_function_00479A20.md) at `0x00479A3F`
- [MiRemoveSystemCacheReferences](../4C/MiRemoveSystemCacheReferences_function_004CFE50.md) at `0x004CFEB4`

### Static image references
- `0x002861D3` → RVA `0x00E30088` (`.data`; read)
- `0x0028634B` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x0028635F` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x00286385` → RVA `0x00E3D840` (`.data`; read)
- `0x0028638C` → RVA `0x00E3CEE0` (`.data`; read)
- `0x00286461` → RVA `0x00F0DE58` (`.data`; read)
- `0x002864AB` → RVA `0x00E38D00` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **5**
  - `0x002863CA` → [MiReturnImageBase](../../page/98/MiReturnImageBase_function_00988B00.md) (`.text` → `PAGE`)
  - `0x00286420` → [MiSegmentDelete](../../page/A1/MiSegmentDelete_function_00A1FBB4.md) (`.text` → `PAGE`)
  - `0x00286442` → [MiSegmentDelete](../../page/A1/MiSegmentDelete_function_00A1FBB4.md) (`.text` → `PAGE`)
  - `0x00286585` → [MiReturnImageBase](../../page/98/MiReturnImageBase_function_00988B00.md) (`.text` → `PAGE`)
  - `0x002865A2` → [MiPurgeImageSection](../../page/AD/MiPurgeImageSection_function_00ADBFF4.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002861B0  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
002861B5  55                              push rbp
002861B6  56                              push rsi
002861B7  57                              push rdi
002861B8  41 54                           push r12
002861BA  41 55                           push r13
002861BC  41 56                           push r14
002861BE  41 57                           push r15
002861C0  48 83 EC 40                     sub rsp, 0x40
002861C4  44 0F B7 41 3C                  movzx r8d, word ptr [rcx + 0x3c]
002861C9  45 33 ED                        xor r13d, r13d
002861CC  4C 8B 61 40                     mov r12, qword ptr [rcx + 0x40]
002861D0  45 33 F6                        xor r14d, r14d
002861D3  48 8B 05 AE 9E BA 00            mov rax, qword ptr [rip + 0xba9eae]
002861DA  33 FF                           xor edi, edi
002861DC  33 DB                           xor ebx, ebx
002861DE  48 C7 44 24 20 FF FF FF FF      mov qword ptr [rsp + 0x20], 0xffffffffffffffff
002861E7  4D 85 E4                        test r12, r12
002861EA  0F 57 C0                        xorps xmm0, xmm0
002861ED  0F B6 F2                        movzx esi, dl
002861F0  48 8B E9                        mov rbp, rcx
002861F3  41 0F 95 C5                     setne r13b
002861F7  41 81 E0 FF 03 00 00            and r8d, 0x3ff
002861FE  F3 0F 7F 44 24 28               movdqu xmmword ptr [rsp + 0x28], xmm0
00286204  4E 8B 3C C0                     mov r15, qword ptr [rax + r8*8]
00286208  48 39 59 28                     cmp qword ptr [rcx + 0x28], rbx
0028620C  74 39                           je 0x140286247
0028620E  48 83 C1 50                     add rcx, 0x50
00286212  48 39 19                        cmp qword ptr [rcx], rbx
00286215  0F 84 0A 01 00 00               je 0x140286325
0028621B  48 8B 11                        mov rdx, qword ptr [rcx]
0028621E  BB 04 00 00 00                  mov ebx, 4
00286223  8B 42 08                        mov eax, dword ptr [rdx + 8]
00286226  4C 8B 02                        mov r8, qword ptr [rdx]
00286229  A8 03                           test al, 3
0028622B  0F 84 72 02 00 00               je 0x1402864a3
00286231  4C 89 32                        mov qword ptr [rdx], r14
00286234  4C 8B F2                        mov r14, rdx
00286237  4C 89 01                        mov qword ptr [rcx], r8
0028623A  49 8B D0                        mov rdx, r8
0028623D  4D 85 C0                        test r8, r8
00286240  75 E1                           jne 0x140286223
00286242  E9 EF 00 00 00                  jmp 0x140286336
00286247  48 39 59 18                     cmp qword ptr [rcx + 0x18], rbx
0028624B  75 C1                           jne 0x14028620e
0028624D  8B 41 38                        mov eax, dword ptr [rcx + 0x38]
00286250  49 F7 C4 F0 FF FF FF            test r12, -0x10
00286257  0F 84 CD 01 00 00               je 0x14028642a
0028625D  48 39 59 20                     cmp qword ptr [rcx + 0x20], rbx
00286261  0F 84 E5 01 00 00               je 0x14028644c
00286267  A8 20                           test al, 0x20
00286269  0F 84 9A 00 00 00               je 0x140286309
0028626F  4C 8D 44 24 20                  lea r8, [rsp + 0x20]
00286274  BA 01 00 00 00                  mov edx, 1
00286279  E8 EE 4A 1F 00                  call 0x14047ad6c
0028627E  8B 4D 38                        mov ecx, dword ptr [rbp + 0x38]
00286281  BA 10 00 00 00                  mov edx, 0x10
00286286  0F BA E1 11                     bt ecx, 0x11
0028628A  0F 82 2F 03 00 00               jb 0x1402865bf
00286290  F6 45 60 01                     test byte ptr [rbp + 0x60], 1
00286294  48 8D 45 48                     lea rax, [rbp + 0x48]
00286298  74 04                           je 0x14028629e
0028629A  8B DA                           mov ebx, edx
0028629C  EB 04                           jmp 0x1402862a2
0028629E  3B DA                           cmp ebx, edx
002862A0  75 1A                           jne 0x1402862bc
002862A2  83 C9 04                        or ecx, 4
002862A5  48 C7 45 28 01 00 00 00         mov qword ptr [rbp + 0x28], 1
002862AD  89 4D 38                        mov dword ptr [rbp + 0x38], ecx
002862B0  40 0F B6 D6                     movzx edx, sil
002862B4  48 8B C8                        mov rcx, rax
002862B7  E8 04 20 FC FF                  call 0x1402482c0
002862BC  8B 45 38                        mov eax, dword ptr [rbp + 0x38]
002862BF  25 00 00 02 08                  and eax, 0x8020000
002862C4  3D 00 00 02 00                  cmp eax, 0x20000
002862C9  0F 84 B1 02 00 00               je 0x140286580
002862CF  F6 45 60 01                     test byte ptr [rbp + 0x60], 1
002862D3  74 1C                           je 0x1402862f1
002862D5  33 D2                           xor edx, edx
002862D7  41 B9 FF FF FF FF               mov r9d, 0xffffffff
002862DD  48 8B CD                        mov rcx, rbp
002862E0  44 8D 42 20                     lea r8d, [rdx + 0x20]
002862E4  E8 87 FA 0D 00                  call 0x140365d70
002862E9  48 8B CD                        mov rcx, rbp
002862EC  E8 BB 1B 23 00                  call 0x1404b7eac
002862F1  83 FB 10                        cmp ebx, 0x10
002862F4  0F 83 2F 02 00 00               jae 0x140286529
002862FA  8B C3                           mov eax, ebx
002862FC  F6 C3 08                        test bl, 8
002862FF  0F 85 AF 02 00 00               jne 0x1402865b4
00286305  A8 02                           test al, 2
00286307  75 18                           jne 0x140286321
00286309  F7 45 38 00 00 04 00            test dword ptr [rbp + 0x38], 0x40000
00286310  0F 85 0B 02 00 00               jne 0x140286521
00286316  48 8B CD                        mov rcx, rbp
00286319  E8 BE E0 1B 00                  call 0x1404443dc
0028631E  48 8B F8                        mov rdi, rax
00286321  48 8D 4D 50                     lea rcx, [rbp + 0x50]
00286325  F6 C3 04                        test bl, 4
00286328  74 0F                           je 0x140286339
0028632A  48 8B 11                        mov rdx, qword ptr [rcx]
0028632D  48 85 D2                        test rdx, rdx
00286330  0F 85 ED FE FF FF               jne 0x140286223
00286336  83 E3 FB                        and ebx, 0xfffffffb
00286339  85 DB                           test ebx, ebx
0028633B  0F 85 C0 00 00 00               jne 0x140286401
00286341  40 80 FE 11                     cmp sil, 0x11
00286345  0F 84 9D 00 00 00               je 0x1402863e8
0028634B  F6 05 B4 07 D4 00 01            test byte ptr [rip + 0xd407b4], 1
00286352  0F 85 09 01 00 00               jne 0x140286461
00286358  C7 45 48 00 00 00 00            mov dword ptr [rbp + 0x48], 0
0028635F  83 3D BA 09 D4 00 00            cmp dword ptr [rip + 0xd409ba], 0
00286366  74 0D                           je 0x140286375
00286368  44 0F 20 C1                     mov rcx, cr8
0028636C  40 0F B6 D6                     movzx edx, sil
00286370  E8 23 F3 26 00                  call 0x1404f5698
00286375  40 0F B6 C6                     movzx eax, sil
00286379  44 0F 22 C0                     mov cr8, rax
0028637D  49 8B CE                        mov rcx, r14
00286380  E8 6B 02 00 00                  call 0x1402865f0
00286385  48 8B 0D B4 74 BB 00            mov rcx, qword ptr [rip + 0xbb74b4]
0028638C  48 8B 05 4D 6B BB 00            mov rax, qword ptr [rip + 0xbb6b4d]
00286393  48 3B C8                        cmp rcx, rax
00286396  0F 83 0F 01 00 00               jae 0x1402864ab
0028639C  48 85 FF                        test rdi, rdi
0028639F  74 24                           je 0x1402863c5
002863A1  4D 85 E4                        test r12, r12
002863A4  0F 85 21 02 00 00               jne 0x1402865cb
002863AA  48 8B D7                        mov rdx, rdi
002863AD  49 8B CF                        mov rcx, r15
002863B0  E8 DB 04 00 00                  call 0x140286890
002863B5  4C 8B CF                        mov r9, rdi
002863B8  45 8B C5                        mov r8d, r13d
002863BB  33 D2                           xor edx, edx
002863BD  49 8B CF                        mov rcx, r15
002863C0  E8 0B 04 00 00                  call 0x1402867d0
002863C5  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
002863CA  E8 31 27 70 00                  call 0x140988b00
002863CF  48 8B 9C 24 90 00 00 00         mov rbx, qword ptr [rsp + 0x90]
002863D7  48 83 C4 40                     add rsp, 0x40
002863DB  41 5F                           pop r15
002863DD  41 5E                           pop r14
002863DF  41 5D                           pop r13
002863E1  41 5C                           pop r12
002863E3  5F                              pop rdi
002863E4  5E                              pop rsi
002863E5  5D                              pop rbp
002863E6  C3                              ret
002863E7  CC                              int3
002863E8  F6 05 17 07 D4 00 01            test byte ptr [rip + 0xd40717], 1
002863EF  0F 85 8D 00 00 00               jne 0x140286482
002863F5  C7 45 48 00 00 00 00            mov dword ptr [rbp + 0x48], 0
002863FC  E9 7C FF FF FF                  jmp 0x14028637d
00286401  F6 C3 01                        test bl, 1
00286404  0F 85 FB 00 00 00               jne 0x140286505
0028640A  48 8D 4D 48                     lea rcx, [rbp + 0x48]
0028640E  40 80 FE 11                     cmp sil, 0x11
00286412  74 26                           je 0x14028643a
00286414  40 0F B6 D6                     movzx edx, sil
00286418  E8 D3 AA 03 00                  call 0x1402c0ef0
0028641D  48 8B CD                        mov rcx, rbp
00286420  E8 8F 97 79 00                  call 0x140a1fbb4
00286425  E9 72 FF FF FF                  jmp 0x14028639c
0028642A  83 C8 01                        or eax, 1
0028642D  BB 02 00 00 00                  mov ebx, 2
00286432  89 41 38                        mov dword ptr [rcx + 0x38], eax
00286435  E9 E7 FE FF FF                  jmp 0x140286321
0028643A  E8 A1 33 FC FF                  call 0x1402497e0
0028643F  48 8B CD                        mov rcx, rbp
00286442  E8 6D 97 79 00                  call 0x140a1fbb4
00286447  E9 50 FF FF FF                  jmp 0x14028639c
0028644C  83 C8 01                        or eax, 1
0028644F  BB 02 00 00 00                  mov ebx, 2
00286454  89 41 38                        mov dword ptr [rcx + 0x38], eax
00286457  E8 E8 CB 1D 00                  call 0x140463044
0028645C  E9 C0 FE FF FF                  jmp 0x140286321
00286461  8B 05 F1 79 C8 00               mov eax, dword ptr [rip + 0xc879f1]
00286467  85 C0                           test eax, eax
00286469  0F 85 E9 FE FF FF               jne 0x140286358
0028646F  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
00286474  48 8D 4D 48                     lea rcx, [rbp + 0x48]
00286478  E8 C7 AA 03 00                  call 0x1402c0f44
0028647D  E9 DD FE FF FF                  jmp 0x14028635f
00286482  8B 05 D0 79 C8 00               mov eax, dword ptr [rip + 0xc879d0]
00286488  85 C0                           test eax, eax
0028648A  0F 85 65 FF FF FF               jne 0x1402863f5
00286490  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
00286495  48 8D 4D 48                     lea rcx, [rbp + 0x48]
00286499  E8 A6 AA 03 00                  call 0x1402c0f44
0028649E  E9 DA FE FF FF                  jmp 0x14028637d
002864A3  48 8B CA                        mov rcx, rdx
002864A6  E9 8F FD FF FF                  jmp 0x14028623a
002864AB  48 8D 0D 4E 28 BB 00            lea rcx, [rip + 0xbb284e]
002864B2  E8 F5 72 21 00                  call 0x14049d7ac
002864B7  85 C0                           test eax, eax
002864B9  0F 84 DD FE FF FF               je 0x14028639c
002864BF  33 C9                           xor ecx, ecx
002864C1  E8 96 38 13 00                  call 0x1403b9d5c
002864C6  48 8B D8                        mov rbx, rax
002864C9  48 85 C0                        test rax, rax
002864CC  0F 84 CA FE FF FF               je 0x14028639c
002864D2  48 8B 0B                        mov rcx, qword ptr [rbx]
002864D5  48 83 B9 38 08 00 00 00         cmp qword ptr [rcx + 0x838], 0
002864DD  74 11                           je 0x1402864f0
002864DF  48 81 C1 F8 06 00 00            add rcx, 0x6f8
002864E6  45 33 C0                        xor r8d, r8d
002864E9  33 D2                           xor edx, edx
002864EB  E8 20 8E 0B 00                  call 0x14033f310
002864F0  48 8B CB                        mov rcx, rbx
002864F3  E8 64 38 13 00                  call 0x1403b9d5c
002864F8  48 8B D8                        mov rbx, rax
002864FB  48 85 C0                        test rax, rax
002864FE  75 D2                           jne 0x1402864d2
00286500  E9 97 FE FF FF                  jmp 0x14028639c
00286505  45 33 C0                        xor r8d, r8d
00286508  48 C7 45 28 01 00 00 00         mov qword ptr [rbp + 0x28], 1
00286510  40 0F B6 D6                     movzx edx, sil
00286514  48 8B CD                        mov rcx, rbp
00286517  E8 00 C9 1D 00                  call 0x140462e1c
0028651C  E9 7B FE FF FF                  jmp 0x14028639c
00286521  83 CB 01                        or ebx, 1
00286524  E9 F8 FD FF FF                  jmp 0x140286321
00286529  48 8D 4D 48                     lea rcx, [rbp + 0x48]
0028652D  83 E3 EF                        and ebx, 0xffffffef
00286530  E8 5B 21 FC FF                  call 0x140248690
00286535  0F B6 F0                        movzx esi, al
00286538  8B 45 38                        mov eax, dword ptr [rbp + 0x38]
0028653B  83 E0 FB                        and eax, 0xfffffffb
0028653E  48 83 6D 28 01                  sub qword ptr [rbp + 0x28], 1
00286543  89 45 38                        mov dword ptr [rbp + 0x38], eax
00286546  75 64                           jne 0x1402865ac
00286548  48 39 7D 18                     cmp qword ptr [rbp + 0x18], rdi
0028654C  75 5E                           jne 0x1402865ac
0028654E  48 39 7D 20                     cmp qword ptr [rbp + 0x20], rdi
00286552  0F 85 A2 FD FF FF               jne 0x1402862fa
00286558  83 C8 01                        or eax, 1
0028655B  4C 8D 44 24 20                  lea r8, [rsp + 0x20]
00286560  BB 02 00 00 00                  mov ebx, 2
00286565  89 45 38                        mov dword ptr [rbp + 0x38], eax
00286568  48 8B CD                        mov rcx, rbp
0028656B  8D 53 FF                        lea edx, [rbx - 1]
0028656E  E8 F9 47 1F 00                  call 0x14047ad6c
00286573  48 8B CD                        mov rcx, rbp
00286576  E8 C9 CA 1D 00                  call 0x140463044
0028657B  E9 A1 FD FF FF                  jmp 0x140286321
00286580  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00286585  E8 76 25 70 00                  call 0x140988b00
0028658A  0F 57 C0                        xorps xmm0, xmm0
0028658D  48 C7 44 24 20 FF FF FF FF      mov qword ptr [rsp + 0x20], 0xffffffffffffffff
00286596  83 CB 04                        or ebx, 4
00286599  48 8B CD                        mov rcx, rbp
0028659C  F3 0F 7F 44 24 28               movdqu xmmword ptr [rsp + 0x28], xmm0
002865A2  E8 4D 5A 85 00                  call 0x140adbff4
002865A7  E9 23 FD FF FF                  jmp 0x1402862cf
002865AC  83 CB 08                        or ebx, 8
002865AF  E9 46 FD FF FF                  jmp 0x1402862fa
002865B4  83 E3 F6                        and ebx, 0xfffffff6
002865B7  83 CB 04                        or ebx, 4
002865BA  E9 62 FD FF FF                  jmp 0x140286321
002865BF  0F BA E1 1B                     bt ecx, 0x1b
002865C3  0F 43 DA                        cmovae ebx, edx
002865C6  E9 C5 FC FF FF                  jmp 0x140286290
002865CB  45 33 C0                        xor r8d, r8d
002865CE  48 8B D7                        mov rdx, rdi
002865D1  49 8B CF                        mov rcx, r15
002865D4  E8 37 1E FC FF                  call 0x140248410
002865D9  E9 CC FD FF FF                  jmp 0x1402863aa
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiCheckControlArea(__int64 a1, unsigned __int8 a2)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p78;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (64);
    v_r13 = 0;
    v_r14 = 0;
    v_rdi = 0;
    v_rbx = 0;
    v_stack_m58 = -1;
    v_r13 = (*(unsigned __int64 *)(a1 + 64) != 0) ? 1 : 0;
    a3 = (unsigned int)((*(unsigned __int16 *)(a1 + 60)) & (0x3FFULL));
    v_stack_m50 = v_xmm0;
    if ((*(unsigned __int64 *)(a1 + 40)) == 0) goto loc_00286247;
loc_0028620E:
    a1 = (a1) + (80);
    if ((*(unsigned __int64 *)(a1)) == 0) goto loc_00286325;
loc_00286223:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 8)))) & (3)) == 0) goto loc_002864A3;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1)) = 0;
    *(unsigned __int64 *)(a1) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1));
loc_0028623A:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1)) != 0) goto loc_00286223;
    goto loc_00286336;
loc_00286247:
    if ((*(unsigned __int64 *)(a1 + 24)) != 4) goto loc_0028620E;
    if (((*(unsigned __int64 *)(a1 + 64)) & (-16)) == 0) goto loc_0028642A;
    if ((*(unsigned __int64 *)(a1 + 32)) == 4) goto loc_0028644C;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 56)))) & (32)) == 0) goto loc_00286309;
    result = MiImageUnused(a1, 1, v_stack_m58, a4);
    if (condition_is_below) goto loc_002865BF;
loc_00286290:
    if (((*(unsigned __int8 *)(a1 + 96)) & (1)) == 0) goto loc_0028629E;
    goto loc_002862A2;
loc_0028629E:
    result = a1 + 72;
    if (16 == 16) {
        a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 56))) | (4));
        *(unsigned __int64 *)(a1 + 40) = 1;
        *(unsigned int *)(a1 + 56) = (unsigned int)(a1);
        a2 = a2;
        a1 = a1 + 72;
        result = MiReleaseSpinLockExclusive(a1, a2, v_stack_m58, a4);
    }
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 56))) & (0x8020000ULL));
    if (((unsigned int)(result)) == 0x20000ULL) goto loc_00286580;
loc_002862CF:
    if (((*(unsigned __int8 *)(a1 + 96)) & (1)) != 0) {
        a2 = 0;
        a4 = 0xFFFFFFFFULL;
        a1 = a1;
        a3 = a2 + 32;
        result = MiWalkEntireImage(a1, a2, a3, a4);
        a1 = a1;
        result = MiDeleteDebuggerPatches(a1, a2, a3, a4);
    }
    if (16 >= 16) goto loc_00286529;
loc_002862FA:
    if (((16) & (8)) != 0) goto loc_002865B4;
    if (((16) & (2)) != 0) goto loc_00286321;
loc_00286309:
    if (((*(unsigned int *)(a1 + 56)) & (0x40000ULL)) != 0) goto loc_00286521;
    result = MiInsertUnusedSegment(a1, a2, a3, a4);
loc_00286321:
loc_00286325:
    if (((16) & (4)) == 0) goto loc_00286339;
    if (*(unsigned __int64 *)(a1 + 80) != 0) goto loc_00286223;
loc_00286336:
    v_rbx = (unsigned int)((16) & (0xFFFFFFFBULL));
loc_00286339:
    if ((unsigned int)(v_rbx) != 0) goto loc_00286401;
    if (0 == 17) goto loc_002863E8;
    if (((*(unsigned __int8 *)(v_rip + 13895604)) & (1)) != 0) goto loc_00286461;
loc_00286358:
    *(unsigned int *)(a1 + 72) = 0;
loc_0028635F:
    if ((*(unsigned int *)(v_rip + 13896122)) != 0) {
        a1 = v_cr8;
        a2 = 0;
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a3, a4);
    }
loc_0028637D:
    result = MiReleaseControlAreaWaiters(*(unsigned __int64 *)(a1), a2, a3, a4);
    if ((*(unsigned __int64 *)(v_rip + 12285108)) >= (*(unsigned __int64 *)(v_rip + 12282701))) goto loc_002864AB;
loc_0028639C:
    if (result == 0) goto loc_002863C5;
    if (*(unsigned __int64 *)(a1 + 64) != 0) goto loc_002865CB;
loc_002863AA:
    result = MiReturnResident(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12230318) + a3 * 8), result, a3, a4);
    a2 = 0;
    result = MiReturnCrossPartitionCharges(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12230318) + a3 * 8), a2, (unsigned int)((unsigned int)(v_r13)), result);
loc_002863C5:
    result = MiReturnImageBase(v_stack_m58, a2, (unsigned int)((unsigned int)(v_r13)), result);
    v_rsp = (v_rsp) + (64);
    return result;
loc_002863E8:
    if (((*(unsigned __int8 *)(v_rip + 13895447)) & (1)) != 0) goto loc_00286482;
loc_002863F5:
    *(unsigned int *)(a1 + 72) = 0;
    goto loc_0028637D;
loc_00286401:
    if ((((unsigned __int8)(v_stack_p18)) & (1)) != 0) goto loc_00286505;
    if (0 == 17) goto loc_0028643A;
    result = ExReleaseSpinLockExclusive(a1 + 72, 0, (unsigned int)((unsigned int)(v_r13)), result);
    result = MiSegmentDelete(a1, 0, (unsigned int)((unsigned int)(v_r13)), result);
    goto loc_0028639C;
loc_0028642A:
    result = (unsigned int)((result) | (1));
    *(unsigned int *)(a1 + 56) = (unsigned int)(result);
    goto loc_00286321;
loc_0028643A:
    result = ExReleaseSpinLockExclusiveFromDpcLevel(a1, 0, (unsigned int)((unsigned int)(v_r13)), result);
    result = MiSegmentDelete(a1, 0, (unsigned int)((unsigned int)(v_r13)), result);
    goto loc_0028639C;
loc_0028644C:
    result = (unsigned int)((result) | (1));
    *(unsigned int *)(a1 + 56) = (unsigned int)(result);
    result = MiClearFilePointer(a1, 0, (unsigned int)((unsigned int)(v_r13)), result);
    goto loc_00286321;
loc_00286461:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13138417))) != 0) goto loc_00286358;
    result = ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented(a1 + 72, v_stack_p78, (unsigned int)((unsigned int)(v_r13)), result);
    goto loc_0028635F;
loc_00286482:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13138384))) != 0) goto loc_002863F5;
    result = ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented(a1 + 72, v_stack_p78, (unsigned int)((unsigned int)(v_r13)), result);
    goto loc_0028637D;
loc_002864A3:
    goto loc_0028623A;
loc_002864AB:
    result = MiShouldTrimUnusedSegments(v_rip + 12265550, v_stack_p78, (unsigned int)((unsigned int)(v_r13)), result);
    if ((unsigned int)(result) == 0) goto loc_0028639C;
    a1 = 0;
    result = PsGetNextPartition(a1, v_stack_p78, (unsigned int)((unsigned int)(v_r13)), result);
    if (result == 0) goto loc_0028639C;
loc_002864D2:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result) + 2104)) != 0) {
        a1 = (*(unsigned __int64 *)(result)) + (0x6F8ULL);
        a3 = 0;
        a2 = 0;
        result = KeSetEvent(a1, a2, a3, result);
    }
    result = PsGetNextPartition(result, a2, a3, result);
    if (result != 0) goto loc_002864D2;
    goto loc_0028639C;
loc_00286505:
    a3 = 0;
    *(unsigned __int64 *)(a1 + 40) = 1;
    result = MiCleanSection(a1, 0, a3, result);
    goto loc_0028639C;
loc_00286521:
    v_rbx = (unsigned int)((result) | (1));
    goto loc_00286321;
loc_00286529:
    v_rbx = (unsigned int)((v_rbx) & (0xFFFFFFEFULL));
    result = ExAcquireSpinLockExclusive(a1 + 72, 0, a3, result);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 56))) & (0xFFFFFFFBULL));
    *(unsigned int *)(a1 + 56) = (unsigned int)(result);
    if (condition_is_not_equal) goto loc_002865AC;
    if ((*(unsigned __int64 *)(a1 + 24)) != result) goto loc_002865AC;
    if ((*(unsigned __int64 *)(a1 + 32)) != result) goto loc_002862FA;
    result = (unsigned int)((result) | (1));
    *(unsigned int *)(a1 + 56) = (unsigned int)(result);
    result = MiImageUnused(a1, 2 - 1, v_stack_p20, result);
    result = MiClearFilePointer(a1, 2 - 1, v_stack_p20, result);
    goto loc_00286321;
loc_00286580:
    result = MiReturnImageBase(v_stack_p20, 2 - 1, v_stack_p20, result);
    v_stack_p20 = -1;
    v_rbx = (unsigned int)((2) | (4));
    v_stack_p28 = v_xmm0;
    result = MiPurgeImageSection(a1, 2 - 1, v_stack_p20, result);
    goto loc_002862CF;
loc_002865AC:
    v_rbx = (unsigned int)((v_rbx) | (8));
    goto loc_002862FA;
loc_002865B4:
    v_rbx = (unsigned int)((v_rbx) & (0xFFFFFFF6ULL));
    v_rbx = (unsigned int)((v_rbx) | (4));
    goto loc_00286321;
loc_002865BF:
    if (condition_is_above_or_equal) { v_rbx = (unsigned int)(2 - 1); }
    goto loc_00286290;
loc_002865CB:
    a3 = 0;
    result = MiReturnCommit(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12230318) + a3 * 8), result, a3, result);
    goto loc_002863AA;
}
```

## 5. (Beta) C Style

```c
int64_t MiCheckControlArea(void *Arg1, uint8_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p78;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (64);
    local_r13 = 0;
    local_r14 = 0;
    local_rdi = 0;
    local_rbx = 0;
    v_stack_m58 = -1;
    local_r13 = (*(uint64_t *)(arg1 + 0x40) != 0) ? 1 : 0;
    a3 = (uint32_t)((*(uint16_t *)(arg1 + 0x3C)) & (0x3FFULL));
    v_stack_m50 = v_xmm0;
    if ((*(uint64_t *)(arg1 + 0x28)) == 0) goto loc_00286247;
loc_0028620E:
    Arg1 = (Arg1) + (80);
    if ((*(uint64_t *)(arg1)) == 0) goto loc_00286325;
loc_00286223:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x8)))) & (3)) == 0) goto loc_002864A3;
    *(uint64_t *)(*(uint64_t *)(arg1)) = 0;
    *(uint64_t *)(arg1) = *(uint64_t *)(*(uint64_t *)(arg1));
loc_0028623A:
    if (*(uint64_t *)(*(uint64_t *)(arg1)) != 0) goto loc_00286223;
    goto loc_00286336;
loc_00286247:
    if ((*(uint64_t *)(arg1 + 0x18)) != 4) goto loc_0028620E;
    if (((*(uint64_t *)(arg1 + 0x40)) & (-16)) == 0) goto loc_0028642A;
    if ((*(uint64_t *)(arg1 + 0x20)) == 4) goto loc_0028644C;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x38)))) & (32)) == 0) goto loc_00286309;
    result = MiImageUnused(Arg1, 1, v_stack_m58, a4);
    if (condition_is_below) goto loc_002865BF;
loc_00286290:
    if (((*(uint8_t *)(arg1 + 0x60)) & (1)) == 0) goto loc_0028629E;
    goto loc_002862A2;
loc_0028629E:
    result = Arg1 + 72;
    if (16 == 16) {
        Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x38))) | (4));
        *(uint64_t *)(arg1 + 0x28) = 1;
        *(uint32_t *)(arg1 + 0x38) = (uint32_t)(Arg1);
        Arg2 = Arg2;
        Arg1 = Arg1 + 72;
        result = MiReleaseSpinLockExclusive(Arg1, Arg2, v_stack_m58, a4);
    }
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x38))) & (0x8020000ULL));
    if (((uint32_t)(result)) == 0x20000ULL) goto loc_00286580;
loc_002862CF:
    if (((*(uint8_t *)(arg1 + 0x60)) & (1)) != 0) {
        Arg2 = 0;
        a4 = 0xFFFFFFFFULL;
        Arg1 = Arg1;
        a3 = Arg2 + 32;
        result = MiWalkEntireImage(Arg1, Arg2, a3, a4);
        Arg1 = Arg1;
        result = MiDeleteDebuggerPatches(Arg1, Arg2, a3, a4);
    }
    if (16 >= 16) goto loc_00286529;
loc_002862FA:
    if (((16) & (8)) != 0) goto loc_002865B4;
    if (((16) & (2)) != 0) goto loc_00286321;
loc_00286309:
    if (((*(uint32_t *)(arg1 + 0x38)) & (0x40000ULL)) != 0) goto loc_00286521;
    result = MiInsertUnusedSegment(Arg1, Arg2, a3, a4);
loc_00286321:
loc_00286325:
    if (((16) & (4)) == 0) goto loc_00286339;
    if (*(uint64_t *)(arg1 + 0x50) != 0) goto loc_00286223;
loc_00286336:
    local_rbx = (uint32_t)((16) & (0xFFFFFFFBULL));
loc_00286339:
    if ((uint32_t)(local_rbx) != 0) goto loc_00286401;
    if (0 == 17) goto loc_002863E8;
    if (((*(uint8_t *)(v_rip + 0xD407B4)) & (1)) != 0) goto loc_00286461;
loc_00286358:
    *(uint32_t *)(arg1 + 0x48) = 0;
loc_0028635F:
    if ((*(uint32_t *)(v_rip + 0xD409BA)) != 0) {
        Arg1 = v_cr8;
        Arg2 = 0;
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, a3, a4);
    }
loc_0028637D:
    result = MiReleaseControlAreaWaiters(*(uint64_t *)(arg1), Arg2, a3, a4);
    if ((*(uint64_t *)(v_rip + 0xBB74B4)) >= (*(uint64_t *)(v_rip + 0xBB6B4D))) goto loc_002864AB;
loc_0028639C:
    if (result == 0) goto loc_002863C5;
    if (*(uint64_t *)(arg1 + 0x40) != 0) goto loc_002865CB;
loc_002863AA:
    result = MiReturnResident(*(uint64_t *)(*(uint64_t *)(v_rip + 0xBA9EAE) + a3 * 8), result, a3, a4);
    Arg2 = 0;
    result = MiReturnCrossPartitionCharges(*(uint64_t *)(*(uint64_t *)(v_rip + 0xBA9EAE) + a3 * 8), Arg2, (uint32_t)((uint32_t)(local_r13)), result);
loc_002863C5:
    result = MiReturnImageBase(v_stack_m58, Arg2, (uint32_t)((uint32_t)(local_r13)), result);
    local_rsp = (local_rsp) + (64);
    return result;
loc_002863E8:
    if (((*(uint8_t *)(v_rip + 0xD40717)) & (1)) != 0) goto loc_00286482;
loc_002863F5:
    *(uint32_t *)(arg1 + 0x48) = 0;
    goto loc_0028637D;
loc_00286401:
    if ((((uint8_t)(v_stack_p18)) & (1)) != 0) goto loc_00286505;
    if (0 == 17) goto loc_0028643A;
    result = ExReleaseSpinLockExclusive(Arg1 + 72, 0, (uint32_t)((uint32_t)(local_r13)), result);
    result = MiSegmentDelete(Arg1, 0, (uint32_t)((uint32_t)(local_r13)), result);
    goto loc_0028639C;
loc_0028642A:
    result = (uint32_t)((result) | (1));
    *(uint32_t *)(arg1 + 0x38) = (uint32_t)(result);
    goto loc_00286321;
loc_0028643A:
    result = ExReleaseSpinLockExclusiveFromDpcLevel(Arg1, 0, (uint32_t)((uint32_t)(local_r13)), result);
    result = MiSegmentDelete(Arg1, 0, (uint32_t)((uint32_t)(local_r13)), result);
    goto loc_0028639C;
loc_0028644C:
    result = (uint32_t)((result) | (1));
    *(uint32_t *)(arg1 + 0x38) = (uint32_t)(result);
    result = MiClearFilePointer(Arg1, 0, (uint32_t)((uint32_t)(local_r13)), result);
    goto loc_00286321;
loc_00286461:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC879F1))) != 0) goto loc_00286358;
    result = ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented(Arg1 + 72, v_stack_p78, (uint32_t)((uint32_t)(local_r13)), result);
    goto loc_0028635F;
loc_00286482:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC879D0))) != 0) goto loc_002863F5;
    result = ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented(Arg1 + 72, v_stack_p78, (uint32_t)((uint32_t)(local_r13)), result);
    goto loc_0028637D;
loc_002864A3:
    goto loc_0028623A;
loc_002864AB:
    result = MiShouldTrimUnusedSegments(v_rip + 12265550, v_stack_p78, (uint32_t)((uint32_t)(local_r13)), result);
    if ((uint32_t)(result) == 0) goto loc_0028639C;
    Arg1 = 0;
    result = PsGetNextPartition(Arg1, v_stack_p78, (uint32_t)((uint32_t)(local_r13)), result);
    if (result == 0) goto loc_0028639C;
loc_002864D2:
    if ((*(uint64_t *)(*(uint64_t *)(result) + 0x838)) != 0) {
        Arg1 = (*(uint64_t *)(result)) + (0x6F8ULL);
        a3 = 0;
        Arg2 = 0;
        result = KeSetEvent(Arg1, Arg2, a3, result);
    }
    result = PsGetNextPartition(result, Arg2, a3, result);
    if (result != 0) goto loc_002864D2;
    goto loc_0028639C;
loc_00286505:
    a3 = 0;
    *(uint64_t *)(arg1 + 0x28) = 1;
    result = MiCleanSection(Arg1, 0, a3, result);
    goto loc_0028639C;
loc_00286521:
    local_rbx = (uint32_t)((result) | (1));
    goto loc_00286321;
loc_00286529:
    local_rbx = (uint32_t)((local_rbx) & (0xFFFFFFEFULL));
    result = ExAcquireSpinLockExclusive(Arg1 + 72, 0, a3, result);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x38))) & (0xFFFFFFFBULL));
    *(uint32_t *)(arg1 + 0x38) = (uint32_t)(result);
    if (condition_is_not_equal) goto loc_002865AC;
    if ((*(uint64_t *)(arg1 + 0x18)) != result) goto loc_002865AC;
    if ((*(uint64_t *)(arg1 + 0x20)) != result) goto loc_002862FA;
    result = (uint32_t)((result) | (1));
    *(uint32_t *)(arg1 + 0x38) = (uint32_t)(result);
    result = MiImageUnused(Arg1, 2 - 1, v_stack_p20, result);
    result = MiClearFilePointer(Arg1, 2 - 1, v_stack_p20, result);
    goto loc_00286321;
loc_00286580:
    result = MiReturnImageBase(v_stack_p20, 2 - 1, v_stack_p20, result);
    v_stack_p20 = -1;
    local_rbx = (uint32_t)((2) | (4));
    v_stack_p28 = v_xmm0;
    result = MiPurgeImageSection(Arg1, 2 - 1, v_stack_p20, result);
    goto loc_002862CF;
loc_002865AC:
    local_rbx = (uint32_t)((local_rbx) | (8));
    goto loc_002862FA;
loc_002865B4:
    local_rbx = (uint32_t)((local_rbx) & (0xFFFFFFF6ULL));
    local_rbx = (uint32_t)((local_rbx) | (4));
    goto loc_00286321;
loc_002865BF:
    if (condition_is_above_or_equal) { local_rbx = (uint32_t)(2 - 1); }
    goto loc_00286290;
loc_002865CB:
    a3 = 0;
    result = MiReturnCommit(*(uint64_t *)(*(uint64_t *)(v_rip + 0xBA9EAE) + a3 * 8), result, a3, result);
    goto loc_002863AA;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg1` | `+ 0x28` | `64` | `R/W` |
| `Arg1` | `+ 0x28` | `64` | `W` |
| `Arg1` | `+ 0x38` | `32` | `R` |
| `Arg1` | `+ 0x38` | `32` | `W` |
| `Arg1` | `+ 0x3C` | `16` | `R` |
| `Arg1` | `+ 0x40` | `64` | `R` |
| `Arg1` | `+ 0x48` | `32` | `W` |
| `Arg1` | `+ 0x48` | `64` | `R` |
| `Arg1` | `+ 0x50` | `64` | `R` |
| `Arg1` | `+ 0x60` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002861B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
