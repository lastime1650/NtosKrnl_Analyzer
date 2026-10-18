# sub_0020D8DF

- RVA: `0x0020D8DF`–`0x0020DE87` (길이 `1,448` bytes)
- VA: `0x000000014020D8DF`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D9B0`
- 디코드: `338`개 명령, `1,448/1,448` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **29**; 고유 호출 대상: **15**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0020D8E6` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0020D960` → [KiWaitSatisfyOther](../41/KiWaitSatisfyOther_function_0041C870.md) (function, `0x0041C870`)
- `0x0020D984` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0020D994` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0020D9B0` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0020D9E5` → [KiWaitSatisfyMutant](../3C/KiWaitSatisfyMutant_function_003C6490.md) (function, `0x003C6490`)
- `0x0020DA39` → [KiSatisfyThreadWait](../35/KiSatisfyThreadWait_function_00352B40.md) (function, `0x00352B40`)
- `0x0020DA43` → [RtlRaiseStatus](../2F/RtlRaiseStatus_function_002F6A50.md) (function, `0x002F6A50`)
- `0x0020DA57` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0020DA66` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0020DA7E` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0020DA8E` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0020DAA6` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0020DAB6` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0020DAD5` → [KiProcessDeferredReadyList](../25/KiProcessDeferredReadyList_function_00250800.md) (function, `0x00250800`)
- `0x0020DAEF` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0020DAFE` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0020DB3A` → [KeAbPreAcquire](../21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0020DB4E` → [KeAbPreWait](KeAbPreWait_function_0020E560.md) (function, `0x0020E560`)
- `0x0020DBF0` → [KeAbPreAcquire](../21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0020DC03` → [_report_rangecheckfailure](../4F/_report_rangecheckfailure_function_004F5FDC.md) (function, `0x004F5FDC`)
- `0x0020DC09` → [KeDisableInterrupts](../21/KeDisableInterrupts_function_00217BE0.md) (function, `0x00217BE0`)
- `0x0020DC76` → [KeDisableInterrupts](../21/KeDisableInterrupts_function_00217BE0.md) (function, `0x00217BE0`)
- `0x0020DD28` → [KeDisableInterrupts](../21/KeDisableInterrupts_function_00217BE0.md) (function, `0x00217BE0`)
- `0x0020DD77` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x0020DDB9` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x0020DDDE` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x0020DE41` → [KiSrcuReportQuiescent](../5C/KiSrcuReportQuiescent_function_005C2C08.md) (function, `0x005C2C08`)
- `0x0020DE52` → [KiSrcuFlushCompleted](../5C/KiSrcuFlushCompleted_function_005C22B4.md) (function, `0x005C22B4`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0020D8FD` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x0020D976` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x0020DE74` → RVA `0x00F210E8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **25**
  - `0x0020D8EB` → [sub_0020D5AD + 0x25C](Unknown_function_0020D5AD.md) (`tail-transfer`)
  - `0x0020D8F9` → [sub_0020D5AD + 0x2E0](Unknown_function_0020D5AD.md) (`tail-transfer`)
  - `0x0020D971` → [sub_0020D5AD + 0x2FD](Unknown_function_0020D5AD.md) (`tail-transfer`)
  - `0x0020D97E` → [sub_0020D1EC + 0x2F4](Unknown_function_0020D1EC.md) (`tail-transfer`)
  - `0x0020D98B` → [sub_0020D1EC + 0x2F4](Unknown_function_0020D1EC.md) (`tail-transfer`)
  - `0x0020D999` → [sub_0020D1EC + 0x2F6](Unknown_function_0020D1EC.md) (`tail-transfer`)
  - `0x0020D9A8` → [sub_0020D1EC + 0x1CD](Unknown_function_0020D1EC.md) (`tail-transfer`)
  - `0x0020D9B5` → [sub_0020D5AD + 0xE0](Unknown_function_0020D5AD.md) (`tail-transfer`)
  - `0x0020D9F1` → [sub_0020D5AD + 0x2FD](Unknown_function_0020D5AD.md) (`tail-transfer`)
  - `0x0020DAA0` → [sub_0020D5AD + 0x80](Unknown_function_0020D5AD.md) (`tail-transfer`)
  - `0x0020DAAD` → [sub_0020D5AD + 0x80](Unknown_function_0020D5AD.md) (`tail-transfer`)
  - `0x0020DABB` → [sub_0020D5AD + 0x82](Unknown_function_0020D5AD.md) (`tail-transfer`)
  - `0x0020DADC` → [sub_0020D5AD + 0x315](Unknown_function_0020D5AD.md) (`tail-transfer`)
  - `0x0020DB11` → [sub_0020D1EC + 0x1CD](Unknown_function_0020D1EC.md) (`tail-transfer`)
  - `0x0020DB7C` → [sub_0020D5AD + 0x167](Unknown_function_0020D5AD.md) (`tail-transfer`)
  - `0x0020DC9B` → [sub_0020D1EC + 0x27D](Unknown_function_0020D1EC.md) (`tail-transfer`)
  - `0x0020DCBE` → [sub_0020D1EC + 0x7C](Unknown_function_0020D1EC.md) (`tail-transfer`)
  - `0x0020DCD5` → [sub_0020D1EC + 0x27D](Unknown_function_0020D1EC.md) (`tail-transfer`)
  - `0x0020DCDE` → [sub_0020D1EC + 0x27D](Unknown_function_0020D1EC.md) (`tail-transfer`)
  - `0x0020DD16` → [sub_0020D5AD + 0x1A8](Unknown_function_0020D5AD.md) (`tail-transfer`)
  - `0x0020DD22` → [sub_0020D1EC + 0x89](Unknown_function_0020D1EC.md) (`tail-transfer`)
  - `0x0020DD3C` → [sub_0020D1EC + 0x89](Unknown_function_0020D1EC.md) (`tail-transfer`)
  - `0x0020DD58` → [sub_0020D1EC + 0x89](Unknown_function_0020D1EC.md) (`tail-transfer`)
  - `0x0020DD9A` → [sub_0020D1EC + 0x7C](Unknown_function_0020D1EC.md) (`tail-transfer`)
  - `0x0020DE0D` → [sub_006D670A](../6D/Unknown_function_006D670A.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0020D8DF  0F B6 D0                        movzx edx, al
0020D8E2  40 0F B6 CE                     movzx ecx, sil
0020D8E6  E8 11 7E 2E 00                  call 0x1404f56fc
0020D8EB  E9 19 FF FF FF                  jmp 0x14020d809
0020D8F0  8B F5                           mov esi, ebp
0020D8F2  F0 48 0F BA 6F 40 00            lock bts qword ptr [rdi + 0x40], 0
0020D8F9  73 92                           jae 0x14020d88d
0020D8FB  FF C6                           inc esi
0020D8FD  85 35 A9 79 DB 00               test dword ptr [rip + 0xdb79a9], esi
0020D903  0F 84 40 01 00 00               je 0x14020da49
0020D909  F3 90                           pause
0020D90B  48 8B 47 40                     mov rax, qword ptr [rdi + 0x40]
0020D90F  48 85 C0                        test rax, rax
0020D912  74 DE                           je 0x14020d8f2
0020D914  EB E5                           jmp 0x14020d8fb
0020D916  44 8B F5                        mov r14d, ebp
0020D919  0F 1F 80 00 00 00 00            nop dword ptr [rax]
0020D920  F0 48 0F BA 6F 40 00            lock bts qword ptr [rdi + 0x40], 0
0020D927  73 1D                           jae 0x14020d946
0020D929  41 FF C6                        inc r14d
0020D92C  44 85 35 79 79 DB 00            test dword ptr [rip + 0xdb7979], r14d
0020D933  0F 84 37 01 00 00               je 0x14020da70
0020D939  F3 90                           pause
0020D93B  48 8B 47 40                     mov rax, qword ptr [rdi + 0x40]
0020D93F  48 85 C0                        test rax, rax
0020D942  74 DC                           je 0x14020d920
0020D944  EB E3                           jmp 0x14020d929
0020D946  F6 47 70 07                     test byte ptr [rdi + 0x70], 7
0020D94A  75 19                           jne 0x14020d965
0020D94C  41 8B C7                        mov eax, r15d
0020D94F  48 8B CE                        mov rcx, rsi
0020D952  48 89 87 C8 00 00 00            mov qword ptr [rdi + 0xc8], rax
0020D959  48 89 AF D0 03 00 00            mov qword ptr [rdi + 0x3d0], rbp
0020D960  E8 0B EF 20 00                  call 0x14041c870
0020D965  4C 8B 54 24 48                  mov r10, qword ptr [rsp + 0x48]
0020D96A  F0 81 26 7F FF FF FF            lock and dword ptr [rsi], 0xffffff7f
0020D971  E9 34 FF FF FF                  jmp 0x14020d8aa
0020D976  8B 05 3C 91 DB 00               mov eax, dword ptr [rip + 0xdb913c]
0020D97C  A8 40                           test al, 0x40
0020D97E  0F 84 5C FB FF FF               je 0x14020d4e0
0020D984  E8 07 1B 10 00                  call 0x14030f490
0020D989  84 C0                           test al, al
0020D98B  0F 84 4F FB FF FF               je 0x14020d4e0
0020D991  41 8B CC                        mov ecx, r12d
0020D994  E8 C7 1A 10 00                  call 0x14030f460
0020D999  E9 44 FB FF FF                  jmp 0x14020d4e2
0020D99E  41 88 6C 3C 72                  mov byte ptr [r12 + rdi + 0x72], bpl
0020D9A3  BE 01 01 00 00                  mov esi, 0x101
0020D9A8  E9 0C FA FF FF                  jmp 0x14020d3b9
0020D9AD  0F B6 D3                        movzx edx, bl
0020D9B0  E8 47 7D 2E 00                  call 0x1404f56fc
0020D9B5  E9 D3 FC FF FF                  jmp 0x14020d68d
0020D9BA  F6 47 70 07                     test byte ptr [rdi + 0x70], 7
0020D9BE  4C 8B 54 24 48                  mov r10, qword ptr [rsp + 0x48]
0020D9C3  75 A5                           jne 0x14020d96a
0020D9C5  41 8B C7                        mov eax, r15d
0020D9C8  48 89 87 C8 00 00 00            mov qword ptr [rdi + 0xc8], rax
0020D9CF  48 89 AF D0 03 00 00            mov qword ptr [rdi + 0x3d0], rbp
0020D9D6  83 6E 04 01                     sub dword ptr [rsi + 4], 1
0020D9DA  75 8E                           jne 0x14020d96a
0020D9DC  4D 8B C2                        mov r8, r10
0020D9DF  48 8B D7                        mov rdx, rdi
0020D9E2  48 8B CE                        mov rcx, rsi
0020D9E5  E8 A6 8A 1B 00                  call 0x1403c6490
0020D9EA  F0 81 26 7F FF FF FF            lock and dword ptr [rsi], 0xffffff7f
0020D9F1  E9 B4 FE FF FF                  jmp 0x14020d8aa
0020D9F6  F0 81 26 7F FF FF FF            lock and dword ptr [rsi], 0xffffff7f
0020D9FD  0F 1F 00                        nop dword ptr [rax]
0020DA00  F0 48 0F BA 6F 40 00            lock bts qword ptr [rdi + 0x40], 0
0020DA07  73 1B                           jae 0x14020da24
0020DA09  FF C5                           inc ebp
0020DA0B  85 2D 9B 78 DB 00               test dword ptr [rip + 0xdb789b], ebp
0020DA11  0F 84 CA 00 00 00               je 0x14020dae1
0020DA17  F3 90                           pause
0020DA19  48 8B 47 40                     mov rax, qword ptr [rdi + 0x40]
0020DA1D  48 85 C0                        test rax, rax
0020DA20  74 DE                           je 0x14020da00
0020DA22  EB E5                           jmp 0x14020da09
0020DA24  4C 8B 4C 24 70                  mov r9, qword ptr [rsp + 0x70]
0020DA29  44 8B C3                        mov r8d, ebx
0020DA2C  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
0020DA31  48 8B D7                        mov rdx, rdi
0020DA34  44 89 7C 24 20                  mov dword ptr [rsp + 0x20], r15d
0020DA39  E8 02 51 14 00                  call 0x140352b40
0020DA3E  B9 91 01 00 C0                  mov ecx, 0xc0000191
0020DA43  E8 08 90 0E 00                  call 0x1402f6a50
0020DA48  CC                              int3
0020DA49  8B 05 69 90 DB 00               mov eax, dword ptr [rip + 0xdb9069]
0020DA4F  A8 40                           test al, 0x40
0020DA51  0F 84 B2 FE FF FF               je 0x14020d909
0020DA57  E8 34 1A 10 00                  call 0x14030f490
0020DA5C  84 C0                           test al, al
0020DA5E  0F 84 A5 FE FF FF               je 0x14020d909
0020DA64  8B CE                           mov ecx, esi
0020DA66  E8 F5 19 10 00                  call 0x14030f460
0020DA6B  E9 9B FE FF FF                  jmp 0x14020d90b
0020DA70  8B 05 42 90 DB 00               mov eax, dword ptr [rip + 0xdb9042]
0020DA76  A8 40                           test al, 0x40
0020DA78  0F 84 BB FE FF FF               je 0x14020d939
0020DA7E  E8 0D 1A 10 00                  call 0x14030f490
0020DA83  84 C0                           test al, al
0020DA85  0F 84 AE FE FF FF               je 0x14020d939
0020DA8B  41 8B CE                        mov ecx, r14d
0020DA8E  E8 CD 19 10 00                  call 0x14030f460
0020DA93  E9 A3 FE FF FF                  jmp 0x14020d93b
0020DA98  8B 05 1A 90 DB 00               mov eax, dword ptr [rip + 0xdb901a]
0020DA9E  A8 40                           test al, 0x40
0020DAA0  0F 84 87 FB FF FF               je 0x14020d62d
0020DAA6  E8 E5 19 10 00                  call 0x14030f490
0020DAAB  84 C0                           test al, al
0020DAAD  0F 84 7A FB FF FF               je 0x14020d62d
0020DAB3  41 8B CE                        mov ecx, r14d
0020DAB6  E8 A5 19 10 00                  call 0x14030f460
0020DABB  E9 6F FB FF FF                  jmp 0x14020d62f
0020DAC0  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
0020DAC9  48 8D 94 24 98 00 00 00         lea rdx, [rsp + 0x98]
0020DAD1  45 0F B6 C6                     movzx r8d, r14b
0020DAD5  E8 26 2D 04 00                  call 0x140250800
0020DADA  8B C6                           mov eax, esi
0020DADC  E9 E1 FD FF FF                  jmp 0x14020d8c2
0020DAE1  8B 05 D1 8F DB 00               mov eax, dword ptr [rip + 0xdb8fd1]
0020DAE7  A8 40                           test al, 0x40
0020DAE9  0F 84 28 FF FF FF               je 0x14020da17
0020DAEF  E8 9C 19 10 00                  call 0x14030f490
0020DAF4  84 C0                           test al, al
0020DAF6  0F 84 1B FF FF FF               je 0x14020da17
0020DAFC  8B CD                           mov ecx, ebp
0020DAFE  E8 5D 19 10 00                  call 0x14030f460
0020DB03  E9 11 FF FF FF                  jmp 0x14020da19
0020DB08  40 88 6F 72                     mov byte ptr [rdi + 0x72], bpl
0020DB0C  BE 01 01 00 00                  mov esi, 0x101
0020DB11  E9 A3 F8 FF FF                  jmp 0x14020d3b9
0020DB16  4D 8B EC                        mov r13, r12
0020DB19  49 0F BC C0                     bsf rax, r8
0020DB1D  33 D2                           xor edx, edx
0020DB1F  44 8B E0                        mov r12d, eax
0020DB22  4D 0F B3 E0                     btr r8, r12
0020DB26  89 84 24 84 00 00 00            mov dword ptr [rsp + 0x84], eax
0020DB2D  4C 89 44 24 60                  mov qword ptr [rsp + 0x60], r8
0020DB32  45 33 C0                        xor r8d, r8d
0020DB35  49 8B 4C C5 00                  mov rcx, qword ptr [r13 + rax*8]
0020DB3A  E8 F1 26 00 00                  call 0x140210230
0020DB3F  4C 8B F0                        mov r14, rax
0020DB42  48 85 C0                        test rax, rax
0020DB45  74 2C                           je 0x14020db73
0020DB47  48 8B C8                        mov rcx, rax
0020DB4A  4D 0F AB E7                     bts r15, r12
0020DB4E  E8 0D 0A 00 00                  call 0x14020e560
0020DB53  41 0F B6 46 08                  movzx eax, byte ptr [r14 + 8]
0020DB58  4C 8B 44 24 60                  mov r8, qword ptr [rsp + 0x60]
0020DB5D  24 3F                           and al, 0x3f
0020DB5F  02 C0                           add al, al
0020DB61  8B CE                           mov ecx, esi
0020DB63  0C 01                           or al, 1
0020DB65  FF C6                           inc esi
0020DB67  88 84 0C A4 00 00 00            mov byte ptr [rsp + rcx + 0xa4], al
0020DB6E  4D 85 C0                        test r8, r8
0020DB71  75 A6                           jne 0x14020db19
0020DB73  4C 8B 54 24 78                  mov r10, qword ptr [rsp + 0x78]
0020DB78  8B 4C 24 50                     mov ecx, dword ptr [rsp + 0x50]
0020DB7C  E9 93 FB FF FF                  jmp 0x14020d714
0020DB81  44 8B F5                        mov r14d, ebp
0020DB84  49 8B D7                        mov rdx, r15
0020DB87  48 85 D2                        test rdx, rdx
0020DB8A  0F 84 7F 01 00 00               je 0x14020dd0f
0020DB90  48 0F BC C2                     bsf rax, rdx
0020DB94  44 8B C0                        mov r8d, eax
0020DB97  89 84 24 88 00 00 00            mov dword ptr [rsp + 0x88], eax
0020DB9E  4C 0F B3 C2                     btr rdx, r8
0020DBA2  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
0020DBA7  4E 8B 0C C0                     mov r9, qword ptr [rax + r8*8]
0020DBAB  49 3B C9                        cmp rcx, r9
0020DBAE  74 05                           je 0x14020dbb5
0020DBB0  41 FF C6                        inc r14d
0020DBB3  EB D2                           jmp 0x14020db87
0020DBB5  4D 0F B3 C7                     btr r15, r8
0020DBB9  41 8B C6                        mov eax, r14d
0020DBBC  65 4C 8B 04 25 88 01 00 00      mov r8, qword ptr gs:[0x188]
0020DBC5  4C 8D A4 24 A4 00 00 00         lea r12, [rsp + 0xa4]
0020DBCD  4C 03 E0                        add r12, rax
0020DBD0  49 8B C9                        mov rcx, r9
0020DBD3  49 8B B0 70 04 00 00            mov rsi, qword ptr [r8 + 0x470]
0020DBDA  45 33 C0                        xor r8d, r8d
0020DBDD  41 0F B6 04 24                  movzx eax, byte ptr [r12]
0020DBE2  48 D1 E8                        shr rax, 1
0020DBE5  48 6B D0 58                     imul rdx, rax, 0x58
0020DBE9  48 03 F2                        add rsi, rdx
0020DBEC  48 8D 56 10                     lea rdx, [rsi + 0x10]
0020DBF0  E8 3B 26 00 00                  call 0x140210230
0020DBF5  C6 46 1A 01                     mov byte ptr [rsi + 0x1a], 1
0020DBF9  41 83 FE 06                     cmp r14d, 6
0020DBFD  0F 82 08 01 00 00               jb 0x14020dd0b
0020DC03  E8 D4 83 2E 00                  call 0x1404f5fdc
0020DC08  CC                              int3
0020DC09  E8 D2 9F 00 00                  call 0x140217be0
0020DC0E  4D 8B BE F8 38 00 00            mov r15, qword ptr [r14 + 0x38f8]
0020DC15  44 0F B6 C0                     movzx r8d, al
0020DC19  4D 85 FF                        test r15, r15
0020DC1C  0F 84 C6 01 00 00               je 0x14020dde8
0020DC22  49 8B 07                        mov rax, qword ptr [r15]
0020DC25  49 39 6F F8                     cmp qword ptr [r15 - 8], rbp
0020DC29  0F 85 E3 01 00 00               jne 0x14020de12
0020DC2F  49 3B C7                        cmp rax, r15
0020DC32  0F 85 8B 00 00 00               jne 0x14020dcc3
0020DC38  49 89 AE F8 38 00 00            mov qword ptr [r14 + 0x38f8], rbp
0020DC3F  49 8B 47 30                     mov rax, qword ptr [r15 + 0x30]
0020DC43  49 89 2F                        mov qword ptr [r15], rbp
0020DC46  48 8B 40 38                     mov rax, qword ptr [rax + 0x38]
0020DC4A  49 89 47 10                     mov qword ptr [r15 + 0x10], rax
0020DC4E  45 84 C0                        test r8b, r8b
0020DC51  0F 85 99 00 00 00               jne 0x14020dcf0
0020DC57  4D 8B 47 10                     mov r8, qword ptr [r15 + 0x10]
0020DC5B  4D 3B 47 18                     cmp r8, qword ptr [r15 + 0x18]
0020DC5F  74 57                           je 0x14020dcb8
0020DC61  49 8B 47 28                     mov rax, qword ptr [r15 + 0x28]
0020DC65  49 8B 57 20                     mov rdx, qword ptr [r15 + 0x20]
0020DC69  48 8B 08                        mov rcx, qword ptr [rax]
0020DC6C  48 85 4A 28                     test qword ptr [rdx + 0x28], rcx
0020DC70  0F 84 C4 01 00 00               je 0x14020de3a
0020DC76  E8 65 9F 00 00                  call 0x140217be0
0020DC7B  44 0F B6 C0                     movzx r8d, al
0020DC7F  49 39 2F                        cmp qword ptr [r15], rbp
0020DC82  75 2B                           jne 0x14020dcaf
0020DC84  49 8B 8E F8 38 00 00            mov rcx, qword ptr [r14 + 0x38f8]
0020DC8B  48 85 C9                        test rcx, rcx
0020DC8E  0F 84 93 01 00 00               je 0x14020de27
0020DC94  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
0020DC98  48 39 08                        cmp qword ptr [rax], rcx
0020DC9B  0F 85 C8 F7 FF FF               jne 0x14020d469
0020DCA1  49 89 0F                        mov qword ptr [r15], rcx
0020DCA4  49 89 47 08                     mov qword ptr [r15 + 8], rax
0020DCA8  4C 89 38                        mov qword ptr [rax], r15
0020DCAB  4C 89 79 08                     mov qword ptr [rcx + 8], r15
0020DCAF  45 84 C0                        test r8b, r8b
0020DCB2  0F 85 C6 00 00 00               jne 0x14020dd7e
0020DCB8  41 BF 02 00 00 00               mov r15d, 2
0020DCBE  E9 A5 F5 FF FF                  jmp 0x14020d268
0020DCC3  49 89 86 F8 38 00 00            mov qword ptr [r14 + 0x38f8], rax
0020DCCA  49 8B 0F                        mov rcx, qword ptr [r15]
0020DCCD  49 8B 47 08                     mov rax, qword ptr [r15 + 8]
0020DCD1  4C 39 79 08                     cmp qword ptr [rcx + 8], r15
0020DCD5  0F 85 8E F7 FF FF               jne 0x14020d469
0020DCDB  4C 39 38                        cmp qword ptr [rax], r15
0020DCDE  0F 85 85 F7 FF FF               jne 0x14020d469
0020DCE4  48 89 08                        mov qword ptr [rax], rcx
0020DCE7  48 89 41 08                     mov qword ptr [rcx + 8], rax
0020DCEB  E9 4F FF FF FF                  jmp 0x14020dc3f
0020DCF0  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
0020DCF9  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
0020DD00  4D 85 C0                        test r8, r8
0020DD03  75 58                           jne 0x14020dd5d
0020DD05  FB                              sti
0020DD06  E9 4C FF FF FF                  jmp 0x14020dc57
0020DD0B  41 88 2C 24                     mov byte ptr [r12], bpl
0020DD0F  48 89 AF D0 03 00 00            mov qword ptr [rdi + 0x3d0], rbp
0020DD16  E9 3A FA FF FF                  jmp 0x14020d755
0020DD1B  41 39 AE E0 38 00 00            cmp dword ptr [r14 + 0x38e0], ebp
0020DD22  0F 85 4D F5 FF FF               jne 0x14020d275
0020DD28  E8 B3 9E 00 00                  call 0x140217be0
0020DD2D  41 38 AE E5 38 00 00            cmp byte ptr [r14 + 0x38e5], bpl
0020DD34  0F 85 22 01 00 00               jne 0x14020de5c
0020DD3A  84 C0                           test al, al
0020DD3C  0F 84 33 F5 FF FF               je 0x14020d275
0020DD42  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
0020DD4B  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
0020DD52  4D 85 C0                        test r8, r8
0020DD55  75 69                           jne 0x14020ddc0
0020DD57  FB                              sti
0020DD58  E9 18 F5 FF FF                  jmp 0x14020d275
0020DD5D  41 0F 0D 08                     prefetchw byte ptr [r8]
0020DD61  41 8B 00                        mov eax, dword ptr [r8]
0020DD64  8B D0                           mov edx, eax
0020DD66  0F BA F2 15                     btr edx, 0x15
0020DD6A  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
0020DD6F  75 F3                           jne 0x14020dd64
0020DD71  0F BA E0 15                     bt eax, 0x15
0020DD75  73 8E                           jae 0x14020dd05
0020DD77  E8 54 54 05 00                  call 0x1402631d0
0020DD7C  EB 87                           jmp 0x14020dd05
0020DD7E  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
0020DD87  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
0020DD8E  4D 85 C0                        test r8, r8
0020DD91  75 0C                           jne 0x14020dd9f
0020DD93  FB                              sti
0020DD94  41 BF 02 00 00 00               mov r15d, 2
0020DD9A  E9 C9 F4 FF FF                  jmp 0x14020d268
0020DD9F  41 0F 0D 08                     prefetchw byte ptr [r8]
0020DDA3  41 8B 00                        mov eax, dword ptr [r8]
0020DDA6  8B D0                           mov edx, eax
0020DDA8  0F BA F2 15                     btr edx, 0x15
0020DDAC  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
0020DDB1  75 F3                           jne 0x14020dda6
0020DDB3  0F BA E0 15                     bt eax, 0x15
0020DDB7  73 DA                           jae 0x14020dd93
0020DDB9  E8 12 54 05 00                  call 0x1402631d0
0020DDBE  EB D3                           jmp 0x14020dd93
0020DDC0  41 0F 0D 08                     prefetchw byte ptr [r8]
0020DDC4  41 8B 00                        mov eax, dword ptr [r8]
0020DDC7  8B D0                           mov edx, eax
0020DDC9  0F BA F2 15                     btr edx, 0x15
0020DDCD  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
0020DDD2  75 F3                           jne 0x14020ddc7
0020DDD4  0F BA E0 15                     bt eax, 0x15
0020DDD8  0F 83 79 FF FF FF               jae 0x14020dd57
0020DDDE  E8 ED 53 05 00                  call 0x1402631d0
0020DDE3  E9 6F FF FF FF                  jmp 0x14020dd57
0020DDE8  45 84 C0                        test r8b, r8b
0020DDEB  0F 84 C7 FE FF FF               je 0x14020dcb8
0020DDF1  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
0020DDFA  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
0020DE01  4D 85 C0                        test r8, r8
0020DE04  74 8D                           je 0x14020dd93
0020DE06  41 0F 0D 08                     prefetchw byte ptr [r8]
0020DE0A  41 8B 00                        mov eax, dword ptr [r8]
0020DE0D  E9 F8 88 4C 00                  jmp 0x1406d670a
0020DE12  4C 3B F8                        cmp r15, rax
0020DE15  0F 84 33 FE FF FF               je 0x14020dc4e
0020DE1B  49 89 86 F8 38 00 00            mov qword ptr [r14 + 0x38f8], rax
0020DE22  E9 27 FE FF FF                  jmp 0x14020dc4e
0020DE27  4D 89 7F 08                     mov qword ptr [r15 + 8], r15
0020DE2B  4D 89 3F                        mov qword ptr [r15], r15
0020DE2E  4D 89 BE F8 38 00 00            mov qword ptr [r14 + 0x38f8], r15
0020DE35  E9 75 FE FF FF                  jmp 0x14020dcaf
0020DE3A  49 8B D0                        mov rdx, r8
0020DE3D  49 8D 4F F8                     lea rcx, [r15 - 8]
0020DE41  E8 C2 4D 3B 00                  call 0x1405c2c08
0020DE46  85 C0                           test eax, eax
0020DE48  0F 84 6A FE FF FF               je 0x14020dcb8
0020DE4E  49 8B 4F 30                     mov rcx, qword ptr [r15 + 0x30]
0020DE52  E8 5D 44 3B 00                  call 0x1405c22b4
0020DE57  E9 5C FE FF FF                  jmp 0x14020dcb8
0020DE5C  41 39 AE E0 38 00 00            cmp dword ptr [r14 + 0x38e0], ebp
0020DE63  0F 85 D1 FE FF FF               jne 0x14020dd3a
0020DE69  41 88 AE E5 38 00 00            mov byte ptr [r14 + 0x38e5], bpl
0020DE70  F0 09 2C 24                     lock or dword ptr [rsp], ebp
0020DE74  48 8B 0D 6D 32 D1 00            mov rcx, qword ptr [rip + 0xd1326d]
0020DE7B  49 89 8E E8 38 00 00            mov qword ptr [r14 + 0x38e8], rcx
0020DE82  E9 B3 FE FF FF                  jmp 0x14020dd3a
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0020D8DF(void)
{
    __int64 result;
    unsigned int v_stack_p0;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p48;
    unsigned int v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;
    unsigned int v_stack_p84;
    unsigned int v_stack_p88;
    unsigned __int64 v_stack_p98;
    unsigned __int64 v_stack_pA4;

    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(v_rsi), (unsigned __int8)(result), a3, a4);
}
```

## 5. (Beta) C Style

```c
void sub_0020D8DF(void)
{
    int64_t result;
    uint32_t v_stack_p0;
    uint32_t v_stack_p20;
    uint64_t v_stack_p48;
    uint32_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;
    uint32_t v_stack_p84;
    uint32_t v_stack_p88;
    uint64_t v_stack_p98;
    uint64_t v_stack_pA4;

    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(local_rsi), (uint8_t)(result), a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0020D8DF&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
