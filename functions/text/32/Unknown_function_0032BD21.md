# sub_0032BD21

- RVA: `0x0032BD21`–`0x0032C244` (길이 `1,315` bytes)
- VA: `0x000000014032BD21`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007618C`
- 디코드: `299`개 명령, `1,315/1,315` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **16**; 고유 호출 대상: **15**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x0032BD24` → [MiIsPrototypePteVadLookup](MiIsPrototypePteVadLookup_function_00328B70.md) (function, `0x00328B70`)
- `0x0032BD5A` → [MI_PROTO_FORMAT_COMBINED](../22/MI_PROTO_FORMAT_COMBINED_function_0022F720.md) (function, `0x0022F720`)
- `0x0032BDF1` → [MiGetImageProtoProtection](../24/MiGetImageProtoProtection_function_0024A0A0.md) (function, `0x0024A0A0`)
- `0x0032BE2F` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x0032BE45` → [MiInvalidPteConforms](../37/MiInvalidPteConforms_function_00372A10.md) (function, `0x00372A10`)
- `0x0032BEC4` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x0032BFF4` → [MiGetProtoPteAddress](MiGetProtoPteAddress_function_0032E970.md) (function, `0x0032E970`)
- `0x0032C007` → [MiVadExtentCommitted](MiVadExtentCommitted_function_0032E930.md) (function, `0x0032E930`)
- `0x0032C041` → [MiTryLockProtoPoolPageAtDpc](../28/MiTryLockProtoPoolPageAtDpc_function_0028B3C8.md) (function, `0x0028B3C8`)
- `0x0032C05B` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x0032C0AC` → [MiCaptureProtectionFromLockedProto](../46/MiCaptureProtectionFromLockedProto_function_00460744.md) (function, `0x00460744`)
- `0x0032C137` → [MiRotatedToFrameBuffer](../2C/MiRotatedToFrameBuffer_function_002C5FE4.md) (function, `0x002C5FE4`)
- `0x0032C18C` → [MiLockSpecialPurposeMemoryCachedPage](../40/MiLockSpecialPurposeMemoryCachedPage_function_004049F0.md) (function, `0x004049F0`)
- `0x0032C1CA` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0032C1DE` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0032C1EE` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0032BD31` → RVA `0x00E2DC80` (`.data`; read)
- `0x0032BDD5` → RVA `0x00E30088` (`.data`; read)
- `0x0032BE08` → RVA `0x00011070` (`.rdata`; read)
- `0x0032BE7D` → RVA `0x00E2DCE0` (`.data`; read)
- `0x0032C073` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x0032C1D0` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **27**
  - `0x0032BD87` → [sub_0032C29C + 0x86](Unknown_function_0032C29C.md) (`tail-transfer`)
  - `0x0032BDAD` → [sub_0032C29C + 0x8F](Unknown_function_0032C29C.md) (`tail-transfer`)
  - `0x0032BDBF` → [sub_0032C29C + 0x8F](Unknown_function_0032C29C.md) (`tail-transfer`)
  - `0x0032BDF6` → [sub_0032BA64 + 0x1D2](Unknown_function_0032BA64.md) (`tail-transfer`)
  - `0x0032BE02` → [sub_0032BA64 + 0x135](Unknown_function_0032BA64.md) (`tail-transfer`)
  - `0x0032BE13` → [sub_0032BC4B + 0x2A](Unknown_function_0032BC4B.md) (`tail-transfer`)
  - `0x0032BE3C` → [sub_0032BA64 + 0x18D](Unknown_function_0032BA64.md) (`tail-transfer`)
  - `0x0032BF26` → [sub_0032BA64 + 0x18D](Unknown_function_0032BA64.md) (`tail-transfer`)
  - `0x0032BF5D` → [sub_0032C29C + 0xB7](Unknown_function_0032C29C.md) (`tail-transfer`)
  - `0x0032BF7A` → [sub_0032BA64 + 0x1B6](Unknown_function_0032BA64.md) (`tail-transfer`)
  - `0x0032BFB0` → [sub_0032BA64 + 0x1D0](Unknown_function_0032BA64.md) (`tail-transfer`)
  - `0x0032C020` → [sub_0032BA64 + 0x1D0](Unknown_function_0032BA64.md) (`tail-transfer`)
  - `0x0032C02D` → [sub_0032BA64 + 0x1D0](Unknown_function_0032BA64.md) (`tail-transfer`)
  - `0x0032C063` → [sub_0032BA64 + 0x1D0](Unknown_function_0032BA64.md) (`tail-transfer`)
  - `0x0032C06B` → [sub_0032BA64 + 0x1D0](Unknown_function_0032BA64.md) (`tail-transfer`)
  - `0x0032C0BD` → [sub_0032BA64 + 0x1D2](Unknown_function_0032BA64.md) (`tail-transfer`)
  - `0x0032C126` → [sub_0032C29C](Unknown_function_0032C29C.md) (`tail-transfer`)
  - `0x0032C12F` → [sub_0032BA64 + 0x1D2](Unknown_function_0032BA64.md) (`tail-transfer`)
  - `0x0032C13E` → [sub_0032C29C + 0x27](Unknown_function_0032C29C.md) (`tail-transfer`)
  - `0x0032C177` → [sub_0032C29C + 0x12](Unknown_function_0032C29C.md) (`tail-transfer`)
  - `0x0032C182` → [sub_0032BA64 + 0x1D2](Unknown_function_0032BA64.md) (`tail-transfer`)
  - `0x0032C197` → [sub_0032BA64 + 0x18D](Unknown_function_0032BA64.md) (`tail-transfer`)
  - `0x0032C1E5` → [sub_0032C29C + 0xAA](Unknown_function_0032C29C.md) (`tail-transfer`)
  - `0x0032C21F` → [sub_0032BA64 + 0x1D0](Unknown_function_0032BA64.md) (`tail-transfer`)
  - `0x0032C228` → [sub_0032BA64 + 0x108](Unknown_function_0032BA64.md) (`tail-transfer`)
  - `0x0032C237` → [sub_0032C29C + 0x7D](Unknown_function_0032C29C.md) (`tail-transfer`)
  - `0x0032C23F` → [sub_0032BA64 + 0x1D2](Unknown_function_0032BA64.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0032BD21  48 8B CF                        mov rcx, rdi
0032BD24  E8 47 CE FF FF                  call 0x140328b70
0032BD29  85 C0                           test eax, eax
0032BD2B  0F 85 57 02 00 00               jne 0x14032bf88
0032BD31  48 8B 05 48 1F B0 00            mov rax, qword ptr [rip + 0xb01f48]
0032BD38  4C 8B C7                        mov r8, rdi
0032BD3B  48 85 C0                        test rax, rax
0032BD3E  74 13                           je 0x14032bd53
0032BD40  40 F6 C7 10                     test dil, 0x10
0032BD44  0F 85 78 03 00 00               jne 0x14032c0c2
0032BD4A  4C 8B C0                        mov r8, rax
0032BD4D  49 F7 D0                        not r8
0032BD50  4C 23 C7                        and r8, rdi
0032BD53  48 8B CF                        mov rcx, rdi
0032BD56  49 C1 F8 10                     sar r8, 0x10
0032BD5A  E8 C1 39 F0 FF                  call 0x14022f720
0032BD5F  84 C0                           test al, al
0032BD61  0F 85 2A 03 00 00               jne 0x14032c091
0032BD67  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0032BD70  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
0032BD77  48 8B 81 80 02 00 00            mov rax, qword ptr [rcx + 0x280]
0032BD7E  48 85 C0                        test rax, rax
0032BD81  74 21                           je 0x14032bda4
0032BD83  4C 3B 40 20                     cmp r8, qword ptr [rax + 0x20]
0032BD87  0F 87 95 05 00 00               ja 0x14032c322
0032BD8D  4C 3B 40 18                     cmp r8, qword ptr [rax + 0x18]
0032BD91  73 08                           jae 0x14032bd9b
0032BD93  48 8B 00                        mov rax, qword ptr [rax]
0032BD96  48 85 C0                        test rax, rax
0032BD99  75 E8                           jne 0x14032bd83
0032BD9B  48 85 C0                        test rax, rax
0032BD9E  0F 85 5C 04 00 00               jne 0x14032c200
0032BDA4  8B 4D 30                        mov ecx, dword ptr [rbp + 0x30]
0032BDA7  8B C1                           mov eax, ecx
0032BDA9  24 70                           and al, 0x70
0032BDAB  3C 20                           cmp al, 0x20
0032BDAD  0F 85 78 05 00 00               jne 0x14032c32b
0032BDB3  81 E1 80 0F 00 00               and ecx, 0xf80
0032BDB9  81 F9 80 03 00 00               cmp ecx, 0x380
0032BDBF  0F 85 66 05 00 00               jne 0x14032c32b
0032BDC5  48 8B 45 48                     mov rax, qword ptr [rbp + 0x48]
0032BDC9  41 BD FF 03 00 00               mov r13d, 0x3ff
0032BDCF  49 8B D0                        mov rdx, r8
0032BDD2  48 8B 08                        mov rcx, qword ptr [rax]
0032BDD5  48 8B 05 AC 42 B0 00            mov rax, qword ptr [rip + 0xb042ac]
0032BDDC  0F B7 49 3C                     movzx ecx, word ptr [rcx + 0x3c]
0032BDE0  49 23 CD                        and rcx, r13
0032BDE3  48 8B 0C C8                     mov rcx, qword ptr [rax + rcx*8]
0032BDE7  0F B7 01                        movzx eax, word ptr [rcx]
0032BDEA  48 8B CD                        mov rcx, rbp
0032BDED  66 41 89 07                     mov word ptr [r15], ax
0032BDF1  E8 AA E2 F1 FF                  call 0x14024a0a0
0032BDF6  E9 3B FE FF FF                  jmp 0x14032bc36
0032BDFB  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
0032BDFF  48 85 C0                        test rax, rax
0032BE02  0F 84 91 FD FF FF               je 0x14032bb99
0032BE08  48 8D 0D 61 52 CE FF            lea rcx, [rip - 0x31ad9f]
0032BE0F  46 8B 04 81                     mov r8d, dword ptr [rcx + r8*4]
0032BE13  E9 5D FE FF FF                  jmp 0x14032bc75
0032BE18  49 BE FF FF FF FF FF 00 00 00   movabs r14, 0xffffffffff
0032BE22  49 BD 00 00 00 00 00 DE FF FF   movabs r13, 0xffffde0000000000
0032BE2C  48 8B CE                        mov rcx, rsi
0032BE2F  E8 6C 6A F5 FF                  call 0x1402828a0
0032BE34  48 8B D8                        mov rbx, rax
0032BE37  48 0F BA E0 0B                  bt rax, 0xb
0032BE3C  0F 83 AF FD FF FF               jae 0x14032bbf1
0032BE42  48 8B C8                        mov rcx, rax
0032BE45  E8 C6 6B 04 00                  call 0x140372a10
0032BE4A  85 C0                           test eax, eax
0032BE4C  74 DE                           je 0x14032be2c
0032BE4E  48 8B 05 2B 1E B0 00            mov rax, qword ptr [rip + 0xb01e2b]
0032BE55  48 85 C0                        test rax, rax
0032BE58  74 12                           je 0x14032be6c
0032BE5A  F6 C3 10                        test bl, 0x10
0032BE5D  0F 85 1C 01 00 00               jne 0x14032bf7f
0032BE63  48 8B C8                        mov rcx, rax
0032BE66  48 F7 D1                        not rcx
0032BE69  48 23 CB                        and rcx, rbx
0032BE6C  48 C1 E9 0C                     shr rcx, 0xc
0032BE70  49 23 CE                        and rcx, r14
0032BE73  4C 8D 04 49                     lea r8, [rcx + rcx*2]
0032BE77  4D 03 C0                        add r8, r8
0032BE7A  49 8B C5                        mov rax, r13
0032BE7D  48 3B 0D 5C 1E B0 00            cmp rcx, qword ptr [rip + 0xb01e5c]
0032BE84  4A 8D 14 C0                     lea rdx, [rax + r8*8]
0032BE88  48 89 94 24 88 00 00 00         mov qword ptr [rsp + 0x88], rdx
0032BE90  77 9A                           ja 0x14032be2c
0032BE92  48 B8 28 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000028
0032BE9C  48 8B C0                        mov rax, rax
0032BE9F  4A 8B 04 C0                     mov rax, qword ptr [rax + r8*8]
0032BEA3  48 C1 E8 36                     shr rax, 0x36
0032BEA7  0F BA E0 00                     bt eax, 0
0032BEAB  0F 83 7B FF FF FF               jae 0x14032be2c
0032BEB1  45 33 FF                        xor r15d, r15d
0032BEB4  F0 48 0F BA 6A 18 3F            lock bts qword ptr [rdx + 0x18], 0x3f
0032BEBB  0F 82 AF 01 00 00               jb 0x14032c070
0032BEC1  48 8B CE                        mov rcx, rsi
0032BEC4  E8 D7 69 F5 FF                  call 0x1402828a0
0032BEC9  4C 8B BC 24 A0 00 00 00         mov r15, qword ptr [rsp + 0xa0]
0032BED1  4C 8B 84 24 88 00 00 00         mov r8, qword ptr [rsp + 0x88]
0032BED9  48 3B C3                        cmp rax, rbx
0032BEDC  0F 85 E9 01 00 00               jne 0x14032c0cb
0032BEE2  49 8B 40 28                     mov rax, qword ptr [r8 + 0x28]
0032BEE6  41 BD FF 03 00 00               mov r13d, 0x3ff
0032BEEC  48 8B 15 95 41 B0 00            mov rdx, qword ptr [rip + 0xb04195]
0032BEF3  48 C1 E8 2B                     shr rax, 0x2b
0032BEF7  49 23 C5                        and rax, r13
0032BEFA  48 8B 04 C2                     mov rax, qword ptr [rdx + rax*8]
0032BEFE  8B 40 04                        mov eax, dword ptr [rax + 4]
0032BF01  84 C0                           test al, al
0032BF03  0F 88 7E 02 00 00               js 0x14032c187
0032BF09  49 8B 40 08                     mov rax, qword ptr [r8 + 8]
0032BF0D  49 B9 00 00 00 00 00 00 00 80   movabs r9, 0x8000000000000000
0032BF17  49 0B C1                        or rax, r9
0032BF1A  48 3B C6                        cmp rax, rsi
0032BF1D  0F 85 7F 02 00 00               jne 0x14032c1a2
0032BF23  4D 85 C0                        test r8, r8
0032BF26  0F 84 C5 FC FF FF               je 0x14032bbf1
0032BF2C  49 8B 40 28                     mov rax, qword ptr [r8 + 0x28]
0032BF30  48 8B 0D 51 41 B0 00            mov rcx, qword ptr [rip + 0xb04151]
0032BF37  48 C1 E8 2B                     shr rax, 0x2b
0032BF3B  49 23 C5                        and rax, r13
0032BF3E  4C 8B 0C C1                     mov r9, qword ptr [rcx + rax*8]
0032BF42  49 8B 40 28                     mov rax, qword ptr [r8 + 0x28]
0032BF46  48 8B 0D 3B 41 B0 00            mov rcx, qword ptr [rip + 0xb0413b]
0032BF4D  48 C1 E8 2B                     shr rax, 0x2b
0032BF51  49 23 C5                        and rax, r13
0032BF54  48 8B 04 C1                     mov rax, qword ptr [rcx + rax*8]
0032BF58  8B 40 04                        mov eax, dword ptr [rax + 4]
0032BF5B  84 C0                           test al, al
0032BF5D  0F 88 F0 03 00 00               js 0x14032c353
0032BF63  41 0F B7 01                     movzx eax, word ptr [r9]
0032BF67  66 41 89 07                     mov word ptr [r15], ax
0032BF6B  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
0032BF75  F0 49 21 40 18                  lock and qword ptr [r8 + 0x18], rax
0032BF7A  E9 9B FC FF FF                  jmp 0x14032bc1a
0032BF7F  48 83 E1 EF                     and rcx, 0xffffffffffffffef
0032BF83  E9 E4 FE FF FF                  jmp 0x14032be6c
0032BF88  48 C1 EF 05                     shr rdi, 5
0032BF8C  83 E7 1F                        and edi, 0x1f
0032BF8F  48 C1 E6 19                     shl rsi, 0x19
0032BF93  48 B9 00 00 00 00 80 F6 FF FF   movabs rcx, 0xfffff68000000000
0032BF9D  48 8B C1                        mov rax, rcx
0032BFA0  48 C1 E0 19                     shl rax, 0x19
0032BFA4  48 2B F0                        sub rsi, rax
0032BFA7  48 C1 FE 10                     sar rsi, 0x10
0032BFAB  41 0F BA E0 15                  bt r8d, 0x15
0032BFB0  0F 82 7E FC FF FF               jb 0x14032bc34
0032BFB6  48 8B 45 48                     mov rax, qword ptr [rbp + 0x48]
0032BFBA  4C 8D 8C 24 90 00 00 00         lea r9, [rsp + 0x90]
0032BFC2  41 BD FF 03 00 00               mov r13d, 0x3ff
0032BFC8  48 8B D6                        mov rdx, rsi
0032BFCB  48 C1 EA 0C                     shr rdx, 0xc
0032BFCF  41 B8 0C 00 00 00               mov r8d, 0xc
0032BFD5  48 8B 08                        mov rcx, qword ptr [rax]
0032BFD8  48 8B 05 A9 40 B0 00            mov rax, qword ptr [rip + 0xb040a9]
0032BFDF  0F B7 49 3C                     movzx ecx, word ptr [rcx + 0x3c]
0032BFE3  49 23 CD                        and rcx, r13
0032BFE6  48 8B 0C C8                     mov rcx, qword ptr [rax + rcx*8]
0032BFEA  0F B7 01                        movzx eax, word ptr [rcx]
0032BFED  48 8B CD                        mov rcx, rbp
0032BFF0  66 41 89 07                     mov word ptr [r15], ax
0032BFF4  E8 77 29 00 00                  call 0x14032e970
0032BFF9  4C 8B F0                        mov r14, rax
0032BFFC  48 85 C0                        test rax, rax
0032BFFF  74 68                           je 0x14032c069
0032C001  48 8B D6                        mov rdx, rsi
0032C004  48 8B CD                        mov rcx, rbp
0032C007  E8 24 29 00 00                  call 0x14032e930
0032C00C  85 C0                           test eax, eax
0032C00E  74 59                           je 0x14032c069
0032C010  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
0032C018  48 8B 00                        mov rax, qword ptr [rax]
0032C01B  48 83 78 40 00                  cmp qword ptr [rax + 0x40], 0
0032C020  0F 85 0E FC FF FF               jne 0x14032bc34
0032C026  F7 40 38 00 20 00 00            test dword ptr [rax + 0x38], 0x2000
0032C02D  0F 85 01 FC FF FF               jne 0x14032bc34
0032C033  45 33 C9                        xor r9d, r9d
0032C036  4C 8D 84 24 98 00 00 00         lea r8, [rsp + 0x98]
0032C03E  49 8B CE                        mov rcx, r14
0032C041  E8 82 F3 F5 FF                  call 0x14028b3c8
0032C046  85 C0                           test eax, eax
0032C048  0F 88 C9 01 00 00               js 0x14032c217
0032C04E  49 8B 1E                        mov rbx, qword ptr [r14]
0032C051  B2 11                           mov dl, 0x11
0032C053  48 8B 8C 24 98 00 00 00         mov rcx, qword ptr [rsp + 0x98]
0032C05B  E8 30 A0 F1 FF                  call 0x140246090
0032C060  48 85 DB                        test rbx, rbx
0032C063  0F 85 CB FB FF FF               jne 0x14032bc34
0032C069  33 FF                           xor edi, edi
0032C06B  E9 C4 FB FF FF                  jmp 0x14032bc34
0032C070  41 FF C7                        inc r15d
0032C073  44 85 3D 32 92 C9 00            test dword ptr [rip + 0xc99232], r15d
0032C07A  0F 84 50 01 00 00               je 0x14032c1d0
0032C080  F3 90                           pause
0032C082  48 8B 42 18                     mov rax, qword ptr [rdx + 0x18]
0032C086  48 85 C0                        test rax, rax
0032C089  0F 89 25 FE FF FF               jns 0x14032beb4
0032C08F  EB DF                           jmp 0x14032c070
0032C091  49 8D 40 E0                     lea rax, [r8 - 0x20]
0032C095  48 25 00 F0 FF FF               and rax, 0xfffffffffffff000
0032C09B  48 8B 40 10                     mov rax, qword ptr [rax + 0x10]
0032C09F  48 8B 00                        mov rax, qword ptr [rax]
0032C0A2  0F B7 00                        movzx eax, word ptr [rax]
0032C0A5  49 8B C8                        mov rcx, r8
0032C0A8  66 41 89 07                     mov word ptr [r15], ax
0032C0AC  E8 93 46 13 00                  call 0x140460744
0032C0B1  8B C0                           mov eax, eax
0032C0B3  48 8D 0D B6 4F CE FF            lea rcx, [rip - 0x31b04a]
0032C0BA  8B 04 81                        mov eax, dword ptr [rcx + rax*4]
0032C0BD  E9 74 FB FF FF                  jmp 0x14032bc36
0032C0C2  49 83 E0 EF                     and r8, 0xffffffffffffffef
0032C0C6  E9 88 FC FF FF                  jmp 0x14032bd53
0032C0CB  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
0032C0D5  F0 49 21 40 18                  lock and qword ptr [r8 + 0x18], rax
0032C0DA  E9 4D FD FF FF                  jmp 0x14032be2c
0032C0DF  48 3B 15 FA 1B B0 00            cmp rdx, qword ptr [rip + 0xb01bfa]
0032C0E6  77 31                           ja 0x14032c119
0032C0E8  48 B8 28 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000028
0032C0F2  48 8B C0                        mov rax, rax
0032C0F5  4A 8B 04 C0                     mov rax, qword ptr [rax + r8*8]
0032C0F9  48 C1 E8 36                     shr rax, 0x36
0032C0FD  0F BA E0 00                     bt eax, 0
0032C101  73 16                           jae 0x14032c119
0032C103  48 8B 43 28                     mov rax, qword ptr [rbx + 0x28]
0032C107  41 BD FF 03 00 00               mov r13d, 0x3ff
0032C10D  48 C1 E8 2B                     shr rax, 0x2b
0032C111  66 41 23 C5                     and ax, r13w
0032C115  66 41 89 07                     mov word ptr [r15], ax
0032C119  8B 45 30                        mov eax, dword ptr [rbp + 0x30]
0032C11C  C1 E8 07                        shr eax, 7
0032C11F  83 E0 1F                        and eax, 0x1f
0032C122  40 F6 C7 10                     test dil, 0x10
0032C126  0F 84 70 01 00 00               je 0x14032c29c
0032C12C  83 C8 08                        or eax, 8
0032C12F  E9 02 FB FF FF                  jmp 0x14032bc36
0032C134  48 8B CE                        mov rcx, rsi
0032C137  E8 A8 9E F9 FF                  call 0x1402c5fe4
0032C13C  85 C0                           test eax, eax
0032C13E  0F 84 7F 01 00 00               je 0x14032c2c3
0032C144  48 0F BA E7 0B                  bt rdi, 0xb
0032C149  B8 04 00 00 00                  mov eax, 4
0032C14E  BA 01 00 00 00                  mov edx, 1
0032C153  0F 42 D0                        cmovb edx, eax
0032C156  8B 45 30                        mov eax, dword ptr [rbp + 0x30]
0032C159  44 8B C0                        mov r8d, eax
0032C15C  41 81 E0 00 0C 00 00            and r8d, 0xc00
0032C163  A9 80 03 00 00                  test eax, 0x380
0032C168  0F 95 C1                        setne cl
0032C16B  41 81 F8 00 0C 00 00            cmp r8d, 0xc00
0032C172  0F 94 C0                        sete al
0032C175  84 C8                           test al, cl
0032C177  0F 84 31 01 00 00               je 0x14032c2ae
0032C17D  83 CA 18                        or edx, 0x18
0032C180  8B C2                           mov eax, edx
0032C182  E9 AF FA FF FF                  jmp 0x14032bc36
0032C187  33 D2                           xor edx, edx
0032C189  49 8B C8                        mov rcx, r8
0032C18C  E8 5F 88 0D 00                  call 0x1404049f0
0032C191  4C 8B C0                        mov r8, rax
0032C194  48 85 C0                        test rax, rax
0032C197  0F 84 54 FA FF FF               je 0x14032bbf1
0032C19D  E9 67 FD FF FF                  jmp 0x14032bf09
0032C1A2  49 8B 40 28                     mov rax, qword ptr [r8 + 0x28]
0032C1A6  48 0F BA E0 28                  bt rax, 0x28
0032C1AB  0F 82 72 FD FF FF               jb 0x14032bf23
0032C1B1  49 8B 40 08                     mov rax, qword ptr [r8 + 8]
0032C1B5  4C 8B CB                        mov r9, rbx
0032C1B8  4C 8B C6                        mov r8, rsi
0032C1BB  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0032C1C0  BA 11 04 00 00                  mov edx, 0x411
0032C1C5  B9 1A 00 00 00                  mov ecx, 0x1a
0032C1CA  E8 91 14 1D 00                  call 0x1404fd660
0032C1CF  CC                              int3
0032C1D0  8B 05 E2 A8 C9 00               mov eax, dword ptr [rip + 0xc9a8e2]
0032C1D6  A8 40                           test al, 0x40
0032C1D8  0F 84 A2 FE FF FF               je 0x14032c080
0032C1DE  E8 AD 32 FE FF                  call 0x14030f490
0032C1E3  84 C0                           test al, al
0032C1E5  0F 84 5B 01 00 00               je 0x14032c346
0032C1EB  41 8B CF                        mov ecx, r15d
0032C1EE  E8 6D 32 FE FF                  call 0x14030f460
0032C1F3  48 8B 94 24 88 00 00 00         mov rdx, qword ptr [rsp + 0x88]
0032C1FB  E9 82 FE FF FF                  jmp 0x14032c082
0032C200  4C 39 50 30                     cmp qword ptr [rax + 0x30], r10
0032C204  0F 84 9A FB FF FF               je 0x14032bda4
0032C20A  48 8B 40 38                     mov rax, qword ptr [rax + 0x38]
0032C20E  48 8B 40 18                     mov rax, qword ptr [rax + 0x18]
0032C212  E9 8B FE FF FF                  jmp 0x14032c0a2
0032C217  4C 89 33                        mov qword ptr [rbx], r14
0032C21A  BF 00 01 00 00                  mov edi, 0x100
0032C21F  E9 10 FA FF FF                  jmp 0x14032bc34
0032C224  41 83 C8 08                     or r8d, 8
0032C228  E9 3F F9 FF FF                  jmp 0x14032bb6c
0032C22D  25 00 00 20 04                  and eax, 0x4200000
0032C232  3D 00 00 20 04                  cmp eax, 0x4200000
0032C237  0F 84 DC 00 00 00               je 0x14032c319
0032C23D  8B C1                           mov eax, ecx
0032C23F  E9 F2 F9 FF FF                  jmp 0x14032bc36
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0032BD21(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13, __int64 a14, __int64 a15, __int64 a16, __int64 a17, __int64 a18, __int64 a19)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p88;
    unsigned __int64 v_stack_pA0;

    result = MiIsPrototypePteVadLookup(v_rdi, a2, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_0032BF88;
    if (*(unsigned __int64 *)(v_rip + 11542344) == 0) goto loc_0032BD53;
    if ((((unsigned __int8)(v_rdi)) & (16)) != 0) goto loc_0032C0C2;
    a3 = ~(*(unsigned __int64 *)(v_rip + 11542344));
    a3 = (a3) & (v_rdi);
loc_0032BD53:
    a3 = (a3) >> (16);
    result = MI_PROTO_FORMAT_COMBINED(v_rdi, a2, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_0032C091;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 640) == 0) goto loc_0032BDA4;
loc_0032BD83:
    if (a3 >= (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 640) + 24))) goto loc_0032BD9B;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 640)) != 0) goto loc_0032BD83;
loc_0032BD9B:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 640)) != 0) goto loc_0032C200;
loc_0032BDA4:
    result = (unsigned __int8)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rbp + 48))))) & (112));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbp + 48))) & (0xF80ULL));
    a1 = (*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 72)) + 60)) & ((unsigned int)(0x3FFULL));
    *(unsigned __int16 *)(v_r15) = (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11551404) + a1 * 8)));
    result = MiGetImageProtoProtection(v_rbp, a3, a3, a4);
loc_0032BF88:
    v_rdi = (v_rdi) >> (5);
    v_rdi = (unsigned int)((v_rdi) & (31));
    v_rsi = (v_rsi) << (25);
    result = (v_rbp) << (25);
    v_rsi = (v_rsi) - (result);
    v_rsi = (v_rsi) >> (16);
    a2 = (v_rsi) >> (12);
    a1 = (*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 72)) + 60)) & ((unsigned int)(0x3FFULL));
    *(unsigned __int16 *)(v_r15) = (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11550889) + a1 * 8)));
    result = MiGetProtoPteAddress(v_rbp, a2, 12, a18);
    if (result == 0) goto loc_0032C069;
    result = MiVadExtentCommitted(v_rbp, v_rsi, 12, a18);
    if ((unsigned int)(result) == 0) goto loc_0032C069;
    a4 = 0;
    result = MiTryLockProtoPoolPageAtDpc(result, v_rsi, a19, a4);
    if (sign_flag) goto loc_0032C217;
    result = MiUnlockProtoPoolPage(a19, 17, a19, a4);
loc_0032C069:
    v_rdi = 0;
loc_0032C091:
    result = (a19 - 32) & (0xFFFFFFFFFFFFF000ULL);
loc_0032C0A2:
    *(unsigned __int16 *)(v_r15) = (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 16))));
    result = MiCaptureProtectionFromLockedProto(a19, 17, a19, a4);
loc_0032C0C2:
    a3 = (a19) & (-17);
    goto loc_0032BD53;
loc_0032C200:
    if ((*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(v_rip - 3256394 + (unsigned int)((unsigned int)(result)) * 4)) + 48)) == v_r10) goto loc_0032BDA4;
    goto loc_0032C0A2;
loc_0032C217:
    *(unsigned __int64 *)(*(unsigned __int64 *)(result)) = result;
}
```

## 5. (Beta) C Style

```c
int64_t sub_0032BD21(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, uint64_t Arg10, uint64_t Arg11, uint64_t Arg12, uint64_t Arg13, uint64_t Arg14, uint64_t Arg15, uint64_t Arg16, uint64_t Arg17, void *Arg18, int64_t Arg19)
{
    uint8_t *arg18 = (uint8_t *)Arg18;

    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    uint64_t v_stack_p20;
    uint64_t v_stack_p88;
    uint64_t v_stack_pA0;

    result = MiIsPrototypePteVadLookup(local_rdi, Arg2, Arg3, Arg4);
    if ((uint32_t)(result) != 0) goto loc_0032BF88;
    if (*(uint64_t *)(v_rip + 0xB01F48) == 0) goto loc_0032BD53;
    if ((((uint8_t)(local_rdi)) & (16)) != 0) goto loc_0032C0C2;
    Arg3 = ~(*(uint64_t *)(v_rip + 0xB01F48));
    Arg3 = (Arg3) & (local_rdi);
loc_0032BD53:
    Arg3 = (Arg3) >> (16);
    result = MI_PROTO_FORMAT_COMBINED(local_rdi, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) != 0) goto loc_0032C091;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x280) == 0) goto loc_0032BDA4;
loc_0032BD83:
    if (Arg3 >= (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x280) + 0x18))) goto loc_0032BD9B;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x280)) != 0) goto loc_0032BD83;
loc_0032BD9B:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x280)) != 0) goto loc_0032C200;
loc_0032BDA4:
    result = (uint8_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rbp + 0x30))))) & (112));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbp + 0x30))) & (0xF80ULL));
    Arg1 = (*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp + 0x48)) + 0x3C)) & ((uint32_t)(0x3FFULL));
    *(uint16_t *)(local_r15) = (uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB042AC) + Arg1 * 8)));
    result = MiGetImageProtoProtection(local_rbp, Arg3, Arg3, Arg4);
loc_0032BF88:
    local_rdi = (local_rdi) >> (5);
    local_rdi = (uint32_t)((local_rdi) & (31));
    local_rsi = (local_rsi) << (25);
    result = (local_rbp) << (25);
    local_rsi = (local_rsi) - (result);
    local_rsi = (local_rsi) >> (16);
    Arg2 = (local_rsi) >> (12);
    Arg1 = (*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp + 0x48)) + 0x3C)) & ((uint32_t)(0x3FFULL));
    *(uint16_t *)(local_r15) = (uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB040A9) + Arg1 * 8)));
    result = MiGetProtoPteAddress(local_rbp, Arg2, 12, Arg18);
    if (result == 0) goto loc_0032C069;
    result = MiVadExtentCommitted(local_rbp, local_rsi, 12, Arg18);
    if ((uint32_t)(result) == 0) goto loc_0032C069;
    Arg4 = 0;
    result = MiTryLockProtoPoolPageAtDpc(result, local_rsi, Arg19, Arg4);
    if (sign_flag) goto loc_0032C217;
    result = MiUnlockProtoPoolPage(Arg19, 17, Arg19, Arg4);
loc_0032C069:
    local_rdi = 0;
loc_0032C091:
    result = (Arg19 - 32) & (0xFFFFFFFFFFFFF000ULL);
loc_0032C0A2:
    *(uint16_t *)(local_r15) = (uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x10))));
    result = MiCaptureProtectionFromLockedProto(Arg19, 17, Arg19, Arg4);
loc_0032C0C2:
    Arg3 = (Arg19) & (-17);
    goto loc_0032BD53;
loc_0032C200:
    if ((*(uint64_t *)((uint32_t)(*(uint32_t *)(v_rip - 0x31B04A + (uint32_t)((uint32_t)(result)) * 4)) + 0x30)) == local_r10) goto loc_0032BDA4;
    goto loc_0032C0A2;
loc_0032C217:
    *(uint64_t *)(*(uint64_t *)(result)) = result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg18` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0032BD21&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
