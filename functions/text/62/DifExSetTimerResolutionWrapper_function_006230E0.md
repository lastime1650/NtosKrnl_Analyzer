# DifExSetTimerResolutionWrapper

- RVA: `0x006230E0`–`0x00623247` (길이 `359` bytes)
- VA: `0x00000001406230E0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00093E28`
- 디코드: `99`개 명령, `359/359` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00623111` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00623139` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0062316C` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00623193` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006231AC` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x006231B7` → [ExSetTimerResolution](../49/ExSetTimerResolution_function_0049E7D0.md) (function, `0x0049E7D0`)
- `0x006231E4` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062320B` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00623224` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0062314B` → RVA `0x00F048B8` (`.data`; read)
- `0x00623159` → RVA `0x00F04980` (`.data`; read)
- `0x00623165` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006230E0  4C 8B DC                        mov r11, rsp
006230E3  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
006230E7  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
006230EB  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
006230EF  57                              push rdi
006230F0  41 56                           push r14
006230F2  41 57                           push r15
006230F4  48 83 EC 40                     sub rsp, 0x40
006230F8  33 C0                           xor eax, eax
006230FA  0F 57 C0                        xorps xmm0, xmm0
006230FD  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
00623102  44 8B F9                        mov r15d, ecx
00623105  49 89 43 D8                     mov qword ptr [r11 - 0x28], rax
00623109  B9 80 01 00 00                  mov ecx, 0x180
0062310E  44 8A F2                        mov r14b, dl
00623111  E8 1E 29 E7 FF                  call 0x140495a34
00623116  48 8B F0                        mov rsi, rax
00623119  48 85 C0                        test rax, rax
0062311C  0F 84 8F 00 00 00               je 0x1406231b1
00623122  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00623125  A8 18                           test al, 0x18
00623127  74 0C                           je 0x140623135
00623129  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
0062312E  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00623133  EB 0E                           jmp 0x140623143
00623135  A8 04                           test al, 4
00623137  74 0A                           je 0x140623143
00623139  E8 CA 0A EB FF                  call 0x1404d3c08
0062313E  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00623143  40 32 ED                        xor bpl, bpl
00623146  44 89 7C 24 2C                  mov dword ptr [rsp + 0x2c], r15d
0062314B  40 38 2D 66 17 8E 00            cmp byte ptr [rip + 0x8e1766], bpl
00623152  44 88 74 24 28                  mov byte ptr [rsp + 0x28], r14b
00623157  75 0C                           jne 0x140623165
00623159  F7 05 1D 18 8E 00 00 08 00 00   test dword ptr [rip + 0x8e181d], 0x800
00623163  74 13                           je 0x140623178
00623165  48 8D 0D 14 0D 8E 00            lea rcx, [rip + 0x8e0d14]
0062316C  E8 AF 34 BF FF                  call 0x140216620
00623171  40 8A E8                        mov bpl, al
00623174  84 C0                           test al, al
00623176  74 39                           je 0x1406231b1
00623178  48 8D 7E 20                     lea rdi, [rsi + 0x20]
0062317C  48 8B 1F                        mov rbx, qword ptr [rdi]
0062317F  EB 1A                           jmp 0x14062319b
00623181  48 8D 43 F0                     lea rax, [rbx - 0x10]
00623185  48 85 C0                        test rax, rax
00623188  74 0E                           je 0x140623198
0062318A  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062318E  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00623193  E8 38 79 09 00                  call 0x1406baad0
00623198  48 8B 1B                        mov rbx, qword ptr [rbx]
0062319B  48 3B DF                        cmp rbx, rdi
0062319E  75 E1                           jne 0x140623181
006231A0  40 84 ED                        test bpl, bpl
006231A3  74 0C                           je 0x1406231b1
006231A5  48 8D 0D D4 0C 8E 00            lea rcx, [rip + 0x8e0cd4]
006231AC  E8 CF 6C D2 FF                  call 0x140349e80
006231B1  41 8A D6                        mov dl, r14b
006231B4  41 8B CF                        mov ecx, r15d
006231B7  E8 14 B6 E7 FF                  call 0x14049e7d0
006231BC  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
006231C0  48 85 F6                        test rsi, rsi
006231C3  74 64                           je 0x140623229
006231C5  40 32 FF                        xor dil, dil
006231C8  40 38 3D E9 16 8E 00            cmp byte ptr [rip + 0x8e16e9], dil
006231CF  75 0C                           jne 0x1406231dd
006231D1  F7 05 A5 17 8E 00 00 08 00 00   test dword ptr [rip + 0x8e17a5], 0x800
006231DB  74 13                           je 0x1406231f0
006231DD  48 8D 0D 9C 0C 8E 00            lea rcx, [rip + 0x8e0c9c]
006231E4  E8 37 34 BF FF                  call 0x140216620
006231E9  40 8A F8                        mov dil, al
006231EC  84 C0                           test al, al
006231EE  74 39                           je 0x140623229
006231F0  48 83 C6 30                     add rsi, 0x30
006231F4  48 8B 1E                        mov rbx, qword ptr [rsi]
006231F7  EB 1A                           jmp 0x140623213
006231F9  48 8D 43 F0                     lea rax, [rbx - 0x10]
006231FD  48 85 C0                        test rax, rax
00623200  74 0E                           je 0x140623210
00623202  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00623206  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0062320B  E8 C0 78 09 00                  call 0x1406baad0
00623210  48 8B 1B                        mov rbx, qword ptr [rbx]
00623213  48 3B DE                        cmp rbx, rsi
00623216  75 E1                           jne 0x1406231f9
00623218  40 84 FF                        test dil, dil
0062321B  74 0C                           je 0x140623229
0062321D  48 8D 0D 5C 0C 8E 00            lea rcx, [rip + 0x8e0c5c]
00623224  E8 57 6C D2 FF                  call 0x140349e80
00623229  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
0062322D  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
00623232  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
00623237  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
0062323C  48 83 C4 40                     add rsp, 0x40
00623240  41 5F                           pop r15
00623242  41 5E                           pop r14
00623244  5F                              pop rdi
00623245  C3                              ret
00623246  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifExSetTimerResolutionWrapper(int a1, unsigned __int8 a2)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m28;
    unsigned int v_stack_m2C;
    unsigned __int8 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    v_rsp = (v_rsp) - (64);
    result = 0;
    v_stack_m38 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 40) = 0;
    result = DifGetAPIThunkContextById(384, a2, a3, a4);
    if (result == 0) goto loc_006231B1;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00623135;
    v_stack_m38 = v_stack_p0;
    goto loc_00623143;
loc_00623135:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m38 = result;
    }
    v_rbp = 0;
    v_stack_m2C = (unsigned int)((unsigned int)(a1));
    v_stack_m30 = a2;
    if ((*(unsigned __int8 *)(v_rip + 9312102)) != 0) goto loc_00623165;
    if (((*(unsigned int *)(v_rip + 9312285)) & (0x800ULL)) == 0) goto loc_00623178;
loc_00623165:
    result = ExAcquireRundownProtection(v_rip + 9309460, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006231B1;
loc_00623178:
    goto loc_0062319B;
loc_00623181:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062319B:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00623181;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9309396;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ExSetTimerResolution((unsigned int)((unsigned int)((unsigned int)(a1))), a2, a3, a4);
    v_stack_m28 = (unsigned int)(result);
    if (result == 0) goto loc_00623229;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9311977)) != 0) goto loc_006231DD;
    if (((*(unsigned int *)(v_rip + 9312165)) & (0x800ULL)) == 0) goto loc_006231F0;
loc_006231DD:
    result = ExAcquireRundownProtection(v_rip + 9309340, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00623229;
loc_006231F0:
    v_rsi = (result) + (48);
    goto loc_00623213;
loc_006231F9:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00623213:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_006231F9;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9309276;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return (unsigned int)(v_stack_m28);
}
```

## 5. (Beta) C Style

```c
int64_t DifExSetTimerResolutionWrapper(int32_t Arg1, uint8_t Arg2)
{
    int64_t result;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m28;
    uint32_t v_stack_m2C;
    uint8_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    local_rsp = (local_rsp) - (64);
    result = 0;
    v_stack_m38 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x28) = 0;
    result = DifGetAPIThunkContextById(384, Arg2, a3, a4);
    if (result == 0) goto loc_006231B1;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00623135;
    v_stack_m38 = v_stack_p0;
    goto loc_00623143;
loc_00623135:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, a3, a4);
        v_stack_m38 = result;
    }
    local_rbp = 0;
    v_stack_m2C = (uint32_t)((uint32_t)(Arg1));
    v_stack_m30 = Arg2;
    if ((*(uint8_t *)(v_rip + 0x8E1766)) != 0) goto loc_00623165;
    if (((*(uint32_t *)(v_rip + 0x8E181D)) & (0x800ULL)) == 0) goto loc_00623178;
loc_00623165:
    result = ExAcquireRundownProtection(v_rip + 9309460, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_006231B1;
loc_00623178:
    goto loc_0062319B;
loc_00623181:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_0062319B:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00623181;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9309396;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    result = ExSetTimerResolution((uint32_t)((uint32_t)((uint32_t)(Arg1))), Arg2, a3, a4);
    v_stack_m28 = (uint32_t)(result);
    if (result == 0) goto loc_00623229;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8E16E9)) != 0) goto loc_006231DD;
    if (((*(uint32_t *)(v_rip + 0x8E17A5)) & (0x800ULL)) == 0) goto loc_006231F0;
loc_006231DD:
    result = ExAcquireRundownProtection(v_rip + 9309340, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00623229;
loc_006231F0:
    local_rsi = (result) + (48);
    goto loc_00623213;
loc_006231F9:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_00623213:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_006231F9;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9309276;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return (uint32_t)(v_stack_m28);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006230E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006230E0[BB_006230E0]
  bb_00623122[BB_00623122]
  bb_00623129[BB_00623129]
  bb_00623135[BB_00623135]
  bb_00623139[BB_00623139]
  bb_00623143[BB_00623143]
  bb_00623159[BB_00623159]
  bb_00623165[BB_00623165]
  bb_00623178[BB_00623178]
  bb_00623181[BB_00623181]
  bb_0062318A[BB_0062318A]
  bb_00623198[BB_00623198]
  bb_0062319B[BB_0062319B]
  bb_006231A0[BB_006231A0]
  bb_006231A5[BB_006231A5]
  bb_006231B1[BB_006231B1]
  bb_006231C5[BB_006231C5]
  bb_006231D1[BB_006231D1]
  bb_006231DD[BB_006231DD]
  bb_006231F0[BB_006231F0]
  bb_006231F9[BB_006231F9]
  bb_00623202[BB_00623202]
  bb_00623210[BB_00623210]
  bb_00623213[BB_00623213]
  bb_00623218[BB_00623218]
  bb_0062321D[BB_0062321D]
  bb_00623229[BB_00623229]
  bb_00623246[BB_00623246]
  bb_006230E0 -->|branch| bb_006231B1
  bb_006230E0 -->|fallthrough| bb_00623122
  bb_00623122 -->|branch| bb_00623135
  bb_00623122 -->|fallthrough| bb_00623129
  bb_00623129 -->|branch| bb_00623143
  bb_00623135 -->|branch| bb_00623143
  bb_00623135 -->|fallthrough| bb_00623139
  bb_00623139 -->|flow| bb_00623143
  bb_00623143 -->|branch| bb_00623165
  bb_00623143 -->|fallthrough| bb_00623159
  bb_00623159 -->|branch| bb_00623178
  bb_00623159 -->|fallthrough| bb_00623165
  bb_00623165 -->|branch| bb_006231B1
  bb_00623165 -->|fallthrough| bb_00623178
  bb_00623178 -->|branch| bb_0062319B
  bb_00623181 -->|branch| bb_00623198
  bb_00623181 -->|fallthrough| bb_0062318A
  bb_0062318A -->|flow| bb_00623198
  bb_00623198 -->|flow| bb_0062319B
  bb_0062319B -->|branch| bb_00623181
  bb_0062319B -->|fallthrough| bb_006231A0
  bb_006231A0 -->|branch| bb_006231B1
  bb_006231A0 -->|fallthrough| bb_006231A5
  bb_006231A5 -->|flow| bb_006231B1
  bb_006231B1 -->|branch| bb_00623229
  bb_006231B1 -->|fallthrough| bb_006231C5
  bb_006231C5 -->|branch| bb_006231DD
  bb_006231C5 -->|fallthrough| bb_006231D1
  bb_006231D1 -->|branch| bb_006231F0
  bb_006231D1 -->|fallthrough| bb_006231DD
  bb_006231DD -->|branch| bb_00623229
  bb_006231DD -->|fallthrough| bb_006231F0
  bb_006231F0 -->|branch| bb_00623213
  bb_006231F9 -->|branch| bb_00623210
  bb_006231F9 -->|fallthrough| bb_00623202
  bb_00623202 -->|flow| bb_00623210
  bb_00623210 -->|flow| bb_00623213
  bb_00623213 -->|branch| bb_006231F9
  bb_00623213 -->|fallthrough| bb_00623218
  bb_00623218 -->|branch| bb_00623229
  bb_00623218 -->|fallthrough| bb_0062321D
  bb_0062321D -->|flow| bb_00623229
```
