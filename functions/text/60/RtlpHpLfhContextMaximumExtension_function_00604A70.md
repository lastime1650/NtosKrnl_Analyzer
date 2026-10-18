# RtlpHpLfhContextMaximumExtension

- RVA: `0x00604A70`–`0x00604AFD` (길이 `141` bytes)
- VA: `0x0000000140604A70`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00071750`
- 디코드: `40`개 명령, `141/141` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [RtlpHpHeapAllocate](RtlpHpHeapAllocate_function_00602D98.md) at `0x00602DBF`

### Static image references
- `0x00604A8A` → RVA `0x00F059A0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00604A70  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00604A75  B8 40 00 00 00                  mov eax, 0x40
00604A7A  BA 00 01 00 00                  mov edx, 0x100
00604A7F  3B C8                           cmp ecx, eax
00604A81  0F 46 C1                        cmovbe eax, ecx
00604A84  44 8B C0                        mov r8d, eax
00604A87  44 8B D0                        mov r10d, eax
00604A8A  8B 05 10 0F 90 00               mov eax, dword ptr [rip + 0x900f10]
00604A90  8B C8                           mov ecx, eax
00604A92  C1 E9 07                        shr ecx, 7
00604A95  83 E1 01                        and ecx, 1
00604A98  49 C1 E2 08                     shl r10, 8
00604A9C  44 8B D9                        mov r11d, ecx
00604A9F  49 C1 E3 06                     shl r11, 6
00604AA3  44 8B C9                        mov r9d, ecx
00604AA6  8D 59 01                        lea ebx, [rcx + 1]
00604AA9  B9 00 02 00 00                  mov ecx, 0x200
00604AAE  41 0F AF D8                     imul ebx, r8d
00604AB2  C1 E3 06                        shl ebx, 6
00604AB5  A8 04                           test al, 4
00604AB7  74 0E                           je 0x140604ac7
00604AB9  41 8D 51 01                     lea edx, [r9 + 1]
00604ABD  C1 E2 0D                        shl edx, 0xd
00604AC0  48 C1 EA 02                     shr rdx, 2
00604AC4  48 03 D1                        add rdx, rcx
00604AC7  41 C1 E0 04                     shl r8d, 4
00604ACB  49 8D 83 80 00 00 00            lea rax, [r11 + 0x80]
00604AD2  44 3B C1                        cmp r8d, ecx
00604AD5  41 0F 42 C8                     cmovb ecx, r8d
00604AD9  48 03 C3                        add rax, rbx
00604ADC  48 8B 5C 24 08                  mov rbx, qword ptr [rsp + 8]
00604AE1  48 0F AF CA                     imul rcx, rdx
00604AE5  48 C1 E0 07                     shl rax, 7
00604AE9  49 03 CA                        add rcx, r10
00604AEC  48 03 C1                        add rax, rcx
00604AEF  B9 C0 F8 3F 00                  mov ecx, 0x3ff8c0
00604AF4  48 3B C1                        cmp rax, rcx
00604AF7  48 0F 43 C1                     cmovae rax, rcx
00604AFB  C3                              ret
00604AFC  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpHpLfhContextMaximumExtension(int a1)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_rbx;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    result = 64;
    if (a1 <= 64) { result = a1; }
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9441040))))) >> (7));
    a1 = (unsigned int)((a1) & (1));
    v_r10 = ((unsigned int)((unsigned int)(result))) << (8);
    v_r11 = ((unsigned int)(a1)) << (6);
    v_rbx = (unsigned int)((a1 + 1) * ((unsigned int)((unsigned int)((unsigned int)(result)))));
    v_rbx = (unsigned int)((v_rbx) << (6));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 9441040)))) & (4)) != 0) {
        a2 = (unsigned int)(a1) + 1;
        a2 = (unsigned int)((a2) << (13));
        a2 = (a2) >> (2);
        a2 = (a2) + (512);
    }
    a3 = (unsigned int)(((unsigned int)((unsigned int)(result))) << (4));
    a1 = 512;
    if (((unsigned int)(a3)) < 512) { a1 = (unsigned int)(a3); }
    result = (v_r11 + 128) + (v_rbx);
    a1 = (a1) * (a2);
    result = (result) << (7);
    a1 = (a1) + (v_r10);
    result = (result) + (a1);
    if (result >= ((unsigned int)(0x3FF8C0ULL))) { result = (unsigned int)(0x3FF8C0ULL); }
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t RtlpHpLfhContextMaximumExtension(int32_t Arg1)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_rbx;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    result = 64;
    if (Arg1 <= 64) { result = Arg1; }
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x900F10))))) >> (7));
    Arg1 = (uint32_t)((Arg1) & (1));
    local_r10 = ((uint32_t)((uint32_t)(result))) << (8);
    local_r11 = ((uint32_t)(Arg1)) << (6);
    local_rbx = (uint32_t)((Arg1 + 1) * ((uint32_t)((uint32_t)((uint32_t)(result)))));
    local_rbx = (uint32_t)((local_rbx) << (6));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x900F10)))) & (4)) != 0) {
        a2 = (uint32_t)(Arg1) + 1;
        a2 = (uint32_t)((a2) << (13));
        a2 = (a2) >> (2);
        a2 = (a2) + (512);
    }
    a3 = (uint32_t)(((uint32_t)((uint32_t)(result))) << (4));
    Arg1 = 512;
    if (((uint32_t)(a3)) < 512) { Arg1 = (uint32_t)(a3); }
    result = (local_r11 + 128) + (local_rbx);
    Arg1 = (Arg1) * (a2);
    result = (result) << (7);
    Arg1 = (Arg1) + (local_r10);
    result = (result) + (Arg1);
    if (result >= ((uint32_t)(0x3FF8C0ULL))) { result = (uint32_t)(0x3FF8C0ULL); }
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00604A70&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00604A70[BB_00604A70]
  bb_00604AB9[BB_00604AB9]
  bb_00604AC7[BB_00604AC7]
  bb_00604AFC[BB_00604AFC]
  bb_00604A70 -->|branch| bb_00604AC7
  bb_00604A70 -->|fallthrough| bb_00604AB9
  bb_00604AB9 -->|flow| bb_00604AC7
```
