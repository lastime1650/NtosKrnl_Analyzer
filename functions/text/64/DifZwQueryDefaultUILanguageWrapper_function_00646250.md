# DifZwQueryDefaultUILanguageWrapper

- RVA: `0x00646250`–`0x006463AD` (길이 `349` bytes)
- VA: `0x0000000140646250`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060130`
- 디코드: `94`개 명령, `349/349` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0064627D` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x006462A5` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x006462D3` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006462FA` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00646313` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0064631B` → [ZwQueryDefaultUILanguage](../6A/ZwQueryDefaultUILanguage_function_006AD950.md) (function, `0x006AD950`)
- `0x00646348` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0064636F` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00646388` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x006462B7` → RVA `0x00F048B8` (`.data`; read)
- `0x006462C0` → RVA `0x00F04980` (`.data`; read)
- `0x006462CC` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00646250  4C 8B DC                        mov r11, rsp
00646253  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
00646257  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
0064625B  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
0064625F  49 89 7B 20                     mov qword ptr [r11 + 0x20], rdi
00646263  41 56                           push r14
00646265  48 83 EC 40                     sub rsp, 0x40
00646269  33 C0                           xor eax, eax
0064626B  0F 57 C0                        xorps xmm0, xmm0
0064626E  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
00646273  48 8B E9                        mov rbp, rcx
00646276  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
0064627A  8D 48 3A                        lea ecx, [rax + 0x3a]
0064627D  E8 B2 F7 E4 FF                  call 0x140495a34
00646282  48 8B F0                        mov rsi, rax
00646285  48 85 C0                        test rax, rax
00646288  0F 84 8A 00 00 00               je 0x140646318
0064628E  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00646291  A8 18                           test al, 0x18
00646293  74 0C                           je 0x1406462a1
00646295  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
0064629A  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0064629F  EB 0E                           jmp 0x1406462af
006462A1  A8 04                           test al, 4
006462A3  74 0A                           je 0x1406462af
006462A5  E8 5E D9 E8 FF                  call 0x1404d3c08
006462AA  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
006462AF  40 32 FF                        xor dil, dil
006462B2  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
006462B7  40 38 3D FA E5 8B 00            cmp byte ptr [rip + 0x8be5fa], dil
006462BE  75 0C                           jne 0x1406462cc
006462C0  F7 05 B6 E6 8B 00 00 08 00 00   test dword ptr [rip + 0x8be6b6], 0x800
006462CA  74 13                           je 0x1406462df
006462CC  48 8D 0D AD DB 8B 00            lea rcx, [rip + 0x8bdbad]
006462D3  E8 48 03 BD FF                  call 0x140216620
006462D8  40 8A F8                        mov dil, al
006462DB  84 C0                           test al, al
006462DD  74 39                           je 0x140646318
006462DF  4C 8D 76 20                     lea r14, [rsi + 0x20]
006462E3  49 8B 1E                        mov rbx, qword ptr [r14]
006462E6  EB 1A                           jmp 0x140646302
006462E8  48 8D 43 F0                     lea rax, [rbx - 0x10]
006462EC  48 85 C0                        test rax, rax
006462EF  74 0E                           je 0x1406462ff
006462F1  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006462F5  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
006462FA  E8 D1 47 07 00                  call 0x1406baad0
006462FF  48 8B 1B                        mov rbx, qword ptr [rbx]
00646302  49 3B DE                        cmp rbx, r14
00646305  75 E1                           jne 0x1406462e8
00646307  40 84 FF                        test dil, dil
0064630A  74 0C                           je 0x140646318
0064630C  48 8D 0D 6D DB 8B 00            lea rcx, [rip + 0x8bdb6d]
00646313  E8 68 3B D0 FF                  call 0x140349e80
00646318  48 8B CD                        mov rcx, rbp
0064631B  E8 30 76 06 00                  call 0x1406ad950
00646320  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00646324  48 85 F6                        test rsi, rsi
00646327  74 64                           je 0x14064638d
00646329  40 32 FF                        xor dil, dil
0064632C  40 38 3D 85 E5 8B 00            cmp byte ptr [rip + 0x8be585], dil
00646333  75 0C                           jne 0x140646341
00646335  F7 05 41 E6 8B 00 00 08 00 00   test dword ptr [rip + 0x8be641], 0x800
0064633F  74 13                           je 0x140646354
00646341  48 8D 0D 38 DB 8B 00            lea rcx, [rip + 0x8bdb38]
00646348  E8 D3 02 BD FF                  call 0x140216620
0064634D  40 8A F8                        mov dil, al
00646350  84 C0                           test al, al
00646352  74 39                           je 0x14064638d
00646354  48 83 C6 30                     add rsi, 0x30
00646358  48 8B 1E                        mov rbx, qword ptr [rsi]
0064635B  EB 1A                           jmp 0x140646377
0064635D  48 8D 43 F0                     lea rax, [rbx - 0x10]
00646361  48 85 C0                        test rax, rax
00646364  74 0E                           je 0x140646374
00646366  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0064636A  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0064636F  E8 5C 47 07 00                  call 0x1406baad0
00646374  48 8B 1B                        mov rbx, qword ptr [rbx]
00646377  48 3B DE                        cmp rbx, rsi
0064637A  75 E1                           jne 0x14064635d
0064637C  40 84 FF                        test dil, dil
0064637F  74 0C                           je 0x14064638d
00646381  48 8D 0D F8 DA 8B 00            lea rcx, [rip + 0x8bdaf8]
00646388  E8 F3 3A D0 FF                  call 0x140349e80
0064638D  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
00646391  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
00646396  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
0064639B  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
006463A0  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
006463A5  48 83 C4 40                     add rsp, 0x40
006463A9  41 5E                           pop r14
006463AB  C3                              ret
006463AC  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwQueryDefaultUILanguageWrapper(__int64 a1)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m18;
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
    result = DifGetAPIThunkContextById(result + 58, a2, a3, a4);
    if (result == 0) goto loc_00646318;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_006462A1;
    v_stack_m28 = v_stack_p0;
    goto loc_006462AF;
loc_006462A1:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    v_rdi = 0;
    v_stack_m20 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9168378)) != 0) goto loc_006462CC;
    if (((*(unsigned int *)(v_rip + 9168566)) & (0x800ULL)) == 0) goto loc_006462DF;
loc_006462CC:
    result = ExAcquireRundownProtection(v_rip + 9165741, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00646318;
loc_006462DF:
    goto loc_00646302;
loc_006462E8:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00646302:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_006462E8;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9165677;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ZwQueryDefaultUILanguage(a1, a2, a3, a4);
    v_stack_m18 = (unsigned int)(result);
    if (result == 0) goto loc_0064638D;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9168261)) != 0) goto loc_00646341;
    if (((*(unsigned int *)(v_rip + 9168449)) & (0x800ULL)) == 0) goto loc_00646354;
loc_00646341:
    result = ExAcquireRundownProtection(v_rip + 9165624, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0064638D;
loc_00646354:
    v_rsi = (result) + (48);
    goto loc_00646377;
loc_0064635D:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00646377:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0064635D;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9165560;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return (unsigned int)(v_stack_m18);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwQueryDefaultUILanguageWrapper(int64_t Arg1)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m18;
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
    result = DifGetAPIThunkContextById(result + 58, a2, a3, a4);
    if (result == 0) goto loc_00646318;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_006462A1;
    v_stack_m28 = v_stack_p0;
    goto loc_006462AF;
loc_006462A1:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    local_rdi = 0;
    v_stack_m20 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8BE5FA)) != 0) goto loc_006462CC;
    if (((*(uint32_t *)(v_rip + 0x8BE6B6)) & (0x800ULL)) == 0) goto loc_006462DF;
loc_006462CC:
    result = ExAcquireRundownProtection(v_rip + 9165741, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00646318;
loc_006462DF:
    goto loc_00646302;
loc_006462E8:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_00646302:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_006462E8;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9165677;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    result = ZwQueryDefaultUILanguage(Arg1, a2, a3, a4);
    v_stack_m18 = (uint32_t)(result);
    if (result == 0) goto loc_0064638D;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8BE585)) != 0) goto loc_00646341;
    if (((*(uint32_t *)(v_rip + 0x8BE641)) & (0x800ULL)) == 0) goto loc_00646354;
loc_00646341:
    result = ExAcquireRundownProtection(v_rip + 9165624, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0064638D;
loc_00646354:
    local_rsi = (result) + (48);
    goto loc_00646377;
loc_0064635D:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_00646377:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0064635D;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9165560;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return (uint32_t)(v_stack_m18);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00646250&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00646250[BB_00646250]
  bb_0064628E[BB_0064628E]
  bb_00646295[BB_00646295]
  bb_006462A1[BB_006462A1]
  bb_006462A5[BB_006462A5]
  bb_006462AF[BB_006462AF]
  bb_006462C0[BB_006462C0]
  bb_006462CC[BB_006462CC]
  bb_006462DF[BB_006462DF]
  bb_006462E8[BB_006462E8]
  bb_006462F1[BB_006462F1]
  bb_006462FF[BB_006462FF]
  bb_00646302[BB_00646302]
  bb_00646307[BB_00646307]
  bb_0064630C[BB_0064630C]
  bb_00646318[BB_00646318]
  bb_00646329[BB_00646329]
  bb_00646335[BB_00646335]
  bb_00646341[BB_00646341]
  bb_00646354[BB_00646354]
  bb_0064635D[BB_0064635D]
  bb_00646366[BB_00646366]
  bb_00646374[BB_00646374]
  bb_00646377[BB_00646377]
  bb_0064637C[BB_0064637C]
  bb_00646381[BB_00646381]
  bb_0064638D[BB_0064638D]
  bb_006463AC[BB_006463AC]
  bb_00646250 -->|branch| bb_00646318
  bb_00646250 -->|fallthrough| bb_0064628E
  bb_0064628E -->|branch| bb_006462A1
  bb_0064628E -->|fallthrough| bb_00646295
  bb_00646295 -->|branch| bb_006462AF
  bb_006462A1 -->|branch| bb_006462AF
  bb_006462A1 -->|fallthrough| bb_006462A5
  bb_006462A5 -->|flow| bb_006462AF
  bb_006462AF -->|branch| bb_006462CC
  bb_006462AF -->|fallthrough| bb_006462C0
  bb_006462C0 -->|branch| bb_006462DF
  bb_006462C0 -->|fallthrough| bb_006462CC
  bb_006462CC -->|branch| bb_00646318
  bb_006462CC -->|fallthrough| bb_006462DF
  bb_006462DF -->|branch| bb_00646302
  bb_006462E8 -->|branch| bb_006462FF
  bb_006462E8 -->|fallthrough| bb_006462F1
  bb_006462F1 -->|flow| bb_006462FF
  bb_006462FF -->|flow| bb_00646302
  bb_00646302 -->|branch| bb_006462E8
  bb_00646302 -->|fallthrough| bb_00646307
  bb_00646307 -->|branch| bb_00646318
  bb_00646307 -->|fallthrough| bb_0064630C
  bb_0064630C -->|flow| bb_00646318
  bb_00646318 -->|branch| bb_0064638D
  bb_00646318 -->|fallthrough| bb_00646329
  bb_00646329 -->|branch| bb_00646341
  bb_00646329 -->|fallthrough| bb_00646335
  bb_00646335 -->|branch| bb_00646354
  bb_00646335 -->|fallthrough| bb_00646341
  bb_00646341 -->|branch| bb_0064638D
  bb_00646341 -->|fallthrough| bb_00646354
  bb_00646354 -->|branch| bb_00646377
  bb_0064635D -->|branch| bb_00646374
  bb_0064635D -->|fallthrough| bb_00646366
  bb_00646366 -->|flow| bb_00646374
  bb_00646374 -->|flow| bb_00646377
  bb_00646377 -->|branch| bb_0064635D
  bb_00646377 -->|fallthrough| bb_0064637C
  bb_0064637C -->|branch| bb_0064638D
  bb_0064637C -->|fallthrough| bb_00646381
  bb_00646381 -->|flow| bb_0064638D
```
