# deflate_slow

- RVA: `0x005F4430`–`0x005F4A6D` (길이 `1,597` bytes)
- VA: `0x00000001405F4430`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000D046C`
- 디코드: `364`개 명령, `1,597/1,597` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **10**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x005F4478` → [fill_window](fill_window_function_005F4EF0.md) (function, `0x005F4EF0`)
- `0x005F45C5` → [longest_match](longest_match_function_005F539C.md) (function, `0x005F539C`)
- `0x005F482C` → [tr_flush_block](../60/tr_flush_block_function_00600AF8.md) (function, `0x00600AF8`)
- `0x005F4840` → [flush_pending](flush_pending_function_005F5258.md) (function, `0x005F5258`)
- `0x005F48E8` → [tr_flush_block](../60/tr_flush_block_function_00600AF8.md) (function, `0x00600AF8`)
- `0x005F48FC` → [flush_pending](flush_pending_function_005F5258.md) (function, `0x005F5258`)
- `0x005F49F1` → [tr_flush_block](../60/tr_flush_block_function_00600AF8.md) (function, `0x00600AF8`)
- `0x005F4A02` → [flush_pending](flush_pending_function_005F5258.md) (function, `0x005F5258`)
- `0x005F4A43` → [tr_flush_block](../60/tr_flush_block_function_00600AF8.md) (function, `0x00600AF8`)
- `0x005F4A54` → [flush_pending](flush_pending_function_005F5258.md) (function, `0x005F5258`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x005F44B0` → RVA `0x00E67B40` (`.data`; read)
- `0x005F4698` → RVA `0x00036720` (`.rdata`; read)
- `0x005F46C3` → RVA `0x00036520` (`.rdata`; read)
- `0x005F46D0` → RVA `0x00036620` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005F4430  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
005F4435  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
005F443A  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
005F443F  57                              push rdi
005F4440  41 54                           push r12
005F4442  41 55                           push r13
005F4444  41 56                           push r14
005F4446  41 57                           push r15
005F4448  48 83 EC 20                     sub rsp, 0x20
005F444C  33 FF                           xor edi, edi
005F444E  4C 8D B9 E4 00 00 00            lea r15, [rcx + 0xe4]
005F4455  44 8B E2                        mov r12d, edx
005F4458  48 8B D9                        mov rbx, rcx
005F445B  49 8B F7                        mov rsi, r15
005F445E  4D 8B F7                        mov r14, r15
005F4461  8D 6F 02                        lea ebp, [rdi + 2]
005F4464  44 8D 6F 01                     lea r13d, [rdi + 1]
005F4468  8B 83 EC 00 00 00               mov eax, dword ptr [rbx + 0xec]
005F446E  3D 06 01 00 00                  cmp eax, 0x106
005F4473  73 30                           jae 0x1405f44a5
005F4475  48 8B CB                        mov rcx, rbx
005F4478  E8 73 0A 00 00                  call 0x1405f4ef0
005F447D  8B 83 EC 00 00 00               mov eax, dword ptr [rbx + 0xec]
005F4483  3D 06 01 00 00                  cmp eax, 0x106
005F4488  73 10                           jae 0x1405f449a
005F448A  45 85 E4                        test r12d, r12d
005F448D  0F 84 83 04 00 00               je 0x1405f4916
005F4493  4C 8D B3 E4 00 00 00            lea r14, [rbx + 0xe4]
005F449A  49 8B F7                        mov rsi, r15
005F449D  85 C0                           test eax, eax
005F449F  0F 84 AA 04 00 00               je 0x1405f494f
005F44A5  8B D7                           mov edx, edi
005F44A7  83 F8 03                        cmp eax, 3
005F44AA  0F 82 D1 00 00 00               jb 0x1405f4581
005F44B0  39 3D 8A 36 87 00               cmp dword ptr [rip + 0x87368a], edi
005F44B6  44 0F B7 0E                     movzx r9d, word ptr [rsi]
005F44BA  48 8B 83 A0 00 00 00            mov rax, qword ptr [rbx + 0xa0]
005F44C1  74 4E                           je 0x1405f4511
005F44C3  41 8B 14 01                     mov edx, dword ptr [r9 + rax]
005F44C7  8B CA                           mov ecx, edx
005F44C9  81 E1 FF FF FF 00               and ecx, 0xffffff
005F44CF  8B C7                           mov eax, edi
005F44D1  83 BB FC 00 00 00 06            cmp dword ptr [rbx + 0xfc], 6
005F44D8  0F 4C CA                        cmovl ecx, edx
005F44DB  F2 0F 38 F1 C1                  crc32 eax, ecx
005F44E0  8B C8                           mov ecx, eax
005F44E2  8B 83 CC 00 00 00               mov eax, dword ptr [rbx + 0xcc]
005F44E8  48 23 C8                        and rcx, rax
005F44EB  48 8B 83 B8 00 00 00            mov rax, qword ptr [rbx + 0xb8]
005F44F2  0F B7 14 48                     movzx edx, word ptr [rax + rcx*2]
005F44F6  66 44 89 0C 48                  mov word ptr [rax + rcx*2], r9w
005F44FB  8B 8B 9C 00 00 00               mov ecx, dword ptr [rbx + 0x9c]
005F4501  48 8B 83 B0 00 00 00            mov rax, qword ptr [rbx + 0xb0]
005F4508  49 23 C9                        and rcx, r9
005F450B  66 89 14 48                     mov word ptr [rax + rcx*2], dx
005F450F  EB 6D                           jmp 0x1405f457e
005F4511  41 0F B6 44 01 02               movzx eax, byte ptr [r9 + rax + 2]
005F4517  44 8B 83 C0 00 00 00            mov r8d, dword ptr [rbx + 0xc0]
005F451E  8B 8B D0 00 00 00               mov ecx, dword ptr [rbx + 0xd0]
005F4524  8B 93 9C 00 00 00               mov edx, dword ptr [rbx + 0x9c]
005F452A  41 D3 E0                        shl r8d, cl
005F452D  49 23 D1                        and rdx, r9
005F4530  48 8B 8B B0 00 00 00            mov rcx, qword ptr [rbx + 0xb0]
005F4537  44 33 C0                        xor r8d, eax
005F453A  44 23 83 CC 00 00 00            and r8d, dword ptr [rbx + 0xcc]
005F4541  48 8B 83 B8 00 00 00            mov rax, qword ptr [rbx + 0xb8]
005F4548  44 89 83 C0 00 00 00            mov dword ptr [rbx + 0xc0], r8d
005F454F  42 0F B7 04 40                  movzx eax, word ptr [rax + r8*2]
005F4554  66 89 04 51                     mov word ptr [rcx + rdx*2], ax
005F4558  48 8B 83 B0 00 00 00            mov rax, qword ptr [rbx + 0xb0]
005F455F  8B 8B 9C 00 00 00               mov ecx, dword ptr [rbx + 0x9c]
005F4565  49 23 C9                        and rcx, r9
005F4568  0F B7 14 48                     movzx edx, word ptr [rax + rcx*2]
005F456C  8B 8B C0 00 00 00               mov ecx, dword ptr [rbx + 0xc0]
005F4572  48 8B 83 B8 00 00 00            mov rax, qword ptr [rbx + 0xb8]
005F4579  66 44 89 0C 48                  mov word ptr [rax + rcx*2], r9w
005F457E  0F B7 D2                        movzx edx, dx
005F4581  8B 8B D8 00 00 00               mov ecx, dword ptr [rbx + 0xd8]
005F4587  44 8B C5                        mov r8d, ebp
005F458A  8B 83 E8 00 00 00               mov eax, dword ptr [rbx + 0xe8]
005F4590  89 8B F0 00 00 00               mov dword ptr [rbx + 0xf0], ecx
005F4596  89 83 DC 00 00 00               mov dword ptr [rbx + 0xdc], eax
005F459C  89 AB D8 00 00 00               mov dword ptr [rbx + 0xd8], ebp
005F45A2  85 D2                           test edx, edx
005F45A4  74 5D                           je 0x1405f4603
005F45A6  3B 8B F8 00 00 00               cmp ecx, dword ptr [rbx + 0xf8]
005F45AC  73 55                           jae 0x1405f4603
005F45AE  8B 8B 94 00 00 00               mov ecx, dword ptr [rbx + 0x94]
005F45B4  8B 06                           mov eax, dword ptr [rsi]
005F45B6  81 E9 06 01 00 00               sub ecx, 0x106
005F45BC  2B C2                           sub eax, edx
005F45BE  3B C1                           cmp eax, ecx
005F45C0  77 41                           ja 0x1405f4603
005F45C2  48 8B CB                        mov rcx, rbx
005F45C5  E8 D2 0D 00 00                  call 0x1405f539c
005F45CA  89 83 D8 00 00 00               mov dword ptr [rbx + 0xd8], eax
005F45D0  44 8B C0                        mov r8d, eax
005F45D3  83 F8 05                        cmp eax, 5
005F45D6  77 2B                           ja 0x1405f4603
005F45D8  44 39 AB 00 01 00 00            cmp dword ptr [rbx + 0x100], r13d
005F45DF  74 19                           je 0x1405f45fa
005F45E1  83 F8 03                        cmp eax, 3
005F45E4  75 1D                           jne 0x1405f4603
005F45E6  8B 8B E4 00 00 00               mov ecx, dword ptr [rbx + 0xe4]
005F45EC  2B 8B E8 00 00 00               sub ecx, dword ptr [rbx + 0xe8]
005F45F2  81 F9 00 10 00 00               cmp ecx, 0x1000
005F45F8  76 09                           jbe 0x1405f4603
005F45FA  89 AB D8 00 00 00               mov dword ptr [rbx + 0xd8], ebp
005F4600  44 8B C5                        mov r8d, ebp
005F4603  8B 83 F0 00 00 00               mov eax, dword ptr [rbx + 0xf0]
005F4609  83 F8 03                        cmp eax, 3
005F460C  0F 82 38 02 00 00               jb 0x1405f484a
005F4612  44 3B C0                        cmp r8d, eax
005F4615  0F 87 2F 02 00 00               ja 0x1405f484a
005F461B  8B 8B 44 17 00 00               mov ecx, dword ptr [rbx + 0x1744]
005F4621  48 8D B3 E4 00 00 00            lea rsi, [rbx + 0xe4]
005F4628  44 0F B7 0E                     movzx r9d, word ptr [rsi]
005F462C  44 8A C0                        mov r8b, al
005F462F  66 44 2B 8B DC 00 00 00         sub r9w, word ptr [rbx + 0xdc]
005F4637  41 80 E8 03                     sub r8b, 3
005F463B  8B AB EC 00 00 00               mov ebp, dword ptr [rbx + 0xec]
005F4641  66 45 2B CD                     sub r9w, r13w
005F4645  48 8B 83 38 17 00 00            mov rax, qword ptr [rbx + 0x1738]
005F464C  83 C5 FD                        add ebp, -3
005F464F  03 2E                           add ebp, dword ptr [rsi]
005F4651  44 88 0C 01                     mov byte ptr [rcx + rax], r9b
005F4655  41 0F B7 C9                     movzx ecx, r9w
005F4659  44 01 AB 44 17 00 00            add dword ptr [rbx + 0x1744], r13d
005F4660  8B 93 44 17 00 00               mov edx, dword ptr [rbx + 0x1744]
005F4666  48 8B 83 38 17 00 00            mov rax, qword ptr [rbx + 0x1738]
005F466D  66 C1 E9 08                     shr cx, 8
005F4671  88 0C 02                        mov byte ptr [rdx + rax], cl
005F4674  44 01 AB 44 17 00 00            add dword ptr [rbx + 0x1744], r13d
005F467B  8B 8B 44 17 00 00               mov ecx, dword ptr [rbx + 0x1744]
005F4681  48 8B 83 38 17 00 00            mov rax, qword ptr [rbx + 0x1738]
005F4688  44 88 04 01                     mov byte ptr [rcx + rax], r8b
005F468C  B8 FF FF 00 00                  mov eax, 0xffff
005F4691  44 01 AB 44 17 00 00            add dword ptr [rbx + 0x1744], r13d
005F4698  48 8D 0D 81 20 A4 FF            lea rcx, [rip - 0x5bdf7f]
005F469F  66 44 03 C8                     add r9w, ax
005F46A3  41 0F B6 C0                     movzx eax, r8b
005F46A7  0F B6 0C 08                     movzx ecx, byte ptr [rax + rcx]
005F46AB  B8 00 01 00 00                  mov eax, 0x100
005F46B0  66 44 01 AC 8B 10 05 00 00      add word ptr [rbx + rcx*4 + 0x510], r13w
005F46B9  66 44 3B C8                     cmp r9w, ax
005F46BD  41 0F B7 C1                     movzx eax, r9w
005F46C1  73 09                           jae 0x1405f46cc
005F46C3  48 8D 0D 56 1E A4 FF            lea rcx, [rip - 0x5be1aa]
005F46CA  EB 0B                           jmp 0x1405f46d7
005F46CC  48 C1 E8 07                     shr rax, 7
005F46D0  48 8D 0D 49 1F A4 FF            lea rcx, [rip - 0x5be0b7]
005F46D7  48 03 C1                        add rax, rcx
005F46DA  0F B6 00                        movzx eax, byte ptr [rax]
005F46DD  66 44 01 AC 83 00 0A 00 00      add word ptr [rbx + rax*4 + 0xa00], r13w
005F46E6  41 8B C5                        mov eax, r13d
005F46E9  8B 8B F0 00 00 00               mov ecx, dword ptr [rbx + 0xf0]
005F46EF  2B C1                           sub eax, ecx
005F46F1  01 83 EC 00 00 00               add dword ptr [rbx + 0xec], eax
005F46F7  44 8B 93 44 17 00 00            mov r10d, dword ptr [rbx + 0x1744]
005F46FE  44 8B 9B 48 17 00 00            mov r11d, dword ptr [rbx + 0x1748]
005F4705  8D 41 FE                        lea eax, [rcx - 2]
005F4708  89 83 F0 00 00 00               mov dword ptr [rbx + 0xf0], eax
005F470E  44 01 2E                        add dword ptr [rsi], r13d
005F4711  39 2E                           cmp dword ptr [rsi], ebp
005F4713  0F 87 BA 00 00 00               ja 0x1405f47d3
005F4719  39 3D 21 34 87 00               cmp dword ptr [rip + 0x873421], edi
005F471F  44 0F B7 0E                     movzx r9d, word ptr [rsi]
005F4723  48 8B 83 A0 00 00 00            mov rax, qword ptr [rbx + 0xa0]
005F472A  74 4E                           je 0x1405f477a
005F472C  41 8B 14 01                     mov edx, dword ptr [r9 + rax]
005F4730  8B CA                           mov ecx, edx
005F4732  81 E1 FF FF FF 00               and ecx, 0xffffff
005F4738  8B C7                           mov eax, edi
005F473A  83 BB FC 00 00 00 06            cmp dword ptr [rbx + 0xfc], 6
005F4741  0F 4C CA                        cmovl ecx, edx
005F4744  F2 0F 38 F1 C1                  crc32 eax, ecx
005F4749  8B C8                           mov ecx, eax
005F474B  8B 83 CC 00 00 00               mov eax, dword ptr [rbx + 0xcc]
005F4751  48 23 C8                        and rcx, rax
005F4754  48 8B 83 B8 00 00 00            mov rax, qword ptr [rbx + 0xb8]
005F475B  0F B7 14 48                     movzx edx, word ptr [rax + rcx*2]
005F475F  66 44 89 0C 48                  mov word ptr [rax + rcx*2], r9w
005F4764  8B 8B 9C 00 00 00               mov ecx, dword ptr [rbx + 0x9c]
005F476A  48 8B 83 B0 00 00 00            mov rax, qword ptr [rbx + 0xb0]
005F4771  49 23 C9                        and rcx, r9
005F4774  66 89 14 48                     mov word ptr [rax + rcx*2], dx
005F4778  EB 59                           jmp 0x1405f47d3
005F477A  41 0F B6 44 01 02               movzx eax, byte ptr [r9 + rax + 2]
005F4780  44 8B 83 C0 00 00 00            mov r8d, dword ptr [rbx + 0xc0]
005F4787  8B 8B D0 00 00 00               mov ecx, dword ptr [rbx + 0xd0]
005F478D  8B 93 9C 00 00 00               mov edx, dword ptr [rbx + 0x9c]
005F4793  41 D3 E0                        shl r8d, cl
005F4796  48 8B 8B B0 00 00 00            mov rcx, qword ptr [rbx + 0xb0]
005F479D  44 33 C0                        xor r8d, eax
005F47A0  44 23 83 CC 00 00 00            and r8d, dword ptr [rbx + 0xcc]
005F47A7  48 8B 83 B8 00 00 00            mov rax, qword ptr [rbx + 0xb8]
005F47AE  49 23 D1                        and rdx, r9
005F47B1  44 89 83 C0 00 00 00            mov dword ptr [rbx + 0xc0], r8d
005F47B8  42 0F B7 04 40                  movzx eax, word ptr [rax + r8*2]
005F47BD  66 89 04 51                     mov word ptr [rcx + rdx*2], ax
005F47C1  8B 8B C0 00 00 00               mov ecx, dword ptr [rbx + 0xc0]
005F47C7  48 8B 83 B8 00 00 00            mov rax, qword ptr [rbx + 0xb8]
005F47CE  66 44 89 0C 48                  mov word ptr [rax + rcx*2], r9w
005F47D3  83 83 F0 00 00 00 FF            add dword ptr [rbx + 0xf0], -1
005F47DA  0F 85 2E FF FF FF               jne 0x1405f470e
005F47E0  44 8B 83 E4 00 00 00            mov r8d, dword ptr [rbx + 0xe4]
005F47E7  BD 02 00 00 00                  mov ebp, 2
005F47EC  41 FF C0                        inc r8d
005F47EF  89 BB E0 00 00 00               mov dword ptr [rbx + 0xe0], edi
005F47F5  89 AB D8 00 00 00               mov dword ptr [rbx + 0xd8], ebp
005F47FB  44 89 83 E4 00 00 00            mov dword ptr [rbx + 0xe4], r8d
005F4802  45 3B D3                        cmp r10d, r11d
005F4805  0F 85 3C 01 00 00               jne 0x1405f4947
005F480B  8B 83 D4 00 00 00               mov eax, dword ptr [rbx + 0xd4]
005F4811  85 C0                           test eax, eax
005F4813  78 0B                           js 0x1405f4820
005F4815  8B D0                           mov edx, eax
005F4817  48 03 93 A0 00 00 00            add rdx, qword ptr [rbx + 0xa0]
005F481E  EB 03                           jmp 0x1405f4823
005F4820  48 8B D7                        mov rdx, rdi
005F4823  44 2B C0                        sub r8d, eax
005F4826  45 33 C9                        xor r9d, r9d
005F4829  48 8B CB                        mov rcx, rbx
005F482C  E8 C7 C2 00 00                  call 0x140600af8
005F4831  8B 83 E4 00 00 00               mov eax, dword ptr [rbx + 0xe4]
005F4837  48 8B 0B                        mov rcx, qword ptr [rbx]
005F483A  89 83 D4 00 00 00               mov dword ptr [rbx + 0xd4], eax
005F4840  E8 13 0A 00 00                  call 0x1405f5258
005F4845  E9 C4 00 00 00                  jmp 0x1405f490e
005F484A  48 8D B3 E4 00 00 00            lea rsi, [rbx + 0xe4]
005F4851  8B 06                           mov eax, dword ptr [rsi]
005F4853  39 BB E0 00 00 00               cmp dword ptr [rbx + 0xe0], edi
005F4859  0F 84 D7 00 00 00               je 0x1405f4936
005F485F  8D 48 FF                        lea ecx, [rax - 1]
005F4862  48 8B D5                        mov rdx, rbp
005F4865  48 8B 83 A0 00 00 00            mov rax, qword ptr [rbx + 0xa0]
005F486C  44 0F B6 04 01                  movzx r8d, byte ptr [rcx + rax]
005F4871  48 8B 83 38 17 00 00            mov rax, qword ptr [rbx + 0x1738]
005F4878  8B 8B 44 17 00 00               mov ecx, dword ptr [rbx + 0x1744]
005F487E  40 88 3C 01                     mov byte ptr [rcx + rax], dil
005F4882  8B 83 44 17 00 00               mov eax, dword ptr [rbx + 0x1744]
005F4888  FF C0                           inc eax
005F488A  89 83 44 17 00 00               mov dword ptr [rbx + 0x1744], eax
005F4890  49 2B D5                        sub rdx, r13
005F4893  75 DC                           jne 0x1405f4871
005F4895  8B C8                           mov ecx, eax
005F4897  48 8B 83 38 17 00 00            mov rax, qword ptr [rbx + 0x1738]
005F489E  44 88 04 01                     mov byte ptr [rcx + rax], r8b
005F48A2  44 01 AB 44 17 00 00            add dword ptr [rbx + 0x1744], r13d
005F48A9  66 46 01 AC 83 0C 01 00 00      add word ptr [rbx + r8*4 + 0x10c], r13w
005F48B2  8B 83 48 17 00 00               mov eax, dword ptr [rbx + 0x1748]
005F48B8  39 83 44 17 00 00               cmp dword ptr [rbx + 0x1744], eax
005F48BE  75 41                           jne 0x1405f4901
005F48C0  8B 83 D4 00 00 00               mov eax, dword ptr [rbx + 0xd4]
005F48C6  85 C0                           test eax, eax
005F48C8  78 0B                           js 0x1405f48d5
005F48CA  8B D0                           mov edx, eax
005F48CC  48 03 93 A0 00 00 00            add rdx, qword ptr [rbx + 0xa0]
005F48D3  EB 03                           jmp 0x1405f48d8
005F48D5  48 8B D7                        mov rdx, rdi
005F48D8  44 8B 83 E4 00 00 00            mov r8d, dword ptr [rbx + 0xe4]
005F48DF  45 33 C9                        xor r9d, r9d
005F48E2  44 2B C0                        sub r8d, eax
005F48E5  48 8B CB                        mov rcx, rbx
005F48E8  E8 0B C2 00 00                  call 0x140600af8
005F48ED  8B 83 E4 00 00 00               mov eax, dword ptr [rbx + 0xe4]
005F48F3  48 8B 0B                        mov rcx, qword ptr [rbx]
005F48F6  89 83 D4 00 00 00               mov dword ptr [rbx + 0xd4], eax
005F48FC  E8 57 09 00 00                  call 0x1405f5258
005F4901  44 01 AB E4 00 00 00            add dword ptr [rbx + 0xe4], r13d
005F4908  FF 8B EC 00 00 00               dec dword ptr [rbx + 0xec]
005F490E  48 8B 03                        mov rax, qword ptr [rbx]
005F4911  39 78 18                        cmp dword ptr [rax + 0x18], edi
005F4914  75 31                           jne 0x1405f4947
005F4916  33 C0                           xor eax, eax
005F4918  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
005F491D  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
005F4922  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
005F4927  48 83 C4 20                     add rsp, 0x20
005F492B  41 5F                           pop r15
005F492D  41 5E                           pop r14
005F492F  41 5D                           pop r13
005F4931  41 5C                           pop r12
005F4933  5F                              pop rdi
005F4934  C3                              ret
005F4935  CC                              int3
005F4936  FF C0                           inc eax
005F4938  44 89 AB E0 00 00 00            mov dword ptr [rbx + 0xe0], r13d
005F493F  FF 8B EC 00 00 00               dec dword ptr [rbx + 0xec]
005F4945  89 06                           mov dword ptr [rsi], eax
005F4947  4C 8B F6                        mov r14, rsi
005F494A  E9 19 FB FF FF                  jmp 0x1405f4468
005F494F  39 BB E0 00 00 00               cmp dword ptr [rbx + 0xe0], edi
005F4955  74 63                           je 0x1405f49ba
005F4957  41 8B 0E                        mov ecx, dword ptr [r14]
005F495A  48 8B D5                        mov rdx, rbp
005F495D  48 8B 83 A0 00 00 00            mov rax, qword ptr [rbx + 0xa0]
005F4964  41 2B CD                        sub ecx, r13d
005F4967  44 0F B6 04 01                  movzx r8d, byte ptr [rcx + rax]
005F496C  48 8B 83 38 17 00 00            mov rax, qword ptr [rbx + 0x1738]
005F4973  8B 8B 44 17 00 00               mov ecx, dword ptr [rbx + 0x1744]
005F4979  40 88 3C 01                     mov byte ptr [rcx + rax], dil
005F497D  8B 83 44 17 00 00               mov eax, dword ptr [rbx + 0x1744]
005F4983  FF C0                           inc eax
005F4985  89 83 44 17 00 00               mov dword ptr [rbx + 0x1744], eax
005F498B  49 2B D5                        sub rdx, r13
005F498E  75 DC                           jne 0x1405f496c
005F4990  8B C8                           mov ecx, eax
005F4992  4C 8D B3 E4 00 00 00            lea r14, [rbx + 0xe4]
005F4999  48 8B 83 38 17 00 00            mov rax, qword ptr [rbx + 0x1738]
005F49A0  44 88 04 01                     mov byte ptr [rcx + rax], r8b
005F49A4  44 01 AB 44 17 00 00            add dword ptr [rbx + 0x1744], r13d
005F49AB  66 46 01 AC 83 0C 01 00 00      add word ptr [rbx + r8*4 + 0x10c], r13w
005F49B4  89 BB E0 00 00 00               mov dword ptr [rbx + 0xe0], edi
005F49BA  45 8B 06                        mov r8d, dword ptr [r14]
005F49BD  8B C5                           mov eax, ebp
005F49BF  44 3B C5                        cmp r8d, ebp
005F49C2  41 0F 42 C0                     cmovb eax, r8d
005F49C6  89 83 58 17 00 00               mov dword ptr [rbx + 0x1758], eax
005F49CC  41 83 FC 04                     cmp r12d, 4
005F49D0  75 48                           jne 0x1405f4a1a
005F49D2  8B 83 D4 00 00 00               mov eax, dword ptr [rbx + 0xd4]
005F49D8  85 C0                           test eax, eax
005F49DA  78 09                           js 0x1405f49e5
005F49DC  8B F8                           mov edi, eax
005F49DE  48 03 BB A0 00 00 00            add rdi, qword ptr [rbx + 0xa0]
005F49E5  44 2B C0                        sub r8d, eax
005F49E8  45 8B CD                        mov r9d, r13d
005F49EB  48 8B D7                        mov rdx, rdi
005F49EE  48 8B CB                        mov rcx, rbx
005F49F1  E8 02 C1 00 00                  call 0x140600af8
005F49F6  41 8B 06                        mov eax, dword ptr [r14]
005F49F9  48 8B 0B                        mov rcx, qword ptr [rbx]
005F49FC  89 83 D4 00 00 00               mov dword ptr [rbx + 0xd4], eax
005F4A02  E8 51 08 00 00                  call 0x1405f5258
005F4A07  48 8B 03                        mov rax, qword ptr [rbx]
005F4A0A  8B 48 18                        mov ecx, dword ptr [rax + 0x18]
005F4A0D  F7 D9                           neg ecx
005F4A0F  1B C0                           sbb eax, eax
005F4A11  F7 D8                           neg eax
005F4A13  03 C5                           add eax, ebp
005F4A15  E9 FE FE FF FF                  jmp 0x1405f4918
005F4A1A  39 BB 44 17 00 00               cmp dword ptr [rbx + 0x1744], edi
005F4A20  74 43                           je 0x1405f4a65
005F4A22  8B 83 D4 00 00 00               mov eax, dword ptr [rbx + 0xd4]
005F4A28  85 C0                           test eax, eax
005F4A2A  78 0B                           js 0x1405f4a37
005F4A2C  8B D0                           mov edx, eax
005F4A2E  48 03 93 A0 00 00 00            add rdx, qword ptr [rbx + 0xa0]
005F4A35  EB 03                           jmp 0x1405f4a3a
005F4A37  48 8B D7                        mov rdx, rdi
005F4A3A  44 2B C0                        sub r8d, eax
005F4A3D  45 33 C9                        xor r9d, r9d
005F4A40  48 8B CB                        mov rcx, rbx
005F4A43  E8 B0 C0 00 00                  call 0x140600af8
005F4A48  41 8B 06                        mov eax, dword ptr [r14]
005F4A4B  48 8B 0B                        mov rcx, qword ptr [rbx]
005F4A4E  89 83 D4 00 00 00               mov dword ptr [rbx + 0xd4], eax
005F4A54  E8 FF 07 00 00                  call 0x1405f5258
005F4A59  48 8B 03                        mov rax, qword ptr [rbx]
005F4A5C  39 78 18                        cmp dword ptr [rax + 0x18], edi
005F4A5F  0F 84 B1 FE FF FF               je 0x1405f4916
005F4A65  41 8B C5                        mov eax, r13d
005F4A68  E9 AB FE FF FF                  jmp 0x1405f4918
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall deflate_slow(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (32);
    v_rdi = 0;
loc_005F4468:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 236)))) >= 262) goto loc_005F44A5;
    result = fill_window(a1, a2, a3, a4);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 236)))) >= 262) goto loc_005F449A;
    if ((unsigned int)((unsigned int)(a2)) == 0) goto loc_005F4916;
loc_005F449A:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 236))) == 0) goto loc_005F494F;
loc_005F44A5:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 236)))) < 3) goto loc_005F4581;
    if ((*(unsigned int *)(v_rip + 8861322)) == 0) goto loc_005F4511;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int16 *)(a1 + 228) + *(unsigned __int64 *)(a1 + 160) * 1))))) & (0xFFFFFFULL));
    if ((*(unsigned int *)(a1 + 252)) < 6) { a1 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int16 *)(a1 + 228) + *(unsigned __int64 *)(a1 + 160) * 1))); }
    a1 = (0) & ((unsigned int)(*(unsigned int *)(a1 + 204)));
    *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 184) + a1 * 2) = (unsigned __int16)(*(unsigned __int16 *)(a1 + 228));
    a1 = ((unsigned int)(*(unsigned int *)(a1 + 156))) & (*(unsigned __int16 *)(a1 + 228));
    *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 176) + a1 * 2) = (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 184) + a1 * 2));
    goto loc_005F457E;
loc_005F4511:
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 192))) << ((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 208)))));
    a2 = ((unsigned int)(*(unsigned int *)(a1 + 156))) & (*(unsigned __int16 *)(a1 + 228));
    a3 = (unsigned int)((a3) ^ ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int16 *)(a1 + 228) + *(unsigned __int64 *)(a1 + 176) * 1 + 2))));
    a3 = (unsigned int)((a3) & (*(unsigned int *)(a1 + 204)));
    *(unsigned int *)(a1 + 192) = (unsigned int)(a3);
    *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 176) + a2 * 2) = (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 184) + a3 * 2));
    a1 = ((unsigned int)(*(unsigned int *)(a1 + 156))) & (*(unsigned __int16 *)(a1 + 228));
    *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 184) + (unsigned int)(*(unsigned int *)(a1 + 192)) * 2) = (unsigned __int16)(*(unsigned __int16 *)(a1 + 228));
loc_005F457E:
loc_005F4581:
    *(unsigned int *)(a1 + 240) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 216)));
    *(unsigned int *)(a1 + 220) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 232)));
    *(unsigned int *)(a1 + 216) = (unsigned int)(v_rdi + 2);
    if ((unsigned int)((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 176) + a1 * 2))) == 0) goto loc_005F4603;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 216)))) >= (*(unsigned int *)(a1 + 248))) goto loc_005F4603;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 148))) - (262));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 228))) - ((unsigned int)((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 176) + a1 * 2)))));
    if (((unsigned int)(result)) > ((unsigned int)(a1))) goto loc_005F4603;
    result = longest_match(a1, (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 176) + a1 * 2)), (unsigned int)((unsigned int)(v_rdi + 2)), *(unsigned __int16 *)(a1 + 228));
    *(unsigned int *)(a1 + 216) = (unsigned int)(result);
    if (((unsigned int)(result)) > 5) goto loc_005F4603;
    if ((*(unsigned int *)(a1 + 256)) == ((unsigned int)(v_rdi + 1))) goto loc_005F45FA;
    if (((unsigned int)(result)) != 3) goto loc_005F4603;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 228))) - (*(unsigned int *)(a1 + 232)));
    if (((unsigned int)(a1)) >= = 0x1000ULL) {
        *(unsigned int *)(a1 + 216) = (unsigned int)(v_rdi + 2);
        a3 = (unsigned int)(v_rdi + 2);
    }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 240)))) < 3) goto loc_005F484A;
    if (((unsigned int)(a3)) > ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 240))))) goto loc_005F484A;
    a4 = (unsigned __int16)((*(unsigned __int16 *)(a1 + 228)) - (*(unsigned __int16 *)(a1 + 220)));
    a3 = (unsigned __int8)(((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 240)))) - (3));
    a4 = (unsigned __int16)((a4) - ((unsigned __int16)(v_rdi + 1)));
    v_rbp = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 236))) + (-3));
    v_rbp = (unsigned int)((v_rbp) + (*(unsigned int *)(a1 + 228)));
    *(unsigned __int8 *)((unsigned int)(*(unsigned int *)(a1 + 5956)) + *(unsigned __int64 *)(a1 + 5944) * 1) = (unsigned __int8)(a4);
    a1 = (unsigned __int16)(((unsigned __int16)(a4)) >> (8));
    *(unsigned __int8 *)((unsigned int)(*(unsigned int *)(a1 + 5956)) + *(unsigned __int64 *)(a1 + 5944) * 1) = (unsigned __int8)(a1);
    *(unsigned __int8 *)((unsigned int)(*(unsigned int *)(a1 + 5956)) + *(unsigned __int64 *)(a1 + 5944) * 1) = (unsigned __int8)(a3);
    a4 = (unsigned __int16)((a4) + ((unsigned __int16)((unsigned int)(0xFFFFULL))));
    if (((unsigned __int16)(a4)) >= 256) goto loc_005F46CC;
    goto loc_005F46D7;
loc_005F46CC:
    result = ((unsigned __int16)(a4)) >> (7);
loc_005F46D7:
    result = (result) + (v_rip - 6021303);
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rdi + 1))) - ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 240)))));
    *(unsigned int *)(a1 + 240) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 240)) - 2);
loc_005F470E:
    if ((*(unsigned int *)(a1 + 228)) > ((unsigned int)(v_rbp))) goto loc_005F47D3;
    if ((*(unsigned int *)(v_rip + 8860705)) == 0) goto loc_005F477A;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int16 *)(a1 + 228) + *(unsigned __int64 *)(a1 + 160) * 1))))) & (0xFFFFFFULL));
    if ((*(unsigned int *)(a1 + 252)) < 6) { a1 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int16 *)(a1 + 228) + *(unsigned __int64 *)(a1 + 160) * 1))); }
    a1 = (0) & ((unsigned int)(*(unsigned int *)(a1 + 204)));
    *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 184) + a1 * 2) = (unsigned __int16)(*(unsigned __int16 *)(a1 + 228));
    a1 = ((unsigned int)(*(unsigned int *)(a1 + 156))) & (*(unsigned __int16 *)(a1 + 228));
    *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 176) + a1 * 2) = (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 184) + a1 * 2));
    goto loc_005F47D3;
loc_005F477A:
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 192))) << ((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 208)))));
    a3 = (unsigned int)((a3) ^ ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int16 *)(a1 + 228) + *(unsigned __int64 *)(a1 + 176) * 1 + 2))));
    a3 = (unsigned int)((a3) & (*(unsigned int *)(a1 + 204)));
    a2 = ((unsigned int)(*(unsigned int *)(a1 + 156))) & (*(unsigned __int16 *)(a1 + 228));
    *(unsigned int *)(a1 + 192) = (unsigned int)(a3);
    *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 176) + a2 * 2) = (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 184) + a3 * 2));
    *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 184) + (unsigned int)(*(unsigned int *)(a1 + 192)) * 2) = (unsigned __int16)(*(unsigned __int16 *)(a1 + 228));
loc_005F47D3:
    if (condition_is_not_equal) goto loc_005F470E;
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 228))) + 1);
    *(unsigned int *)(a1 + 224) = 0;
    *(unsigned int *)(a1 + 216) = 2;
    *(unsigned int *)(a1 + 228) = (unsigned int)(a3);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 5956)))) != ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 5960))))) goto loc_005F4947;
    if (sign_flag) goto loc_005F4820;
    a2 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 212))))) + (*(unsigned __int64 *)(a1 + 160));
    goto loc_005F4823;
loc_005F4820:
loc_005F4823:
    a3 = (unsigned int)((a3) - ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 212)))));
    a4 = 0;
    result = tr_flush_block(a1, 0, a3, a4);
    *(unsigned int *)(a1 + 212) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 228)));
    result = flush_pending(*(unsigned __int64 *)(a1), 0, a3, a4);
    goto loc_005F490E;
loc_005F484A:
    if ((*(unsigned int *)(a1 + 224)) == 0) goto loc_005F4936;
loc_005F4871:
    *(unsigned __int8 *)((unsigned int)(*(unsigned int *)(a1 + 5956)) + *(unsigned __int64 *)(a1 + 5944) * 1) = 0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 5956))) + 1);
    *(unsigned int *)(a1 + 5956) = (unsigned int)(result);
    a2 = (2) - (v_rdi + 1);
    if (condition_is_not_equal) goto loc_005F4871;
    *(unsigned __int8 *)((unsigned int)((unsigned int)(result)) + *(unsigned __int64 *)(a1 + 5944) * 1) = (unsigned __int8)(*(unsigned __int8 *)((unsigned int)(*(unsigned int *)(a1 + 228)) - 1 + *(unsigned __int64 *)(a1 + 160) * 1));
    if ((*(unsigned int *)(a1 + 5956)) != ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 5960))))) goto loc_005F4901;
    if (sign_flag) goto loc_005F48D5;
    a2 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 212))))) + (*(unsigned __int64 *)(a1 + 160));
    goto loc_005F48D8;
loc_005F48D5:
loc_005F48D8:
    a4 = 0;
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 228))) - ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 212)))));
    result = tr_flush_block(a1, 0, a3, a4);
    *(unsigned int *)(a1 + 212) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 228)));
    result = flush_pending(*(unsigned __int64 *)(a1), 0, a3, a4);
loc_005F4901:
loc_005F490E:
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1) + 24)) != 0) goto loc_005F4947;
loc_005F4916:
    result = 0;
loc_005F4918:
    v_rsp = (v_rsp) + (32);
    return result;
loc_005F4936:
    result = (unsigned int)((result) + 1);
    *(unsigned int *)(v_stack_p8 + 224) = (unsigned int)(v_rdi + 1);
    *(unsigned int *)(v_stack_p18) = (unsigned int)(result);
loc_005F4947:
    goto loc_005F4468;
loc_005F494F:
    if ((*(unsigned int *)(v_stack_p8 + 224)) == 0) goto loc_005F49BA;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p18))) - ((unsigned int)(v_rdi + 1)));
loc_005F496C:
    *(unsigned __int8 *)((unsigned int)(*(unsigned int *)(v_stack_p8 + 5956)) + *(unsigned __int64 *)(v_stack_p8 + 5944) * 1) = 0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p8 + 5956))) + 1);
    *(unsigned int *)(v_stack_p8 + 5956) = (unsigned int)(result);
    a2 = (v_stack_p10) - (v_rdi + 1);
    if (condition_is_not_equal) goto loc_005F496C;
    *(unsigned __int8 *)((unsigned int)((unsigned int)(result)) + *(unsigned __int64 *)(v_stack_p8 + 5944) * 1) = (unsigned __int8)(*(unsigned __int8 *)(a1 + *(unsigned __int64 *)(v_stack_p8 + 160) * 1));
    *(unsigned int *)(v_stack_p8 + 224) = 0;
loc_005F49BA:
    result = (unsigned int)((unsigned int)(v_stack_p10));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 228)))) < ((unsigned int)(v_stack_p10))) { result = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 228))); }
    *(unsigned int *)(v_stack_p8 + 5976) = (unsigned int)(result);
    if (((unsigned int)((unsigned int)(a2))) != 4) goto loc_005F4A1A;
    if (!(sign_flag)) {
        v_rdi = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 212)));
        v_rdi = (v_rdi) + (*(unsigned __int64 *)(v_stack_p8 + 160));
    }
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p8 + 228))) - ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 212)))));
    result = tr_flush_block(v_stack_p8, v_rdi, a3, (unsigned int)((unsigned int)(v_rdi + 1)));
    *(unsigned int *)(v_stack_p8 + 212) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 228)));
    result = flush_pending(*(unsigned __int64 *)(v_stack_p8), v_rdi, a3, (unsigned int)((unsigned int)(v_rdi + 1)));
    a1 = (unsigned int)(-((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p8) + 24))));
    result = (unsigned int)(-(*(unsigned __int64 *)(v_stack_p8)));
    result = (unsigned int)((result) + ((unsigned int)(v_stack_p10)));
    goto loc_005F4918;
loc_005F4A1A:
    if ((*(unsigned int *)(v_stack_p8 + 5956)) == ((unsigned int)(v_rdi))) goto loc_005F4A65;
    if (sign_flag) goto loc_005F4A37;
    a2 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 212))))) + (*(unsigned __int64 *)(v_stack_p8 + 160));
    goto loc_005F4A3A;
loc_005F4A37:
loc_005F4A3A:
    a3 = (unsigned int)((a3) - ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 212)))));
    a4 = 0;
    result = tr_flush_block(v_stack_p8, v_rdi, a3, a4);
    *(unsigned int *)(v_stack_p8 + 212) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 228)));
    result = flush_pending(*(unsigned __int64 *)(v_stack_p8), v_rdi, a3, a4);
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_stack_p8) + 24)) == ((unsigned int)(v_rdi))) goto loc_005F4916;
loc_005F4A65:
    goto loc_005F4918;
}
```

## 5. (Beta) C Style

```c
int64_t deflate_slow(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (32);
    local_rdi = 0;
loc_005F4468:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xEC)))) >= 262) goto loc_005F44A5;
    result = fill_window(Arg1, Arg2, a3, a4);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xEC)))) >= 262) goto loc_005F449A;
    if ((uint32_t)((uint32_t)(Arg2)) == 0) goto loc_005F4916;
loc_005F449A:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xEC))) == 0) goto loc_005F494F;
loc_005F44A5:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xEC)))) < 3) goto loc_005F4581;
    if ((*(uint32_t *)(v_rip + 0x87368A)) == 0) goto loc_005F4511;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint16_t *)(arg1 + 0xE4) + *(uint64_t *)(arg1 + 0xA0) * 1))))) & (0xFFFFFFULL));
    if ((*(uint32_t *)(arg1 + 0xFC)) < 6) { Arg1 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint16_t *)(arg1 + 0xE4) + *(uint64_t *)(arg1 + 0xA0) * 1))); }
    Arg1 = (0) & ((uint32_t)(*(uint32_t *)(arg1 + 0xCC)));
    *(uint16_t *)(*(uint64_t *)(arg1 + 0xB8) + arg1 * 2) = (uint16_t)(*(uint16_t *)(arg1 + 0xE4));
    Arg1 = ((uint32_t)(*(uint32_t *)(arg1 + 0x9C))) & (*(uint16_t *)(arg1 + 0xE4));
    *(uint16_t *)(*(uint64_t *)(arg1 + 0xB0) + arg1 * 2) = (uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0xB8) + arg1 * 2));
    goto loc_005F457E;
loc_005F4511:
    a3 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0xC0))) << ((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0xD0)))));
    Arg2 = ((uint32_t)(*(uint32_t *)(arg1 + 0x9C))) & (*(uint16_t *)(arg1 + 0xE4));
    a3 = (uint32_t)((a3) ^ ((uint32_t)(*(uint8_t *)(*(uint16_t *)(arg1 + 0xE4) + *(uint64_t *)(arg1 + 0xB0) * 1 + 0x2))));
    a3 = (uint32_t)((a3) & (*(uint32_t *)(arg1 + 0xCC)));
    *(uint32_t *)(arg1 + 0xC0) = (uint32_t)(a3);
    *(uint16_t *)(*(uint64_t *)(arg1 + 0xB0) + Arg2 * 2) = (uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0xB8) + a3 * 2));
    Arg1 = ((uint32_t)(*(uint32_t *)(arg1 + 0x9C))) & (*(uint16_t *)(arg1 + 0xE4));
    *(uint16_t *)(*(uint64_t *)(arg1 + 0xB8) + (uint32_t)(*(uint32_t *)(arg1 + 0xC0)) * 2) = (uint16_t)(*(uint16_t *)(arg1 + 0xE4));
loc_005F457E:
loc_005F4581:
    *(uint32_t *)(arg1 + 0xF0) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xD8)));
    *(uint32_t *)(arg1 + 0xDC) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xE8)));
    *(uint32_t *)(arg1 + 0xD8) = (uint32_t)(local_rdi + 2);
    if ((uint32_t)((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0xB0) + arg1 * 2))) == 0) goto loc_005F4603;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xD8)))) >= (*(uint32_t *)(arg1 + 0xF8))) goto loc_005F4603;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x94))) - (262));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0xE4))) - ((uint32_t)((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0xB0) + arg1 * 2)))));
    if (((uint32_t)(result)) > ((uint32_t)(Arg1))) goto loc_005F4603;
    result = longest_match(Arg1, (uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0xB0) + arg1 * 2)), (uint32_t)((uint32_t)(local_rdi + 2)), *(uint16_t *)(arg1 + 0xE4));
    *(uint32_t *)(arg1 + 0xD8) = (uint32_t)(result);
    if (((uint32_t)(result)) > 5) goto loc_005F4603;
    if ((*(uint32_t *)(arg1 + 0x100)) == ((uint32_t)(local_rdi + 1))) goto loc_005F45FA;
    if (((uint32_t)(result)) != 3) goto loc_005F4603;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0xE4))) - (*(uint32_t *)(arg1 + 0xE8)));
    if (((uint32_t)(Arg1)) >= = 0x1000ULL) {
        *(uint32_t *)(arg1 + 0xD8) = (uint32_t)(local_rdi + 2);
        a3 = (uint32_t)(local_rdi + 2);
    }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xF0)))) < 3) goto loc_005F484A;
    if (((uint32_t)(a3)) > ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xF0))))) goto loc_005F484A;
    a4 = (uint16_t)((*(uint16_t *)(arg1 + 0xE4)) - (*(uint16_t *)(arg1 + 0xDC)));
    a3 = (uint8_t)(((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0xF0)))) - (3));
    a4 = (uint16_t)((a4) - ((uint16_t)(local_rdi + 1)));
    local_rbp = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0xEC))) + (-3));
    local_rbp = (uint32_t)((local_rbp) + (*(uint32_t *)(arg1 + 0xE4)));
    *(uint8_t *)((uint32_t)(*(uint32_t *)(arg1 + 0x1744)) + *(uint64_t *)(arg1 + 0x1738) * 1) = (uint8_t)(a4);
    Arg1 = (uint16_t)(((uint16_t)(a4)) >> (8));
    *(uint8_t *)((uint32_t)(*(uint32_t *)(arg1 + 0x1744)) + *(uint64_t *)(arg1 + 0x1738) * 1) = (uint8_t)(Arg1);
    *(uint8_t *)((uint32_t)(*(uint32_t *)(arg1 + 0x1744)) + *(uint64_t *)(arg1 + 0x1738) * 1) = (uint8_t)(a3);
    a4 = (uint16_t)((a4) + ((uint16_t)((uint32_t)(0xFFFFULL))));
    if (((uint16_t)(a4)) >= 256) goto loc_005F46CC;
    goto loc_005F46D7;
loc_005F46CC:
    result = ((uint16_t)(a4)) >> (7);
loc_005F46D7:
    result = (result) + (v_rip - 6021303);
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rdi + 1))) - ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xF0)))));
    *(uint32_t *)(arg1 + 0xF0) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xF0)) - 2);
loc_005F470E:
    if ((*(uint32_t *)(arg1 + 0xE4)) > ((uint32_t)(local_rbp))) goto loc_005F47D3;
    if ((*(uint32_t *)(v_rip + 0x873421)) == 0) goto loc_005F477A;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint16_t *)(arg1 + 0xE4) + *(uint64_t *)(arg1 + 0xA0) * 1))))) & (0xFFFFFFULL));
    if ((*(uint32_t *)(arg1 + 0xFC)) < 6) { Arg1 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint16_t *)(arg1 + 0xE4) + *(uint64_t *)(arg1 + 0xA0) * 1))); }
    Arg1 = (0) & ((uint32_t)(*(uint32_t *)(arg1 + 0xCC)));
    *(uint16_t *)(*(uint64_t *)(arg1 + 0xB8) + arg1 * 2) = (uint16_t)(*(uint16_t *)(arg1 + 0xE4));
    Arg1 = ((uint32_t)(*(uint32_t *)(arg1 + 0x9C))) & (*(uint16_t *)(arg1 + 0xE4));
    *(uint16_t *)(*(uint64_t *)(arg1 + 0xB0) + arg1 * 2) = (uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0xB8) + arg1 * 2));
    goto loc_005F47D3;
loc_005F477A:
    a3 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0xC0))) << ((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0xD0)))));
    a3 = (uint32_t)((a3) ^ ((uint32_t)(*(uint8_t *)(*(uint16_t *)(arg1 + 0xE4) + *(uint64_t *)(arg1 + 0xB0) * 1 + 0x2))));
    a3 = (uint32_t)((a3) & (*(uint32_t *)(arg1 + 0xCC)));
    Arg2 = ((uint32_t)(*(uint32_t *)(arg1 + 0x9C))) & (*(uint16_t *)(arg1 + 0xE4));
    *(uint32_t *)(arg1 + 0xC0) = (uint32_t)(a3);
    *(uint16_t *)(*(uint64_t *)(arg1 + 0xB0) + Arg2 * 2) = (uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0xB8) + a3 * 2));
    *(uint16_t *)(*(uint64_t *)(arg1 + 0xB8) + (uint32_t)(*(uint32_t *)(arg1 + 0xC0)) * 2) = (uint16_t)(*(uint16_t *)(arg1 + 0xE4));
loc_005F47D3:
    if (condition_is_not_equal) goto loc_005F470E;
    a3 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0xE4))) + 1);
    *(uint32_t *)(arg1 + 0xE0) = 0;
    *(uint32_t *)(arg1 + 0xD8) = 2;
    *(uint32_t *)(arg1 + 0xE4) = (uint32_t)(a3);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1744)))) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1748))))) goto loc_005F4947;
    if (sign_flag) goto loc_005F4820;
    Arg2 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xD4))))) + (*(uint64_t *)(arg1 + 0xA0));
    goto loc_005F4823;
loc_005F4820:
loc_005F4823:
    a3 = (uint32_t)((a3) - ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xD4)))));
    a4 = 0;
    result = tr_flush_block(Arg1, 0, a3, a4);
    *(uint32_t *)(arg1 + 0xD4) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xE4)));
    result = flush_pending(*(uint64_t *)(arg1), 0, a3, a4);
    goto loc_005F490E;
loc_005F484A:
    if ((*(uint32_t *)(arg1 + 0xE0)) == 0) goto loc_005F4936;
loc_005F4871:
    *(uint8_t *)((uint32_t)(*(uint32_t *)(arg1 + 0x1744)) + *(uint64_t *)(arg1 + 0x1738) * 1) = 0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x1744))) + 1);
    *(uint32_t *)(arg1 + 0x1744) = (uint32_t)(result);
    Arg2 = (2) - (local_rdi + 1);
    if (condition_is_not_equal) goto loc_005F4871;
    *(uint8_t *)((uint32_t)((uint32_t)(result)) + *(uint64_t *)(arg1 + 0x1738) * 1) = (uint8_t)(*(uint8_t *)((uint32_t)(*(uint32_t *)(arg1 + 0xE4)) - 0x1 + *(uint64_t *)(arg1 + 0xA0) * 1));
    if ((*(uint32_t *)(arg1 + 0x1744)) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1748))))) goto loc_005F4901;
    if (sign_flag) goto loc_005F48D5;
    Arg2 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xD4))))) + (*(uint64_t *)(arg1 + 0xA0));
    goto loc_005F48D8;
loc_005F48D5:
loc_005F48D8:
    a4 = 0;
    a3 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0xE4))) - ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xD4)))));
    result = tr_flush_block(Arg1, 0, a3, a4);
    *(uint32_t *)(arg1 + 0xD4) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xE4)));
    result = flush_pending(*(uint64_t *)(arg1), 0, a3, a4);
loc_005F4901:
loc_005F490E:
    if ((*(uint32_t *)(*(uint64_t *)(arg1) + 0x18)) != 0) goto loc_005F4947;
loc_005F4916:
    result = 0;
loc_005F4918:
    local_rsp = (local_rsp) + (32);
    return result;
loc_005F4936:
    result = (uint32_t)((result) + 1);
    *(uint32_t *)(v_stack_p8 + 0xE0) = (uint32_t)(local_rdi + 1);
    *(uint32_t *)(v_stack_p18) = (uint32_t)(result);
loc_005F4947:
    goto loc_005F4468;
loc_005F494F:
    if ((*(uint32_t *)(v_stack_p8 + 0xE0)) == 0) goto loc_005F49BA;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p18))) - ((uint32_t)(local_rdi + 1)));
loc_005F496C:
    *(uint8_t *)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x1744)) + *(uint64_t *)(v_stack_p8 + 0x1738) * 1) = 0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x1744))) + 1);
    *(uint32_t *)(v_stack_p8 + 0x1744) = (uint32_t)(result);
    Arg2 = (v_stack_p10) - (local_rdi + 1);
    if (condition_is_not_equal) goto loc_005F496C;
    *(uint8_t *)((uint32_t)((uint32_t)(result)) + *(uint64_t *)(v_stack_p8 + 0x1738) * 1) = (uint8_t)(*(uint8_t *)(arg1 + *(uint64_t *)(v_stack_p8 + 0xA0) * 1));
    *(uint32_t *)(v_stack_p8 + 0xE0) = 0;
loc_005F49BA:
    result = (uint32_t)((uint32_t)(v_stack_p10));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0xE4)))) < ((uint32_t)(v_stack_p10))) { result = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0xE4))); }
    *(uint32_t *)(v_stack_p8 + 0x1758) = (uint32_t)(result);
    if (((uint32_t)((uint32_t)(Arg2))) != 4) goto loc_005F4A1A;
    if (!(sign_flag)) {
        local_rdi = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0xD4)));
        local_rdi = (local_rdi) + (*(uint64_t *)(v_stack_p8 + 0xA0));
    }
    a3 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p8 + 0xE4))) - ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0xD4)))));
    result = tr_flush_block(v_stack_p8, local_rdi, a3, (uint32_t)((uint32_t)(local_rdi + 1)));
    *(uint32_t *)(v_stack_p8 + 0xD4) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0xE4)));
    result = flush_pending(*(uint64_t *)(v_stack_p8), local_rdi, a3, (uint32_t)((uint32_t)(local_rdi + 1)));
    Arg1 = (uint32_t)(-((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p8) + 0x18))));
    result = (uint32_t)(-(*(uint64_t *)(v_stack_p8)));
    result = (uint32_t)((result) + ((uint32_t)(v_stack_p10)));
    goto loc_005F4918;
loc_005F4A1A:
    if ((*(uint32_t *)(v_stack_p8 + 0x1744)) == ((uint32_t)(local_rdi))) goto loc_005F4A65;
    if (sign_flag) goto loc_005F4A37;
    Arg2 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0xD4))))) + (*(uint64_t *)(v_stack_p8 + 0xA0));
    goto loc_005F4A3A;
loc_005F4A37:
loc_005F4A3A:
    a3 = (uint32_t)((a3) - ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0xD4)))));
    a4 = 0;
    result = tr_flush_block(v_stack_p8, local_rdi, a3, a4);
    *(uint32_t *)(v_stack_p8 + 0xD4) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0xE4)));
    result = flush_pending(*(uint64_t *)(v_stack_p8), local_rdi, a3, a4);
    if ((*(uint32_t *)(*(uint64_t *)(v_stack_p8) + 0x18)) == ((uint32_t)(local_rdi))) goto loc_005F4916;
loc_005F4A65:
    goto loc_005F4918;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `16` | `R` |
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x0` | `32` | `R/W` |
| `Arg1` | `+ 0x0` | `32` | `W` |
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x94` | `32` | `R` |
| `Arg1` | `+ 0x9C` | `32` | `R` |
| `Arg1` | `+ 0xA0` | `64` | `R` |
| `Arg1` | `+ 0xB0` | `64` | `R` |
| `Arg1` | `+ 0xB8` | `64` | `R` |
| `Arg1` | `+ 0xC0` | `32` | `R` |
| `Arg1` | `+ 0xC0` | `32` | `W` |
| `Arg1` | `+ 0xCC` | `32` | `R` |
| `Arg1` | `+ 0xD0` | `32` | `R` |
| `Arg1` | `+ 0xD4` | `32` | `R` |
| `Arg1` | `+ 0xD4` | `32` | `W` |
| `Arg1` | `+ 0xD8` | `32` | `R` |
| `Arg1` | `+ 0xD8` | `32` | `W` |
| `Arg1` | `+ 0xDC` | `16` | `R` |
| `Arg1` | `+ 0xDC` | `32` | `W` |
| `Arg1` | `+ 0xE0` | `32` | `R` |
| `Arg1` | `+ 0xE0` | `32` | `W` |
| `Arg1` | `+ 0xE4` | `32` | `R` |
| `Arg1` | `+ 0xE4` | `32` | `R/W` |
| `Arg1` | `+ 0xE4` | `32` | `W` |
| `Arg1` | `+ 0xE4` | `64` | `R` |
| `Arg1` | `+ 0xE8` | `32` | `R` |
| `Arg1` | `+ 0xEC` | `32` | `R` |
| `Arg1` | `+ 0xEC` | `32` | `R/W` |
| `Arg1` | `+ 0xF0` | `32` | `R` |
| `Arg1` | `+ 0xF0` | `32` | `R/W` |
| `Arg1` | `+ 0xF0` | `32` | `W` |

추가 오프셋 12개는 표에서 생략했습니다.

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005F4430&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
