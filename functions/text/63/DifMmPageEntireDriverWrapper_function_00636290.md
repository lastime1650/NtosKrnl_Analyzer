# DifMmPageEntireDriverWrapper

- RVA: `0x00636290`–`0x006363F1` (길이 `353` bytes)
- VA: `0x0000000140636290`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060130`
- 디코드: `94`개 명령, `353/353` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x006362BF` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x006362E7` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00636315` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0063633C` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00636355` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0063635D` → [MmPageEntireDriver](../../page/A4/MmPageEntireDriver_function_00A4BBB0.md) (function, `0x00A4BBB0`)
- `0x0063638B` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006363B2` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006363CB` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x006362F9` → RVA `0x00F048B8` (`.data`; read)
- `0x00636302` → RVA `0x00F04980` (`.data`; read)
- `0x0063630E` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0063635D` → [MmPageEntireDriver](../../page/A4/MmPageEntireDriver_function_00A4BBB0.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00636290  4C 8B DC                        mov r11, rsp
00636293  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
00636297  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
0063629B  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
0063629F  49 89 7B 20                     mov qword ptr [r11 + 0x20], rdi
006362A3  41 56                           push r14
006362A5  48 83 EC 40                     sub rsp, 0x40
006362A9  33 C0                           xor eax, eax
006362AB  0F 57 C0                        xorps xmm0, xmm0
006362AE  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
006362B3  48 8B E9                        mov rbp, rcx
006362B6  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
006362BA  B9 DA 00 00 00                  mov ecx, 0xda
006362BF  E8 70 F7 E5 FF                  call 0x140495a34
006362C4  48 8B F0                        mov rsi, rax
006362C7  48 85 C0                        test rax, rax
006362CA  0F 84 8A 00 00 00               je 0x14063635a
006362D0  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
006362D3  A8 18                           test al, 0x18
006362D5  74 0C                           je 0x1406362e3
006362D7  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
006362DC  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
006362E1  EB 0E                           jmp 0x1406362f1
006362E3  A8 04                           test al, 4
006362E5  74 0A                           je 0x1406362f1
006362E7  E8 1C D9 E9 FF                  call 0x1404d3c08
006362EC  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
006362F1  40 32 FF                        xor dil, dil
006362F4  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
006362F9  40 38 3D B8 E5 8C 00            cmp byte ptr [rip + 0x8ce5b8], dil
00636300  75 0C                           jne 0x14063630e
00636302  F7 05 74 E6 8C 00 00 08 00 00   test dword ptr [rip + 0x8ce674], 0x800
0063630C  74 13                           je 0x140636321
0063630E  48 8D 0D 6B DB 8C 00            lea rcx, [rip + 0x8cdb6b]
00636315  E8 06 03 BE FF                  call 0x140216620
0063631A  40 8A F8                        mov dil, al
0063631D  84 C0                           test al, al
0063631F  74 39                           je 0x14063635a
00636321  4C 8D 76 20                     lea r14, [rsi + 0x20]
00636325  49 8B 1E                        mov rbx, qword ptr [r14]
00636328  EB 1A                           jmp 0x140636344
0063632A  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063632E  48 85 C0                        test rax, rax
00636331  74 0E                           je 0x140636341
00636333  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00636337  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0063633C  E8 8F 47 08 00                  call 0x1406baad0
00636341  48 8B 1B                        mov rbx, qword ptr [rbx]
00636344  49 3B DE                        cmp rbx, r14
00636347  75 E1                           jne 0x14063632a
00636349  40 84 FF                        test dil, dil
0063634C  74 0C                           je 0x14063635a
0063634E  48 8D 0D 2B DB 8C 00            lea rcx, [rip + 0x8cdb2b]
00636355  E8 26 3B D1 FF                  call 0x140349e80
0063635A  48 8B CD                        mov rcx, rbp
0063635D  E8 4E 58 41 00                  call 0x140a4bbb0
00636362  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00636367  48 85 F6                        test rsi, rsi
0063636A  74 64                           je 0x1406363d0
0063636C  40 32 FF                        xor dil, dil
0063636F  40 38 3D 42 E5 8C 00            cmp byte ptr [rip + 0x8ce542], dil
00636376  75 0C                           jne 0x140636384
00636378  F7 05 FE E5 8C 00 00 08 00 00   test dword ptr [rip + 0x8ce5fe], 0x800
00636382  74 13                           je 0x140636397
00636384  48 8D 0D F5 DA 8C 00            lea rcx, [rip + 0x8cdaf5]
0063638B  E8 90 02 BE FF                  call 0x140216620
00636390  40 8A F8                        mov dil, al
00636393  84 C0                           test al, al
00636395  74 39                           je 0x1406363d0
00636397  48 83 C6 30                     add rsi, 0x30
0063639B  48 8B 1E                        mov rbx, qword ptr [rsi]
0063639E  EB 1A                           jmp 0x1406363ba
006363A0  48 8D 43 F0                     lea rax, [rbx - 0x10]
006363A4  48 85 C0                        test rax, rax
006363A7  74 0E                           je 0x1406363b7
006363A9  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006363AD  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
006363B2  E8 19 47 08 00                  call 0x1406baad0
006363B7  48 8B 1B                        mov rbx, qword ptr [rbx]
006363BA  48 3B DE                        cmp rbx, rsi
006363BD  75 E1                           jne 0x1406363a0
006363BF  40 84 FF                        test dil, dil
006363C2  74 0C                           je 0x1406363d0
006363C4  48 8D 0D B5 DA 8C 00            lea rcx, [rip + 0x8cdab5]
006363CB  E8 B0 3A D1 FF                  call 0x140349e80
006363D0  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
006363D5  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
006363DA  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
006363DF  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
006363E4  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
006363E9  48 83 C4 40                     add rsp, 0x40
006363ED  41 5E                           pop r14
006363EF  C3                              ret
006363F0  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifMmPageEntireDriverWrapper(__int64 a1)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (64);
    result = 0;
    v_stack_m28 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 24) = 0;
    result = DifGetAPIThunkContextById(218, a2, a3, a4);
    if (result == 0) goto loc_0063635A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_006362E3;
    v_stack_m28 = v_stack_p0;
    goto loc_006362F1;
loc_006362E3:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    v_rdi = 0;
    v_stack_m20 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9233848)) != 0) goto loc_0063630E;
    if (((*(unsigned int *)(v_rip + 9234036)) & (0x800ULL)) == 0) goto loc_00636321;
loc_0063630E:
    result = ExAcquireRundownProtection(v_rip + 9231211, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063635A;
loc_00636321:
    goto loc_00636344;
loc_0063632A:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00636344:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0063632A;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9231147;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = MmPageEntireDriver(a1, a2, a3, a4);
    v_stack_m18 = result;
    if (result == 0) goto loc_006363D0;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9233730)) != 0) goto loc_00636384;
    if (((*(unsigned int *)(v_rip + 9233918)) & (0x800ULL)) == 0) goto loc_00636397;
loc_00636384:
    result = ExAcquireRundownProtection(v_rip + 9231093, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006363D0;
loc_00636397:
    v_rsi = (result) + (48);
    goto loc_006363BA;
loc_006363A0:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_006363BA:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_006363A0;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9231029;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return v_stack_m18;
}
```

## 5. (Beta) C Style

```c
int64_t DifMmPageEntireDriverWrapper(int64_t Arg1)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (64);
    result = 0;
    v_stack_m28 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x18) = 0;
    result = DifGetAPIThunkContextById(218, a2, a3, a4);
    if (result == 0) goto loc_0063635A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_006362E3;
    v_stack_m28 = v_stack_p0;
    goto loc_006362F1;
loc_006362E3:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    local_rdi = 0;
    v_stack_m20 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8CE5B8)) != 0) goto loc_0063630E;
    if (((*(uint32_t *)(v_rip + 0x8CE674)) & (0x800ULL)) == 0) goto loc_00636321;
loc_0063630E:
    result = ExAcquireRundownProtection(v_rip + 9231211, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0063635A;
loc_00636321:
    goto loc_00636344;
loc_0063632A:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_00636344:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0063632A;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9231147;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    result = MmPageEntireDriver(Arg1, a2, a3, a4);
    v_stack_m18 = result;
    if (result == 0) goto loc_006363D0;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8CE542)) != 0) goto loc_00636384;
    if (((*(uint32_t *)(v_rip + 0x8CE5FE)) & (0x800ULL)) == 0) goto loc_00636397;
loc_00636384:
    result = ExAcquireRundownProtection(v_rip + 9231093, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_006363D0;
loc_00636397:
    local_rsi = (result) + (48);
    goto loc_006363BA;
loc_006363A0:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_006363BA:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_006363A0;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9231029;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return v_stack_m18;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00636290&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00636290[BB_00636290]
  bb_006362D0[BB_006362D0]
  bb_006362D7[BB_006362D7]
  bb_006362E3[BB_006362E3]
  bb_006362E7[BB_006362E7]
  bb_006362F1[BB_006362F1]
  bb_00636302[BB_00636302]
  bb_0063630E[BB_0063630E]
  bb_00636321[BB_00636321]
  bb_0063632A[BB_0063632A]
  bb_00636333[BB_00636333]
  bb_00636341[BB_00636341]
  bb_00636344[BB_00636344]
  bb_00636349[BB_00636349]
  bb_0063634E[BB_0063634E]
  bb_0063635A[BB_0063635A]
  bb_0063636C[BB_0063636C]
  bb_00636378[BB_00636378]
  bb_00636384[BB_00636384]
  bb_00636397[BB_00636397]
  bb_006363A0[BB_006363A0]
  bb_006363A9[BB_006363A9]
  bb_006363B7[BB_006363B7]
  bb_006363BA[BB_006363BA]
  bb_006363BF[BB_006363BF]
  bb_006363C4[BB_006363C4]
  bb_006363D0[BB_006363D0]
  bb_006363F0[BB_006363F0]
  bb_00636290 -->|branch| bb_0063635A
  bb_00636290 -->|fallthrough| bb_006362D0
  bb_006362D0 -->|branch| bb_006362E3
  bb_006362D0 -->|fallthrough| bb_006362D7
  bb_006362D7 -->|branch| bb_006362F1
  bb_006362E3 -->|branch| bb_006362F1
  bb_006362E3 -->|fallthrough| bb_006362E7
  bb_006362E7 -->|flow| bb_006362F1
  bb_006362F1 -->|branch| bb_0063630E
  bb_006362F1 -->|fallthrough| bb_00636302
  bb_00636302 -->|branch| bb_00636321
  bb_00636302 -->|fallthrough| bb_0063630E
  bb_0063630E -->|branch| bb_0063635A
  bb_0063630E -->|fallthrough| bb_00636321
  bb_00636321 -->|branch| bb_00636344
  bb_0063632A -->|branch| bb_00636341
  bb_0063632A -->|fallthrough| bb_00636333
  bb_00636333 -->|flow| bb_00636341
  bb_00636341 -->|flow| bb_00636344
  bb_00636344 -->|branch| bb_0063632A
  bb_00636344 -->|fallthrough| bb_00636349
  bb_00636349 -->|branch| bb_0063635A
  bb_00636349 -->|fallthrough| bb_0063634E
  bb_0063634E -->|flow| bb_0063635A
  bb_0063635A -->|branch| bb_006363D0
  bb_0063635A -->|fallthrough| bb_0063636C
  bb_0063636C -->|branch| bb_00636384
  bb_0063636C -->|fallthrough| bb_00636378
  bb_00636378 -->|branch| bb_00636397
  bb_00636378 -->|fallthrough| bb_00636384
  bb_00636384 -->|branch| bb_006363D0
  bb_00636384 -->|fallthrough| bb_00636397
  bb_00636397 -->|branch| bb_006363BA
  bb_006363A0 -->|branch| bb_006363B7
  bb_006363A0 -->|fallthrough| bb_006363A9
  bb_006363A9 -->|flow| bb_006363B7
  bb_006363B7 -->|flow| bb_006363BA
  bb_006363BA -->|branch| bb_006363A0
  bb_006363BA -->|fallthrough| bb_006363BF
  bb_006363BF -->|branch| bb_006363D0
  bb_006363BF -->|fallthrough| bb_006363C4
  bb_006363C4 -->|flow| bb_006363D0
```
