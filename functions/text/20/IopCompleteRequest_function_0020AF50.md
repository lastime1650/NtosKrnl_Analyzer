# IopCompleteRequest

- RVA: `0x0020AF50`–`0x0020B57A` (길이 `1,578` bytes)
- VA: `0x000000014020AF50`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0005D7D8`
- 디코드: `370`개 명령, `1,578/1,578` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **24**; 고유 호출 대상: **14**
- 직접 호출자로 확인된 함수: **9**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0020AFE4` → [IopProcessBufferedIoCompletion](../3E/IopProcessBufferedIoCompletion_function_003ED220.md) (function, `0x003ED220`)
- `0x0020B059` → [ObfReferenceObjectWithTag](../21/ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x0020B102` → [ObDereferenceObjectDeferDeleteWithTag](../26/ObDereferenceObjectDeferDeleteWithTag_function_00263EA0.md) (function, `0x00263EA0`)
- `0x0020B123` → [IopDequeueIrpFromThread](IopDequeueIrpFromThread_function_00207B20.md) (function, `0x00207B20`)
- `0x0020B12B` → [IoFreeIrp](../24/IoFreeIrp_function_0024DF70.md) (function, `0x0024DF70`)
- `0x0020B14C` → [IopUpdateIrpTransferCount](../3E/IopUpdateIrpTransferCount_function_003ED420.md) (function, `0x003ED420`)
- `0x0020B16D` → [IopDequeueIrpFromThread](IopDequeueIrpFromThread_function_00207B20.md) (function, `0x00207B20`)
- `0x0020B1A1` → [IoFreeIrp](../24/IoFreeIrp_function_0024DF70.md) (function, `0x0024DF70`)
- `0x0020B1CA` → [ObDereferenceObjectDeferDeleteWithTag](../26/ObDereferenceObjectDeferDeleteWithTag_function_00263EA0.md) (function, `0x00263EA0`)
- `0x0020B1EE` → [ObfDereferenceObjectWithTag](../2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x0020B20A` → [KeSetEvent](../33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x0020B2A1` → [KeInsertQueueApc](KeInsertQueueApc_function_00203F10.md) (function, `0x00203F10`)
- `0x0020B304` → [KeInsertQueueEx](../39/KeInsertQueueEx_function_00397910.md) (function, `0x00397910`)
- `0x0020B311` → [IopDequeueIrpFromFileObject](../3E/IopDequeueIrpFromFileObject_function_003ED548.md) (function, `0x003ED548`)
- `0x0020B325` → [KeSetEvent](../33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x0020B343` → [ObfDereferenceObjectWithTag](../2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x0020B36C` → [IopDequeueIrpFromFileObject](../3E/IopDequeueIrpFromFileObject_function_003ED548.md) (function, `0x003ED548`)
- `0x0020B3EB` → [IoFreeIrp](../24/IoFreeIrp_function_0024DF70.md) (function, `0x0024DF70`)
- `0x0020B3FD` → [IopDecrementCompletionContextUsageCount](../45/IopDecrementCompletionContextUsageCount_function_00452678.md) (function, `0x00452678`)
- `0x0020B437` → [ObfDereferenceObjectWithTag](../2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x0020B47C` → [IopIncrementCompletionContextUsageCountAndReadData](../44/IopIncrementCompletionContextUsageCountAndReadData_function_00443C60.md) (function, `0x00443C60`)
- `0x0020B4C4` → [IoFreeIrp](../24/IoFreeIrp_function_0024DF70.md) (function, `0x0024DF70`)
- `0x0020B4F2` → [KeSetEvent](../33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x0020B526` → [IoFreeMdl](../29/IoFreeMdl_function_0029EA80.md) (function, `0x0029EA80`)

### Direct callers
- [IoRemoveIoCompletion](IoRemoveIoCompletion_function_0020B580.md) at `0x0020B73D`
- [IopCompleteIrpInFileObjectList](../24/IopCompleteIrpInFileObjectList_function_0024F330.md) at `0x0024F9CE`
- [sub_00251225](../25/Unknown_function_00251225.md) at `0x00251446`
- [IopfCompleteRequest](../29/IopfCompleteRequest_function_0029B5F8.md) at `0x0029BC02`
- [NtSetInformationFile](../29/NtSetInformationFile_function_0029C5E0.md) at `0x0029CDD8`
- [sub_006D6658](../6D/Unknown_function_006D6658.md) at `0x006D669C`
- [IopAbortRequest](../../page/71/IopAbortRequest_function_0071AC40.md) at `0x0071AC59`
- [NtQueryInformationFile](../../page/8A/NtQueryInformationFile_function_008AD630.md) at `0x008ADEF7`
- [IopSynchronousServiceTail](../../page/8E/IopSynchronousServiceTail_function_008EB440.md) at `0x008EB7DC`

### Static image references
- `0x0020B265` → RVA `0x00A34070` (`IopUserCompletion`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **4**
  - `0x0020B542` → [sub_006D663E + 0x6](../6D/Unknown_function_006D663E.md) (`tail-transfer`)
  - `0x0020B552` → [sub_006D663E](../6D/Unknown_function_006D663E.md) (`tail-transfer`)
  - `0x0020B55B` → [sub_006D663E](../6D/Unknown_function_006D663E.md) (`tail-transfer`)
  - `0x0020B561` → [sub_006D663E + 0x6](../6D/Unknown_function_006D663E.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0020AF50  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
0020AF55  53                              push rbx
0020AF56  56                              push rsi
0020AF57  57                              push rdi
0020AF58  41 54                           push r12
0020AF5A  41 55                           push r13
0020AF5C  41 56                           push r14
0020AF5E  41 57                           push r15
0020AF60  48 81 EC 90 00 00 00            sub rsp, 0x90
0020AF67  4C 8B E9                        mov r13, rcx
0020AF6A  48 89 4C 24 78                  mov qword ptr [rsp + 0x78], rcx
0020AF6F  45 33 E4                        xor r12d, r12d
0020AF72  4C 89 64 24 28                  mov qword ptr [rsp + 0x28], r12
0020AF77  4C 89 64 24 48                  mov qword ptr [rsp + 0x48], r12
0020AF7C  44 88 A4 24 E8 00 00 00         mov byte ptr [rsp + 0xe8], r12b
0020AF84  48 8D 59 88                     lea rbx, [rcx - 0x78]
0020AF88  48 89 5C 24 58                  mov qword ptr [rsp + 0x58], rbx
0020AF8D  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0020AF96  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
0020AF9B  49 8B 31                        mov rsi, qword ptr [r9]
0020AF9E  48 89 74 24 60                  mov qword ptr [rsp + 0x60], rsi
0020AFA3  4D 85 C0                        test r8, r8
0020AFA6  0F 85 F3 03 00 00               jne 0x14020b39f
0020AFAC  44 88 A4 24 E0 00 00 00         mov byte ptr [rsp + 0xe0], r12b
0020AFB4  4C 8D 7B 10                     lea r15, [rbx + 0x10]
0020AFB8  4C 89 7C 24 70                  mov qword ptr [rsp + 0x70], r15
0020AFBD  41 8B 07                        mov eax, dword ptr [r15]
0020AFC0  0F BA E0 15                     bt eax, 0x15
0020AFC4  0F 82 6E 05 00 00               jb 0x14020b538
0020AFCA  84 C0                           test al, al
0020AFCC  0F 88 FC 04 00 00               js 0x14020b4ce
0020AFD2  0F BA E0 0D                     bt eax, 0xd
0020AFD6  0F 82 F8 01 00 00               jb 0x14020b1d4
0020AFDC  4C 89 64 24 38                  mov qword ptr [rsp + 0x38], r12
0020AFE1  48 8B CB                        mov rcx, rbx
0020AFE4  E8 37 22 1E 00                  call 0x1403ed220
0020AFE9  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
0020AFED  48 85 C9                        test rcx, rcx
0020AFF0  0F 85 2D 05 00 00               jne 0x14020b523
0020AFF6  4C 89 63 08                     mov qword ptr [rbx + 8], r12
0020AFFA  48 8D 7B 30                     lea rdi, [rbx + 0x30]
0020AFFE  48 89 7C 24 68                  mov qword ptr [rsp + 0x68], rdi
0020B003  8B 07                           mov eax, dword ptr [rdi]
0020B005  25 00 00 00 C0                  and eax, 0xc0000000
0020B00A  3D 00 00 00 C0                  cmp eax, 0xc0000000
0020B00F  0F 84 61 03 00 00               je 0x14020b376
0020B015  48 85 F6                        test rsi, rsi
0020B018  0F 84 77 03 00 00               je 0x14020b395
0020B01E  48 8B 8E B0 00 00 00            mov rcx, qword ptr [rsi + 0xb0]
0020B025  48 85 C9                        test rcx, rcx
0020B028  0F 84 67 03 00 00               je 0x14020b395
0020B02E  41 F7 07 00 20 00 00            test dword ptr [r15], 0x2000
0020B035  0F 84 2C 04 00 00               je 0x14020b467
0020B03B  4C 8B 31                        mov r14, qword ptr [rcx]
0020B03E  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
0020B043  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
0020B047  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0020B04C  4D 85 F6                        test r14, r14
0020B04F  74 0D                           je 0x14020b05e
0020B051  BA 44 66 6C 74                  mov edx, 0x746c6644
0020B056  49 8B CE                        mov rcx, r14
0020B059  E8 B2 56 00 00                  call 0x140210710
0020B05E  8B 07                           mov eax, dword ptr [rdi]
0020B060  25 00 00 00 C0                  and eax, 0xc0000000
0020B065  3D 00 00 00 C0                  cmp eax, 0xc0000000
0020B06A  0F 84 97 03 00 00               je 0x14020b407
0020B070  44 89 64 24 20                  mov dword ptr [rsp + 0x20], r12d
0020B075  48 8B 4B 48                     mov rcx, qword ptr [rbx + 0x48]
0020B079  F6 43 47 10                     test byte ptr [rbx + 0x47], 0x10
0020B07D  75 0A                           jne 0x14020b089
0020B07F  48 8B 43 38                     mov rax, qword ptr [rbx + 0x38]
0020B083  48 89 41 08                     mov qword ptr [rcx + 8], rax
0020B087  EB 06                           jmp 0x14020b08f
0020B089  8B 43 38                        mov eax, dword ptr [rbx + 0x38]
0020B08C  89 41 04                        mov dword ptr [rcx + 4], eax
0020B08F  90                              nop
0020B090  8B 07                           mov eax, dword ptr [rdi]
0020B092  89 01                           mov dword ptr [rcx], eax
0020B094  EB 24                           jmp 0x14020b0ba
0020B096  45 33 E4                        xor r12d, r12d
0020B099  4C 8B AC 24 D0 00 00 00         mov r13, qword ptr [rsp + 0xd0]
0020B0A1  48 8B 5C 24 58                  mov rbx, qword ptr [rsp + 0x58]
0020B0A6  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
0020B0AB  4C 8B 74 24 28                  mov r14, qword ptr [rsp + 0x28]
0020B0B0  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
0020B0B5  4C 8B 7C 24 70                  mov r15, qword ptr [rsp + 0x70]
0020B0BA  48 8B 4B 50                     mov rcx, qword ptr [rbx + 0x50]
0020B0BE  48 85 C9                        test rcx, rcx
0020B0C1  0F 85 59 02 00 00               jne 0x14020b320
0020B0C7  48 85 F6                        test rsi, rsi
0020B0CA  0F 85 25 01 00 00               jne 0x14020b1f5
0020B0D0  8B 07                           mov eax, dword ptr [rdi]
0020B0D2  25 00 00 00 C0                  and eax, 0xc0000000
0020B0D7  3D 00 00 00 C0                  cmp eax, 0xc0000000
0020B0DC  75 66                           jne 0x14020b144
0020B0DE  80 7B 41 00                     cmp byte ptr [rbx + 0x41], 0
0020B0E2  0F 85 59 03 00 00               jne 0x14020b441
0020B0E8  41 F7 07 00 20 00 00            test dword ptr [r15], 0x2000
0020B0EF  0F 85 71 02 00 00               jne 0x14020b366
0020B0F5  48 85 F6                        test rsi, rsi
0020B0F8  74 0D                           je 0x14020b107
0020B0FA  BA 44 66 6C 74                  mov edx, 0x746c6644
0020B0FF  48 8B CE                        mov rcx, rsi
0020B102  E8 99 8D 05 00                  call 0x140263ea0
0020B107  41 F7 07 00 80 00 00            test dword ptr [r15], 0x8000
0020B10E  0F 85 77 03 00 00               jne 0x14020b48b
0020B114  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
0020B119  48 89 BB 98 00 00 00            mov qword ptr [rbx + 0x98], rdi
0020B120  48 8B CB                        mov rcx, rbx
0020B123  E8 F8 C9 FF FF                  call 0x140207b20
0020B128  48 8B CB                        mov rcx, rbx
0020B12B  E8 40 2E 04 00                  call 0x14024df70
0020B130  48 81 C4 90 00 00 00            add rsp, 0x90
0020B137  41 5F                           pop r15
0020B139  41 5E                           pop r14
0020B13B  41 5D                           pop r13
0020B13D  41 5C                           pop r12
0020B13F  5F                              pop rdi
0020B140  5E                              pop rsi
0020B141  5B                              pop rbx
0020B142  C3                              ret
0020B143  CC                              int3
0020B144  48 8B 54 24 38                  mov rdx, qword ptr [rsp + 0x38]
0020B149  48 8B CB                        mov rcx, rbx
0020B14C  E8 CF 22 1E 00                  call 0x1403ed420
0020B151  48 8B CB                        mov rcx, rbx
0020B154  41 F7 07 00 20 00 00            test dword ptr [r15], 0x2000
0020B15B  0F 85 AD 01 00 00               jne 0x14020b30e
0020B161  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
0020B166  48 89 BB 98 00 00 00            mov qword ptr [rbx + 0x98], rdi
0020B16D  E8 AE C9 FF FF                  call 0x140207b20
0020B172  41 8B 0F                        mov ecx, dword ptr [r15]
0020B175  8B C1                           mov eax, ecx
0020B177  25 00 80 00 00                  and eax, 0x8000
0020B17C  75 05                           jne 0x14020b183
0020B17E  48 83 63 58 FE                  and qword ptr [rbx + 0x58], 0xfffffffffffffffe
0020B183  85 C0                           test eax, eax
0020B185  0F 84 8E 00 00 00               je 0x14020b219
0020B18B  4D 85 F6                        test r14, r14
0020B18E  0F 85 17 01 00 00               jne 0x14020b2ab
0020B194  0F BA E1 0F                     bt ecx, 0xf
0020B198  0F 82 18 02 00 00               jb 0x14020b3b6
0020B19E  48 8B CB                        mov rcx, rbx
0020B1A1  E8 CA 2D 04 00                  call 0x14024df70
0020B1A6  4D 85 F6                        test r14, r14
0020B1A9  75 3B                           jne 0x14020b1e6
0020B1AB  80 BC 24 E8 00 00 00 00         cmp byte ptr [rsp + 0xe8], 0
0020B1B3  0F 85 41 02 00 00               jne 0x14020b3fa
0020B1B9  48 85 F6                        test rsi, rsi
0020B1BC  0F 84 6E FF FF FF               je 0x14020b130
0020B1C2  BA 44 66 6C 74                  mov edx, 0x746c6644
0020B1C7  48 8B CE                        mov rcx, rsi
0020B1CA  E8 D1 8C 05 00                  call 0x140263ea0
0020B1CF  E9 5C FF FF FF                  jmp 0x14020b130
0020B1D4  48 8B 7B 58                     mov rdi, qword ptr [rbx + 0x58]
0020B1D8  48 83 E7 F9                     and rdi, 0xfffffffffffffff9
0020B1DC  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
0020B1E1  E9 FB FD FF FF                  jmp 0x14020afe1
0020B1E6  BA 44 66 6C 74                  mov edx, 0x746c6644
0020B1EB  49 8B CE                        mov rcx, r14
0020B1EE  E8 ED C6 0E 00                  call 0x1402f78e0
0020B1F3  EB B6                           jmp 0x14020b1ab
0020B1F5  F7 46 50 00 00 00 04            test dword ptr [rsi + 0x50], 0x4000000
0020B1FC  75 11                           jne 0x14020b20f
0020B1FE  45 33 C0                        xor r8d, r8d
0020B201  33 D2                           xor edx, edx
0020B203  48 8D 8E 98 00 00 00            lea rcx, [rsi + 0x98]
0020B20A  E8 01 41 13 00                  call 0x14033f310
0020B20F  8B 07                           mov eax, dword ptr [rdi]
0020B211  89 46 38                        mov dword ptr [rsi + 0x38], eax
0020B214  E9 B7 FE FF FF                  jmp 0x14020b0d0
0020B219  48 8B 43 58                     mov rax, qword ptr [rbx + 0x58]
0020B21D  48 85 C0                        test rax, rax
0020B220  0F 84 65 FF FF FF               je 0x14020b18b
0020B226  80 BC 24 E0 00 00 00 00         cmp byte ptr [rsp + 0xe0], 0
0020B22E  0F 85 32 03 00 00               jne 0x14020b566
0020B234  B9 02 00 00 00                  mov ecx, 2
0020B239  48 8B 53 60                     mov rdx, qword ptr [rbx + 0x60]
0020B23D  44 0F B6 43 40                  movzx r8d, byte ptr [rbx + 0x40]
0020B242  41 C6 45 00 12                  mov byte ptr [r13], 0x12
0020B247  41 C6 45 02 58                  mov byte ptr [r13 + 2], 0x58
0020B24C  83 F9 02                        cmp ecx, 2
0020B24F  75 07                           jne 0x14020b258
0020B251  0F B6 8F 4A 02 00 00            movzx ecx, byte ptr [rdi + 0x24a]
0020B258  4C 8B 4C 24 78                  mov r9, qword ptr [rsp + 0x78]
0020B25D  41 88 49 50                     mov byte ptr [r9 + 0x50], cl
0020B261  49 89 7D 08                     mov qword ptr [r13 + 8], rdi
0020B265  48 8D 0D 04 8E 82 00            lea rcx, [rip + 0x828e04]
0020B26C  49 89 4D 20                     mov qword ptr [r13 + 0x20], rcx
0020B270  48 8D 0D F9 8D 82 00            lea rcx, [rip + 0x828df9]
0020B277  49 89 4D 28                     mov qword ptr [r13 + 0x28], rcx
0020B27B  49 89 45 30                     mov qword ptr [r13 + 0x30], rax
0020B27F  45 88 45 51                     mov byte ptr [r13 + 0x51], r8b
0020B283  49 89 55 38                     mov qword ptr [r13 + 0x38], rdx
0020B287  41 C6 45 52 00                  mov byte ptr [r13 + 0x52], 0
0020B28C  41 C6 45 01 00                  mov byte ptr [r13 + 1], 0
0020B291  41 B9 02 00 00 00               mov r9d, 2
0020B297  45 33 C0                        xor r8d, r8d
0020B29A  48 8B 53 48                     mov rdx, qword ptr [rbx + 0x48]
0020B29E  49 8B CD                        mov rcx, r13
0020B2A1  E8 6A 8C FF FF                  call 0x140203f10
0020B2A6  E9 FB FE FF FF                  jmp 0x14020b1a6
0020B2AB  48 83 7B 60 00                  cmp qword ptr [rbx + 0x60], 0
0020B2B0  0F 84 DE FE FF FF               je 0x14020b194
0020B2B6  F7 46 50 00 00 00 02            test dword ptr [rsi + 0x50], 0x2000000
0020B2BD  0F 85 39 02 00 00               jne 0x14020b4fc
0020B2C3  41 8B C4                        mov eax, r12d
0020B2C6  85 C0                           test eax, eax
0020B2C8  0F 85 C6 FE FF FF               jne 0x14020b194
0020B2CE  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
0020B2D3  49 89 45 00                     mov qword ptr [r13], rax
0020B2D7  44 89 A3 B8 00 00 00            mov dword ptr [rbx + 0xb8], r12d
0020B2DE  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
0020B2E2  8B 48 48                        mov ecx, dword ptr [rax + 0x48]
0020B2E5  83 F9 08                        cmp ecx, 8
0020B2E8  0F 84 81 02 00 00               je 0x14020b56f
0020B2EE  83 F9 14                        cmp ecx, 0x14
0020B2F1  0F 84 78 02 00 00               je 0x14020b56f
0020B2F7  48 8D 93 A8 00 00 00            lea rdx, [rbx + 0xa8]
0020B2FE  45 8B C4                        mov r8d, r12d
0020B301  49 8B CE                        mov rcx, r14
0020B304  E8 07 C6 18 00                  call 0x140397910
0020B309  E9 98 FE FF FF                  jmp 0x14020b1a6
0020B30E  48 8B D6                        mov rdx, rsi
0020B311  E8 32 22 1E 00                  call 0x1403ed548
0020B316  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
0020B31B  E9 52 FE FF FF                  jmp 0x14020b172
0020B320  45 33 C0                        xor r8d, r8d
0020B323  33 D2                           xor edx, edx
0020B325  E8 E6 3F 13 00                  call 0x14033f310
0020B32A  48 85 F6                        test rsi, rsi
0020B32D  0F 84 9D FD FF FF               je 0x14020b0d0
0020B333  41 8B 07                        mov eax, dword ptr [r15]
0020B336  A8 04                           test al, 4
0020B338  75 0E                           jne 0x14020b348
0020B33A  BA 44 66 6C 74                  mov edx, 0x746c6644
0020B33F  48 8B 4B 50                     mov rcx, qword ptr [rbx + 0x50]
0020B343  E8 98 C5 0E 00                  call 0x1402f78e0
0020B348  F6 46 50 02                     test byte ptr [rsi + 0x50], 2
0020B34C  0F 95 C1                        setne cl
0020B34F  41 F7 07 00 10 00 00            test dword ptr [r15], 0x1000
0020B356  0F 94 C0                        sete al
0020B359  84 C8                           test al, cl
0020B35B  0F 84 6F FD FF FF               je 0x14020b0d0
0020B361  E9 98 FE FF FF                  jmp 0x14020b1fe
0020B366  48 8B D6                        mov rdx, rsi
0020B369  48 8B CB                        mov rcx, rbx
0020B36C  E8 D7 21 1E 00                  call 0x1403ed548
0020B371  E9 7F FD FF FF                  jmp 0x14020b0f5
0020B376  44 38 63 41                     cmp byte ptr [rbx + 0x41], r12b
0020B37A  74 19                           je 0x14020b395
0020B37C  41 8B 07                        mov eax, dword ptr [r15]
0020B37F  A8 04                           test al, 4
0020B381  75 12                           jne 0x14020b395
0020B383  48 85 F6                        test rsi, rsi
0020B386  74 0D                           je 0x14020b395
0020B388  F7 46 50 02 00 00 00            test dword ptr [rsi + 0x50], 2
0020B38F  0F 84 80 FC FF FF               je 0x14020b015
0020B395  4C 8B 74 24 28                  mov r14, qword ptr [rsp + 0x28]
0020B39A  E9 BF FC FF FF                  jmp 0x14020b05e
0020B39F  49 83 38 01                     cmp qword ptr [r8], 1
0020B3A3  0F 85 03 FC FF FF               jne 0x14020afac
0020B3A9  C6 84 24 E0 00 00 00 01         mov byte ptr [rsp + 0xe0], 1
0020B3B1  E9 FE FB FF FF                  jmp 0x14020afb4
0020B3B6  48 8B 43 58                     mov rax, qword ptr [rbx + 0x58]
0020B3BA  4C 8B C0                        mov r8, rax
0020B3BD  4C 8B C8                        mov r9, rax
0020B3C0  49 D1 E9                        shr r9, 1
0020B3C3  41 83 E1 03                     and r9d, 3
0020B3C7  49 FF C9                        dec r9
0020B3CA  4B 8D 14 09                     lea rdx, [r9 + r9]
0020B3CE  48 8B C8                        mov rcx, rax
0020B3D1  48 83 E1 F9                     and rcx, 0xfffffffffffffff9
0020B3D5  48 0B D1                        or rdx, rcx
0020B3D8  F0 48 0F B1 53 58               lock cmpxchg qword ptr [rbx + 0x58], rdx
0020B3DE  4C 3B C0                        cmp r8, rax
0020B3E1  75 D7                           jne 0x14020b3ba
0020B3E3  45 85 C9                        test r9d, r9d
0020B3E6  75 08                           jne 0x14020b3f0
0020B3E8  48 8B CB                        mov rcx, rbx
0020B3EB  E8 80 2B 04 00                  call 0x14024df70
0020B3F0  4C 8B 74 24 28                  mov r14, qword ptr [rsp + 0x28]
0020B3F5  E9 AC FD FF FF                  jmp 0x14020b1a6
0020B3FA  48 8B CE                        mov rcx, rsi
0020B3FD  E8 76 72 24 00                  call 0x140452678
0020B402  E9 B2 FD FF FF                  jmp 0x14020b1b9
0020B407  44 38 63 41                     cmp byte ptr [rbx + 0x41], r12b
0020B40B  0F 85 5F FC FF FF               jne 0x14020b070
0020B411  48 8B 4B 50                     mov rcx, qword ptr [rbx + 0x50]
0020B415  48 85 C9                        test rcx, rcx
0020B418  0F 84 B2 FC FF FF               je 0x14020b0d0
0020B41E  48 85 F6                        test rsi, rsi
0020B421  0F 84 A9 FC FF FF               je 0x14020b0d0
0020B427  41 8B 07                        mov eax, dword ptr [r15]
0020B42A  A8 04                           test al, 4
0020B42C  0F 85 9E FC FF FF               jne 0x14020b0d0
0020B432  BA 44 66 6C 74                  mov edx, 0x746c6644
0020B437  E8 A4 C4 0E 00                  call 0x1402f78e0
0020B43C  E9 8F FC FF FF                  jmp 0x14020b0d0
0020B441  41 8B 07                        mov eax, dword ptr [r15]
0020B444  A8 04                           test al, 4
0020B446  0F 85 9C FC FF FF               jne 0x14020b0e8
0020B44C  48 85 F6                        test rsi, rsi
0020B44F  0F 84 EF FC FF FF               je 0x14020b144
0020B455  F7 46 50 02 00 00 00            test dword ptr [rsi + 0x50], 2
0020B45C  0F 85 86 FC FF FF               jne 0x14020b0e8
0020B462  E9 DD FC FF FF                  jmp 0x14020b144
0020B467  4C 8D 4C 24 48                  lea r9, [rsp + 0x48]
0020B46C  4C 8D 44 24 28                  lea r8, [rsp + 0x28]
0020B471  48 8D 94 24 E8 00 00 00         lea rdx, [rsp + 0xe8]
0020B479  48 8B CE                        mov rcx, rsi
0020B47C  E8 DF 87 23 00                  call 0x140443c60
0020B481  4C 8B 74 24 28                  mov r14, qword ptr [rsp + 0x28]
0020B486  E9 C1 FB FF FF                  jmp 0x14020b04c
0020B48B  48 8B 43 58                     mov rax, qword ptr [rbx + 0x58]
0020B48F  4C 8B C0                        mov r8, rax
0020B492  4C 8B C8                        mov r9, rax
0020B495  49 D1 E9                        shr r9, 1
0020B498  41 83 E1 03                     and r9d, 3
0020B49C  49 FF C9                        dec r9
0020B49F  4B 8D 14 09                     lea rdx, [r9 + r9]
0020B4A3  48 8B C8                        mov rcx, rax
0020B4A6  48 83 E1 F9                     and rcx, 0xfffffffffffffff9
0020B4AA  48 0B D1                        or rdx, rcx
0020B4AD  F0 48 0F B1 53 58               lock cmpxchg qword ptr [rbx + 0x58], rdx
0020B4B3  4C 3B C0                        cmp r8, rax
0020B4B6  75 D7                           jne 0x14020b48f
0020B4B8  45 85 C9                        test r9d, r9d
0020B4BB  0F 85 6F FC FF FF               jne 0x14020b130
0020B4C1  48 8B CB                        mov rcx, rbx
0020B4C4  E8 A7 2A 04 00                  call 0x14024df70
0020B4C9  E9 62 FC FF FF                  jmp 0x14020b130
0020B4CE  8B 43 30                        mov eax, dword ptr [rbx + 0x30]
0020B4D1  89 46 38                        mov dword ptr [rsi + 0x38], eax
0020B4D4  48 8B 84 24 F0 00 00 00         mov rax, qword ptr [rsp + 0xf0]
0020B4DC  48 8B 08                        mov rcx, qword ptr [rax]
0020B4DF  48 89 8B A0 00 00 00            mov qword ptr [rbx + 0xa0], rcx
0020B4E6  48 8D 8E 98 00 00 00            lea rcx, [rsi + 0x98]
0020B4ED  45 33 C0                        xor r8d, r8d
0020B4F0  33 D2                           xor edx, edx
0020B4F2  E8 19 3E 13 00                  call 0x14033f310
0020B4F7  E9 34 FC FF FF                  jmp 0x14020b130
0020B4FC  80 7B 41 00                     cmp byte ptr [rbx + 0x41], 0
0020B500  0F 85 BD FD FF FF               jne 0x14020b2c3
0020B506  8B 43 30                        mov eax, dword ptr [rbx + 0x30]
0020B509  25 00 00 00 C0                  and eax, 0xc0000000
0020B50E  3D 00 00 00 80                  cmp eax, 0x80000000
0020B513  0F 84 AA FD FF FF               je 0x14020b2c3
0020B519  B8 01 00 00 00                  mov eax, 1
0020B51E  E9 A3 FD FF FF                  jmp 0x14020b2c6
0020B523  48 8B 39                        mov rdi, qword ptr [rcx]
0020B526  E8 55 35 09 00                  call 0x14029ea80
0020B52B  48 8B CF                        mov rcx, rdi
0020B52E  48 85 FF                        test rdi, rdi
0020B531  75 F0                           jne 0x14020b523
0020B533  E9 BE FA FF FF                  jmp 0x14020aff6
0020B538  48 89 8B 98 00 00 00            mov qword ptr [rbx + 0x98], rcx
0020B53F  48 85 F6                        test rsi, rsi
0020B542  0F 84 FC B0 4C 00               je 0x1406d6644
0020B548  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
0020B54C  8B 48 48                        mov ecx, dword ptr [rax + 0x48]
0020B54F  83 F9 08                        cmp ecx, 8
0020B552  0F 84 E6 B0 4C 00               je 0x1406d663e
0020B558  83 F9 14                        cmp ecx, 0x14
0020B55B  0F 84 DD B0 4C 00               je 0x1406d663e
0020B561  E9 DE B0 4C 00                  jmp 0x1406d6644
0020B566  0F BE 4B 46                     movsx ecx, byte ptr [rbx + 0x46]
0020B56A  E9 CA FC FF FF                  jmp 0x14020b239
0020B56F  41 BC 01 00 00 00               mov r12d, 1
0020B575  E9 7D FD FF FF                  jmp 0x14020b2f7
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopCompleteRequest(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_mA0;
    unsigned int v_stack_mA8;
    unsigned __int8 v_stack_p18;
    unsigned __int8 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p78;
    unsigned __int64 v_stack_p8;
    unsigned __int8 v_stack_pE0;
    unsigned __int8 v_stack_pE8;

    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (144);
    v_stack_m50 = a1;
    v_r12 = 0;
    v_stack_mA0 = 0;
    v_stack_m80 = 0;
    v_stack_p20 = 0;
    v_stack_m70 = a1 - 120;
    v_stack_m88 = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_stack_m68 = *(unsigned __int64 *)(a4);
    if (a3 != 0) goto loc_0020B39F;
loc_0020AFAC:
    v_stack_p18 = 0;
loc_0020AFB4:
    v_stack_m58 = a1 - 120 + 16;
    if (condition_is_below) goto loc_0020B538;
    if (sign_flag) goto loc_0020B4CE;
    if (condition_is_below) goto loc_0020B1D4;
    v_stack_m90 = 0;
loc_0020AFE1:
    result = IopProcessBufferedIoCompletion(a1 - 120, a2, a3, a4);
    if (*(unsigned __int64 *)(a1 - 120 + 8) != 0) goto loc_0020B523;
loc_0020AFF6:
    *(unsigned __int64 *)(a1 - 120 + 8) = 0;
    v_stack_m60 = a1 - 120 + 48;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 - 120 + 48))) & (0xC0000000ULL));
    if (((unsigned int)(result)) == 0xC0000000ULL) goto loc_0020B376;
loc_0020B015:
    if (*(unsigned __int64 *)(a4) == 0) goto loc_0020B395;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a4) + 176) == 0) goto loc_0020B395;
    if (((*(unsigned int *)(a1 - 120 + 16)) & (0x2000ULL)) == 0) goto loc_0020B467;
    v_stack_mA0 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4) + 176));
    v_stack_m80 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4) + 176) + 8);
loc_0020B04C:
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4) + 176) + 8);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4) + 176)) != 0) {
        a2 = 0x746C6644ULL;
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4) + 176));
        result = ObfReferenceObjectWithTag(a1, a2, a3, a4);
    }
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 - 120 + 48))) & (0xC0000000ULL));
    if (((unsigned int)(result)) == 0xC0000000ULL) goto loc_0020B407;
loc_0020B070:
    v_stack_mA8 = 0;
    if (((*(unsigned __int8 *)(a1 - 120 + 71)) & (16)) != 0) goto loc_0020B089;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 - 120 + 72) + 8) = *(unsigned __int64 *)(a1 - 120 + 56);
    goto loc_0020B08F;
loc_0020B089:
    *(unsigned int *)(*(unsigned __int64 *)(a1 - 120 + 72) + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 - 120 + 56)));
loc_0020B08F:
    *(unsigned int *)(*(unsigned __int64 *)(a1 - 120 + 72)) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 - 120 + 48)));
    goto loc_0020B0BA;
loc_0020B0BA:
    if (*(unsigned __int64 *)(a1 - 120 + 80) != 0) goto loc_0020B320;
    if (*(unsigned __int64 *)(a4) != 0) goto loc_0020B1F5;
loc_0020B0D0:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 - 120 + 48))) & (0xC0000000ULL));
    if (((unsigned int)(result)) != 0xC0000000ULL) goto loc_0020B144;
    if ((*(unsigned __int8 *)(a1 - 120 + 65)) != 0) goto loc_0020B441;
loc_0020B0E8:
    if (((*(unsigned int *)(a1 - 120 + 16)) & (0x2000ULL)) != 0) goto loc_0020B366;
loc_0020B0F5:
    if (*(unsigned __int64 *)(a4) != 0) {
        a2 = 0x746C6644ULL;
        a1 = *(unsigned __int64 *)(a4);
        result = ObDereferenceObjectDeferDeleteWithTag(a1, a2, a3, a4);
    }
    if (((*(unsigned int *)(a1 - 120 + 16)) & (0x8000ULL)) != 0) goto loc_0020B48B;
    *(unsigned __int64 *)(a1 - 120 + 152) = v_stack_m88;
    result = IopDequeueIrpFromThread(a1 - 120, a2, a3, a4);
    result = IoFreeIrp(a1 - 120, a2, a3, a4);
loc_0020B130:
    v_rsp = (v_rsp) + (144);
    return result;
loc_0020B144:
    result = IopUpdateIrpTransferCount(a1 - 120, v_stack_p38, a3, a4);
    if (((*(unsigned int *)(a1 - 120 + 16)) & (0x2000ULL)) != 0) goto loc_0020B30E;
    *(unsigned __int64 *)(a1 - 120 + 152) = v_stack_p40;
    result = IopDequeueIrpFromThread(a1 - 120, v_stack_p38, a3, a4);
loc_0020B172:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 - 120 + 16))))) & (0x8000ULL));
    if (!(condition_is_not_equal)) {
    }
    if ((unsigned int)(result) == 0) goto loc_0020B219;
loc_0020B18B:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4) + 176)) != 0) goto loc_0020B2AB;
loc_0020B194:
    if (condition_is_below) goto loc_0020B3B6;
    result = IoFreeIrp(a1 - 120, v_stack_p38, a3, a4);
loc_0020B1A6:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4) + 176)) != 0) goto loc_0020B1E6;
loc_0020B1AB:
    if (v_stack_pE8 != 0) goto loc_0020B3FA;
loc_0020B1B9:
    if (*(unsigned __int64 *)(a4) == 0) goto loc_0020B130;
    result = ObDereferenceObjectDeferDeleteWithTag(*(unsigned __int64 *)(a4), (unsigned int)(0x746C6644ULL), a3, a4);
    goto loc_0020B130;
loc_0020B1D4:
    v_rdi = (*(unsigned __int64 *)(a1 - 120 + 88)) & (-7);
    v_stack_p38 = v_rdi;
    goto loc_0020AFE1;
loc_0020B1E6:
    result = ObfDereferenceObjectWithTag(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4) + 176)), (unsigned int)(0x746C6644ULL), a3, a4);
    goto loc_0020B1AB;
loc_0020B1F5:
    if (((*(unsigned int *)(*(unsigned __int64 *)(a4) + 80)) & (0x4000000ULL)) == 0) {
        a3 = 0;
        a2 = 0;
        a1 = *(unsigned __int64 *)(a4) + 152;
        result = KeSetEvent(a1, a2, a3, a4);
    }
    *(unsigned int *)(*(unsigned __int64 *)(a4) + 56) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rdi)));
    goto loc_0020B0D0;
loc_0020B219:
    if (*(unsigned __int64 *)(a1 - 120 + 88) == 0) goto loc_0020B18B;
    if (v_stack_pE0 != 0) goto loc_0020B566;
loc_0020B239:
    *(unsigned __int8 *)(a1) = 18;
    *(unsigned __int8 *)(a1 + 2) = 88;
    if (2 == 2) {
        a1 = *(unsigned __int8 *)(v_rdi + 586);
    }
    *(unsigned __int8 *)(v_stack_p78 + 80) = (unsigned __int8)(a1);
    *(unsigned __int64 *)(a1 + 8) = v_rdi;
    *(unsigned __int64 *)(a1 + 32) = v_rip + 8556036;
    *(unsigned __int64 *)(a1 + 40) = v_rip + 8556025;
    *(unsigned __int64 *)(a1 + 48) = *(unsigned __int64 *)(a1 - 120 + 88);
    *(unsigned __int8 *)(a1 + 81) = (unsigned __int8)(*(unsigned __int8 *)(a1 - 120 + 64));
    *(unsigned __int64 *)(a1 + 56) = *(unsigned __int64 *)(a1 - 120 + 96);
    *(unsigned __int8 *)(a1 + 82) = 0;
    *(unsigned __int8 *)(a1 + 1) = 0;
    a3 = 0;
    result = KeInsertQueueApc(a1, *(unsigned __int64 *)(a1 - 120 + 72), a3, 2);
    goto loc_0020B1A6;
loc_0020B2AB:
    if ((*(unsigned __int64 *)(a1 - 120 + 96)) == 0) goto loc_0020B194;
    if (((*(unsigned int *)(*(unsigned __int64 *)(a4) + 80)) & (0x2000000ULL)) != 0) goto loc_0020B4FC;
loc_0020B2C3:
loc_0020B2C6:
    if (0 != 0) goto loc_0020B194;
    *(unsigned __int64 *)(a1) = v_stack_p48;
    *(unsigned int *)(a1 - 120 + 184) = 0;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4) + 8) + 72)))) == 8) goto loc_0020B56F;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4) + 8) + 72)))) == 20) goto loc_0020B56F;
loc_0020B2F7:
    result = KeInsertQueueEx(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4) + 176)), a1 - 120 + 168, 0, 2);
    goto loc_0020B1A6;
loc_0020B30E:
    result = IopDequeueIrpFromFileObject(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4) + 176)), *(unsigned __int64 *)(a4), 0, 2);
    goto loc_0020B172;
loc_0020B320:
    a3 = 0;
    a2 = 0;
    result = KeSetEvent(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4) + 176)), a2, a3, 2);
    if (*(unsigned __int64 *)(a4) == 0) goto loc_0020B0D0;
    result = (unsigned int)(*(unsigned int *)(a1 - 120 + 16));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 - 120 + 16)))) & (4)) == 0) {
        a2 = 0x746C6644ULL;
        a1 = *(unsigned __int64 *)(a1 - 120 + 80);
        result = ObfDereferenceObjectWithTag(a1, a2, a3, 2);
    }
    a1 = (((*(unsigned __int8 *)(*(unsigned __int64 *)(a4) + 80)) & (2)) != 0) ? 1 : 0;
    result = (((*(unsigned int *)(a1 - 120 + 16)) & (0x1000ULL)) == 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_0020B0D0;
    goto loc_0020B1FE;
loc_0020B366:
    result = IopDequeueIrpFromFileObject(a1 - 120, *(unsigned __int64 *)(a4), a3, 2);
    goto loc_0020B0F5;
loc_0020B376:
    if ((*(unsigned __int8 *)(a1 - 120 + 65)) == 0) goto loc_0020B395;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 - 120 + 16)))) & (4)) != 0) goto loc_0020B395;
    if (*(unsigned __int64 *)(a4) == 0) goto loc_0020B395;
    if (((*(unsigned int *)(*(unsigned __int64 *)(a4) + 80)) & (2)) == 0) goto loc_0020B015;
loc_0020B395:
    goto loc_0020B05E;
loc_0020B39F:
    if ((*(unsigned __int64 *)(a3)) != 1) goto loc_0020AFAC;
    v_stack_pE0 = 1;
    goto loc_0020AFB4;
loc_0020B3B6:
loc_0020B3BA:
    a4 = (*(unsigned __int64 *)(a1 - 120 + 88)) >> (1);
    a4 = (unsigned int)((a4) & (3));
    a4 = (a4) - 1;
    a1 = (*(unsigned __int64 *)(a1 - 120 + 88)) & (-7);
    a2 = (a4 + a4 * 1) | (a1);
    if ((*(unsigned __int64 *)(a1 - 120 + 88)) != (*(unsigned __int64 *)(a1 - 120 + 88))) goto loc_0020B3BA;
    result = *(unsigned __int64 *)(a1 - 120 + 88);
    if ((unsigned int)(a4) == 0) {
        a1 = a1 - 120;
        result = IoFreeIrp(a1, a2, *(unsigned __int64 *)(a1 - 120 + 88), a4);
    }
    goto loc_0020B1A6;
loc_0020B3FA:
    result = IopDecrementCompletionContextUsageCount(*(unsigned __int64 *)(a4), a2, *(unsigned __int64 *)(a1 - 120 + 88), a4);
    goto loc_0020B1B9;
loc_0020B407:
    if ((*(unsigned __int8 *)(a1 - 120 + 65)) != 0) goto loc_0020B070;
    if (*(unsigned __int64 *)(a1 - 120 + 80) == 0) goto loc_0020B0D0;
    if (*(unsigned __int64 *)(a4) == 0) goto loc_0020B0D0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 - 120 + 16)))) & (4)) != 0) goto loc_0020B0D0;
    result = ObfDereferenceObjectWithTag(*(unsigned __int64 *)(a1 - 120 + 80), (unsigned int)(0x746C6644ULL), *(unsigned __int64 *)(a1 - 120 + 88), a4);
    goto loc_0020B0D0;
loc_0020B441:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 - 120 + 16)))) & (4)) != 0) goto loc_0020B0E8;
    if (*(unsigned __int64 *)(a4) == 0) goto loc_0020B144;
    if (((*(unsigned int *)(*(unsigned __int64 *)(a4) + 80)) & (2)) != 0) goto loc_0020B0E8;
    goto loc_0020B144;
loc_0020B467:
    result = IopIncrementCompletionContextUsageCountAndReadData(*(unsigned __int64 *)(a4), v_stack_pE8, v_stack_p28, v_stack_p48);
    goto loc_0020B04C;
loc_0020B48B:
loc_0020B48F:
    a4 = (*(unsigned __int64 *)(a1 - 120 + 88)) >> (1);
    a4 = (unsigned int)((a4) & (3));
    a4 = (a4) - 1;
    a1 = (*(unsigned __int64 *)(a1 - 120 + 88)) & (-7);
    a2 = (a4 + a4 * 1) | (a1);
    if ((*(unsigned __int64 *)(a1 - 120 + 88)) != (*(unsigned __int64 *)(a1 - 120 + 88))) goto loc_0020B48F;
    if ((unsigned int)(a4) != 0) goto loc_0020B130;
    result = IoFreeIrp(a1 - 120, a2, *(unsigned __int64 *)(a1 - 120 + 88), a4);
    goto loc_0020B130;
loc_0020B4CE:
    *(unsigned int *)(*(unsigned __int64 *)(a4) + 56) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 - 120 + 48)));
    *(unsigned __int64 *)(a1 - 120 + 160) = *(unsigned __int64 *)(a5);
    a3 = 0;
    a2 = 0;
    result = KeSetEvent(*(unsigned __int64 *)(a4) + 152, a2, a3, a4);
    goto loc_0020B130;
loc_0020B4FC:
    if ((*(unsigned __int8 *)(a1 - 120 + 65)) != 0) goto loc_0020B2C3;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 - 120 + 48))) & (0xC0000000ULL));
    if (((unsigned int)(result)) == 0x80000000ULL) goto loc_0020B2C3;
    goto loc_0020B2C6;
loc_0020B523:
    result = IoFreeMdl(*(unsigned __int64 *)(a4) + 152, a2, a3, a4);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a4) + 152) != 0) goto loc_0020B523;
    goto loc_0020AFF6;
loc_0020B538:
    *(unsigned __int64 *)(a1 - 120 + 152) = *(unsigned __int64 *)(*(unsigned __int64 *)(a4) + 152);
loc_0020B566:
    goto loc_0020B239;
loc_0020B56F:
    goto loc_0020B2F7;
}
```

## 5. (Beta) C Style

```c
int64_t IopCompleteRequest(void *Arg1, int64_t Arg2, int64_t Arg3, void *Arg4, void *Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg4 = (uint8_t *)Arg4;
    uint8_t *arg5 = (uint8_t *)Arg5;

    int64_t result;
    int64_t local_r12;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_mA0;
    uint32_t v_stack_mA8;
    uint8_t v_stack_p18;
    uint8_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p78;
    uint64_t v_stack_p8;
    uint8_t v_stack_pE0;
    uint8_t v_stack_pE8;

    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (144);
    v_stack_m50 = Arg1;
    local_r12 = 0;
    v_stack_mA0 = 0;
    v_stack_m80 = 0;
    v_stack_p20 = 0;
    v_stack_m70 = Arg1 - 120;
    v_stack_m88 = *(uint64_t *)(gs_base + (0 + 0x188));
    v_stack_m68 = *(uint64_t *)(arg4);
    if (Arg3 != 0) goto loc_0020B39F;
loc_0020AFAC:
    v_stack_p18 = 0;
loc_0020AFB4:
    v_stack_m58 = Arg1 - 120 + 16;
    if (condition_is_below) goto loc_0020B538;
    if (sign_flag) goto loc_0020B4CE;
    if (condition_is_below) goto loc_0020B1D4;
    v_stack_m90 = 0;
loc_0020AFE1:
    result = IopProcessBufferedIoCompletion(Arg1 - 120, Arg2, Arg3, Arg4);
    if (*(uint64_t *)(arg1 - 0x78 + 0x8) != 0) goto loc_0020B523;
loc_0020AFF6:
    *(uint64_t *)(arg1 - 0x78 + 0x8) = 0;
    v_stack_m60 = Arg1 - 120 + 48;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 - 0x78 + 0x30))) & (0xC0000000ULL));
    if (((uint32_t)(result)) == 0xC0000000ULL) goto loc_0020B376;
loc_0020B015:
    if (*(uint64_t *)(arg4) == 0) goto loc_0020B395;
    if (*(uint64_t *)(*(uint64_t *)(arg4) + 0xB0) == 0) goto loc_0020B395;
    if (((*(uint32_t *)(arg1 - 0x78 + 0x10)) & (0x2000ULL)) == 0) goto loc_0020B467;
    v_stack_mA0 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg4) + 0xB0));
    v_stack_m80 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg4) + 0xB0) + 0x8);
loc_0020B04C:
    result = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg4) + 0xB0) + 0x8);
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg4) + 0xB0)) != 0) {
        Arg2 = 0x746C6644ULL;
        Arg1 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg4) + 0xB0));
        result = ObfReferenceObjectWithTag(Arg1, Arg2, Arg3, Arg4);
    }
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 - 0x78 + 0x30))) & (0xC0000000ULL));
    if (((uint32_t)(result)) == 0xC0000000ULL) goto loc_0020B407;
loc_0020B070:
    v_stack_mA8 = 0;
    if (((*(uint8_t *)(arg1 - 0x78 + 0x47)) & (16)) != 0) goto loc_0020B089;
    *(uint64_t *)(*(uint64_t *)(arg1 - 0x78 + 0x48) + 0x8) = *(uint64_t *)(arg1 - 0x78 + 0x38);
    goto loc_0020B08F;
loc_0020B089:
    *(uint32_t *)(*(uint64_t *)(arg1 - 0x78 + 0x48) + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 - 0x78 + 0x38)));
loc_0020B08F:
    *(uint32_t *)(*(uint64_t *)(arg1 - 0x78 + 0x48)) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 - 0x78 + 0x30)));
    goto loc_0020B0BA;
loc_0020B0BA:
    if (*(uint64_t *)(arg1 - 0x78 + 0x50) != 0) goto loc_0020B320;
    if (*(uint64_t *)(arg4) != 0) goto loc_0020B1F5;
loc_0020B0D0:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 - 0x78 + 0x30))) & (0xC0000000ULL));
    if (((uint32_t)(result)) != 0xC0000000ULL) goto loc_0020B144;
    if ((*(uint8_t *)(arg1 - 0x78 + 0x41)) != 0) goto loc_0020B441;
loc_0020B0E8:
    if (((*(uint32_t *)(arg1 - 0x78 + 0x10)) & (0x2000ULL)) != 0) goto loc_0020B366;
loc_0020B0F5:
    if (*(uint64_t *)(arg4) != 0) {
        Arg2 = 0x746C6644ULL;
        Arg1 = *(uint64_t *)(arg4);
        result = ObDereferenceObjectDeferDeleteWithTag(Arg1, Arg2, Arg3, Arg4);
    }
    if (((*(uint32_t *)(arg1 - 0x78 + 0x10)) & (0x8000ULL)) != 0) goto loc_0020B48B;
    *(uint64_t *)(arg1 - 0x78 + 0x98) = v_stack_m88;
    result = IopDequeueIrpFromThread(Arg1 - 120, Arg2, Arg3, Arg4);
    result = IoFreeIrp(Arg1 - 120, Arg2, Arg3, Arg4);
loc_0020B130:
    local_rsp = (local_rsp) + (144);
    return result;
loc_0020B144:
    result = IopUpdateIrpTransferCount(Arg1 - 120, v_stack_p38, Arg3, Arg4);
    if (((*(uint32_t *)(arg1 - 0x78 + 0x10)) & (0x2000ULL)) != 0) goto loc_0020B30E;
    *(uint64_t *)(arg1 - 0x78 + 0x98) = v_stack_p40;
    result = IopDequeueIrpFromThread(Arg1 - 120, v_stack_p38, Arg3, Arg4);
loc_0020B172:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 - 0x78 + 0x10))))) & (0x8000ULL));
    if (!(condition_is_not_equal)) {
    }
    if ((uint32_t)(result) == 0) goto loc_0020B219;
loc_0020B18B:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg4) + 0xB0)) != 0) goto loc_0020B2AB;
loc_0020B194:
    if (condition_is_below) goto loc_0020B3B6;
    result = IoFreeIrp(Arg1 - 120, v_stack_p38, Arg3, Arg4);
loc_0020B1A6:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg4) + 0xB0)) != 0) goto loc_0020B1E6;
loc_0020B1AB:
    if (v_stack_pE8 != 0) goto loc_0020B3FA;
loc_0020B1B9:
    if (*(uint64_t *)(arg4) == 0) goto loc_0020B130;
    result = ObDereferenceObjectDeferDeleteWithTag(*(uint64_t *)(arg4), (uint32_t)(0x746C6644ULL), Arg3, Arg4);
    goto loc_0020B130;
loc_0020B1D4:
    local_rdi = (*(uint64_t *)(arg1 - 0x78 + 0x58)) & (-7);
    v_stack_p38 = local_rdi;
    goto loc_0020AFE1;
loc_0020B1E6:
    result = ObfDereferenceObjectWithTag(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg4) + 0xB0)), (uint32_t)(0x746C6644ULL), Arg3, Arg4);
    goto loc_0020B1AB;
loc_0020B1F5:
    if (((*(uint32_t *)(*(uint64_t *)(arg4) + 0x50)) & (0x4000000ULL)) == 0) {
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = *(uint64_t *)(arg4) + 152;
        result = KeSetEvent(Arg1, Arg2, Arg3, Arg4);
    }
    *(uint32_t *)(*(uint64_t *)(arg4) + 0x38) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rdi)));
    goto loc_0020B0D0;
loc_0020B219:
    if (*(uint64_t *)(arg1 - 0x78 + 0x58) == 0) goto loc_0020B18B;
    if (v_stack_pE0 != 0) goto loc_0020B566;
loc_0020B239:
    *(uint8_t *)(arg1) = 18;
    *(uint8_t *)(arg1 + 0x2) = 88;
    if (2 == 2) {
        Arg1 = *(uint8_t *)(local_rdi + 0x24A);
    }
    *(uint8_t *)(v_stack_p78 + 0x50) = (uint8_t)(Arg1);
    *(uint64_t *)(arg1 + 0x8) = local_rdi;
    *(uint64_t *)(arg1 + 0x20) = v_rip + 8556036;
    *(uint64_t *)(arg1 + 0x28) = v_rip + 8556025;
    *(uint64_t *)(arg1 + 0x30) = *(uint64_t *)(arg1 - 0x78 + 0x58);
    *(uint8_t *)(arg1 + 0x51) = (uint8_t)(*(uint8_t *)(arg1 - 0x78 + 0x40));
    *(uint64_t *)(arg1 + 0x38) = *(uint64_t *)(arg1 - 0x78 + 0x60);
    *(uint8_t *)(arg1 + 0x52) = 0;
    *(uint8_t *)(arg1 + 0x1) = 0;
    Arg3 = 0;
    result = KeInsertQueueApc(Arg1, *(uint64_t *)(arg1 - 0x78 + 0x48), Arg3, 2);
    goto loc_0020B1A6;
loc_0020B2AB:
    if ((*(uint64_t *)(arg1 - 0x78 + 0x60)) == 0) goto loc_0020B194;
    if (((*(uint32_t *)(*(uint64_t *)(arg4) + 0x50)) & (0x2000000ULL)) != 0) goto loc_0020B4FC;
loc_0020B2C3:
loc_0020B2C6:
    if (0 != 0) goto loc_0020B194;
    *(uint64_t *)(arg1) = v_stack_p48;
    *(uint32_t *)(arg1 - 0x78 + 0xB8) = 0;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg4) + 0x8) + 0x48)))) == 8) goto loc_0020B56F;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg4) + 0x8) + 0x48)))) == 20) goto loc_0020B56F;
loc_0020B2F7:
    result = KeInsertQueueEx(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg4) + 0xB0)), Arg1 - 120 + 168, 0, 2);
    goto loc_0020B1A6;
loc_0020B30E:
    result = IopDequeueIrpFromFileObject(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg4) + 0xB0)), *(uint64_t *)(arg4), 0, 2);
    goto loc_0020B172;
loc_0020B320:
    Arg3 = 0;
    Arg2 = 0;
    result = KeSetEvent(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg4) + 0xB0)), Arg2, Arg3, 2);
    if (*(uint64_t *)(arg4) == 0) goto loc_0020B0D0;
    result = (uint32_t)(*(uint32_t *)(arg1 - 0x78 + 0x10));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 - 0x78 + 0x10)))) & (4)) == 0) {
        Arg2 = 0x746C6644ULL;
        Arg1 = *(uint64_t *)(arg1 - 0x78 + 0x50);
        result = ObfDereferenceObjectWithTag(Arg1, Arg2, Arg3, 2);
    }
    Arg1 = (((*(uint8_t *)(*(uint64_t *)(arg4) + 0x50)) & (2)) != 0) ? 1 : 0;
    result = (((*(uint32_t *)(arg1 - 0x78 + 0x10)) & (0x1000ULL)) == 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_0020B0D0;
    goto loc_0020B1FE;
loc_0020B366:
    result = IopDequeueIrpFromFileObject(Arg1 - 120, *(uint64_t *)(arg4), Arg3, 2);
    goto loc_0020B0F5;
loc_0020B376:
    if ((*(uint8_t *)(arg1 - 0x78 + 0x41)) == 0) goto loc_0020B395;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 - 0x78 + 0x10)))) & (4)) != 0) goto loc_0020B395;
    if (*(uint64_t *)(arg4) == 0) goto loc_0020B395;
    if (((*(uint32_t *)(*(uint64_t *)(arg4) + 0x50)) & (2)) == 0) goto loc_0020B015;
loc_0020B395:
    goto loc_0020B05E;
loc_0020B39F:
    if ((*(uint64_t *)(Arg3)) != 1) goto loc_0020AFAC;
    v_stack_pE0 = 1;
    goto loc_0020AFB4;
loc_0020B3B6:
loc_0020B3BA:
    Arg4 = (*(uint64_t *)(arg1 - 0x78 + 0x58)) >> (1);
    Arg4 = (uint32_t)((Arg4) & (3));
    Arg4 = (Arg4) - 1;
    Arg1 = (*(uint64_t *)(arg1 - 0x78 + 0x58)) & (-7);
    Arg2 = (Arg4 + Arg4 * 1) | (Arg1);
    if ((*(uint64_t *)(arg1 - 0x78 + 0x58)) != (*(uint64_t *)(arg1 - 0x78 + 0x58))) goto loc_0020B3BA;
    result = *(uint64_t *)(arg1 - 0x78 + 0x58);
    if ((uint32_t)(Arg4) == 0) {
        Arg1 = Arg1 - 120;
        result = IoFreeIrp(Arg1, Arg2, *(uint64_t *)(arg1 - 0x78 + 0x58), Arg4);
    }
    goto loc_0020B1A6;
loc_0020B3FA:
    result = IopDecrementCompletionContextUsageCount(*(uint64_t *)(arg4), Arg2, *(uint64_t *)(arg1 - 0x78 + 0x58), Arg4);
    goto loc_0020B1B9;
loc_0020B407:
    if ((*(uint8_t *)(arg1 - 0x78 + 0x41)) != 0) goto loc_0020B070;
    if (*(uint64_t *)(arg1 - 0x78 + 0x50) == 0) goto loc_0020B0D0;
    if (*(uint64_t *)(arg4) == 0) goto loc_0020B0D0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 - 0x78 + 0x10)))) & (4)) != 0) goto loc_0020B0D0;
    result = ObfDereferenceObjectWithTag(*(uint64_t *)(arg1 - 0x78 + 0x50), (uint32_t)(0x746C6644ULL), *(uint64_t *)(arg1 - 0x78 + 0x58), Arg4);
    goto loc_0020B0D0;
loc_0020B441:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 - 0x78 + 0x10)))) & (4)) != 0) goto loc_0020B0E8;
    if (*(uint64_t *)(arg4) == 0) goto loc_0020B144;
    if (((*(uint32_t *)(*(uint64_t *)(arg4) + 0x50)) & (2)) != 0) goto loc_0020B0E8;
    goto loc_0020B144;
loc_0020B467:
    result = IopIncrementCompletionContextUsageCountAndReadData(*(uint64_t *)(arg4), v_stack_pE8, v_stack_p28, v_stack_p48);
    goto loc_0020B04C;
loc_0020B48B:
loc_0020B48F:
    Arg4 = (*(uint64_t *)(arg1 - 0x78 + 0x58)) >> (1);
    Arg4 = (uint32_t)((Arg4) & (3));
    Arg4 = (Arg4) - 1;
    Arg1 = (*(uint64_t *)(arg1 - 0x78 + 0x58)) & (-7);
    Arg2 = (Arg4 + Arg4 * 1) | (Arg1);
    if ((*(uint64_t *)(arg1 - 0x78 + 0x58)) != (*(uint64_t *)(arg1 - 0x78 + 0x58))) goto loc_0020B48F;
    if ((uint32_t)(Arg4) != 0) goto loc_0020B130;
    result = IoFreeIrp(Arg1 - 120, Arg2, *(uint64_t *)(arg1 - 0x78 + 0x58), Arg4);
    goto loc_0020B130;
loc_0020B4CE:
    *(uint32_t *)(*(uint64_t *)(arg4) + 0x38) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 - 0x78 + 0x30)));
    *(uint64_t *)(arg1 - 0x78 + 0xA0) = *(uint64_t *)(arg5);
    Arg3 = 0;
    Arg2 = 0;
    result = KeSetEvent(*(uint64_t *)(arg4) + 152, Arg2, Arg3, Arg4);
    goto loc_0020B130;
loc_0020B4FC:
    if ((*(uint8_t *)(arg1 - 0x78 + 0x41)) != 0) goto loc_0020B2C3;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 - 0x78 + 0x30))) & (0xC0000000ULL));
    if (((uint32_t)(result)) == 0x80000000ULL) goto loc_0020B2C3;
    goto loc_0020B2C6;
loc_0020B523:
    result = IoFreeMdl(*(uint64_t *)(arg4) + 152, Arg2, Arg3, Arg4);
    if (*(uint64_t *)(*(uint64_t *)(arg4) + 0x98) != 0) goto loc_0020B523;
    goto loc_0020AFF6;
loc_0020B538:
    *(uint64_t *)(arg1 - 0x78 + 0x98) = *(uint64_t *)(*(uint64_t *)(arg4) + 0x98);
loc_0020B566:
    goto loc_0020B239;
loc_0020B56F:
    goto loc_0020B2F7;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `- 0x78` | `64` | `R` |
| `Arg1` | `+ 0x0` | `8` | `W` |
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg1` | `+ 0x1` | `8` | `W` |
| `Arg1` | `+ 0x2` | `8` | `W` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `W` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `W` |
| `Arg1` | `+ 0x28` | `64` | `W` |
| `Arg1` | `+ 0x30` | `32` | `R` |
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x30` | `64` | `W` |
| `Arg1` | `+ 0x38` | `32` | `R` |
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg1` | `+ 0x38` | `64` | `W` |
| `Arg1` | `+ 0x40` | `8` | `R` |
| `Arg1` | `+ 0x41` | `8` | `R` |
| `Arg1` | `+ 0x46` | `8` | `R` |
| `Arg1` | `+ 0x47` | `8` | `R` |
| `Arg1` | `+ 0x48` | `64` | `R` |
| `Arg1` | `+ 0x50` | `64` | `R` |
| `Arg1` | `+ 0x51` | `8` | `W` |
| `Arg1` | `+ 0x52` | `8` | `W` |
| `Arg1` | `+ 0x58` | `64` | `R` |
| `Arg1` | `+ 0x58` | `64` | `R/W` |
| `Arg1` | `+ 0x60` | `64` | `R` |
| `Arg1` | `+ 0x98` | `64` | `W` |
| `Arg1` | `+ 0xA0` | `64` | `W` |
| `Arg1` | `+ 0xA8` | `64` | `R` |
| `Arg1` | `+ 0xB8` | `32` | `W` |

추가 오프셋 2개는 표에서 생략했습니다.

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0020AF50&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
