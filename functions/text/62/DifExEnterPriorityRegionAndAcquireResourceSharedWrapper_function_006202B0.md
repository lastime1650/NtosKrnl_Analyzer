# DifExEnterPriorityRegionAndAcquireResourceSharedWrapper

- RVA: `0x006202B0`–`0x00620411` (길이 `353` bytes)
- VA: `0x00000001406202B0`
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
- `0x006202DF` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00620307` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00620335` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062035C` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00620375` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0062037D` → [ExEnterPriorityRegionAndAcquireResourceShared](../21/ExEnterPriorityRegionAndAcquireResourceShared_function_00213870.md) (function, `0x00213870`)
- `0x006203AB` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006203D2` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006203EB` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00620319` → RVA `0x00F048B8` (`.data`; read)
- `0x00620322` → RVA `0x00F04980` (`.data`; read)
- `0x0062032E` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006202B0  4C 8B DC                        mov r11, rsp
006202B3  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
006202B7  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
006202BB  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
006202BF  49 89 7B 20                     mov qword ptr [r11 + 0x20], rdi
006202C3  41 56                           push r14
006202C5  48 83 EC 40                     sub rsp, 0x40
006202C9  33 C0                           xor eax, eax
006202CB  0F 57 C0                        xorps xmm0, xmm0
006202CE  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
006202D3  48 8B E9                        mov rbp, rcx
006202D6  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
006202DA  B9 92 01 00 00                  mov ecx, 0x192
006202DF  E8 50 57 E7 FF                  call 0x140495a34
006202E4  48 8B F0                        mov rsi, rax
006202E7  48 85 C0                        test rax, rax
006202EA  0F 84 8A 00 00 00               je 0x14062037a
006202F0  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
006202F3  A8 18                           test al, 0x18
006202F5  74 0C                           je 0x140620303
006202F7  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
006202FC  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00620301  EB 0E                           jmp 0x140620311
00620303  A8 04                           test al, 4
00620305  74 0A                           je 0x140620311
00620307  E8 FC 38 EB FF                  call 0x1404d3c08
0062030C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00620311  40 32 FF                        xor dil, dil
00620314  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
00620319  40 38 3D 98 45 8E 00            cmp byte ptr [rip + 0x8e4598], dil
00620320  75 0C                           jne 0x14062032e
00620322  F7 05 54 46 8E 00 00 08 00 00   test dword ptr [rip + 0x8e4654], 0x800
0062032C  74 13                           je 0x140620341
0062032E  48 8D 0D 4B 3B 8E 00            lea rcx, [rip + 0x8e3b4b]
00620335  E8 E6 62 BF FF                  call 0x140216620
0062033A  40 8A F8                        mov dil, al
0062033D  84 C0                           test al, al
0062033F  74 39                           je 0x14062037a
00620341  4C 8D 76 20                     lea r14, [rsi + 0x20]
00620345  49 8B 1E                        mov rbx, qword ptr [r14]
00620348  EB 1A                           jmp 0x140620364
0062034A  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062034E  48 85 C0                        test rax, rax
00620351  74 0E                           je 0x140620361
00620353  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00620357  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0062035C  E8 6F A7 09 00                  call 0x1406baad0
00620361  48 8B 1B                        mov rbx, qword ptr [rbx]
00620364  49 3B DE                        cmp rbx, r14
00620367  75 E1                           jne 0x14062034a
00620369  40 84 FF                        test dil, dil
0062036C  74 0C                           je 0x14062037a
0062036E  48 8D 0D 0B 3B 8E 00            lea rcx, [rip + 0x8e3b0b]
00620375  E8 06 9B D2 FF                  call 0x140349e80
0062037A  48 8B CD                        mov rcx, rbp
0062037D  E8 EE 34 BF FF                  call 0x140213870
00620382  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00620387  48 85 F6                        test rsi, rsi
0062038A  74 64                           je 0x1406203f0
0062038C  40 32 FF                        xor dil, dil
0062038F  40 38 3D 22 45 8E 00            cmp byte ptr [rip + 0x8e4522], dil
00620396  75 0C                           jne 0x1406203a4
00620398  F7 05 DE 45 8E 00 00 08 00 00   test dword ptr [rip + 0x8e45de], 0x800
006203A2  74 13                           je 0x1406203b7
006203A4  48 8D 0D D5 3A 8E 00            lea rcx, [rip + 0x8e3ad5]
006203AB  E8 70 62 BF FF                  call 0x140216620
006203B0  40 8A F8                        mov dil, al
006203B3  84 C0                           test al, al
006203B5  74 39                           je 0x1406203f0
006203B7  48 83 C6 30                     add rsi, 0x30
006203BB  48 8B 1E                        mov rbx, qword ptr [rsi]
006203BE  EB 1A                           jmp 0x1406203da
006203C0  48 8D 43 F0                     lea rax, [rbx - 0x10]
006203C4  48 85 C0                        test rax, rax
006203C7  74 0E                           je 0x1406203d7
006203C9  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006203CD  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
006203D2  E8 F9 A6 09 00                  call 0x1406baad0
006203D7  48 8B 1B                        mov rbx, qword ptr [rbx]
006203DA  48 3B DE                        cmp rbx, rsi
006203DD  75 E1                           jne 0x1406203c0
006203DF  40 84 FF                        test dil, dil
006203E2  74 0C                           je 0x1406203f0
006203E4  48 8D 0D 95 3A 8E 00            lea rcx, [rip + 0x8e3a95]
006203EB  E8 90 9A D2 FF                  call 0x140349e80
006203F0  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
006203F5  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
006203FA  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
006203FF  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
00620404  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
00620409  48 83 C4 40                     add rsp, 0x40
0062040D  41 5E                           pop r14
0062040F  C3                              ret
00620410  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifExEnterPriorityRegionAndAcquireResourceSharedWrapper(__int64 a1)
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
    result = DifGetAPIThunkContextById(402, a2, a3, a4);
    if (result == 0) goto loc_0062037A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00620303;
    v_stack_m28 = v_stack_p0;
    goto loc_00620311;
loc_00620303:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    v_rdi = 0;
    v_stack_m20 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9323928)) != 0) goto loc_0062032E;
    if (((*(unsigned int *)(v_rip + 9324116)) & (0x800ULL)) == 0) goto loc_00620341;
loc_0062032E:
    result = ExAcquireRundownProtection(v_rip + 9321291, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062037A;
loc_00620341:
    goto loc_00620364;
loc_0062034A:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00620364:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0062034A;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9321227;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ExEnterPriorityRegionAndAcquireResourceShared(a1, a2, a3, a4);
    v_stack_m18 = result;
    if (result == 0) goto loc_006203F0;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9323810)) != 0) goto loc_006203A4;
    if (((*(unsigned int *)(v_rip + 9323998)) & (0x800ULL)) == 0) goto loc_006203B7;
loc_006203A4:
    result = ExAcquireRundownProtection(v_rip + 9321173, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006203F0;
loc_006203B7:
    v_rsi = (result) + (48);
    goto loc_006203DA;
loc_006203C0:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_006203DA:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_006203C0;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9321109;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return v_stack_m18;
}
```

## 5. (Beta) C Style

```c
int64_t DifExEnterPriorityRegionAndAcquireResourceSharedWrapper(int64_t Arg1)
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
    result = DifGetAPIThunkContextById(402, a2, a3, a4);
    if (result == 0) goto loc_0062037A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00620303;
    v_stack_m28 = v_stack_p0;
    goto loc_00620311;
loc_00620303:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    local_rdi = 0;
    v_stack_m20 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8E4598)) != 0) goto loc_0062032E;
    if (((*(uint32_t *)(v_rip + 0x8E4654)) & (0x800ULL)) == 0) goto loc_00620341;
loc_0062032E:
    result = ExAcquireRundownProtection(v_rip + 9321291, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0062037A;
loc_00620341:
    goto loc_00620364;
loc_0062034A:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_00620364:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0062034A;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9321227;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    result = ExEnterPriorityRegionAndAcquireResourceShared(Arg1, a2, a3, a4);
    v_stack_m18 = result;
    if (result == 0) goto loc_006203F0;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8E4522)) != 0) goto loc_006203A4;
    if (((*(uint32_t *)(v_rip + 0x8E45DE)) & (0x800ULL)) == 0) goto loc_006203B7;
loc_006203A4:
    result = ExAcquireRundownProtection(v_rip + 9321173, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_006203F0;
loc_006203B7:
    local_rsi = (result) + (48);
    goto loc_006203DA;
loc_006203C0:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_006203DA:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_006203C0;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9321109;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return v_stack_m18;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006202B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006202B0[BB_006202B0]
  bb_006202F0[BB_006202F0]
  bb_006202F7[BB_006202F7]
  bb_00620303[BB_00620303]
  bb_00620307[BB_00620307]
  bb_00620311[BB_00620311]
  bb_00620322[BB_00620322]
  bb_0062032E[BB_0062032E]
  bb_00620341[BB_00620341]
  bb_0062034A[BB_0062034A]
  bb_00620353[BB_00620353]
  bb_00620361[BB_00620361]
  bb_00620364[BB_00620364]
  bb_00620369[BB_00620369]
  bb_0062036E[BB_0062036E]
  bb_0062037A[BB_0062037A]
  bb_0062038C[BB_0062038C]
  bb_00620398[BB_00620398]
  bb_006203A4[BB_006203A4]
  bb_006203B7[BB_006203B7]
  bb_006203C0[BB_006203C0]
  bb_006203C9[BB_006203C9]
  bb_006203D7[BB_006203D7]
  bb_006203DA[BB_006203DA]
  bb_006203DF[BB_006203DF]
  bb_006203E4[BB_006203E4]
  bb_006203F0[BB_006203F0]
  bb_00620410[BB_00620410]
  bb_006202B0 -->|branch| bb_0062037A
  bb_006202B0 -->|fallthrough| bb_006202F0
  bb_006202F0 -->|branch| bb_00620303
  bb_006202F0 -->|fallthrough| bb_006202F7
  bb_006202F7 -->|branch| bb_00620311
  bb_00620303 -->|branch| bb_00620311
  bb_00620303 -->|fallthrough| bb_00620307
  bb_00620307 -->|flow| bb_00620311
  bb_00620311 -->|branch| bb_0062032E
  bb_00620311 -->|fallthrough| bb_00620322
  bb_00620322 -->|branch| bb_00620341
  bb_00620322 -->|fallthrough| bb_0062032E
  bb_0062032E -->|branch| bb_0062037A
  bb_0062032E -->|fallthrough| bb_00620341
  bb_00620341 -->|branch| bb_00620364
  bb_0062034A -->|branch| bb_00620361
  bb_0062034A -->|fallthrough| bb_00620353
  bb_00620353 -->|flow| bb_00620361
  bb_00620361 -->|flow| bb_00620364
  bb_00620364 -->|branch| bb_0062034A
  bb_00620364 -->|fallthrough| bb_00620369
  bb_00620369 -->|branch| bb_0062037A
  bb_00620369 -->|fallthrough| bb_0062036E
  bb_0062036E -->|flow| bb_0062037A
  bb_0062037A -->|branch| bb_006203F0
  bb_0062037A -->|fallthrough| bb_0062038C
  bb_0062038C -->|branch| bb_006203A4
  bb_0062038C -->|fallthrough| bb_00620398
  bb_00620398 -->|branch| bb_006203B7
  bb_00620398 -->|fallthrough| bb_006203A4
  bb_006203A4 -->|branch| bb_006203F0
  bb_006203A4 -->|fallthrough| bb_006203B7
  bb_006203B7 -->|branch| bb_006203DA
  bb_006203C0 -->|branch| bb_006203D7
  bb_006203C0 -->|fallthrough| bb_006203C9
  bb_006203C9 -->|flow| bb_006203D7
  bb_006203D7 -->|flow| bb_006203DA
  bb_006203DA -->|branch| bb_006203C0
  bb_006203DA -->|fallthrough| bb_006203DF
  bb_006203DF -->|branch| bb_006203F0
  bb_006203DF -->|fallthrough| bb_006203E4
  bb_006203E4 -->|flow| bb_006203F0
```
