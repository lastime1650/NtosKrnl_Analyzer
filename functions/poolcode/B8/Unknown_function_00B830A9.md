# sub_00B830A9

- RVA: `0x00B830A9`–`0x00B836C7` (길이 `1,566` bytes)
- VA: `0x0000000140B830A9`
- 실행 섹션: `POOLCODE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007BE44`
- 디코드: `365`개 명령, `1,566/1,566` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **13**; 고유 호출 대상: **12**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **17**

### Outgoing calls
- `0x00B83136` → [ExpAcquireSpinLockSharedAtDpcLevelInstrumented](../../text/27/ExpAcquireSpinLockSharedAtDpcLevelInstrumented_function_0027CD20.md) (function, `0x0027CD20`)
- `0x00B831A7` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00B8338F` → [ObpPushStackInfo](../../text/21/ObpPushStackInfo_function_002109E4.md) (function, `0x002109E4`)
- `0x00B83436` → [KiLowerIrqlProcessIrqlFlags](../../text/4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x00B83471` → [ExpPoolTrackerReturnLimit](../../text/36/ExpPoolTrackerReturnLimit_function_00361570.md) (function, `0x00361570`)
- `0x00B834CD` → [RtlpHpVsContextFree](../../text/36/RtlpHpVsContextFree_function_00361630.md) (function, `0x00361630`)
- `0x00B83563` → [KiAcquireQueuedSpinLockInstrumented](../../text/27/KiAcquireQueuedSpinLockInstrumented_function_00275850.md) (function, `0x00275850`)
- `0x00B835B5` → [ExpWaitForSpinLockSharedAndAcquire](../../text/36/ExpWaitForSpinLockSharedAndAcquire_function_00362380.md) (function, `0x00362380`)
- `0x00B835C6` → [KiRaiseIrqlProcessIrqlFlags](../../text/4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x00B835DD` → [RtlpHpSegPageRangeShrink](../../text/2E/RtlpHpSegPageRangeShrink_function_002E2FA0.md) (function, `0x002E2FA0`)
- `0x00B835FF` → [RtlpLogHeapFailure](../../text/35/RtlpLogHeapFailure_function_0035B7BC.md) (function, `0x0035B7BC`)
- `0x00B8367C` → [RtlpHpEnvCompactionSchedule](../../text/32/RtlpHpEnvCompactionSchedule_function_003264A0.md) (function, `0x003264A0`)
- `0x00B8368A` → [KiRaiseIrqlProcessIrqlFlags](../../text/4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00B830C9` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x00B83103` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x00B83110` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x00B8311D` → RVA `0x00F0DE58` (`.data`; read)
- `0x00B8312F` → RVA `0x00EFACF8` (`.data`; read)
- `0x00B8313B` → RVA `0x00EFED38` (`.data`; read)
- `0x00B83145` → RVA `0x00EFED30` (`.data`; read)
- `0x00B831CA` → RVA `0x00FC7228` (`ALMOSTRO`; read)
- `0x00B831E1` → RVA `0x00EFED20` (`.data`; read)
- `0x00B832A1` → RVA `0x00FC6AB0` (`ALMOSTRO`; read)
- `0x00B83322` → RVA `0x00E27F80` (`.data`; read)
- `0x00B83379` → RVA `0x00FC5010` (`ALMOSTRO`; read)
- `0x00B833F7` → RVA `0x00FCF100` (`CACHEALI`; read/write)
- `0x00B83413` → RVA `0x00EFACF8` (`.data`; read/write)
- `0x00B835CB` → RVA `0x00EFAD00` (`.data`; read)
- `0x00B8361C` → RVA `0x00EFED60` (`.data`; read)
- `0x00B8366A` → RVA `0x00EFA7BC` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **13**
  - `0x00B83136` → [ExpAcquireSpinLockSharedAtDpcLevelInstrumented](../../text/27/ExpAcquireSpinLockSharedAtDpcLevelInstrumented_function_0027CD20.md) (`POOLCODE` → `.text`)
  - `0x00B831A7` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`POOLCODE` → `.text`)
  - `0x00B8338F` → [ObpPushStackInfo](../../text/21/ObpPushStackInfo_function_002109E4.md) (`POOLCODE` → `.text`)
  - `0x00B83436` → [KiLowerIrqlProcessIrqlFlags](../../text/4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (`POOLCODE` → `.text`)
  - `0x00B83471` → [ExpPoolTrackerReturnLimit](../../text/36/ExpPoolTrackerReturnLimit_function_00361570.md) (`POOLCODE` → `.text`)
  - `0x00B834CD` → [RtlpHpVsContextFree](../../text/36/RtlpHpVsContextFree_function_00361630.md) (`POOLCODE` → `.text`)
  - `0x00B83563` → [KiAcquireQueuedSpinLockInstrumented](../../text/27/KiAcquireQueuedSpinLockInstrumented_function_00275850.md) (`POOLCODE` → `.text`)
  - `0x00B835B5` → [ExpWaitForSpinLockSharedAndAcquire](../../text/36/ExpWaitForSpinLockSharedAndAcquire_function_00362380.md) (`POOLCODE` → `.text`)
  - `0x00B835C6` → [KiRaiseIrqlProcessIrqlFlags](../../text/4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (`POOLCODE` → `.text`)
  - `0x00B835DD` → [RtlpHpSegPageRangeShrink](../../text/2E/RtlpHpSegPageRangeShrink_function_002E2FA0.md) (`POOLCODE` → `.text`)
  - `0x00B835FF` → [RtlpLogHeapFailure](../../text/35/RtlpLogHeapFailure_function_0035B7BC.md) (`POOLCODE` → `.text`)
  - `0x00B8367C` → [RtlpHpEnvCompactionSchedule](../../text/32/RtlpHpEnvCompactionSchedule_function_003264A0.md) (`POOLCODE` → `.text`)
  - `0x00B8368A` → [KiRaiseIrqlProcessIrqlFlags](../../text/4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (`POOLCODE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **37**
  - `0x00B830B1` → [sub_00B82950 + 0xB9](Unknown_function_00B82950.md) (`tail-transfer`)
  - `0x00B830C1` → [sub_00B82950 + 0x2B8](Unknown_function_00B82950.md) (`tail-transfer`)
  - `0x00B8318E` → [sub_00B8371E + 0x52A](Unknown_function_00B8371E.md) (`tail-transfer`)
  - `0x00B831D1` → [sub_00B82950 + 0x5C](Unknown_function_00B82950.md) (`tail-transfer`)
  - `0x00B831DB` → [sub_00B82950 + 0x5C](Unknown_function_00B82950.md) (`tail-transfer`)
  - `0x00B831E9` → [sub_00B8371E + 0x584](Unknown_function_00B8371E.md) (`tail-transfer`)
  - `0x00B8320A` → [sub_00B8371E + 0x846](Unknown_function_00B8371E.md) (`tail-transfer`)
  - `0x00B83288` → [sub_00B8371E + 0x44A](Unknown_function_00B8371E.md) (`tail-transfer`)
  - `0x00B83295` → [sub_00B8371E + 0x44A](Unknown_function_00B8371E.md) (`tail-transfer`)
  - `0x00B83318` → [sub_00B8371E](Unknown_function_00B8371E.md) (`tail-transfer`)
  - `0x00B83356` → [sub_00B8371E + 0x20E](Unknown_function_00B8371E.md) (`tail-transfer`)
  - `0x00B833A5` → [sub_00B8371E + 0x356](Unknown_function_00B8371E.md) (`tail-transfer`)
  - `0x00B833B9` → [sub_00B82950 + 0x5C](Unknown_function_00B82950.md) (`tail-transfer`)
  - `0x00B8340D` → [sub_00B8371E + 0x333](Unknown_function_00B8371E.md) (`tail-transfer`)
  - `0x00B8344B` → [sub_00B8371E + 0x6D](Unknown_function_00B8371E.md) (`tail-transfer`)
  - `0x00B8345B` → [sub_00B82950 + 0x120](Unknown_function_00B82950.md) (`tail-transfer`)
  - `0x00B83476` → [sub_00B82950 + 0x719](Unknown_function_00B82950.md) (`tail-transfer`)
  - `0x00B834A0` → [sub_00B82950 + 0x63D](Unknown_function_00B82950.md) (`tail-transfer`)
  - `0x00B834B3` → [sub_00B82950 + 0x63D](Unknown_function_00B82950.md) (`tail-transfer`)
  - `0x00B834D4` → [sub_00B82950 + 0x724](Unknown_function_00B82950.md) (`tail-transfer`)
  - `0x00B834E8` → [sub_00B82950 + 0x724](Unknown_function_00B82950.md) (`tail-transfer`)
  - `0x00B83549` → [sub_00B82950 + 0x724](Unknown_function_00B82950.md) (`tail-transfer`)
  - `0x00B83556` → [sub_00B82950 + 0x221](Unknown_function_00B82950.md) (`tail-transfer`)
  - `0x00B83568` → [sub_00B82950 + 0x235](Unknown_function_00B82950.md) (`tail-transfer`)
  - `0x00B8357F` → [sub_00B82950 + 0x5C8](Unknown_function_00B82950.md) (`tail-transfer`)
  - `0x00B835D2` → [sub_00B82950 + 0x210](Unknown_function_00B82950.md) (`tail-transfer`)
  - `0x00B835E2` → [sub_00B82950 + 0x724](Unknown_function_00B82950.md) (`tail-transfer`)
  - `0x00B83604` → [sub_00B82950 + 0x724](Unknown_function_00B82950.md) (`tail-transfer`)
  - `0x00B83628` → [sub_00B82950 + 0x1CC](Unknown_function_00B82950.md) (`tail-transfer`)
  - `0x00B83640` → [sub_00B82950 + 0x1AB](Unknown_function_00B82950.md) (`tail-transfer`)
  - `0x00B8364A` → [sub_00B82950 + 0x1AB](Unknown_function_00B82950.md) (`tail-transfer`)
  - `0x00B83664` → [sub_00B8371E + 0x54](Unknown_function_00B8371E.md) (`tail-transfer`)
  - `0x00B83672` → [sub_00B82950 + 0x527](Unknown_function_00B82950.md) (`tail-transfer`)
  - `0x00B83681` → [sub_00B82950 + 0x527](Unknown_function_00B82950.md) (`tail-transfer`)
  - `0x00B836A0` → [sub_00B82950 + 0x6FF](Unknown_function_00B82950.md) (`tail-transfer`)
  - `0x00B836B8` → [sub_00B82950 + 0x6DE](Unknown_function_00B82950.md) (`tail-transfer`)
  - `0x00B836C2` → [sub_00B82950 + 0x6DE](Unknown_function_00B82950.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B830A9  48 83 CA 01                     or rdx, 1
00B830AD  48 89 55 97                     mov qword ptr [rbp - 0x69], rdx
00B830B1  E9 53 F9 FF FF                  jmp 0x140b82a09
00B830B6  45 8B CC                        mov r9d, r12d
00B830B9  49 8D 50 20                     lea rdx, [r8 + 0x20]
00B830BD  49 8D 40 30                     lea rax, [r8 + 0x30]
00B830C1  E9 42 FB FF FF                  jmp 0x140b82c08
00B830C6  49 8B CD                        mov rcx, r13
00B830C9  48 8D 05 30 CF 47 FF            lea rax, [rip - 0xb830d0]
00B830D0  48 C1 E9 27                     shr rcx, 0x27
00B830D4  BF 00 01 00 00                  mov edi, 0x100
00B830D9  81 E1 FF 01 00 00               and ecx, 0x1ff
00B830DF  BE 40 00 00 00                  mov esi, 0x40
00B830E4  81 C1 00 FF FF FF               add ecx, 0xffffff00
00B830EA  0F B6 84 01 A8 8A E3 00         movzx eax, byte ptr [rcx + rax + 0xe38aa8]
00B830F2  3C 04                           cmp al, 4
00B830F4  74 05                           je 0x140b830fb
00B830F6  3C 05                           cmp al, 5
00B830F8  0F 44 F7                        cmove esi, edi
00B830FB  45 0F 20 C6                     mov r14, cr8
00B830FF  44 0F 22 C2                     mov cr8, rdx
00B83103  44 39 25 16 3C 44 00            cmp dword ptr [rip + 0x443c16], r12d
00B8310A  0F 85 76 05 00 00               jne 0x140b83686
00B83110  F6 05 EF 39 44 00 21            test byte ptr [rip + 0x4439ef], 0x21
00B83117  0F 84 67 04 00 00               je 0x140b83584
00B8311D  8B 05 35 AD 38 00               mov eax, dword ptr [rip + 0x38ad35]
00B83123  85 C0                           test eax, eax
00B83125  0F 85 59 04 00 00               jne 0x140b83584
00B8312B  41 0F B6 D6                     movzx edx, r14b
00B8312F  48 8D 0D C2 7B 37 00            lea rcx, [rip + 0x377bc2]
00B83136  E8 E5 9B 6F FF                  call 0x14027cd20
00B8313B  4C 8B 05 F6 BB 37 00            mov r8, qword ptr [rip + 0x37bbf6]
00B83142  49 8B C5                        mov rax, r13
00B83145  4C 8B 0D E4 BB 37 00            mov r9, qword ptr [rip + 0x37bbe4]
00B8314C  41 BA 01 00 00 00               mov r10d, 1
00B83152  48 C1 E8 0C                     shr rax, 0xc
00B83156  48 69 C8 5F 9E 00 00            imul rcx, rax, 0x9e5f
00B8315D  41 8D 50 FF                     lea edx, [r8 - 1]
00B83161  48 8B C1                        mov rax, rcx
00B83164  48 C1 E8 20                     shr rax, 0x20
00B83168  48 33 C8                        xor rcx, rax
00B8316B  23 D1                           and edx, ecx
00B8316D  8B CA                           mov ecx, edx
00B8316F  48 C1 E1 05                     shl rcx, 5
00B83173  49 03 C9                        add rcx, r9
00B83176  48 8B 01                        mov rax, qword ptr [rcx]
00B83179  49 3B C5                        cmp rax, r13
00B8317C  0F 84 3C 02 00 00               je 0x140b833be
00B83182  FF C2                           inc edx
00B83184  8B C2                           mov eax, edx
00B83186  49 3B C0                        cmp rax, r8
00B83189  72 E2                           jb 0x140b8316d
00B8318B  45 85 D2                        test r10d, r10d
00B8318E  0F 85 B4 0A 00 00               jne 0x140b83c48
00B83194  BA 22 00 00 00                  mov edx, 0x22
00B83199  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00B8319E  4C 8B CE                        mov r9, rsi
00B831A1  4D 8B C5                        mov r8, r13
00B831A4  8D 4A F7                        lea ecx, [rdx - 9]
00B831A7  E8 B4 A4 97 FF                  call 0x1404fd660
00B831AC  CC                              int3
00B831AD  49 8B CE                        mov rcx, r14
00B831B0  A8 04                           test al, 4
00B831B2  74 12                           je 0x140b831c6
00B831B4  41 0F B7 06                     movzx eax, word ptr [r14]
00B831B8  66 41 23 C0                     and ax, r8w
00B831BC  0F B7 C0                        movzx eax, ax
00B831BF  48 C1 E0 04                     shl rax, 4
00B831C3  48 2B C8                        sub rcx, rax
00B831C6  48 33 49 08                     xor rcx, qword ptr [rcx + 8]
00B831CA  48 33 0D 57 40 44 00            xor rcx, qword ptr [rip + 0x444057]
00B831D1  0F 84 D5 F7 FF FF               je 0x140b829ac
00B831D7  48 83 F9 FF                     cmp rcx, -1
00B831DB  0F 84 CB F7 FF FF               je 0x140b829ac
00B831E1  8B 05 39 BB 37 00               mov eax, dword ptr [rip + 0x37bb39]
00B831E7  85 C0                           test eax, eax
00B831E9  0F 85 B3 0A 00 00               jne 0x140b83ca2
00B831EF  49 8B C5                        mov rax, r13
00B831F2  48 C1 E8 27                     shr rax, 0x27
00B831F6  25 FF 01 00 00                  and eax, 0x1ff
00B831FB  05 00 FF FF FF                  add eax, 0xffffff00
00B83200  0F B6 84 18 A8 8A E3 00         movzx eax, byte ptr [rax + rbx + 0xe38aa8]
00B83208  3C 05                           cmp al, 5
00B8320A  0F 84 54 0D 00 00               je 0x140b83f64
00B83210  BE 40 00 00 00                  mov esi, 0x40
00B83215  41 F6 46 03 04                  test byte ptr [r14 + 3], 4
00B8321A  49 8B D6                        mov rdx, r14
00B8321D  74 15                           je 0x140b83234
00B8321F  41 0F B7 06                     movzx eax, word ptr [r14]
00B83223  66 41 23 C0                     and ax, r8w
00B83227  0F B7 C8                        movzx ecx, ax
00B8322A  48 F7 D9                        neg rcx
00B8322D  48 C1 E1 04                     shl rcx, 4
00B83231  48 03 D1                        add rdx, rcx
00B83234  0F B7 42 02                     movzx eax, word ptr [rdx + 2]
00B83238  44 8B 72 04                     mov r14d, dword ptr [rdx + 4]
00B8323C  0F B6 D8                        movzx ebx, al
00B8323F  48 C1 E3 04                     shl rbx, 4
00B83243  66 C1 E8 08                     shr ax, 8
00B83247  A8 08                           test al, 8
00B83249  0F 84 61 01 00 00               je 0x140b833b0
00B8324F  48 8B FA                        mov rdi, rdx
00B83252  48 8B C2                        mov rax, rdx
00B83255  48 33 7A 08                     xor rdi, qword ptr [rdx + 8]
00B83259  48 33 05 C8 3F 44 00            xor rax, qword ptr [rip + 0x443fc8]
00B83260  48 89 42 08                     mov qword ptr [rdx + 8], rax
00B83264  48 33 3D BD 3F 44 00            xor rdi, qword ptr [rip + 0x443fbd]
00B8326B  0F 84 3A 01 00 00               je 0x140b833ab
00B83271  48 83 FF FF                     cmp rdi, -1
00B83275  0F 84 30 01 00 00               je 0x140b833ab
00B8327B  48 B8 00 00 00 00 00 80 FF FF   movabs rax, 0xffff800000000000
00B83285  48 3B F8                        cmp rdi, rax
00B83288  0F 82 DA 08 00 00               jb 0x140b83b68
00B8328E  0F B6 07                        movzx eax, byte ptr [rdi]
00B83291  24 7F                           and al, 0x7f
00B83293  3C 03                           cmp al, 3
00B83295  0F 85 CD 08 00 00               jne 0x140b83b68
00B8329B  81 E6 00 01 00 00               and esi, 0x100
00B832A1  48 3B 3D 08 38 44 00            cmp rdi, qword ptr [rip + 0x443808]
00B832A8  0F 84 CB 00 00 00               je 0x140b83379
00B832AE  48 8B 8F F8 02 00 00            mov rcx, qword ptr [rdi + 0x2f8]
00B832B5  48 8D 15 44 CD 47 FF            lea rdx, [rip - 0xb832bc]
00B832BC  41 8B C4                        mov eax, r12d
00B832BF  48 89 4D 97                     mov qword ptr [rbp - 0x69], rcx
00B832C3  48 85 F6                        test rsi, rsi
00B832C6  0F 95 C0                        setne al
00B832C9  44 8B F8                        mov r15d, eax
00B832CC  8B C0                           mov eax, eax
00B832CE  48 C1 E0 07                     shl rax, 7
00B832D2  48 89 45 BF                     mov qword ptr [rbp - 0x41], rax
00B832D6  46 0F B6 AC FA 50 73 FC 00      movzx r13d, byte ptr [rdx + r15*8 + 0xfc7350]
00B832DF  4C 8D 24 08                     lea r12, [rax + rcx]
00B832E3  41 0F 0D 0C 24                  prefetchw byte ptr [r12]
00B832E8  49 8B 34 24                     mov rsi, qword ptr [r12]
00B832EC  49 8B 44 24 40                  mov rax, qword ptr [r12 + 0x40]
00B832F1  49 83 7C 24 50 00               cmp qword ptr [r12 + 0x50], 0
00B832F7  74 25                           je 0x140b8331e
00B832F9  49 6B CF 38                     imul rcx, r15, 0x38
00B832FD  48 3B C6                        cmp rax, rsi
00B83300  76 1C                           jbe 0x140b8331e
00B83302  4C 8D 82 48 66 F0 00            lea r8, [rdx + 0xf06648]
00B83309  4C 03 C1                        add r8, rcx
00B8330C  48 8B C8                        mov rcx, rax
00B8330F  48 2B CE                        sub rcx, rsi
00B83312  49 8B 10                        mov rdx, qword ptr [r8]
00B83315  48 3B CA                        cmp rcx, rdx
00B83318  0F 87 00 04 00 00               ja 0x140b8371e
00B8331E  4C 8B 5D BF                     mov r11, qword ptr [rbp - 0x41]
00B83322  4C 8D 15 57 4C 2A 00            lea r10, [rip + 0x2a4c57]
00B83329  4C 8B C3                        mov r8, rbx
00B8332C  48 3B DE                        cmp rbx, rsi
00B8332F  4C 8B CE                        mov r9, rsi
00B83332  48 8B CE                        mov rcx, rsi
00B83335  48 8B C6                        mov rax, rsi
00B83338  4C 0F 42 CB                     cmovb r9, rbx
00B8333C  48 2B CB                        sub rcx, rbx
00B8333F  33 D2                           xor edx, edx
00B83341  48 3B DE                        cmp rbx, rsi
00B83344  48 0F 42 D1                     cmovb rdx, rcx
00B83348  F0 49 0F B1 14 24               lock cmpxchg qword ptr [r12], rdx
00B8334E  48 8B F0                        mov rsi, rax
00B83351  75 D9                           jne 0x140b8332c
00B83353  49 2B D9                        sub rbx, r9
00B83356  0F 85 D0 05 00 00               jne 0x140b8392c
00B8335C  41 F6 C5 04                     test r13b, 4
00B83360  74 0C                           je 0x140b8336e
00B83362  49 F7 D8                        neg r8
00B83365  F0 4E 01 84 FF 00 02 00 00      lock add qword ptr [rdi + r15*8 + 0x200], r8
00B8336E  4C 8B 6D 67                     mov r13, qword ptr [rbp + 0x67]
00B83372  45 33 E4                        xor r12d, r12d
00B83375  4C 8B 7D 77                     mov r15, qword ptr [rbp + 0x77]
00B83379  83 3D 90 1C 44 00 00            cmp dword ptr [rip + 0x441c90], 0
00B83380  74 12                           je 0x140b83394
00B83382  33 D2                           xor edx, edx
00B83384  48 8D 4F D0                     lea rcx, [rdi - 0x30]
00B83388  45 8B CE                        mov r9d, r14d
00B8338B  44 8D 42 01                     lea r8d, [rdx + 1]
00B8338F  E8 50 D6 68 FF                  call 0x1402109e4
00B83394  48 C7 C6 FF FF FF FF            mov rsi, 0xffffffffffffffff
00B8339B  F0 48 0F C1 77 D0               lock xadd qword ptr [rdi - 0x30], rsi
00B833A1  48 83 EE 01                     sub rsi, 1
00B833A5  0F 8E C9 06 00 00               jle 0x140b83a74
00B833AB  BF 80 00 00 00                  mov edi, 0x80
00B833B0  BA 00 01 00 00                  mov edx, 0x100
00B833B5  4D 8D 75 F0                     lea r14, [r13 - 0x10]
00B833B9  E9 EE F5 FF FF                  jmp 0x140b829ac
00B833BE  48 85 C9                        test rcx, rcx
00B833C1  0F 84 CD FD FF FF               je 0x140b83194
00B833C7  8B 41 0C                        mov eax, dword ptr [rcx + 0xc]
00B833CA  48 C7 C6 FF FF FF FF            mov rsi, 0xffffffffffffffff
00B833D1  8B 59 08                        mov ebx, dword ptr [rcx + 8]
00B833D4  8B D0                           mov edx, eax
00B833D6  48 C1 EA 08                     shr rdx, 8
00B833DA  81 E2 FF 0F 00 00               and edx, 0xfff
00B833E0  48 89 55 97                     mov qword ptr [rbp - 0x69], rdx
00B833E4  48 8B 51 10                     mov rdx, qword ptr [rcx + 0x10]
00B833E8  48 89 55 9F                     mov qword ptr [rbp - 0x61], rdx
00B833EC  85 C7                           test edi, eax
00B833EE  0F 85 15 02 00 00               jne 0x140b83609
00B833F4  48 8B FE                        mov rdi, rsi
00B833F7  F0 FF 0D 02 BD 44 00            lock dec dword ptr [rip + 0x44bd02]
00B833FE  4C 89 61 18                     mov qword ptr [rcx + 0x18], r12
00B83402  F0 48 FF 01                     lock inc qword ptr [rcx]
00B83406  F6 05 F9 36 44 00 01            test byte ptr [rip + 0x4436f9], 1
00B8340D  0F 85 3E 06 00 00               jne 0x140b83a51
00B83413  F0 81 25 DA 78 37 00 FF FF FF BF  lock and dword ptr [rip + 0x3778da], 0xbfffffff
00B8341E  F0 FF 0D D3 78 37 00            lock dec dword ptr [rip + 0x3778d3]
00B83425  44 39 25 F4 38 44 00            cmp dword ptr [rip + 0x4438f4], r12d
00B8342C  74 0D                           je 0x140b8343b
00B8342E  44 0F 20 C1                     mov rcx, cr8
00B83432  41 0F B6 D6                     movzx edx, r14b
00B83436  E8 5D 22 97 FF                  call 0x1404f5698
00B8343B  41 0F B6 C6                     movzx eax, r14b
00B8343F  44 0F 22 C0                     mov cr8, rax
00B83443  48 8D 47 FF                     lea rax, [rdi - 1]
00B83447  48 83 F8 FD                     cmp rax, -3
00B8344B  0F 86 3A 03 00 00               jbe 0x140b8378b
00B83451  48 8B 55 9F                     mov rdx, qword ptr [rbp - 0x61]
00B83455  4D 8B F5                        mov r14, r13
00B83458  49 8B FD                        mov rdi, r13
00B8345B  E9 10 F6 FF FF                  jmp 0x140b82a70
00B83460  48 C1 EF 08                     shr rdi, 8
00B83464  4D 8B C1                        mov r8, r9
00B83467  F7 D7                           not edi
00B83469  49 8B D6                        mov rdx, r14
00B8346C  83 E7 01                        and edi, 1
00B8346F  8B CF                           mov ecx, edi
00B83471  E8 FA E0 7D FF                  call 0x140361570
00B83476  E9 EE FB FF FF                  jmp 0x140b83069
00B8347B  49 8B C0                        mov rax, r8
00B8347E  44 89 65 B3                     mov dword ptr [rbp - 0x4d], r12d
00B83482  49 23 C1                        and rax, r9
00B83485  49 8B D0                        mov rdx, r8
00B83488  48 2B D0                        sub rdx, rax
00B8348B  41 8B CA                        mov ecx, r10d
00B8348E  48 C1 FA 05                     sar rdx, 5
00B83492  48 D3 E2                        shl rdx, cl
00B83495  48 03 D0                        add rdx, rax
00B83498  41 0F B6 C3                     movzx eax, r11b
00B8349C  24 03                           and al, 3
00B8349E  3C 03                           cmp al, 3
00B834A0  0F 85 E7 FA FF FF               jne 0x140b82f8d
00B834A6  4C 3B F2                        cmp r14, rdx
00B834A9  0F 84 28 01 00 00               je 0x140b835d7
00B834AF  41 80 FB 0F                     cmp r11b, 0xf
00B834B3  0F 85 D4 FA FF FF               jne 0x140b82f8d
00B834B9  4C 3B F2                        cmp r14, rdx
00B834BC  0F 86 15 01 00 00               jbe 0x140b835d7
00B834C2  48 8B 4B 20                     mov rcx, qword ptr [rbx + 0x20]
00B834C6  4C 8D 4D B3                     lea r9, [rbp - 0x4d]
00B834CA  4D 8B C6                        mov r8, r14
00B834CD  E8 5E E1 7D FF                  call 0x140361630
00B834D2  85 C0                           test eax, eax
00B834D4  0F 84 9A FB FF FF               je 0x140b83074
00B834DA  4C 8B 43 18                     mov r8, qword ptr [rbx + 0x18]
00B834DE  8B 4D B3                        mov ecx, dword ptr [rbp - 0x4d]
00B834E1  41 0F B7 40 44                  movzx eax, word ptr [r8 + 0x44]
00B834E6  3B C8                           cmp ecx, eax
00B834E8  0F 83 86 FB FF FF               jae 0x140b83074
00B834EE  83 C1 0F                        add ecx, 0xf
00B834F1  48 C1 E9 04                     shr rcx, 4
00B834F5  44 0F B6 94 31 80 0B 01 00      movzx r10d, byte ptr [rcx + rsi + 0x10b80]
00B834FE  41 FF CA                        dec r10d
00B83501  4F 8D 0C D0                     lea r9, [r8 + r10*8]
00B83505  49 8B 89 C0 01 00 00            mov rcx, qword ptr [r9 + 0x1c0]
00B8350C  48 8B C1                        mov rax, rcx
00B8350F  48 89 4D 97                     mov qword ptr [rbp - 0x69], rcx
00B83513  48 C1 E8 10                     shr rax, 0x10
00B83517  48 8B D1                        mov rdx, rcx
00B8351A  F6 C1 01                        test cl, 1
00B8351D  74 22                           je 0x140b83541
00B8351F  66 83 F8 01                     cmp ax, 1
00B83523  76 0B                           jbe 0x140b83530
00B83525  66 FF C8                        dec ax
00B83528  66 89 45 99                     mov word ptr [rbp - 0x67], ax
00B8352C  48 8B 55 97                     mov rdx, qword ptr [rbp - 0x69]
00B83530  48 8B C1                        mov rax, rcx
00B83533  F0 49 0F B1 91 C0 01 00 00      lock cmpxchg qword ptr [r9 + 0x1c0], rdx
00B8353C  48 3B C1                        cmp rax, rcx
00B8353F  75 C4                           jne 0x140b83505
00B83541  4B 8B 8C D0 C0 01 00 00         mov rcx, qword ptr [r8 + r10*8 + 0x1c0]
00B83549  E9 26 FB FF FF                  jmp 0x140b83074
00B8354E  8B 05 04 A9 38 00               mov eax, dword ptr [rip + 0x38a904]
00B83554  85 C0                           test eax, eax
00B83556  0F 85 15 F6 FF FF               jne 0x140b82b71
00B8355C  48 8B D1                        mov rdx, rcx
00B8355F  48 8D 4D C7                     lea rcx, [rbp - 0x39]
00B83563  E8 E8 22 6F FF                  call 0x140275850
00B83568  E9 18 F6 FF FF                  jmp 0x140b82b85
00B8356D  41 B9 01 00 00 00               mov r9d, 1
00B83573  49 8D 50 08                     lea rdx, [r8 + 8]
00B83577  49 8D 40 18                     lea rax, [r8 + 0x18]
00B8357B  45 8D 51 17                     lea r10d, [r9 + 0x17]
00B8357F  E9 94 F9 FF FF                  jmp 0x140b82f18
00B83584  0F 0D 0D 6D 77 37 00            prefetchw byte ptr [rip + 0x37776d]
00B8358B  8B 05 67 77 37 00               mov eax, dword ptr [rip + 0x377767]
00B83591  0F BA F0 1F                     btr eax, 0x1f
00B83595  8D 48 01                        lea ecx, [rax + 1]
00B83598  F0 0F B1 0D 58 77 37 00         lock cmpxchg dword ptr [rip + 0x377758], ecx
00B835A0  0F 84 95 FB FF FF               je 0x140b8313b
00B835A6  85 C0                           test eax, eax
00B835A8  79 EB                           jns 0x140b83595
00B835AA  41 0F B6 D6                     movzx edx, r14b
00B835AE  48 8D 0D 43 77 37 00            lea rcx, [rip + 0x377743]
00B835B5  E8 C6 ED 7D FF                  call 0x140362380
00B835BA  E9 7C FB FF FF                  jmp 0x140b8313b
00B835BF  0F B6 D0                        movzx edx, al
00B835C2  40 0F B6 CF                     movzx ecx, dil
00B835C6  E8 31 21 97 FF                  call 0x1404f56fc
00B835CB  48 8D 0D 2E 77 37 00            lea rcx, [rip + 0x37772e]
00B835D2  E9 89 F5 FF FF                  jmp 0x140b82b60
00B835D7  49 8B D0                        mov rdx, r8
00B835DA  48 8B CB                        mov rcx, rbx
00B835DD  E8 BE F9 75 FF                  call 0x1402e2fa0
00B835E2  E9 8D FA FF FF                  jmp 0x140b83074
00B835E7  48 8B 16                        mov rdx, qword ptr [rsi]
00B835EA  4D 8B C6                        mov r8, r14
00B835ED  4C 89 64 24 28                  mov qword ptr [rsp + 0x28], r12
00B835F2  B9 11 00 00 00                  mov ecx, 0x11
00B835F7  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
00B835FC  4C 8B CF                        mov r9, rdi
00B835FF  E8 B8 81 7D FF                  call 0x14035b7bc
00B83604  E9 6B FA FF FF                  jmp 0x140b83074
00B83609  48 8B 79 18                     mov rdi, qword ptr [rcx + 0x18]
00B8360D  48 33 3D 14 3C 44 00            xor rdi, qword ptr [rip + 0x443c14]
00B83614  49 33 FD                        xor rdi, r13
00B83617  E9 DB FD FF FF                  jmp 0x140b833f7
00B8361C  48 8B 05 3D B7 37 00            mov rax, qword ptr [rip + 0x37b73d]
00B83623  8B 04 C8                        mov eax, dword ptr [rax + rcx*8]
00B83626  85 C0                           test eax, eax
00B83628  0F 84 EE F4 FF FF               je 0x140b82b1c
00B8362E  41 89 00                        mov dword ptr [r8], eax
00B83631  48 8B 05 28 B7 37 00            mov rax, qword ptr [rip + 0x37b728]
00B83638  48 8B 44 C8 48                  mov rax, qword ptr [rax + rcx*8 + 0x48]
00B8363D  48 85 C0                        test rax, rax
00B83640  0F 84 B5 F4 FF FF               je 0x140b82afb
00B83646  49 89 40 48                     mov qword ptr [r8 + 0x48], rax
00B8364A  E9 AC F4 FF FF                  jmp 0x140b82afb
00B8364F  C6 44 32 5C 01                  mov byte ptr [rdx + rsi + 0x5c], 1
00B83654  48 8B 0E                        mov rcx, qword ptr [rsi]
00B83657  48 8B 41 38                     mov rax, qword ptr [rcx + 0x38]
00B8365B  48 8B 00                        mov rax, qword ptr [rax]
00B8365E  48 C1 E8 08                     shr rax, 8
00B83662  3C 01                           cmp al, 1
00B83664  0F 85 08 01 00 00               jne 0x140b83772
00B8366A  8B 05 4C 71 37 00               mov eax, dword ptr [rip + 0x37714c]
00B83670  85 C0                           test eax, eax
00B83672  0F 85 FF F7 FF FF               jne 0x140b82e77
00B83678  48 8B 49 38                     mov rcx, qword ptr [rcx + 0x38]
00B8367C  E8 1F 2E 7A FF                  call 0x1403264a0
00B83681  E9 F1 F7 FF FF                  jmp 0x140b82e77
00B83686  41 0F B6 CE                     movzx ecx, r14b
00B8368A  E8 6D 20 97 FF                  call 0x1404f56fc
00B8368F  E9 7C FA FF FF                  jmp 0x140b83110
00B83694  48 8B 05 C5 B6 37 00            mov rax, qword ptr [rip + 0x37b6c5]
00B8369B  8B 04 C8                        mov eax, dword ptr [rax + rcx*8]
00B8369E  85 C0                           test eax, eax
00B836A0  0F 84 A9 F9 FF FF               je 0x140b8304f
00B836A6  41 89 01                        mov dword ptr [r9], eax
00B836A9  48 8B 05 B0 B6 37 00            mov rax, qword ptr [rip + 0x37b6b0]
00B836B0  48 8B 44 C8 48                  mov rax, qword ptr [rax + rcx*8 + 0x48]
00B836B5  48 85 C0                        test rax, rax
00B836B8  0F 84 70 F9 FF FF               je 0x140b8302e
00B836BE  49 89 41 48                     mov qword ptr [r9 + 0x48], rax
00B836C2  E9 67 F9 FF FF                  jmp 0x140b8302e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00B830A9(__int64 a1, __int64 a2, __int64 a3)
{
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;

    a2 = (a2) | (1);
    *(unsigned __int64 *)(v_rbp - 105) = a2;
}
```

## 5. (Beta) C Style

```c
int64_t sub_00B830A9(int64_t Arg1, int64_t Arg2, int64_t Arg3)
{
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;

    Arg2 = (Arg2) | (1);
    *(uint64_t *)(local_rbp - 0x69) = Arg2;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=poolcode&rva=0x00B830A9&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
